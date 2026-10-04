# Prueba en el proyecto que reportó

Hecha por Cimiento el 2026-10-04, en una copia temporal de scilit (`C:/DesarrollosClaude/personales/scilit`) (`02·F29`).

| Qué se probó | Cómo | Resultado |
|---|---|---|
| `git commit -F - <<'EOF'` | `freno.destinos`: ninguna ruta | Pasa |
| `sed -i` con el patrón `\*\*Al` | `freno.destinos`: ['documentacion/analysis/spec.md'] | Pasa |
| `mkdir -p templates/registration` desde `proyectos/scilit/`, con el plan que declara `proyectos/scilit/templates/registration/login.html` | `freno.motivo` con el plan real: se deja | Pasa |

**Resultado:** pasa
