# Resultado de Pruebas — Fase `B-EP-006-HU-007-marcar-deja-fecha-y-referencia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-006-HU-007-marcar-deja-fecha-y-referencia` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el defecto que la fase `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` dejó probado con fallo esperado quedó arreglado, y su prueba pasó a correr como cualquier otra.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la memoria en verde | 59 | **59** |
| Pruebas marcadas como fallo esperado | 0 | **0**, eran 5 |

---

## 3. Qué se arregló

**Lo que decía la consola se perdía al cerrarla.**

Marcar una señal como reemplazada imprimía «S-001 marcada reemplazada por S-002» y **no guardaba ni por cuál ni cuándo**. Archivar tampoco dejaba fecha. De una señal marcada no se sabía nada de lo que la marca prometía.

Se notó usándolo: esta misma sesión marcó una señal de terminología como reemplazada y tuvo que rodear el defecto escribiendo la nueva con el enlace puesto a mano.

**Y apareció un tercer defecto, en la propia prueba.** La que comprueba que la marca de vigencia no dependa del huso usaba 181 días como si fueran seis meses, cuando el contador va por meses de calendario: fallaba o pasaba según el mes en que se corriera. Ahora cuenta seis meses de calendario.

| Antes | Ahora |
|---|---|
| Marcar no guardaba por cuál ni cuándo | Guarda las dos cosas |
| Archivar no dejaba fecha | La deja |
| Una prueba pasaba o fallaba según el mes | Cuenta meses de calendario |

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El fallo esperado se destapa, no se borra

La fase `A` no podía arreglar esto: su plan declaraba que no se tocaba el programa (`02·F8`). Dejó el defecto **probado y marcado como fallo esperado**, que es la forma de que no se pierda: el día que se arregle, la prueba pasa a «éxito inesperado» y obliga a volver.

Es exactamente lo que ocurrió acá: al arreglar, la corrida reportó éxitos inesperados y hubo que volver a destaparlas una por una.

### 4.2 La corrida completa

```
Ran 59 tests in 5.7s
OK
```

Sin un solo fallo esperado en el archivo, donde había cinco.

---

## 5. Defectos encontrados

**Ninguno nuevo.**

---

## 6. Evidencias

- `memoria/memoria.py` y `memoria/semantica.py`
- `memoria/pruebas.py`, con las pruebas destapadas
