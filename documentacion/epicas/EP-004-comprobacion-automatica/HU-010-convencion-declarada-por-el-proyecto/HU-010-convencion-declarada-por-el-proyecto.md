# HU-010 — Comprobar el código contra la convención que el proyecto declara

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-010 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — los cinco criterios ejecutados en la fase `A`, tres de ellos provocados con su contraprueba |
---

## 2. Narrativa

- **Como** quien define el estándar
- **Quiero** que el proyecto declare su convención y su dominio en un formato que un programa lea, y que las reglas que dependen de eso se comprueben solas
- **Para** que "sigue la convención" deje de ser una discusión y pase a responderse con un sí o un no

---

## 3. Contexto y descripción

Hay reglas del estándar que hoy nadie comprueba, y no por descuido: no se pueden comprobar. La base es agnóstica a propósito, así que no sabe si en este proyecto las tablas van en minúsculas con guion bajo, dónde viven los módulos, qué tablas son del negocio y cuáles las trae el marco de trabajo, ni qué entidades no se editan nunca.

Sin esa declaración, un programa que revise nombres estaría inventando la convención, y eso es justo lo que el criterio prohíbe.

Esta historia cierra el hueco por el lado correcto: primero el proyecto declara, en un formato mínimo y fijo, contra qué se compara; después los programas comparan. Lo que el proyecto no declara, no se comprueba, y eso también queda dicho para que se vea qué se está dejando pasar.

Es el trabajo que la épica había dejado diferido en su §5.3.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El proyecto declara su convención en un archivo de su carpeta de configuración del agente, en tabla de claves fijas |
| RN-02 | El proyecto declara su dominio en otro archivo: qué entidades hay, en qué tabla viven, cuál es su clave natural y cuáles no se editan nunca |
| RN-03 | Lo que no se declara no se comprueba, y el programa dice qué quedó sin comprobar por eso |
| RN-04 | La clave de la declaración no se traduce ni se reordena: es la que el programa lee |
| RN-05 | El código que el proyecto declara como heredado queda fuera de la comprobación, porque la convención es para lo nuevo |
| RN-06 | Todo hallazgo de esta familia es aviso: un nombre puede tener un motivo que el programa no ve |
| RN-07 | La declaración vive en un solo sitio; lo que ya está en ella no se repite en prosa en otro archivo |

### 3.2 Supuestos

- El proyecto tiene una convención, aunque no esté escrita. Escribirla es trabajo de una sesión, no de un mes.
- Las migraciones son la fuente fiable de qué tablas y columnas existen.

### 3.3 Fuera de alcance

- Renombrar lo que no cumple. Los programas reportan.
- Adivinar la convención leyendo el código. Si nadie la declaró, no se comprueba.
- Comprobar la estructura de las carpetas de trabajo, que no depende del proyecto. Eso es HU-006.

---

## 4. Criterios de aceptación

### CA-01 — Sin declaración no se comprueba, y se dice

```gherkin
Dado que un proyecto no declaró su convención
Cuando se corre la comprobación
Entonces no reporta ningún incumplimiento de nombres
Y dice qué comprobaciones se quedaron sin correr por falta de declaración
```

**Cómo validarlo:**

1. Tomar un proyecto de prueba sin la declaración llena.
2. Correr la comprobación de la convención. Resultado esperado: no marca ningún nombre.
3. Leer la salida. Resultado esperado: enumera cada clave sin declarar y qué regla queda sin comprobar por cada una.
- **Aprobado cuando:** no se inventa ninguna convención y se ve qué se está dejando pasar.

### CA-02 — Un nombre fuera de la convención declarada se reporta

```gherkin
Dado que el proyecto declaró cómo se escriben las tablas y las columnas
Cuando una migración crea una tabla que no sigue esa forma
Entonces la comprobación la reporta con su archivo, su línea y la convención esperada
```

**Cómo validarlo:**

1. En el proyecto de prueba, declarar la convención de tablas y de columnas.
2. Crear una migración con una tabla que no la siga. Resultado esperado: al correr, la reporta y nombra la convención declarada.
3. Corregir el nombre y volver a correr. Resultado esperado: deja de reportarla.
4. Declarar esa migración como código heredado y repetir con un nombre malo. Resultado esperado: no la reporta.
- **Aprobado cuando:** reporta lo nuevo que no cumple y respeta lo declarado como heredado.

### CA-03 — Una tabla de dominio sin auditoría se reporta

```gherkin
Dado que el proyecto declaró qué entidades son de dominio y qué columnas de auditoría usa
Cuando la migración que crea esa tabla no las trae
Entonces la comprobación reporta cuáles faltan
Y no reporta las tablas que el marco de trabajo trae
```

**Cómo validarlo:**

1. Declarar una entidad de dominio con su tabla, y declarar las columnas de auditoría.
2. Crear la tabla sin esas columnas. Resultado esperado: al correr, reporta cuáles faltan, una por una.
3. Comprobar que una tabla no declarada, de las que trae el marco de trabajo, no aparece en la salida. Resultado esperado: no aparece.
- **Aprobado cuando:** solo se le exige auditoría a lo declarado como dominio.

