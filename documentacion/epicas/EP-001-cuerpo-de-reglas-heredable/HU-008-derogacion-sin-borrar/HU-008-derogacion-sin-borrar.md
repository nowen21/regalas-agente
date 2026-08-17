# HU-008 — Derogar una regla sin borrarla ni renumerarla

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | Quien define el estándar |
| **Estado** | Backlog |

## 2. Narrativa

- **Como** quien va a leer dentro de dos años un documento que cita una regla
- **Quiero** que esa regla siga existiendo aunque ya no se exija
- **Para** entender qué decía cuando el trabajo se hizo, en vez de encontrar una cita rota

## 3. Contexto y descripción

Las especificaciones, los commits y el trabajo cerrado citan las reglas por su identificador. Si una regla se borra, todas esas citas quedan apuntando a nada. Si se renumera, quedan apuntando a otra cosa, que es peor: se lee como si el trabajo hubiera cumplido algo que nunca se le exigió.

Esta historia define qué se hace cuando una regla deja de aplicar. La respuesta es derogarla: se queda escrita, marcada como sin vigencia, diciendo desde cuándo y qué la reemplaza.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Ninguna regla se borra |
| RN-02 | Ningún identificador se reutiliza ni se renumera |
| RN-03 | La regla derogada dice desde cuándo lo está y por qué |
| RN-04 | Si otra regla la reemplaza, la derogada la nombra |
| RN-05 | Una regla derogada no se cuenta como incumplida por nadie |

### 3.2 Supuestos

- Habrá reglas que dejen de tener sentido, porque el estándar va a cambiar con el tiempo.

### 3.3 Fuera de alcance

- El número de versión que acompaña a la derogación. Eso es EP-002.
- El programa que detecta que una regla desapareció entre dos versiones. Eso es EP-004.

## 4. Criterios de aceptación

### CA-01 — Una regla derogada sigue siendo legible

```gherkin
Dado que una regla dejó de aplicar y fue derogada
Cuando alguien sigue una cita vieja hasta esa regla
Entonces la encuentra, con su texto original
Y ve que está derogada, desde cuándo y por qué
```

**Cómo validarlo:**

1. Tomar una regla existente y derogarla siguiendo el procedimiento.
2. Desde un documento viejo que la citaba, seguir la cita. Resultado esperado: llega a la regla, no a un enlace roto.
3. Leer la regla. Resultado esperado: se ve el texto original, la marca de derogada, la fecha y el motivo.
- **Aprobado cuando:** la cita vieja sigue llevando a un texto legible que se explica solo.

### CA-02 — Un identificador liberado no se reutiliza

```gherkin
Dado que una regla fue derogada
Cuando se crea una regla nueva en el mismo capítulo
Entonces recibe un identificador libre, distinto al de la derogada
```

**Cómo validarlo:**

1. Anotar el identificador de la regla que se derogó.
2. Crear una regla nueva en ese mismo capítulo siguiendo el procedimiento. Resultado esperado: el identificador que le toca es uno que nunca se usó.
3. Revisar el capítulo completo. Resultado esperado: el identificador de la derogada aparece una sola vez, en ella.
- **Aprobado cuando:** ningún identificador aparece dos veces en la historia del capítulo.

### CA-03 — Una regla derogada no se cuenta como incumplimiento

```gherkin
Dado que existe una regla derogada
Cuando se revisa un proyecto contra el cuerpo de reglas
Entonces la derogada no aparece como algo por cumplir
```

**Cómo validarlo:**

1. Revisar un proyecto de prueba contra el cuerpo de reglas y leer la lista de lo que se le exige.
2. Buscar en esa lista la regla derogada. Resultado esperado: no está.
3. Buscar la regla que la reemplazó, si hay. Resultado esperado: esa sí está.
- **Aprobado cuando:** la derogada no exige nada y su reemplazo sí.

### Criterios de aceptación transversales

- [ ] **Límites** — está definido qué pasa cuando la regla derogada no tiene reemplazo.
- [ ] **No regresión** — derogar una regla no reabre trabajo ya cerrado.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Permanencia | El texto de una regla derogada no se edita ni se resume |
| Visibilidad | La marca de derogada se ve al abrir la regla, sin buscar en otro lado |
| Trazabilidad | La derogada nombra a la que la reemplaza, si existe |

## 6. Tareas técnicas derivadas

- [ ] Escribir la regla que prohíbe borrar y renumerar.
- [ ] Definir la marca de derogada y qué datos lleva.
- [ ] Definir dónde queda la regla derogada dentro de su capítulo.
- [ ] Escribir qué hacer cuando no hay reemplazo.

## 7. Fases que la implementan

> Trazabilidad hacia abajo. Se completa a medida que la historia se descompone en fases (`02·F12.2`). El enlace se escribe en los dos lados: la fase declara qué criterios cubre y acá se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-001-HU-008-retrodocumentar-la-derogacion](A-EP-001-HU-008-retrodocumentar-la-derogacion/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase retro-documenta y agrega dos pruebas.** La derogación ya se usó ocho veces —`F4.1` a `F4.5`, `F6`, `F7` e `ID2`—, y nada comprueba que sigan ahí: si mañana alguien borra una, nadie se entera.

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
| Dependencia | HU-001, por el identificador estable | Alto |
| Dependencia | HU-007, porque derogar es parte del procedimiento de mantener el cuerpo | Alto |
| Riesgo | Que el capítulo se llene de reglas derogadas y estorbe la lectura | Se define dónde quedan, separadas de las vigentes |
| Riesgo | Que alguien borre una regla por costumbre | La prohibición queda escrita y es candidata a comprobarse con un programa |

## 9. Definition of Ready

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y verificables
- [ ] Formato del identificador ya definido
- [ ] Dependencias identificadas

## 10. Definition of Done

- [ ] La regla que prohíbe borrar y renumerar está escrita
- [ ] La marca de derogada está definida y aplicada a un caso de prueba
- [ ] Una cita vieja sigue llevando a un texto legible
- [ ] Todos los criterios de aceptación verificados

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Parcial | Necesita el identificador estable |
| Negociable | Sí | Dónde queda la derogada se discute |
| Valiosa | Sí | Es lo que sostiene que una cita de hace años siga sirviendo |
| Estimable | Sí | Alcance corto |
| Pequeña | Sí | Una regla y una marca |
| Testeable | Sí | Se verifica derogando una regla de prueba |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
