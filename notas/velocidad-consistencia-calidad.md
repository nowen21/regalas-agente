# El estándar frente a: velocidad, consistencia y calidad

> De los tres, el estándar clava dos y el tercero tiene un matiz importante.

| | ¿Cumple? | Cómo |
|---|---|---|
| **Consistencia** | ✅ **Su fuerza #1** | Toda sesión trabaja igual: mismas reglas (`00`–`16`), la spec evita que cada charla reinterprete el negocio, la memoria conserva las decisiones. Mismo resultado con distinto día, proyecto o modelo. |
| **Calidad** | ✅ **Fuerte** | Pruebas + triangulación (`08`, `T7`), calidad de código (`07`), seguridad (`04`), trazabilidad (`13`·DOC3), atributos ISO 25010 (`16`), puertas de calidad. |
| **Velocidad** | ⚠️ **Matizado** | No optimiza el **primer borrador**; agrega fricción a propósito (spec antes de código, aprobar plan, correr pruebas, documentar). |

## El matiz de la velocidad

El estándar cambia **velocidad inicial** por **velocidad sostenida**:

- **Más lento por tarea suelta:** pedir spec, plan y pruebas tiene ceremonia. Para un cambio trivial, se siente más lento.
- **Más rápido en el proyecto entero:** evita **retrabajo** (bugs que cuestan más después), evita **re-entender** el proyecto cada sesión (`02`·F1), evita **re-discutir** decisiones ya tomadas, y ejecuta de corrido una vez aprobado el plan (`02`·F3, sin permiso por cada paso).
- **Velocidad cruda:** subiría al construir el **orquestador con sub-agentes en paralelo** (varios roles a la vez).

## En una frase

**Consistencia y calidad: de fábrica. Velocidad: sacrifica el arranque por el neto** — más lento en lo trivial, bastante más rápido en la vida del proyecto. La velocidad cruda vendría con el orquestador en paralelo.

Es el trade-off clásico: para ir **rápido y bien de forma sostenida**, hay que ir **un poco más despacio al principio**.
