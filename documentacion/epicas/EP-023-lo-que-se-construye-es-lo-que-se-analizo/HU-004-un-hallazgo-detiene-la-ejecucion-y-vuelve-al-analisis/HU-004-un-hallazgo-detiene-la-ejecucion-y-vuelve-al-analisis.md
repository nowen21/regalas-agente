# HU-004 · Un hallazgo detiene la ejecución y vuelve al análisis

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (puntos 6, 13, 14, 17, 18 y 24) y del [análisis 2](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-2.md) (punto 7). Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `base/13-documentacion/`, `plantillas/` |
| **Tipo** | Técnica |
| **Prioridad** | Orden 5 de 7 |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Lista: aprobada el 2026-10-01 |

---

## 2. Narrativa

- **Como** el usuario, que plantea la necesidad y aprueba (análisis 1, conclusión 40)
- **Quiero** que un hallazgo detenga la ejecución y vuelva al análisis
- **Para** que al ejecutar un plan solo aparezcan los hallazgos que no se podían prever

---

## 3. Contexto y descripción

Del [problema de la épica](../epica.md#31-situación-actual), esta HU resuelve que nada detiene al agente cuando aparece un hallazgo al ejecutar el plan ([análisis 4](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

### 3.1 Reglas de negocio

Son las conclusiones de las que salen los puntos de esta HU.

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | El hallazgo, el pendiente, la HU y el plan se reescriben en su mismo archivo con la versión vigente. El análisis nunca se reescribe | Análisis 1, conclusión 9 |
| RN-02 | Un hallazgo al ejecutar el plan no abre un pendiente nuevo: vuelve al último análisis, se abre el siguiente y el hallazgo y el pendiente pasan a la versión siguiente | Análisis 1, conclusión 10 |
| RN-03 | Cuando aparece un hallazgo, la ejecución se detiene en ese momento. Ni el plan ni la HU se cierran | Análisis 1, conclusión 18 |
| RN-04 | El análisis siguiente trata solo lo que falló y sus implicaciones sobre lo ya hecho | Análisis 1, conclusión 19 |
| RN-05 | Si el análisis cambia lo pedido, la HU y el plan pasan a la versión siguiente en su mismo archivo; no se crean otros | Análisis 1, conclusión 24 |
| RN-06 | Si la fase ya cerró y aparece un hallazgo sobre lo construido, la fase se reabre | Análisis 1, conclusión 33 |
| RN-07 | Cada plan registra cuántos hallazgos salieron al ejecutarlo | Análisis 1, conclusión 41 |
| RN-08 | El análisis de un hallazgo decide primero si es parte del plan en curso. Si lo es, mejora el pendiente y se resuelve antes de seguir; si no, se crea su pendiente y el plan continúa | Análisis 2, conclusión 7 |

### 3.2 Supuestos

Ninguno.

### 3.3 Fuera de alcance

- Los puntos que la propuesta final reparte a las otras HU.

---

## 4. Criterios de aceptación

### CA-01 · Versiones en el mismo archivo y análisis numerados

**Sale de:** análisis 1, punto 6.

```gherkin
Dado que el hallazgo, el pendiente, la HU o el plan cambian
Entonces se reescriben en su mismo archivo
Y los análisis se numeran sin reescribirse
```

**Cómo validarlo:**
1. Buscar en `base/` la regla que lo exige.

**Aprobado cuando:** la regla existe y dice lo del criterio.

### CA-02 · Un hallazgo detiene la ejecución y nada cierra

**Sale de:** análisis 1, punto 13.

```gherkin
Dado un plan en ejecución
Cuando aparece un hallazgo
Entonces la ejecución se detiene
Y ni el plan ni la HU pueden cerrar mientras no se resuelva
```

**Cómo validarlo:**
1. Anotar un hallazgo durante la ejecución de un plan.
2. Intentar cerrar el plan y la HU.

**Aprobado cuando:** la ejecución queda detenida y ninguno de los dos cierra.

### CA-03 · El análisis siguiente trata solo lo que falló

**Sale de:** análisis 1, punto 14.

```gherkin
Dado un hallazgo que abre el análisis siguiente
Cuando se lee lo que exige el estándar
Entonces ese análisis trata solo lo que falló y sus implicaciones sobre lo ya hecho
```

**Cómo validarlo:**
1. Buscar en `base/` la regla que lo exige.

**Aprobado cuando:** la regla existe y dice lo del criterio.

### CA-04 · `02·F8` y `02·F9` detienen y vuelven al análisis

**Sale de:** análisis 1, punto 17.

```gherkin
Dado que 02·F8 y 02·F9 hoy amplían el plan y siguen
Cuando se ajustan
Entonces dicen que la ejecución se detiene y vuelve al análisis
```

**Cómo validarlo:**
1. Abrir [`02·F8`](../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) y [`02·F9`](../../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md).

**Aprobado cuando:** las dos dicen lo del criterio.

### CA-05 · El plan pasa de versión y la fase cerrada se reabre

**Sale de:** análisis 1, punto 18.

```gherkin
Dado que «el plan aprobado no se modifica» (02/base.md), las fases que complementan a otra de 02·F12 y «una fase cerrada no se reabre» de 13·DOC12 se ajustan
Entonces el plan pasa a la versión siguiente con aprobación nueva
Y la fase cerrada se reabre si aparece un hallazgo
```

**Cómo validarlo:**
1. Abrir [`02/base.md`](../../../../base/02-flujo-de-trabajo/base.md), [`02·F12`](../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) y [`13·DOC12`](../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

**Aprobado cuando:** los tres dicen lo del criterio.

### CA-06 · El plan registra sus hallazgos

**Sale de:** análisis 1, punto 24.

```gherkin
Dado un plan ejecutado
Cuando se lee
Entonces dice cuántos hallazgos salieron al ejecutarlo
```

**Cómo validarlo:**
1. Abrir la plantilla del plan de trabajo en `plantillas/ciclo-vida-proyectos/`.

**Aprobado cuando:** pide cuántos hallazgos salieron.

### CA-07 · El análisis del hallazgo decide primero si es parte del plan

**Sale de:** análisis 2, punto 7.

```gherkin
Dado un hallazgo que abre un análisis
Cuando se lee lo que exige el estándar
Entonces ese análisis decide primero si el hallazgo es parte del plan en curso
Y si lo es, mejora el pendiente y se resuelve antes de seguir
Y si no, se crea su pendiente y el plan continúa
```

**Cómo validarlo:**
1. Buscar en `base/` la regla que lo exige, y la plantilla del análisis.

**Aprobado cuando:** dicen lo del criterio.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | N/A |
| RNF-02 | **Seguridad** | N/A |
| RNF-03 | **Auditoría** | N/A |
| RNF-04 | **Accesibilidad** | N/A |
| RNF-05 | **Compatibilidad** | N/A |
| RNF-06 | **Trazabilidad** | Cada criterio cita el punto de lo que se tiene que hacer del que sale (análisis 1, conclusión 39) |

---

## 6. Diseño y referencias

| Campo | Valor |
|---|---|
| Documento funcional | [análisis 1](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) y [análisis 2](../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-2.md) |
| Mockup / Prototipo | N/A |
| Contrato de API | N/A |

---

## 7. Tareas técnicas derivadas

Las fija el plan de cada fase (`02·F14`).

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| N/A: todavía no se descompone en fases | | | | | | |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001: las demás HU se apoyan en el análisis | Bloqueante |
| La necesita | HU-007: necesita que esta HU defina qué pasa con un hallazgo | Bloqueante |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [ ] Diseño / mockup disponible: N/A
- [ ] Dependencias identificadas y desbloqueadas: depende de la HU-001
- [x] Estimada
- [ ] Cumple criterios INVEST: no es independiente

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Pruebas pasando
- [ ] `VERSION` y `CHANGELOG.md` actualizados
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☐ | Depende de la HU-001 |
| **N**egociable | ✅ | |
| **V**aliosa | ✅ | |
| **E**stimable | ✅ | Talla M |
| **S**mall (pequeña) | ☐ | Siete criterios: puede pedir más de una fase |
| **T**esteable | ✅ | Cada criterio dice dónde mirar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Creación de la HU |
| 2026-10-01 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | El contexto dice la parte del problema de la épica que resuelve, según el análisis 4 |
| 2026-10-01 | Ing. José Dúmar Jiménez Ruíz | **Aprobada** |
