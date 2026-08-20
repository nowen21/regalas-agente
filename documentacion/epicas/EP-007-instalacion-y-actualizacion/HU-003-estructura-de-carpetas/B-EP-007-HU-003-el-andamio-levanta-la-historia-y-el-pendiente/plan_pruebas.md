# Plan de Pruebas — Fase B-EP-007-HU-003: el andamio levanta la historia y el pendiente

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-007-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `B-EP-007-HU-003` de la [HU](../HU-003-estructura-de-carpetas.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| De programa | Que cada modo deje el archivo y las filas en los dos sentidos | Copia temporal del árbol |
| Con los validadores | Que `estandar`, `fases` y `pendientes` no reclamen nada sobre lo creado | La misma copia |
| Regresión | El modo de fase intacto; las dos suites | El repositorio |

### 3.2 Técnicas

- **Se lee lo que hay**: el número siguiente con un hueco en medio (HU-001 y HU-003 existen → HU-004, no HU-003).
- **Las dos formas del §9**: una épica con cuatro columnas y otra con seis.
- **Los marcadores se cuentan**: el documento nuevo trae los mismos `«…»` de contenido que la plantilla, ni uno menos.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-003 | [CA-04](../HU-003-estructura-de-carpetas.md#ca-04--la-historia-y-el-pendiente-nacen-con-su-esqueleto-y-sus-índices-puestos) · la historia | [CP-001](#cp-001--la-historia-nace-con-sus-índices), [CP-002](#cp-002--el-número-se-lee-lo-que-hay) | ☐ |
| HU-003 | CA-04 · el pendiente | [CP-003](#cp-003--el-pendiente-nace-con-su-fila-y-su-historia-en-el-mapa) | ☐ |
| HU-003 | CA-04 · sin contenido | [CP-004](#cp-004--no-escribe-contenido) | ☐ |
| HU-003 | CA-04 · los validadores callan | [CP-005](#cp-005--los-validadores-no-reclaman-nada) | ☐ |
| HU-003 | No regresión | [CP-006](#cp-006--el-modo-de-fase-sigue-igual) | ☐ |

**Cobertura:** 5 de 5 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — La historia nace con sus índices

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Copiar `plantillas/`, `EP-005/epica.md` y su README a una carpeta temporal | Listo |
| 2 | `crear_hu(raiz, "EP-005-…", "prueba-del-andamio", escribir=True)` | Carpeta `HU-015-prueba-del-andamio/` con `HU-015-prueba-del-andamio.md` y `README.md` |
| 3 | Leer el §9 de `epica.md` | Una fila nueva con `[HU-015](HU-015-prueba-del-andamio/HU-015-prueba-del-andamio.md)` y tantas celdas como la cabecera |
| 4 | Leer el README de la épica | Una fila nueva con el enlace `DOC14` |

### CP-002 — El número se lee de lo que hay

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Épica temporal con `HU-001-a/` y `HU-003-c/` | `siguiente_hu` da `HU-004` |

### CP-003 — El pendiente nace con su fila y su historia en el mapa

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `crear_pendiente(raiz, "prueba", "EP-005-…/HU-015-…", escribir=True)` sobre la copia | `pendientes/NN-prueba.md` con la ficha y la historia enlazada |
| 2 | Leer `pendientes/README.md` | Una fila con `NN` en la sección «Sin agrupar», y la historia en el mapa con `NN` |

### CP-004 — No escribe contenido

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar `«` en la HU creada y en `plantillas/HU.md` | Iguales, menos los dos que son estructura (`HU-000` y `«Épica padre»`) |

### CP-005 — Los validadores no reclaman nada

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `enlaces.validar_enlaces` y `pendientes.validar` sobre la copia | Nada sobre lo recién creado |

### CP-006 — El modo de fase sigue igual

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `andamio.py EP HU descripcion` sin `--aplicar` | La misma salida de siempre |
| 2 | Las dos suites enteras | Pasan |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que escriba contenido o pise un archivo existente | Inmediato |
| **Alta** | Que una fila entre con el número de columnas equivocado | Antes de cerrar |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Índices escritos a mano al bajar un defecto por la cadena | 0 |
| Marcadores de contenido perdidos | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
