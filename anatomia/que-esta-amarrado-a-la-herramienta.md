# Qué sobrevive si mañana el agente es otro

**Medido el 2026-08-18**, del punto 1 del [pendiente 15](../pendientes/hecho/el-estandar-depende-de-una-sola-herramienta.md). Contesta una sola pregunta: **si el usuario deja de trabajar con esta herramienta, ¿qué se queda y qué se cae?**

Hasta hoy nadie lo sabía. Las reglas son texto y sirven en cualquier parte; **lo que las hace cumplir, no** — y no había ningún archivo que dijera cuáles piezas están amarradas.

## Las tres columnas

| | Qué es | Qué pasa si cambia el agente |
|---|---|---|
| 🟢 **Sirve con cualquiera** | Texto y programas que solo leen y escriben archivos | **Se queda entero** |
| 🟡 **Adaptador** | Lo que habla con *esta* herramienta: sus enganches, su archivo de entrada, su formato | **Hay que rehacerlo** |
| ⚪ **De la máquina** | Rutas locales, configuración que no se versiona | No viaja, y no debe |

## 2026-08-19 · el adaptador se mudó a su propia carpeta

**Los ocho `hook_*` ya no viven en `validadores/`.** Están en
[`adaptadores/claude-code/`](../adaptadores/claude-code/), y el contrato de qué
necesita el estándar de cualquier agente está en
[`adaptadores/contrato.md`](../adaptadores/contrato.md).

**La frontera, en una línea:** `validadores/` es lo que sirve con cualquier
agente; `adaptadores/` es lo que existe **porque una herramienta concreta lo
llama**.

**El recuento no cambia, y eso es lo importante.** Siguen siendo 18 amarradas
de 59: `validar.py amarre` mira **las dos carpetas**. Mirar solo `validadores/`
habría dicho «10 de 51» y habría sonado a mejora, cuando lo que hubo fue una
mudanza — y un adaptador que nadie mira vuelve a ser el problema que este mapa
vino a resolver.

**Los proyectos instalados se enteran solos.** La ruta vieja quedó vencida en
su `.claude/settings.json`, y `checklist.py` compara el comando exacto: lo
reporta en el primer mensaje de la siguiente sesión, y el instalador lo
reemplaza.

## Los programas: 24 amarrados de 69

**Un tercio.** El resto —45— solo lee y escribe archivos, y funcionaría igual con cualquier agente o sin ninguno.

| Pieza | Cuánto la nombra | Qué es |
|---|---:|---|
| `pruebas.py` | 72 | 🟡 pero **engañoso**: son las pruebas *de* los adaptadores, no adaptador |
| `instalar.py` | 54 | 🟡 **el amarre grande** — escribe `.claude/settings.json` |
| `checklist.py` | 18 | 🟡 revisa que los enganches estén puestos |
| `sesion.py` | 14 | 🟡 |
| `hook_resumen` · `hook_historico` · `hook_recuerdos` · `hook_senales` · `hook_sesion` · `hook_md` · `hook_checklist` · `hook_relacionadas` · `hook_presupuesto` · `hook_checkpoint` · `hook_veredicto` · `hook_externo` | 3 a 8 | 🟡 **son la definición de adaptador**: existen porque la herramienta los llama |
| `version.py` · `versiones.py` · `historico.py` · `recuerdos.py` · `cargador.py` · `brevedad.py` | 1 a 8 | 🟡 **a medias** — el trabajo es agnóstico y solo el borde nombra la herramienta |

### Las 46 libres, por su nombre

**Se nombran una por una a propósito.** Antes iban solo por su total, y así una pieza nueva entraba en el recuento sin que nadie la hubiera mirado — que es como envejece un mapa escrito a mano.

