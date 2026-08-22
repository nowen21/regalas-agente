<!-- sesion: bef7f802-f5de-415a-98d5-53d98363648e -->
<!-- nombre: preguntado -->

# 2026-08-22 — El encuadre enlaza la cadena no la copia

## Conversación

### 1 · Usuario — 2026-08-22 11:42:17
> no entiendo qué es lo que se quiere comunicar:
>
> "
> Encuadre para el agente: este documento es el planteamiento de entrada. Dice qué se necesita y qué no se negocia; el cómo y el cuándo los pone el estándar. El agente sigue el flujo: análisis (02·F1) → alcance (proponer-alcance) → épica/HU (13·DOC15) → especificación (02·F2) → plan aprobado (02·F4) → implementación. No generar código hasta que el plan esté aprobado.
> "
> 00 ID9

**Agente** — 2026-08-22 11:43:17
<!-- agente: 1526080f-e12c-447c-b018-8efd5d7aa256 -->

Dice tres cosas, y ninguna es información nueva:

1. **Qué es este documento** — el planteamiento: recoge *qué* se necesita y *qué no se negocia*; el *cómo* y el *cuándo* no los pone el usuario, los pone el estándar.
2. **Por dónde tiene que pasar el agente** antes de tocar código — la cadena, con los IDs de cada eslabón.
3. **No hay código sin plan aprobado.**

El 2 y el 3 ya están escritos en el estándar: la cadena es [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) y la prohibición es [`02·F2`](base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) + [`02·F4`](base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md). Repetirlos acá es lo que rompe `00·ID9`: seis enlaces y una flecha larga para decir algo que el agente ya cargó al abrir la sesión.

Y peor que largo: **la cadena que copia no es la de `F0`**. `F0` dice `planteamiento → épica → HU → especificación → plan → código`. El encuadre dice `análisis → alcance → épica/HU → especificación → plan → implementación`. Dos versiones de la misma cadena en el mismo repo, y la copia es la que se desactualiza.

Lo único que aporta el párrafo es el punto 1 —qué papel juega este archivo—, y eso cabe en dos líneas:

> **Para el agente:** este documento dice *qué* se necesita y *qué no se negocia*. El *cómo* y el *cuándo* los pone el estándar: se recorre la cadena de [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) sin saltar eslabones.

¿Lo reemplazo por eso en [prompts/cimiento-planteamiento.md](prompts/cimiento-planteamiento.md)?

### 2 · Usuario — 2026-08-22 11:47:32
> si y qué diga que debe aplicar la regla 00 ID9

**Agente** — 2026-08-22 11:48:55
<!-- agente: e4aa86b5-2fcc-48c3-a093-86bdb92ae631 -->

Hecho. El encuadre de [prompts/cimiento-planteamiento.md](prompts/cimiento-planteamiento.md) quedó así:

> **Para el agente:** este documento dice **qué** se necesita y **qué no se negocia**. El **cómo** y el **cuándo** los pone el estándar: se recorre la cadena de `02·F0` sin saltar eslabones. Lo que se responda sobre este documento se escribe bajo `00·ID9`: la menor extensión con la que se entienda.

De paso revisé la plantilla: [plantillas/ciclo-vida-proyectos/01-planteamiento.md](plantillas/ciclo-vida-proyectos/01-planteamiento.md) **enlaza** `02·F0`, no copia la cadena. La cadena mal escrita se inventó al llenar el archivo, no la arrastra el molde — así que no hay nada que corregir allá.

El hallazgo quedó escrito en [historico-chat/resumenes/2026-08-22/sesion-3.md](historico-chat/resumenes/2026-08-22/sesion-3.md).

Dos cosas:

**Nombre de la sesión** — esta se está guardando como `2026-08-22-sesion-3.md`, que no dice de qué trata. Propongo `2026-08-22-el-encuadre-enlaza-la-cadena-no-la-copia.md` — el encuadre del planteamiento duplicaba la cadena de `02·F0` con una versión desactualizada; se reemplazó por el enlace. ¿Va? Si sí, lo corro y te paso la línea `/rename`.

**Commit** — no toqué git. ¿Commiteo estos cambios o los dejas para revisar?

### 3 · Usuario — 2026-08-22 14:46:44
> si

**Agente** — 2026-08-22 14:48:51
<!-- agente: ebf8c296-4cab-42fe-b431-7eff88063b9d -->

Listo.

**Sesión renombrada** a [2026-08-22-el-encuadre-enlaza-la-cadena-no-la-copia.md](historico-chat/2026-08-22-el-encuadre-enlaza-la-cadena-no-la-copia.md), con su resumen y los dos índices al día.

**Commiteado** en dos commits — `98e710c` (el encuadre + histórico) y `d356fca` (cierre del resumen). Sin `push`.

**Solo commiteé lo de esta sesión.** El árbol tiene bastante trabajo en curso de otras sesiones que dejé intacto: las once plantillas del ciclo, `validadores/plantillas.py` y sus pruebas, la HU-002 y la HU-012, y los pendientes 77 y 78 sin versionar. No es mío tocarlo.

Un detalle: el pendiente [77-el-planteamiento-conserva-su-encuadre.md](pendientes/hecho/el-planteamiento-conserva-su-encuadre.md) —de otra sesión— toca exactamente este archivo. Vale la pena mirar si lo que acabo de escribir choca con lo que ese pendiente quiere, antes de que la otra sesión avance.

Falta la línea que solo puedes correr tú, para que la pestaña y `/resume` muestren el mismo nombre:

```
/rename el-encuadre-enlaza-la-cadena-no-la-copia
```
