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

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ no quedó ninguno abierto |
| Toda historia disparada está escrita en su épica | ☑ no disparó ninguna |
| Lo que se hizo está aprobado y guardado | ☐ falta la aprobación del usuario y el commit |

**Todavía no se cierra:** falta guardar, y falta lo que la sesión vino a hacer, que es construir `F-014`.
