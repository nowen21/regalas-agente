# Estado de fase — Fase «A-EP-005-HU-013-el-enganche-del-checkpoint» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva siga desde ahí sin releer la conversación. Se actualiza en cada puerta.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-013-el-enganche-del-checkpoint` |
| **Módulo** | Automatismos — enganches |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-013](../HU-013-el-checkpoint-se-reclama-solo.md) · pendiente 64 |
| **Última actualización** | 2026-08-20, al cierre |

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, cierre documental con trazabilidad sin faltantes.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase en la HU, §8 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «solucione de una» y «toda mejora debe estar dentro de una fase» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | mensaje al usuario con los punteros | ☑ |
| 5 | Aprobación del plan detallado | 👤 «si aprobado los tres planes» | ☑ |
| 6 | Ejecución continua | las tareas del plan | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☑ Cumple, ciclo 1 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | | ☐ |
| 11 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 (CA-01, CA-02, CA-03) |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `validadores/checkpoint.py` |
| T-02 | Hecha | `adaptadores/claude-code/hook_checkpoint.py` |
| T-03 | Hecha | Fila en `HOOKS_CLAUDE`; la prueba de la frontera cuenta contra la lista |
| T-04 | Hecha | 8 casos, en verde |
| T-05 | Hecha | Especificación §4.5 y §13, mapa del sitio, mapa del amarre |
| T-06 | Hecha | 9 de 9 proyectos; verificado en AgroSystem |

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Fechas, no contenido; el enganche no escribe el checkpoint | S-008 en `documentacion/senales.md` |

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte (`00·N2`), junto con el de las otras dos fases del día.

## 4. Si se bloqueó

No se bloqueó.
