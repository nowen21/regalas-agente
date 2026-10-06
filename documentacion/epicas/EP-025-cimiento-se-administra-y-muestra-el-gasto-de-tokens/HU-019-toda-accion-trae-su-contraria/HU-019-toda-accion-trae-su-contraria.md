# HU-019 · Toda acción trae su contraria


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-019 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien construye con el estándar, en Cimiento o en un proyecto que lo hereda
- **Quiero** que ninguna acción que crea o cambia algo se dé por terminada sin la acción que lo deja como estaba
- **Para** que un error se corrija con una herramienta y no tocando archivos a mano

---

## 3. Contexto y descripción

El 2026-10-05 el andamio creó una HU con el número equivocado y no había cómo quitarla; el freno bloqueó con razón y el usuario tuvo que borrar a mano. Ninguna regla pedía la contraria de lo que se construye ([análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 2, punto 2).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Regla nueva del capítulo `02`: ninguna acción que crea o cambia algo se da por terminada sin la acción que lo deja como estaba, y su prueba | Acuerdo 2 |
| RN-02 | Rige para el código de Cimiento y para el de cada proyecto que lo hereda | Acuerdo 2 |
| RN-03 | Los planes nuevos la declaran: la plantilla del plan de trabajo trae dónde | Acuerdo 2 |
| RN-04 | Versión MAYOR: obliga a los proyectos a declararla en sus planes nuevos | `20·M10` |

### 3.2 Supuestos

- Las fases ya cerradas no se reabren por esta regla (`20·M10`, retroactividad).

### 3.3 Fuera de alcance

- Un validador que lo compruebe: primero se cumple a mano (`20·M19`).

---

## 4. Criterios de aceptación

### CA-01 · La regla existe con su forma

**Sale de:** análisis 3 del pendiente 119, punto 2.

```gherkin
Dado el capítulo 02 del estándar
Cuando se abre su catálogo
Entonces está la regla «Toda acción trae su contraria», en su archivo, con su ejemplo, su línea «Aplica a» y su checklist en CUMPLE
Y el mapa de tareas la trae
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py metareglas` y `python validadores/validar.py estandar` desde la raíz → sin fallas sobre la regla nueva.
2. Buscar la regla en `base/mapa-de-tareas.md` → aparece bajo sus tareas.

**Aprobado cuando:** los validadores no le encuentran fallas.

### CA-02 · El plan la declara

**Sale de:** análisis 3 del pendiente 119, punto 2.

```gherkin
Dado la plantilla del plan de trabajo
Cuando se abre una fase nueva con el andamio
Entonces su plan trae la sección de la contraria de cada acción nueva
```

**Cómo validarlo:**
1. Abrir `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` → trae la sección 2.8 con su tabla.

**Aprobado cuando:** la sección está y enlaza la regla.

### CA-03 · Queda versionado

**Sale de:** `20·M10`.

```gherkin
Dado el cambio de la regla y la plantilla
Cuando se revisa el registro
Entonces CHANGELOG.md tiene la entrada MAYOR y VERSION sube
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py versionado` → sin fallas.

**Aprobado cuando:** la versión sube de mayor y la entrada dice qué hace un proyecto al día.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | La regla se entiende sin saber del tema (`00·ID7`) |

---

## 6. Diseño y referencias

Documento funcional: [análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 2. Procedimiento: [`20` meta-reglas](../../../../base/20-meta-reglas/base.md#cómo-se-agrega-una-regla-nueva-procedimiento).

---

## 7. Tareas técnicas derivadas

- [x] La regla y su lugar en el catálogo.
- [x] La sección en la plantilla del plan.
- [x] El mapa de tareas, el registro de validables y la versión.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-019-la-regla-y-su-plantilla` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-019-la-regla-y-su-plantilla/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-019-la-regla-y-su-plantilla/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-019-la-regla-y-su-plantilla/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que repita lo que ya dice `03·D2` | Se cita: la migración reversible es un caso de esta regla |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 3 del pendiente 119 |
