# Plan de Pruebas — Fase C-EP-004-HU-008: la corrida entera vuelve a verde

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-004-HU-008 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `C-EP-004-HU-008` de la [HU](../HU-008-corrida-completa.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que las dos funciones escriban el texto que `DOC14` pide | Carpetas temporales |
| Regresión | La suite entera en `OK` | El repositorio |

### 3.2 Técnicas

- **El texto esperado se calcula con `enlaces._texto_esperado`**, el mismo que usa el validador, no con una cadena escrita a mano.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-008 | [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | [CP-001](#cp-001--el-enlace-al-resumen-dice-dónde-vive), [CP-002](#cp-002--la-línea-del-día-dice-dónde-vive), [CP-003](#cp-003--la-corrida-entera-termina-en-ok) | ☐ |

**Cobertura:** 1 de 1 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — El enlace al resumen dice dónde vive

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Carpeta temporal con `historico-chat/resumenes/2026-01-01/tema.md`; llamar `_enlace_al_resumen(carpeta, "2026-01-01-tema.md")` | ` · [historico-chat/resumenes/2026-01-01/tema.md](resumenes/2026-01-01/tema.md)` |

### CP-002 — La línea del día dice dónde vive

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Carpeta temporal con `historico-chat/resumenes/README.md` con sección `## Días`; llamar `_indexar_dias(raiz, "2026-01-01")` | La línea nueva es `- [historico-chat/resumenes/2026-01-01/](2026-01-01/) — sin escribir todavía.` |
| 2 | `enlaces._texto_esperado` sobre esa línea | `None`: ya está bien |

### CP-003 — La corrida entera termina en OK

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `python -m unittest discover -s validadores/tests -p "test_*.py"` | `OK` |
| 2 | `python validadores/pruebas.py` | `OK` |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Alta** | Que la corrida siga en rojo por algo que esta fase debía cerrar | Antes de cerrar |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Pruebas en rojo en `validadores/tests/` | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
