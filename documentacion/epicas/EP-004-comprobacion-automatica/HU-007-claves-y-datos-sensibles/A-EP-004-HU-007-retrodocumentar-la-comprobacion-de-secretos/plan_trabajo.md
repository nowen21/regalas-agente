# Plan de Trabajo — Fase A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-007](../HU-007-claves-y-datos-sensibles.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-007 Comprobar que no salgan claves ni datos sensibles](../HU-007-claves-y-datos-sensibles.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-007](../HU-007-claves-y-datos-sensibles.md). El entregable son programas de comprobación: sus criterios de aceptación, `00·N6` y `04·S4` son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). Los dos programas existen: [`secretos.py`](../../../../../validadores/secretos.py) busca claves incrustadas (`04·S4`) y [`versionado.py`](../../../../../validadores/versionado.py) busca lo que no debería estar versionado (`09·G3`), por `validar.py secretos` y `validar.py versionado`. Sale de la fila de HU-007 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-007 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-007-claves-y-datos-sensibles.md#ca-01--una-clave-escrita-en-el-código-se-reporta) | Una clave escrita en el código se reporta | Corriendo: `validar.py secretos`. Sin prueba propia de esta HU |
| [CA-02](../HU-007-claves-y-datos-sensibles.md#ca-02--un-archivo-que-no-debe-guardarse-se-reporta) | Un archivo que no debe guardarse se reporta | Corriendo: `validar.py versionado`. Sin prueba propia |
| [CA-03](../HU-007-claves-y-datos-sensibles.md#ca-03--un-ejemplo-no-se-confunde-con-una-clave) | Un ejemplo no se confunde con una clave | Es el caso que más duele: un falso positivo hace que el programa se ignore. Hay un acuerdo del usuario sobre datos de prueba sin secretos literales, y **sin prueba que lo fije** |

**Por qué una sola fase.** Los tres CA son la misma comprobación vista desde el acierto y desde el falso positivo (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que una clave se detecta, que un archivo que no debe versionarse se detecta, y que un ejemplo no se confunde con una clave — que es lo que decide si alguien le cree al programa.

**Fuera de alcance:**

- **Enmascarar la clave antes de que se escriba,** que es [EP-005 · HU-002](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) y todavía no existe.
- **El núcleo que lo prohíbe,** que es `00·N6` y ya tiene su fase en [EP-001 · HU-003](../../../EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/plan_trabajo.md).
- **Ampliar lo que el programa reconoce como clave.** Si en la prueba se le escapa un formato, se anota y se propone.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 corriendo los dos subcomandos sobre este repositorio: sin hallazgos.

**Lo que ya existe:** el programa que busca claves incrustadas y el que revisa qué está versionado; la regla blindada que lo prohíbe y la del capítulo de seguridad que lo detalla; el acuerdo de no usar secretos literales en los datos de prueba, que es lo que evita que la propia suite dispare el detector.

**Lo que no existe:**

1. **La prueba por criterio de esta HU,** en particular la del falso positivo.
2. **La lista escrita de qué se considera ejemplo.** Está dentro del programa; quien reciba un falso positivo no tiene dónde leer por qué.
3. **La constancia de qué formatos de clave reconoce** y cuáles no.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/docs/secretos.md` | Modificar | Le entra qué se considera clave y qué se considera ejemplo |
| `validadores/pruebas.py` | Modificar | Los tres casos de esta HU, si no están cubiertos |
| `…/A-EP-004-HU-007-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-007-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con los formatos reconocidos |
| `HU-007-claves-y-datos-sensibles.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ni `secretos.py` ni `versionado.py` se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas y documentación sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tienen punto de entrada:** `validar.py secretos` y `validar.py versionado`.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las claves de la prueba se arman y no se copian de ninguna parte | Usar una clave vieja ya rotada | Una clave real en el repositorio es una clave filtrada, aunque esté rotada ([`00·N6`](../../../../../base/00-nucleo-blindado.md)) |
| El caso del falso positivo pesa igual que los dos aciertos | Probar solo que detecta | Un detector con falsos positivos se apaga, y entonces no detecta nada |
| Lo que se le escape se anota | Ampliar el programa de paso | Ampliar el detector cambia lo que falla en todos los proyectos: se propone |

### 2.7 Dudas por resolver antes de escribir

Ninguna: todo lo que la fase afirma se verificó contra el repositorio.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una clave escrita en el código se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: una clave armada para la prueba, escrita en un archivo de una carpeta temporal, se reporta con su archivo y su línea | `plan_pruebas.md` | 2,0 |

### CA-02 — Un archivo que no debe guardarse se reporta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-02 | Caso de prueba: un archivo de configuración con secretos, puesto bajo control de versiones, se reporta | `plan_pruebas.md` | 1,5 |

### CA-03 — Un ejemplo no se confunde con una clave

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Caso de prueba: un ejemplo de documentación y un dato de prueba no se reportan | `plan_pruebas.md` | 2,0 |
| T-04 | Levantar la lista de lo que hoy se considera ejemplo y no clave, leída del programa | `resultado_pruebas.md` | 1,5 |

### RNF — Que nadie apague el detector por ruido

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 8,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02 primero. T-03 → T-04 después, que son el falso positivo y su lista. T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Clave armada en carpeta temporal | T-01 |
| CA-02 | Archivo con secretos puesto bajo control de versiones | T-02 |
| CA-03 | Ejemplo de documentación y dato de prueba, ninguno reportado | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: los programas no se tocan. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N6`](../../../../../base/00-nucleo-blindado.md), [`04`](../../../../../base/04-seguridad.md), [`09`](../../../../../base/09-git.md), [`12`](../../../../../base/12-privacidad-datos.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la clave armada quede escrita en el repositorio por error | Sería el propio defecto que la HU previene | Se crea y se borra en carpeta temporal, y la prueba comprueba que nada quedó |
| R-02 | Que al probar el falso positivo aparezcan varios en el repositorio | Se destapa trabajo | Se anotan; ajustar el detector se propone aparte |
| R-03 | Que la lista de formatos reconocidos quede vieja | Documento que miente | La lista se levanta del programa, y la prueba falla si dejan de coincidir |

---

## 11. Definition of Done

- [ ] Los tres casos están escritos y corridos, incluido el del falso positivo.
- [ ] Está escrito qué se considera clave y qué se considera ejemplo.
- [ ] Ninguna clave real ni armada quedó en el repositorio.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
