# Resultado de Pruebas — Fase `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**La estación de una fase sale de su tabla, y las 209 se leen de una corrida.** Los tres criterios cumplen.

**Lo que decidió el diseño salió de correrlo, no de pensarlo.** Tres veces seguidas en la misma función el lector suponía que todo seguía la convención de hoy: reconocía una sola marca de cumplida, trataba una casilla con prosa como pendiente, y comparaba la frase contra tablas de otro modelo. Reconociendo las dos marcas, las fases terminadas pasaron de **18 a 76**; comparando solo cuando el modelo coincide, las acusadas de contradicción bajaron de **47 a 33**.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-004 | La tabla manda · la fase terminada · la estación que no aplica | ✅ |
| CP-005 | El nombre de la puerta · los días quieta · el «no se sabe» | ✅ |
| CP-007 | **Las dos marcas · la casilla con prosa · el modelo de la tabla** | ✅ |

**11 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Estado |
|---|---|---|---|
| 1 | **Solo se reconocía `☑`.** 76 fases que cierran con `✅` aparecían sin terminar | **Alta** | **Corregido**, con prueba propia |
| 2 | **Una casilla con prosa se contaba como pendiente.** Las fases viejas cuentan qué pasó con la estación en vez de marcarla | **Alta** | **Corregido:** «sin marcar» tiene su propio nombre |
| 3 | **Se comparaba la frase contra tablas de otro modelo.** 107 de 209 no son de trece estaciones | **Crítica** | **Corregido:** solo se compara cuando coinciden |

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Se ve la estación actual | CP-004 | ✅ Cumple |
| CA-02 · Se ve qué falta | CP-005 | ✅ Cumple |
| CA-03 · Dice desde cuándo | CP-005 | ✅ Cumple |

**3 de 3.**

---

## 6. Concepto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |

---

## 7. Las dos baterías completas

| Batería | Pruebas | Resultado |
|---|---|---|
| La plataforma | 552 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **Si las 33 fases que quedan en desacuerdo están mal.** Puede que la frase esté vieja o que la tabla lo esté; el módulo dice cuál manda, no cuál tiene razón.
- **Si alguien va a mirar la lista.** Una fase detenida hace 200 días sale desde hoy; que se retome es otra cosa.
