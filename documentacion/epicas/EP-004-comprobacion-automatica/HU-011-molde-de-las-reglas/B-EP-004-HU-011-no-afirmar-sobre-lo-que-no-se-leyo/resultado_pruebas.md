# Resultado de Pruebas — Fase B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Qué se midió antes de dejarlo

Sobre AgroSystem, apuntar con `--raiz` pasó de una falla y cuatro avisos falsos a **un aviso que dice qué usar en su lugar**. Sobre el estándar sigue comprobando igual, sin incumplimientos. Y `--catalogo` sigue encontrando las 56 reglas propias sin respaldo, que era lo que sí servía.

---

## 2. Ejecución caso por caso

| Caso | Qué entra | Qué sale |
|---|---|---|
| Apuntar a un proyecto | una carpeta con `.agente/` | ninguna falla, y un aviso que nombra la bandera buena |
| El estándar se reconoce | tiene cuerpo de reglas y versión | sí |
| Carpeta con cuerpo de reglas pero sin versión | a medio instalar | no es el estándar |
| Sobre el estándar sigue comprobando | el repositorio real | sin el aviso de carpeta ajena |
| Sin los archivos no se reporta nada | carpeta vacía | silencio |
| Con los archivos sigue comprobando | versión sin su entrada | falla, y con el dato en el mensaje |

**Buena parte de los casos son de lo que NO debe hacer.** Una comprobación que reprueba de más, o un enmascarador que tapa de más, se apaga a la semana, y entonces no queda nada.

---

## 3. Suites que la fase toca  ·  `02·F5`

| Suite | Cuántas |
|---|---|
| test_metareglas_no_afirma_sobre_un_proyecto | 7 pruebas |
| test_checklist_cadena | 3 pruebas |

Todas en verde.

---

## 4. Defectos encontrados

Ninguno propio.

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** lo que la fase A dejó en rojo quedó cerrado, comprobado sobre casos reales y no sobre ejemplos escritos para la ocasión.

**Lo que no cubre, dicho para que el «Cumple» no se lea de más:** no se revisaron los demás subcomandos. `--raiz` significa «el proyecto» en casi todos, y si el mismo problema aparece en otro sale como pendiente aparte.

---

## 6. Evidencias

- `validadores/metareglas.py`
- `validadores/tests/test_metareglas_no_afirma_sobre_un_proyecto.py`
