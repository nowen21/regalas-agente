# Funcionalidad implementada — Fase `A-EP-011-HU-002-lo-que-se-repitio-sale-contado` (módulo Medición)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-011-HU-002-lo-que-se-repitio-sale-contado` |
| **Épica / HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md](../../epica.md) · [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) |
| **Módulo** | Medición |
| **Fecha de cierre** | 2026-08-31 |

---

## 1. Qué se implementó — resumen

**Lo que el usuario tuvo que repetir sale contado**, de lo más repetido a lo menos, con cuántas veces y en qué sesiones. Sobre lo indexado de este repositorio: **1 389 correcciones**, y en la cima cosas que se pidieron veintidós, veintiuna y diecinueve veces.

**Lo mismo dicho de tres maneras sale como una fila.** Es lo que la historia llamaba «lo difícil», y salió **contando frases compartidas**: sin instalar nada y sin salir a la red.

Y el reporte cierra diciendo lo que es: **el patrón, no la regla**. Lo que amerite regla entra por la cadena de siempre.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Se miran los mensajes del usuario» (§6) | servicio | `correcciones` en [plataforma/nucleo/medicion/repeticion.py](../../../../../plataforma/nucleo/medicion/repeticion.py) | ✅ | CP-001 |
| «Se agrupan los que dicen lo mismo» (§6) | servicio | `frases_de` | ✅ | CP-002 |
| «Los más repetidos, con cuántas veces y en qué sesiones» (§6) | servicio | `correcciones` | ✅ | CP-003 |
| «Si no hay nada repetido, se dice» (§6) | servicio | `cuantas_correcciones` y la orden | ✅ | CP-005 |
| «`RN-1` mostrar el patrón, nunca decidir la regla» (§4) | orden | La línea de cierre del reporte | ✅ | §3 del resultado |
| «`RN-6` qué cuenta como corrección» (§4) | servicio | `es_correccion` y `CONFIRMACIONES` | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | Qué cuenta, y cómo se agrupa |
| T-03 · T-04 | El conteo por período, y los dos silencios |
| T-05 | `correcciones_que_se_repiten` |
| T-06 · T-07 | 16 pruebas, y la corrida sobre lo real |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/medicion/` | 38 pruebas, en verde |
| El caso real del `CA-03` | Las tres formas, una fila |
| Las dos baterías del repositorio | En verde |

**Lo que las pruebas no dicen:** si el reporte sirve. La historia lo mide por lo que produzca — si de acá no nace ninguna regla, no sirvió. Eso lo juzga el usuario.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py correcciones_que_se_repiten
python manage.py correcciones_que_se_repiten --desde 2026-08-01 --limite 20
```

Antes hay que tener indexado lo conversado, que lo hace `indexar_conversaciones`.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Todo mensaje del usuario cuenta, menos una lista cerrada** | Ningún programa lee intención. Lo que sí puede es no contar «si» ni «hágale», que son la mitad de lo que se escribe |
| **Se agrupa por frase compartida** | Dos correcciones que dicen lo mismo se parecen poco como textos; lo que comparten es la frase |
| **No se agrupa en cadena** | Basta una cadena larga para que el reporte diga que todo es lo mismo |
| **Lo que la herramienta pega al mensaje no cuenta** | Se midió: sin sacarlo, las catorce primeras filas eran ruido del editor |
| El reporte cierra diciendo que no es la regla | Una lista ordenada se lee como una lista de tareas |

Señal registrada: [`S-099`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **Sin pantalla**, como la fase anterior. Llega cuando la vista de un proyecto la pida.
- **La lista de confirmaciones y la de palabras vacías están escritas en el código.** Son cortas y se leen; el día que haya que ajustarlas por otro idioma, salen a un archivo del proyecto.
- **`F-032` ya tiene la fuente que le faltaba:** decía que recibe cuántas correcciones se repiten, y hasta hoy nada las contaba.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/medicion/spec.md](../../../../medicion/spec.md) | La `RN-6`, su registro en la §15, y la fase en la §13 |
| [documentacion/senales.md](../../../../senales.md) | `S-099` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

Nada que desplegar y **ninguna migración**: el módulo solo lee lo que la fase anterior dejó indexado.
