# HU-038 — El agente escribe solo sobre el asunto en curso

> Nace del [pendiente 95](../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md), aprobado por el usuario el 2026-09-27.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-038 |
| **Épica / Feature** | [EP-001 — Cuerpo de reglas heredable y en capas](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas, capítulo 00 |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | 2 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

- **Como** lector de lo que el agente entrega
- **Quiero** que cada dato, explicación o comentario sirva al asunto que se está tratando
- **Para** no tener que decidir, dato por dato, cuál me sirve y cuál sobra

---

## 3. Contexto y descripción

Ninguna regla exige que el agente se quede en el asunto. `00·ID9` y `01·C5` exigen extensión, y un dato corto y claro que no tiene que ver con el tema cumple las dos.

El caso que lo destapó: el pendiente de la norma colombiana decía «No entra en HU-037, que está terminada y dejó la norma fuera de su alcance». Era cierto y corto, y no le servía al pendiente.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La regla rige todo lo que el agente entrega: documentos y respuesta del chat |
| RN-02 | Un dato sirve al asunto si cambia lo que el lector decide o hace sobre ese asunto |
| RN-03 | Lo que no sirve al asunto se quita aunque sea cierto y corto |
| RN-04 | La regla extiende `00·ID7`, `00·ID8` y `00·ID9`, y las tres siguen rigiendo |
| RN-05 | Se cumple releyendo antes de entregar: ningún programa decide si un dato sirve al asunto |

### 3.2 Supuestos

- El identificador `00·ID11` sigue libre al construir la regla.

### 3.3 Fuera de alcance

- La extensión del texto, que sigue en `ID9` y `C5`.
- Un validador automático, por la RN-05.

---

## 4. Criterios de aceptación

### CA-01 — La regla existe, con su identificador y su checklist

```gherkin
Dado que ninguna regla exige quedarse en el asunto
Cuando se escribe la regla por el procedimiento de las meta-reglas
Entonces existe con una sola exigencia, su ejemplo y su checklist en CUMPLE
Y aparece en la tabla del capítulo 00
```

**Cómo validarlo:**
1. Abrir `base/00-identidad-y-rol/reglas/ID11-escribe-solo-sobre-el-asunto-en-curso.md` → resultado esperado: el cuerpo exige tratar solo el asunto en curso y trae el ejemplo INCORRECTO/CORRECTO.
2. Abrir `base/00-identidad-y-rol/base.md` → resultado esperado: `ID11` está en la tabla de reglas.
3. Correr `python validadores/validar.py metareglas` → resultado esperado: 0 fallas.

Se aprueba cuando los tres pasos dan lo esperado.

### CA-02 — La regla declara en qué se apoya

```gherkin
Dado que la regla existe
Cuando se lee su cuerpo
Entonces declara "extiende 00·ID7, 00·ID8 y 00·ID9" entre paréntesis
```

**Cómo validarlo:**
1. Leer el cuerpo de la regla → resultado esperado: la dependencia está entre paréntesis, con las tres reglas enlazadas.
2. Correr `python validadores/validar.py estandar` → resultado esperado: sin incumplimientos.

Se aprueba cuando la dependencia está declarada como pide `M7` y los enlaces resuelven.

### CA-03 — La regla queda clasificada como no validable

```gherkin
Dado que la regla existe
Cuando se busca en el registro de reglas comprobables
Entonces aparece como no validable, con el motivo de la RN-05
```

**Cómo validarlo:**
1. Buscar `ID11` en `validadores/reglas-validables.md` → resultado esperado: una fila que la marca como no validable y dice por qué.

Se aprueba cuando la fila existe con su motivo.

### CA-04 — Los pendientes abiertos de la sesión cumplen la regla

```gherkin
Dado que la regla existe
Cuando se releen los pendientes 96 y 97 contra ella
Entonces ninguno lleva un dato que no sirva a su asunto
```

**Cómo validarlo:**
1. Releer `pendientes/96-la-norma-del-espanol-de-colombia-no-tiene-regla.md` → resultado esperado: sin la frase sobre HU-037 ni otro dato ajeno a la norma colombiana.
2. Releer `pendientes/97-el-andamio-exige-la-historia-antes-que-el-pendiente.md` → resultado esperado: sin la frase sobre la épica candidata ni otro dato ajeno al andamio.

Se aprueba cuando el usuario lee los dos y no encuentra nada que sobre.

### Criterios de aceptación transversales

- [ ] **No regresión** — `validar.py metareglas`, `estandar` y `pendientes` quedan sin fallas.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | La regla se registra en `CHANGELOG.md` y sube `VERSION` como MENOR |
| RNF-02 | **Compatibilidad** | Rige lo que se entregue de aquí en adelante: ningún documento ya escrito se reescribe por ella, salvo los del CA-04 |

---

## 6. Diseño y referencias

- Documento funcional: el [pendiente 95](../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md)

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la regla, con su checklist aplicado
- [ ] Agregarla a la tabla del capítulo 00
- [ ] Clasificarla en `validadores/reglas-validables.md`
- [ ] Releer los pendientes 96 y 97 contra ella
- [ ] Versionar y registrar el cambio
- [ ] Cerrar el pendiente 95

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-001-HU-038-la-regla-del-asunto-en-curso` | CA-01 a CA-04 | | por escribir | por escribir | | Sin empezar |

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
| Riesgo | Que la regla se lea como otra forma de pedir textos cortos | El ejemplo muestra una frase corta que igual sobra |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Regla escrita y en rama principal
- [ ] Validadores sin fallas
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No espera a otra historia |
| **N**egociable | ☑ | La redacción del cuerpo se ajusta en la fase |
| **V**aliosa | ☑ | Hoy un dato que sobra no incumple ninguna regla |
| **E**stimable | ☑ | Una regla, un registro y dos pendientes para releer |
| **S**mall (pequeña) | ☑ | Una fase |
| **T**esteable | ☑ | Tres criterios se comprueban con validadores y uno leyendo |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-27 | El agente | Creación de la HU, a partir del pendiente 95 |
