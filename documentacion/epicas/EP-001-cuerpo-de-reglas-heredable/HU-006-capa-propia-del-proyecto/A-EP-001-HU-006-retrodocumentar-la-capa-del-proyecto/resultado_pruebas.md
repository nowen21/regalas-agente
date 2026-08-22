# Resultado de Pruebas — Fase A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |
| **Proyecto de prueba** | **AgroSystem** (`C:\wamp64\www\proyectos\personales\agro-system`), Laravel + Livewire + Spatie |

---

## 1. Dos cosas del plan resultaron falsas, y hay que decirlo primero

El plan se escribió el 2026-08-17 y su línea base envejeció. Al ejecutarlo, dos afirmaciones no se sostuvieron:

**Primera: el proyecto propuesto no servía para esta fase.** La propuesta 12 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) decía **shopnest-mesa**, por ser el único que reporta al estándar y tener estructura completa. Comprobado: **shopnest-mesa no tiene `.agente/reglas-proyecto.md`**, o sea que no tiene capa propia de reglas, que es exactamente lo que esta fase viene a probar. Se cambió a **AgroSystem**, que sí la tiene, con 56 reglas `P` escritas.

| Proyecto | `reglas-proyecto.md` | Sirve para esta fase |
|---|---|---|
| shopnest-mesa | **no** | No |
| AgroSystem | sí, 56 reglas `P` | **Sí** |
| RNI | sí | Sí, queda de reserva |

**Segunda: la comprobación de `M16` sí existe.** El plan la daba por inexistente en su «Lo que no existe», punto 1. La construyó el [pendiente 53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) y hoy corre. Lo que quedaba era encontrar cómo se invoca, y no es como el plan suponía.

---

## 2. Ejecución caso por caso

| Caso | Qué se corrió | Qué salió | Concepto |
|---|---|---|---|
| CA-01 | Leer la capa propia de AgroSystem y su declaración de precedencia | El propio archivo declara el orden: `00` núcleo → `01`-`17` convenciones → **reglas `P`**, y dice que una `P` puede endurecer o complementar una convención pero nunca contradecir el núcleo | Cumple |
| CA-02 | `python validadores/validar.py metareglas --catalogo <proyecto>` | **56 fallas de 56 reglas.** Ninguna de las reglas `P` de AgroSystem declara su respaldo | Cumple |
| CA-03 | Buscar en la capa propia un ajuste que afloje una regla `[BLINDADA]` | No hay ninguno, y el propio archivo escribe la prohibición. El caso no se pudo provocar sobre el proyecto real, y provocarlo ahí está prohibido por la decisión 35 del pendiente 59 | Cumple a medias, ver §4 |
| RNF | `validar.py version --raiz <proyecto>` sobre shopnest-mesa | Avisa: el proyecto declara v27.2.0 y el estándar va en v32.0.0. Avisa y no detiene, que es lo previsto | Cumple |

---

## 3. Verificaciones manuales

**Cómo se invoca la comprobación de `M16`, que era lo que faltaba saber:**

```
python validadores/validar.py metareglas --catalogo <ruta del proyecto>     ← correcto
python validadores/validar.py metareglas --raiz    <ruta del proyecto>     ← no sirve
```

Con `--raiz` el programa corre **las meta-reglas del estándar contra la carpeta del proyecto**, y busca ahí `CHANGELOG.md`, `VERSION`, `base/20-meta-reglas/estructura-regla.md` y `validadores/reglas-validables.md`, que un proyecto no tiene. Devuelve **una falla y cuatro avisos, los cinco falsos**. Queda como defecto en §4.

**Las 56 fallas de `M16` no son un defecto del validador: son un defecto de AgroSystem.** El proyecto escribió 56 reglas propias y ninguna dice qué regla de base concreta. Eso es exactamente lo que `M16` existe para impedir, y nunca se había corrido sobre él.

---

## 4. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Alta** | `metareglas --raiz <proyecto>` reporta una falla y cuatro avisos falsos: corre las comprobaciones del estándar contra un proyecto, que no tiene esos archivos. Un veredicto falso enseña a ignorar los veredictos | **Abierto.** Necesita su pendiente |
| D-02 | **Alta** | Las 56 reglas `P` de AgroSystem no declaran respaldo. Es del proyecto, no del estándar, y va por el canal de defectos de vuelta | **Abierto.** Es del proyecto |
| D-03 | Media | El CA-03 no se pudo provocar: ningún proyecto real tiene un ajuste que contradiga el núcleo, y escribir uno en un proyecto real está prohibido por la decisión 35. Se comprobó por lectura, no por ejecución | **Abierto** |
| D-04 | Baja | El plan daba por inexistente la comprobación de `M16`, construida cinco días antes de ejecutarlo | **Cerrado** al comprobarlo |

---

## 5. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, el ajuste manda sobre la convención | Lectura de la declaración de precedencia de la capa propia, y el cuerpo central sin cambios | Cumple |
| CA-02, una regla propia sin respaldo no se acepta | La comprobación corre y encuentra 56 de 56 | Cumple |
| CA-03, el ajuste que contradice el núcleo no aplica | Por lectura. No se pudo provocar sin escribir en un proyecto real | **No cumple** |

## 5.1 Lo que el plan exigía

El plan pedía provocar los tres casos. Dos se provocaron; el tercero no, y no por descuido: **provocarlo exige escribir un ajuste que afloje una regla blindada en un proyecto real**, y la decisión 35 del pendiente 59 lo prohíbe expresamente. Lo que falta es hacerlo sobre un proyecto de mentira en carpeta temporal, que es lo que esa misma decisión manda.

---

## 6. Veredicto de la fase

**Concepto:** No cumple.

**Justificación:** el CA-03 quedó en «No», y la fase no cierra con un criterio en rojo. Los otros dos sí quedaron cumplidos, y con evidencia dura: la comprobación de `M16` corre y encuentra 56 incumplimientos reales.

**Qué falta para que cumpla:** provocar el CA-03 sobre un proyecto de mentira en carpeta temporal, escribiendo un ajuste que afloje una regla `[BLINDADA]` y dejando dicho qué pasa. Es una tarea, no una fase nueva.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Las 56 fallas de `M16` | `validar.py metareglas --catalogo C:\wamp64\www\proyectos\personales\agro-system` |
| EV-02 | Los cinco veredictos falsos de `--raiz` | §3 de este documento |
| EV-03 | La capa propia de AgroSystem, con su declaración de precedencia | `.agente/reglas-proyecto.md` del proyecto |
| EV-04 | El aviso de versión atrasada | `validar.py version --raiz <shopnest-mesa>` |

---

## 8. Ciclos anteriores

Ninguno: la fase estaba aprobada desde el 2026-08-17 y nunca se había ejecutado.
