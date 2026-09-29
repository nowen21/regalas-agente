# Resultado de Pruebas · Fase `D-EP-004-HU-012-las-marcas-se-miden-al-escribir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `D-EP-004-HU-012-las-marcas-se-miden-al-escribir` |
| **HU** | [HU-012](../HU-012-marcas-de-generacion-automatica.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.5.0 sin commit; carpetas temporales |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

**CA-05 · CP-001, que al escribir lleguen las marcas de lo escrito**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `Write` de un `.md` con raya y viñeta con negrita | Código 0 y las dos marcas en el contexto | Cumple (`test_write_con_marcas_las_devuelve_sin_detener`) |
| 2 | `Edit` sin marcas sobre un archivo con marcas viejas | Sin aviso | Cumple (`test_edit_sin_marcas_no_repite_las_viejas`) |
| 3 | `Write` de un `.py` | Nada | Cumple |
| 4 | Enlace roto y una marca | Código 2, con el enlace y las marcas | Cumple |
| 5 | Marca dentro de código | No se reporta | Cumple |

**CA-06 · CP-002, que el molde lleno no sume marcas y se siga leyendo**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Marcas del molde vacío | Cero | Cero; antes eran 3, en la línea «Viene de», que también pasó a tabla |
| 2 | Hallazgo lleno con el molde nuevo | Cero | Cero |
| 3 | `resumen.hallazgos()` sobre el nuevo | Id, título y estado | Cumple |
| 4 | `resumen.hallazgos()` sobre la forma vieja | Lo mismo que antes | Cumple; también sobre el resumen real del 2026-09-28, con sus 9 hallazgos |
| 5 | `resumen._retoma()` y `viene_de()` en las dos formas | La pregunta viva y el propósito | Cumple |

**RNF · CP-003, versionado y pruebas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `VERSION` y `CHANGELOG.md` | `39.5.0`, MENOR, en palabras llanas | Cumple; `test_la_entrada_del_registro_se_entiende` en OK |
| 2 | `versionado`, `estandar` y las pruebas de la fase | 0 fallas y OK | 0 fallas; 86 pruebas en OK: 4 clases de `pruebas.py` que usan `resumen.py` (29) y 8 archivos de `tests/` (57), entre ellos los 11 casos nuevos |

**Tropiezo al ejecutar:** se lanzó por error la corrida de las 568 pruebas de `pruebas.py`, en contra de `02·F5`. El usuario la detuvo antes de terminar. Se corrieron después solo las que la fase toca.

## 3. Veredicto

| CA | Veredicto |
|---|---|
| CA-05 | Cumple |
| CA-06 | Cumple |

**Concepto de la fase:** Cumple, 3 de 3. **Defectos abiertos:** ninguno.
