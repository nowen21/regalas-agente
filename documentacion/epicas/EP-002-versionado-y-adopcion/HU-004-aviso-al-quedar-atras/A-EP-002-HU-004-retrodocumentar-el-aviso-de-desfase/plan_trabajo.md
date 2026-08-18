# Plan de Trabajo — Fase A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase (módulo Versionado y adopción)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-004](../HU-004-aviso-al-quedar-atras.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` |
| **Épica** | [EP-002 Versionado y adopción](../../epica.md) |
| **HU** | [HU-004 Avisar al abrir sesión cuando el proyecto quedó atrás](../HU-004-aviso-al-quedar-atras.md) — una sola (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | [HU-004](../HU-004-aviso-al-quedar-atras.md). El entregable es el mensaje de un enganche: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El aviso existe y sale solo: [`hook_sesion.py`](../../../../../validadores/hook_sesion.py) corre al abrir, [`version.py`](../../../../../validadores/version.py) decide el desfase y `validar.py version` lo dice en la línea de comandos. Sale de la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-004 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-004-aviso-al-quedar-atras.md#ca-01--el-proyecto-atrasado-recibe-el-aviso-al-abrir-sesión) | El proyecto atrasado recibe el aviso al abrir sesión | Corriendo, **pero incompleto**: el mensaje dice qué versión declara y cuál es la vigente, y no dice qué cambió entre las dos |
| [CA-02](../HU-004-aviso-al-quedar-atras.md#ca-02--el-proyecto-al-día-no-recibe-nada) | El proyecto al día no recibe nada | Cumplido: sin desfase, `comparar` no devuelve motivo. Sin prueba propia |
| [CA-03](../HU-004-aviso-al-quedar-atras.md#ca-03--el-aviso-no-migra-ni-detiene) | El aviso no migra ni detiene | Cumplido con una excepción escrita: la derogación sin adoptar **sí** detiene la fase ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) |

**Por qué una sola fase.** Los tres CA se comprueban corriendo el mismo enganche sobre tres proyectos en tres estados (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado el aviso en sus tres estados —atrasado, al día y con derogación sin adoptar— y decidir qué se hace con la parte del mensaje que la RN-02 pide y no está.

**Fuera de alcance:**

- **La declaración de la versión adoptada,** que es [HU-003](../../HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md).
- **Migrar un proyecto.** La RN-03 es explícita: informar y decidir son cosas distintas.
- **La comprobación de la derogación sin adoptar,** ya retro-documentada en [EP-004 · HU-015](../../../EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22/plan_trabajo.md). Acá se cita como línea base.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `version.py` y corriendo `validar.py version` sobre este repositorio.

**Lo que ya existe:** el enganche de apertura, que entrega el aviso en pantalla sin que nadie lo pida (RN-01); `comparar`, que devuelve motivo solo si la declarada es menor que la vigente, y nada si está al día (RN-04); el texto del aviso, que dice que subir es decisión del usuario y que las fases cerradas quedan selladas (RN-03); `sin_adoptar`, que separa las derogaciones que caen dentro del desfase.

**Lo que no existe:**

1. **El «qué cambió entre las dos» del mensaje** (RN-02). El aviso nombra las dos versiones y no el tramo del registro que las separa.
2. **La prueba de los tres estados.** Ninguna de las 246 pruebas cubre esta HU por su criterio de aceptación.
3. **La constancia de la excepción del CA-03.** Que la derogación sin adoptar detenga la fase está escrito en el `CHANGELOG` y en `F22`, y no en esta HU, que dice que el aviso no detiene.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `…/A-EP-002-HU-004-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-002-HU-004-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con lo que falta del mensaje |
| `validadores/pruebas.py` | Modificar | Pruebas de `comparar` en los tres estados |
| `HU-004-aviso-al-quedar-atras.md` | Modificar | §7 nombra esta fase; el CA-03 anota la excepción de `F22`; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `version.py` y `hook_sesion.py` no se tocan. Completar el mensaje es la duda 1.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna mientras no se toque el mensaje. Si la duda 1 resuelve completarlo, cambia el texto que `comparar` devuelve, y de eso dependen `validar.py version`, `hook_sesion.py` y las pruebas que lo citen: se declara antes de tocarlo.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un enganche de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El aviso **sí tiene** punto de entrada: sale en pantalla al abrir la sesión, sin que nadie lo pida, y también con `validar.py version`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las pruebas se escriben contra `comparar`, que es núcleo puro | Probar el enganche completo | `comparar` está aislado de disco a propósito, y probarlo ahí no necesita montar un proyecto |
| El CA-03 se cierra dejando escrita la excepción de `F22` | Marcarlo cumplido sin nombrarla | La HU dice «el aviso no detiene» y hay un caso en que sí: quien lea la HU tiene que encontrarlo |
| Completar el mensaje no se hace de oficio | Agregarle el tramo del registro al pasar | Cambia lo que ve el usuario en cada apertura de sesión: se propone y se decide |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si el aviso pasa a decir qué cambió entre las dos versiones, y con qué detalle — la lista de entradas del registro, o solo cuántas y de qué tipo | Usuario | Pendiente |

La duda 1 no bloquea las pruebas: bloquea solo el cambio del mensaje.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El proyecto atrasado recibe el aviso al abrir sesión

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Prueba: con versión declarada menor que la vigente, `comparar` devuelve motivo con las dos versiones | `validadores/pruebas.py` | 1,5 |
| T-02 | Dejar escrito que el mensaje no dice qué cambió entre las dos, y presentar la duda 1 con lo que costaría cada opción | `resultado_pruebas.md` | 1,5 |

### CA-02 — El proyecto al día no recibe nada

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: con la versión al día, `comparar` no devuelve nada; y sin versión declarada, devuelve el aviso de que falta fijarla | `validadores/pruebas.py` | 1,5 |

### CA-03 — El aviso no migra ni detiene

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Caso de prueba: con desfase, el trabajo sigue y nada se actualiza solo | `plan_pruebas.md` | 1,5 |
| T-05 | Caso de prueba de la excepción: con una derogación dentro del desfase, la fase **sí** se detiene | `plan_pruebas.md` | 1,5 |
| T-06 | Anotar la excepción en el CA-03 de la HU, con el enlace a `F22` | `HU-004-aviso-al-quedar-atras.md` | 1,0 |

### RNF — Que el aviso no se vuelva ruido

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Comprobar que el aviso sale una vez por apertura y no en cada mensaje | Legibilidad | 1,0 |
| T-08 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 8 tareas · 11,0 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-03 primero, que son núcleo puro. T-04 → T-05 después, con proyectos de prueba en carpeta temporal. T-02, T-06, T-07 y T-08 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Prueba de `comparar` con desfase, y la constancia de lo que al mensaje le falta | T-01, T-02 |
| CA-02 | Prueba de `comparar` al día y sin versión declarada | T-03 |
| CA-03 | Dos casos opuestos: con desfase simple sigue, con derogación se detiene | T-04, T-05 |
| RNF | Revisión de cuántas veces sale el aviso | T-07 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con un `CLAUDE.md` de mentira para cada estado, y este repositorio. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo que entra son pruebas y una anotación en la HU.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica mientras el mensaje no cambie. Si la duda 1 resuelve completarlo, la subida sería **MENOR**: el aviso diría más, sin obligar a nadie a hacer nada nuevo.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que completar el mensaje rompa pruebas que citan su texto | Suite roja | Solo se toca con la duda 1 resuelta y el plan ampliado | Abierto |
| R-02 | Que el CA-03 y `F22` se lean como contradicción | Confunde a quien abre una fase | La excepción queda escrita en la HU, no solo en la regla | Abierto |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio | Abierto |

---

## 11. Definition of Done

- [ ] Los tres estados del aviso tienen prueba: atrasado, al día y sin versión declarada.
- [ ] Está probado que el aviso no migra, y que la derogación sin adoptar sí detiene.
- [ ] El CA-03 de la HU nombra su excepción.
- [ ] Lo que al mensaje le falta quedó escrito, con la decisión planteada.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
