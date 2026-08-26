# Resultado de Pruebas — Fase B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Qué se midió antes de dejarlo

**Medido antes de dejarlo, que es lo que [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) pide.** Sobre el histórico completo de este repositorio el patrón nuevo tocaría **cero líneas**: ningún falso positivo en el corpus real. Y sobre el resto del repositorio apareció el único que importaba, `clave = h.regla`, que es código pegado y no una credencial. Esa medición fue la que obligó a pedir un número o una longitud.

---

## 2. Ejecución caso por caso

| Caso | Qué entra | Qué sale |
|---|---|---|
| Asignación sin comillas | `API_KEY=supersecreto123456` | se tapa el valor, no la variable |
| Con dos puntos | `password: MiClave123456` | se tapa |
| La palabra en español | `la contraseña: Patito2026` | se tapa |
| Valor largo sin números | `secret=abcdefghijklmnop` | se tapa |
| Código pegado en el chat | `clave = h.regla or algo` | **no** se tapa |
| Valor corto y sin números | `token: xyz` | **no** se tapa |
| Lee del entorno | `API_KEY=os.environ[...]` | **no** se tapa |
| Un molde | `password: changeme` | **no** se tapa |
| Una frase normal | «La clave del asunto es que el proceso sirva» | **no** se toca |

**Buena parte de los casos son de lo que NO debe hacer.** Una comprobación que reprueba de más, o un enmascarador que tapa de más, se apaga a la semana, y entonces no queda nada.

---

## 3. Suites que la fase toca  ·  `02·F5`

| Suite | Cuántas |
|---|---|
| test_la_clave_sin_comillas_se_enmascara | 12 pruebas |
| test_la_clave_no_llega_al_historico | 11 pruebas |
| test_el_historico_se_busca_por_tema | 7 pruebas |

Todas en verde.

---

## 4. Defectos encontrados

Ninguno propio.

---

## 5. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** lo que la fase A dejó en rojo quedó cerrado, comprobado sobre casos reales y no sobre ejemplos escritos para la ocasión.

**Lo que no cubre, dicho para que el «Cumple» no se lea de más:** la clave dicha enteramente en prosa —«el token de producción es X»— sigue sin taparse cuando no hay dos puntos ni igual. Es el punto 2 del pendiente, y se dejó por el riesgo de tapar de más, que es el que vuelve inútil un enmascarador.

---

## 6. Evidencias

- `validadores/enmascarar.py`
- `validadores/tests/test_la_clave_sin_comillas_se_enmascara.py`
