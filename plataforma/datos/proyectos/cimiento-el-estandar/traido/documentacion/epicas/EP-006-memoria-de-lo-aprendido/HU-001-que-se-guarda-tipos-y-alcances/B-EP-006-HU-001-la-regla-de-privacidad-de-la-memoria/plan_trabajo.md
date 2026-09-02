# Plan de Trabajo — Fase `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` |
| **Épica** | [EP-006](../../epica.md) |
| **HU** | [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md), **una sola** (`F12.1`) |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el criterio transversal de privacidad**, que dejó la fase [`A`](../A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance/resultado_pruebas.md) en «No cumple» el 2026-08-17. Los dos criterios numerados quedaron verificados; lo que faltaba era que alguna regla dijera que en la memoria no van datos personales ni claves, y **no había ninguna**.

**Es un rojo de los que no se cierran midiendo.** Escribir una regla del estándar es fijar norma, y eso lo decide el usuario (`01·C4`). Estuvo trece días esperando esa decisión, que llegó el 2026-08-30.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla que el criterio pedía, por el procedimiento del capítulo `20`.

**Fuera de alcance:**

- **Construir la comprobación.** La mitad que un programa puede ver se declara y se enruta; no se construye acá.
- **Limpiar la memoria que ya existe.** Si hay algo que sacar, es trabajo aparte y se mide antes.
- Los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
104 cumplen, 5 no cumplen, 5 sin veredicto
```

### 2.1 Que la regla no existía, comprobado

Se buscó en [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), que es donde el criterio la esperaba: **cero menciones** de dato personal, credencial, clave o secreto. La regla dice qué se registra como señal; no dice qué no.

`00·N6` sí prohíbe escribir una credencial, en cualquier parte. Lo que no cubre el núcleo es **el dato personal**, y ese era el hueco.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `base/04-seguridad.md` | Modificar | Estándar | La regla `S19`, al final del capítulo |
| `validadores/reglas-validables.md` | Modificar | Estándar | Su clasificación, con lo que sí y lo que no |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `36.0.0`, MAYOR |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-001-que-se-guarda-tipos-y-alcances.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La regla va en `04`, seguridad | Ponerla en `13`, documentación | No es cómo se escribe un documento: es qué dato puede salir de una sesión y quedar guardado |
| No declara depender de `00·N6` | Escribir «extiende `N6`» | `20·M7` prohíbe extender una `[BLINDADA]`. La regla la nombra y no la toca |
| Se declara qué mitad **no** es comprobable | Clasificarla como validable a secas | El dato personal no se detecta sin decidir qué nombre propio es de una persona; prometerlo sería un veredicto falso |
| **MAYOR**, no menor | Versionarla como aditiva | Un proyecto al día tiene que revisar su memoria: eso es algo nuevo que hacer |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Comprobar que la regla no existe | Análisis | 0,25 h | — | EV-01 |
| T-02 | Escribir `04·S19` con su checklist | Estándar | 1 h | T-01 | EV-02 |
| T-03 | Clasificarla en el registro de validables | Estándar | 0,5 h | T-02 | EV-02 |
| T-04 | Versionar y declarar el veredicto | Documentación | 0,5 h | T-03 | EV-03 |

**Total estimado:** 2,25 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero porque si la regla existiera, esto no sería escribir sino enlazar.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| Transversal · Privacidad | Que exista la regla, con su checklist aplicado y `validar.py metareglas` en verde | EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Ninguno. La fase escribe norma; no toca datos ni memoria existente.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. La regla no se deroga: nunca llegó a regir.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Obliga a migrar.** Un proyecto al día tiene que revisar su memoria y sacar lo que no debería estar. El aviso de desfase lo informa al abrir sesión; no migra solo.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M5`, el formato canónico de la regla, con una sola exigencia y su ejemplo.
- `20·M7`, nada extiende ni deroga una `[BLINDADA]`: por eso `S19` nombra a `N6` sin declarar dependencia.
- `20·M9`, se decide si es validable, y se dice qué mitad no lo es.
- `20·M10`, todo cambio de regla se versiona y se registra.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Declarar la regla validable entera | Prometería una comprobación que nadie puede escribir | `T-03` dice qué mitad no lo es | Cerrado |
| B-02 | Escribir «extiende `N6`» | `20·M7` lo prohíbe y la comprobación lo caza | La regla lo nombra sin declararlo | Cerrado |
| B-03 | Firmar el checklist sin aplicarlo | Es lo que le pasó a `S18` el 2026-08-27 | El cuerpo se midió antes de escribirlo: 303 de 320 | Cerrado |

---

## 11. Definition of Done

- [x] La regla escrita, con su checklist
- [x] Clasificada en el registro de validables
- [x] `validar.py metareglas` sin incumplimientos
- [x] `CHANGELOG.md` y `VERSION` al día
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
