# Resultado de Pruebas — Fase `B-EP-006-HU-004-degradar-sin-el-modelo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-006-HU-004-degradar-sin-el-modelo` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el defecto que la fase `A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado` dejó probado con fallo esperado quedó arreglado, y su prueba pasó a correr como cualquier otra.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la memoria en verde | 59 | **59** |
| Pruebas marcadas como fallo esperado | 0 | **0**, eran 5 |

---

## 3. Qué se arregló

**El más grave de los tres, porque rompía lo que no dependía de él.**

Saber si las librerías opcionales están puestas no es lo mismo que poder cargar el modelo: puede faltar el archivo, o no haber red la primera vez. Con las librerías instaladas y el modelo ausente, la búsqueda **se caía entera y se llevaba por delante la búsqueda por palabra**, que no necesita ni modelo ni red.

Esa es la promesa que la historia hace: que instalar lo semántico sea opcional **de verdad**. Una parte opcional que al fallar tumba la que no lo es, no es opcional.

| Antes | Ahora |
|---|---|
| Con el modelo ausente, la búsqueda entera se cae | Degrada a búsqueda por palabra |
| El error no se explicaba | El modo lo dice: «léxica (el modelo no se pudo cargar)» |

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
