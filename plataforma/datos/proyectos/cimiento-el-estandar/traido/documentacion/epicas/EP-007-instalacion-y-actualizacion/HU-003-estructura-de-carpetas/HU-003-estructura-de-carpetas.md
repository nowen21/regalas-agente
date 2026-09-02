# HU-003 — Crear la estructura de carpetas del trabajo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — los dos CA y los dos transversales verificados el 2026-08-17 |
---

## 2. Narrativa

- **Como** quien abre un proyecto por primera vez
- **Quiero** encontrar las carpetas del trabajo ya creadas
- **Para** que la documentación no termine repartida donde a cada uno se le ocurra

---

## 3. Contexto y descripción

Si la estructura no está puesta, cada sesión inventa la suya: la documentación en una carpeta hoy y en otra mañana. Después nadie encuentra nada, y el trabajo de ordenar cuesta más que el de crear.

Dejarla creada desde el principio evita eso. Y separa dos mundos que no se mezclan: el código del proyecto, donde el agente no manda, y el espacio de trabajo del agente, que sí gestiona.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El instalador crea las carpetas que el trabajo necesita |
| RN-02 | Se separa el código del proyecto del espacio de trabajo del agente |
| RN-03 | Las carpetas se crean vacías: qué va adentro no lo decide el instalador |
| RN-04 | Cada carpeta lleva su índice desde el día uno |
| RN-05 | Si una carpeta ya existe, no se toca |

### 3.2 Supuestos

- La estructura es la misma para cualquier proyecto, sin importar su lenguaje.

### 3.3 Fuera de alcance

- Mover el código que ya existe en el proyecto.
- Decidir cómo se organiza el código por dentro.

---

## 4. Criterios de aceptación

### CA-01 — Las carpetas quedan creadas y con su índice

```gherkin
Dado que se instala en un proyecto sin estructura
Cuando termina la instalación
Entonces existen las carpetas del trabajo
Y cada una tiene su índice
```

**Cómo validarlo:**

1. Instalar en una carpeta de proyecto vacía.
2. Revisar la estructura. Resultado esperado: están las carpetas declaradas.
3. Abrir cada índice. Resultado esperado: existe y dice qué va en esa carpeta.
- **Aprobado cuando:** la estructura queda lista para trabajar.

### CA-02 — Lo que ya existía no se toca

```gherkin
Dado que el proyecto ya tenía una de esas carpetas con contenido
Cuando se instala
Entonces esa carpeta queda como estaba
```

**Cómo validarlo:**

1. Crear a mano una de las carpetas con un archivo adentro.
2. Instalar. Resultado esperado: el archivo sigue ahí y la carpeta no se recreó.
- **Aprobado cuando:** instalar nunca vacía nada.

### CA-04 — La historia y el pendiente nacen con su esqueleto y sus índices puestos

```gherkin
Dado que hay que bajar un defecto por la cadena
Cuando se pide al andamio una historia nueva en una épica, o un pendiente nuevo enrutado a una historia
Entonces el archivo nace desde su plantilla, con los marcadores de contenido intactos
Y las filas de los índices quedan puestas en los dos sentidos: la épica, su README, el índice del backlog y el mapa de historias
```

**Cómo validarlo:**

1. Correr `python validadores/andamio.py hu <épica> <slug> --aplicar`. Resultado esperado: carpeta `HU-NNN-<slug>/` con su documento y su `README.md`; una fila nueva en el §9 de `epica.md` y otra en el `README.md` de la épica.
2. Correr `python validadores/andamio.py pendiente <slug> --hu <épica>/<HU> --aplicar`. Resultado esperado: `pendientes/NN-<slug>.md` con su ficha, una fila en el índice del backlog y la historia nombrada en el mapa.
3. Correr `validar.py estandar`, `fases` y `pendientes`. Resultado esperado: sin fallas sobre lo recién creado.
- **Aprobado cuando:** bajar un defecto por la cadena no exige escribir ningún índice a mano. Salió del pendiente 69: el 2026-08-20 fueron quince escrituras de índice por defecto.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto que ya tiene toda la estructura no cambia en nada.
- [ ] **Compatibilidad** — funciona con rutas largas, con espacios y con tildes.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Idempotencia** | Correrlo de nuevo no cambia nada |
| **Universalidad** | La misma estructura sirve a cualquier proyecto |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Declarar cuáles son las carpetas del trabajo.
- [ ] Crearlas si faltan, sin tocar las que ya están.
- [ ] Poner el índice de cada una.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas](A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-007-HU-003-retrodocumentar-la-estructura-de-carpetas/resultado_pruebas.md#6-veredicto-de-la-fase) — los dos CA y los dos transversales verificados. Pendiente el commit |

**La fase retro-documenta.** La estructura está exigida, declarada, creada por el instalador y comprobada por la revisión. La prueba que falta es la que más importa: que instalar sobre un proyecto que ya trabajó no le borre nada — y eso se rompe en la segunda corrida.

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
| Dependencia | HU-001, porque es un paso de la instalación | Alto |
| Riesgo | Que el proyecto ya tenga una carpeta con ese nombre y otro uso | No se toca lo que ya existe |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Las carpetas se crean con su índice
- [ ] Lo que ya existía no se toca
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Es un paso del instalador |
| **N**egociable | Sí | Cuáles son las carpetas se puede discutir |
| **V**aliosa | Sí | Evita que la documentación se disperse |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Crear carpetas e índices |
| **T**esteable | Sí | Se prueba instalando en vacío y sobre lo existente |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Los dos CA verificados: la estructura queda completa y reinstalar no cambia nada. Los transversales también: un proyecto al día no cambia, y funciona con rutas con espacios y tildes |
| [B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente](B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente/README.md) | CA-04 | Cerrada el 2026-08-20: Cumple, 1 de 1 CA |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Nace el `CA-04` desde el pendiente 69: el andamio levanta solo la fase; la historia, el pendiente y sus índices se escriben a mano. Se abre la fase B |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Fase B ejecutada y cerrada: el andamio levanta la historia y el pendiente con sus índices. 27.2.0 |
