# EP-017 — Una aprobación dice sobre qué texto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-017 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Aprobaciones |
| **Versión del producto** | 4, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-015`, `F-016`, `F-017` |
| **Estado** | Terminada el 2026-09-01: sus tres historias cumplen |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que «este documento está aprobado» quiera decir algo: que se sepa quién lo aprobó, cuándo, y **sobre qué texto exacto**.

## 3. Problema y oportunidad

**Situación actual, medida el 2026-09-01.** Las aprobaciones se escriben a mano dentro de los documentos: **21 documentos** de este repositorio traen una línea del estilo de `| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ |`.

**Esa línea no dice sobre qué texto se aprobó.** El documento pudo cambiar tres veces desde entonces y la marca sigue ahí igual. La ficha de `F-015` lo dice sin rodeos: *«es la pieza que hoy no existe, y de la que se sostiene todo el gobierno»*.

**Y el daño no es teórico.** La ficha de `F-017` cuenta el caso que la originó: **se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor.** Nada avisó.

## 4. Objetivo y propuesta de valor

Que una aprobación responda la única pregunta que importa: **¿lo aprobado sigue siendo lo que hay?**

**Beneficios esperados:**

- Saber sobre qué texto se aprobó, no solo que se aprobó.
- Que editar un documento aprobado le quite la aprobación, y se diga.
- Que la historia de lo autorizado no se pierda.

## 5. Alcance

**Dentro:**

- Registrar la aprobación con su huella (`F-015`).
- Mostrar el estado de cada documento, **con palabras** (`F-016`).
- Caducar la aprobación cuando el texto cambia (`F-017`).

**Fuera:**

- **Decidir si algo merece aprobarse.** La plataforma registra; quien aprueba es una persona.
- **Migrar las 21 marcas escritas a mano.** Cada una diría que se aprobó un texto que hoy no se puede reconstruir.
- Comprobar la identidad de quien aprueba.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-015` Registrar una aprobación con su firma | Quién, cuándo y sobre qué texto | 4 |
| `F-016` Ver qué está aprobado y qué está en borrador | El estado, dicho con palabras | 4 |
| `F-017` Caducar la aprobación cuando el texto cambia | El aviso, y qué cambió | 4 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Aprueba, y decide qué hacer cuando algo caduca |
| El agente | Consulta el estado antes de construir sobre un documento |
| El módulo Auditoría | Guarda que se aprobó, quién y cuándo |

## 7. Criterios de aceptación de la épica

- Una aprobación guarda **sobre qué texto** se dio.
- **No se aprueba un documento que no existe.**
- Editar un documento aprobado le quita la aprobación, y se dice cuánto cambió.
- **La aprobación anterior no se borra.**
- Los tres estados se dicen **con palabras**, no con color.
- Un documento sin aprobación aparece así, no vacío.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Aprobaciones sin huella del texto | **Cero** |
| Documentos aprobados que cambiaron sin avisar | **Cero** |
| Aprobaciones borradas | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-registrar-una-aprobacion-con-su-firma/HU-001-registrar-una-aprobacion-con-su-firma.md) | Registrar una aprobación con su firma | `F-015` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-ver-que-esta-aprobado-y-que-no/HU-002-ver-que-esta-aprobado-y-que-no.md) | Ver qué está aprobado y qué no | `F-016` | **Terminada el 2026-09-01** |
| [HU-003](HU-003-caducar-la-aprobacion-cuando-el-texto-cambia/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md) | Caducar la aprobación cuando el texto cambia | `F-017` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Módulo nuevo:** Aprobaciones, con [especificación](../../aprobaciones/spec.md) aprobada el 2026-09-01.

**Es el segundo módulo de la plataforma con una entidad propia.** Los demás calculan al pedir, porque su respuesta está en el texto. Esta no: **el texto no sabe quién lo aprobó**. Aprobar es un hecho que ocurrió, y si no queda escrito no ocurrió para nadie más.

## 11. Dependencias

Depende de `EP-009`, la auditoría, donde queda registrado que se aprobó.

**La ficha de `F-015` dice depender de `F-014`, y no la bloquea:** lo que necesita es que haya documentos, y los hay.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que «aprobado» siga sin decir sobre qué** | La huella va siempre, y sin ella no se guarda |
| Que caducar borre la historia | Nada se borra: la anterior se queda |
| Que el estado se comunique solo con color | Los tres estados tienen su frase |

## 13. Supuestos y restricciones

**Supuestos:** que el documento vive en el proyecto y se puede leer.

**Restricciones:** la aprobación es un hecho, no una opinión de la plataforma; nada se borra; quien aprueba es una persona.

## 14. Hoja de ruta

Versión 4. Va primero de esa versión: es de lo que se sostiene el resto del gobierno.

## 15. Definition of Ready

- ☑ Las tres funcionalidades están en el inventario, con su ficha.
- ☑ Medidas las 21 marcas escritas a mano.
- ☑ El módulo Aprobaciones, con [especificación](../../aprobaciones/spec.md) aprobada.

## 16. Definition of Done

- ☑ Las tres historias cerradas, con veredicto por criterio.
- ☑ Comprobado que editar quita la aprobación.
- ☑ Comprobado que la anterior no se borra.
- ☑ Comprobado que un documento sin aprobación aparece así.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Terminada**: las tres historias construidas y probadas el mismo día |
| 2026-09-01 | Nace del inventario aprobado, para cubrir las tres funcionalidades de Aprobaciones |
