# Resultado de Pruebas — Fase B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Resumen de la ejecución

| Métrica | Antes | Después |
|---|---|---|
| Marcas en `plantillas/ciclo-vida-proyectos/` | 197 en 10 archivos | **126 en 10 archivos** |
| Raya larga como inciso | 92 | 59 |
| Punto medio fuera de una cita | 62 | 24 |
| Viñeta que abre con negrita y dos puntos | 43 | 43 |

**Se quitaron 71.** Ninguna de las 126 que quedan es adorno de prosa.

---

## 2. Ejecución caso por caso

| # | Qué se hizo | Qué salió |
|---|---|---|
| 1 | Volcar cada marca con archivo, línea y clase | 213 apariciones en 10 archivos, clasificadas en 7 clases |
| 2 | Escribir en formato canónico las citas de regla del molde de la especificación (`` `01`·C3 `` → `` `01·C3` ``) | 13 marcas menos, y 13 citas que ahora sí son citas |
| 3 | Raya de inciso a coma, paréntesis o dos puntos | 25 líneas cambiadas en 9 moldes |
| 4 | Revisión línea por línea de esas 25 | 6 quedaron mal y se corrigieron a mano |
| 5 | Punto medio de prosa a coma | 41 líneas en 21 moldes |
| 6 | Reponer el marcador `«…»` que el paso anterior rompió | 24 marcadores repuestos en 20 moldes |
| 7 | Recontar y volver a clasificar | 126, todas notación |
| 8 | Las suites que dependen de los moldes: marcas, trinquete, andamio, instalador y origen de las reglas | 47 pruebas, todas en verde |
| 9 | `validar.py estandar`, `fases`, `pendientes` | Sin incumplimientos; 0 fallas y avisos previos |

---

## 3. Verificaciones manuales

**Las 126 que quedan, clasificadas una por una:**

| Clase | Cuántas | Por qué no se toca |
|---|---|---|
| Etiqueta de campo del formulario (`- **Objetivo:** «…»`) | 43 | Es el rótulo del campo que hay que llenar, no una viñeta de prosa |
| Celda de tabla | 40 | Separa dato de dato dentro de una celda |
| Título y nombre de sección (`# EP-000 — «Título»`, `## 1. Necesidad — en una frase`) | 23 | Renombrarlas hace que los 650 documentos ya escritos reporten «sección de la plantilla ausente» |
| Identificador con su enunciado (`**CAE-01** — «texto»`) | 21 | Es la forma en que esta casa nombra un criterio y lo enuncia |


**Comparación sección por sección contra la versión anterior:** ninguna sección desapareció, ninguna cambió de nombre y ninguna perdió una exigencia. Los cambios son de puntuación dentro de la frase, salvo seis donde la frase se reescribió y quedan a la vista en el control de versiones.

---

## 4. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Crítica** | El reemplazo del punto medio rompió el marcador `«…»` en 24 sitios. Lo leen `flujo.py`, `comun.py` y `andamio.py` para saber si una celda quedó sin llenar | **Corregido** el mismo día. El [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) lo advertía por escrito y no se leyó antes de ejecutar |
| D-02 | Alta | La coma quedó donde iban dos puntos en 6 de las 25 líneas | **Corregido** a mano tras revisar una por una |
| D-03 | Alta | `test_plantillas_origen_regla` empezó a fallar: su fixture copia literal una línea del molde de la especificación | **Corregido.** El fixture se puso al día |
| D-04 | — | **Se reportó un defecto que no existe.** El agente afirmó que el recuento contaba 14 marcas dentro de bloques de código. Es falso: `lineas_utiles()` ya los salta, y `contar()` la usa. Las 14 las contó un clasificador improvisado del propio agente, no `marcas.py` | **Cerrado por falso** el mismo día, al comprobarlo |

---

## 5. Veredicto por criterio de aceptación

| Exigencia | Cómo se comprobó | Concepto |
|---|---|---|
| [CA-04](../HU-012-marcas-de-generacion-automatica.md#ca-04--los-moldes-del-ciclo-no-llevan-adorno-de-prosa), paso 1: hay recuento con su reparto | §1 | Cumple |
| CA-04, paso 2: lo que queda es notación | §3 | Cumple |
| CA-04, paso 3: ningún molde pide menos | §3, comparación sección por sección | Cumple |
| CA-04, paso 4: sin incumplimientos nuevos | §2, casos 8 y 9 | Cumple |

## 5.1 Lo que el plan exigía

El plan pedía llegar a que **ninguna marca sea adorno de prosa**, y eso se cumplió. El [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md) pedía además que el recuento diera **0**, y eso no se cumple: las 126 que quedan son todas notación, y qué hacer con ellas lo decide el usuario.

**El pendiente 78 queda abierto**, con su meta corregida por lo que se midió.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el CA-04 quedó verde en sus cuatro pasos. El adorno de prosa se fue, la notación se conservó, ningún molde perdió una exigencia y las suites que dependen de los moldes quedaron en verde.

**Lo que no cierra con esta fase** es el pendiente 78 completo, y está dicho arriba con el motivo.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Volcado clasificado | Este documento, §2 y §3 |
| EV-02 | Los moldes | `plantillas/ciclo-vida-proyectos/`, 21 archivos tocados |
| EV-03 | Recuento final | `python validadores/marcas.py --raiz plantillas/ciclo-vida-proyectos` |
| EV-04 | Las suites que dependen de los moldes | 47 pruebas en verde |

---

## 8. Ciclos anteriores

Ninguno para esta fase. La fase A de esta misma HU contó las marcas el 2026-08-18 y puso el trinquete; esta es la primera que limpia.
