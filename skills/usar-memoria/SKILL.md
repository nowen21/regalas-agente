---
name: usar-memoria
description: Consulta y registra señales en la memoria central buscable (SQLite+FTS5). Úsala ANTES de trabajar en un tema (traer señales relevantes) y AL CERRAR (registrar decisiones, errores resueltos, gotchas, aprendizajes). Es el backend operativo de la memoria por señales (13·DOC5). Responde a "qué sabemos de X", "guardá esta decisión/lección".
---

# Usar memoria (señales buscables)

Backend **operativo** de la memoria por señales: una base central SQLite+FTS5 compartida por todos los proyectos. El campo `scope` separa lo de cada proyecto de lo común (`organizacion`). El agente la usa con el helper `memoria/memoria.py` del estándar (ruta central declarada en la capa 3).

## Cuándo se usa

- **Antes de trabajar** en un tema: buscar señales relevantes (recencia + relevancia) y aplicarlas. Es la extensión de `02`·F1 a la memoria.
- **Al cerrar / al aprender algo**: registrar la señal nueva con el `scope` correcto.

## Consultar (antes de actuar)

```
python <ruta-estandar>/memoria/memoria.py search "palabras clave del tema" \
    --scope proyecto:<slug-del-proyecto>     # lo de este proyecto
python <ruta-estandar>/memoria/memoria.py search "palabras clave" --scope organizacion
```

- Buscar en **dos alcances**: el del proyecto actual **y** `organizacion` (las lecciones universales).
- **Verificar antes de confiar** (`01`·C2): una señal vieja puede estar obsoleta; si nombra un archivo/función, confirmar que aún existe.
- **Búsqueda por significado (opcional):** si están instalados los extras (`memoria/requirements-semantica.txt`), `search` es **híbrida** —léxica (FTS5) ∪ semántica— y encuentra señales relevantes aunque no compartan las palabras exactas. Corre local, offline; el contenido no sale de la máquina. Tras agregar señales, actualizar los vectores con `memoria.py indexar` (incremental). Sin los extras, `search` sigue funcionando solo con FTS5. `--lexica` fuerza solo palabras.

## Registrar (al cerrar o aprender algo)

```
python <ruta-estandar>/memoria/memoria.py add \
    --tipo <decision|error-resuelto|patron|aprendizaje|alternativa-descartada|supuesto|restriccion|pregunta-abierta|gotcha|deuda-tecnica> \
    --titulo "resumen corto" --what "..." --why "..." --where "archivo:linea" --learned "..." \
    --scope <organizacion | proyecto:<slug> | modulo:<slug>> --autor agente
```

**Elegir el `scope` con criterio:**
- `organizacion` → lecciones/decisiones/reglas que sirven a **cualquier** proyecto (seguridad, preferencias del usuario, reglas del cliente, gotchas del entorno). Estas **viajan** a los demás proyectos.
- `proyecto:<slug>` → algo propio de **ese** proyecto.
- `modulo:<slug>` → algo propio de un módulo.

## Supersesión (una decisión cambia)

No borrar la vieja: registrar la nueva enlazando a la anterior.

```
python <ruta-estandar>/memoria/memoria.py add --tipo decision --titulo "..." --reemplaza S-003 ...
```

Marca `S-003` como `reemplazada` y deja rastro (`13`·DOC5, patrón "Decisiones ya tomadas").

## Vigencia y poda (que lo viejo no tape lo nuevo)

Cada señal guarda su **última revisión** (`revisada`), no solo cuándo se creó. En `search` y `list`, una señal sin revisar hace más de 6 meses sale marcada `⚠ sin verificar hace Nm` (ajustable con `--meses`); a igualdad de relevancia, la más reciente va primero.

```
python .../memoria.py revisar S-003                      # la confirmo: revisada = hoy
python .../memoria.py revisar --viejas --scope proyecto:x # ritual: las más viejas primero
python .../memoria.py archivar S-003                     # poda: sale de search, se conserva
```

- **Ritual de revisión:** cada tanto, `revisar --viejas` de un scope y, señal por señal, confirmar (`revisar <id>`), reemplazar (`add --reemplaza`) o podar (`archivar`).
- **Podar ≠ borrar:** `archivar` deja `estado='archivada'` (fuera de `search`, pero la señal se conserva). No hay comando de borrado. Las `decision` y `restriccion` son historia: se pueden archivar, nunca borrar.

## Deuda diferida y preguntas abiertas (que no se pierdan)

Lo que el agente **difiere** —lo de `§Fuera-de-scope` del spec, un `gap-N`, una duda sin resolver— se registra como señal `deuda-tecnica` o `pregunta-abierta`, y se **cierra** cuando alguna fase lo resuelve. Así "¿qué queda abierto del módulo X?" es una consulta, no releer 40 specs.

```
python .../memoria.py pendientes --scope modulo:facturacion    # lo abierto de un scope
python .../memoria.py cerrar S-014 --ref "F3 / commit abc1234" # resuelto: fuera, con rastro
```

Enganches en el flujo (`02`):
- **Al declarar algo en `§Fuera-de-scope`** (o un `gap`): registrar la señal (`add --tipo deuda-tecnica|pregunta-abierta`). No basta con escribirlo en el spec.
- **Al abrir una fase:** `pendientes --scope <módulo>` antes de planificar, para no re-diferir lo mismo.
- **Al cerrar una fase:** `cerrar <id> --ref "<fase / commit>"` lo que esa fase resolvió.

`cerrar` deja `estado='cerrada'` con fecha y referencia: sale de `search` y de `pendientes`, pero se conserva (nunca se borra).

## Primera vez

Si la base no existe: `python <ruta-estandar>/memoria/memoria.py init` (crea `memoria/senales.db`, ignorado por git — es data del usuario).

Ver: `13`·DOC5 (registrar señales), `memoria/esquema.sql`, y las notas [`memoria-por-senales.md`](../../notas/memoria-por-senales.md) (qué guardar, `scope`) y [`memoria-buscable-fts5.md`](../../notas/memoria-buscable-fts5.md).
