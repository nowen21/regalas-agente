# HU-006 — Sacar del almacén local lo que deba vivir en el repositorio

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso — CA-02, RNF y transversales cumplidos; el CA-01 falla en un punto |
---

## 2. Narrativa

- **Como** quien revisa lo que la IA recuerda
- **Quiero** que nada quede guardado en el almacén propio de la herramienta
- **Para** poder leerlo, corregirlo y que no dependa de una sola máquina

---

## 3. Contexto y descripción

La herramienta con la que se conversa tiene su propio almacén de memoria, fuera del proyecto. Lo que quede ahí es invisible: no se revisa, no viaja y nadie sabe qué dice.

Pedirle a la IA que no lo use no alcanza, porque dónde guarda su memoria lo decide la herramienta. Lo que sí funciona es dejar el almacén vacío: lo que aparezca se mueve al repositorio.

Es la contraparte, del lado de la memoria, del automatismo que recoge; aquí se define la regla y el destino, allá el momento en que corre.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El almacén propio de la herramienta queda vacío |
| RN-02 | Lo que aparezca ahí se mueve al repositorio, sin dejar copia ni puntero |
| RN-03 | Ni el texto ni un enlace al texto se quedan en el almacén |
| RN-04 | Lo movido conserva su tipo y su alcance |
| RN-05 | Nada se pisa al mover: si el nombre está ocupado, entra con otro y se avisa |

### 3.2 Supuestos

- El almacén de la herramienta se puede leer y vaciar desde la máquina donde se trabaja.

### 3.3 Fuera de alcance

- El momento en que corre la recogida. Eso es EP-005.
- Cambiar cómo funciona la herramienta.

---

## 4. Criterios de aceptación

### CA-01 — El almacén queda vacío

```gherkin
Dado que la herramienta guardó algo en su propio almacén
Cuando se aplica la regla
Entonces eso queda en el repositorio
Y el almacén queda vacío
```

**Cómo validarlo:**

1. Dejar algo en el almacén de la herramienta.
2. Aplicar la recogida. Resultado esperado: aparece en el repositorio.
3. Mirar el almacén. Resultado esperado: vacío, sin copia ni puntero.
- **Aprobado cuando:** no queda memoria fuera del repositorio.

### CA-02 — No queda un puntero en lugar del texto

```gherkin
Dado que se movió algo al repositorio
Cuando se revisa el almacén de la herramienta
Entonces no hay ni el texto ni una nota que diga dónde quedó
```

**Cómo validarlo:**

1. Después de mover, abrir el almacén. Resultado esperado: no hay archivos.
2. Buscar una nota que apunte al repositorio. Resultado esperado: no hay.
- **Aprobado cuando:** hay una sola versión, y está donde se puede revisar.

### Criterios de aceptación transversales

- [ ] **Límites** — nombres que solo difieren en mayúsculas se tratan como el mismo archivo.
- [ ] **Privacidad** — lo movido pasa por la misma revisión que el resto de lo guardado.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Integridad** | Nada se pierde ni se pisa al mover |
| **Verificabilidad** | Se puede comprobar que el almacén quedó vacío |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), criterio CAE-06.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la regla de que el almacén queda vacío.
- [ ] Definir el destino de lo movido, según su tipo y alcance.
- [ ] Comprobar que el almacén está vacío.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local](A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local/resultado_pruebas.md#6-veredicto-de-la-fase) — el almacén queda vacío; el recogido se lleva también lo que no es recuerdo. Pendiente el commit |

**La fase retro-documenta.** El vaciado corre solo. La parte fina es el CA-02: que no quede un puntero — un puntero es peor que nada, porque parece que hay memoria donde no hay.

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
| Dependencia | HU-002, porque define el destino | Alto |
| Dependencia | EP-005, porque ahí se decide cuándo corre la recogida | Alto |
| Riesgo | Que la herramienta cambie dónde guarda | La ubicación se declara en un solo lugar |
| Riesgo | Que queden dos versiones del mismo recuerdo | Se mueve, no se copia, y eso es criterio de aceptación |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El almacén de la herramienta queda vacío
- [ ] No queda copia ni puntero
- [ ] Nada se pisa al mover
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el destino de HU-002 |
| **N**egociable | Sí | Cuándo se recoge se puede discutir |
| **V**aliosa | Sí | Evita memoria invisible que no viaja |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Mover con cuidado |
| **T**esteable | Sí | Se prueba dejando algo en el almacén |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. El almacén de la máquina está vacío y el puntero también se saca. CA-01 en «No»: el recogido no distingue qué es recuerdo, y resolverlo toca `01·C19` |
