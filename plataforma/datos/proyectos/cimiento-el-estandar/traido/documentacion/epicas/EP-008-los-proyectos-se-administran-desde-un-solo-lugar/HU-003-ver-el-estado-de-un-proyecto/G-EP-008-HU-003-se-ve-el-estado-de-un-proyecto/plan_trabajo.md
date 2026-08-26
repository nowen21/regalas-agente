# Plan de Trabajo — Fase G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto` |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../../epica.md) |
| **HU** | [HU-003 Ver el estado de un proyecto](../HU-003-ver-el-estado-de-un-proyecto.md), una sola |
| **Módulo** | Proyectos |
| **Especificación** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), §6 |
| **Versión del producto** | 1, fase G de ocho |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que el usuario sepa en qué va cualquiera de sus proyectos sin entrar a su carpeta.

**Qué entra.** Calcular el estado desde lo que la plataforma tiene traído: qué etapas del ciclo tienen documento, qué fases están abiertas, y qué está aprobado y desde cuándo. Y **corregir un hueco de la fase E**, explicado abajo.

**Qué no entra.** Abrir un documento traído para leerlo, que es de la versión 2. Cambiar el estado desde la plataforma, que es de la versión 5.

## 2. Análisis previo: línea base verificada

**Se midió antes de planear, y salieron dos problemas.** Es la misma disciplina de la fase E, y esta vez lo que encontró no era una oportunidad sino dos defectos.

### El primero: las etapas del ciclo no se traen, y `CA-01` las pide

`CA-01` exige ver **qué etapas tienen documento**. Las siete etapas del ciclo de vida de este proyecto viven en `cvds/`, y la fase E recorre solo `documentacion/`. Peor: `cvds/` **ni siquiera aparece en la lista de carpetas que se declaran como no miradas**, así que se estaba saltando **en silencio**, que es justo lo que `RN-4` prohíbe.

**No es un defecto del alcance de la fase E: es un defecto de la fase E.** Su plan decía que recorría «la documentación del ciclo de vida», y las etapas del ciclo son documentación del ciclo. Se descubrió acá porque esta fase es la primera que necesita leerlas.

**Qué se decidió.** El usuario eligió el 2026-08-25 que `cvds/` **entre a lo que se trae**. Las etapas del ciclo son justo lo que la plataforma vino a administrar; que estén fuera de `documentacion/` es una peculiaridad de cómo está armado este repositorio, no una razón para ignorarlas.

**Qué hay en `cvds/`**, contado: 16 archivos. Siete son el documento de cada etapa, y el resto son sus documentos propios, todos con molde en el estándar:

| Archivo | Qué es |
|---|---|
| `planificacion/README.md` y los otros seis | El documento de cada etapa del ciclo |
| `analisis-requisitos/inventario-funcionalidades.md` | El inventario |
| `planificacion/estudio-factibilidad.md`, `acta-de-constitucion.md` | Los de planificación |
| `diseno/modelo-de-datos.md`, `decisiones-de-arquitectura.md`, `diseno-de-interfaz.md`, `contrato-de-la-interfaz.md` | Los de diseño |
| `cvds/README.md`, `cvds/cumplimiento.md` | El índice, y uno que habrá que ver si tiene molde |

### El segundo: la estación de una fase se escribe de doce formas

Contando los 125 `estado-fase.md` del repositorio, la línea que dice en qué estación va aparece así:

```
38  "9 · commit único"          6  "8, cierre documental"
17  "8 · cierre documental"     6  "12, commit"
13  "11 · cierre documental"    6  "cerrada"
 7  "6 · ejecución continua"    3  "10 · reporte al usuario"
 7  "4 · pausa y presentación"  5  (no se pudo leer)
```

Hay estaciones 10, 11 y 12, de un ciclo más largo que el de nueve. Y cinco que no se dejan leer.

**Qué se decidió.** No se adivina. Se lee el número inicial cuando está, y cuando no, **el estado dice «no se pudo leer»** con la ruta del archivo. Cinco fases ilegibles son un dato que el usuario puede corregir; un estado inventado es una afirmación sobre lo que no se leyó (`04·R4`).

### Lo demás que se midió

**215 de 975 documentos traen marca de aprobación.** El resto no, y es lo normal: no todo documento se aprueba. `CA-03` pide distinguir lo aprobado de lo que no, y con esa marca alcanza.

### 2.1 Archivos que se crean o modifican

`plataforma/nucleo/proyectos/` y sus plantillas, para calcular y mostrar el estado.

