# Estado de fase — Fase «A-EP-007-HU-001-rellenar-los-marcadores-al-copiar» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-001-rellenar-los-marcadores-al-copiar` |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Planteamiento / Épica / HU** | [EP-007](../../epica.md) · [HU-001](../HU-001-instalar-con-una-linea.md) · [pendiente 40](../../../../../pendientes/hecho/el-instalador-rellena-los-marcadores.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8.

Se usan las **once etapas de [`02·F15`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)**, que es la fuente única del ciclo de una fase en este repositorio.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 el usuario pidió las tres piezas | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | presentados al usuario | ☑ |
| 5 | Aprobación del plan detallado | 👤 aprobados el 2026-08-16 | ☑ |
| 6 | Ejecución continua | plan implementado | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto por CA | ☑ Cumple, ciclo 2 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 **acá está detenida** | ☐ |
| 10 | Reporte al usuario | hash, resumen y estado | ☐ |
| 11 | Publicación / despliegue | 👤 autorizado | ☐ |

**La fase se detuvo una vez, en la estación 6.** La prueba salió roja por el criterio del plan, no por el código: pedía que no quedara **ningún** hueco, y los cuatro archivos de `.agente/` llegan con huecos a propósito. Se reportó, el usuario aprobó corregir el criterio y la ejecución siguió. Está en el [`resultado_pruebas.md`](resultado_pruebas.md) §2 y como `DEF-01`.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 (CA-01, CA-02 y el RNF de compatibilidad) |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno. El `DEF-01` era del plan, no del código, y quedó corregido |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `instalar_stack` rellena |
| T-02 | Hecha | `instalar_recuerdos` rellena |
| T-03 | Hecha | `instalar_agente_config` rellena |
| T-04 | Hecha | `validadores/tests/test_instalar_marcadores.py`, la primera prueba del repositorio |
| T-05 | Hecha | `validadores/docs/instalar.md` dice qué rellena cada función y qué hueco no se toca |
| T-06 | Hecha | La segunda corrida está dentro del CP-003 |
| T-07 | Hecha | `CHANGELOG` 21.1.0 y `VERSION` |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| La huella del stack sale del central y no del texto copiado, así que rellenar no rompe la comparación | Se verificó en esta fase; queda en el plan §2.2 |
| Probar función por función no habría atrapado el defecto: hacen falta pruebas de integración de la instalación entera | Queda en el plan de pruebas §3.1 |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)), y es lo único que detiene la fase.
- **Un proyecto instalado antes de este cambio no se arregla solo** en los 4 archivos de `.agente/`, porque no se pisan. Quedó respondida en el `CHANGELOG` de la 21.1.0. Si hace falta arreglarlos, es fase aparte.
- **Avisarle a `shopnest-mesa`** que su reporte cerró. Depende del [pendiente 36](../../../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md).

---

## 4. Si se bloqueó

No está bloqueada. Se detuvo una vez en la estación 6, por el `DEF-01`, y se desbloqueó con la aprobación del usuario el mismo día.