`acciones.py` · `aislamiento.py` · `andamio.py` · `calidad.py` · `cerrar.py` · `checkpoint.py` · `ci.py` · `citas.py` · `codigo.py` · `commits.py` · `comun.py` · `conteo.py` · `cruces.py` · `declaracion.py` · `dependencias.py` · `enlaces.py` · `enmascarar.py` · `entidades.py` · `errores.py` · `esquema.py` · `estructura.py` · `expediente.py` · `externo.py` · `fases.py` · `flujo.py` · `guardian_version.py` · `herramientas.py` · `indices.py` · `inmutable.py` · `marcas.py` · `metareglas.py` · `migraciones.py` · `numeracion.py` · `pendientes.py` · `plantillas.py` · `presupuesto.py` · `rama.py` · `reaperturas.py` · `relacionadas.py` · `rendimiento.py` · `respaldo.py` · `resumen.py` · `secretos.py` · `seguridad.py` · `sitio.py` · `temas.py` · `traza.py` · `trazabilidad.py` · `validar.py` · `veredicto.py` · `versionado.py` · `vigencia.py`

Ninguna nombra la herramienta. **Funcionan con cualquier agente, o sin ninguno.**

**Los ocho `hook_*` son el adaptador de verdad.** `instalar.py` es lo que los enchufa. Todo lo demás está amarrado por el borde y se despega con poco.

## Y el hallazgo que no se buscaba: `base/` nombra la herramienta 26 veces

**`base/` es lo que se hereda y lo que se declara agnóstico.** [`20·M3`](../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) prohíbe nombrar una tecnología concreta.

| Dónde | Cuántas |
|---|---:|
| [`base/01-conducta.md`](../base/01-conducta.md) | **14** |
| [`base/20-meta-reglas/base.md`](../base/20-meta-reglas/base.md) | 3 |
| [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) | 2 |
| Otros siete archivos | 1 cada uno |

**Casi todas son `CLAUDE.md`**, el archivo de entrada de esta herramienta. Ninguna nombra un enganche ni un formato — la dependencia es de **un nombre de archivo**, no de la máquina que hay detrás.

**Eso es una buena noticia y conviene decirlo así:** el amarre de `base/` es superficial. Cambiar el agente obligaría a renombrar un archivo en diez sitios, no a reescribir reglas. Pero **hoy `M3` se incumple diez veces y nadie lo reporta**, porque el validador de tecnología busca lenguajes y frameworks, no herramientas de agente.

## Dónde pesa de verdad

| Carpeta | Marcas | Qué significa |
|---|---:|---|
| `historico-chat/` | 578 | **No cuenta**: es la transcripción, y ahí la herramienta se nombra porque se habló de ella |
| `validadores/` | 470 | Lo real, y concentrado en `instalar.py` y los ocho enganches |
| `documentacion/` | 344 | Fases que documentan haber construido los adaptadores |
| `pendientes/` | 72 | Reportes sobre la herramienta |
| `anatomia/` | 29 | Este mapa y sus vecinos |
| **`base/`** | **26** | **Lo único que preocupa** — ver arriba |
| `plantillas/` | 24 | Lo que se hereda; mismo caso que `base/` |
| `interfaz/` · `memoria/` · `metricas/` | **0** | Limpias |

## Lo que este mapa no hace

- **No mueve nada.** Recoger el adaptador en una carpeta propia es el punto 2 del pendiente, y es trabajo aparte.
- **No escribe el contrato** — qué necesita el estándar de cualquier agente. Es el punto 3.
- **No se actualiza solo.** Un archivo nuevo bajo `validadores/` no aparece acá hasta que alguien lo agregue, y eso es justo lo que `CA-03` de su historia pide que se note. Mientras tanto, el recuento se rehace corriendo la medición.

## Cómo se rehace

Se cuentan las apariciones de `.claude`, `CLAUDE.md`, `settings.json`, `hook_`, `PostToolUse`, `UserPromptSubmit`, `SessionStart` y `Stop` en cada archivo. **Se cuenta el nombre de la herramienta, no la palabra «agente»**: el estándar habla de un agente todo el tiempo y eso no es amarre.

## 2026-08-20 · cuatro piezas más, y el recuento sigue diciendo lo mismo

**`checkpoint.py` y `veredicto.py` son libres; `hook_checkpoint.py` y `hook_veredicto.py` son adaptador**, por el mismo corte de siempre: comparar dos fechas o copiar una celda sirve con cualquier agente; enterarse de que se escribió un archivo es de la herramienta. El recuento pasa de 21 de 62 a **23 de 66**, y la proporción no se mueve: un tercio.

