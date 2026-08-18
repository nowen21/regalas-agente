# Plan de Trabajo — Fase B-EP-005-HU-003-el-hallazgo-grave-detiene (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-005-HU-003-el-hallazgo-grave-detiene` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-003 Disparar las comprobaciones al escribir un archivo](../HU-003-disparo-al-escribir-un-archivo.md) — una sola (`F12.1`) |
| **Complementa** | [`A-EP-005-HU-003`](../A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md), que cerró en **No cumple** |
| **Módulo** | Automatismos |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-005-HU-003-el-hallazgo-grave-detiene` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐞 **Defecto**. El CA-03 pide que el hallazgo grave **detenga** y el resto avise. Hoy **todo avisa**: el enganche informa y el trabajo sigue en los dos casos.

**CA de la HU que cubre esta fase**

| Exigencia de HU-003 | Qué exige | Estado tras la fase A |
|---|---|---|
| [CA-03](../HU-003-disparo-al-escribir-un-archivo.md#ca-03--el-hallazgo-grave-detiene-el-resto-avisa) | El hallazgo grave **detiene**; el resto avisa | **En «No».** Nada detiene |
| Transversal · **Reversibilidad** | Detener nunca deja el archivo a medias | **N/A hoy**, porque nada detiene. **Pasa a aplicar** con esta fase |

**Esta fase enciende un transversal que hoy no aplica.** Es su parte más delicada: en cuanto algo detenga, «detener sin dejar el archivo a medias» deja de ser teoría.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que un documento con un incumplimiento **grave** no se pueda dejar así, y que detenerlo no rompa nada.

**Fuera de alcance:**

- **Cambiar qué se considera grave.** La severidad la fija cada validador, y `EP-004 · HU-003` ya la documentó.
- **Detener por avisos.** Un validador que reprueba por algo discutible se vuelve ruido, y lo que se ignora después no son solo sus avisos.
- **Los otros cinco enganches.** Solo el de escritura.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 corriendo `hook_md.py` como orden del sistema.

**Lo que ya existe:** el disparo al escribir, que corre en el momento; el silencio ante lo que no le toca, comprobado mirando el código de salida; y la separación falla/aviso en `comun.py`, con su contrato ya escrito.

**Lo que no existe:** cualquier camino por el que un hallazgo de severidad falla haga algo distinto de imprimirse.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/hook_md.py` | Modificar | Con una falla, termina de forma que la herramienta lo entienda como «detener»; con avisos, sigue |
| `validadores/docs/hook_md.md` | Modificar | Qué detiene, qué avisa y qué pasa con el archivo ya escrito |
| `documentacion/automatismos/spec.md` | Modificar | §4.3 pasa de «lo que todavía no hace» a la regla |
| `validadores/pruebas.py` | Modificar | Los casos de detener, de no detener y de reversibilidad |
| `…/B-EP-005-HU-003-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-003-disparo-al-escribir-un-archivo.md` | Modificar | §8 nombra esta fase; §1 cambia de estado al cerrar |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

`hook_md.py` lo dispara la herramienta al escribir un archivo, y **lo instala `instalar.py` en todos los proyectos**. Cambiar lo que devuelve cambia el comportamiento de todos los proyectos que ya lo tienen instalado — **es lo más invasivo de las ocho fases `B`**, y por eso §8 lo trata aparte.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: es un enganche de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El enganche de escritura, ya registrado. No cambia de forma; cambia qué devuelve ante una falla.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El archivo se escribe y después se avisa de que hay que arreglarlo** | Impedir la escritura | El enganche corre **después** de escribir: no puede impedirla sin deshacerla, y deshacer la escritura de otro es más peligroso que el defecto que se busca. «Detener» es detener el **trabajo**, no la escritura |
| Solo detiene la **falla**, nunca el aviso | Detener también con avisos | Los avisos incluyen falsos positivos conocidos. Detener por ellos haría que se apague el enganche, y con él se pierde también lo que sí sirve |
| Lo que detiene **dice qué arreglar y dónde**, en el mismo mensaje | Un «detenido» seco | Detener sin decir qué es la peor forma de detener: obliga a correr el validador a mano |
| Se prueba **por el camino real**, disparando el enganche como orden del sistema | Llamar a la función | Lo que importa es lo que la herramienta recibe, no lo que la función devuelve |

### 2.7 Dudas por resolver antes de escribir

