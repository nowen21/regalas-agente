# 2026-08-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-08-la-documentacion-de-los-validadores.md](../../2026-08-08-la-documentacion-de-los-validadores.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-16.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)).
>
> Empezó el 2026-08-08 a las 22:42 y terminó el 2026-08-09 a las 22:33. El resumen queda en el día en que empezó.

**Viene de:** —, es trabajo nuevo.

**Propósito:** poder entender qué hace cada archivo de `validadores/` sin abrir el código.

---

## Hallazgos de esta sesión

### H-1 · Treinta y siete programas y ninguna forma de saber qué hace cada uno

- **Qué pasó:** el usuario pidió la documentación técnica de cada archivo de `validadores/`, sacada **del código fuente** y no de suposiciones ni de documentación previa.
- **Por qué importa:** los validadores son la mitad del agente que corre sin IA. Sin saber qué hace cada uno, la única forma de tocarlos es leerlos enteros.
- **Qué lo soluciona:** un documento por archivo, todos con la misma estructura: qué hace, de qué depende y quién lo usa, qué tiene adentro, y cómo se ejecuta.
- **Qué se decidió:** 40 documentos en [validadores/docs/](../../../validadores/docs/README.md), más el índice, que agrupa por lo que hacen y trae el mapa de relaciones en dos formas: los cinco niveles —cada nivel solo usa los de arriba— y la tabla completa de «usa a / lo usan».
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [validadores/docs/](../../../validadores/docs/README.md), commit `bc22f21`.
- **Nace en:** 2026-08-08 · la documentación de los validadores.
- **Cerrado en:** 2026-08-08 · la documentación de los validadores.
- **Con qué se retoma:** —.

### H-2 · «Solo lo que se le pide, y sin tanto tecnicismo»

- **Qué pasó:** el usuario cortó a los tres documentos: *«en la documentación solo coloque lo que se le pide, no me interesa saber qué no hace, y si considera que se debe agregar hágalo en los pendientes. Necesito entender qué hace cada archivo en lenguaje claro»*.
- **Por qué importa:** son dos instrucciones en una, y las dos se siguen aplicando. La documentación describe **lo que hay**, no lo que falta; y lo que el agente cree que falta va al backlog, no al documento.
- **Qué lo soluciona:** rehacer lo escrito con ese criterio.
- **Qué se decidió:** se rehicieron los tres y siguió con el resto. Después el usuario afinó el vocabulario: «devuelve» pasó a «retorna» en los 40 documentos —256 reemplazos— y se agregó al final de cada uno la sección **«Ejemplos de lo que retorna»**, con valores reales sacados del código y también los casos borde, que es donde uno se traba.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** las memorias de [estilo de redacción simple](../../memory/estilo-redaccion-simple.md) y [manuales claros](../../memory/manuales-claros.md).
- **Nace en:** 2026-08-08 · la documentación de los validadores.
- **Cerrado en:** 2026-08-08 · la documentación de los validadores.
- **Con qué se retoma:** —.

### H-3 · Documentar destapó tres cosas del código que no estaban dichas

- **Qué pasó:** al leer los 37 archivos aparecieron tres hechos que ningún documento recogía: [`instalar.py`](../../../validadores/instalar.py) importa a cuatro módulos **dentro de las funciones** y no al comienzo, porque tres de ellos lo importan a él; `recuerdos.py` e `historico.py` son los únicos que no dependen de nada del paquete; y `codigo.py` es la base de seis validadores, pero `esquema.py` lo usa solo por una función de una línea.
- **Por qué importa:** el primero es una dependencia circular resuelta a mano. Quien mueva ese import al encabezado rompe el paquete y no va a entender por qué.
- **Qué lo soluciona:** que quede escrito donde se busca.
- **Qué se decidió:** quedó en el documento de cada archivo.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [validadores/docs/](../../../validadores/docs/README.md).
- **Nace en:** 2026-08-08 · la documentación de los validadores.
- **Cerrado en:** 2026-08-08 · la documentación de los validadores.
- **Con qué se retoma:** —.

### H-4 · GitHub bloqueó el push por una clave de ejemplo con forma real

- **Qué pasó:** al subir, GitHub rechazó el envío: en un documento había una clave de Stripe escrita con la forma real de una clave de verdad, como ejemplo.
- **Por qué importa:** una clave de mentira con forma real se comporta como una de verdad ante cualquier detector. Y si entra al historial, quitarla del archivo ya no basta.
- **Qué lo soluciona:** escribir los ejemplos con la forma cortada, y rehacer el commit antes de subirlo para que no quede en el historial.
- **Qué se decidió:** se cambiaron las de Stripe, AWS y GitHub, y se rehízo el commit.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [fixtures sin secretos literales](../../memory/fixtures-sin-secretos-literales.md), que ya existía y esto confirmó.
- **Nace en:** 2026-08-08 · la documentación de los validadores.
- **Cerrado en:** 2026-08-08 · la documentación de los validadores.
- **Con qué se retoma:** —.

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los cuatro |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ commit `bc22f21`, 42 archivos, sin `VERSION` ni `CHANGELOG` porque no toca `base/` ni `plantillas/` |
