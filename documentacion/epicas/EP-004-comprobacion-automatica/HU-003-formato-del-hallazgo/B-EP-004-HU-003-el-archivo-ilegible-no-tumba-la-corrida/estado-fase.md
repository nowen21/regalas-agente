# Estado de fase — Fase B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida` |
| **Módulo** | Comprobación automática — [`validadores/comun.py`](../../../../../validadores/comun.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-003](../HU-003-formato-del-hallazgo.md) · **defecto** de la fase [`A`](../A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 4 — pausa y presentación. **Última puerta pasada:** 3, con el plan de trabajo y el plan de pruebas escritos.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 🐞 el veredicto «No cumple» de la fase A | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 pendiente: falta presentarlo | ☐ |
| 5 | Aprobación del plan detallado | 👤 pendiente | ☐ |
| 6 | Ejecución continua | 8 tareas, ninguna empezada | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** El arreglo toca el punto por el que leen **casi todos** los validadores: hoy todos se caen igual ante un archivo que no se puede decodificar.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Todavía no se ejecutó** |
| **CA cumplidos** | 0 de 2 numerados. Los dos ya estaban en «Sí» tras la fase A y hay que mantenerlos |
| **CA en "No"** | El **transversal de errores** viene en «No» desde la fase A, y es lo que esta viene a cerrar |
| **Defectos abiertos aceptados** | Ninguno propio. Hereda el `D-01` de la fase A, que es su motivo |
| **Fuente** | El `resultado_pruebas.md` de esta fase, que aún no existe. Los casos están en [`plan_pruebas.md`](plan_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Pendiente | La lectura tolera ausente, sin permisos y mal codificado |
| T-02 | Pendiente | Que quien lea pueda saber que falló, sin cambiar la firma |
| T-03 | Pendiente | Que el archivo ilegible se reporte con su ruta — **tolerar no es callar** |
| T-04 | Pendiente | Destapar la prueba en rojo esperado |
| T-05 | Pendiente | Caso: la corrida sigue **y reporta lo demás** — CP-002 |
| T-06 | Pendiente | El validador de pendientes vuelve a la lectura común |
| T-07 | Pendiente | Escribir en el contrato qué pasa con el archivo que no se puede leer |
| T-08 | Pendiente | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 0 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La lectura devuelve vacío y **quien la llamó decide**: no sabe qué regla se estaba comprobando, así que no puede armar el mensaje | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| **Tolerar no es callar.** El archivo ilegible se reporta con su ruta; saltarlo en silencio escondería un problema del repositorio | §2.6 del plan y T-03 |
| Sale como **aviso**: no se sabe si el archivo importa, y la propia HU decidió que lo dudoso avisa | §2.6 del plan |
| **El caso mide que la corrida siga y reporte lo demás**, no que no reviente. Una lectura tolerante con una corrida que muere más arriba no arregla nada | CP-002 del [`plan_pruebas.md`](plan_pruebas.md) |
| Hay un préstamo que cerrar: el validador de pendientes nació con su propia lectura **porque la común no servía**. Que vuelva es la prueba de que el arreglo sirve | §2 del plan y CP-004 |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar: §2.7 no dejó dudas.
- **Si un enlace roto pasa por bueno en un archivo leído con reemplazos** (riesgo `R-02`): se anota en el aviso que ese archivo no se revisó entero.
- **Si cambiar la lectura rompe un validador que dependía de que lanzara** (riesgo `R-03`): la suite entera es la red — 357 pruebas la usan de forma indirecta.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 4 esperando la aprobación del plan, que es la puerta normal, no un bloqueo.
