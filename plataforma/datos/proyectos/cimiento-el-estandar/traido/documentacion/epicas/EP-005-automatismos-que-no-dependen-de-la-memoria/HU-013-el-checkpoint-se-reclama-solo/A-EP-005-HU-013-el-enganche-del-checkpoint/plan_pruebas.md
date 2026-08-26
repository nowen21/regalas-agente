# Plan de Pruebas — Fase A-EP-005-HU-013: el enganche del checkpoint

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-013 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `A-EP-005-HU-013` de la [HU](../HU-013-el-checkpoint-se-reclama-solo.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que el módulo reconozca la fase y decida bien falta / atrasado / al día | Carpetas temporales |
| De enganche | Que el programa del adaptador lea la entrada, imprima y salga con 0 | Subproceso con JSON por la entrada estándar |
| Regresión | Que las dos suites sigan en verde, y que la de la frontera cuente bien | El repositorio |

### 3.2 Técnicas

- **Fechas forzadas** con `os.utime`: el orden de escritura no puede depender del reloj.
- **El mismo archivo en dos estados**: atrasado y al día, para aislar que la única diferencia es la fecha del checkpoint.
- **Huella antes y después**: lo que comprueba que el enganche no escribe.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera: se toca `instalar.py`, que las dos cubren.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-013 | [CA-01](../HU-013-el-checkpoint-se-reclama-solo.md#ca-01--una-puerta-pasa-sin-checkpoint-y-se-avisa) | [CP-001](#cp-001--sin-checkpoint-se-avisa-y-se-nombra-la-fase) | ☐ |
| HU-013 | [CA-02](../HU-013-el-checkpoint-se-reclama-solo.md#ca-02--el-checkpoint-existe-pero-quedó-atrás) | [CP-002](#cp-002--el-checkpoint-atrasado-se-avisa-con-el-documento), [CP-003](#cp-003--al-día-calla) | ☐ |
| HU-013 | [CA-03](../HU-013-el-checkpoint-se-reclama-solo.md#ca-03--lo-que-no-es-puerta-calla-y-el-enganche-no-toca-el-checkpoint) | [CP-004](#cp-004--los-cuatro-silencios), [CP-005](#cp-005--la-huella-no-cambia) | ☐ |
| HU-013 | Límites · entrada rota o archivo borrado | [CP-006](#cp-006--la-entrada-rota-y-el-archivo-que-ya-no-está) | ☐ |
| HU-013 | RNF-01 · no lee el contenido | [CP-007](#cp-007--solo-mira-fechas) | ☐ |
| HU-013 | RNF-02 · el aviso dice dónde | [CP-001](#cp-001--sin-checkpoint-se-avisa-y-se-nombra-la-fase) | ☐ |
| HU-013 | No regresión | [CP-008](#cp-008--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 7 de 7 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — Sin checkpoint se avisa, y se nombra la fase

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear `A-EP-001-HU-001-prueba/resultado_pruebas.md` sin `estado-fase.md` | La carpeta existe |
| 2 | Correr el enganche con esa ruta como `file_path` | Imprime un aviso con «A-EP-001-HU-001-prueba» y «falta» |
| 3 | Leer el código de salida | 0 |

### CP-002 — El checkpoint atrasado se avisa, con el documento

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir `estado-fase.md` con fecha 1000 y `funcionalidad_implementada.md` con fecha 2000 | Las dos existen |
| 2 | Correr el enganche con la ruta del segundo | Aviso con la fase y `funcionalidad_implementada.md` |

### CP-003 — Al día, calla

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner `estado-fase.md` con fecha 3000 y repetir el enganche | Sin salida, código 0 |

### CP-004 — Los cuatro silencios

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con la ruta de `estado-fase.md` | Sin salida |
| 2 | Correr con la ruta de `plan_pruebas.md` | Sin salida |
| 3 | Correr con la ruta de `README.md` de la fase | Sin salida |
| 4 | Correr con un `.md` fuera de cualquier fase | Sin salida |

### CP-005 — La huella no cambia

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar la huella de `estado-fase.md` | Un valor |
| 2 | Correr el enganche con un `resultado_pruebas.md` atrasado | Avisa |
| 3 | Volver a calcular la huella | La misma |

### CP-006 — La entrada rota y el archivo que ya no está

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con «esto no es JSON» por la entrada | Código 0, sin salida |
| 2 | Correr con la ruta de un `resultado_pruebas.md` que se borró | Código 0, sin salida |

### CP-007 — Solo mira fechas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir un `resultado_pruebas.md` ilegible (bytes al azar) y un checkpoint atrasado | Avisa igual: no intentó leer el contenido |

### CP-008 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa, incluida la de la frontera corregida |
| 2 | `validadores/pruebas.py` entera | 365 de 365, como en la línea base del día |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que el enganche escriba o borre el checkpoint | Inmediato |
| **Alta** | Que avise en archivos que no son puerta, o que calle con el checkpoint atrasado | Antes de cerrar |
| **Media** | La redacción del aviso | Se reporta |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — 7 de 7 |
| Avisos falsos sobre los cuatro silencios | 0 |
| Pruebas del repositorio que dejan de pasar | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
