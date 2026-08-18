# Funcionalidad implementada — Fase A-EP-004-HU-018-el-numero-de-pendiente-libre (módulo Comprobación automática)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Nace `validadores/pendientes.py` con su subcomando. Y al construirlo apareció lo que la HU no preveía: **al cerrarse, un pendiente pierde su número**, así que la carpeta sola no sabe cuáles están tomados.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-018-el-numero-de-pendiente-libre` |
| **Módulo** | Comprobación automática — [`validadores/pendientes.py`](../../../../../validadores/pendientes.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-018: CA-01, CA-02, CA-03 y sus tres transversales |
| **Fecha de cierre** | 2026-08-17 · **Versión** 23.3.0 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nace un validador.** `python validadores/validar.py pendientes` dice si hay números repetidos, si la carpeta y el índice cuadran, y **cuál es el próximo número libre** — que es la pregunta que se hace quien va a abrir un pendiente.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Decir el próximo número libre | programa | [`pendientes.py`](../../../../../validadores/pendientes.py) · `proximo_libre()` | ✅ **Construido acá** | CP-001 |
| Avisar del número repetido | programa | El mismo · `validar()` | ✅ **Construido acá** | CP-002 |
| Cruzar la carpeta con el índice | programa | El mismo | ✅ **Construido acá** | CP-003 |
| **Leer también los números que solo viven en el índice** | programa | El mismo · `numeros_del_indice()` | ✅ **Construido acá** | El hallazgo |
| Su punto de entrada | programa | [`validar.py`](../../../../../validadores/validar.py) · `cmd_pendientes` | ✅ **Construido acá** | CP-001 |
| Qué mira y qué no | documentación | [`docs/pendientes.md`](../../../../../validadores/docs/pendientes.md) | ✅ Escrito acá | — |
| Las seis exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `NumeracionDePendientes` | ✅ Escritas acá | 14 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Dice el próximo libre, y no entrega huecos | ✅ |
| CA-02 | Falla con el repetido, incluidos los ceros a la izquierda | ✅ |
| CA-03 | Los dos sentidos, como aviso | ✅ |
| Transversal · Límites | Carpeta vacía, archivo sin número, ceros a la izquierda | ✅ |
| Transversal · Errores | El nombre no interpretable avisa y la corrida sigue | ✅ |
| Transversal · No regresión | `validar.py estandar` da lo mismo | ✅ |

---

## 3. El hallazgo, que cambió el diseño antes de cerrar

**La primera versión leía solo la carpeta y dijo que el próximo libre era el 02.**

El 02 existió: era «vigencia y poda de la memoria», cerrado el 2026-08-06. Al cerrarse, su archivo se movió a `hecho/` **y se renombró** — perdió el número. Mirando los archivos, el 02 parece libre.

**Dónde sobrevive la numeración:** solo en el índice, en su fila tachada `| ~~02~~ |`. El programa quedó leyendo **la carpeta y el índice juntos**.

| Medición, 2026-08-17 | Valor |
|---|---:|
| Pendientes con archivo | **39** |
| Números tomados de verdad | **54** |
| Números que existen **solo** en el índice | **15** |
| Próximo libre | **59** |

**Si la fase hubiera cerrado con la primera versión**, el siguiente pendiente habría nacido con el 02 y habría roto en silencio toda cita al 02 anterior — que es exactamente el daño que esta HU viene a evitar. Un validador equivocado habría sido peor que ninguno, porque se le habría creído.

**Lo destapó el caso del paso 3 de CP-001**, que el plan de pruebas sí había escrito.

---

## 4. Decisiones y señales

| Decisión | La alternativa | Por qué esta |
|---|---|---|
| El próximo libre es **el siguiente al mayor**, no el primer hueco | Reutilizar huecos | Los pendientes se citan por número. Entregar un hueco haría que «el 02» apuntara a dos cosas según cuándo se leyera |
| Los números se leen de **la carpeta y el índice** | Solo la carpeta | Cerrar un pendiente le quita el número al archivo; el índice es la única memoria completa |
| El repetido es **falla**; el descuadre con el índice, **aviso** | Todo falla | El repetido no se resuelve leyendo: los dos archivos existen y ninguno pisa al otro. El descuadre se arregla editando un `.md` |
| `pendientes.py` **no usa `comun.leer`** | Usarlo | Hoy revienta con el archivo ausente, y esto tiene que correr sobre una carpeta que aún no tiene índice. El motivo está escrito en el código, con el defecto al que apunta |

---

## 5. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que `comun.leer` tolere el archivo ausente o ilegible | `D-01` de la fase [`A-EP-004-HU-003`](../../HU-003-formato-del-hallazgo/A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md) |
| Que cerrar un pendiente **conserve** su número en el nombre del archivo | Sin destino. Hoy se resuelve leyendo el índice; conservarlo lo haría innecesario. Relacionado con el [pendiente 54](../../../../../pendientes/54-cerrar-un-pendiente-rompe-sus-citas.md) |
| Contar las HU sin fase | [HU-017](../../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) |

**Lo que deja esta fase:** la carpeta de pendientes parecía la fuente de la numeración y no lo es. Quince de sus cincuenta y cuatro números no están en ningún nombre de archivo — solo en una fila tachada del índice que nadie estaba obligado a mantener.
