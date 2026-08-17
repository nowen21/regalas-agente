# Plan de Trabajo — Fase «B-EP-007-HU-001-prepara-su-propia-salida» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-007-HU-001-prepara-su-propia-salida` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-001 — Instalar con una línea](../HU-001-instalar-con-una-linea.md) — **una sola** (`F12.1`) |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Especificación del módulo** | No existe. Sigue declarada como deuda desde la fase [`A`](../A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md) (§10, `B-02`) |
| **Fecha apertura** | 2026-08-16 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- 📝 **Modifica fase(s):** ninguna. No corrige lo que la fase `A` hizo; corrige algo que ya estaba desde que el instalador existe.
- ✨ **Funcionalidad nueva:** ninguna. Es robustez.

**De dónde sale:** el [pendiente 45](../../../../../pendientes/45-el-instalador-revienta-al-imprimir-sin-preparar-la-salida.md), que nació en [validadores-y-hooks](../../../../../pendientes/hecho/validadores-y-hooks.md) y se destapó como el `DEF-02` de [poner-al-dia-lo-ya-instalado](../../../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md).

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Una línea deja el proyecto listo](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | ☐ |

**Por qué el CA-01.** «Una línea deja el proyecto listo» no se cumple si el programa se muere a mitad de camino por escribir una flecha en pantalla. Que hoy solo pase llamándolo como biblioteca no cambia qué exige el criterio.

---

## 1. Objetivo y alcance

**Objetivo:** que `instalar()` prepare su propia salida, para que quien lo llame no tenga que conocer un detalle que no es suyo.

**Fuera de alcance:**

- **Los demás validadores.** Cada uno tiene su propio arranque y esta fase no los revisa. Si alguno tiene el mismo hueco, es otro pendiente.
- **Cambiar los caracteres que se imprimen.** Quitar la flecha y las tildes taparía el síntoma y empeoraría el texto, que se lee en español.
- **Escribir la especificación del módulo.** Deuda heredada.

---

## 2. Análisis previo — línea base verificada

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/instalar.py` | Modificar | Instalación | Una línea al entrar a `instalar()` |
| `validadores/tests/test_instalar_reparar.py` | Modificar | Test | El caso nuevo, y se le quita el rodeo que puso la fase anterior |
| `validadores/docs/instalar.md` | Modificar | Documentación | Decir que `instalar()` prepara su salida |
| `pendientes/README.md` · `pendientes/hecho/` | Modificar / Nuevo | Backlog | Cerrar el 45 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | PARCHE |

**Verificado el 2026-08-16:** `preparar_salida()` vive en `validadores/comun.py` línea 47, `instalar.py` ya la importa (línea 47) y hoy solo la llama `main()`.

### 2.2 Matriz de dependencias del cambio

| Quién | Impacto |
|---|---|
| `main()` | La sigue llamando. Llamarla dos veces no hace daño: `reconfigure` es idempotente |
| Los enganches que corren el instalador | Ninguno: hoy pasan por `main()` y seguirán pasando |
| La prueba de la fase `A-EP-007-HU-006` | Se le quita el `preparar_salida()` de arranque, que era el rodeo |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Preparar la salida al entrar a `instalar()` | Dejarlo solo en `main()` y documentarlo | Documentar un detalle interno es pedirle al de afuera que conozca las tripas del de adentro |
| Dejar la llamada de `main()` donde está | Quitarla | `main()` imprime antes de llamar a `instalar()` —la lista de proyectos, el aviso de simulación—, así que la necesita igual |
| La prueba fuerza una consola que no admite la flecha | Confiar en la consola de la máquina | Bajo `unittest` la salida suele venir ya en UTF-8, así que sin forzarla la prueba pasa en verde con el defecto puesto |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `instalar()` llama a `preparar_salida()` al entrar | Instalación | 0,2 h | — | EV-01 |
| T-02 | Caso de prueba con la salida forzada a `cp1252` | Test | 1 h | T-01 | EV-01 |
| T-03 | Quitar el `preparar_salida()` de arranque de `test_instalar_reparar.py` | Test | 0,2 h | T-01 | EV-01 |
| T-04 | `validadores/docs/instalar.md` | Documentación | 0,3 h | T-01 | EV-02 |
| T-05 | Cerrar el 45 en `pendientes/` | Backlog | 0,3 h | T-04 | — |
| T-06 | `CHANGELOG.md` y `VERSION` | Versionado | 0,3 h | T-05 | — |

**Total estimado:** 2,3 h

**Por qué el T-03 es del alcance y no una limpieza suelta:** mientras el rodeo esté puesto, la prueba nueva pasa aunque el arreglo no exista. Quitarlo es lo que hace que la prueba pruebe.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-02 → T-04 → T-05 → T-06

> Solo se tocan los archivos de §2.1 ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-01](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | Prueba automática con la salida forzada a una codificación que no admite la flecha | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de la prueba | `resultado_pruebas.md` de esta fase |
| EV-02 | Documentación al día | `funcionalidad_implementada.md` del cierre |

---

## 6. Datos y ambiente de prueba

Carpeta temporal desechable y copia desechable del estándar, como la fase `A-EP-007-HU-006`. Nunca un proyecto real ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

---

## 7. Reversión / rollback

Una línea. Se revierte volviendo el commit atrás, y nada queda escrito de forma distinta: `preparar_salida()` no toca archivos, solo la consola del proceso.

---

## 8. Producción y migración incremental

No toca nada instalado. El programa vive en el estándar y los proyectos lo llaman por su dirección, así que ya corren esta versión sin hacer nada.

---

## 9. Reglas del estándar aplicadas

[`02·F23`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar), [`20·M10`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la prueba pase en verde con el defecto puesto | La fase se daría por cumplida sin estarlo | Se comprueba a propósito: se revierte la línea del T-01 y la prueba tiene que ponerse roja | Abierto hasta la corrida |
| B-02 | Que forzar la codificación en la prueba rompa la salida de las otras pruebas | Ruido o fallas cruzadas | La salida se restaura al terminar el caso | Abierto hasta la corrida |

---

## 11. Definition of Done

- [ ] El CA-01 verificado con evidencia
- [ ] La prueba se pone roja si se revierte el arreglo
- [ ] El rodeo de la fase anterior, quitado
- [ ] Documentación, pendiente cerrado, `CHANGELOG` y `VERSION`
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** Vive en el `funcionalidad_implementada.md` de esta fase.
