# Plan de Trabajo — Fase A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-001](../HU-001-transcripcion-de-la-sesion.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-001 Escribir la sesión a medida que pasa, con hora del reloj](../HU-001-transcripcion-de-la-sesion.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El enganche existe y está corriendo ahora mismo: [`hook_historico.py`](../../../../../validadores/hook_historico.py) se dispara con cada mensaje del usuario y al terminar cada respuesta, y [`historico.py`](../../../../../validadores/historico.py) escribe el archivo y su línea en el índice. Esta misma sesión quedó escrita así. Sale de la fila de HU-001 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-001 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-001-transcripcion-de-la-sesion.md#ca-01--la-sesión-se-escribe-sola-desde-el-primer-intercambio) | La sesión se escribe sola, desde el primer intercambio | Corriendo, y es la exigencia que el `CLAUDE.md` del repositorio pone primero: la escribe el programa, no el agente |
| [CA-02](../HU-001-transcripcion-de-la-sesion.md#ca-02--cada-intercambio-lleva-su-hora-real) | Cada intercambio lleva su hora real | Corriendo: la hora la pone el reloj de la máquina. **Y es lo que evita el defecto que ya pasó seis veces**: el agente escribiendo la transcripción a mano con horas inventadas |
| [CA-03](../HU-001-transcripcion-de-la-sesion.md#ca-03--la-sesión-aparece-en-el-índice) | La sesión aparece en el índice | Corriendo, y con su caso difícil resuelto: renombrar la sesión mueve el archivo **y** corrige la línea del índice, cerrado en la fase B de [HU-008](../../HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/README.md) |

**Por qué una sola fase.** Los tres CA los cumple el mismo enganche en la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar en la especificación del módulo qué se le exige al enganche que escribe la sesión, y probarlo — incluido el caso que ya falló seis veces, que es el agente escribiendo la transcripción por su cuenta.

**Fuera de alcance:**

- **El resumen de la sesión,** que es [HU-008](../../HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) y ya tiene sus dos fases cerradas.
- **Enmascarar una clave pegada en el chat,** que es [HU-002](../../HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) y todavía no existe. Mientras no exista, lo que se pegue en el chat queda escrito tal cual.
- **Cambiar el enganche.** Si al probar aparece algo, se para y se propone.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: la transcripción de esta sesión existe, con su hora por intercambio, y su línea está en el índice.

**Lo que ya existe:** el enganche, en sus dos disparos —al mandar el mensaje y al terminar la respuesta—; el programa que escribe y mantiene el índice; la orden escrita en el `CLAUDE.md` del repositorio de que el agente **no** escriba la transcripción; y el renombrado, que mueve el archivo y corrige su línea.

**Lo que no existe:**

1. **El incremento en la especificación.** La del módulo cubre otros enganches; el de la transcripción no está.
2. **La prueba de que la hora la pone el reloj** y no el texto.
3. **El caso escrito del defecto conocido:** la transcripción escrita a mano, que pasó seis veces y está anotada en el pendiente [29](../../../../../pendientes/29-la-transcripcion-se-escribio-dos-veces.md).

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/automatismos/spec.md` | Modificar | Le entra el incremento del enganche de la transcripción |
| `validadores/pruebas.py` | Modificar | La prueba de la hora |
| `…/A-EP-005-HU-001-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-001-transcripcion-de-la-sesion.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni `hook_historico.py` ni `historico.py` se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas y documentación sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y no hace falta pedirlo:** el enganche corre solo con cada mensaje.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba de la hora se hace sobre el programa, no sobre una sesión real | Abrir una sesión y mirar la hora | Una sesión real da una sola hora; la prueba tiene que fallar si alguien toma la hora del texto |
| El defecto de la transcripción a mano se escribe como caso | Confiar en que la orden del `CLAUDE.md` alcanza | Pasó seis veces con la orden escrita: lo que falta es que se note cuando vuelve a pasar |
| El enganche no se toca | Mejorarlo de paso | Es lo que sostiene el registro de todas las sesiones: cambiarlo sin plan aprobado es tocar el único rastro que queda |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el enganche corre y su comportamiento se puede observar en esta misma sesión.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La sesión se escribe sola, desde el primer intercambio

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: abrir una sesión de prueba, mandar un mensaje y comprobar que el archivo nace con él | `plan_pruebas.md` | 2,0 |
| T-02 | Caso de prueba: la respuesta del agente queda escrita al terminar, sin que nadie lo pida | `plan_pruebas.md` | 1,5 |

### CA-02 — Cada intercambio lleva su hora real

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: la hora la pone el programa y no viene del texto del mensaje | `validadores/pruebas.py` | 2,0 |
| T-04 | Anotar en el resultado el defecto de la transcripción escrita a mano, con el pendiente [29](../../../../../pendientes/29-la-transcripcion-se-escribio-dos-veces.md) | `resultado_pruebas.md` | 1,0 |

### CA-03 — La sesión aparece en el índice

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: la sesión nueva aparece en el índice con su línea, y al renombrarla la línea sigue apuntando bien | `plan_pruebas.md` | 2,0 |

### RNF — Que el registro no dependa de que el agente se acuerde

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 6 tareas · 10,5 horas.**

---

## 4. Secuencia de ejecución

T-03 primero, que es la prueba corta. T-01 → T-02 → T-05 con una sesión de prueba. T-04 y T-06 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Sesión de prueba: el archivo nace con el primer mensaje | T-01, T-02 |
| CA-02 | Prueba de que la hora la pone el reloj, y la constancia del defecto conocido | T-03, T-04 |
| CA-03 | Línea en el índice, antes y después de renombrar | T-05 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: el enganche no se toca. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md), [`15`](../../../../../base/15-registros-inmutables.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la sesión de prueba ensucie el histórico del repositorio | Rastro falso entre las sesiones reales | La sesión de prueba corre contra una carpeta temporal, no contra `historico-chat/` |
| R-02 | Que la prueba de la hora quede atada al formato de fecha | Se rompe al cambiar el formato | Se comprueba que la hora venga del reloj, no cómo se ve escrita |
| R-03 | Que otra sesión esté escribiendo en el índice del histórico | Pisar trabajo ajeno | Se relee antes de escribir |

---

## 11. Definition of Done

- [ ] La especificación del módulo cubre el enganche de la transcripción.
- [ ] Está probado que la sesión nace con el primer mensaje y que la hora la pone el reloj.
- [ ] El caso de la transcripción escrita a mano quedó escrito.
- [ ] La línea del índice sobrevive a un renombrado.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
