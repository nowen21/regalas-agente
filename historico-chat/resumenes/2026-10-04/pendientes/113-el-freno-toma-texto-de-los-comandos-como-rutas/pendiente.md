# Pendiente: el freno toma texto de los comandos como rutas

Se resuelve en el [análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/pendientes/110-el-andamio-no-sirve-desde-un-proyecto/analisis-1.md), que reúne los cinco reportes de scilit.

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: los hallazgos del [resumen de la sesión del 2026-10-03](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-03/sesion.md); seguimiento en scilit: [pendiente 8](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/8-esperando-a-cimiento-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md) |

## El problema

`validadores/freno.py` detuvo órdenes válidas porque tomó como ruta de archivo texto que no lo era:

- `EOF`, el cierre de un `git commit -F - <<'EOF'`: «EL FRENO DETUVO ESTA ACCIÓN (`EOF`)».
- `\*\*Al`, parte de un patrón de `sed`: lo tomó como ruta fuera del proyecto.
- `mkdir -p templates/registration`, aunque el plan aprobado declaraba `templates/registration/login.html`.

Además, al abrir la sesión, marcó como hallazgo lo que escribe el instalador (`documentacion/versiones/`), que corre por mandato de `CLAUDE.md`.

## Por qué importa

Cada falso positivo detiene el trabajo y deja un hallazgo falso en el resumen de la sesión.
