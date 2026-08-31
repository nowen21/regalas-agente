# Resultado de Pruebas — Fase `A-EP-004-HU-010-declaracion-y-comprobacion`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-010-declaracion-y-comprobacion` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

**Estuvo detenida trece días en la estación 7.** El usuario la aprobó el 2026-08-30.

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cinco criterios se ejecutaron. Dos se verificaron contra proyectos reales y tres hubo que provocarlos, porque ningún proyecto real sirve para verlos. Y provocarlos encontró un defecto que llevaba meses reclamando de más en todos los proyectos.

| Métrica | Meta | Real |
|---|---|---|
| Criterios ejecutados | 5 de 5 | **5 de 5** |
| Criterios verificados leyendo en vez de corriendo | 0 | **0** |
| Contrapruebas | una por criterio provocado | **4 de 4** |
| Defectos encontrados | — | **1**, corregido acá |

---

## 3. Resultado por caso

### CA-01 — Sin declaración no se comprueba, y se dice qué quedó sin comprobar

**Verificado contra tres proyectos reales, cada uno en un estado distinto**, que es lo que hace útil el caso:

| Proyecto | Qué declara | Qué dice la comprobación |
|---|---|---|
| shopnest-mesa | La mayoría de las claves | Nombra las tres de inmutables que faltan, y qué regla queda sin comprobar por cada una |
| agro-system | Tiene el archivo, con las claves en blanco | Nombra cada clave sin declarar, con su regla |
| rni-back | No tiene los archivos | Dice que no existen y que sin ellos no hay contra qué comparar |

**Resultado: pasa.** En los tres casos dice **qué** se dejó de comprobar y **por qué**, en vez de callar o de reclamar.

### CA-02, CA-03 y CA-04 — Provocados, porque ningún proyecto real sirve

Los tres piden que se **reporte** un incumplimiento, y no hay dónde verlo: shopnest tiene las migraciones en un formato que el programa no lee, y agro-system no declara sus entidades. Provocarlo en un proyecto real está prohibido por la decisión 35 del pendiente 59, así que se armó uno temporal, con su declaración, sus migraciones y su repositorio.

**Cada uno con su contraprueba**: el mismo proyecto sin el defecto no debe reclamar nada. Sin eso, un validador que reclamara siempre pasaría igual.

| Criterio | Con el defecto | Sin el defecto |
|---|---|---|
| CA-02 · nombre fuera de la convención | `la columna clientes.nombreCompleto no sigue snake_case (EST2)` | Ningún reclamo |
| CA-03 · tabla de dominio sin auditoría | `la tabla facturas es de dominio y le faltan columnas de auditoría` | Ningún reclamo |
| CA-04 · inmutable sin estados ni permiso | `Factura es inmutable y no aparece ninguno de los estados declarados` | Ningún reclamo |

**Resultado: pasan los tres.**

### CA-05 — Un módulo del código sin declarar se reporta

Verificado en los dos lados. Sobre shopnest-mesa, que declara su convención de módulos, reporta **siete** carpetas que encajan con ella y no están en el dominio. Y provocado en el proyecto de prueba, reporta el módulo `cobros`, que existe en el código y no está declarado; sin él, ningún reclamo.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El defecto que apareció al provocar, y que leyendo no se veía

**El reclamo de que una entidad inmutable no tiene su permiso salía siempre, en todo proyecto.**

El patrón se declara como `anular_<recurso>` y la comprobación arma su expresión reemplazando el marcador **sobre el texto ya escapado**. Hasta Python 3.6, `re.escape` escapaba todo lo que no fuera alfanumérico, así que los ángulos salían escapados y el reemplazo encajaba. Desde 3.7 solo escapa lo que de verdad significa algo en una expresión, y los ángulos no.

**El reemplazo dejó de ocurrir en silencio.** La expresión quedaba literal, no encontraba ningún permiso, y toda entidad inmutable de todo proyecto recibía el reclamo. Un reclamo que sale siempre es el que se aprende a ignorar, y ese es el daño: no el falso positivo, sino lo que le enseña al que lo lee.

Se corrigió buscando lo mismo que se escapó, sin suponer cómo quedó escapado. Queda con su prueba de no regresión y su contraprueba.

### 4.2 Por qué las declaraciones del proyecto de prueba se escribieron dos veces

La primera versión declaró los estados por el **nombre de la columna** y el permiso **sin el marcador**. Las dos estaban mal, y el programa tenía razón en reclamar: los estados se buscan como valores entre comillas dentro del esquema, y el patrón del permiso necesita `<recurso>` para saber de qué entidad habla.

Vale dejarlo dicho porque es la trampa de este tipo de prueba: **un caso mal armado se lee igual que un programa roto**. Lo que los separa es mirar qué espera el programa antes de acusarlo.

### 4.3 El proyecto de prueba tiene que ser un repositorio

Las comprobaciones solo miran archivos versionados, y es a propósito: lo que no está guardado todavía no es del proyecto. La primera corrida no encontró ni una migración, y el resultado se leía como si todo estuviera bien.

---

## 5. Defectos encontrados

| ID | Severidad | Qué es | Estado |
|---|---|---|---|
| D-01 | **Alta** | El patrón del permiso no reemplazaba su marcador: el reclamo de `15·IM5` salía en todo proyecto con una entidad inmutable | **Cerrado** en esta fase, con prueba |

---

## 6. Evidencias

- El guion que provoca los cuatro casos con sus contrapruebas: `historico-chat/scripts/2026-08-30/provocar-los-ca-de-hu010.py`
- `validadores/entidades.py`, `recursos_con_permiso`
- `validadores/tests/test_las_entidades_no_acusan_a_ciegas.py`: 7 pruebas, 7 en verde
- Las corridas contra shopnest-mesa, agro-system y rni-back
