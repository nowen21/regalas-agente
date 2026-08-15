# Histórico de sesiones

Registro de lo que se hizo en cada sesión de chat con el agente. Sirve para retomar el trabajo sin releer el chat y para saber por qué quedó algo como quedó.

No es parte del estándar (`base/`, `plantillas/`, `skills/`); es bitácora, igual que `notas/`.

## Cómo se escribe

- Un archivo por sesión: `AAAA-MM-DD-tema.md` (si hay dos sesiones el mismo día, `AAAA-MM-DD-tema-2.md`).
- **El nombre se pone en la sesión, no al final.** El enganche crea `AAAA-MM-DD-sesion.md` porque al abrir el chat todavía no se sabe el tema; apenas hay una respuesta, le recuerda al agente que proponga nombre y resumen —una sola vez— y el usuario aprueba. El cambio lo hace el comando, que mueve el archivo, cambia el título y corrige la línea del índice a la vez:

  ```sh
  python "<estándar>/validadores/historico.py" --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"
  ```

  Con el comando, el agente pasa también la línea `/rename <tema>` para que la sesión de Claude Code —la pestaña, la barra del prompt, `/resume`— se llame igual que el archivo. Esa la pega el usuario: `/rename` es un comando suyo.
- **Es la transcripción del diálogo, no un resumen.** Va **cada** mensaje del usuario y **cada** respuesta del agente, en orden, sin saltarse ninguno.
- **Ambos lados van literales:** el mensaje del usuario tal como lo escribió, y la respuesta del agente tal como la dio (tablas, bloques de código y ejemplos incluidos). No se condensa ni se parafrasea: si el agente dio un ejemplo de 20 líneas, esas 20 líneas quedan.
- Lo único que se omite es la salida cruda de herramientas (listados, resultados de comandos): eso no es diálogo.
- **Cada interacción lleva marca de tiempo** `AAAA-MM-DD HH:MM:SS`, tanto la del usuario como la del agente. Así se ve cuándo pasó cada cosa y cuánto tomó.
- La hora se **lee del reloj del sistema**, nunca se inventa: `date "+%Y-%m-%d %H:%M:%S"` (o `Get-Date -Format "yyyy-MM-dd HH:mm:ss"`). Se toma una al recibir el mensaje del usuario y otra al escribir la respuesta.
- Se crea **apenas la sesión produce su primera decisión o cambio**, y se **actualiza cada vez que se cierra un tema**. No se espera al final: un chat rara vez tiene cierre explícito.
- Los pendientes reales siguen viviendo en `pendientes/`; aquí solo se apunta a ellos.
- **El resumen de la sesión va aparte, en [resumenes/](resumenes/README.md).** Es parte del histórico y por eso vive dentro, pero no se mezcla con la transcripción: aquella guarda lo que se dijo, el resumen guarda lo que quedó — los hallazgos, su estado y la pregunta que sigue viva.

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

Cada línea es una sesión: primero su transcripción, y después del `·` el enlace a **lo que dejó**, si ya tiene resumen ([`resumenes/`](resumenes/README.md)). Para retomar un tema se arranca por el resumen; la transcripción se abre cuando el resumen no alcanza.

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
- [2026-08-07-sesion-6.md](2026-08-07-sesion-6.md) — sesión del 2026-08-07.
- [2026-08-07-sesion-7.md](2026-08-07-sesion-7.md) — el capítulo `02 · Flujo de trabajo` pasa a carpeta y se somete al molde y al checklist: 9 CUMPLE, 10 NO (v2.5.0).
- [2026-08-07-sesion-8.md](2026-08-07-sesion-8.md) — sesión del 2026-08-07.
- [2026-08-07-sesion-9.md](2026-08-07-sesion-9.md) — granularidad de la fase: cuándo un CA por fase (`F12.9`) y cuándo varios (`F12.10`).
- [2026-08-07-memoria-del-agente-en-el-repo.md](2026-08-07-memoria-del-agente-en-el-repo.md) — la memoria del agente pasa a `historico-chat/memory/`; el almacén de la herramienta queda vacío (`01·C19`, v3.0.0).
- [2026-08-07-sesion-11.md](2026-08-07-sesion-11.md) — sesión del 2026-08-07.
- [2026-08-07-sesion-12.md](2026-08-07-sesion-12.md) — sesión del 2026-08-07.
- [2026-08-08-sesion.md](2026-08-08-sesion.md) — el `CLAUDE.md` pasa a ser el setup del agente: la instalación se hace sola con una línea y `02·F13` deja de detener el arranque (v5.0.0).
- [2026-08-08-sesion-2.md](2026-08-08-sesion-2.md) — sesión del 2026-08-08.
- [2026-08-08-sesion-3.md](2026-08-08-sesion-3.md) — sesión del 2026-08-08.
- [2026-08-08-sesion-4.md](2026-08-08-sesion-4.md) — la redacción del estándar pasa a entenderse sin saber del tema: nace `00·ID7` y se deroga `00·ID2` (v6.0.0).
- [2026-08-09-sesion.md](2026-08-09-sesion.md) — sesión del 2026-08-09.
- [2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md](2026-08-12-regla-de-respaldo-de-las-reglas-de-proyecto.md) — nace 20·M16: ninguna regla de proyecto existe sin un criterio de la base que la respalde (8.0.0).
- [2026-08-13-del-brief-a-los-planes-de-la-fase-a.md](2026-08-13-del-brief-a-los-planes-de-la-fase-a.md) — nace el brief del agente y sus siete épicas; las ocho HU de EP-001 y la fase A de HU-001 con sus planes (8.0.1, 8.1.0, 8.2.0, 9.0.0).
- [2026-08-14-resultado-de-pruebas-y-cierre-de-fase.md](2026-08-14-resultado-de-pruebas-y-cierre-de-fase.md) — sigue la sesión anterior: el cierre verifica que el plan de trabajo se hizo, y la deuda técnica dice de dónde salió (9.1.0, 9.2.0).
- [2026-08-13-pendientes-del-diplomado-de-ia.md](2026-08-13-pendientes-del-diplomado-de-ia.md) — cinco pendientes (12–16) que salen de comparar los apuntes del diplomado de IA contra el estándar.
- [2026-08-13-hu-de-la-comprobacion-automatica.md](2026-08-13-hu-de-la-comprobacion-automatica.md) — las 12 HU de EP-004 y donde cae lo que falta del pendiente 01. · [resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md](resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md)
- [2026-08-14-plan-de-trabajo-de-la-ep-001.md](2026-08-14-plan-de-trabajo-de-la-ep-001.md) — el plan de trabajo de la EP-001: bajar sus HU a fases.
- [2026-08-14-molde-para-pedir-en-la-sesion.md](2026-08-14-molde-para-pedir-en-la-sesion.md) — analisis del prompt base del usuario: el molde obligatorio con que se le pide trabajo al agente.
- [2026-08-14-indice-tematico-del-historico.md](2026-08-14-indice-tematico-del-historico.md) — cargar el histórico al iniciar ya lo hace un hook; nace la idea de un índice por temáticas y qué manda entre el brief y el histórico.
- [2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](2026-08-14-h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md) — cerrar H-4 · No había dónde escribir lo aprendido: el resumen de sesión y su enganche. · [resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md](resumenes/2026-08-14/h4-cerrar-h-4-no-habia-donde-escribir-lo-aprendido.md)

<!-- huella: 2a3060c58acb · estandar 15.0.0 -->
- [2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md](2026-08-14-el-enganche-del-resumen-no-crea-el-resumen.md) — por qué lo de H-4 no funciona: el enganche nunca crea el resumen y la prueba lo dio por bueno.
