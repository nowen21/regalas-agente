# Especificación del módulo Memoria  ·  `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Módulo** | Memoria |
| **Funcionalidades que cubre** | [`F-023`](../../cvds/analisis-requisitos/inventario-funcionalidades.md) guardar lo aprendido y devolverlo después · [`F-024`](../../cvds/analisis-requisitos/inventario-funcionalidades.md) consultar y corregir lo guardado |
| **Épica** | [EP-018](../epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/epica.md) |
| **Estado** | Aprobada el 2026-09-01 |
| **Versión del estándar** | 37.2.1 |

---

## 1. Propósito y alcance

**Que lo aprendido en una sesión llegue a la siguiente, y que el usuario pueda verlo y corregirlo.**

Es la mitad del problema que originó todo esto: el chat se borra, y con él se va la corrección que ya se había hecho. La otra mitad —la transcripción— la resuelve el histórico. Acá va **lo que quedó**, no lo que se dijo.

**Entra:** guardar un recuerdo, listar, buscar, corregir y dar de baja.

**No entra:** decidir qué merece recordarse. Eso lo decide quien escribe.

---

## 2. Contexto — qué hay hoy

Los recuerdos ya viven en [`historico-chat/memory/`](../../historico-chat/memory/memory.md): **un archivo por recuerdo, con su línea en el índice**. Lo manda `01·C19`, y por una razón que vale repetir: **la memoria del agente es un archivo del repositorio, no un ajuste de la herramienta.** El almacén de Claude Code queda vacío.

Lo que no hay es forma de consultarlos ni de corregirlos sin abrir los archivos a mano. **Hoy solo el agente ve lo que recuerda**, y esa es la queja escrita en la ficha de `F-024`: es un problema de confianza antes que de comodidad.

---

## 3. Supuestos, dependencias y preguntas abiertas

| # | Qué | Tipo |
|---|---|---|
| 1 | Los recuerdos son archivos de texto en `historico-chat/memory/` | Supuesto, y es la regla `01·C19` |
| 2 | El índice `memory.md` lleva una línea por recuerdo | Supuesto |
| 3 | Quien escribe decide qué merece recordarse | Fuera de alcance |
| 4 | Un recuerdo puede dejar de ser cierto sin que nadie lo note | **Pregunta abierta:** nada lo revisa |

---

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| `RN-1` | Un recuerdo vive donde no se borra: un archivo del repositorio |
| `RN-2` | Guardar no pisa lo que ya está: si el nombre existe, se avisa |
| `RN-3` | Corregir **conserva lo que decía antes**, debajo y marcado |
| `RN-4` | Dar de baja **no borra**: marca el recuerdo y lo deja fuera de lo que se le entrega al agente |
| `RN-5` | Buscar sin coincidencias **lo dice**, no devuelve vacío |
| `RN-6` | Ningún recuerdo guarda credenciales |

---

## 5. Modelo de datos

**Ninguna entidad.** El módulo lee y escribe los archivos que ya existen: `DA-01`, el texto es la verdad.

| Elemento | Dónde |
|---|---|
| La carpeta | `historico-chat/memory/` |
| El índice | `memory.md` |
| Un recuerdo | Un `.md` con su título y su cuerpo |
| La marca de baja | La línea `> **Ya no vale.**` al principio del cuerpo |
| Lo que decía antes | Debajo de la corrección, con su encabezado |

### 5.1 Por qué no hay tabla

Porque todo lo que el módulo responde **está en el texto**. Un recuerdo dado de baja se reconoce por su marca; uno corregido, por lo que quedó escrito debajo. Guardar eso en una base sería tener dos verdades y elegir la peor.

Es lo contrario de [Aprobaciones](../aprobaciones/spec.md), y por el motivo simétrico: allá el hecho ocurrió fuera del texto.

---

## 6. Comportamiento y flujos

