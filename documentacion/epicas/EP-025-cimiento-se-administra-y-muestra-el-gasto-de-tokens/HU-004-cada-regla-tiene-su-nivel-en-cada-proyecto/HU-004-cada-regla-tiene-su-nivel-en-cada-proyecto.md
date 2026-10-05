# HU-004 · Cada regla tiene su nivel en cada proyecto


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/niveles/` |
| **Tipo** | Funcional |
| **Prioridad** | Must: cuarta de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | En curso: la pantalla falla contra la base real (H-6 de la sesión 3 del 2026-10-04) |

---

## 2. Narrativa

- **Como** administrador de Cimiento
- **Quiero** fijar en cada proyecto qué tan rígida es cada regla: frena, avisa o apagada
- **Para** ajustar una regla sin cambiar código, y sin que el cambio alcance a los demás proyectos

---

## 3. Contexto y descripción

Cada regla se aplica como está escrita en el código, igual para todos los proyectos. Ajustarla es un cambio de código, y una regla fija bloqueó a Cimiento para corregirse el 2026-10-04 ([épica](../epica.md), §3).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Cada regla tiene por proyecto uno de tres niveles: frena, avisa o apagada | Análisis 1 del pendiente 119, acuerdo 13 |
| RN-02 | Las reglas del núcleo (`00·N…`) siempre frenan y no aparecen como opción | Acuerdo 13 |
| RN-03 | Una regla sin nivel guardado frena, como hasta hoy | Propuesta del agente: el comportamiento no cambia hasta que alguien lo cambie |
| RN-04 | Las reglas derogadas no aparecen | Propuesta del agente: ya no rigen |
| RN-05 | Cambia el nivel el grupo administrador; el grupo consulta solo lo ve | Acuerdo 14 |
| RN-06 | Cada cambio queda registrado: qué regla, de qué nivel a cuál, quién y cuándo | Épica, §5.4, pregunta 15 |

### 3.2 Supuestos

- La HU-003 está terminada: los proyectos están registrados.

### 3.3 Fuera de alcance

- Que el freno lea el nivel: HU-005.

---

## 4. Criterios de aceptación

### CA-01 · Un administrador cambia el nivel de una regla en un proyecto

**Sale de:** análisis 1 del pendiente 119, punto 13.

```gherkin
Dado un proyecto registrado y una cuenta del grupo administrador
Cuando abre las reglas del proyecto, cambia una regla a «avisa» y guarda
Entonces esa regla queda en «avisa» en ese proyecto
Y en los demás proyectos sigue en «frena»
```

**Cómo validarlo:**
1. En «Proyectos», pulsar «Reglas» en la fila de un proyecto → la lista de reglas por capítulo, todas en «frena».
2. Cambiar `02·F8` a «avisa» y pulsar «Guardar» → la página muestra `02·F8` en «avisa».
3. Abrir las reglas de otro proyecto → `02·F8` sigue en «frena».
4. Correr `python manage.py test core.niveles` → pasan los casos de cambio.

**Aprobado cuando:** el nivel cambia solo en el proyecto elegido.

### CA-02 · Las reglas del núcleo no se pueden cambiar

**Sale de:** análisis 1 del pendiente 119, punto 13.

```gherkin
Dado la lista de reglas de un proyecto
Cuando se busca una regla del núcleo
Entonces no aparece
Y si se envía un cambio para ella, o un nivel que no existe, no se guarda nada
```

**Cómo validarlo:**
1. En las reglas de un proyecto, buscar `00·N1` → no aparece.
2. Correr `python manage.py test core.niveles` → pasan los casos de núcleo y de nivel inválido.

**Aprobado cuando:** el núcleo no aparece ni se guarda, y un nivel inválido no cambia nada.

### CA-03 · Cada cambio queda registrado

**Sale de:** análisis 1 del pendiente 119, punto 13.

```gherkin
Dado un cambio de nivel guardado
Cuando se abre el historial de reglas del proyecto
Entonces aparece la regla, el nivel anterior, el nuevo, la cuenta y la fecha
```

**Cómo validarlo:**
1. Después del CA-01, pulsar «Historial» en las reglas del proyecto → la fila de `02·F8`, de «frena» a «avisa», con la cuenta y la fecha.
2. Correr `python manage.py test core.niveles` → pasa el caso de historial.

**Aprobado cuando:** el cambio aparece con sus cinco datos.

### CA-04 · El grupo consulta solo ve los niveles

**Sale de:** análisis 1 del pendiente 119, punto 13.

```gherkin
Dado una cuenta del grupo consulta
Cuando abre las reglas de un proyecto
Entonces ve los niveles sin poder cambiarlos
Y si envía un cambio, recibe 403 y no se guarda nada
```

**Cómo validarlo:**
1. Correr `python manage.py test core.niveles` → pasan los casos de permiso.

**Aprobado cuando:** consulta ve los niveles y su envío recibe 403.

### Criterios de aceptación transversales

- [ ] Validación: toda entrada obligatoria se valida; un dato inválido se rechaza con mensaje claro y **el estado no cambia** (`04`, `03`).
- [ ] Autorización: solo quien tiene permiso ejecuta la acción; sin permiso se deniega **sin filtrar datos ni su existencia**, y no se elude cambiando parámetros/ruta (`04`).
- [ ] Atomicidad: las operaciones que escriben son todo-o-nada (`03`).
- [ ] Auditoría: las acciones relevantes quedan registradas (quién, qué, cuándo) (`05`, `15`).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Auditoría** | Cada cambio de nivel guarda regla, nivel anterior, nivel nuevo, cuenta y fecha |
| RNF-02 | **Rendimiento** | La lista de reglas se lee de `base/` una vez por proceso, no en cada petición |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdos 12 y 13; punto 13.

Modelo de datos afectado: tablas nuevas de niveles y de cambios de nivel.

---

## 7. Tareas técnicas derivadas

- [ ] Módulo `core/niveles/` con sus dos tablas.
- [ ] Catálogo de reglas configurables desde `base/`.
- [ ] Pantalla de niveles por proyecto e historial.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-004-niveles-por-proyecto` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-004-niveles-por-proyecto/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-004-niveles-por-proyecto/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-004-niveles-por-proyecto/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-003 | Alto |
| Riesgo | Una regla cambie de ID o se derogue después de tener nivel | El nivel guardado de una regla que ya no está en el catálogo no se muestra ni se aplica |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
