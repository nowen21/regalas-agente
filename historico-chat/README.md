# Histórico de sesiones

Registro de lo que se hizo en cada sesión de chat con el agente. Sirve para retomar el trabajo sin releer el chat y para saber por qué quedó algo como quedó.

No es parte del estándar (`base/`, `plantillas/`, `skills/`); es bitácora, igual que `notas/`.

## Cómo se escribe

- Un archivo por sesión: `AAAA-MM-DD-tema.md` (si hay dos sesiones el mismo día, `AAAA-MM-DD-tema-2.md`).
- **Es la transcripción del diálogo, no un resumen.** Va **cada** mensaje del usuario y **cada** respuesta del agente, en orden, sin saltarse ninguno.
- **Ambos lados van literales:** el mensaje del usuario tal como lo escribió, y la respuesta del agente tal como la dio (tablas, bloques de código y ejemplos incluidos). No se condensa ni se parafrasea: si el agente dio un ejemplo de 20 líneas, esas 20 líneas quedan.
- Lo único que se omite es la salida cruda de herramientas (listados, resultados de comandos): eso no es diálogo.
- **Cada interacción lleva marca de tiempo** `AAAA-MM-DD HH:MM:SS`, tanto la del usuario como la del agente. Así se ve cuándo pasó cada cosa y cuánto tomó.
- La hora se **lee del reloj del sistema**, nunca se inventa: `date "+%Y-%m-%d %H:%M:%S"` (o `Get-Date -Format "yyyy-MM-dd HH:mm:ss"`). Se toma una al recibir el mensaje del usuario y otra al escribir la respuesta.
- Se crea **apenas la sesión produce su primera decisión o cambio**, y se **actualiza cada vez que se cierra un tema**. No se espera al final: un chat rara vez tiene cierre explícito.
- Los pendientes reales siguen viviendo en `pendientes/`; aquí solo se apunta a ellos.

## Plantilla

```markdown
# AAAA-MM-DD — Tema

## Conversación

### 1 · Usuario — AAAA-MM-DD HH:MM:SS
> La pregunta, literal.

**Agente** — AAAA-MM-DD HH:MM:SS
La respuesta condensada: qué se decidió, por qué, qué se descartó
y qué archivo se tocó.

### 2 · Usuario — AAAA-MM-DD HH:MM:SS
> La siguiente pregunta, literal.

**Agente** — AAAA-MM-DD HH:MM:SS
…

## Abierto
- Lo que quedó sin cerrar, o "nada".
```

## Índice

- [2026-08-06-historico-chat.md](2026-08-06-historico-chat.md) — se crea esta carpeta; queda el trabajo previo de despliegue y observabilidad (`base/18`, `base/19`).
- [2026-08-06-meta-reglas-2.md](2026-08-06-meta-reglas-2.md) — la regla de reglas (`base/00-meta-reglas.md`); formato del histórico: transcripción literal con marca de tiempo.
- [2026-08-06-sesion-3.md](2026-08-06-sesion-3.md) — sesión nueva; el histórico no se estaba escribiendo, se crea al ser señalado.
- [2026-08-06-sesion-4.md](2026-08-06-sesion-4.md) — sesión del 2026-08-06.
- [2026-08-06-sesion-5.md](2026-08-06-sesion-5.md) — auditoría: qué tanto cumple `base/` sus propias meta-reglas (`00-meta-reglas.md`).
- [2026-08-06-sesion-6.md](2026-08-06-sesion-6.md) — sesión del 2026-08-06.
- [2026-08-06-sesion-7.md](2026-08-06-sesion-7.md) — el agente no recibe audio; alternativas para transcribir.
- [2026-08-06-sesion-8.md](2026-08-06-sesion-8.md) — sesión del 2026-08-06.
- [2026-08-06-sesion-9.md](2026-08-06-sesion-9.md) — se crea la carpeta `diplomado-ia/`.
- [2026-08-07-sesion.md](2026-08-07-sesion.md) — sesión del 2026-08-07.
- [2026-08-07-sesion-2.md](2026-08-07-sesion-2.md) — sesión del 2026-08-07.
- [2026-08-07-sesion-3.md](2026-08-07-sesion-3.md) — sesión del 2026-08-07.
- [2026-08-07-analisis-cumplimiento-reglas.md](2026-08-07-analisis-cumplimiento-reglas.md) — auditoría de las 170 reglas de `base/` contra las 13 meta-reglas del capítulo 20; informe en `analisis/`.
- [2026-08-07-sesion-5.md](2026-08-07-sesion-5.md) — sesión del 2026-08-07.
