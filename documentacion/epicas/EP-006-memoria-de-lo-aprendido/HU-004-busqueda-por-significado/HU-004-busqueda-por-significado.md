# HU-004 — Buscar por significado con un modelo local y opcional

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien no recuerda con qué palabras se guardó algo
- **Quiero** buscar por significado y no solo por la palabra exacta
- **Para** encontrar lo que se escribió con otras palabras hace meses

---

## 3. Contexto y descripción

La búsqueda por palabra falla justo cuando más se necesita: cuando lo que se busca se escribió con otras palabras. "Cobro duplicado" no encuentra "el pago se aplicó dos veces".

Buscar por significado resuelve eso, pero trae una condición que no se negocia: el contenido no puede salir de la máquina. Por eso el modelo corre localmente.

Y es opcional. Si el modelo no está, la búsqueda por palabra sigue funcionando. Una función que rompe todo cuando falta una pieza no es una mejora.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se puede buscar por significado, no solo por palabra exacta |
| RN-02 | El modelo corre en la máquina: el contenido no sale de ahí |
| RN-03 | Es opcional: si el modelo no está, la búsqueda por palabra sigue funcionando |
| RN-04 | Si no está, se dice, en vez de devolver resultados peores en silencio |
| RN-05 | Buscar no modifica lo guardado |

### 3.2 Supuestos

- Existe un modelo que corre en una máquina común sin equipo especial.

### 3.3 Fuera de alcance

- Procesar el contenido fuera de la máquina, por ningún motivo.
- Elegir el modelo concreto en esta historia; se declara aparte.

---

## 4. Criterios de aceptación

### CA-01 — Encuentra lo que se escribió con otras palabras

```gherkin
Dado que hay algo guardado escrito con unas palabras
Cuando se busca lo mismo con palabras distintas
Entonces aparece
```

**Cómo validarlo:**

1. Guardar algo describiendo un problema con unas palabras concretas.
2. Buscarlo con un sinónimo o una frase distinta. Resultado esperado: aparece entre los primeros resultados.
3. Repetir la misma búsqueda por palabra exacta. Resultado esperado: no aparece, que es la diferencia que justifica esta historia.
- **Aprobado cuando:** encuentra lo que la búsqueda por palabra no encuentra.

### CA-02 — Sin el modelo, la búsqueda sigue funcionando

```gherkin
Dado que el modelo no está instalado
Cuando se busca
Entonces la búsqueda por palabra funciona igual
Y se dice que la búsqueda por significado no está disponible
```

**Cómo validarlo:**

1. Quitar el modelo del entorno de prueba.
2. Buscar. Resultado esperado: responde por palabra y avisa que la otra no está.
3. Volver a poner el modelo y buscar. Resultado esperado: vuelve a buscar por significado.
- **Aprobado cuando:** faltar el modelo no rompe nada.

### Criterios de aceptación transversales

- [ ] **Privacidad** — el contenido no sale de la máquina en ningún momento.
- [ ] **Rendimiento** — la primera búsqueda puede tardar más; las siguientes no.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Privacidad** | Todo el procesamiento ocurre en la máquina |
| **Degradación** | Sin el modelo, se sigue pudiendo buscar |
| **Rendimiento** | Aceptable en una máquina común, sin equipo especial |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), criterios CAE-04 y CAE-05.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Elegir y declarar el modelo local.
- [ ] Preparar lo guardado para poder compararlo por significado.
- [ ] Devolver los resultados ordenados por cercanía.
- [ ] Detectar que el modelo no está y avisar sin romper.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

Todavía no se descompuso en fases.

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
| Dependencia | HU-003, porque es la que sigue funcionando cuando esta no está | Alto |
| Riesgo | Que el modelo sea pesado y nadie lo instale | Es opcional, y su ausencia no rompe nada |
| Riesgo | Que se caiga en la tentación de procesar fuera de la máquina | Está prohibido y es criterio de aceptación |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Encuentra lo escrito con otras palabras
- [ ] Sin el modelo, la búsqueda por palabra sigue funcionando
- [ ] El contenido no sale de la máquina
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Se apoya en la búsqueda por palabra |
| **N**egociable | Sí | El modelo concreto se puede discutir |
| **V**aliosa | Sí | Encuentra justo lo que la otra búsqueda pierde |
| **E**stimable | Parcial | Depende del modelo que se elija |
| **S**mall (pequeña) | No | Es la más grande de la épica |
| **T**esteable | Sí | Se prueba buscando con sinónimos |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
