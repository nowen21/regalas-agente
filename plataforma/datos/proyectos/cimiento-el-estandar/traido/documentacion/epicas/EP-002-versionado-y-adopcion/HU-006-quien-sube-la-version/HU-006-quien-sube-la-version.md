# HU-006 — Quién sube la versión cuando hay dos sesiones abiertas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-002 Versionado de las reglas y adopción por proyecto](../epica.md) |
| **Módulo / Componente** | Versionado del estándar |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja con otra sesión abierta al mismo tiempo
- **Quiero** una regla de quién sube la versión
- **Para** que dos sesiones no dejen dos numeraciones vivas del mismo estándar

---

## 3. Contexto y descripción

El 2026-08-14 hubo dos sesiones abiertas sobre el mismo repositorio. Una escribió la versión 10.0.0 mientras la otra subía la 9.0.0, la 9.1.0 y la 9.2.0. Al final del día el número iba en 12.2.0, con entradas del registro escritas por las dos y dos numeraciones vivas.

El número de versión y el registro de cambios son un archivo único cada uno, y ninguna sesión sabe qué está haciendo la otra. Ahí se rompe la regla de que cada sesión sube solo lo suyo: para guardar lo propio hay que arrastrar lo ajeno.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Queda escrito quién sube la versión y en qué momento |
| RN-02 | Dos sesiones abiertas no pueden dejar dos numeraciones vivas |
| RN-03 | Una sesión no arrastra el trabajo de otra para poder guardar el suyo |
| RN-04 | El registro de cambios no pierde ninguna entrada por el cruce |

### 3.2 Supuestos

- Trabajar con dos sesiones abiertas es normal y no se va a prohibir.

### 3.3 Fuera de alcance

- El criterio de qué parte del número sube, que ya está definido.
- Resolver conflictos de contenido entre las dos sesiones.

---

## 4. Criterios de aceptación

### CA-01 — Dos sesiones no dejan dos numeraciones

```gherkin
Dado que dos sesiones cambian reglas el mismo día
Cuando las dos guardan su trabajo
Entonces queda una sola numeración, sin huecos ni números repetidos
```

**Cómo validarlo:**

1. Abrir dos sesiones sobre una copia del repositorio y cambiar una regla en cada una.
2. Guardar las dos, en el orden que sea. Resultado esperado: la numeración queda corrida y sin repetir.
3. Leer el registro. Resultado esperado: están las dos entradas, cada una con su número.
- **Aprobado cuando:** el orden de guardado no produce dos numeraciones.

### CA-02 — Nadie arrastra el trabajo de otro

```gherkin
Dado que una sesión va a guardar su cambio
Cuando la otra dejó trabajo sin guardar en el mismo archivo
Entonces la primera puede guardar lo suyo sin llevarse lo ajeno
```

**Cómo validarlo:**

1. Dejar en una sesión una entrada escrita y sin guardar.
2. Desde la otra, guardar un cambio propio. Resultado esperado: se guarda sin incluir la entrada ajena.
3. Revisar lo que quedó guardado. Resultado esperado: solo lo propio.
- **Aprobado cuando:** cada sesión sube lo suyo, también en estos archivos.

### Criterios de aceptación transversales

- [ ] **No regresión** — el registro no pierde entradas.
- [ ] **Límites** — está definido qué pasa si las dos sesiones suben la misma parte del número.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Simplicidad** | La regla se entiende y se aplica sin herramienta especial |
| **Trazabilidad** | Cada entrada queda con su número y su autor |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** el pendiente 22, que registró el cruce con fechas y números.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Elegir entre las tres opciones: subir la versión al guardar, escribir la entrada en un archivo aparte, o una sola sesión a la vez.
- [ ] Escribir la regla o el acuerdo donde corresponda.
- [ ] Comprobar el cruce con dos sesiones de prueba.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-002-HU-006-quien-manda-sobre-la-version](A-EP-002-HU-006-quien-manda-sobre-la-version/README.md) | CA-01 y CA-02 | **Cerrada 2026-08-18** · v23.11.0 · los dos CA en cumple |

**Cerrada.** Nació [`20·M18`](../../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md) —lo compartido se relee al escribirlo, extendiendo a `M10`— y su comprobación dentro de `validar.py versionado`. De las tres salidas del pendiente 22 se eligió la primera.

**Y quedó algo que la HU no preveía:** el cruce se rompe de dos maneras. El número repetido deja rastro —el registro tiene dos `15.4.0`— y la entrada perdida no. La `RN-04` solo se puede sostener con la regla, no con la comprobación.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001 y HU-002, porque el número y el registro son lo que se cruza | Alto |
| Riesgo | Que la regla elegida sea tan incómoda que se ignore | Se prueba con dos sesiones reales antes de fijarla |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Está escrito quién sube la versión y cuándo
- [ ] Dos sesiones de prueba no dejan dos numeraciones
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Se apoya en el número y el registro |
| **N**egociable | Sí | Hay tres opciones sobre la mesa |
| **V**aliosa | Sí | Evita dos numeraciones del mismo estándar |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un acuerdo escrito |
| **T**esteable | Sí | Se prueba con dos sesiones abiertas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-9 del 2026-08-14 |
| 2026-08-18 | El agente | Cerrada con la fase `A-EP-002-HU-006`: nace `20·M18` y su validador. v23.11.0 |
