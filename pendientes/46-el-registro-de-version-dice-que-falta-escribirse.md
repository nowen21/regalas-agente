# Pendiente · El registro de versión dice que falta escribirse

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **Historia de usuario** | [EP-007 · HU-006 — Poner al día](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/HU-006-poner-al-dia.md) — el registro mal escrito lo escribe esa historia; es su residuo |
| **Proyecto de origen** | **`dp`** (RNI Defensoría) · `C:/DesarrollosClaude/dp` |
| **Su pendiente de seguimiento** | [`documentacion/pendientes/24-el-registro-de-version-se-contradice.md`](../../../../DesarrollosClaude/dp/documentacion/pendientes/24-el-registro-de-version-se-contradice.md) — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a **`dp`**, que lo reportó. No hace falta avisar a los demás: el archivo mal escrito no rompe nada, solo confunde a quien lo lea |
| **Nace de cerrar** | el [44](hecho/poner-al-dia-lo-ya-instalado.md) (v21.2.0). Es el residuo de esa corrección, no su reapertura |

## El problema

Desde el [44](hecho/poner-al-dia-lo-ya-instalado.md), subir de versión es por sí solo motivo de registro: el instalador escribe `documentacion/versiones/<fecha>-<version>.md` y el proyecto llega a 13 de 13. Funciona.

Lo que quedó mal es el contenido de ese archivo. Su apartado **«Qué quedó pendiente»** se calcula **antes** de escribirlo y no se recalcula después, así que el registro recién nacido se lista a sí mismo como faltante:

```
## Qué quedó pendiente

Esto no lo aplica el instalador — es decisión del usuario:

- **versiones** — lo instalado dice `21.2.1` y el último registro dice `20.0.1`:
  falta registrar la actualización
```

El registro que «falta» es el archivo que uno está leyendo.

## Por qué importa

No bloquea nada: la instalación queda en 13 de 13 y una corrida en seco lo confirma. El daño es otro, y es de los que tardan meses en cobrarse.

1. **Queda versionado un documento que afirma algo falso.** La carpeta `documentacion/versiones/` existe para poder decir, dentro de un año, bajo qué versión del estándar cerró cada fase. Que su propio registro diga que no existe es exactamente lo contrario de lo que la carpeta promete.
2. **Manda a buscar lo que se tiene delante.** Quien lo lea sin contexto va a ir a `documentacion/versiones/` a escribir un registro que ya está ahí, o va a correr el instalador otra vez esperando que lo arregle. No lo arregla: en la segunda corrida no hay nada que registrar, así que el archivo malo se queda como está.
3. **Enseña a desconfiar del apartado.** «Qué quedó pendiente» es la única parte del registro que el usuario tiene que leer y actuar. Si la primera vez que la lee dice una cosa que no es, la segunda no la lee.

## Cómo se reproduce

En `dp`, el 2026-08-16:

1. El proyecto estaba en 12 de 13; faltaba `stack-instalacion`, porque el estándar había cambiado esa pieza (`ed454ca0ae7d` → `8b04fd87e6f3`).
2. Se corrió `instalar.py --aplicar`. Copió la pieza, escribió `documentacion/versiones/2026-08-16-21.2.1.md` y reportó **13 de 13**.
3. Ese archivo trae en «Qué quedó pendiente» la línea de `versiones` citando `20.0.1` como último registro, que era cierto un instante antes de escribirse.
4. Una corrida en seco posterior sale limpia. El archivo no se vuelve a tocar, así que la línea falsa se queda ahí para siempre.

**Se repitió el mismo día.** A las 22:03 el estándar subió de la `21.2.1` a la `23.2.0` y se corrió el
instalador otra vez. El registro nuevo, `2026-08-16-23.2.0.md`, trae la misma línea: «lo instalado
dice `23.2.0` y el último registro dice `21.2.1`: falta registrar la actualización». Dos de dos: no
es una condición de carrera, es el orden en que está escrito el instalador.

## Qué falta

Recalcular la lista de faltantes **después** de escribir el registro, y no antes. Dicho de otro modo: el componente `versiones` no puede evaluarse contra el estado previo cuando el propio instalador va a cambiarlo en la misma pasada.

Dos formas, y la primera parece la buena:

**A · Recalcular al final.** El instalador aplica todo, escribe el registro y recién entonces corre la comprobación que alimenta «Qué quedó pendiente». Es lo que el usuario cree que está leyendo, y de paso arregla cualquier otro componente que el instalador toque en la misma corrida y hoy aparezca listado como faltante.

**B · Excluir `versiones` de la lista cuando el registro se acaba de escribir.** Más barato y más estrecho: tapa este caso y deja abierto el mismo defecto para el próximo componente que el instalador aprenda a arreglar solo.

La **A** es la que corresponde, porque el problema no es de `versiones`: es que la foto se toma antes de terminar el trabajo.

## Cómo se sabe que cerró

Se corre el instalador en un proyecto al que le falte algún componente. El registro de versión que escriba tiene el apartado «Qué quedó pendiente» vacío, o solo con lo que de verdad exige una decisión del usuario, y ninguna línea que se refiera a sí mismo.

## Nota aparte, del mismo hallazgo

El archivo [`44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md`](44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md) sigue en esta carpeta con **Estado: abierto**, aunque el [README](README.md) lo da por cerrado el 2026-08-16 (v21.2.0) y su cierre está en [`hecho/poner-al-dia-lo-ya-instalado.md`](hecho/poner-al-dia-lo-ya-instalado.md). El README de esta carpeta dice que al cerrar un pendiente su archivo se borra o se marca con la fecha, y acá no pasó ninguna de las dos. Se anota acá y no en un pendiente aparte porque es una línea de arreglo, no un tema.
