# Pendiente · El registro de versión no se escribe si no cambió ninguna huella

**Estado:** **cerrado** el 2026-08-16 (v21.2.0), junto con el [42](el-arreglo-del-40-no-llegaba-a-lo-ya-instalado.md), porque son el mismo defecto. Qué se hizo: [`hecho/poner-al-dia-lo-ya-instalado.md`](poner-al-dia-lo-ya-instalado.md). La fase que lo cerró: [`A-EP-007-HU-006`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado). Anotado el 2026-08-16.

> El archivo se queda acá y no se mueve a `hecho/`: moverlo rompería los enlaces que lo citan, que es exactamente el [pendiente 54](../54-cerrar-un-pendiente-rompe-sus-citas.md). Decía «abierto» hasta el 2026-08-17, cuando `validar.py estandar` destapó que el índice y el archivo se contradecían.

| | |
|---|---|
| **Proyecto de origen** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | [`pendientes/hecho/06-el-checklist-se-queda-en-12-de-13.md`](../../../../../DesarrollosClaude/personales/shopnest-mesa/pendientes/hecho/06-el-checklist-se-queda-en-12-de-13.md) — **ya cerrado allá**: `shopnest-mesa` lo pasó a `hecho/` cuando comprobó el arreglo |
| **A quién avisar al cerrar** | a **todos los proyectos instalados** — le pasa a cualquiera que se quede una versión atrás sin que cambien sus plantillas. La lista está en [`plantillas/proyectos.md`](../../plantillas/proyectos.md) |

## El problema

El componente `versiones` del checklist reprueba cuando la versión instalada no coincide con el último registro de `documentacion/versiones/`. El instalador es quien escribe ese registro, y lo escribe **solo si alguna huella cambió**.

Cuando el estándar sube de versión sin que cambie ninguna plantilla del proyecto, las dos condiciones se contradicen:

```
· versiones: nada cambió, no hay actualización que registrar

  INSTALACIÓN INCOMPLETA · shopnest-mesa · 12 de 13 · falta: versiones

  - **versiones** — lo instalado dice `21.1.0` y el último registro dice `20.0.1`
    Se arregla así: Escribe un registro cada vez que algo cambia de huella.
```

El instalador dice que no hay nada que registrar, y el checklist dice que falta el registro. **Corriendo el instalador otra vez sale exactamente lo mismo**: no hay salida.

## Por qué importa

Tres cosas, y la tercera es la que hace daño:

1. **El proyecto queda en 12 de 13 para siempre.** Nada de lo que el instalador sabe hacer lo sube.
2. **La única salida es escribir el archivo a mano**, y esos archivos terminan diciendo *«Lo escribió `validadores/instalar.py`. No se edita a mano.»* La salida disponible es la que el propio estándar prohíbe.
3. **El aviso de instalación incompleta se vuelve permanente.** El agente lo repite en cada mensaje, y un aviso que siempre suena se deja de leer — con él se pierden las incompletitudes de verdad. Es el mismo daño del [pendiente 34](enlaces-de-las-plantillas-al-estandar.md), por otra puerta.

Además, el mensaje de ayuda es engañoso: *«Escribe un registro cada vez que algo cambia de huella»* describe lo que el instalador **ya hizo** y no arregla nada. Quien lo lea vuelve a correr el instalador y vuelve al mismo sitio.

## Cómo se reproduce

En `shopnest-mesa`, el 2026-08-16:

1. El estándar pasó de `20.0.1` a `21.1.0` sin tocar ninguna plantilla que el proyecto herede.
2. Se corrió el instalador. Todo salió `ya estaba al día`, salvo `versiones`.
3. Se volvió a correr. Idéntico.
4. El estándar subió a `21.1.1` y se corrió una tercera vez. Idéntico, y **el desfase creció**: el último registro sigue diciendo `20.0.1`.

**El hueco se ensancha solo.** Cada publicación del estándar que no toque las plantillas de un proyecto le suma una versión de atraso al registro, sin que exista forma de ponerlo al día.

## Qué falta

Decidir cuál de estas dos es la buena, que son incompatibles:

**A · Que suba de versión sea por sí solo motivo de registro.** El instalador escribe el registro con la lista de componentes vacía y una línea que diga *«subió la versión del estándar; ningún componente de este proyecto cambió»*. Es honesto y deja el rastro completo de bajo qué versión cerró cada fase, que es para lo que existe la carpeta.

**B · Que `versiones` no reprueba si no hubo nada que registrar.** El checklist compara contra la última versión **que trajo cambios**, no contra la instalada. Más barato, pero deja un hueco: mirando `documentacion/versiones/` no se puede saber desde cuándo el proyecto usa la versión que usa.

**La A parece la buena**, porque es justamente lo que la carpeta promete —*«un registro por actualización, con desde cuándo este proyecto usa cada versión»*— y la B rompe esa promesa. Pero es decisión del estándar, no del proyecto que reporta.

Y en cualquiera de las dos: **corregir el texto de ayuda**, que hoy manda hacer lo que ya se hizo.

## Cómo se sabe que cerró

Un proyecto al que le sube la versión del estándar sin cambiarle ninguna plantilla llega a 13 de 13 corriendo el instalador, sin que nadie edite nada a mano.
