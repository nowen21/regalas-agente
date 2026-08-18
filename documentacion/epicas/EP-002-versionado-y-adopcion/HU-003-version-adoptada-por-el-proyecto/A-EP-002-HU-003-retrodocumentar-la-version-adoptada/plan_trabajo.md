# Plan de Trabajo — Fase A-EP-002-HU-003-retrodocumentar-la-version-adoptada (módulo Versionado y adopción)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-003](../HU-003-version-adoptada-por-el-proyecto.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` |
| **Épica** | [EP-002 Versionado y adopción](../../epica.md) |
| **HU** | [HU-003 Declarar en el proyecto la versión adoptada y la fecha](../HU-003-version-adoptada-por-el-proyecto.md) — una sola (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | [HU-003](../HU-003-version-adoptada-por-el-proyecto.md). El entregable es una declaración en el proyecto y el programa que la lee: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-002-HU-003-retrodocumentar-la-version-adoptada` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). La declaración existe y se usa: la línea «Versión del estándar adoptada» del [`CLAUDE.md.plantilla`](../../../../../plantillas/CLAUDE.md.plantilla), leída por [`version.py`](../../../../../validadores/version.py), y el historial de adopciones en [`documentacion/versiones/`](../../../../versiones/README.md), que escribe [`instalar.py`](../../../../../validadores/instalar.py). Sale de la fila de HU-003 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-003 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-003-version-adoptada-por-el-proyecto.md#ca-01--el-proyecto-declara-su-versión-y-su-fecha) | El proyecto declara su versión y su fecha | Corriendo: `validar.py version` la lee y avisa si falta. Sin prueba propia de esta HU |
| [CA-02](../HU-003-version-adoptada-por-el-proyecto.md#ca-02--una-versión-que-no-existe-se-detecta) | Una versión que no existe se detecta | **A medias.** `version.py` compara con la vigente; que la declarada exista en el registro no lo comprueba nadie |
| [CA-03](../HU-003-version-adoptada-por-el-proyecto.md#ca-03--queda-el-historial-de-adopciones) | Queda el historial de adopciones | Cumplido en forma, roto en contenido: los pendientes [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md) están abiertos sobre ese registro |

**Por qué una sola fase.** Los tres CA se comprueban sobre la misma declaración y el mismo registro de adopciones (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar comprobado que la declaración se lee, que una versión inventada se detecta y que el historial de adopciones sirve para saber bajo qué reglas se cerró cada trabajo.

**Fuera de alcance:**

- **Arreglar el contenido del registro de adopciones.** Los pendientes [44](../../../../../pendientes/hecho/el-registro-no-se-escribe-si-no-cambia-la-huella.md) y [46](../../../../../pendientes/hecho/el-registro-se-escribe-antes-de-contarse.md) ya lo tienen planteado; esta fase mide y no corrige.
- **El aviso al abrir sesión,** que es [HU-004](../../HU-004-aviso-al-quedar-atras/HU-004-aviso-al-quedar-atras.md).
- **El sello del trabajo cerrado,** que es [HU-005](../../HU-005-sellar-el-trabajo-cerrado/HU-005-sellar-el-trabajo-cerrado.md).
- **Adoptar una versión en algún proyecto.** La RN-04 dice que adoptar es decisión de la persona.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 corriendo `validar.py version` y leyendo el índice de adopciones.

**Lo que ya existe:** la línea de la versión adoptada en el `CLAUDE.md` que instala la plantilla; [`version.py`](../../../../../validadores/version.py) con `extraer_adoptada` y `comparar`; el índice de [`documentacion/versiones/`](../../../../versiones/README.md), con una adopción registrada (`15.0.0`, del 2026-08-14), que se versiona con el proyecto justo para que no se quede en una sola máquina.

**Lo que no existe:**

1. **La comprobación de que la versión declarada exista en el registro** (RN-02). Hoy se compara contra la vigente, no contra la lista de versiones que existieron.
2. **La prueba de esta HU.** Que `validar.py version` corra no es lo mismo que tener un caso escrito por criterio de aceptación.
3. **Un registro de adopciones confiable.** Su apartado de pendientes se calcula antes de escribirlo y se lista a sí mismo como faltante — el pendiente 46.

**Un caso a la mano:** este mismo repositorio no declara versión adoptada, y `validar.py version` lo reporta como aviso. Es correcto que no la declare —el estándar no se adopta a sí mismo— y el aviso no lo distingue: queda como hallazgo del CA-01.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `…/A-EP-002-HU-003-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-002-HU-003-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con el caso del propio repositorio |
| `validadores/pruebas.py` | Modificar | Prueba: una versión declarada que no existe en el registro se detecta |
| `HU-003-version-adoptada-por-el-proyecto.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni `version.py` ni `instalar.py` se tocan. Si la prueba del CA-02 exige cambiarlos, se para y se propone.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna mientras la prueba se escriba contra la interfaz que `version.py` ya expone. Si hiciera falta una función nueva ahí, se amplía el plan antes de tocarlo.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos y archivos de texto.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. La declaración se lee en el `CLAUDE.md` del proyecto, y el aviso lo entrega el enganche de apertura de sesión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El caso del estándar que no se adopta a sí mismo queda como hallazgo, no como corrección | Silenciar el aviso acá | Silenciar un aviso es cambiar un validador, y eso se decide con el plan ampliado |
| La lista de versiones que existieron se lee del `CHANGELOG` | Mantener una lista aparte | Dos listas de lo mismo se separan solas |
| El registro de adopciones se mide, no se arregla | Arreglarlo de paso | Ya tiene sus dos pendientes abiertos, y uno de ellos lo reportó otro proyecto |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Sobre qué proyecto instalado se prueban el CA-01 y el CA-03 | Usuario | Pendiente |

La duda 1 bloquea T-01 y T-05. El CA-02 no depende de ella.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El proyecto declara su versión y su fecha

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: en el proyecto elegido, `validar.py version` lee la versión declarada y su fecha | `plan_pruebas.md` | 1,5 |
| T-02 | Dejar escrito el caso del propio estándar, que no declara versión y recibe aviso igual | `resultado_pruebas.md` | 1,0 |

### CA-02 — Una versión que no existe se detecta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: una versión declarada que no está en el registro se detecta | `validadores/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: declarar en copia una versión inventada y comprobar qué reporta hoy | `plan_pruebas.md` | 1,5 |

### CA-03 — Queda el historial de adopciones

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Caso de prueba: por una fase cerrada del proyecto elegido, decir bajo qué versión cerró usando solo el historial | `plan_pruebas.md` | 2,0 |
| T-06 | Anotar contra los pendientes 44 y 46 lo que se encuentre mal en el registro | `resultado_pruebas.md` | 1,0 |

### RNF — Que la declaración se versione con el proyecto

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Comprobar que el registro de adopciones vive en carpeta versionada y no en la que se queda en una máquina | Trazabilidad | 1,0 |
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 11,5 horas.**

---

## 4. Secuencia de ejecución

T-03 → T-04 primero: no dependen de la duda. T-01, T-05 y T-07 detrás de la duda 1. T-02, T-06 y T-08 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). El proyecto de prueba se trabaja en copia.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Corrida de `validar.py version` sobre el proyecto elegido | T-01, y la constancia de T-02 |
| CA-02 | Prueba automática más la declaración inventada en copia | T-03, T-04 |
| CA-03 | Reconstruir con qué versión cerró una fase, usando solo el historial | T-05, T-06 |
| RNF | Revisión de dónde vive el registro | T-07 |

