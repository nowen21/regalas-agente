# Plan de mantenimiento   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué hay que hacerle a Cimiento después de entregado** para que siga sirviendo: cada cuánto, quién, y qué pasa si no se hace.

---

## 1. Qué se mantiene

| Parte | Qué es | Qué la desgasta |
|---|---|---|
| El cuerpo de reglas | `base/`, 257 reglas | Reglas que dejan de responder a un problema real |
| Los moldes | `plantillas/`, 22 moldes | Moldes que se vuelven pesados y nadie llena |
| Los validadores | `validadores/`, 32 comprobaciones | Convenciones que cambian y dejan al lector atrás |
| La plataforma | `plataforma/`, 13 módulos | Índices que quedan viejos frente al disco |
| El expediente | `documentacion/` y `cvds/` | Documentos que dejan de decir lo que pasa |

---

## 2. Lo que hay que hacer, y cada cuánto

| Cada | Qué | Con qué | Si no se hace |
|---|---|---|---|
| **Cada sesión** | Correr las dos baterías | `manage.py test` · `validar.py internas` | Se acumula rojo sin que nadie lo vea |
| **Cada sesión** | Mirar el tablero | `/tablero/` | Los avisos crecen hasta volverse ruido |
| **Antes de planear** | **Traer de nuevo el proyecto** | Su pantalla, o `reconstruir_traido` | **El expediente responde sobre una copia vieja** |
| **Antes de planear** | Revisar el backlog contra lo que ya existe | `pendientes/README.md` | Se planea trabajo que ya está hecho |
| **Antes de publicar** | La puerta de publicación | `manage.py puerta_de_publicacion` | Se publica rompiendo lo anterior |
| **Cada tanto** | Revisar la vigencia de las reglas | `python validadores/vigencia.py` | Reglas que evitan un problema que ya no existe |

**La tercera fila salió de un caso real**, y por eso está: el expediente reportó 22 documentos faltantes que existían, porque la copia traída tenía **546 documentos menos** que el disco.

---

## 3. Lo que está declarado y no se va a arreglar solo

| Qué | Por qué se deja | Cuándo se revisaría |
|---|---|---|
| **33 fases con su frase y su tabla en desacuerdo** | Arreglarlas es reescribir fases cerradas, y eso no se hace | Nunca. Se leen como están |
| **107 fases con tablas de otro modelo** | Lo mismo | Nunca |
| **Seis módulos sin pantalla** | No los pide ninguna ficha | Cuando alguien los use de verdad |
| **La medición inicial que no existe** | No se puede reconstruir | Nunca. Lo que se puede es no repetirlo |

**Que estén acá es lo que las vuelve deuda declarada y no deuda escondida.** Una deuda que nadie escribió se descubre el día que estorba.

---

## 4. Quién

Una sola persona, con el agente. **No hay turnos, no hay guardia y no hay escalamiento**, y decirlo importa: un plan de mantenimiento que promete disponibilidad sin nadie que responda promete lo que no puede.

---

## 5. Cómo entra un cambio después de entregado

El mismo camino de siempre, sin atajos por ser mantenimiento:

1. Lo que se ve se anota en `pendientes/`, o como señal si es un aprendizaje.
2. Un pendiente se baja a historia de usuario (`02·F23`).
3. La historia se construye como fase, con su plan y sus pruebas.
4. Todo cambio de `base/` o `plantillas/` **sube la versión y entra al registro** (`20·M10`).

**Nada se renumera y nada se borra.** Las reglas se derogan (`20·M11`), porque las fases cerradas las citan por su identificador.

---

## 6. Cuándo este plan deja de valer

Cuando Cimiento tenga un usuario que no sea quien lo escribió. **Todo lo de arriba supone una sola persona en una sola máquina**, y esa suposición es la primera que se rompe.
