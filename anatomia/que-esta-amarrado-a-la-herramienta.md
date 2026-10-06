# Qué sobrevive si mañana el agente es otro

Contesta una sola pregunta: **si el usuario deja de trabajar con esta herramienta, ¿qué se queda y qué se cae?** Nació el 2026-08-18, del punto 1 del [pendiente 15](../pendientes/hecho/el-estandar-depende-de-una-sola-herramienta.md). Las reglas son texto y sirven en cualquier parte; lo que las hace cumplir, no siempre.

## Las tres columnas

| | Qué es | Qué pasa si cambia el agente |
|---|---|---|
| **Sirve con cualquiera** | Texto y programas que solo leen y escriben archivos | **Se queda entero** |
| **Adaptador** | Lo que habla con *esta* herramienta: sus enganches, su archivo de entrada, su formato | **Hay que rehacerlo** |
| **De la máquina** | Rutas locales, configuración que no se versiona | No viaja, y no debe |

## 2026-10-05, el código pasó a Cimiento

Desde el análisis 1 del pendiente 116 (filas 13 a 22), los programas viven en [`proyectos/cimiento/core/`](../proyectos/cimiento/core/), repartidos en `comun/`, `validadores/`, `enganches/` y `herramientas/`. En `validadores/` quedaron solo las puertas: los programas que las reglas, las plantillas y los proyectos instalados llaman por esa ruta, y que le pasan la orden a `core/`. Los enganches siguen en [`adaptadores/claude-code/`](../adaptadores/claude-code/).

`validar.py amarre` mira esas seis carpetas, sin las pruebas. **El recuento, corrido y no calculado, da 34 amarrados de 119.** Con `EP-025` entraron siete piezas: tres amarradas (`desinstalar.py`, `guiones.py` y `md.py`) y cuatro libres. Antes del traslado eran 30 de 89: subió el total porque el código se partió en clases y piezas comunes, y bajaron los amarrados porque se fue la suite vieja de pruebas, que nombraba la herramienta sin estar amarrada.

### Las amarradas

| Pieza | Dónde | Qué es |
|---|---|---|
| `hook_acuerdos`, `hook_analisis`, `hook_antes`, `hook_checklist`, `hook_checkpoint`, `hook_despues`, `hook_externo`, `hook_historico`, `hook_md`, `hook_presupuesto`, `hook_recuerdos`, `hook_redaccion`, `hook_reglas`, `hook_relacionadas`, `hook_resumen`, `hook_senales`, `hook_sesion`, `hook_veredicto` | `adaptadores/claude-code/`; ocho tienen además su puente en `validadores/` | **son la definición de adaptador**: existen porque la herramienta los llama |
| `instalar.py` | `core/herramientas/`, y su puerta en `validadores/` | **el amarre grande**: escribe `.claude/settings.json` |
| `enganches.py` | `core/comun/` | el catálogo de los enganches que se instalan, con los eventos de la herramienta (fila 23 del análisis 1 del pendiente 116) |
| `checklist.py` | `core/validadores/` | revisa que los enganches estén puestos |
| `sesion.py` | `core/enganches/` | lo que se entrega al abrir la sesión |
| `desinstalar.py` | `core/herramientas/` | la contraria de `instalar.py`: quita de `.claude/settings.json` lo que el instalador puso (`EP-025·HU-021`) |
| `guiones.py` | `core/enganches/` | reconoce el guion que vuelve a leer la carpeta de sesiones de la herramienta (`EP-025·HU-017`) |
| `md.py` | `core/enganches/` | **a medias**: el trabajo de `hook_md` pasó a `core/` y solo su historia nombra el adaptador (`EP-025·HU-014`) |
| `version.py`, `versiones.py`, `historico.py`, `recuerdos.py`, `recuperar.py`, `mapa_tareas.py`, `brevedad.py`, `expediente.py` | `core/`, y algunas con su puerta en `validadores/` | **a medias**: el trabajo es agnóstico y solo el borde nombra la herramienta |