---

## 6. Datos y ambiente de prueba

Copia local del proyecto que decida la duda 1, y este repositorio. No se escribe en la carpeta viva de ningún proyecto ajeno ([`00·N4`](../../../../../base/00-nucleo-blindado.md)). Ninguna clave real.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo único ejecutable que entra es una prueba. La copia del proyecto se borra al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no cambia nada de lo instalado. Sin subida de versión, porque no se toca `base/` ni `plantillas/`.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N4`](../../../../../base/00-nucleo-blindado.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea dos CA de tres | Elegir el proyecto con el usuario | Abierto |
| R-01 | Que el CA-02 no se pueda cerrar sin tocar `version.py` | Se sale del alcance | Se para y se propone con el plan ampliado | Abierto |
| R-02 | Que el registro de adopciones del proyecto elegido esté con el defecto del 46 | El CA-03 quedaría probado sobre un registro que se contradice | Se prueba igual y se anota: es la evidencia que ese pendiente necesita | Abierto |
| R-03 | Tocar por error la carpeta viva del proyecto de prueba | Daño en trabajo ajeno | Se trabaja en copia, declarado como condición de arranque | Abierto |

---

## 11. Definition of Done

- [ ] Los tres CA tienen su caso escrito y corrido.
- [ ] Una versión declarada que no existe se detecta, con prueba.
- [ ] Se pudo decir bajo qué versión cerró una fase usando solo el historial.
- [ ] Lo que esté mal en el registro quedó anotado en los pendientes 44 y 46.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
