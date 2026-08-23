# Resultado de Pruebas — Fase B-EP-002-HU-003-la-version-declarada-se-comprueba   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-003-la-version-declarada-se-comprueba` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Qué se midió antes de dejarlo

**Comprobado sobre casos reales antes de dejarlo.** Una copia temporal declarando `99.9.9` ahora falla diciendo que esa versión no existe. Y shopnest-mesa, sin tocarlo, falla por lo segundo: declara `27.2.0` y su historial dice `28.0.0`, los dos del 2026-08-20. Esa contradicción llevaba dos días sin que nadie la viera.

---

## 2. Ejecución caso por caso

| Caso | Qué entra | Qué sale |
|---|---|---|
| Versión que no existe | `99.9.9` declarada | falla, y dice que no está en el registro |
| Declarada distinta del historial | declara `1.0.0`, historial dice `2.0.0` | falla, y nombra las dos |
| Proyecto al día | declara la vigente | silencio |
| Proyecto atrasado | declara una anterior | avisa, no falla |
| Sin historial de adopciones | proyecto recién instalado | **no** falla |
| Sin registro de cambios legible | no se sabe qué versiones existen | **no** acusa a nadie |
| El último registro es el mayor | `9.0.0` y `10.0.0` | gana `10.0.0`, no el último alfabético |

**Buena parte de los casos son de lo que NO debe hacer.** Una comprobación que reprueba de más, o un enmascarador que tapa de más, se apaga a la semana, y entonces no queda nada.

---

## 3. Suites que la fase toca  ·  `02·F5`

| Suite | Cuántas |
|---|---|
| test_la_version_adoptada_se_comprueba | 10 pruebas |

Todas en verde.

---

## 4. Defectos encontrados

Ninguno propio.

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** lo que la fase A dejó en rojo quedó cerrado, comprobado sobre casos reales y no sobre ejemplos escritos para la ocasión.

**Lo que no cubre, dicho para que el «Cumple» no se lea de más:** no se decide qué hacer cuando las dos difieren: eso es del usuario, y lo que se pedía es que se vea. Y queda sin averiguar si el instalador escribe el registro sin actualizar la declaración, que explicaría el caso de shopnest-mesa.

---

## 6. Evidencias

- `validadores/version.py`
- `validadores/tests/test_la_version_adoptada_se_comprueba.py`
