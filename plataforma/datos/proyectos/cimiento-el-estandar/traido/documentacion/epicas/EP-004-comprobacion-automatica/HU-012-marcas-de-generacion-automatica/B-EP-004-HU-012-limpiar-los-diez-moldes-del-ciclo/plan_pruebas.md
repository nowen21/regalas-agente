# Plan de Pruebas — Fase `B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo`   ·   `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó y se cerró el 2026-08-22 y **este documento se quedó siendo la plantilla en blanco**: 363 líneas de molde con 36 marcadores sin reemplazar. Lo destapó la [HU-022](../../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md).
>
> **No se inventa nada.** Los casos y las cifras salen del [resultado_pruebas.md](resultado_pruebas.md), que sí se escribió y documenta paso por paso qué se hizo y qué salió. **Lo que no se puede reconstruir —qué se pensó antes de ejecutar— no se escribe.**

---

## 1. Propósito y alcance

Comprobar el `CA-04` de la [HU-012](../HU-012-marcas-de-generacion-automatica.md): **que los moldes del ciclo de vida no le pasen adorno de prosa al proyecto que los copia.**

**Es una limpieza en lote sobre 10 archivos que se reparten a todos los proyectos.** Ese es el riesgo: un reemplazo automático sobre texto que otros programas leen.

**Entra:** quitar la raya larga de inciso, el punto medio de prosa y las citas de regla mal formadas, dejando la notación.

**No entra:** llegar a cero marcas, que es lo que pedía el [pendiente 78](../../../../../pendientes/hecho/los-moldes-se-entregan-limpios-de-marcas.md). Lo que quede siendo notación se conserva, y qué hacer con ella lo decide el usuario.

---

## 2. Estrategia

**De lote con revisión a mano encima.** Un reemplazo masivo sobre texto no se comprueba solo con un recuento: hay que **mirar línea por línea lo que cambió**, porque el daño típico es una frase que queda casi bien.

**Y hay que comprobar lo que NO cambió**, que es lo que de verdad importa: ninguna sección puede desaparecer ni cambiar de nombre. Los 650 documentos ya escritos dependen de esos nombres.

---

## 3. Casos de prueba

| Caso | Qué se hace | Qué debe salir |
|---|---|---|
| **CP-001** · volcar antes de tocar | cada marca con archivo, línea y clase | El reparto completo, clasificado |
| **CP-002** · citas de regla al formato canónico | `` `01`·C3 `` → `` `01·C3` `` | Menos marcas, **y citas que ahora sí son citas** |
| **CP-003** · raya de inciso a puntuación normal | las líneas que la usan como inciso | Cambiadas |
| **CP-004** · **revisión a mano de cada línea cambiada** | las del `CP-003`, una por una | Las que quedaron mal, corregidas |
| **CP-005** · punto medio de prosa a coma | las líneas que lo usan fuera de una cita | Cambiadas |
| **CP-006** · **el marcador `«…»` sigue entero** | los moldes tras el `CP-005` | **Ningún marcador roto** |
| **CP-007** · recontar y reclasificar | los 10 moldes | Lo que queda es **todo notación** |
| **CP-008** · ninguna sección desapareció ni cambió de nombre | comparación sección por sección | Idénticas |
| **CP-009** · las suites que dependen de los moldes | marcas, trinquete, andamio, instalador, origen de reglas | En verde |
| **CP-010** · las comprobaciones del repositorio | `estandar`, `fases`, `pendientes` | Sin incumplimientos nuevos |

**El `CP-006` es el crítico, y se aprendió rompiéndolo.** El reemplazo del punto medio **partió el marcador `«…»` en 24 sitios**, y ese marcador lo leen `flujo.py`, `comun.py` y `andamio.py` para saber si una celda quedó sin llenar. El [pendiente 11](../../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) lo advertía por escrito **y no se leyó antes de ejecutar**.

**El `CP-004` existe porque el `CP-003` no basta.** De 25 líneas cambiadas, **6 quedaron mal**: la coma donde iban dos puntos. Un recuento no lo ve; leerlas sí.

**El `CP-008` es el que protege a los demás.** Renombrar una sección haría que 650 documentos ya escritos reporten «sección de la plantilla ausente».

---

## 4. Criterio de aprobación

- **Ninguna marca que quede es adorno de prosa**, comprobado clasificando una por una.
- Ningún molde perdió una exigencia, ni una sección cambió de nombre.
- Las suites que dependen de los moldes, en verde.
- **El recuento no tiene que dar cero**, y decirlo por escrito con el motivo.

---

## 5. Qué se ejecutó, y con qué resultado

Está en el [resultado_pruebas.md](resultado_pruebas.md). En corto:

| Métrica | Antes | Después |
|---|---|---|
| Marcas en los 10 moldes | 197 | **126** |
| Raya larga como inciso | 92 | 59 |
| Punto medio fuera de cita | 62 | 24 |

**Se quitaron 71, y las 126 que quedan son todas notación**, clasificadas una por una: 43 etiquetas de campo, 40 celdas de tabla, 23 títulos y 21 identificadores con su enunciado.

**Cuatro defectos**, tres reales y uno falso — y el falso también enseña: se reportó que el recuento contaba marcas dentro de bloques de código, y **era mentira**; las había contado un clasificador improvisado del propio agente, no `marcas.py`.

---

## 6. Herramientas y datos

`marcas.py` para el recuento, los 10 moldes reales, y las 47 pruebas de las suites que dependen de ellos. **Ninguna prueba usa credenciales** (`00·N6`).

---

## 7. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | **Retrodocumentado.** La fase cerró el 2026-08-22 sin este documento |