### CA-04 — Una entidad inmutable sin sus estados ni su permiso se reporta

```gherkin
Dado que el proyecto declaró una entidad como inmutable
Cuando su tabla no tiene los estados ni los campos de anulación declarados
Entonces la comprobación lo reporta
Y también reporta si no existe el permiso propio de anular
```

**Cómo validarlo:**

1. Declarar una entidad como inmutable, con sus tres estados, sus campos de anulación y la forma del permiso.
2. Crear la tabla sin los campos de anulación. Resultado esperado: al correr, los nombra uno por uno.
3. Buscar en el código el permiso de anular de esa entidad y quitarlo. Resultado esperado: al correr, reporta que no lo encuentra.
4. Agregar campos y permiso, y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** los tres faltantes se reportan por separado y desaparecen al agregarlos.

### CA-05 — Un módulo del código sin declarar se reporta

```gherkin
Dado que el proyecto declaró dónde viven sus módulos
Cuando existe en el código un módulo que no está declarado
Entonces la comprobación lo reporta
Y también reporta el módulo declarado que no tiene código
```

**Cómo validarlo:**

1. Declarar la ruta donde viven los módulos y declarar dos módulos.
2. Crear en el código un tercer módulo que siga esa ruta, sin declararlo. Resultado esperado: al correr, lo reporta.
3. Borrar el código de uno de los declarados. Resultado esperado: al correr, reporta que está declarado y no tiene código.
- **Aprobado cuando:** los dos sentidos se reportan.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto sin migraciones, uno sin código y una declaración a medio llenar tienen comportamiento definido.
- [ ] **Errores** — una declaración con una clave que el programa no conoce se reporta como declaración mal escrita, no como incumplimiento del código.
- [ ] **No regresión** — un proyecto que no declara nada sigue pasando la corrida como antes.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | El mismo proyecto y la misma declaración dan el mismo resultado |
| **Autonomía** | Sin red y sin IA: se lee el código guardado y la declaración |
| **Claridad** | El mensaje dice la convención esperada, no solo que el nombre está mal |
| **Mantenimiento** | La declaración es una sola; el programa no guarda una copia de la convención |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.3, que difería este trabajo hasta que existiera la declaración.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno propio. Se lee el esquema que declaran las migraciones del proyecto.

---

## 7. Tareas técnicas derivadas

- [ ] Definir el formato mínimo de la declaración: qué claves hay y qué se escribe en cada una.
- [ ] Sumar la declaración a las plantillas que el proyecto hereda, y a lo que el instalador deja puesto.
- [ ] Escribir el lector de la declaración, que no comprueba nada.
- [ ] Comprobar ubicación de módulos y nombres contra lo declarado.
- [ ] Comprobar auditoría, unicidad e índices de las tablas de dominio declaradas.
- [ ] Comprobar estados, campos de anulación y permiso de las entidades inmutables declaradas.
- [ ] Escribir pruebas con proyectos de prueba: sin declaración, con declaración a medias y completa.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| `A-EP-004-HU-010-declaracion-y-comprobacion` | CA-01 a CA-05 y RNF-01 | [documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/plan_trabajo.md](A-EP-004-HU-010-declaracion-y-comprobacion/plan_trabajo.md) | [documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/plan_pruebas.md](A-EP-004-HU-010-declaracion-y-comprobacion/plan_pruebas.md) | [documentacion/epicas/EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/resultado_pruebas.md](A-EP-004-HU-010-declaracion-y-comprobacion/resultado_pruebas.md) | **Cerrada el 2026-08-30.** Veredicto: **Cumple** — los cinco criterios ejecutados, tres provocados con su contraprueba, y encontró que el reclamo del permiso de anular salía en todo proyecto |

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
| Dependencia | HU-003, porque los hallazgos salen con la forma y la severidad ya definidas | Alto |
| Dependencia | EP-007, porque la declaración llega a cada proyecto con la instalación | Medio |
| Riesgo | Que el formato de la declaración pida tanto que nadie la llene | Se empieza con las claves mínimas y todas admiten quedar sin declarar |
| Riesgo | Que la declaración diga una cosa y la prosa del mismo archivo otra | Lo declarado no se repite en prosa; se enlaza |
| Riesgo | Que el código heredado llene la salida de hallazgos | El proyecto declara qué queda fuera, y eso es parte del formato |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El formato de la declaración está escrito y llega a los proyectos con la instalación
- [ ] Las comprobaciones corren contra lo declarado y se saltan lo no declarado
- [ ] La salida dice qué quedó sin comprobar y por qué
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la forma del hallazgo de HU-003 |
| **N**egociable | Sí | Qué claves entran en la declaración se puede discutir |
| **V**aliosa | Sí | Levanta cinco reglas que hoy no comprueba nadie |
| **E**stimable | Sí | El alcance lo fijan esas cinco reglas |
| **S**mall (pequeña) | No | Son el formato, su llegada a los proyectos y tres familias de comprobación |
| **T**esteable | Sí | Se prueba con proyectos de prueba con y sin declaración |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, que levanta el diferido §5.3 de la épica |
