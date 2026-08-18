# Funcionalidad implementada — Fase A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3 (módulo Documentos modelo)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los tres modelos existen, no se pisan, ninguno pide credenciales, y **lo no declarado no genera exigencia** — que es lo correcto, aunque suene a laxitud.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-005-retrodocumentar-los-modelos-de-la-capa-3` |
| **Módulo** | Documentos modelo — [`plantillas/stack.md`](../../../../../plantillas/stack.md), [`dominio.md`](../../../../../plantillas/dominio.md), [`mapeo-nombres.md`](../../../../../plantillas/mapeo-nombres.md) |
| **Especificación del módulo** | [`documentacion/documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md), §4.3 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-005: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió las cuatro reglas de la capa 3 y probó la que más se puede malinterpretar.** Los tres modelos existen desde el principio. Lo que faltaba era decir por escrito **qué pasa con lo que el proyecto no declara**.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-18 · son tres, y los llena el proyecto | documentación | `plantillas/stack.md`, `dominio.md`, `mapeo-nombres.md` | ✅ Ya existían | CP-001 |
| RN-19 · lo no declarado no se comprueba | programa | Los validadores que leen la capa 3 | ✅ Ya existía | CP-003 |
| RN-20 · ninguno pide credenciales | documentación | Los tres modelos | ✅ Ya existía | Transversal |
| RN-21 · llegan con sus marcas puestas | documentación | Los tres | ✅ Ya existía | Transversal |
| Que no se pisen al reinstalar | programa | [`instalar.py`](../../../../../validadores/instalar.py) | ✅ Ya existía | Fase hermana |
| Las cuatro reglas, escritas | documentación | [`documentos-modelo/spec.md`](../../../../documentos-modelo/spec.md) §4.3 | ✅ **Escrito acá** | — |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ModelosDeLaCapaDeProyecto` | ✅ Escritas acá | 3 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Los tres existen y conservan lo que la persona escriba | ✅ |
| CA-02 | Lo que un programa lee está marcado; el resto es prosa libre | ✅ |
| CA-03 | Sin convención declarada no hay hallazgos de nomenclatura | ✅ |
| Transversal · Límites | Llegan con sus marcas `«…»`, que dicen que no están terminados | ✅ |
| Transversal · Privacidad | **Ninguno pide credenciales ni datos personales** | ✅ |

---

## 3. La regla que más se puede malinterpretar

**«Lo no declarado no se comprueba»** suena a laxitud y es lo contrario.

Exigir contra una convención que nadie escribió sería **inventarla**: el validador impondría un criterio que el proyecto nunca aceptó, y el proyecto aprendería a ignorar sus hallazgos. Eso no se queda en los hallazgos falsos — se contagia a los ciertos, que es el daño que el [pendiente 55](../../../../../pendientes/55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) ya describe para otro caso.

**Y no queda impune:** no declarar la convención sale como **instalación incompleta** en el checklist. No se castiga con hallazgos falsos; se cuenta como algo que falta.

---

## 4. La privacidad, que nadie había comprobado

Un modelo que pidiera una contraseña la convertiría en **un archivo versionado en cada proyecto que lo llene**. Se comprobó buscando en los tres las palabras de credencial como dato por llenar: **ninguno las pide**.

Es el transversal que el plan de pruebas no cubría, y era barato de comprobar y caro de descubrir tarde.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| Que los modelos lleguen **con sus marcas puestas** es correcto: es lo que dice que no están terminados (`13·DOC20`). Uno sin marcas parecería lleno | Transversal de límites del [resultado](resultado_pruebas.md) |
| «Lo no declarado no se comprueba» se escribe **con su porqué**, porque sin él se lee como un hueco | §4.3 de la especificación |
| La privacidad se comprueba buscando las palabras en los tres, no leyéndolos por encima | Verificación 2 del resultado |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| El modelo del marco normativo | [HU-004](../../HU-004-modelo-de-la-especificacion/HU-004-modelo-de-la-especificacion.md), ya cerrada |
| Que no se pisen al actualizar | [EP-007 · HU-005](../../../EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) |

**Lo que deja esta fase:** la capa 3 es donde el estándar deja de mandar y el proyecto empieza a decidir. La regla que lo hace funcionar —no exigir contra lo que nadie declaró— llevaba años aplicándose y no estaba escrita en ninguna parte.
