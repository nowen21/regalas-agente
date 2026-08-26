# Estado de fase — Fase «C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde» (módulo «Programas de comprobación — la corrida»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva siga desde ahí sin releer la conversación. Se actualiza en cada puerta.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde` |
| **Módulo** | Programas de comprobación — la corrida |
| **Planteamiento / Épica / HU** | [EP-004](../../epica.md) · [HU-008](../HU-008-corrida-completa.md) · pendiente 68 |
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
| **CA cumplidos** | 1 de 1 (CA-04) |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `historico.py` y `resumen.py` |
| T-02 | Hecha | Un encabezado y cuatro enlaces |
| T-03 | Hecha | 2 casos, y las dos suites en `OK` |

**Hechas:** 3 de 3. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se corrige el programa, no solo el dato | S-011 en `documentacion/senales.md` |

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte (`00·N2`), junto con el de las otras fases del día.

## 4. Si se bloqueó

No se bloqueó.
