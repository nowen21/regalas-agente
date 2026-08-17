# HU-001 — Fijar el criterio de qué se comprueba con un programa

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien define el estándar
- **Quiero** un criterio escrito que separe lo que un programa puede comprobar de lo que hay que leer y juzgar
- **Para** que nadie escriba un programa que opine, y que la lista de lo comprobable no dependa de quién la mire

---

## 3. Contexto y descripción

Hoy no hay criterio escrito. Cada vez que aparece una regla, decidir si se puede comprobar sola es una discusión que empieza de cero, y el resultado cambia según quién la tenga.

Eso tiene dos finales malos, y los dos ya se conocen. Si se automatiza de más, el programa termina juzgando cosas que dependen del significado, marca lo que está bien y la gente deja de creerle. Si se automatiza de menos, quedan reglas que un programa revisaría en un segundo esperando a que alguien se acuerde de revisarlas a mano.

Esta historia escribe la pregunta que decide, una sola, y la deja en un sitio fijo para que la respuesta se dé siempre igual.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La pregunta que decide es una sola: si un programa puede responder sí o no sin opinar, es comprobable |
| RN-02 | Si dos personas pueden discutir si se cumplió, no es comprobable y se queda como criterio |
| RN-03 | Una regla puede ser comprobable a medias: la parte mecánica se automatiza y el resto se declara como criterio |
| RN-04 | El criterio vive en un solo archivo, y ese archivo es el que se consulta al escribir cada regla nueva |
| RN-05 | Lo que un programa comprueba tiene que estar escrito antes en una regla; nunca al revés |

### 3.2 Supuestos

- La mayoría de las reglas del estándar no son comprobables, y eso está bien. El valor está en que se sepa cuáles sí.

### 3.3 Fuera de alcance

- Escribir los programas. Acá se fija el criterio, no se automatiza nada.
- Clasificar regla por regla. Eso es HU-002.

---

## 4. Criterios de aceptación

### CA-01 — El criterio existe y se puede citar

```gherkin
Dado que el estándar tiene reglas escritas
Cuando alguien pregunta si una regla se puede comprobar con un programa
Entonces existe un archivo que responde con una sola pregunta
Y ese archivo se puede citar por su ruta
```

**Cómo validarlo:**

1. Abrir la carpeta de los programas de comprobación del estándar.
2. Buscar el archivo que fija el criterio. Resultado esperado: existe uno solo, y su primer apartado trae la pregunta que decide.
3. Leer la pregunta. Resultado esperado: se entiende sin saber programar y no admite dos lecturas.
- **Aprobado cuando:** el archivo existe, tiene la pregunta y se puede nombrar por su ruta desde la raíz.

### CA-02 — Una regla que se discute queda afuera

```gherkin
Dado que existe una regla cuyo cumplimiento depende de leer y entender un texto
Cuando se le aplica el criterio
Entonces queda clasificada como no comprobable
Y no se escribe ningún programa que la revise
```

**Cómo validarlo:**

1. Tomar una regla que pida escribir claro o decidir con criterio de senior.
2. Aplicarle la pregunta del criterio. Resultado esperado: la respuesta es que no, porque dos personas pueden discutir el resultado.
3. Buscar en la carpeta de programas alguno que la revise. Resultado esperado: no hay ninguno.
- **Aprobado cuando:** la regla queda del lado del criterio y ningún programa pretende revisarla.

### CA-03 — Una regla comprobable a medias se parte

```gherkin
Dado que existe una regla con una parte mecánica y otra de criterio
Cuando se le aplica el criterio
Entonces queda registrada como comprobable en parte
Y está escrito qué mitad revisa el programa y qué mitad se lee
```

**Cómo validarlo:**

1. Tomar una regla que exija a la vez una marca visible y un juicio, por ejemplo que un documento traiga su bloque de resultado y que ese resultado sea correcto.
2. Aplicarle la pregunta. Resultado esperado: la presencia del bloque se responde sí o no; que el resultado sea correcto, no.
3. Revisar cómo quedó registrada. Resultado esperado: dice que es parcial y nombra las dos mitades.
- **Aprobado cuando:** la clasificación distingue las dos mitades y ninguna queda sin dueño.

### Criterios de aceptación transversales

- [ ] **Límites** — está escrito qué se hace con la regla que quedó en duda: se deja como criterio hasta que alguien demuestre lo contrario.
- [ ] **No regresión** — las reglas ya clasificadas conservan su clasificación.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | El criterio se entiende sin saber programar |
| **Estabilidad** | El criterio no cambia con cada regla nueva; si cambia, se versiona como cambio del estándar |
| **Trazabilidad** | Cada clasificación dice contra qué versión del estándar se hizo |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, no hay interfaz.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la pregunta que decide, con su ejemplo de cada lado.
- [ ] Escribir qué se hace con la regla comprobable a medias.
- [ ] Dejar el criterio en un archivo único y enlazarlo desde el capítulo de meta-reglas.
- [ ] Escribir qué se hace con la regla que quedó en duda.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable](A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase retro-documenta.** El criterio existe y se aplicó a las 188 reglas. Lo que falta: **vive en `validadores/`, no en `base/`**, así que un proyecto que hereda recibe la obligación de clasificar y no el criterio con que se decide.

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
| Dependencia | EP-001, porque el criterio se aplica sobre reglas ya escritas | Alto |
| Riesgo | Que el criterio quede tan amplio que todo parezca comprobable | Se escribe con un ejemplo de cada lado, tomado de reglas reales |
| Riesgo | Que se escriba y nadie lo consulte al crear una regla | El paso de clasificar queda dentro del procedimiento de la regla, no aparte |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El criterio está escrito en un archivo único
- [ ] Trae un ejemplo de regla comprobable y uno de regla que se queda como criterio
- [ ] Dice qué se hace con la regla comprobable a medias
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No necesita ningún programa escrito |
| **N**egociable | Sí | La redacción de la pregunta se puede discutir |
| **V**aliosa | Sí | Sin ella, cada regla nueva reabre la misma discusión |
| **E**stimable | Sí | Es un documento corto |
| **S**mall (pequeña) | Sí | Un archivo |
| **T**esteable | Sí | Se prueba aplicándolo a reglas de los dos tipos |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
