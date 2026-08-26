# Funcionalidad implementada — Fase A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo (módulo Comprobación automática)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los tres criterios numerados quedaron verificados sobre una corrida real y el contrato que faltaba está escrito. Falla el **transversal de errores**: un `.md` que no se puede decodificar **tumba la corrida entera** y se lleva todos los hallazgos ya encontrados.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` |
| **Módulo** | Comprobación automática — [`validadores/comun.py`](../../../../../validadores/comun.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-003: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Se escribió el contrato de la salida, que estaba en el código y en ningún documento.** Qué trae un hallazgo y qué hace cada severidad se deducía leyendo `comun.py`; ahora está en [`validadores/docs/comun.md`](../../../../../validadores/docs/comun.md), probado contra una corrida real de 207 hallazgos.

Y al escribir el caso del transversal que el plan no cubría, apareció el defecto.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| El hallazgo trae archivo, línea y regla | programa | [`comun.py`](../../../../../validadores/comun.py) · `Hallazgo` | ✅ Ya existía | CP-001 |
| El de archivo entero deja la línea en 0 | programa | `Hallazgo.__str__` omite el número | ✅ Ya existía | CP-001 |
| El aviso no detiene; la falla sí | programa | `comun.reportar` | ✅ Ya existía | CP-003, CP-004 |
| **El contrato, escrito** | documentación | [`docs/comun.md`](../../../../../validadores/docs/comun.md) | ✅ **Escrito acá** | — |
| **Que el archivo ilegible no tumbe la corrida** | programa | `comun.leer` abre sin red | ❌ **No existe** | CP transversal |
| Las cinco exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `FormatoDelHallazgo` | ✅ Escritas acá | 8 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | 207 de 207 con archivo y regla; dos defectos reales arreglados sin abrir el validador | ✅ |
| CA-02 | 151 avisos y código 0, por el camino real | ✅ |
| CA-03 | Basta una falla entre avisos para terminar en 1 | ✅ |
| Transversal · Límites | El hallazgo de archivo entero tiene forma definida: `linea = 0` | ✅ |
| Transversal · Errores | **El archivo ilegible revienta la corrida con un volcado de Python** | ❌ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17, sobre una corrida real | Valor |
|---|---|
| Hallazgos producidos por `flujo`, `fases` y `trazabilidad` | **207** |
| Con archivo | **207** |
| Con la regla nombrada | **207** |
| Con línea concreta | 122 |
| De archivo entero, con `linea = 0` | **85** |
| Veces que hizo falta abrir el programa para arreglar un defecto | **0** |

**La última fila es la que prueba el CA-01**, y no se probó con un ejemplo: se probó **arreglando dos defectos reales** de esta misma sesión leyendo solo la salida del validador. En la misma tanda se arreglaron cinco y `validar.py estandar` pasó de 5 fallas a 0.

---

## 4. El defecto que apareció por probar lo que el plan no cubría

`comun.leer` abre el archivo sin red. Un `.md` que no sea UTF-8 lanza `UnicodeDecodeError`, la excepción sube hasta arriba y **la corrida entera termina en 1 sin una sola línea de salida útil** — perdiendo todos los hallazgos que ya había encontrado.

Se comprobó de verdad: `validar.py estandar` sobre un árbol con un archivo mal codificado devuelve una traza de Python y nada más.

**Es el peor momento posible para caerse:** cuando ya hay trabajo hecho que reportar. Y es exactamente lo que el transversal de errores de la HU prohíbe — «un mensaje entendible, no un volcado técnico».

**No se arregló acá:** `comun.py` no está en los archivos que §2.1 del plan declara. Queda con su prueba en rojo esperado.

> **Nadie lo habría encontrado.** Es el transversal al que el plan no le escribió caso — el mismo defecto de molde que traen las 51 fases. Acá se ve para qué sirve probarlos igual.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El CA-01 se prueba **arreglando defectos reales**, no leyendo hallazgos de ejemplo: lo que se mide es si alcanzó, y eso solo se sabe al usarlo | CP-002 del [resultado](resultado_pruebas.md) |
| Los códigos de salida se prueban **por los dos caminos**: la función y `validar.py` como orden del sistema. Un código correcto en la función y roto en el arranque no serviría | CP-003 y CP-004 |
| Cuando la prueba y el programa discreparon, **se revisó cuál estaba mal**: el patrón de la prueba no aceptaba `(F2: …)`, y el hallazgo estaba bien. Se corrigió la prueba | §2 del resultado |
| El transversal de errores se prueba aunque el plan no lo pidió | `D-01` |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el archivo ilegible dé un hallazgo y no una excepción (`D-01`) | Fase `B-EP-004-HU-003`, propuesta |
| El criterio de qué es comprobable | [HU-001](../../HU-001-criterio-de-lo-comprobable/HU-001-criterio-de-lo-comprobable.md) |
| Que la corrida completa se pida en una línea | [HU-008](../../HU-008-corrida-completa/HU-008-corrida-completa.md) |

**La advertencia que deja esta fase:** el validador está bien construido para reportar y mal preparado para lo que no puede leer. Lleva versiones dependiendo de que todos los archivos del árbol estén en UTF-8, y el día que uno no lo esté no va a avisar: va a desaparecer.
