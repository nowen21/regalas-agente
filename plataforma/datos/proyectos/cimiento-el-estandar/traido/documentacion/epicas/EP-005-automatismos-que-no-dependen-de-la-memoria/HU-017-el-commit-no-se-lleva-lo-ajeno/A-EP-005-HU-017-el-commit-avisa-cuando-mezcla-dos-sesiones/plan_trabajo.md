# Plan de Trabajo — Fase A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones (módulo Enganches de git)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones` |
| **Épica** | `EP-005` Automatismos que no dependen de la memoria |
| **HU** | `HU-017` El commit no se lleva el trabajo de otra sesión |
| **Módulo** | Enganches de git |
| **Especificación del módulo** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** el guardián que pide el [pendiente 80](../../../../../pendientes/hecho/dos-sesiones-a-la-vez-no-se-pisan.md). El usuario ordenó resolverlo en vez de dejarlo anotado.

**CA de la HU que cubre esta fase:**

| CA de `HU-017` | Estado |
|---|---|
| CA-01, un commit que mezcla dos sesiones avisa | ☐ |
| CA-02, el aviso dice por dónde empezar | ☐ |
| CA-03, no avisa cuando no hay nada que avisar | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que quien commitea se entere de que está arrastrando lo que otra sesión tiene a medio construir.

**Fuera de alcance:** impedir el commit, y saber qué sesión está viva. Los dos están declarados en la [HU](../HU-017-el-commit-no-se-lleva-lo-ajeno.md) §3.3 con su motivo.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Verificado el 2026-08-22:**

1. `adaptadores/claude-code/hook_md.py` es el enganche `PostToolUse` de `Write` y `Edit`. Recibe el JSON de la herramienta, que trae `session_id` y `tool_input.file_path`. Hoy devuelve 0 y no hace nada si el archivo no es un `.md`.
2. El `pre-commit` que escribe `validadores/instalar.py` corre dos comprobaciones sobre lo preparado, `versionado` y `marcas`, las dos cortando el commit si fallan.
3. `validar.py` arma sus subcomandos con `add_parser`, y `cmd_todo` corre todos salvo los de `FUERA_DE_LA_CORRIDA`, cada uno con su motivo escrito.
4. `git` no expone qué sesión lanza el `pre-commit`, y no hay dónde consultarlo.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/sesiones.py` | Nuevo | Validador | El registro y la comprobación |
| `validadores/validar.py` | Modificar | Validador | El subcomando, y su motivo para quedar fuera de la corrida |
| `adaptadores/claude-code/hook_md.py` | Modificar | Adaptador | Anota lo editado, antes del filtro de `.md` |
| `validadores/instalar.py` | Modificar | Instalador | La línea del `pre-commit`, que no corta |
| `validadores/tests/test_dos_sesiones_no_se_pisan.py` | Nuevo | Prueba | Los diez casos |
| `.gitignore` | Modificar | Configuración | El registro no se versiona |

### 2.2 Matriz de dependencias del refactor

No aplica: todo es aditivo. El enganche gana una llamada antes de su filtro y no cambia lo que ya hacía; el `pre-commit` gana una línea que no corta.

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la UI

No aplica. El punto de entrada es el `pre-commit`, que se dispara solo.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se detecta que el commit **mezcla**, no de quién es | Averiguar qué sesión commitea | `git` no lo sabe y no hay dónde consultarlo. Y no hace falta: un commit legítimo sale de una sola conversación |
| Avisa y deja pasar | Rechazar el commit | Retomar lo que otra dejó a medias es legítimo. Y está medido en el [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md): un enganche que rechaza siempre se apaga en una tarde |
| Se anota todo lo que se edita, no solo los `.md` | Anotar solo lo que el enganche ya filtra | Lo que una sesión se llevó por delante la vez que pasó fue un archivo de código a medio corregir |
| El registro caduca a las doce horas | Sin caducidad | Sin ella, el registro de la semana pasada hace saltar el aviso en cada commit, y volvemos al enganche que se apaga |
| El registro no se versiona | Guardarlo como todo lo demás del histórico | Es estado de trabajo, no memoria. Versionarlo lo convierte en el próximo archivo que dos sesiones se pisan |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿Avisar o rechazar? | usuario | Resuelta: avisar, con el motivo de §2.6 |

---

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `anotar()` y su carpeta de registro | Validador | 1 h | — | EV-01 |
| T-02 | `validar_preparados()`, que mira lo que entra al commit | Validador | 1 h | T-01 | EV-01 |
| T-03 | El subcomando en `validar.py`, fuera de la corrida completa con su motivo | Validador | 0,5 h | T-02 | EV-01 |
| T-04 | Anotar desde el enganche, antes del filtro de `.md` | Adaptador | 0,5 h | T-01 | EV-02 |
| T-05 | La línea del `pre-commit`, que no corta el commit | Instalador | 0,5 h | T-03 | EV-02 |
| T-06 | El registro fuera del control de versiones | Configuración | 0,25 h | T-01 | EV-02 |
| T-07 | Los diez casos, la mitad de lo que NO debe avisar | Prueba | 1,5 h | T-02 | EV-03 |

**Total estimado:** 5,25 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05
**Paralelizables:** T-04, T-06 y T-07 pueden ir apenas exista T-02.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Prueba automatizada | EV-03 | ☐ |
| CA-02 | Prueba automatizada sobre el texto del aviso | EV-03 | ☐ |
| CA-03 | Cinco casos de lo que no debe avisar | EV-03 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | El módulo y el subcomando | `validadores/sesiones.py`, `validadores/validar.py` |
| EV-02 | El cableado | `adaptadores/claude-code/hook_md.py`, `validadores/instalar.py`, `.gitignore` |
| EV-03 | Las pruebas | `validadores/tests/test_dos_sesiones_no_se_pisan.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales. La prueba sustituye la lectura de lo preparado para no depender de un repositorio de verdad, que es lo que la volvería lenta y frágil. Ningún dato real ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

---

## 7. Reversión / rollback  ·  Q11

Revertir el commit. Todo es aditivo: quitarlo devuelve el enganche y el `pre-commit` a lo que hacían.

---

## 8. Producción y migración incremental  ·  Q12

Aditivo. Los proyectos ya instalados reciben la línea nueva del `pre-commit` la próxima vez que se corra el instalador. Mientras tanto siguen exactamente como hoy, sin el aviso.

---

## 9. Reglas del estándar aplicadas  ·  Q13

- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente baja a fase.
- [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), que en esta misma jornada ya se incumplió una vez y acá se respeta.
- `20·M10`, por la versión y el registro.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que el aviso salte en commits normales | Se apaga y no sirve para nada | La vigencia de doce horas, y cinco de los diez casos son de lo que no debe avisar | Cerrado |
| R-02 | Que anotar rompa el enganche y bloquee al agente | Peor que el problema que resuelve | La llamada va protegida, y si falla el enganche sigue su curso | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Las suites que la fase toca, en verde
- [x] Trazabilidad escrita en los dos lados
- [x] `CHANGELOG.md` y `VERSION` al día
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
