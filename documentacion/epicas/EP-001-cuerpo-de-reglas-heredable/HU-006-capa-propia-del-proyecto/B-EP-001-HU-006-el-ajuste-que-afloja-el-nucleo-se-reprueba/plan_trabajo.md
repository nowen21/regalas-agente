# Plan de Trabajo — Fase `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-006](../HU-006-capa-propia-del-proyecto.md), **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-03, que quedó en rojo por no haberse podido ejecutar.** La fase [`A`](../A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md) cerró el 2026-08-17 con una razón honesta en su defecto `D-03`: ningún proyecto real tenía un ajuste que contradijera el núcleo, y escribir uno en un proyecto real está prohibido por la decisión 35 del pendiente 59. Se comprobó por lectura, y por lectura no se comprueba nada.

**Lo que faltaba no era el caso: era dónde provocarlo.** La misma decisión 35 dice cómo: en una carpeta temporal, que es lo que hizo la fase `B` de `EP-002·HU-003` con una versión inventada.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** provocar el caso y, si falla, hacer que la comprobación lo vea.

**Fuera de alcance:**

- Los defectos `D-01` y `D-02` de la fase `A`, que son de otro asunto.
- Detectar una contradicción que el proyecto **no declare**. Eso no se lee de un verbo.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
101 cumplen, 8 no cumplen, 5 sin veredicto
```

### 2.1 Qué se provocó, y qué salió

Un proyecto de prueba en carpeta temporal, con este `.agente/reglas-proyecto.md`:

```
## P1 · El agente puede commitear sin pedir permiso
- **Respaldo:** afloja `N2`, que exige pedido explícito.

## P2 · Las credenciales de prueba se pueden dejar escritas
- **Respaldo:** deroga `N6`, que prohíbe escribir una credencial.
```

`validar_catalogo` devolvió **cero hallazgos**.

**Por qué pasaba.** La comprobación mira lo que pide `20·M16`: que haya respaldo y que el ID citado exista. `N2` y `N6` existen, así que el respaldo era válido. La prohibición vive en `20·M7`, y esa comprobación solo recorría las reglas del estándar, nunca las del proyecto. La regla estaba escrita y no se aplicaba donde importa.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/metareglas.py` | Modificar | Comprobación | `_afloja_una_blindada` y su uso en `validar_catalogo` |
| `validadores/pruebas.py` | Modificar | Pruebas | Dos casos: el que afloja y el que endurece |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-006-capa-propia-del-proyecto.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se mira **el verbo del respaldo** | Interpretar si la regla contradice el núcleo | Interpretar la intención de un texto no es comprobar. El verbo es lo que la propia regla declara |
| Lista cerrada de verbos que aflojan | Reprobar toda mención de una regla del núcleo | Endurecer una `[BLINDADA]` es legítimo, y es para lo que existe la capa propia. Reprobarlo la volvería inútil |
| Se declara lo que **no** se promete | Callarlo | Un proyecto que contradiga el núcleo sin decirlo sigue sin detectarse, y el comentario del código lo dice |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Provocar el caso en una carpeta temporal | Calidad | 0,5 h | — | EV-01 |
| T-02 | Hacer que la comprobación lo vea | Comprobación | 1 h | T-01 | EV-02 |
| T-03 | Probar el caso malo y el bueno | Pruebas | 0,5 h | T-02 | EV-03 |
| T-04 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-03 | EV-03 |

**Total estimado:** 2,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. Lo que cambia es un programa que hace cumplir una regla que ya existía.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero y no es trámite: si el caso hubiera pasado, no había nada que construir.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-03, el ajuste que contradice el núcleo no aplica | Provocarlo en carpeta temporal, con su contraprueba | EV-01, EV-03 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas temporales que la propia prueba crea y borra. Ningún proyecto real se toca, que es justamente lo que impedía ejecutar este criterio.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** El proyecto que ya tenga reglas propias las verá comprobadas la próxima vez que corra `validar.py metareglas --catalogo`.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M7`, nada extiende ni deroga una `[BLINDADA]`. Es la regla que esta fase hace cumplir.
- `20·M16`, toda regla del proyecto declara su respaldo.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la comprobación repruebe al que endurece | La capa propia quedaría inservible | `T-03` prueba el caso bueno | Cerrado |
| B-02 | Que se dé por cumplido sin provocar el caso | Es el defecto que dejó este CA en rojo | `T-01` | Cerrado |

---

## 11. Definition of Done

- [x] El caso, provocado
- [x] La comprobación, construida
- [x] Las dos pruebas, en verde
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
