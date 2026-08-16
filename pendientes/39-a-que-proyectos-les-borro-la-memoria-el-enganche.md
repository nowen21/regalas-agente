# Pendiente · A qué proyectos les borró la memoria el enganche, y qué quedó sin recuperar

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-3 del [resumen del 2026-08-07](../historico-chat/resumenes/2026-08-07/memoria-del-agente-en-el-repo.md), que quedó abierto y sin mirar |
| **Dónde estaba antes** | Era el punto 6 del [33](33-defectos-que-destaparon-los-resumenes-viejos.md). Se promovió a pendiente propio el 2026-08-16 porque su urgencia no es la del archivo que lo contenía |
| **Proyecto de origen** | El estándar mismo. El defecto lo causó una pieza del estándar corriendo dentro de los proyectos |

## El problema

El 2026-08-07, `recuerdos.py` **borró memoria de proyectos**. El mecanismo construido para que la memoria no se pierda fue el que la destruyó: en un almacén enlazado con un junction de Windows, la migración comparaba el archivo del almacén con su gemelo del repositorio por la ruta escrita, y como eran el mismo archivo, el `os.remove` se llevaba el único ejemplar. Pasó dos veces en agro-system: al correr el instalador y otra vez sola, en el arranque siguiente.

**El código está corregido** desde la versión 3.1.1, y llega solo a todos los proyectos porque los enganches llaman al estándar por ruta absoluta.

**Lo que no está hecho es lo otro:** el arreglo no deshace el borrado anterior. Nadie revisó proyecto por proyecto cuál tenía el enganche puesto el 2026-08-07 ni en qué estado quedó su memoria. En agro-system se recuperó del último commit; de los demás no se sabe.

## Por qué es lo primero de todo el backlog

Es el único pendiente donde **se pierde información que no está en ninguna otra parte**. Todo lo demás de la lista es trabajo que espera; esto es una recuperación que caduca: lo que no se saque del commit no está en ningún lado, y cada commit nuevo encima lo entierra un poco más.

## Qué hay que hacer

**1 · Listar los proyectos que existían el 2026-08-07 y tenían el enganche.** El registro está en [`plantillas/proyectos.md`](../plantillas/proyectos.md). Los que se instalaron después no pueden estar afectados; la fecha de instalación de cada uno sale del historial de git de ese registro.

**2 · Por cada uno, mirar en qué estado quedó su memoria.** Dos preguntas: ¿tenía el almacén local enlazado con un junction —que es lo que dispara el defecto—, y falta hoy algún recuerdo que su historial de git sí tenga?

**3 · Recuperar lo que falte, del último commit anterior al borrado.** Es el mismo comando que se usó en agro-system.

**4 · Escribir el resultado por proyecto**, incluido «este no estaba afectado». Un proyecto sin revisar y uno revisado y sano se ven igual desde afuera, y esa es exactamente la razón por la que esto lleva nueve días sin hacerse.

## El límite

Lo que no esté commiteado no se recupera de ninguna parte, y eso hay que decirlo por escrito en el proyecto donde pase, no dejarlo como un hueco.

## Cómo se sabe que cerró

Cada proyecto del registro tiene escrito si estaba afectado y qué se recuperó. Ninguno queda en «no se sabe».
