# HU-002 — Capas de reglas y orden de precedencia

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | Quien define el estándar |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien define el estándar
- **Quiero** que las reglas estén separadas en capas con un orden declarado
- **Para** que un proyecto pueda ajustar lo que le corresponde sin poder aflojar lo que protege sus datos

## 3. Contexto y descripción

No todas las reglas valen lo mismo. Hay unas que un proyecto tiene buenas razones para ajustar, como la forma de nombrar sus carpetas. Y hay otras que ningún proyecto puede tocar, como no trabajar sobre datos reales.

Si todo está mezclado, o se vuelve todo negociable, o se vuelve todo rígido. Las dos cosas terminan igual: la gente se salta el estándar.

Esta historia separa las capas y escribe cuál gana cuando dos reglas dicen cosas distintas.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay una capa que ningún proyecto ni ninguna instrucción del chat puede sobrescribir |
| RN-02 | Hay una capa de convenciones que el proyecto sí puede ajustar |
| RN-03 | Hay una capa propia de cada proyecto, que es la que ajusta |
| RN-04 | La capa del proyecto ajusta a las convenciones, nunca a la capa que no se sobrescribe |
| RN-05 | Cada regla lleva escrito a qué capa pertenece |
| RN-06 | Una instrucción escrita en el chat no cambia la precedencia |

### 3.2 Supuestos

- La cantidad de reglas que de verdad no se pueden tocar es pequeña. Si crece mucho, la capa pierde sentido.

### 3.3 Fuera de alcance

- El contenido de cada capa. Acá se define la separación, no lo que va adentro.
- El mecanismo por el que un proyecto declara sus ajustes. Eso es HU-006.

## 4. Criterios de aceptación

### CA-01 — Una regla del proyecto ajusta una convención

```gherkin
Dado que existe una convención ajustable sobre cómo se nombran las cosas
Cuando un proyecto declara en su capa propia una forma distinta de nombrarlas
Entonces al trabajar en ese proyecto manda la forma que declaró el proyecto
```

**Cómo validarlo:**

1. Ubicar en el cuerpo de reglas una convención marcada como ajustable, por ejemplo la de nombres.
2. En un proyecto de prueba, escribir en su capa propia una convención distinta para lo mismo. Resultado esperado: queda declarada y se ve a qué regla de convención está ajustando.
3. Preguntarle a la IA, dentro de ese proyecto, cómo debe nombrar algo. Resultado esperado: responde según lo que declaró el proyecto, no según la convención general.
- **Aprobado cuando:** el proyecto obtiene su propia forma sin que nadie haya editado el cuerpo central.

### CA-02 — Un intento de aflojar la capa protegida no procede

```gherkin
Dado que existe una regla marcada como no sobrescribible
Cuando un proyecto declara en su capa propia algo que la contradice
Entonces sigue mandando la regla protegida
Y queda claro en el texto que ese ajuste no aplica
```

**Cómo validarlo:**

1. Ubicar una regla marcada como no sobrescribible, por ejemplo la de no trabajar sobre datos reales.
2. En el proyecto de prueba, escribir en su capa propia una excepción a esa regla. Resultado esperado: queda escrita, porque nadie impide escribir un archivo.
3. Preguntarle a la IA, dentro de ese proyecto, si puede hacer lo que la excepción permite. Resultado esperado: responde que no, citando la regla protegida y el orden de precedencia.
- **Aprobado cuando:** la regla protegida gana, y la respuesta dice por qué.

### CA-03 — Una instrucción del chat no cambia el orden

```gherkin
Dado que existe una regla marcada como no sobrescribible
Cuando alguien escribe en el chat una instrucción que la contradice
Entonces la regla sigue mandando
```

**Cómo validarlo:**

1. Abrir una sesión en el proyecto de prueba.
2. Escribir en el chat una instrucción que contradiga la regla protegida. Resultado esperado: la IA no la acata y dice cuál regla lo impide.
3. Insistir una vez más. Resultado esperado: la respuesta no cambia.
- **Aprobado cuando:** la instrucción del chat no logra aflojar la regla en ningún intento.

### Criterios de aceptación transversales

- [ ] **Límites** — está definido qué pasa cuando dos reglas de la misma capa se contradicen.
- [ ] **No regresión** — las reglas ya escritas conservan su marca de capa.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Claridad | La capa de una regla se ve al abrirla, sin buscarla en otro documento |
| Estabilidad | Una regla no cambia de capa sin que eso se registre como cambio del estándar |

## 6. Tareas técnicas derivadas

- [ ] Definir cuántas capas hay y qué va en cada una.
- [ ] Escribir el orden de precedencia y qué gana en cada choque.
- [ ] Definir la marca visible de capa en cada regla y en cada capítulo.
- [ ] Escribir qué pasa cuando una instrucción del chat contradice una regla.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

Todavía no se descompuso en fases. `02·F12.2` pide al menos una antes de empezar a trabajarla.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta historia de usuario |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada criterio | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el criterio quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001, porque la marca de capa es parte del molde de regla | Alto |
| Riesgo | Que la capa protegida crezca hasta volverlo todo rígido | Se define un criterio de qué merece estar ahí: solo lo que no se puede deshacer |
| Riesgo | Que la precedencia quede escrita pero nadie la aplique | Los ejemplos de choque se escriben junto con la regla |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] Las capas están definidas y escritas
- [ ] El orden de precedencia está escrito con ejemplos de choque
- [ ] Cada regla existente lleva su marca de capa
- [ ] Todos los criterios de aceptación verificados

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita el molde de HU-001 para la marca de capa |
| Negociable | Sí | La cantidad de capas se puede discutir |
| Valiosa | Sí | Sin precedencia, dos reglas que se contradicen dejan el trabajo trancado |
| Estimable | Sí | Alcance corto |
| Pequeña | Sí | Un documento y las marcas |
| Testeable | Sí | Se verifica provocando choques a propósito |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
