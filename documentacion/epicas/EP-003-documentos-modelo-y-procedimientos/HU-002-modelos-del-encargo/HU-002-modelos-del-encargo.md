# HU-002 — Crear los modelos del encargo: brief, épica, historia de usuario

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien encarga un trabajo
- **Quiero** modelos para escribir la necesidad, la épica y la historia de usuario
- **Para** que dos encargos parecidos queden documentados igual y se puedan comparar

---

## 3. Contexto y descripción

El encargo es la parte de arriba de la cadena: la necesidad escrita, el grupo de trabajo que la resuelve y cada requisito con sus criterios de aceptación. Es donde se decide qué se va a hacer, así que es donde más caro sale improvisar el formato.

Sin modelo, cada épica sale con distintas secciones y cada historia con distinto nivel de detalle. Comparar dos, o retomar una vieja, cuesta más de lo que debería.

Los tres van juntos en una sola historia porque se encadenan: la necesidad da origen a las épicas, la épica a las historias, y cada una apunta a la de arriba.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay un modelo para la necesidad, uno para la épica y uno para la historia de usuario |
| RN-02 | Cada documento apunta al de arriba y lista los de abajo |
| RN-03 | La historia de usuario trae sus criterios de aceptación, y cada uno dice cómo se comprueba |
| RN-04 | Los espacios por llenar usan la marca acordada |
| RN-05 | Un proyecto puede agregar secciones propias, pero no quitar las que trae el modelo |

### 3.2 Supuestos

- Quien escribe el encargo no es necesariamente quien lo va a construir, así que el modelo tiene que sostenerse solo.

### 3.3 Fuera de alcance

- Los modelos de la fase. Eso es HU-003.
- El procedimiento para llenarlos. Eso es HU-006.

---

## 4. Criterios de aceptación

### CA-01 — Los tres modelos existen y se encadenan

```gherkin
Dado que se va a documentar un encargo
Cuando se buscan los modelos
Entonces existen el de la necesidad, el de la épica y el de la historia
Y cada uno tiene dónde nombrar al de arriba y a los de abajo
```

**Cómo validarlo:**

1. Abrir la carpeta de modelos del estándar.
2. Ubicar los tres. Resultado esperado: están los tres, con nombre reconocible.
3. Abrir el de la historia de usuario y buscar dónde nombra su épica. Resultado esperado: hay un campo para eso.
4. Abrir el de la épica y buscar dónde lista sus historias. Resultado esperado: hay una tabla para eso.
- **Aprobado cuando:** la cadena se puede recorrer de arriba abajo y de abajo arriba.

### CA-02 — La historia trae criterios que se pueden comprobar

```gherkin
Dado que se escribe una historia de usuario con el modelo
Cuando se llega a sus criterios de aceptación
Entonces cada uno dice cómo se comprueba, paso a paso
```

**Cómo validarlo:**

1. Llenar el modelo de historia con un caso de prueba.
2. Leer un criterio de aceptación. Resultado esperado: trae el escenario y los pasos para verificarlo.
3. Dárselo a alguien que no conoce el trabajo. Resultado esperado: puede seguir los pasos sin preguntar dónde ni cómo.
- **Aprobado cuando:** un criterio se puede verificar sin quien lo escribió.

### CA-03 — Un encargo llenado a medias se nota

```gherkin
Dado que se llena un modelo del encargo dejando secciones sin completar
Cuando alguien lo abre
Entonces se ve cuáles quedaron sin llenar
```

**Cómo validarlo:**

1. Llenar el modelo de épica a medias.
2. Abrirlo. Resultado esperado: las secciones sin llenar traen la marca acordada.
3. Completar todo. Resultado esperado: no queda ninguna marca.
- **Aprobado cuando:** lo incompleto se distingue de lo terminado.

### Criterios de aceptación transversales

- [ ] **Límites** — una épica sin historias todavía, y una historia sin fases todavía, tienen forma definida.
- [ ] **No regresión** — los documentos ya escritos con estos modelos siguen siendo válidos.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | Cada sección dice qué va adentro, sin suponer que quien llena conoce el método |
| **Uniformidad** | Los tres modelos usan la misma marca y el mismo tono |
| **Proporción** | Un encargo chico no obliga a llenar el formato de uno grande |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, son documentos de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), §5.1 y §5.4 fila 10.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el modelo de la necesidad.
- [ ] Escribir el modelo de la épica, con su lista de historias.
- [ ] Escribir el modelo de la historia de usuario, con sus criterios de aceptación.
- [ ] Dejar en cada uno el enlace al de arriba y al de abajo.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo](A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase retro-documenta y no toca `plantillas/`.** Los tres modelos del encargo existen y se usan a diario; falta su incremento en la especificación del módulo y la prueba del encadenamiento. **Lo que sí falta de verdad** es el planteamiento de este repositorio, que es el pendiente 56 y no se puede reconstruir leyendo el repositorio.

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
| Dependencia | HU-001, porque los modelos usan la marca acordada | Alto |
| Dependencia | EP-001, porque los modelos concretan lo que las reglas exigen | Alto |
| Riesgo | Que el modelo sea tan largo que nadie lo llene entero | Se marca qué secciones son opcionales y se permite borrarlas |
| Riesgo | Que se pida el mismo dato en dos modelos | Cada dato tiene un solo dueño; los demás lo enlazan |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Los tres modelos existen
- [ ] La cadena se recorre en los dos sentidos
- [ ] Los criterios de aceptación traen cómo se comprueban
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la marca de HU-001 |
| **N**egociable | Sí | Las secciones de cada modelo se pueden discutir |
| **V**aliosa | Sí | Es donde se decide qué se va a hacer |
| **E**stimable | Sí | Son tres documentos |
| **S**mall (pequeña) | Parcial | Tres modelos en una historia |
| **T**esteable | Sí | Se prueba escribiendo un encargo real con ellos |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