**Lo que sí se movió es la prueba de la frontera.** Decía «ocho enganches» con el número escrito, la 27.0.0 agregó el noveno sin tocarla y quedó en rojo sin que nadie la corriera. Ahora cuenta contra la lista del instalador: un enganche que nadie enchufa, o un enchufe a un enganche que no existe, es lo que rompe la frontera, no el número.

## 2026-08-20 · el portero, y el recuento sigue diciendo lo mismo

**`externo.py` es libre; `hook_externo.py` es adaptador.** Decidir si una herramienta trajo algo de afuera y redactar el sobre de «dato, no orden» (`01·C27`) sirve con cualquier agente; enterarse de que una herramienta devolvió, y devolverle al agente un contexto adicional, es de la herramienta. El recuento pasa de 23 de 66 a **24 de 68**: un tercio, como siempre.

**Y `traza.py` también es libre.** Emparejar llamadas con respuestas y sumar duraciones lee un formato de transcripción, no habla con la herramienta — el mismo corte que `brevedad.py` y `presupuesto.py`. Con ella el total queda en **24 amarrados de 69**.

## 2026-08-28 · siete piezas que el mapa no nombraba, y el corte no se movió

**El mapa se quedó siete archivos atrás.** Salieron de cuatro fases seguidas —el commit que no se lleva lo ajeno, las rutas de afuera, la estación del commit y el registro del turno— y ninguna volvió a este archivo. Es el mismo defecto que el índice de la épica: **lo que se registra en dos sitios que se editan en momentos distintos, se queda atrás en el segundo**.

| Pieza | Libre o amarrada | Por qué |
|---|---|---|
| `sesiones.py` | 🟢 libre | Preguntarle a git qué cambió y anotarlo en un archivo sirve con cualquier agente |
| `rutas_fuera.py` | 🟢 libre | Decidir si una ruta cae fuera del proyecto es comparar dos rutas |
| `estacion_commit.py` | 🟢 libre | Marcar una casilla en una tabla de Markdown |
| `plan_vs_hecho.py` | 🟢 libre | Cruzar dos documentos del propio proyecto |
| `hook_rutas.py` | 🟡 adaptador | Existe porque la herramienta avisa que se escribió un archivo |
| `hook_estacion.py` | 🟡 adaptador | Lo mismo |
| `hook_turno.py` | 🟡 adaptador | Existe porque la herramienta avisa que terminó el turno |
| `corredor.py` | 🟢 libre | Cargar archivos de prueba y contar lo que corrieron sirve con cualquier agente — y con ninguno |

**El recuento, corrido y no calculado, da 26 amarrados de 82** —con `corredor.py`, que nació al día siguiente de esta línea y entró acá en la misma vuelta, porque su prueba lo reclamó.

## 2026-08-31 · tres piezas más, y el corte sigue donde estaba

De la fase que le puso a cada regla del núcleo quién la hace cumplir
(`EP-005·HU-012`). **Las tres entraron el mismo día que nacieron**, y esta vez no
porque alguien se acordara: la prueba del mapa las reclamó en la primera corrida.

| Pieza | Libre o amarrada | Por qué |
|---|---|---|
| `ejecutable.py` | 🟢 libre | Leer las reglas de `base/` y buscar una línea en cada una sirve con cualquier agente, y sin ninguno |
| `redaccion.py` | 🟢 libre | Contar el trato directo sobre un texto no habla con nadie: recibe la cadena y devuelve un número |
| `hook_redaccion.py` | 🟡 adaptador | Existe porque la herramienta avisa que terminó el turno, y le entrega la transcripción en su formato |

**El recuento, corrido y no calculado, da 27 amarrados de 85.** Sube uno porque de las tres piezas solo el enganche está amarrado.

**El corte es el mismo de siempre**, y por eso se repite: lo que mide vive en
`validadores/`, y lo que existe **porque una herramienta concreta lo llama**
vive en `adaptadores/`. Si mañana el agente es otro, `redaccion.py` se queda
entero y lo único que hay que rehacer son las diez líneas que leen el archivo de
la sesión.
