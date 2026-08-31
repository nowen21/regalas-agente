# HU-006 — Correr la batería completa antes de publicar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien responde por lo que sale del proyecto
- **Quiero** que antes de publicar corran todas las comprobaciones
- **Para** que lo que se publica ya pasó por todos los controles, no solo por los rápidos

---

## 3. Contexto y descripción

Durante el trabajo solo corren las comprobaciones rápidas, porque las lentas estorbarían. Eso deja un hueco: lo lento no se corre nunca.

Publicar es el momento correcto para lo lento. Es la última puerta, pasa pocas veces al día y quien publica está dispuesto a esperar, porque lo que sale ya no se puede retirar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Antes de publicar corre la batería completa, incluidas las lentas |
| RN-02 | Si alguna encuentra un incumplimiento claro, no se publica |
| RN-03 | Los avisos se muestran y no detienen |
| RN-04 | El resultado dice qué corrió, no solo qué falló |
| RN-05 | Publicar sigue necesitando la autorización de la persona: la batería no autoriza nada |

### 3.2 Supuestos

- Publicar es un momento identificable y poco frecuente.

### 3.3 Fuera de alcance

- Las comprobaciones en sí. Eso es EP-004.
- Publicar. Este automatismo solo revisa antes.

---

## 4. Criterios de aceptación

### CA-01 — Antes de publicar corre todo

```gherkin
Dado que se va a publicar el trabajo
Cuando arranca la publicación
Entonces corren todas las comprobaciones, incluidas las lentas
Y el resultado dice cuáles corrieron
```

**Cómo validarlo:**

1. Preparar el proyecto de prueba para publicar.
2. Ejecutar la publicación. Resultado esperado: corre la batería y su salida lista cada comprobación.
3. Comparar con las que corren al escribir un archivo. Resultado esperado: acá corrieron más.
- **Aprobado cuando:** no queda comprobación sin correr.

### CA-02 — Un incumplimiento claro detiene la publicación

```gherkin
Dado que una comprobación encuentra un incumplimiento claro
Cuando se intenta publicar
Entonces la publicación no se hace
Y se dice cuál lo impidió
```

**Cómo validarlo:**

1. Sembrar un incumplimiento claro en el proyecto de prueba.
2. Intentar publicar. Resultado esperado: no publica y nombra la comprobación.
3. Arreglarlo y volver a intentar. Resultado esperado: publica.
- **Aprobado cuando:** lo que no cumple no sale.

### Criterios de aceptación transversales

- [ ] **Autorización** — la batería no reemplaza la autorización de la persona para publicar.
- [ ] **Rendimiento** — la espera es razonable para algo que pasa pocas veces al día.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Completitud** | Corre todo, no una selección |
| **Transparencia** | Dice qué corrió y qué dio cada una |
| **Prudencia** | Ante un incumplimiento claro, no publica |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Enganchar la batería al momento previo a publicar.
- [ ] Reportar qué corrió y qué dio cada comprobación.
- [ ] Detener la publicación ante un incumplimiento claro.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
**Ejecutada el 2026-08-22.** Veredicto: [**Cumple**](A-EP-005-HU-006-la-bateria-antes-de-publicar/resultado_pruebas.md) — con el reparto entre lo que detiene y lo que informa, y su motivo escrito |

**La fase construye, y depende de otra:** la batería es la corrida completa de EP-004 · HU-008. Y tiene un límite claro — publicar lo autoriza una persona (`00·N2`), así que la batería niega el visto bueno, no impide la acción de nadie.

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
| Dependencia | EP-004, porque corre las comprobaciones de esa épica | Alto |
| Dependencia | HU-003, porque comparte con ella qué es rápido y qué es lento | Medio |
| Riesgo | Que la espera lleve a saltarse el control | Se corre solo al publicar, que pasa pocas veces |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La batería completa corre antes de publicar
- [ ] Un incumplimiento claro detiene la publicación
- [ ] El resultado dice qué corrió
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita las comprobaciones de EP-004 |
| **N**egociable | Sí | Qué corre en esta batería se puede discutir |
| **V**aliosa | Sí | Cierra el hueco de lo que nunca se corre |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un enganche y un reporte |
| **T**esteable | Sí | Se prueba sembrando un incumplimiento |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
