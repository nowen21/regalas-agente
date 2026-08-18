# Plan de Trabajo — Fase B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-003 Definir el formato de un hallazgo y su severidad](../HU-003-formato-del-hallazgo.md) — una sola (`F12.1`) |
| **Complementa** | [`A-EP-004-HU-003`](../A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md), que cerró en **No cumple** |
| **Módulo** | Comprobación automática |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐞 **Defecto**. `comun.leer` abre sin red, así que **un `.md` que no sea UTF-8 tumba la corrida entera** con un `UnicodeDecodeError` de Python — y se lleva por delante todos los hallazgos ya encontrados. Comprobado corriendo `validar.py estandar` sobre un árbol con un archivo mal codificado: termina en 1, sin una sola línea de salida útil.

**CA de la HU que cubre esta fase**

| Exigencia de HU-003 | Qué exige | Estado tras la fase A |
|---|---|---|
| Transversal · **Errores** | El archivo que no se puede leer produce **un mensaje entendible, no un volcado técnico** | **En «No».** Produce una traza de Python y la corrida muere |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que un archivo ilegible se convierta en un hallazgo y no en el final de la corrida.

**Fuera de alcance:**

- **Adivinar la codificación.** Si no es UTF-8, se reporta; no se intenta reparar.
- **Cambiar el formato del hallazgo.** Lo que la fase A verificó no se toca.
- **Los demás validadores.** El arreglo va en el punto común por el que todos leen.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `validadores/comun.py` y reproduciendo el caso.

**Lo que ya existe:** `comun.leer(ruta)`, tres líneas, que abre en UTF-8 y devuelve el texto; la usan **todos los validadores menos dos**; y la prueba en rojo esperado `test_errores_el_archivo_que_no_se_puede_leer_no_vuelca_la_excepcion`.

**Lo que no existe:** cualquier red alrededor de esa lectura. Ni para el archivo que no está, ni para el que no se puede decodificar, ni para el que no se puede abrir por permisos.

