# HU-002 — Marcar en cada regla si es comprobable

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Cuerpo de reglas |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien define el estándar
- **Quiero** que cada regla diga si un programa la comprueba, y cuál
- **Para** saber de un vistazo qué parte del estándar se sostiene sola y qué parte depende de que alguien se acuerde

---

## 3. Contexto y descripción

Una regla comprobable que ningún programa revisa es una regla que no se cumple. El problema es que hoy no hay forma de saber cuáles son: habría que abrir los programas, leerlos y deducir qué reglas tocan.

Esta historia cierra ese hueco con un registro único: una lista donde toda regla del estándar aparece clasificada, con el programa que la revisa cuando lo hay. Así la pregunta deja de responderse leyendo código.

El registro sirve además para lo contrario, que es lo que más duele: ver qué reglas se podrían comprobar y todavía no se comprueban.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Toda regla del estándar aparece en el registro, sin excepción |
| RN-02 | Cada regla queda en una de tres listas: ya comprobada, comprobable pendiente, o criterio |
| RN-03 | La regla ya comprobada nombra el programa que la revisa y qué revisa de ella |
| RN-04 | La regla comprobable pendiente dice por qué todavía no se comprueba |
| RN-05 | Clasificar la regla es parte de escribirla, no un paso posterior |
| RN-06 | El registro dice contra qué versión del estándar se hizo la foto |

### 3.2 Supuestos

- La clasificación envejece: al agregar o cambiar reglas hay que revisarla. Se asume que eso se hace en el mismo movimiento del cambio.

### 3.3 Fuera de alcance

- Escribir los programas que faltan. Acá se registra qué falta, no se construye.
- El criterio con el que se clasifica. Eso es HU-001.

---

## 4. Criterios de aceptación

### CA-01 — Toda regla aparece clasificada

```gherkin
Dado que el estándar tiene su cuerpo de reglas escrito
Cuando se recorre el registro de clasificación
Entonces cada regla del estándar aparece en una de las tres listas
Y ninguna aparece en dos
```

**Cómo validarlo:**

1. Contar las reglas del estándar recorriendo los capítulos.
2. Contar las que nombra el registro, sumando las tres listas. Resultado esperado: los dos números coinciden.
3. Buscar una regla cualquiera en el registro. Resultado esperado: aparece una sola vez.
- **Aprobado cuando:** no queda ninguna regla sin clasificar ni ninguna clasificada dos veces.

### CA-02 — La regla comprobada dice quién la comprueba

```gherkin
Dado que una regla está en la lista de las ya comprobadas
Cuando se lee su fila
Entonces nombra el programa que la revisa
Y dice qué parte de la regla revisa ese programa
```

**Cómo validarlo:**

1. Abrir el registro y tomar tres reglas de la lista de comprobadas.
2. Leer la fila de cada una. Resultado esperado: trae el nombre del programa y la descripción de qué comprueba.
3. Abrir uno de esos programas. Resultado esperado: lo que dice el registro es lo que el programa hace.
- **Aprobado cuando:** las tres filas nombran su programa y lo que dicen coincide con el programa.

### CA-03 — Una regla nueva no se publica sin clasificar

```gherkin
Dado que se escribe una regla nueva
Cuando se termina de escribirla
Entonces queda registrada en la lista que le corresponde
Y el procedimiento no se da por cerrado hasta que eso pasa
```

**Cómo validarlo:**

1. Escribir una regla de prueba siguiendo el procedimiento del estándar.
2. Llegar al paso de clasificación. Resultado esperado: el procedimiento lo exige de forma explícita, no como recomendación.
3. Buscar la regla nueva en el registro. Resultado esperado: aparece con su clasificación.
- **Aprobado cuando:** la regla nueva quedó registrada antes de que el cambio se versione.

### Criterios de aceptación transversales

- [ ] **Límites** — está definido qué se hace con una regla derogada: se conserva en el registro, marcada como tal.
- [ ] **No regresión** — la clasificación existente no se pierde al agregar reglas nuevas.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | El registro se lee sin abrir ningún programa |
| **Trazabilidad** | Dice contra qué versión del estándar se hizo la clasificación |
| **Mantenimiento** | Está en un archivo único, para que no haya dos versiones de la verdad |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, no hay interfaz.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), criterio de aceptación CAE-02.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir las tres listas y qué significa cada una.
- [ ] Clasificar todas las reglas existentes.
- [ ] Escribir, por cada regla comprobada, qué programa la revisa.
- [ ] Sumar el paso de clasificación al procedimiento de escribir una regla.
- [ ] Comprobar sola la propia clasificación: que ninguna regla quede fuera del registro.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla](A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase retro-documenta.** La clasificación está completa desde el 2026-08-16. Lo que la vigila es un programa que **no se puede correr**, así que la comprobación se lleva a la suite, que sí corre.

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
| Dependencia | HU-001, porque sin criterio la clasificación es opinión | Alto |
| Riesgo | Que el registro envejezca y deje de coincidir con las reglas | Un programa comprueba que ninguna regla falte en el registro |
| Riesgo | Que se clasifique como comprobable algo que en realidad se discute | Cada clasificación dudosa se resuelve dejándola como criterio |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Todas las reglas del estándar están clasificadas
- [ ] Cada regla comprobada nombra su programa
- [ ] El procedimiento de escribir una regla incluye el paso de clasificar
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el criterio de HU-001 |
| **N**egociable | Sí | La forma del registro se puede discutir |
| **V**aliosa | Sí | Muestra qué parte del estándar se sostiene sola |
| **E**stimable | Sí | El trabajo es proporcional a la cantidad de reglas |
| **S**mall (pequeña) | Parcial | Son muchas reglas, aunque cada una es rápida |
| **T**esteable | Sí | Se cuenta y se compara |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
