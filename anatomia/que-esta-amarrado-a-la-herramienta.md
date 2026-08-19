# Qué sobrevive si mañana el agente es otro

**Medido el 2026-08-18**, del punto 1 del [pendiente 15](../pendientes/15-el-estandar-depende-de-una-sola-herramienta.md). Contesta una sola pregunta: **si el usuario deja de trabajar con esta herramienta, ¿qué se queda y qué se cae?**

Hasta hoy nadie lo sabía. Las reglas son texto y sirven en cualquier parte; **lo que las hace cumplir, no** — y no había ningún archivo que dijera cuáles piezas están amarradas.

## Las tres columnas

| | Qué es | Qué pasa si cambia el agente |
|---|---|---|
| 🟢 **Sirve con cualquiera** | Texto y programas que solo leen y escriben archivos | **Se queda entero** |
| 🟡 **Adaptador** | Lo que habla con *esta* herramienta: sus enganches, su archivo de entrada, su formato | **Hay que rehacerlo** |
| ⚪ **De la máquina** | Rutas locales, configuración que no se versiona | No viaja, y no debe |

## Los programas: 18 amarrados de 59

**Un tercio.** El resto —41— solo lee y escribe archivos, y funcionaría igual con cualquier agente o sin ninguno.

| Pieza | Cuánto la nombra | Qué es |
|---|---:|---|
| `pruebas.py` | 72 | 🟡 pero **engañoso**: son las pruebas *de* los adaptadores, no adaptador |
| `instalar.py` | 54 | 🟡 **el amarre grande** — escribe `.claude/settings.json` |
| `checklist.py` | 18 | 🟡 revisa que los enganches estén puestos |
| `sesion.py` | 14 | 🟡 |
| `hook_resumen` · `hook_historico` · `hook_recuerdos` · `hook_senales` · `hook_sesion` · `hook_md` · `hook_checklist` · `hook_relacionadas` | 3 a 8 | 🟡 **son la definición de adaptador**: existen porque la herramienta los llama |
| `version.py` · `versiones.py` · `historico.py` · `recuerdos.py` · `cargador.py` · `brevedad.py` | 1 a 8 | 🟡 **a medias** — el trabajo es agnóstico y solo el borde nombra la herramienta |

### Las 41 libres, por su nombre

**Se nombran una por una a propósito.** Antes iban solo por su total, y así una pieza nueva entraba en el recuento sin que nadie la hubiera mirado — que es como envejece un mapa escrito a mano.

`acciones.py` · `aislamiento.py` · `andamio.py` · `calidad.py` · `cerrar.py` · `ci.py` · `citas.py` · `codigo.py` · `commits.py` · `comun.py` · `cruces.py` · `declaracion.py` · `dependencias.py` · `enlaces.py` · `enmascarar.py` · `entidades.py` · `errores.py` · `esquema.py` · `estructura.py` · `fases.py` · `flujo.py` · `herramientas.py` · `indices.py` · `marcas.py` · `metareglas.py` · `migraciones.py` · `numeracion.py` · `pendientes.py` · `plantillas.py` · `rama.py` · `reaperturas.py` · `relacionadas.py` · `rendimiento.py` · `respaldo.py` · `resumen.py` · `secretos.py` · `seguridad.py` · `trazabilidad.py` · `validar.py` · `versionado.py` · `vigencia.py`

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