Ninguna **de implementación**. Queda una decisión del usuario que **no bloquea esta fase**: la pregunta 8 y 9 del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) —si otros enganches detienen o avisan— es la misma pregunta en otro sitio, y lo que se decida acá le sirve de precedente.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-03 — El hallazgo grave detiene; el resto avisa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Que una falla haga que el enganche pida detener el trabajo | `validadores/hook_md.py` | 2,0 |
| T-02 | Que el mensaje diga **qué arreglar y dónde**, no solo que se detuvo | `validadores/hook_md.py` | 1,0 |
| T-03 | Caso: un documento con falla detiene; uno con avisos, no | `validadores/pruebas.py` | 2,0 |

### Transversal · Reversibilidad — Detener nunca deja el archivo a medias

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso: tras detener, el archivo escrito **está entero**, tal como lo escribió quien lo escribió | `validadores/pruebas.py` | 1,5 |
| T-05 | Escribir qué pasa con el archivo ya escrito cuando se detiene | `validadores/docs/hook_md.md` | 1,0 |

### Transversal · Errores y Rendimiento — No regresión

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | Caso: lo que no le toca se sigue ignorando en silencio, y el disparo sigue sin notarse | `validadores/pruebas.py` | 1,0 |
| T-07 | Pasar §4.3 de la especificación de «lo que todavía no hace» a la regla | `documentacion/automatismos/spec.md` | 1,0 |
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU | Cierre | 1,5 |

**Total: 8 tareas · 11,0 horas.**

---

## 4. Secuencia de ejecución

T-01 y T-02 juntos: detener sin decir qué no sirve. T-03 comprueba los dos lados —que detiene y que **no** detiene de más—, y ese segundo lado es el que evita que el enganche se vuelva insoportable. T-04 es el transversal que esta fase enciende. T-06 protege lo que ya funcionaba. T-05 y T-07 escriben. T-08 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| Exigencia | Método de verificación | Evidencia |
|---|---|---|
| CA-03 | Escribir un documento con una falla y otro con avisos, y mirar qué recibe la herramienta | T-03 |
| Transversal · Reversibilidad | Leer el archivo después de que el enganche detuvo | T-04 |
| Transversal · Errores · Rendimiento | Los casos de la fase A, otra vez | T-06 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con documentos armados para el caso. **Ningún archivo del repositorio se rompe.**

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. **Y hay una salida más rápida**, que conviene tener escrita: quitar el enganche de los ajustes del proyecto lo desactiva sin tocar el estándar. Si detener resulta insoportable en un proyecto, esa es la puerta.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

**Es el cambio más invasivo de las ocho fases `B`.** El enganche está instalado en todos los proyectos que heredan el estándar, y a partir de aquí un documento con una falla **detiene el trabajo** en todos.

Por eso:

- **Solo detiene la falla**, que es lo que ya estaba definido como incumplimiento claro.
- **El mensaje dice qué arreglar**, para que detener cueste minutos y no una investigación.
- **Se puede desactivar por proyecto** quitando el enganche de sus ajustes, y queda escrito dónde.
- **Sube MAYOR**: obliga a un proyecto al día a hacer algo nuevo — arreglar lo que antes solo se le avisaba.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N3`](../../../../../base/00-nucleo-blindado.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`05·E1`](../../../../../base/05-errores-y-logging.md), [`08·T4`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que detener resulte insoportable y alguien apague el enganche | Se pierde también lo que sí sirve | Solo detiene la falla; el mensaje dice qué arreglar; y queda escrito cómo desactivarlo por proyecto en vez de a escondidas | Abierto |
| R-02 | Que un falso positivo de un validador pase a detener el trabajo | Se bloquea trabajo por un defecto del validador | Los falsos positivos conocidos son **avisos**, no fallas. Si alguno es falla, es defecto de ese validador y se reporta | Abierto |
| R-03 | Que detener deje el archivo a medias | Se pierde trabajo | No puede: el enganche corre **después** de escribir. El caso `T-04` lo comprueba | Abierto |
| R-04 | Que el cambio llegue a proyectos que no lo esperan | Sorpresa en trabajo ajeno | Sube MAYOR, y el aviso de desfase lo informa al abrir la sesión | Abierto |

---

## 11. Definition of Done

- [ ] Un documento con una **falla** detiene el trabajo.
- [ ] Uno con **avisos** no lo detiene.
- [ ] El mensaje dice **qué arreglar y dónde**.
- [ ] Tras detener, el archivo escrito **está entero**.
- [ ] Lo que no le toca se sigue ignorando en silencio, y el disparo sigue sin notarse.
- [ ] Está escrito cómo desactivarlo por proyecto.
- [ ] `CHANGELOG` y `VERSION` con la subida **MAYOR** (`20·M10`).
- [ ] §8 de la HU nombra esta fase.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
