# HU-007 — Marcar lo que dejó de aplicar sin borrarlo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso — CA-02, RNF y no regresión cumplidos; el CA-01 y la trazabilidad, no |
---

## 2. Narrativa

- **Como** quien busca en la memoria y encuentra algo viejo
- **Quiero** que lo que dejó de aplicar esté marcado, no borrado
- **Para** no seguir un consejo que ya no vale, y a la vez entender por qué se hizo así antes

---

## 3. Contexto y descripción

Lo guardado envejece. Una decisión se revierte, un error se arregla de otra forma, una convención cambia. Si eso se borra, se pierde el porqué de lo que todavía está en el código. Si se deja como está, alguien lo va a seguir creyendo.

La salida es la misma que usan las reglas: no se borra, se marca. Queda visible, con la fecha en que dejó de aplicar y qué lo reemplazó.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo que dejó de aplicar se marca, no se borra |
| RN-02 | La marca dice desde cuándo y qué lo reemplazó, si hay algo |
| RN-03 | Lo marcado no aparece primero en las búsquedas, pero sigue encontrándose |
| RN-04 | Marcarlo es una decisión de una persona, no algo que pase por el tiempo |

### 3.2 Supuestos

- El volumen de lo guardado crece despacio, así que marcar a mano es viable.

### 3.3 Fuera de alcance

- Borrar lo viejo. No se borra.
- Detectar solo que algo dejó de aplicar. Eso es criterio, no cálculo.

---

## 4. Criterios de aceptación

### CA-01 — Lo que dejó de aplicar queda marcado y visible

```gherkin
Dado que algo guardado dejó de aplicar
Cuando se marca
Entonces sigue existiendo, con la fecha y qué lo reemplazó
```

**Cómo validarlo:**

1. Marcar como no vigente algo guardado.
2. Abrirlo. Resultado esperado: sigue ahí, con la marca, la fecha y el reemplazo.
3. Buscar el archivo. Resultado esperado: no se borró.
- **Aprobado cuando:** se entiende que ya no vale y por qué se hizo así antes.

### CA-02 — Lo marcado no se confunde con lo vigente

```gherkin
Dado que hay cosas vigentes y cosas marcadas
Cuando se busca
Entonces las vigentes aparecen primero
Y las marcadas se ven como tales
```

**Cómo validarlo:**

1. Buscar una palabra que aparezca en una vigente y en una marcada.
2. Mirar el orden. Resultado esperado: primero la vigente.
3. Mirar cómo se muestra la marcada. Resultado esperado: se ve que ya no aplica.
- **Aprobado cuando:** nadie sigue por error un consejo que caducó.

### Criterios de aceptación transversales

- [ ] **No regresión** — marcar no altera el contenido original.
- [ ] **Trazabilidad** — queda quién lo marcó y cuándo.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Permanencia** | Nada se borra |
| **Claridad** | La marca se ve al abrir, no hay que deducirla |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), §5.3, que difería la poda y la vigencia.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir la marca de que algo dejó de aplicar.
- [ ] Registrar la fecha y el reemplazo.
- [ ] Ordenar las búsquedas para que lo vigente vaya primero.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar](A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar/resultado_pruebas.md#6-veredicto-de-la-fase) — el CA-02 sí, el CA-01 a medias. Pendiente el commit |
| `B-EP-006-HU-007` — **propuesta, sin abrir** | Lo que le falta al CA-01 y al transversal de trazabilidad | Que `cmd_supersede` guarde el `--by` y la fecha, y que archivar deje fecha |

**La fase retro-documentó, y encontró lo que faltaba.** La regla «ninguna se borra» **se cumple**: se comprobó contando el total antes y después de pasar señales por los cuatro estados no vigentes, y nunca bajó. Los cinco estados hacen lo que dicen y la vigencia distingue lo viejo sin revisar de lo fresco.

**Lo que no se cumple** es la otra mitad del CA-01: la señal marcada no dice **cuándo** se marcó ni **qué la reemplazó**. `cmd_supersede` imprime «S-001 marcada reemplazada por S-002» y no guarda nada; archivar tampoco deja fecha. El enlace del reemplazo funciona en un solo sentido — desde la nueva se llega a la vieja, al revés no.

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
| Dependencia | HU-002, porque marca lo que esa historia guardó | Alto |
| Dependencia | HU-003, porque el orden de las búsquedas cambia | Medio |
| Riesgo | Que nadie marque nada y todo parezca vigente | Marcar es parte de cerrar la unidad que cambió la decisión |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Lo que dejó de aplicar se marca y no se borra
- [ ] Lo vigente aparece primero en las búsquedas
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita lo guardado y la búsqueda |
| **N**egociable | Sí | La forma de la marca se puede discutir |
| **V**aliosa | Sí | Evita seguir un consejo que caducó |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Una marca y un orden |
| **T**esteable | Sí | Se prueba marcando algo y buscándolo |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. CA-02, RNF y no regresión verificados; CA-01 y trazabilidad en «No» porque marcar no deja fecha ni dice qué reemplazó. Se propone la fase B |
