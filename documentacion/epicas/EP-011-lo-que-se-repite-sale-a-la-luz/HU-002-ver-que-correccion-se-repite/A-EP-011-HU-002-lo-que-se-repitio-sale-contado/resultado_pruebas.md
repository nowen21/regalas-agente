# Resultado de Pruebas — Fase `A-EP-011-HU-002-lo-que-se-repitio-sale-contado`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-011-HU-002-lo-que-se-repitio-sale-contado` |
| **HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre lo indexado de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 6 |
| Ejecutados | 6 |
| Pasaron | 6 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **16** |

| | Cuánto |
|---|---|
| Mensajes del usuario que cuentan como corrección | **1 389** de 3 720 |
| Filas del reporte que no escribió una persona | **0** (eran 14 de las 14 primeras) |

---

## 2. Ejecución caso por caso

### CP-001 — Qué cuenta como corrección

| Entrada | Salió |
|---|---|
| «si», «Sí», «hágale», «listo», «OK», «siga» | no cuenta |
| «recuerde que todo va en español colombiano» | cuenta |
| «no eso» | no cuenta |
| Un bloque del editor, solo | no cuenta |
| Un bloque del editor más «levante el servidor» | cuenta solo la frase |

**Resultado: pasa.**

### CP-002 — Lo mismo dicho distinto cuenta como uno

**El criterio que la HU llama «lo difícil», y se probó con su caso real.** Sobre lo indexado de verdad:

```
  9  espanol colombiano    3 sesiones (2026-08-28, 2026-08-22, 2026-08-14)
```

Las formas que quedaron en esa fila son de tres días distintos, y ninguna se parece a la otra como texto:

```
adapte la plantilla del manual de instalación al español colombiano
recurede el español colombiano
pero español colombiano cómo sería no le olvide la regala
```

Y **no se agrupa en cadena**: dos correcciones sobre el manual de instalación salen en su propia fila, no metidas en la misma.

**Resultado: pasa.**

### CP-003 — Ordenado, con cuántas veces y dónde

```
 22  debe quedar                        14 sesión(es)
 21  meta reglas                         5 sesión(es)
 19  puede cerrar                       13 sesión(es)
 19  historico chat                     10 sesión(es)
 17  debe tener                         11 sesión(es)
 16  cada proyecto                      11 sesión(es)
```

Cada fila trae sus sesiones enlazadas por su ruta. **Resultado: pasa.**

### CP-004 — El período recorta

Pidiendo desde una fecha, lo de antes no sale. **Resultado: pasa.**

### CP-005 — Sin nada repetido se dice

Tres situaciones, tres respuestas distintas:

| Situación | Qué responde |
|---|---|
| Hubo correcciones y ninguna se repitió | «Nada se repitió en ese período» |
| No hay nada indexado | «Puede que no haya conversaciones indexadas todavía» |
| Una sesión de puras confirmaciones | Cero correcciones, y lo dice |

**Resultado: pasa.** Los dos silencios se distinguen, que es lo que impide leer «no encontré» como «no hay».

### CP-006 — Dos corridas dan la misma lista

**Resultado: pasa.** El orden está fijado por cuenta, por número de sesiones y por la frase.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las primeras catorce filas del reporte | Las escribió una persona. **Antes de sacar lo que pega el editor, ninguna** |
| El cierre del reporte | Dice que el patrón no es la regla, y que lo que amerite entra por la cadena |
| El caso real del `CA-03` | Las tres formas en una fila |

**El módulo solo lee.** No toca el índice ni el histórico.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | **La primera versión del reporte era ruido de la herramienta.** Las catorce primeras filas eran bloques que el editor le pega al mensaje: «this may», «current task», «the user», 139 veces cada una. Ninguna la escribió una persona | Crítica | Arreglado acá: lo que la herramienta pega no cuenta como dicho. Queda como `S-099` |

**Se vio corriéndolo sobre lo real, no leyendo el código.** Con datos inventados el reporte se habría visto perfecto: los bloques del editor no están en una conversación de mentiras.

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-002-ver-que-correccion-se-repite.md#ca-01--el-reporte-sale-por-período) | CP-003, CP-004 | **Cumple** |
| [CA-02](../HU-002-ver-que-correccion-se-repite.md#ca-02--cada-corrección-dice-cuántas-veces-y-dónde) | CP-003 | **Cumple** |
| [CA-03](../HU-002-ver-que-correccion-se-repite.md#ca-03--lo-mismo-dicho-distinto-cuenta-como-uno) | CP-002, con el caso real | **Cumple** |
| [CA-04](../HU-002-ver-que-correccion-se-repite.md#ca-04--sin-nada-repetido-se-dice) | CP-005 | **Cumple** |
| Transversal — no propone la regla | §3 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Qué cuenta como corrección, con su lista cerrada | Hecho, y la lista se lee en el código |
| Agrupar sin red y sin instalar nada | **Salió.** El riesgo `B-01` de la HU queda cerrado, no declarado como deuda |
| Contar, ordenar, recortar por período | Hecho |
| Separar los dos silencios | Hecho |
| El reporte corrido sobre lo real | Hecho, y su salida está arriba |
| Que no se lea como lista de tareas | El reporte cierra diciéndolo |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Los cuatro criterios y el transversal quedaron cumplidos, y el que la HU llamaba «lo difícil» se probó **con el caso real que ella misma nombra**, no con uno inventado.

**El riesgo que la historia daba por probable no se materializó:** agrupar salió sin instalar nada y sin salir a la red, así que no hay deuda que declarar por ahí.

**Lo que la fase no puede decir, y la HU lo pide:** si el reporte sirve. Eso se mide por lo que produzca — si de acá no nace ninguna regla, no sirvió. Es juicio del usuario, y queda abierto a propósito.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 16 pruebas del servicio | `plataforma/nucleo/medicion/tests_repeticion.py` |
| EV-02 | El reporte sobre lo indexado | §2, `CP-002` y `CP-003` |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
