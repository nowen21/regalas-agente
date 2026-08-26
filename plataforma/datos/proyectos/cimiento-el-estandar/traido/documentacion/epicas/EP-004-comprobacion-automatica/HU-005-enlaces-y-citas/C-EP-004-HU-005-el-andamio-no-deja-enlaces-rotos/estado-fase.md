# Estado de fase — Fase «C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos» (módulo «Programas de comprobación — el andamio»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva siga desde ahí sin releer la conversación. Se actualiza en cada puerta.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos` |
| **Módulo** | Programas de comprobación — el andamio |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-005](../HU-005-enlaces-y-citas.md) · pendiente 67 |
| **Última actualización** | 2026-08-20, al cierre |

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, cierre documental con trazabilidad sin faltantes.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase en la HU, §8 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «debe corregir esos hallazgos» | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | mensaje al usuario con los punteros | ☑ |
| 5 | Aprobación del plan detallado | 👤 «OK» a los cuatro planes | ☑ |
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
| **CA cumplidos** | 1 de 1 (CA-05) |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `_reenlazar` en `andamio.py` |
| T-02 | Hecha | 3 casos en verde |

**Hechas:** 2 de 2. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Trasladar solo lo que llega exactamente a la raíz | S-010 en `documentacion/senales.md` |

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte (`00·N2`), junto con el de las otras fases del día.

## 4. Si se bloqueó

No se bloqueó.
