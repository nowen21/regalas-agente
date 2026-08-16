# 2026-08-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-07-memoria-del-agente-en-el-repo.md](../../2026-08-07-memoria-del-agente-en-el-repo.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).

**Viene de:** 2026-08-06 · la anatomía de la regla · H-12. Lo cierra.

**Propósito:** que la memoria del agente quede en el repositorio del proyecto y no en el equipo.

---

## Hallazgos de esta sesión

### H-1 · La memoria del agente vivía donde nadie puede verla

- **Qué pasó:** el usuario lo pidió sin rodeos: nada debe quedar en `~/.claude/projects/<proyecto>/memory`; todo va a `historico-chat/memory/`. Y corrigió al agente cuando lo entendió al revés: *«es al contrario — se guarda en `historico-chat/memory` y allá solo se referencia»*.
- **Por qué importa:** lo local no se ve en git, no se revisa, no se versiona y no viaja a otra máquina. Y dos copias del mismo recuerdo terminan diciendo cosas distintas: la que manda es la que nadie puede leer.
- **Qué lo soluciona:** una regla que lo exija, un programa que recoja lo que aparezca en el almacén local, y que la instalación lo deje puesto en cada proyecto.
- **Qué se decidió:** nace [`01·C19`](../../../base/01-conducta.md), un archivo por recuerdo con su índice, y [`hook_recuerdos.py`](../../../validadores/hook_recuerdos.py) para moverlo solo. Versión **3.0.0**.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`01·C19`](../../../base/01-conducta.md) y la carpeta [historico-chat/memory/](../../memory/memory.md).
- **Nace en:** 2026-08-06 · la anatomía de la regla.
- **Cerrado en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Con qué se retoma:** —.

### H-2 · El enganche que cuidaba la memoria la borró

- **Qué pasó:** el usuario lo vio en su proyecto: *«mire lo que está pasando, me está borrando la memoria»*. En agro-system el almacén local era un **junction** —un enlace de Windows— hacia `historico-chat/memory/`. La migración comparaba el archivo del almacén con su gemelo del repositorio por la ruta escrita, y con el enlace **eran el mismo archivo**: la comparación daba siempre igual, y el `os.remove` borraba el único ejemplar. Pasó dos veces: primero al correr el instalador y después solo, en el arranque siguiente, disparado por el propio enganche que el instalador acababa de registrar.
- **Por qué importa:** es el peor defecto del histórico. El mecanismo construido para que la memoria **no** se pierda fue el que la destruyó, y lo hizo sin que nadie lo pidiera, con la sesión quieta. Se recuperó porque estaba commiteada.
- **Qué lo soluciona:** que un enganche que corre solo en cada arranque y en cada edición **no tenga permiso de destruir**.
- **Qué se decidió:** cuatro cambios en [`recuerdos.py`](../../../validadores/recuerdos.py) — se fue el `os.remove` y todo se **mueve**; si el nombre está ocupado entra como `<nombre>-local.md` y decide el usuario; el almacén enlazado pasa a ser una forma válida de cumplir `C19`, comparando por identidad en disco y no por el texto de la ruta; el instalador no toca la carpeta si ya está enlazada y con índice; y el índice se busca sin distinguir mayúsculas, para que el `MEMORY.md` de la herramienta no se sobrescriba. Verificado contra un junction de Windows real, no simulado. Versión **3.1.1**, marcada como pérdida de datos en el [CHANGELOG](../../../CHANGELOG.md).
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`recuerdos.py`](../../../validadores/recuerdos.py), versión 3.1.1 del [CHANGELOG](../../../CHANGELOG.md).
- **Nace en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Cerrado en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Con qué se retoma:** —.

### H-3 · El arreglo llega solo a los proyectos, pero nadie revisó en qué estado quedaron

- **Qué pasó:** el usuario preguntó dos veces, y la segunda cortó las salvedades: *«no me haga salvedades, ¿está o no?»*. La respuesta honesta fue: el código está corregido y los proyectos lo corren sin reinstalar nada, porque los enganches llaman al estándar por ruta absoluta. Pero **la memoria borrada no vuelve sola**, y el agente no revisó proyecto por proyecto cuál tiene el enganche ni cómo quedó su memoria.
- **Por qué importa:** que el arreglo se propague no significa que el daño esté deshecho. Son dos cosas y se responden por separado.
- **Qué lo soluciona:** recuperar del último commit en cada proyecto afectado, y revisar uno por uno.
- **Qué se decidió:** se dio el comando de recuperación. La revisión proyecto por proyecto **no se hizo** ese día; se hizo el 2026-08-16 y cerró el hallazgo.
- **Estado:** resuelto. La revisión dio que **ningún otro proyecto pudo estar afectado**: el defecto solo se dispara con el almacén enlazado por *junction*, y ninguna de las nueve carpetas `historico-chat/memory/` del registro ni ninguno de los 16 almacenes de `~/.claude/projects/*/memory/` lo está. `agro-system` —el que lo reportó y el único que lo tuvo— ya había restaurado los 75 archivos y sacado la memoria del junction, en su commit `6d4b130`.
- **Responde a:** —.
- **Dispara:** —, era revisar y correr un comando.
- **Orden de resolución:** 1 de 1.
- **Dónde queda:** [pendientes/hecho/memoria-borrada-por-el-enganche.md](../../../pendientes/hecho/memoria-borrada-por-el-enganche.md) — estuvo en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) hasta el 2026-08-16, cuando se promovió a pendiente propio y se cerró.
- **Nace en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Cerrado en:** 2026-08-16 · [qué pendientes trabajamos](../2026-08-16/que-pendientes-trabajamos.md).
- **Con qué se retoma:** —.

### H-4 · Las reglas de documentación tampoco cumplían el molde

- **Qué pasó:** el usuario preguntó si las reglas `DOC` ya cumplían el capítulo 20, y tuvo que insistir dos veces porque el agente respondía por otras. No cumplían. Y cuando el agente listó los defectos y esperó, el usuario cortó: *«¿y qué espera, que le diga que las corrija o qué? Corto y conciso»*.
- **Por qué importa:** es la misma lección de esa noche, dicha por segunda vez en el día: lo que el agente detecta como mal, lo arregla — no pregunta si lo arregla.
- **Qué lo soluciona:** corregirlas.
- **Qué se decidió:** se corrigieron.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [base/13-documentacion](../../../base/13-documentacion/base.md), y la memoria [corregir el defecto que uno mismo detecta](../../memory/corregir-el-defecto-que-uno-mismo-detecta.md).
- **Nace en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Cerrado en:** 2026-08-07 · la memoria del agente en el repositorio.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, H-2 y H-4 |
| Todo hallazgo abierto tiene su pendiente creado | ☑ H-3 en el [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ subido; el usuario pidió no mezclar lo de otras sesiones |