| Flujo | Qué hace |
|---|---|
| **Listar** | Todos los recuerdos, o solo los vigentes |
| **Buscar** | Por palabra, en el título y en el cuerpo |
| **Guardar** | Escribe el archivo y le pone su línea al índice. Si ya existe, **no pisa**: avisa |
| **Corregir** | Cambia el cuerpo y **deja debajo lo que decía antes** |
| **Dar de baja** | Le pone la marca. El archivo queda |
| **Resumen** | Cuántos hay, cuántos vigentes, cuántos de baja |

---

## 7. Interfaz

**La memoria** (`P-07`, en `/proyecto/<id>/memoria/`): qué recuerda el agente sobre este proyecto, con lo dado de baja incluido. Es la mitad que faltaba del problema de la ficha de `F-024` —*hoy solo el agente ve lo que recuerda*—: la de mirar.

**Lo dado de baja también sale**, en gris. Esconderlo dejaría al usuario sin saber que existió, y lo que ya no vale sigue siendo la respuesta a por qué algo se hizo como se hizo.

Corregir y dar de baja siguen por consola: son cambios de estado.

---

## 8. Permisos y autorización

La misma confianza del resto: quien corre la orden es el usuario en su máquina.

---

## 9. Marco normativo

`01·C19` (la memoria es un archivo del repositorio) · `03·DA-01` (el texto es la verdad) · el capítulo `15` (nada se borra) · `13·DOC22` (lo que la sesión deja se escribe cuando aparece).

---

## 10. Plan de pruebas

| Qué | Cuántas |
|---|---|
| Listar, buscar y resumir | 6 |
| Guardar sin pisar | 4 |
| Corregir conservando | 3 |
| Dar de baja sin borrar | 3 |
| **Total** | **16** |

---

## 11. Criterios de aceptación

| ID | Criterio | Estado |
|---|---|---|
| CA-01 | Lo guardado en una sesión se recupera en la siguiente | ☑ |
| CA-02 | Lo de un proyecto no se mezcla con el de otro | ☑ |
| CA-03 | Si no hay nada del tema, **se dice** en vez de inventar | ☑ |
| CA-04 | Se busca por palabra | ☑ |
| CA-05 | Corregir deja constancia de qué decía antes | ☑ |
| CA-06 | Dar de baja no borra: lo deja fuera de lo que se entrega | ☑ |

---

## 12. Decisiones tomadas

| Decisión | Por qué |
|---|---|
| **Sin entidad en la base** | Todo lo que responde está en el texto |
| **Guardar no pisa** | Perder un recuerdo por reusar un nombre es el peor fallo posible acá |
| **Corregir conserva lo anterior** | Un recuerdo corregido cuenta dos cosas: lo que vale hoy y lo que se creía ayer |
| **Dar de baja marca, no borra** | Es la misma razón por la que las reglas se derogan (`20·M11`) |
| **Buscar sin resultados lo dice** | Un vacío se ve igual que una falla — `S-110` |

---

## 13. Trazabilidad

| Funcionalidad | Requisito | Fase | Estado |
|---|---|---|---|
| F-023 | RF-23 | [P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente](../epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-001-guardar-lo-aprendido/P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente/estado-fase.md) | Cerrada el 2026-09-01 |
| F-024 | RF-24 | [Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes](../epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-002-consultar-y-corregir-lo-guardado/Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes/estado-fase.md) | Cerrada el 2026-09-01 |

---

## 14. Cruces con otros módulos

| Módulo | Cómo se cruzan |
|---|---|
| [Seguridad](../seguridad/spec.md) | `RN-6`: ningún recuerdo guarda credenciales |
| [Auditoría](../auditoria/spec.md) | Guardar, corregir y dar de baja quedan registrados |
| [Aprobaciones](../aprobaciones/spec.md) | El caso simétrico: allá el hecho ocurrió fuera del texto, y por eso sí se guarda |

---

## 15. Cambios después de aprobada

Ninguno todavía.
