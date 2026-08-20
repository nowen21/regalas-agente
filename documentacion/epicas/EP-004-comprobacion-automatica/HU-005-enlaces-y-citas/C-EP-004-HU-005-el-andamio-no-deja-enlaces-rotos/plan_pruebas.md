# Plan de Pruebas — Fase C-EP-004-HU-005: el andamio no deja enlaces rotos

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-004-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | La fase `C-EP-004-HU-005` de la [HU](../HU-005-enlaces-y-citas.md) |
| **Fecha** | 2026-08-20 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente: el usuario |
| **Estado** | Borrador |

Una sola fase: van las secciones 3, 5, 6, 9 y 12, como la plantilla indica para una fase chica.

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Que `_reenlazar` traslade lo que llega a la raíz y deje lo demás | Texto en memoria |
| De programa | Que un esqueleto recién levantado pase el validador de enlaces | Carpeta temporal con copia de `plantillas/` |
| Regresión | Las dos suites | El repositorio |

### 3.2 Técnicas

- **El mismo enlace desde dos profundidades** (plantilla en `plantillas/` y en `plantillas/planes/`), para aislar que el prefijo se calcula y no se escribe fijo.
- **Un `../` que no llega a la raíz**, que no debe tocarse.
- **El validador real** sobre el esqueleto, que es lo que envejece bien.

### 3.5 Alcance de la ejecución

`validadores/tests/` entera y `validadores/pruebas.py` entera.

## 5. Matriz de trazabilidad

| HU | CA / exigencia | Caso | Estado |
|---|---|---|---|
| HU-005 | [CA-05](../HU-005-enlaces-y-citas.md#ca-05--lo-que-un-programa-del-estándar-escribe-no-nace-con-enlaces-rotos) | [CP-001](#cp-001--el-esqueleto-nuevo-no-trae-el-enlace-crudo), [CP-002](#cp-002--el-validador-de-enlaces-lo-da-por-bueno) | ☐ |
| HU-005 | Límites · lo que no llega a la raíz | [CP-003](#cp-003--un-enlace-que-no-llega-a-la-raíz-no-se-toca) | ☐ |
| HU-005 | No regresión | [CP-004](#cp-004--nada-de-lo-que-ya-estaba-deja-de-pasar) | ☐ |

**Cobertura:** 3 de 3 exigencias con caso = 100%.

## 6. Casos de prueba

### CP-001 — El esqueleto nuevo no trae el enlace crudo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Copiar `plantillas/` a una carpeta temporal con `documentacion/epicas/EP-001-p/HU-001-p/` | Listo |
| 2 | Levantar una fase con `andamio.crear(..., escribir=True)` | Cinco documentos |
| 3 | Buscar `](../../base/` y `«RUTA-ESTANDAR»` en los cinco | No están |
| 4 | Buscar `](../../../../../base/` en `resultado_pruebas.md` y en `estado-fase.md` | Está en los dos |

### CP-002 — El validador de enlaces lo da por bueno

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sobre la carpeta temporal, con una `base/08-pruebas.md` mínima puesta, correr `enlaces.validar_enlaces` | Ningún roto dentro de la fase |

### CP-003 — Un enlace que no llega a la raíz no se toca

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `_reenlazar` sobre un texto con `](../otra/cosa.md)` desde `plantillas/planes/` | Queda igual |

### CP-004 — Nada de lo que ya estaba deja de pasar

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Las dos suites enteras | Pasan (salvo lo previo que el pendiente 68 cierra en su fase) |

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Alta** | Que se reescriba un enlace que no iba a la raíz | Antes de cerrar |
| **Media** | Que quede una forma de enlace sin atender | Se reporta |

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Enlaces rotos en un esqueleto nuevo | 0 |
| Pruebas del repositorio que dejan de pasar | 0 |

Un solo concepto: **Cumple** o **No cumple**. Se escribe en el resultado, no acá.
