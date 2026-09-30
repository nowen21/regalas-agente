# Guiones del 2026-09-28

De la fase `B` de `EP-005·HU-023`: que cada regla diga a qué tareas aplica. No se vuelven a correr; se guardan para leer cómo se hizo.

| Archivo | Qué hizo |
|---|---|
| [historico-chat/scripts/2026-09-28/listar-reglas-sin-tareas.py](listar-reglas-sin-tareas.py) | Listó las 242 reglas vigentes sin línea `**Aplica a:**`, con su título y su cuerpo, para leerlas una por una |
| [historico-chat/scripts/2026-09-28/reglas-sin-tareas.md](reglas-sin-tareas.md) | Esa lista, tal como salió antes de anotarlas |
| [historico-chat/scripts/2026-09-28/clasificacion-de-tareas.tsv](clasificacion-de-tareas.tsv) | La decisión del agente: qué tareas lleva cada regla, leída la regla |
| [historico-chat/scripts/2026-09-28/poner-lineas-aplica-a.py](poner-lineas-aplica-a.py) | Escribió las 242 líneas desde esa tabla, después del ejemplo de cada regla y antes de lo que la cierra |

De las fases `C` de HU-009 (EP-005), `D` de HU-012 (EP-004) y `C` de HU-023 (EP-005). **Se escribieron fuera del repositorio**, en la carpeta temporal de la herramienta, en contra de [`04·S18`](../../../base/04-seguridad.md#s18--el-guion-de-apoyo-se-escribe-dentro-del-repositorio-y-se-queda), y se trajeron acá el mismo día cuando el usuario lo señaló.

| Archivo | Qué hizo |
|---|---|
| [historico-chat/scripts/2026-09-28/arreglar.py](arreglar.py) | Intentó unir cadenas partidas en `recuerdos.py` y dañó el final del archivo; se restauró desde git |
| [historico-chat/scripts/2026-09-28/medir.py](medir.py) | Midió los caracteres y el tiempo del arranque en el estándar, en un proyecto y sin estructura base |
| [historico-chat/scripts/2026-09-28/clase_cargador.py](clase_cargador.py) | Las pruebas nuevas de `cargador.py` para `pruebas.py` |
| [historico-chat/scripts/2026-09-28/reemplazar_clase.py](reemplazar_clase.py) | Puso esa clase en `pruebas.py` en lugar de la vieja |
| [historico-chat/scripts/2026-09-28/parche_hook_md.py](parche_hook_md.py) | Agregó a `hook_md.py` la medición de las marcas de lo recién escrito |
| [historico-chat/scripts/2026-09-28/parche_sesion.py](parche_sesion.py) | Pasó a tabla los campos del hallazgo en `plantillas/sesion.md` |
| [historico-chat/scripts/2026-09-28/parche_sesion2.py](parche_sesion2.py) | Ajustó las explicaciones del mismo molde a la forma de celda |
| [historico-chat/scripts/2026-09-28/parche_sesion3.py](parche_sesion3.py) | Pasó a tabla el «Viene de» y devolvió el punto medio a las celdas |
| [historico-chat/scripts/2026-09-28/parche_resumen.py](parche_resumen.py) | Enseñó a `resumen.py` a leer los campos en tabla y en viñeta |
| [historico-chat/scripts/2026-09-28/parche_hu023.py](parche_hu023.py) | Sumó a HU-023 las reglas de negocio RN-07 a RN-09 y los criterios CA-08 a CA-10 |
| [historico-chat/scripts/2026-09-28/tareas_nuevo.md](tareas_nuevo.md) | El texto nuevo de `base/tareas.md`, con las columnas de palabras clave y de acciones |
| [historico-chat/scripts/2026-09-28/parche_recuperar.py](parche_recuperar.py) | Cambió `recuperar.py` para elegir por la palabra clave |
| [historico-chat/scripts/2026-09-28/parche_pruebas.py](parche_pruebas.py) | Reescribió las pruebas del recuperador a mensajes con palabra clave |
| [historico-chat/scripts/2026-09-28/parche_mover.py](parche_mover.py) | Llevó los archivos por tarea a `base/reglas-por-tarea/`, como decía el plan, y dejó de contar una lectura parcial como completa |
