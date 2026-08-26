# Funcionalidad implementada — Fase A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos (módulo Instalación)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los seis enganches quedan registrados en nueve momentos, no se duplican al reinstalar, y **ninguno detiene la sesión** cuando no encuentra nada que hacer.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) y los seis `hook_*.py` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-004: CA-01, CA-02 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase levantó la tabla que faltaba y probó lo que nadie había probado.** Los seis enganches se instalan desde hace versiones; lo que no existía era el documento que dijera **cuándo corre cada uno y qué pasa si falla**, ni una prueba de que ninguno tumbe la sesión.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Registrar los seis en sus momentos | programa | [`instalar.py`](../../../../../validadores/instalar.py) · `instalar_claude` | ✅ Ya existía | CP-001 |
| No duplicarlos al reinstalar | programa | El mismo | ✅ Ya existía | CP-004 |
| Que ninguno detenga la sesión | programa | Cada `hook_*.py` termina en 0 | ✅ Ya existía | CP-003 |
| **La tabla de los seis, con su momento y su fallo** | documentación | §2 del [resultado_pruebas.md](resultado_pruebas.md) | ✅ **Escrita acá** | — |
| Las cuatro exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `GenerarLosAutomatismos` | ✅ Escritas acá | 4 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Seis enganches, nueve registros, y los cuatro probados terminan en 0 sobre una carpeta vacía | ✅ |
| CA-02 | Dos instalaciones dejan los ajustes idénticos | ✅ |
| Transversal · Límites | El enganche corre contra un proyecto sin nada y no revienta | ✅ |
| Transversal · Compatibilidad | La ruta generada funciona con espacios | ✅ |

---

## 3. La tabla que faltaba

| Enganche | Cuándo corre | Si falla |
|---|---|---|
| `hook_sesion.py` | Al abrir la sesión | La sesión abre sin las reglas puestas |
| `hook_recuerdos.py` | Al abrir · al escribir un archivo | Quedan dos copias del mismo recuerdo |
| `hook_resumen.py` | Al abrir · en cada mensaje | El resumen no nace solo |
| `hook_historico.py` | En cada mensaje · al terminar la respuesta | **Se pierde la sesión** |
| `hook_checklist.py` | En cada mensaje | Nadie se entera de una instalación incompleta |
| `hook_md.py` | Al escribir un archivo | El documento mal formado pasa sin aviso |

**La cuarta fila es la única cuyo fallo destruye.** Los otros cinco dejan de ayudar; `hook_historico.py` pierde información que no se puede reponer, porque el chat se borra y el repositorio no la tiene. Saber eso cambia qué se vigila primero.

---

## 4. Lo que este caso ya destapó, esta misma sesión

Al escribir la prueba de que ningún enganche revienta apareció que **`hook_resumen.py` era el único de los seis que no preparaba su salida**. Su texto lleva acentos, así que salía en la página de códigos de la consola, y con la salida en una tubería no se podía ni decodificar.

Se corrigió en la **23.2.1**, y nació la prueba que recorre los seis para que la lista no vuelva a quedar coja cuando nazca el séptimo. Es el [pendiente 45](../../../../../pendientes/hecho/instalar-prepara-su-propia-salida.md) otra vez, en otro archivo.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| Los enganches se prueban contra una **carpeta vacía**, que es donde revientan: con todo instalado, un enganche frágil pasa igual | CP-003 del [resultado](resultado_pruebas.md) |
| La tabla dice **qué pasa si falla**, no solo qué hace: es lo que permite decidir cuál vigilar primero | §3 de este documento |
| No se desinstala nada para probar: el escenario se arma con una carpeta nueva | CP-003 |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el fallo de un enganche quede **dicho**, y no solo no detenga | Sin destino. Hoy termina en 0 y calla |
| Los automatismos que no dependen de la memoria | [EP-005](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md) |
| Mostrar antes de hacer | [HU-002](../../HU-002-mostrar-antes-de-hacer/HU-002-mostrar-antes-de-hacer.md) |

**Lo que deja esta fase:** los seis enganches son seguros —ninguno tumba la sesión— y esa seguridad tiene un costo que conviene saber: **cuando fallan, callan**. Un `hook_historico.py` que deje de escribir no avisa a nadie, y lo que se pierde no vuelve.
