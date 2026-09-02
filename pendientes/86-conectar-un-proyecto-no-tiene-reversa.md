# Pendiente · Conectar un proyecto no tiene reversa, y desconectar está decidido pero no pedido

> **Este pendiente es del producto, no del cuerpo de reglas.** Entra por acá porque es el camino que la etapa de análisis dejó escrito en su sección 11: un cambio a lo ya acordado se pide como pendiente, el agente dice a qué le pega, y el usuario aprueba.

**Estado:** **hecho** el 2026-09-02. Lo cerró `F-035`, construida el 2026-08-31: desconectar, reconectar, renombrar, corregir la ruta y corregir la versión declarada. Las cinco cosas que este pendiente pedía.

| | |
|---|---|
| **Historia de usuario** | [EP-008 · HU-004](../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md), cerrada el 2026-08-31 |
| **De dónde sale** | El usuario lo vio al mirar la primera pantalla, el 2026-08-25: *"pero eso no tiene administración?"* |
| **Proyecto de origen** | Cimiento, como producto |

## El problema

La especificación del módulo Proyectos, aprobada el 2026-08-25, dice dos cosas sobre desconectar:

- §7: *"Conectar y desconectar piden confirmación"*.
- §12, como decisión tomada: *"Desconectar no borra la documentación"*, contra la alternativa de borrarla, porque *"desconectar es reversible; borrar no"*.

**Está decidido cómo debe comportarse, y no hay ninguna funcionalidad que lo construya.** No existe `F-` ni `RF-` que lo pida, así que ninguna fase lo va a hacer. La especificación quedó prometiendo un comportamiento que el inventario nunca pidió.

Lo mismo pasa con renombrar un proyecto y con corregir la versión de reglas que declara.

**Lo que sí está cubierto**, y por eso no entra acá: corregir la ruta perdida es el `CA-3` de `F-002`, y lo construye la fase C.

## Por qué importa

**Conectar no tiene reversa.** Hoy, si el usuario escribe mal el nombre o apunta a la carpeta equivocada, el proyecto queda registrado así para siempre: no hay cómo quitarlo ni cómo corregirlo. La única salida es editar a mano el texto de la plataforma, que es exactamente lo que la plataforma vino a evitar.

Es más grave de lo que parece porque choca con la escala de riesgo del propio estándar: una acción que **no se deshace** exige aprobación de esa acción concreta. Conectar se comporta hoy como si no se deshiciera, cuando debería ser de las que se deshacen solas.

Y la plataforma se llama «administrar los proyectos desde un solo lugar». Mostrar y conectar no es administrar: administrar incluye deshacer.

## Qué falta

Una funcionalidad que administre un proyecto ya conectado. Tres cosas, y ninguna borra nada:

1. **Desconectar.** El proyecto sale de la lista y **su documentación se queda**. Ya está decidido así en la especificación; falta pedirlo.
2. **Renombrar.** El nombre cambia y la carpeta no se mueve. El código de la fase B ya guarda el identificador aparte del nombre justamente para esto, y hoy no hay dónde usarlo.
3. **Corregir la versión de reglas que declara.** Hoy solo se lee del `CLAUDE.md` del proyecto al conectar, y si allá cambia, la plataforma no se entera.

Las tres piden confirmación y las tres quedan en la auditoría, como cualquier otro cambio.

## El límite

Este pendiente **no** cubre:

- **Corregir la ruta perdida**, que es `F-002` `CA-3` y lo hace la fase C.
- **Borrar la documentación de un proyecto.** Desconectar no borra, y eso ya está decidido. Si algún día hace falta borrar, es otra discusión y otra funcionalidad.
- **Configurar qué reglas rigen en cada proyecto**, que es `F-004` y va en la versión 5.

## A qué le pega

| Documento | Qué cambia |
|---|---|
| [cvds/analisis-requisitos/README.md](../cvds/analisis-requisitos/README.md) | Un requisito funcional nuevo, y su fila en la trazabilidad |
| [cvds/analisis-requisitos/inventario-funcionalidades.md](../cvds/analisis-requisitos/inventario-funcionalidades.md) | Una ficha nueva, la tabla de resumen y la cuenta |
| [cvds/implementacion/README.md](../cvds/implementacion/README.md) | En qué versión entra, y su fase |
| [documentacion/proyectos/spec.md](../documentacion/proyectos/spec.md) | Su §1 dice qué está dentro del alcance y no nombra desconectar, aunque §7 y §12 sí lo tratan. Se corrige esa contradicción |
| [EP-008](../documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md) | Una historia de usuario nueva |

**Lo que no cambia:** la fase B, que se termina como está aprobada. Esto entra después.

## En qué versión debería entrar

**Propuesta: la versión 1**, y no más adelante.

La razón no es que sea cómodo: es que **hoy conectar no se puede deshacer**. Mientras eso siga así, cada proyecto que se conecte mal queda mal para siempre, y el arreglo es editar a mano lo que la plataforma administra. Postergarlo acumula errores que después hay que limpiar de otra forma.

Es lo contrario del caso del [85](85-las-conversaciones-completas-no-se-pueden-analizar.md), que sí se pudo postergar sin perder nada porque el texto ya estaba escrito y se puede indexar hacia atrás.

## Cómo se sabrá que cerró

Que el usuario pueda conectar un proyecto con el nombre equivocado, darse cuenta, y dejarlo como estaba antes: desconectado o con el nombre corregido, sin abrir un solo archivo a mano y sin que la documentación se pierda.
