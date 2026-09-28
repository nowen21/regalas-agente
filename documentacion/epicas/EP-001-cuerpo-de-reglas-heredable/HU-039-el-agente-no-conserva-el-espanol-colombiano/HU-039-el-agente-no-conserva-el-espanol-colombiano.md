# HU-039 · El agente no conserva el español colombiano

> Nace del [pendiente 96](../../../../pendientes/96-el-agente-no-conserva-el-espanol-colombiano.md), aprobado por el usuario el 2026-09-27.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-039 |
| **Épica / Feature** | [EP-001 · Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas, capítulo 00 |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | 3 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Terminada |

## 2. Narrativa

- **Como** lector colombiano de lo que el agente entrega
- **Quiero** que sus textos sigan la ortografía, el léxico, la gramática y la redacción del español de Colombia
- **Para** leerlos con naturalidad, sin tener que corregirle palabras ni formas de otro país

## 3. Contexto y descripción

Ninguna regla le exige al agente seguir las normas ortográficas, léxicas, gramaticales y de redacción del español de Colombia. Por eso sus textos pueden traer palabras, expresiones o formas de redacción que no son las de aquí, y eso afecta la claridad y la naturalidad de lo que entrega.

Lo que el estándar tiene hoy no alcanza: [`00·ID10`](../../../../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md) pide escribir en la variedad del idioma del proyecto, pero no dice qué es escribirla bien; y la sección 5 de [`marcadores-de-ia.md`](../../../../base/00-identidad-y-rol/marcadores-de-ia.md#L73) trae palabras de España con su equivalente colombiano, pero como marca de texto generado por máquina, no como norma.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La norma rige lo que el agente entrega en un proyecto que declara español de Colombia: documentos y respuestas del chat |
| RN-02 | La norma cubre cuatro frentes: ortografía, léxico, gramática y redacción |
| RN-03 | Escribir en la variedad del proyecto no basta: el texto también debe cumplir la norma de esa variedad |
| RN-04 | Lo que hoy vive como marca de texto generado y es norma, el léxico de la sección 5 del anexo de `00·ID8`, pasa a la norma y deja de estar en dos sitios |

### 3.2 Supuestos

- El identificador `00·ID12` sigue libre al construir la regla.

### 3.3 Fuera de alcance

- La persona y la forma verbal, que siguen en `00·ID10`.
- Otras variedades del español y otros idiomas.
- El texto que ve el usuario final de un producto, que gobierna `17·I4`.
- Construir el conteo automático en `validadores/marcas.py`: aquí solo se clasifica qué parte se puede contar.

## 4. Criterios de aceptación

### CA-01 · La regla existe, con su identificador y su checklist

```gherkin
Dado que ninguna regla exige la norma del español de Colombia
Cuando se escribe la regla por el procedimiento de las meta-reglas
Entonces existe con una sola exigencia, su ejemplo y su checklist en CUMPLE
Y aparece en la tabla del capítulo 00
```

**Cómo validarlo:**
1. Abrir `base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md` → resultado esperado: tiene encabezado en imperativo, cuerpo, ejemplo INCORRECTO/CORRECTO y checklist en CUMPLE.
2. Abrir `base/00-identidad-y-rol/base.md` → resultado esperado: `ID12` está en la tabla de reglas.
3. Correr `python validadores/validar.py metareglas` → resultado esperado: 0 fallas.

Se aprueba cuando los tres pasos dan lo esperado.

### CA-02 · El cuerpo de la regla recoge las reglas de negocio

```gherkin
Dado que la regla existe
Cuando se lee su cuerpo
Entonces dice que rige documentos y chat en un proyecto que declara español de Colombia
Y nombra ortografía, léxico, gramática y redacción
Y declara "extiende 00·ID8" entre paréntesis
```

**Cómo validarlo:**
1. Leer el cuerpo de la regla → resultado esperado: dice a qué contenido aplica y con qué condición (RN-01).
2. En el mismo cuerpo → resultado esperado: nombra los cuatro frentes (RN-02).
3. En el mismo cuerpo → resultado esperado: la dependencia `extiende 00·ID8`, enlazada.
4. Correr `python validadores/validar.py estandar` → resultado esperado: sin incumplimientos.

Se aprueba cuando los cuatro pasos dan lo esperado.

### CA-03 · El anexo existe con sus cuatro secciones

```gherkin
Dado que la regla remite a un anexo
Cuando se abre base/00-identidad-y-rol/espanol-de-colombia.md
Entonces tiene una sección por frente: ortografía, léxico, gramática y redacción
```

**Cómo validarlo:**
1. Abrir `base/00-identidad-y-rol/espanol-de-colombia.md` → resultado esperado: cuatro secciones, una por frente, cada una con su tabla de qué se escribe y qué no.

Se aprueba cuando el anexo existe con las cuatro secciones.

### CA-04 · El léxico queda en un solo sitio

```gherkin
Dado que el anexo de la norma existe
Cuando se abre la sección 5 de marcadores-de-ia.md
Entonces remite al anexo nuevo en vez de repetir la tabla
Y la línea que decía que la regla "todavía no existe" cita 00·ID10 y 00·ID12
```

**Cómo validarlo:**
1. Abrir la sección 5 de `base/00-identidad-y-rol/marcadores-de-ia.md` → resultado esperado: una línea que remite a `espanol-de-colombia.md`, sin la tabla de léxico.
2. Abrir «Lo que este anexo no cubre» en el mismo archivo → resultado esperado: ya no dice que la regla no existe; cita `ID10` e `ID12`.

Se aprueba cuando los dos pasos dan lo esperado (RN-04).

### CA-05 · El ejemplo incumple los cuatro frentes

```gherkin
Dado que la regla existe
Cuando se lee su ejemplo INCORRECTO
Entonces trae una falta de ortografía, una de léxico, una de gramática y una de redacción
Y el CORRECTO las resuelve todas
```

**Cómo validarlo:**
1. Leer el ejemplo INCORRECTO → resultado esperado: se puede señalar una falta de cada frente.
2. Leer el ejemplo CORRECTO → resultado esperado: ninguna de esas faltas sigue.

Se aprueba cuando cada frente tiene su falta en el INCORRECTO y ninguna queda en el CORRECTO (RN-03).

### CA-06 · Un proyecto que no declara español de Colombia no queda obligado

```gherkin
Dado un proyecto que declara otro idioma u otra variedad
Cuando se lee la regla
Entonces su condición lo deja fuera
```

**Cómo validarlo:**
1. Leer el comienzo del cuerpo de la regla → resultado esperado: la exigencia empieza con «Si el proyecto declara español de Colombia».

Se aprueba cuando la condición está en el cuerpo, que es lo que la deja entrar en `base/` sin romper `20·M3`.

### CA-07 · La regla queda clasificada como validable en parte

```gherkin
Dado que la regla existe
Cuando se busca en el registro de reglas comprobables
Entonces dice qué parte se puede contar y cuál hay que leer
```

**Cómo validarlo:**
1. Buscar `ID12` en `validadores/reglas-validables.md` → resultado esperado: una fila que dice que se pueden contar las tildes de pregunta, los signos de apertura, *vosotros*, *os* y el léxico de España, y que la concordancia y el régimen de las preposiciones se leen.

Se aprueba cuando la fila existe con las dos partes.

### Criterios de aceptación transversales

- [ ] No regresión: `validar.py metareglas`, `estandar` y `pendientes` quedan sin fallas.

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | La regla se registra en `CHANGELOG.md` y sube `VERSION` como MENOR |
| RNF-02 | **Compatibilidad** | Rige lo que se entregue de aquí en adelante: ningún documento ya escrito se reescribe por ella |

## 6. Diseño y referencias

- Documento funcional: el [pendiente 96](../../../../pendientes/96-el-agente-no-conserva-el-espanol-colombiano.md)
- Regla que la nueva extiende: [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), con su anexo [`marcadores-de-ia.md`](../../../../base/00-identidad-y-rol/marcadores-de-ia.md)
- Regla que no cambia: [`00·ID10`](../../../../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md)

## 7. Tareas técnicas derivadas

- [x] Escribir la regla, con su checklist aplicado
- [x] Escribir el anexo `espanol-de-colombia.md` con sus cuatro secciones
- [x] Llevar el léxico de la sección 5 de `marcadores-de-ia.md` al anexo y actualizar su cierre
- [x] Agregar la regla a la tabla del capítulo 00
- [x] Clasificarla en `validadores/reglas-validables.md`
- [x] Versionar y registrar el cambio
- [x] Cerrar el pendiente 96

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano`](A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano/) | CA-01 a CA-07 | | [plan_trabajo](A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano/plan_trabajo.md) | [plan_pruebas](A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano/plan_pruebas.md) | [resultado](A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano/resultado_pruebas.md) · cumple | Cerrada |

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
| Riesgo | Que el anexo se llene de localismos que un lector de otra región no entienda | Cada entrada del léxico lleva la palabra que se usa en Colombia y se entiende en todo el país, no la jerga regional |
| Riesgo | Que al sacar la tabla de léxico de `marcadores-de-ia.md`, `marcas.py` deje de contar algo que hoy cuenta | Antes de moverla se comprueba qué lee `marcas.py` de esa sección |

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Regla y anexo escritos y en rama principal
- [x] Validadores sin fallas
- [x] Todos los criterios de aceptación verificados
- [x] Requisitos no funcionales validados
- [ ] Aceptada por el usuario

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No espera a otra historia |
| **N**egociable | ☑ | El contenido del anexo se ajusta en la fase |
| **V**aliosa | ☑ | Hoy un texto con léxico de España o sin tildes no incumple ninguna regla |
| **E**stimable | ☑ | Una regla, un anexo y dos ajustes en el anexo de marcas |
| **S**mall (pequeña) | ☑ | Una fase |
| **T**esteable | ☑ | Tres criterios se comprueban con validadores o buscando en archivos, y cuatro leyendo |

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-27 | El agente | Creación de la HU, a partir del pendiente 96 |
| 2026-09-27 | El agente | Fase `A` cerrada con veredicto Cumple: la regla `00·ID12` y su anexo, versión 38.2.0 |
