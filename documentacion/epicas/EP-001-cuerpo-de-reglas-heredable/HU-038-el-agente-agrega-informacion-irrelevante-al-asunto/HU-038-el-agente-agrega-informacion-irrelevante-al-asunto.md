# HU-038 · El agente agrega información irrelevante al asunto que está tratando

> Nace del [pendiente 95](../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md), aprobado por el usuario el 2026-09-27.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-038 |
| **Épica / Feature** | [EP-001 · Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas, capítulo 00 |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | 2 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Terminada |

## 2. Narrativa

- **Como** lector del contenido generado por el agente
- **Quiero** que cada dato, explicación o comentario esté directamente relacionado con el asunto que se está tratando
- **Para** no tener que revisar y decidir qué información es pertinente y cuál debe ser descartada.

## 3. Contexto y descripción

Ninguna regla de `base/` establece que el contenido generado por el agente deba limitarse estrictamente al asunto que se está tratando.

- **00·ID9** exige expresar lo mismo en menos palabras, pero no establece que la información deba ser relevante para el tema.
- **01·C5** exige respuestas cortas, tampoco pide pertinencia, y solo rige el chat.

Por lo tanto, el agente puede cumplir ambas reglas y, aun así, agregar información breve, clara y completamente irrelevante para el asunto que está trabajando.

El problema no es la **extensión** de la información, sino su **pertinencia respecto al tema, objetivo y alcance del elemento que se está tratando**.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La regla aplica a todo el contenido que genere el agente, tanto en **documentos como en las respuestas del chat**. |
| RN-02 | Un dato se considera pertinente cuando está directamente relacionado con el **tema, objetivo y alcance** del elemento que se está tratando y aporta a su comprensión, análisis, resolución o documentación.|
| RN-03 | La información que no sea pertinente debe omitirse, aunque sea **breve, clara y correcta**. |
| RN-04 | La pertinencia debe evaluarse de forma independiente de la extensión del contenido: cumplir con `00·ID9` y `01·C5` **no garantiza que la información sea pertinente**.|

### 3.2 Supuestos

- El identificador `00·ID11` sigue libre al construir la regla.

### 3.3 Fuera de alcance

- La extensión del contenido, que sigue en `00·ID9` y `01·C5`.
- Un validador automático: decidir si un dato es pertinente pide leerlo.

## 4. Criterios de aceptación

### CA-01 · La regla existe, con su identificador y su checklist

```gherkin
Dado que ninguna regla exige que el contenido sea pertinente
Cuando se escribe la regla por el procedimiento de las meta-reglas
Entonces existe con una sola exigencia, su ejemplo y su checklist en CUMPLE
Y aparece en la tabla del capítulo 00
```

**Cómo validarlo:**
1. Abrir `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` → resultado esperado: el archivo existe, con cuerpo, ejemplo INCORRECTO/CORRECTO y checklist en CUMPLE.
2. Abrir `base/00-identidad-y-rol/base.md` → resultado esperado: `ID11` está en la tabla de reglas.
3. Correr `python validadores/validar.py metareglas` → resultado esperado: 0 fallas.

Se aprueba cuando los tres pasos dan lo esperado.

### CA-02 · El cuerpo de la regla recoge las cuatro reglas de negocio

```gherkin
Dado que la regla existe
Cuando se lee su cuerpo
Entonces dice que rige los documentos y las respuestas del chat
Y que un dato es pertinente si se relaciona con el tema, el objetivo y el alcance del elemento que se está tratando
Y que lo no pertinente se omite aunque sea breve, claro y correcto
Y que cumplir 00·ID9 y 01·C5 no garantiza la pertinencia
```

**Cómo validarlo:**
1. Leer el cuerpo de la regla → resultado esperado: dice a qué contenido aplica (RN-01).
2. En el mismo cuerpo → resultado esperado: dice contra qué se mide la pertinencia (RN-02).
3. En el mismo cuerpo → resultado esperado: dice que lo no pertinente se omite aunque sea breve, claro y correcto (RN-03).
4. En el cuerpo o en su ejemplo → resultado esperado: queda claro que un texto corto también puede incumplirla (RN-04).

Se aprueba cuando las cuatro reglas de negocio se leen en la regla.

### CA-03 · La regla declara en qué se apoya

```gherkin
Dado que la regla existe
Cuando se lee su cuerpo
Entonces declara "extiende 00·ID7, 00·ID8 y 00·ID9" entre paréntesis
```

**Cómo validarlo:**
1. Leer el cuerpo de la regla → resultado esperado: la dependencia está entre paréntesis, con las tres reglas enlazadas.
2. Correr `python validadores/validar.py estandar` → resultado esperado: sin incumplimientos.

Se aprueba cuando la dependencia está declarada como pide `20·M7` y los enlaces resuelven.

### CA-04 · La regla queda clasificada como no validable

```gherkin
Dado que la regla existe
Cuando se busca en el registro de reglas comprobables
Entonces aparece como no validable, porque decidir si un dato es pertinente pide leerlo
```

**Cómo validarlo:**
1. Buscar `ID11` en `validadores/reglas-validables.md` → resultado esperado: una fila que la marca como no validable y dice por qué.

Se aprueba cuando la fila existe con su motivo.

### Criterios de aceptación transversales

- [ ] No regresión: `validar.py metareglas`, `estandar` y `pendientes` quedan sin fallas.

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | La regla se registra en `CHANGELOG.md` y sube `VERSION` como MENOR |
| RNF-02 | **Compatibilidad** | Rige lo que se entregue de aquí en adelante: ningún documento ya escrito se reescribe por ella |

## 6. Diseño y referencias

- Documento funcional: el [pendiente 95](../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md)
- Reglas que la nueva extiende: [`00·ID7`](../../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) y [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)

## 7. Tareas técnicas derivadas

- [x] Escribir la regla, con las cuatro reglas de negocio y su checklist aplicado
- [x] Agregarla a la tabla del capítulo 00
- [x] Clasificarla en `validadores/reglas-validables.md`
- [x] Versionar y registrar el cambio
- [x] Cerrar el pendiente 95

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto`](A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/) | CA-01 a CA-04 | | [plan_trabajo](A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/plan_trabajo.md) | [plan_pruebas](A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/plan_pruebas.md) | [resultado](A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto/resultado_pruebas.md) · cumple | Cerrada |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la regla se lea como otra forma de pedir textos cortos | La RN-04 y el ejemplo de la regla muestran una frase corta que igual sobra |
| Riesgo | Que al aplicarla se quite un dato que sí era pertinente | La RN-02 pide juzgar cada dato contra el tema, el objetivo y el alcance del elemento, no contra el gusto de quien relee |

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Regla escrita y en rama principal (al commitear)
- [x] Validadores sin fallas
- [x] Todos los criterios de aceptación verificados
- [x] Requisitos no funcionales validados
- [ ] Aceptada por el usuario

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No espera a otra historia |
| **N**egociable | ☑ | La redacción del cuerpo se ajusta en la fase |
| **V**aliosa | ☑ | Hoy un dato que no es pertinente no incumple ninguna regla |
| **E**stimable | ☑ | Una regla y su registro |
| **S**mall (pequeña) | ☑ | Una fase |
| **T**esteable | ☑ | Dos criterios se comprueban con validadores y dos leyendo |

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-27 | El agente | Creación de la HU, a partir del pendiente 95 |
| 2026-09-27 | El usuario | Título y contexto tomados del pendiente 95; narrativa y reglas de negocio RN-01 a RN-04 redactadas por el usuario |
| 2026-09-27 | El agente | Reescrita con la plantilla: CA-02 para las reglas de negocio, riesgo de quitar lo pertinente, referencias a `00·ID7`, `00·ID8` y `00·ID9` |
| 2026-09-27 | El agente | CA-06: el caso borde de un dato que parece ajeno pero es pertinente |
| 2026-09-27 | El usuario | Salen el CA-05 y el CA-06: aplicar la regla a los pendientes 96 y 97 no es parte de esta HU |
| 2026-09-27 | El agente | Fase `A` cerrada con veredicto Cumple: la regla `00·ID11` existe, versión 38.1.0 |