> **Ya hay un archivo del repositorio que la esquiva:** `validadores/pendientes.py`, nacido el mismo día, usa su propia lectura porque necesitaba correr sobre una carpeta sin índice. Eso es la señal de que el hueco molesta a quien construye.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/comun.py` | Modificar | `leer()` tolera el archivo ausente, el ilegible y el mal codificado |
| `validadores/docs/comun.md` | Modificar | El contrato de la salida dice qué pasa con el archivo que no se puede leer |
| `validadores/pruebas.py` | Modificar | Destapar la prueba en rojo, y sumar el caso de la corrida completa sobre un árbol con un archivo roto |
| `validadores/pendientes.py` | Modificar | Vuelve a usar `comun.leer`, que era lo que quería |
| `…/B-EP-004-HU-003-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-003-formato-del-hallazgo.md` | Modificar | §8 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | La fila de HU-003 vuelve a quedar completa |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

**`comun.leer` la usan casi todos los validadores.** Cambiar qué hace ante un archivo ilegible cambia el comportamiento de todos — y esa es la intención: hoy todos se caen igual. **La firma no cambia** y el caso feliz devuelve lo mismo, así que ninguno necesita tocarse.

**El único que cambia a propósito es `pendientes.py`**, que deja su lectura propia.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: son programas de línea de comandos sobre archivos del repositorio.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

Ninguno nuevo. Lo que cambia es qué imprime `validar.py` cuando encuentra un archivo que no puede leer.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `leer()` devuelve **cadena vacía** y el validador que la llamó decide | Que `leer()` devuelva un `Hallazgo` | `leer()` no sabe qué regla se estaba comprobando; devolver un hallazgo la obligaría a inventar el mensaje |
| El archivo ilegible **se reporta**, no se salta en silencio | Ignorarlo | Un archivo que nadie puede leer es un problema del repositorio, no del validador. Saltarlo lo escondería |
| Se reporta como **aviso**, no como falla | Falla | No se sabe si el archivo importa. Un binario con extensión `.md` es raro, no necesariamente un incumplimiento — y `HU-003` ya decidió que lo dudoso avisa |
| Se lee con `errors="replace"` y **se dice que se reemplazaron caracteres** | Fallar al primer byte raro | Un acento mal codificado no puede impedir comprobar los enlaces del resto del archivo |

### 2.7 Dudas por resolver antes de escribir

Ninguna. El caso está reproducido y el criterio de severidad lo fija la propia HU.

---

## 3. Desglose de tareas por criterio de aceptación

### Transversal · Errores — El archivo que no se puede leer da un mensaje entendible

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | `leer()` tolera el archivo ausente, el de permisos y el mal codificado, y devuelve cadena vacía | `validadores/comun.py` | 1,5 |
| T-02 | Que quien lea pueda saber que la lectura falló, sin cambiar la firma | `validadores/comun.py` | 1,5 |
| T-03 | Que la corrida reporte el archivo ilegible como aviso, con su ruta | `validadores/comun.py` | 1,5 |
| T-04 | Destapar `test_errores_el_archivo_que_no_se_puede_leer_no_vuelca_la_excepcion` | `validadores/pruebas.py` | 0,5 |
| T-05 | Caso: `validar.py estandar` sobre un árbol con un `.md` mal codificado termina en 0 **y reporta los demás hallazgos** | `validadores/pruebas.py` | 2,0 |

### No regresión

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | `pendientes.py` vuelve a usar `comun.leer` | `validadores/pendientes.py` | 0,5 |
| T-07 | Escribir en el contrato qué pasa con el archivo que no se puede leer | `validadores/docs/comun.md` | 1,0 |
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 10,0 horas.**

---

## 4. Secuencia de ejecución

T-01 primero, que es el arreglo. T-02 y T-03 lo completan: sin ellos, el archivo roto se saltaría en silencio, que es la otra forma de esconderlo. T-04 destapa. T-05 es el caso que importa —**la corrida sigue y reporta lo demás**—. T-06 y T-07 limpian. T-08 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| Exigencia | Método de verificación | Evidencia |
|---|---|---|
| Transversal · Errores | Correr `validar.py estandar` sobre un árbol con un archivo mal codificado y leer la salida | T-05 |
| No regresión | La suite entera, y `validar.py estandar` sobre este repositorio | T-08 |

---

## 6. Datos y ambiente de prueba

Árboles temporales con archivos rotos armados para la prueba. **Ningún archivo del repositorio se rompe**: el caso se monta aparte ([`08·T4`](../../../../../base/08-pruebas.md)).

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo que cambia es una función de tres líneas y el archivo que la esquivaba; deshacerlo devuelve el comportamiento anterior.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No hay datos que migrar. El cambio es **aditivo en seguridad**: donde antes la corrida moría, ahora sigue y avisa. Un proyecto sin archivos rotos no nota nada.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`05·E1`](../../../../../base/05-errores-y-logging.md), [`08·T4`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que tolerar la lectura esconda un archivo que de verdad importa | Un defecto pasa callado | Por eso T-03: se reporta con su ruta. Tolerar no es callar | Abierto |
| R-02 | Que `errors="replace"` haga que un enlace roto pase por bueno | Falso negativo | Se anota en el aviso que el archivo se leyó con reemplazos, para que quien lo lea sepa que ese archivo no se revisó entero | Abierto |
| R-03 | Que cambiar `leer()` rompa un validador que dependía de que lanzara | Regresión | La suite entera es la red: 357 pruebas la usan de forma indirecta | Abierto |

---

## 11. Definition of Done

- [ ] Un `.md` mal codificado **no tumba la corrida**, y los demás hallazgos se reportan igual.
- [ ] El archivo ilegible sale como aviso, con su ruta y sin volcado técnico.
- [ ] `pendientes.py` vuelve a usar `comun.leer`.
- [ ] El contrato de la salida dice qué pasa con el archivo que no se puede leer.
- [ ] La prueba de fallo esperado queda en verde **sin la marca**.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §8 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
