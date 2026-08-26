# Plan de Trabajo — Fase A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos (módulo Instalación)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-004](../HU-004-generar-los-automatismos.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-004 Generar y poner los automatismos](../HU-004-generar-los-automatismos.md) — una sola (`F12.1`) |
| **Módulo** | Instalación |
| **Especificación del módulo** | [HU-004](../HU-004-generar-los-automatismos.md). Los enganches tienen su especificación en [documentacion/automatismos/spec.md](../../../../automatismos/spec.md); lo que esta HU cubre es **ponerlos**, y eso son los criterios de aceptación de acá |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). Está en producción: [`instalar.py`](../../../../../validadores/instalar.py) registra los seis enganches —al abrir la sesión, al mandar un mensaje, al terminar la respuesta y después de escribir un archivo— y esos son los que sostienen la transcripción, el resumen, la memoria y la revisión de instalación. Sale de la fila de HU-004 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-004 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-004-generar-los-automatismos.md#ca-01--los-automatismos-quedan-puestos-y-corriendo) | Los automatismos quedan puestos y corriendo | Corriendo: los seis quedan registrados en la instalación. Sin prueba propia de esta HU |
| [CA-02](../HU-004-generar-los-automatismos.md#ca-02--si-uno-falla-el-trabajo-no-se-detiene) | Si uno falla, el trabajo no se detiene | Corriendo por diseño —la revisión de instalación dice explícitamente que no traba nada— y **sin prueba** |

**Por qué una sola fase.** Los dos CA se comprueban sobre la misma instalación y los mismos seis enganches (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar probado que los seis enganches quedan puestos, que cada uno corre cuando dice, y que ninguno puede detener el trabajo si falla.

**Fuera de alcance:**

- **Lo que hace cada enganche.** Eso es de EP-005, que tiene una HU por enganche.
- **Agregar enganches nuevos.** Los que puedan venir de otras fases se suman ahí, no acá.
- **Cambiar el instalador.** Si al probar aparece algo, se propone.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo la lista de enganches que el instalador registra: seis, en cuatro momentos distintos.

**Lo que ya existe:** el registro de los seis enganches; los cuatro momentos en que se disparan; el criterio escrito de que un aviso que sale siempre deja de leerse, que es por lo que la revisión de instalación se calla cuando no falta nada; y la declaración de que no traba nada, porque un proyecto a medio instalar igual puede tener trabajo urgente.

**Lo que no existe:**

1. **La prueba de que quedan puestos.**
2. **La prueba de que ninguno detiene el trabajo si falla.** Es la exigencia más importante y nadie la corre: un enganche que se cae en cada mensaje haría inutilizable la herramienta.
3. **La tabla de los seis** con su momento y su comportamiento ante el fallo, que hoy hay que reconstruir leyendo el instalador.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/pruebas.py` | Modificar | La prueba del enganche que falla |
| `…/A-EP-007-HU-004-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron, con la tabla de los seis |
| `HU-004-generar-los-automatismos.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `instalar.py` y los seis enganches no se tocan.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: se agregan pruebas sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque es un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

Los enganches no se piden: corren solos en sus cuatro momentos. Esta fase no lo cambia.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El fallo se simula, no se provoca rompiendo un enganche real | Romper uno a propósito en el repositorio | Romper un enganche del repositorio afecta a todas las sesiones abiertas |
| La tabla se levanta del instalador, no de la documentación | Copiarla de `docs/` | Lo que corre es lo que el instalador registra; la documentación puede estar vieja |
| El CA-02 se prueba con un fallo de verdad, no con un aviso | Comprobar solo que el aviso no trabe | Lo que hay que probar es el caso malo: el enganche que se cae |

### 2.7 Dudas por resolver antes de escribir

Ninguna: la instalación se puede correr sobre una carpeta temporal.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Los automatismos quedan puestos y corriendo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Caso de prueba: instalar en un proyecto de prueba y comprobar que los seis quedan registrados | `plan_pruebas.md` | 2,0 |
| T-02 | Caso de prueba: comprobar que cada uno se dispara en el momento que declara | `plan_pruebas.md` | 2,5 |

### CA-02 — Si uno falla, el trabajo no se detiene

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: con un enganche que falla, la sesión sigue y el fallo queda dicho | `validadores/pruebas.py` | 2,5 |
| T-04 | Levantar la tabla de los seis enganches con el momento en que corren y qué pasa si fallan | `resultado_pruebas.md` | 2,0 |

### RNF — Que ningún automatismo trabe el trabajo

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 5 tareas · 10,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02 primero. T-03 después, que es la prueba dura. T-04 al final, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Los seis registrados, y cada uno disparándose en su momento | T-01, T-02 |
| CA-02 | Enganche que falla con la sesión siguiendo, y la tabla de los seis | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Proyectos de prueba en carpetas temporales. No se instala ni se actualiza ningún proyecto vivo. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Las carpetas de prueba se borran al terminar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

No aplica: no se toca el instalador ni los enganches. Sin subida de versión.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N1`](../../../../../base/00-nucleo-blindado.md), [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), [`05·E1`](../../../../../base/05-errores-y-logging.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que un enganche sí detenga el trabajo al fallar | Defecto grave: la herramienta quedaría trabada | Se para y se reporta de inmediato |
| R-02 | Que probar los disparos exija abrir sesiones de verdad | Ruido en el histórico | Se prueba la función de cada enganche, que está separada del disparo |
| R-03 | Que la tabla de los seis quede vieja al agregar uno | Documento que miente | La tabla se levanta del instalador, y la prueba del CA-01 recorre lo que él registra |

---

## 11. Definition of Done

- [ ] Los seis enganches quedan registrados, con prueba.
- [ ] Cada uno se dispara en el momento que declara.
- [ ] Hay prueba de que un enganche que falla no detiene el trabajo y lo dice.
- [ ] La tabla de los seis está escrita, con su momento y su comportamiento ante el fallo.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
