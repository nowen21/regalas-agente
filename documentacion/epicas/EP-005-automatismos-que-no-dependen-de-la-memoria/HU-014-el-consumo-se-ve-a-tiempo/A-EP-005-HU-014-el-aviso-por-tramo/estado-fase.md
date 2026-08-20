# Estado de fase — Fase «A-EP-005-HU-014-el-aviso-por-tramo» (módulo «Automatismos — enganches»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva siga desde ahí sin releer la conversación. Se actualiza en cada puerta.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-014-el-aviso-por-tramo` |
| **Módulo** | Automatismos — enganches |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-014](../HU-014-el-consumo-se-ve-a-tiempo.md) · pendiente 65 |
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
| T-01 | Hecha | El caso fija el texto y las cifras del cierre |
| T-02 | Hecha | `TRAMO`, `tramo()`, `cruzo_tramo()`, `aviso_de_tramo()` |
| T-03 | Hecha | `--modo cierre|aviso`, cierre por defecto |
| T-04 | Hecha | Fila `UserPromptSubmit` con `--modo aviso` |
| T-05 | Hecha | 8 casos, en verde |
| T-06 | Hecha | Especificación §4.6 y §13, mapa del sitio |
| T-07 | Hecha | 9 de 9 proyectos; verificado en AgroSystem |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un millón por tramo, sin estado compartido; el comando de cierre no se toca | S-009 en `documentacion/senales.md` |

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte (`00·N2`), junto con el de las otras dos fases del día.

## 4. Si se bloqueó

No se bloqueó.