### Las libres, por su nombre

Se nombran una por una a propósito: así una pieza nueva no entra al recuento sin que nadie la haya mirado.

`acciones.py`, `acuerdos.py`, `aislamiento.py`, `analisis.py`, `analisis_en_curso.py`, `andamio.py`, `archivos.py`, `autorizado.py`, `aviso_resuelto.py`, `base.py`, `calidad.py`, `cambios.py`, `cargador.py`, `cerrar.py`, `checkpoint.py`, `ci.py`, `citas.py`, `codigo.py`, `commits.py`, `configuracion.py`, `consola.py`, `conteo.py`, `corredor.py`, `cruces.py`, `declaracion.py`, `dependencias.py`, `ejecutable.py`, `enlaces.py`, `enmascarar.py`, `entidades.py`, `epicas.py`, `errores.py`, `esquema.py`, `estacion.py`, `estado_en_base.py`, `estructura.py`, `externo.py`, `fase.py`, `fases.py`, `flujo.py`, `freno.py`, `git.py`, `guardian_version.py`, `hallazgos.py`, `herramientas.py`, `hook_estacion.py`, `hook_rutas.py`, `hook_turno.py`, `indices.py`, `inmutable.py`, `marcas.py`, `markdown.py`, `metareglas.py`, `migraciones.py`, `moldes.py`, `niveles.py`, `numeracion.py`, `origen.py`, `parecidas.py`, `pendientes.py`, `plan_vs_hecho.py`, `plantillas.py`, `presupuesto.py`, `proyecto.py`, `rama.py`, `reaperturas.py`, `redaccion.py`, `relacionadas.py`, `rendimiento.py`, `repetidas.py`, `respaldo.py`, `resumen.py`, `retirar.py`, `rutas_fuera.py`, `secretos.py`, `seguridad.py`, `sesiones.py`, `sitio.py`, `temas.py`, `traza.py`, `trazabilidad.py`, `validar.py`, `veredicto.py`, `veredictos.py`, `versionado.py`, `vigencia.py`

Ninguna nombra la herramienta. **Funcionan con cualquier agente, o sin ninguno.** Tres enganches salen libres (`hook_estacion`, `hook_rutas` y `hook_turno`): los llama git o reciben la ruta, y no nombran nada de la herramienta en su código, aunque vivan en el adaptador.

## El corte, en una línea

Lo que mide vive en `core/`; lo que existe **porque una herramienta concreta lo llama** vive en `adaptadores/`. Si mañana el agente es otro, `core/` se queda entero y lo que hay que rehacer son los enganches y las líneas de `instalar.py` que escriben la configuración de la herramienta.

## `base/` y la herramienta

La medición del 2026-08-18 encontró que `base/` nombraba la herramienta 26 veces, casi todas como `CLAUDE.md`, el archivo de entrada. Es un amarre superficial (renombrar un archivo, no reescribir reglas), pero [`20·M3`](../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) lo prohíbe y el validador de tecnología no lo ve, porque busca lenguajes y frameworks.

## Cómo se rehace

Se cuentan las apariciones de `.claude`, `CLAUDE.md`, `settings.json`, `hook_`, `PostToolUse`, `UserPromptSubmit`, `SessionStart` y `Stop` en cada archivo. Se cuenta el nombre de la herramienta, no la palabra «agente»: el estándar habla de un agente todo el tiempo y eso no es amarre. Lo hace `validar.py amarre`, con la misma lista que este mapa.

## Lo que este mapa no hace

- **No se actualiza solo.** Una pieza nueva no aparece acá hasta que alguien la agregue; `validar.py amarre` lo reclama en la primera corrida.
- **No dice si la clasificación es la correcta**: eso se lee.

La historia de cada pieza antes del 2026-10-05 está en el historial de git de este archivo.
