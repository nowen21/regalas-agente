# Plan de Trabajo — Fase B-EP-004-HU-002-el-analizador-ve-todas-las-reglas (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-002 Marcar en cada regla si es comprobable](../HU-002-marca-de-comprobable-en-cada-regla.md) — una sola (`F12.1`) |
| **Complementa** | [`A-EP-004-HU-002`](../A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla/resultado_pruebas.md), que cerró en **No cumple** |
| **Módulo** | Comprobación automática |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐞 **Defecto**, doble. `metareglas.reglas()` solo reconoce las reglas escritas como `## `, así que **las cuatro del capítulo 16 —escritas con `###`— no existen para el programa**: nunca se les aplicó ninguna de las 20 filas del checklist, y todo salió en verde. Y `metareglas.py` **no tiene subcomando** en `validar.py`, así que ni siquiera corre en el trabajo normal.

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado tras la fase A |
|---|---|---|
| [CA-01](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-01--toda-regla-aparece-clasificada) | **Toda** regla aparece clasificada | **En «No».** De las que el analizador ve, ninguna falta; cuatro no las ve |
| [CA-03](../HU-002-marca-de-comprobable-en-cada-regla.md#ca-03--una-regla-nueva-no-se-publica-sin-clasificar) | Una regla nueva **no se publica** sin clasificar | **En «No».** Avisa, no detiene, y no corre |

**Cierra además el punto 2 del [pendiente 53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)**, que ya estaba abierto.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el analizador vea todas las reglas escritas, y que la comprobación se pueda correr y detenga cuando falta clasificar.

**Fuera de alcance:**

- **Reescribir el capítulo 16** para que use `##`. Cambiar `base/` para acomodar al programa es al revés: el programa se adapta a lo escrito.
- **Los otros validadores sin punto de entrada.** El pendiente 53 tiene más puntos; acá se cierra el 2.
- **Clasificar reglas.** Si al verlas aparecen sin clasificar, se listan: clasificarlas es de `EP-001 · HU-009`.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 corriendo `metareglas.validar()` y contando los encabezados del árbol.

**Lo que ya existe:** `metareglas.validar()`, con sus 20 filas de checklist; el registro `reglas-validables.md` con 205 entradas; y **dos pruebas en rojo esperado**, `test_el_analizador_ve_todas_las_reglas_escritas_en_base` y `test_la_regla_sin_clasificar_detiene_la_publicacion`.

**Lo medido:** **200** reglas reconocidas, **4** escritas con `###` —todas del capítulo 16— y **5** sub-reglas de `F12` escritas como viñeta. Ninguna de las nueve pasa por el checklist.

**Lo que no existe:**

1. Que el analizador reconozca `###` y las sub-reglas en viñeta.
2. Un subcomando que corra `metareglas.py`.
3. Que la regla sin clasificar sea **falla** y no aviso.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/metareglas.py` | Modificar | `reglas()` reconoce `###` y las sub-reglas; la fila 18 pasa a falla |
| `validadores/validar.py` | Modificar | Su subcomando `metareglas` |
| `validadores/docs/metareglas.md` | Nuevo | Qué mira, qué no, y qué cuenta como regla |
| `validadores/pruebas.py` | Modificar | Destapar las dos pruebas, y sumar los casos de las formas de escribir una regla |
| `validadores/reglas-validables.md` | Modificar | **Solo si** al ver las nueve aparecen sin clasificar |
| `…/B-EP-004-HU-002-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-002-marca-de-comprobable-en-cada-regla.md` | Modificar | §8 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md` | Modificar | Su punto 2 queda cerrado |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

`metareglas.reglas()` la usan `validar()`, `validar_catalogo()` y **las pruebas de tres fases distintas** —la clasificación, la derogación y el molde—. Ampliar qué reconoce **hace que esas tres vean más reglas**, y eso puede destapar hallazgos nuevos: es la intención.

**Lo que hay que vigilar:** que las pruebas de la derogación sigan pasando. Reconocen las derogadas por su marca, y las sub-reglas `F4.x` derogadas van a entrar al conjunto.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Nace uno:** `python validadores/validar.py metareglas`. Es la mitad del defecto.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El programa se adapta a lo escrito**, no al revés | Reescribir el capítulo 16 con `##` | Cambiar `base/` para acomodar al analizador invierte quién manda. Y el día que alguien escriba otra regla con `###`, el defecto vuelve |
| La regla sin clasificar pasa a **falla** | Dejarla en aviso | El CA-03 dice «no se publica sin clasificar». Un aviso no impide publicar nada |
| Si al ver las nueve aparecen sin clasificar, **se listan y no se clasifican acá** | Clasificarlas de paso | Clasificar es de `EP-001 · HU-009`, y decidir si una regla es validable no es trabajo de una fase que arregla un analizador |
| El subcomando se llama `metareglas`, como el archivo | Meterlo dentro de `estandar` | `estandar` ya hace tres cosas; una cuarta la vuelve inseguible, y el pendiente 53 pide poder correrla sola |

### 2.7 Dudas por resolver antes de escribir

Ninguna. Las nueve reglas invisibles están identificadas una por una y el criterio de severidad lo fija el propio CA-03.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Toda regla aparece clasificada

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | `reglas()` reconoce las escritas con `###` | `validadores/metareglas.py` | 2,0 |
| T-02 | `reglas()` reconoce las sub-reglas escritas como viñeta | `validadores/metareglas.py` | 2,0 |
| T-03 | Destapar `test_el_analizador_ve_todas_las_reglas_escritas_en_base` | `validadores/pruebas.py` | 0,5 |
| T-04 | Listar las que aparezcan sin clasificar al verlas, **sin clasificarlas** | `resultado_pruebas.md` | 1,0 |

### CA-03 — Una regla nueva no se publica sin clasificar

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Su subcomando en `validar.py` | `validadores/validar.py` | 1,0 |
| T-06 | La fila 18 pasa de aviso a **falla** | `validadores/metareglas.py` | 1,0 |
| T-07 | Destapar `test_la_regla_sin_clasificar_detiene_la_publicacion` | `validadores/pruebas.py` | 0,5 |

### No regresión

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-08 | Caso: las derogadas siguen sin que se les reclame nada, ahora que hay más a la vista | `validadores/pruebas.py` | 1,5 |
| T-09 | Escribir qué mira, qué no, y qué cuenta como regla | `validadores/docs/metareglas.md` | 1,5 |
| T-10 | Cerrar el punto 2 del pendiente 53, y correr y cerrar la trazabilidad | Cierre | 1,5 |

**Total: 10 tareas · 12,5 horas.**

---

## 4. Secuencia de ejecución

T-01 y T-02 amplían lo que se ve. T-03 destapa **después**. T-04 mira qué apareció, **sin arreglarlo**. T-05 y T-06 encienden la puerta, y T-07 la destapa. T-08 es la red: ampliar el conjunto mete las derogadas, y hay que comprobar que no se les reclama nada. T-09 y T-10 cierran.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| Exigencia | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Contar las reglas que el analizador ve contra los encabezados de regla del árbol | T-03, T-04 |
| CA-03 | Escribir una regla sin clasificar en copia y correr el subcomando | T-07 |
| No regresión | Las derogadas, el molde y la clasificación existente | T-08 |

---

## 6. Datos y ambiente de prueba

Árboles temporales para el caso de la regla sin clasificar. **No se escribe ninguna regla de mentira en `base/`**, ni un minuto ([`08·T4`](../../../../../base/08-pruebas.md)).

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Deshacerlo devuelve el analizador corto y el aviso, y no deja datos que restaurar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

**Sube MAYOR:** la regla sin clasificar pasa a detener. Un proyecto que herede el estándar y escriba reglas propias sin clasificar empieza a reprobar.

**Lo que amortigua:** que hoy, sobre este repositorio, no hay ninguna sin clasificar entre las que el analizador ve. Lo que puede aparecer son las nueve que estaban invisibles — y por eso T-04 las lista antes de encender la falla.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T4`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que al ver nueve reglas más aparezcan decenas de hallazgos nuevos del checklist | La corrida se llena de rojo | **Es lo que se busca**: llevan versiones sin comprobarse. Se listan y se decide qué hacer, sin taparlos |
| R-02 | Que las derogadas entren al conjunto y se les empiece a reclamar | Falso incumplimiento | T-08 es la red. La fila 18 ya salta las derogadas; hay que comprobar que sigue haciéndolo |
| R-03 | Que la falla nueva bloquee a un proyecto heredero por sus propias reglas | Se bloquea trabajo ajeno | Sube MAYOR y el aviso de desfase lo informa. Y `validar_catalogo` ya distingue el catálogo del proyecto |
| R-04 | Que reconocer viñetas meta texto que no es una regla | Ruido | El patrón exige la forma completa del identificador, y T-02 trae su caso negativo |

---

## 11. Definition of Done

- [ ] El analizador ve las cuatro reglas del capítulo 16 y las sub-reglas en viñeta.
- [ ] Lo que aparezca sin clasificar queda **listado**, no clasificado a la carrera.
- [ ] `validar.py metareglas` existe y corre.
- [ ] La regla sin clasificar **detiene**.
- [ ] Las derogadas siguen sin que se les reclame nada.
- [ ] Está escrito qué cuenta como regla para el analizador.
- [ ] El punto 2 del pendiente 53 queda cerrado.
- [ ] `CHANGELOG` y `VERSION` con la subida **MAYOR** (`20·M10`).
- [ ] §8 de la HU nombra esta fase.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
