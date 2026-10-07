# HU-006 · Los archivos de `base/` quedan quietos en la versión 55.1.0

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/`, el freno y el control del commit |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra Cimiento
- **Quiero** que los archivos de `base/`, `VERSION` y `CHANGELOG.md` no se vuelvan a tocar
- **Para** que el estándar tenga una sola fuente, la base, y git guarde la historia anterior sin que nadie la cambie

---

## 3. Contexto y descripción

Dos fuentes del estándar se separan. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 15 y 20, punto 12 de «Lo que se tiene que hacer», y de `20·M10`. El título dice 55.1.0 porque esa era la versión al aprobar el análisis; los archivos quedan en la que tengan al congelar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Con el estándar congelado, el freno no deja escribir `base/`, `VERSION` ni `CHANGELOG.md` en la carpeta del estándar (acuerdo 20) |
| RN-02 | Con el estándar congelado, un commit que los toque no pasa; uno que toque `plantillas/` pide una versión del estándar registrada en la base después del último commit (`20·M10`) |
| RN-03 | Congelar es una orden: pone la base al día con git, alinea su versión con la de `VERSION` y deja la marca; la contraria la quita |
| RN-04 | El agente lee las reglas completas de la base, con `ver_estandar`, no de los archivos |

### 3.2 Supuestos

- Los commits pendientes que tocan `base/` se hacen antes de congelar.

### 3.3 Fuera de alcance

- Otros proyectos: su carpeta `base/`, si la tienen, no es el estándar.

---

## 4. Criterios de aceptación

### CA-01 · El freno no deja tocar `base/`

**Sale de:** análisis 1 del pendiente 132, punto 12 de «Lo que se tiene que hacer»

```gherkin
Dado el estándar congelado
Cuando el agente intenta escribir base/x.md, VERSION o CHANGELOG.md en la carpeta del estándar
Entonces el freno lo detiene y dice que el estándar se cambia en la pantalla de Cimiento
Y sin congelar, o en otro proyecto, no lo detiene por esto
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-02 · El commit no deja pasar `base/` y pide la versión de las plantillas en la base

**Sale de:** `20·M10`

```gherkin
Dado el estándar congelado
Cuando un commit trae base/, VERSION o CHANGELOG.md
Entonces el control del commit lo detiene
Y si trae plantillas/ sin una versión del estándar registrada en la base después del último commit, también lo detiene
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-03 · Congelar y descongelar

**Sale de:** RN-03, `02·F30`

```gherkin
Dado el estándar sin congelar
Cuando se corre manage.py congelar_base
Entonces la base queda al día con git, su versión no queda por debajo de la de VERSION, y queda la marca
Y manage.py congelar_base --deshacer la quita
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-04 · El agente lee las reglas completas de la base

**Sale de:** RN-04

```gherkin
Dado el estándar en la base
Cuando el enganche de reglas nombra dónde están las reglas completas, o el arranque dice cómo llegan
Entonces dice la orden ver_estandar con la ruta, no que se lea el archivo
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Saber si está congelado cuesta una consulta por proceso |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Ninguno: la marca es un ajuste común |

---

## 7. Tareas técnicas derivadas

- [ ] La marca, congelar y descongelar.
- [ ] El freno y el control del commit.
- [ ] `registrar_version`.
- [ ] Los textos que dicen dónde leer las reglas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-006-congelar-base` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-006-congelar-base/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-006-congelar-base/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-006-congelar-base/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Otra sesión en medio de un cambio de `base/` queda detenida | El aviso dice cómo seguir: la pantalla o `proponer` |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Una sola fuente del estándar |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
