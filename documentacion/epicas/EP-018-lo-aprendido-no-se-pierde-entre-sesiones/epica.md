# EP-018 — Lo aprendido no se pierde entre sesiones

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-018 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Memoria |
| **Versión del producto** | 4, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-023`, `F-024` |
| **Estado** | Terminada el 2026-09-01: sus dos historias cumplen |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que lo que una sesión aprende llegue a la siguiente, y que el usuario pueda verlo, corregirlo y darlo de baja.

## 3. Problema y oportunidad

**Es la mitad del problema que originó todo esto.** Lo dice la ficha de `F-023` con esas palabras: *«sin esto, cada sesión vuelve a empezar»*. El chat se borra, y con él se va la corrección que ya se había hecho una vez. Y dos veces. Y tres.

La otra mitad ya está resuelta: la transcripción vive en `historico-chat/`, y la escribe un enganche del programa. Lo que faltaba es **lo que quedó**, separado de lo que se dijo.

**Y hay un segundo problema, que es de confianza.** La ficha de `F-024` lo dice: *«hoy solo el agente ve lo que recuerda»*. Los recuerdos son archivos del repositorio —`01·C19` lo manda—, pero no hay forma de consultarlos ni de corregirlos sin abrirlos a mano. Un recuerdo equivocado sigue rigiendo hasta que alguien lo encuentra.

## 4. Objetivo y propuesta de valor

Que la memoria del agente sea **visible y corregible por el usuario**.

**Beneficios esperados:**

- Que la corrección hecha una vez no haya que hacerla otra.
- Que el usuario vea qué recuerda el agente, y lo pueda cambiar.
- Que lo que dejó de ser cierto se marque, sin perder qué se creía antes.

## 5. Alcance

**Dentro:**

- Guardar un recuerdo, y devolverlo después (`F-023`).
- Listar, buscar, corregir y dar de baja (`F-024`).

**Fuera:**

- **Decidir qué merece recordarse.** Eso lo decide quien escribe.
- Revisar solo si un recuerdo sigue siendo cierto. Nada lo revisa, y queda declarado.
- La pantalla.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-023` Guardar lo aprendido y devolverlo después | El recuerdo escrito donde no se borra | 4 |
| `F-024` Consultar y corregir lo guardado | Ver, buscar, corregir y dar de baja | 4 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El agente | Escribe lo que la sesión dejó, y al abrir recibe lo vigente |
| El usuario | Consulta, corrige y da de baja |
| El módulo Auditoría | Guarda que se escribió, se corrigió o se dio de baja |

## 7. Criterios de aceptación de la épica

- Lo guardado en una sesión **se recupera en la siguiente**.
- Lo de un proyecto **no se mezcla** con el de otro.
- Si no hay nada del tema, **se dice** en vez de inventar.
- **Guardar no pisa** lo que ya está.
- Corregir **deja constancia de qué decía antes**.
- Dar de baja **no borra**: lo saca de lo que se le entrega al agente.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Recuerdos perdidos al guardar uno nuevo | **Cero** |
| Correcciones que borran lo anterior | **Cero** |
| Recuerdos borrados | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-guardar-lo-aprendido/HU-001-guardar-lo-aprendido.md) | Guardar lo aprendido | `F-023` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-consultar-y-corregir-lo-guardado/HU-002-consultar-y-corregir-lo-guardado.md) | Consultar y corregir lo guardado | `F-024` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Módulo nuevo:** Memoria, con [especificación](../../memoria/spec.md) aprobada el 2026-09-01.

**Sin entidad en la base, y eso es una decisión.** El módulo lee y escribe los archivos que ya existen en `historico-chat/memory/`, porque `DA-01` manda que el texto sea la verdad y acá **todo lo que responde está en el texto**: un recuerdo dado de baja se reconoce por su marca, uno corregido por lo que quedó escrito debajo.

**Es el caso simétrico de [EP-017](../EP-017-una-aprobacion-dice-sobre-que-texto/epica.md).** Allá el hecho ocurrió fuera del texto —el texto no sabe quién lo aprobó— y por eso sí se guarda. Acá el hecho **es** el texto.

## 11. Dependencias

Depende de `F-001`, el almacén, y de que exista `historico-chat/memory/`, que existe desde que lo pidió `01·C19`.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que guardar pise un recuerdo existente** | No pisa: si el nombre está, avisa |
| Que corregir borre lo que se creía antes | Lo anterior queda debajo, marcado |
| Que dar de baja borre el archivo | Solo le pone la marca |
| Que un recuerdo equivocado siga rigiendo | **Se acepta y se declara:** nada lo revisa solo |

## 13. Supuestos y restricciones

**Supuestos:** los recuerdos son archivos de texto, uno por recuerdo, con su línea en el índice.

**Restricciones:** el almacén de Claude Code queda vacío (`01·C19`); nada se borra; quien decide qué recordar es quien escribe.

## 14. Hoja de ruta

Versión 4, después de `EP-017`.

## 15. Definition of Ready

- ☑ Las dos funcionalidades están en el inventario, con su ficha.
- ☑ La carpeta `historico-chat/memory/` existe y tiene recuerdos.
- ☑ El módulo Memoria, con [especificación](../../memoria/spec.md) aprobada.

## 16. Definition of Done

- ☑ Las dos historias cerradas, con veredicto por criterio.
- ☑ Comprobado que guardar no pisa.
- ☑ Comprobado que corregir conserva lo anterior.
- ☑ Comprobado que dar de baja no borra.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Terminada**: las dos historias construidas y probadas el mismo día |
| 2026-09-01 | Nace del inventario aprobado, para cubrir las dos funcionalidades de Memoria |
