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

## Primera vez

Si la base no existe: `python <ruta-estandar>/memoria/memoria.py init` (crea `memoria/senales.db`, ignorado por git — es data del usuario).

Ver: `13`·DOC5 (registrar señales), `memoria/esquema.sql`, y las notas [`memoria-por-senales.md`](../../notas/memoria-por-senales.md) (qué guardar, `scope`) y [`memoria-buscable-fts5.md`](../../notas/memoria-buscable-fts5.md).
