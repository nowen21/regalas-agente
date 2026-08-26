# Plan de Trabajo — Fase A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-007](../HU-007-recoger-lo-guardado-por-fuera.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-007 Recoger al abrir sesión lo que quedó guardado por fuera del repositorio](../HU-007-recoger-lo-guardado-por-fuera.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El enganche existe y corre al abrir la sesión y con cada escritura: [`hook_recuerdos.py`](../../../../../validadores/hook_recuerdos.py) recoge lo que quedó en el almacén local de la herramienta y lo mueve al repositorio, como exige `01·C19`. Sale de la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-007 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-007-recoger-lo-guardado-por-fuera.md#ca-01--lo-guardado-por-fuera-se-recoge-al-abrir-sesión) | Lo guardado por fuera se recoge al abrir sesión | Corriendo: el enganche está registrado al abrir la sesión y después de cada escritura |
| [CA-02](../HU-007-recoger-lo-guardado-por-fuera.md#ca-02--nada-se-pisa) | Nada se pisa | Corriendo, y es la mitad delicada: recoger sin pisar lo que el usuario ya escribió en el repositorio |

**Por qué una sola fase.** Los dos CA los cumple el mismo enganche en la misma corrida (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar en la especificación qué recoge el enganche, de dónde y con qué cuidado, y probar que no pisa lo que ya está escrito.

**Fuera de alcance:**

- **Qué se guarda como recuerdo y con qué forma,** que es de EP-006.
- **La regla que obliga a que la memoria viva en el repositorio,** que es `01·C19` y tiene su fase en [EP-001 · HU-004](../../../EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia/plan_trabajo.md).
- **Cambiar el enganche.** Si al probar aparece algo, se para y se propone.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: el enganche está registrado en los dos momentos, y el índice de la memoria del repositorio lo dice explícitamente — «lo mueve el programa, no el agente».

**Lo que ya existe:** el enganche, en sus dos disparos; el índice de la memoria del repositorio, que declara que el almacén local queda vacío y por qué —dos versiones del mismo recuerdo terminan diciendo cosas distintas, y la que manda es la que nadie puede leer—; y la regla que lo exige.

**Lo que no existe:**

1. **El incremento en la especificación** de este enganche.
2. **La prueba de que no pisa.** Es lo que separa recoger de destruir, y nadie lo comprueba por criterio de esta HU.
3. **El caso del choque de nombres.** Dos recuerdos con el mismo nombre y contenido distinto no está resuelto por escrito.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `documentacion/automatismos/spec.md` | Modificar | El incremento del recogido |
| `validadores/pruebas.py` | Modificar | La prueba de que no pisa |
| `…/A-EP-005-HU-007-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-007-recoger-lo-guardado-por-fuera.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `hook_recuerdos.py` y `recuerdos.py` no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas y documentación sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y no hace falta pedirlo:** corre al abrir la sesión y después de cada escritura.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El caso del choque de nombres se prueba y se escribe, no se cambia | Ajustar el programa para resolverlo | Primero hay que saber qué hace hoy; cambiar el recogido puede perder un recuerdo |
| La prueba usa un almacén local de mentira | Probar con el almacén real de la máquina | El almacén real tiene lo del usuario: una prueba no lo toca |
| El CA-02 se prueba con contenido distinto, no solo con el mismo nombre | Comprobar solo que no duplique | Pisar es sobrescribir contenido, y con el mismo texto no se notaría |

### 2.7 Dudas por resolver antes de escribir

Ninguna: el enganche corre y su comportamiento se puede observar.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Lo guardado por fuera se recoge al abrir sesión

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: un recuerdo puesto en el almacén local aparece en el repositorio al abrir | `plan_pruebas.md` | 2,0 |
| T-02 | Caso de prueba: el almacén local queda vacío después — ni el texto ni un puntero | `plan_pruebas.md` | 1,5 |

### CA-02 — Nada se pisa

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: con un recuerdo que ya existe en el repositorio, el recogido no lo sobrescribe | `validadores/pruebas.py` | 2,0 |
| T-04 | Caso de prueba: dos recuerdos con el mismo nombre y contenido distinto, y qué hace el programa | `plan_pruebas.md` | 1,5 |

### RNF — Que recoger no sea destruir

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 5 tareas · 9,0 horas.**

---

## 4. Secuencia de ejecución

T-03 primero, que es la prueba dura. T-01 → T-02 → T-04 después. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Recuerdo en el almacén local, presente en el repositorio y ausente del almacén | T-01, T-02 |
| CA-02 | Recuerdo existente que no se sobrescribe, y el choque de nombres | T-03, T-04 |

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

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`01·C19`](../../../../../base/01-conducta.md), [`15`](../../../../../base/15-registros-inmutables.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la prueba toque el almacén real de la máquina | Se perdería un recuerdo del usuario | Se usa un almacén de mentira en carpeta temporal, declarado como condición de arranque |
| R-02 | Que el choque de nombres resulte mal resuelto hoy | Se destapa un defecto | Se anota y se propone: perder un recuerdo es grave y merece su propia fase |
| R-03 | Que otra sesión esté tocando `validadores/pruebas.py` | Pisar trabajo ajeno | Se guarda solo lo propio |

---

## 11. Definition of Done

- [ ] La especificación cubre qué recoge el enganche y de dónde.
- [ ] Está probado que un recuerdo del almacén local llega al repositorio y que el almacén queda vacío.
- [ ] Está probado que no se pisa un recuerdo con contenido distinto.
- [ ] El caso del choque de nombres quedó escrito, con lo que el programa hace hoy.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
