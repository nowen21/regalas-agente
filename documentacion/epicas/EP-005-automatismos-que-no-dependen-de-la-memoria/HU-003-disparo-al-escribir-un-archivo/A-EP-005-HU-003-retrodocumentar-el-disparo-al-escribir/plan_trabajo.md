# Plan de Trabajo — Fase A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-disparo-al-escribir-un-archivo.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-003 Disparar las comprobaciones al escribir un archivo](../HU-003-disparo-al-escribir-un-archivo.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md)). El enganche existe y corre con cada escritura: [`hook_md.py`](../../../../../validadores/hook_md.py) mira si el archivo es un documento del proyecto y, si lo es, corre las dos comprobaciones de enlaces; si no, no hace nada. Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-003-disparo-al-escribir-un-archivo.md#ca-01--al-escribir-un-archivo-corre-la-comprobación) | Al escribir un archivo corre la comprobación | Corriendo, y esta sesión lo probó sin querer: al escribir un plan con un enlace roto, el aviso llegó de inmediato |
| [CA-02](../HU-003-disparo-al-escribir-un-archivo.md#ca-02--lo-que-no-le-toca-se-ignora-en-silencio) | Lo que no le toca se ignora en silencio | Corriendo: si no es un documento, o está fuera de la carpeta revisada, no hace nada |
| [CA-03](../HU-003-disparo-al-escribir-un-archivo.md#ca-03--el-hallazgo-grave-detiene-el-resto-avisa) | El hallazgo grave detiene; el resto avisa | **A medias.** El enganche devuelve el detalle para que se arregle en el momento, y no distingue entre detener y avisar como sí lo hace la línea de comandos |

**Por qué una sola fase.** Los tres CA los cumple el mismo enganche, y el tercero solo se puede juzgar viendo los otros dos (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar en la especificación qué dispara el enganche, qué ignora y qué hace con cada severidad — y decir si el CA-03 se cumple o si falta algo.

**Fuera de alcance:**

- **Ampliar lo que el enganche comprueba.** Hoy corre las de enlaces; agregarle más es otra decisión.
- **El capítulo que rige lo que se escribe,** que es [HU-010](../../HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md) y usa el mismo disparo.
- **El formato del hallazgo,** que es [EP-004 · HU-003](../../../EP-004-comprobacion-automatica/HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md).

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo el enganche y su documentación, y viéndolo actuar al escribir los planes de esta sesión.

**Lo que ya existe:** el enganche, registrado para dispararse después de escribir o cambiar un archivo; su decisión de tres pasos —no es documento, está fuera de la carpeta, o sí le toca—; las dos comprobaciones de enlaces que corre; y la devolución del detalle al agente para que arregle en el momento en vez de dejarlo para después.

**Lo que no existe:**

1. **El incremento en la especificación** de este enganche.
2. **La prueba del silencio.** Que ignore lo que no le toca es la mitad de su valor —un enganche que habla siempre se ignora— y nadie lo comprueba por criterio de esta HU.
3. **La respuesta al CA-03.** Qué hace hoy con una falla frente a un aviso no está escrito en ninguna parte.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/automatismos/spec.md` | Modificar | El incremento del enganche de escritura |
| `validadores/pruebas.py` | Modificar | La prueba del silencio |
| `…/A-EP-005-HU-003-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-003-disparo-al-escribir-un-archivo.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `hook_md.py` no se toca. Si el CA-03 pide un cambio, se para y se propone.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas y documentación sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y no hace falta pedirlo:** corre después de cada escritura.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El CA-03 se responde midiendo, no cambiando | Ajustar el enganche para que detenga | Primero hay que saber qué hace; cambiar el enganche que corre en cada escritura sin plan aprobado es riesgoso |
| La prueba del silencio pesa igual que la del disparo | Probar solo que dispara | Un enganche que habla de más se apaga, y apagado no dispara nada |
| Los casos se arman en carpeta temporal | Escribir un enlace roto en el repositorio | Dejar el repositorio en rojo estorba a las demás sesiones |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el enganche corre y su comportamiento se puede observar.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Al escribir un archivo corre la comprobación

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: escribir un documento con un enlace roto y comprobar que el aviso llega en el momento | `plan_pruebas.md` | 1,5 |

### CA-02 — Lo que no le toca se ignora en silencio

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-02 | Prueba: con un archivo que no es documento, el enganche no reporta y no falla | `validadores/pruebas.py` | 1,5 |
| T-03 | Caso de prueba: un documento de otra carpeta no dispara nada | `plan_pruebas.md` | 1,0 |

### CA-03 — El hallazgo grave detiene; el resto avisa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Levantar qué hace hoy el enganche con una falla y con un aviso, y compararlo con lo que la HU pide | `resultado_pruebas.md` | 2,0 |
| T-05 | Caso de prueba: un enlace roto —que es falla— y un índice desactualizado, y qué pasa con cada uno | `plan_pruebas.md` | 2,0 |

### RNF — Que el enganche no se vuelva ruido

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 6 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-02 → T-03 primero, que son el silencio. T-01 y T-05 después. T-04 con lo que se vea, y T-06 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Documento con enlace roto, aviso inmediato | T-01 |
| CA-02 | Archivo que no es documento y documento de otra carpeta | T-02, T-03 |
| CA-03 | Falla y aviso comparados con lo que la HU pide | T-04, T-05 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica mientras el enganche no se toque. Si el CA-03 obliga a cambiarlo, sería **MAYOR**: cambiaría lo que pasa al escribir un archivo en cada proyecto instalado. Eso se propone, no se hace acá.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`05·E1`](../../../../../base/05-errores-y-logging.md), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que el CA-03 quede sin cumplir | La fila del inventario no cierra | Se escribe qué falta y se propone: es un resultado, no un fracaso |
| R-02 | Que las pruebas del enganche dependan de la herramienta que lo dispara | Prueba frágil | Se prueba la función que decide, que está separada a propósito del disparo |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio |

---

## 11. Definition of Done

- [ ] La especificación cubre qué dispara el enganche y qué ignora.
- [ ] Hay prueba de que lo que no le toca se ignora en silencio.
- [ ] Está escrito qué hace hoy con una falla y con un aviso, y si eso cumple el CA-03.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
