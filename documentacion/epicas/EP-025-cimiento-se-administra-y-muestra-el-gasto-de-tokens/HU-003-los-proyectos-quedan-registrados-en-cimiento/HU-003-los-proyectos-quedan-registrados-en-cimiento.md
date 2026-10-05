# HU-003 · Los proyectos quedan registrados en Cimiento


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/proyectos/` |
| **Tipo** | Funcional |
| **Prioridad** | Must: tercera de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | En curso: falla contra la base real, donde ya estaba el registro de la plataforma vieja (H-6 de la sesión 3 del 2026-10-04) |

---

## 2. Narrativa

- **Como** administrador de Cimiento
- **Quiero** registrar cada proyecto con su ruta y sus límites de aviso
- **Para** que los niveles de las reglas y el gasto de tokens queden de un proyecto, y Cimiento sepa dónde están sus registros de Claude Code

---

## 3. Contexto y descripción

Cimiento no sabe qué proyectos existen ni dónde están sus `.jsonl`, que Claude Code guarda en `~/.claude/projects/«carpeta»/`, con un nombre que sale de la ruta del proyecto. Los niveles de las reglas (HU-004) y el gasto (HU-006) son de un proyecto, y los avisos (HU-009) usan sus límites ([épica](../epica.md), §5.4).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Un proyecto tiene nombre, ruta, carpeta de Claude Code y dos límites de aviso: por enganche y por archivo leído, en tokens | Análisis 1 del pendiente 119, acuerdos 10 y 11 |
| RN-02 | La carpeta de Claude Code se calcula desde la ruta, no se escribe | Punto 4 |
| RN-03 | La ruta tiene que existir y no puede estar dos veces, sin distinguir mayúsculas | Épica, §5.4, pregunta 5 |
| RN-04 | Los límites son números enteros mayores que cero | Épica, §5.4, pregunta 5 |
| RN-05 | Un proyecto no se borra: se desactiva, y su historia queda | Épica, §5.4, preguntas 7 y 8 |
| RN-06 | Registra y edita el grupo administrador; el grupo consulta solo ve la lista | Acuerdo 14 |
| RN-07 | Límites por defecto: 2000 tokens por enganche y 10 000 por archivo leído | Propuesta del agente: cambian por proyecto sin tocar código |

### 3.2 Supuestos

- Claude Code nombra la carpeta de un proyecto con su ruta: la letra de la unidad en minúscula y cada carácter que no es letra o número cambiado por `-` (verificado el 2026-10-04 en 19 carpetas de esta máquina).

### 3.3 Fuera de alcance

- Traer los proyectos de `plantillas/proyectos.md`: el instalador sigue anotando ahí.
- Los niveles de las reglas (HU-004) y el gasto (HU-006).

---

## 4. Criterios de aceptación

### CA-01 · Un administrador registra un proyecto

**Sale de:** análisis 1 del pendiente 119, punto 4.

```gherkin
Dado una cuenta del grupo administrador
Cuando registra un proyecto con nombre y una ruta que existe
Entonces el proyecto aparece en la lista, activo, con su carpeta de Claude Code calculada
Y con los límites escritos, o los de por defecto
```

**Cómo validarlo:**
1. Entrar con una cuenta administradora y abrir «Proyectos» en el menú.
2. Pulsar «Registrar», escribir el nombre y la ruta de una carpeta que existe → vuelve a la lista con el proyecto.
3. Revisar la fila → la carpeta de Claude Code es la ruta con la unidad en minúscula y `-` en lugar de lo que no es letra o número.
4. Correr `python manage.py test core.proyectos` → pasan los casos de registro.

**Aprobado cuando:** el proyecto queda en la lista con su carpeta y sus límites.

### CA-02 · Lo que no vale no se guarda

**Sale de:** análisis 1 del pendiente 119, punto 4.

```gherkin
Dado el formulario de registro
Cuando la ruta no existe, ya está registrada, el nombre se repite o un límite no es mayor que cero
Entonces el formulario dice qué campo está mal
Y no se guarda nada
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos` → pasan los casos de validación.

**Aprobado cuando:** cada caso muestra su mensaje y la cantidad de proyectos no cambia.

### CA-03 · Un proyecto se edita y se desactiva

**Sale de:** análisis 1 del pendiente 119, punto 4.

```gherkin
Dado un proyecto registrado
Cuando un administrador cambia sus límites o lo desactiva
Entonces la lista muestra los límites nuevos o el proyecto como inactivo
Y el proyecto sigue en la base
```

**Cómo validarlo:**
1. En «Proyectos», pulsar «Editar» en una fila, cambiar un límite y desmarcar «Activo» → la fila muestra el límite nuevo y «Inactivo».
2. Correr `python manage.py test core.proyectos` → pasan los casos de edición.

**Aprobado cuando:** el cambio se ve en la lista y el proyecto no se borró.

### CA-04 · El grupo consulta solo ve

**Sale de:** análisis 1 del pendiente 119, punto 12.

```gherkin
Dado una cuenta del grupo consulta
Cuando abre la lista de proyectos
Entonces la ve sin los botones de registrar ni editar
Y si pide el formulario de registro o de edición, recibe 403
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos` → pasan los casos de permiso.

**Aprobado cuando:** consulta ve la lista y recibe 403 en los formularios.

### Criterios de aceptación transversales

- [ ] Validación: toda entrada obligatoria se valida; un dato inválido se rechaza con mensaje claro y **el estado no cambia** (`04`, `03`).
- [ ] Límites: vacío, nulo, mínimo, máximo y duplicado tienen comportamiento definido (`08`).
- [ ] Autorización: solo quien tiene permiso ejecuta la acción; sin permiso se deniega **sin filtrar datos ni su existencia**, y no se elude cambiando parámetros/ruta (`04`).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | Los formularios llevan su protección CSRF |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdos 2, 10 y 11; punto 4.

Modelo de datos afectado: tabla nueva de proyectos.

---

## 7. Tareas técnicas derivadas

- [ ] Módulo `core/proyectos/` con el modelo y su migración.
- [ ] Cálculo de la carpeta de Claude Code.
- [ ] Lista, registro y edición, con permiso por grupo.
- [ ] «Proyectos» en el menú.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-003-registro-de-proyectos` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-003-registro-de-proyectos/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-003-registro-de-proyectos/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-003-registro-de-proyectos/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-002 | Alto |
| Riesgo | Claude Code cambie cómo nombra la carpeta | El cálculo vive en una sola función, con su prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
