# 2026-09-01 · El orden de las versiones  ·  `[CAPA 3]`

Lo que dejó esta sesión. La conversación literal vive en la transcripción; acá va lo que hay que poder encontrar sin releerla.

---

## De dónde viene esta sesión

**Viene de:** nada, es trabajo nuevo. Se abrió para construir `F-014`, la última funcionalidad obligatoria de la versión 2, y no llegó a construirse: el plan que la ordena resultó estar mal leído.

---

## Hallazgos de esta sesión

### H-1 · La columna «Depende de» se estaba leyendo como orden de construcción

- **Qué pasó:** al abrir `F-014` —versión 2— apareció que su ficha dice **Depende de F-011**, que está en la versión 5. Se propuso intercambiarlas de versión y se hizo. **Al contar después, los pares fuera de orden pasaron de dos a tres:** `F-014` arrastra a `F-015` y a `F-025`. El movimiento se deshizo entero y el reparto quedó como estaba.
- **Por qué importa:** el recorrido completo de las 35 fichas mostró que la columna no dice lo que se le estaba pidiendo. **`F-027`, de la versión 1, y `F-025`, de la versión 2, están cerradas, construidas y funcionando sin su dependencia**, porque la importación trae los documentos y las fases ya escritos. Quien lea esa columna como orden de trabajo reordena un plan que no estaba mal, y de paso cree bloqueado lo que no lo está: `F-014` se puede construir hoy.
- **Qué lo soluciona:** el inventario ahora explica qué dice la columna y qué no, con las dos funcionalidades cerradas como prueba; y el plan de implementación dice por qué ninguna versión se movió, con una tabla de cambios a la línea base. No dispara historia: es un defecto de dos documentos, no una capacidad que falte.
- **Qué se decidió:** **`F-014` se queda en la versión 2 y se construye sobre lo importado.** El desorden aparente se arregla en la columna, que es donde estaba el error.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-103` · [cvds/analisis-requisitos/inventario-funcionalidades.md](../../../cvds/analisis-requisitos/inventario-funcionalidades.md) · [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) §2
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-2 · Una convención de marcado que usa los signos de la prosa no se puede contar

- **Qué pasó:** el módulo iba a contar dos clases de espacio por llenar: `«…»` y el que trae nombre, como `«RESPONSABLE»`. **Se midió antes de construir** sobre las 130 historias de usuario reales: 341 marcas, 75 también en el molde, y **cero** todavía en la línea del molde. Ninguna era un hueco.
- **Por qué importa:** acá se cita con esas mismas comillas todo el tiempo, así que una marca con nombre no se distingue de una cita. Contarlas habría dado por incompleto **todo documento bien escrito**, que es el mismo error que una vez dio 559 documentos incompletos donde había 31. Y no se habría visto en las pruebas: con documentos inventados el conteo se ve perfecto.
- **Qué lo soluciona:** ya construido. El módulo cuenta solo el anónimo y lista el de nombre aparte, porque cuando `F-011` cree documentos desde el molde sí van a ser ciertos.
- **Qué se decidió:** **dos listas**, decidido por el usuario el 2026-09-01. La cuenta manda sobre los ciertos.
- **Estado:** resuelto acá
- **Responde a:** EP-013 · HU-001 · CA-03
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-104` · [documentacion/ciclo-de-vida/spec.md](../../../documentacion/ciclo-de-vida/spec.md) §5.1 · `plataforma/nucleo/ciclo_de_vida/huecos.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-3 · 24 documentos con espacios por llenar que el expediente nunca mostró

- **Qué pasó:** al comparar la cuenta nueva con la del módulo Expediente salieron **54 contra 31**. Los 24 de diferencia **son todos índices**, y un índice no entra al expediente. El uno que va al revés es una marca dentro de un bloque cercado, donde se escribe para mostrarla.
- **Por qué importa:** el expediente se usa para decidir si un proyecto está listo para entregar, y venía diciendo 31 cuando eran 54. No estaba mal: estaba respondiendo otra pregunta. Pero quien lea 31 y crea que es todo lo que falta, se equivoca.
- **Qué lo soluciona:** llenar esos 24 es trabajo de la `HU-002`, que ya está escrita y aprobada. No hace falta pieza nueva.
- **Qué se decidió:** las dos cuentas se quedan, cada una con su alcance dicho. La del expediente cuenta lo que se entrega; la del ciclo, todo lo traído.
- **Estado:** resuelto acá
- **Responde a:** EP-013 · HU-001 · CA-02
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la §3 del [resultado de pruebas](../../../documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/A-EP-013-HU-001-los-huecos-de-un-documento-se-ven/resultado_pruebas.md)
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ no quedó ninguno abierto |
| Toda historia disparada está escrita en su épica | ☑ no disparó ninguna |
| Lo que se hizo está aprobado y guardado | ☐ falta el commit de `EP-013` |

**Todavía no se cierra:** falta guardar. Lo que la sesión vino a hacer avanzó: `EP-013` nació, sus dos historias quedaron aprobadas, el módulo Ciclo de vida tiene especificación, y su primera fase cerró con **Cumple**. Queda la `HU-002`, que es la que escribe.