**Y `plataforma/nucleo/importacion/moldes.py`**, para corregir el hueco de la fase E: agregar `cvds/` a lo que se recorre, y los moldes de sus documentos. Queda declarado acá porque es de otro módulo, y en el cierre se anota como defecto de una fase ya cerrada.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| El estado se calcula al pedirlo, y no se guarda | Guardarlo y actualizarlo | El modelo de datos lo dice: un estado guardado a mano envejece y miente |
| Se calcula desde lo **traído**, no leyendo la carpeta del proyecto | Ir a leer el proyecto cada vez | `CA-01` dice «sin abrir su carpeta». Y leer mil archivos ajenos en cada pantalla rompería `RNF-02` |
| `cvds/` entra a lo que se trae | Declararlo como carpeta que no se mira | Decidido por el usuario el 2026-08-25: las etapas del ciclo son lo que la plataforma vino a administrar |
| Una estación que no se puede leer se dice, con su ruta | Suponer que está cerrada, o dejarla fuera | Suponer es afirmar sobre lo que no se leyó. Y dejarla fuera la esconde |
| Lo aprobado se dice **con palabras**, no con color | Marcarlo solo con un color | `CA-03` lo exige, y un color no se lee en voz alta ni sirve para quien no lo distingue |
| El estado de un proyecto sin nada traído dice qué haría falta | Mostrar la pantalla vacía | `CA-02`. Una pantalla vacía se lee como un error de la plataforma |

### 2.7 Dudas por resolver antes de escribir

Ninguna. Las dos que había se midieron y las decidió el usuario antes de escribir el plan.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Corregir el hueco de la fase E: `cvds/` entra, con los moldes de sus documentos | Traer reconoce también las etapas del ciclo |
| 2 | Calcular qué etapas tienen documento | La lista de las etapas, con cuáles tienen y cuáles no |
| 3 | Calcular qué fases hay y en qué estación van | El recuento, y las que no se pudieron leer con su ruta |
| 4 | Calcular qué está aprobado y desde cuándo | Cuántos aprobados, cuántos no |
| 5 | Que el estado de un proyecto sin nada diga qué haría falta | El texto, no una pantalla vacía |
| 6 | Mostrarlo en la pantalla del proyecto, con palabras | La pantalla |
| 7 | Medir que cincuenta proyectos con estado listan bajo un segundo | La medición, con su número escrito |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6 → 7. La 1 va primero porque sin ella la 2 no tiene qué leer.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-01` el estado se ve sin abrir la carpeta | Se trae un proyecto, se pide su estado, y se comprueba que no se leyó su carpeta |
| `CA-02` un proyecto sin trabajo abierto lo dice | Se pide el estado de uno recién conectado |
| `CA-03` lo aprobado se distingue, con palabras | Se trae un proyecto con documentos aprobados y sin aprobar |
| Transversal `RNF-02` | Se listan cincuenta proyectos y se mide |
| Transversal: ruta perdida | Se borra la carpeta de un proyecto traído y se pide su estado |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Proyectos de mentira creados y borrados por la prueba. El caso real vuelve a ser este repositorio, ya traído.

## 7. Reversión

Se descarta la rama de la fase. El estado no se guarda, así que revertir no deja datos que limpiar.

## 8. Producción y migración

Lo traído antes de esta fase no incluye `cvds/`. **No hay que migrar nada**: basta con volver a traer, que no duplica y actualiza lo que cambió.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Proyectos describe esto en su §6 |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `04·R4` no afirmar sobre lo que no se leyó | Una estación ilegible se dice, no se supone |
| `02·F8` editar solo lo que el plan declara | Tocar `importacion/moldes.py` queda declarado en §2.1, con su razón |
| `01·C7` ante dos lecturas, preguntar | Las dos dudas se midieron y las decidió el usuario |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que calcular el estado de cincuenta proyectos rompa `RNF-02` | Es la tarea 7. Se mide, y el número se escribe |
| 2 | Que el estado se calcule leyendo el proyecto y no lo traído | Es lo que `CA-01` prohíbe. La prueba comprueba que con la carpeta borrada el estado sale igual |
| 3 | Que las doce formas de escribir la estación crezcan a trece | Por eso no se adivina: lo que no se pueda leer se dice, y el usuario decide |

## 11. Definition of Done

- ☐ `cvds/` entra a lo que se trae, con los moldes de sus documentos.
- ☐ El estado dice qué etapas tienen documento.
- ☐ El estado dice cuántas fases hay, en qué estación, y cuáles no se pudieron leer.
- ☐ El estado dice qué está aprobado y desde cuándo, con palabras.
- ☐ Un proyecto sin nada traído dice qué haría falta.
- ☐ Un proyecto con la ruta perdida muestra su estado igual.
- ☐ Medido cuánto tarda listar cincuenta proyectos con estado, con el número escrito.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los siete puntos de la sección 11 tengan veredicto. **En el cierre se anota el defecto de la fase E**, que estaba cerrada cuando se encontró.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md).
