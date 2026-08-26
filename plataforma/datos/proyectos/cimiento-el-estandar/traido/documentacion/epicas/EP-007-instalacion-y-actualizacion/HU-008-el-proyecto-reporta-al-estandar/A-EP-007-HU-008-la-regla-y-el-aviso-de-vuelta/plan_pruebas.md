# Plan de Pruebas — Fase A-EP-007-HU-008: la regla y el aviso de vuelta

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-008 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | A quién le toca el aviso, y qué dice | Proyectos de mentira en carpetas temporales |
| Documental | Que la regla pase su checklist y las plantillas se nombren entre sí | El repositorio |
| Regresión | Que cerrar un pendiente siga funcionando igual | Las dos suites |

**Este programa escribe en el repositorio de otro proyecto**, y eso cambia dónde está el riesgo. Lo que hay que probar no es sobre todo que el aviso llegue —eso es visible— sino **que no llegue a quien no debe, que no escriba de más y que no duplique**. Un aviso de menos se nota; uno de más ensucia el backlog ajeno y nadie lo relaciona con acá.

### 3.2 Técnicas

- **Proyectos de mentira, siempre tres**, para poder comprobar que a dos **no** les llegó. Con uno solo, «llegó al de origen» y «llegó a todos» dan lo mismo.
- **Comparación de la carpeta antes y después**, para fijar que no se escribió nada fuera de `pendientes/`.
- **Repetición**, para la idempotencia.

### 3.5 Alcance de la corrida

`validadores/tests/` entera, `validadores/pruebas.py` entera —se toca `cerrar.py`, que ya tiene sus casos—, `validar.py estandar`, `validar.py pendientes` y `validar.py metareglas`.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-01 · los dos pendientes, cada uno nombrando al otro | [CP-001](#cp-001--las-dos-plantillas-se-nombran-entre-sí) | ☐ |
| CA-02 · sin proyecto de origen se reporta | [CP-002](#cp-002--el-proyecto-de-origen-se-comprueba) | ☐ |
| CA-03 · el aviso llega al de origen y a nadie más | [CP-003](#cp-003--el-aviso-llega-solo-a-quien-le-toca) | ☐ |
| CA-04 · «a todos» llega a todos | [CP-004](#cp-004--el-arreglo-que-rige-para-todos-avisa-a-todos) | ☐ |
| RNF-02 · idempotencia | [CP-005](#cp-005--cerrar-dos-veces-no-duplica-el-aviso) | ☐ |
| Transversal · errores | [CP-006](#cp-006--lo-que-no-se-puede-hacer-se-dice-no-se-rompe) | ☐ |
| Transversal · el alcance de la escritura | [CP-007](#cp-007--no-escribe-nada-fuera-de-la-carpeta-de-pendientes) | ☐ |
| No regresión | [CP-008](#cp-008--cerrar-un-pendiente-sigue-funcionando) | ☐ |

**Cobertura:** 8 de 8 exigencias con caso = 100%, transversales incluidas y contadas.

---

## 6. Casos de prueba

### CP-001 — Las dos plantillas se nombran entre sí

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la del estándar | Enlaza la del proyecto y dice que los dos se escriben en la misma sesión |
| 2 | Abrir la del proyecto | Enlaza la del estándar y dice que **no se cierra al reportar** |
| 3 | Buscar la casilla del proyecto de origen | Está, con el aviso de que no es opcional |

> **Los dos se escriben juntos o no sirve ninguno.** Uno sin el otro es exactamente la mitad que falló los dos días de agosto que originaron este pendiente: el 15 se anotó solo acá, el 16 solo allá.

---

### CP-002 — El proyecto de origen se comprueba

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un pendiente con la casilla vacía | Se reporta |
| 2 | Con el marcador `«…»` sin llenar | Se reporta — una casilla con el molde puesto vale lo mismo que vacía |
| 3 | Con el nombre puesto | No se reporta |
| 4 | Sin la casilla | **No se reporta**: la mayoría del backlog nace acá y no viene de ningún proyecto |

> El paso 4 es el que evita que la comprobación se vuelva ruido sobre treinta pendientes que no tienen nada que ver.

---

### CP-003 — El aviso llega solo a quien le toca

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tres proyectos de mentira, ficha que nombra al segundo | — |
| 2 | Cerrar | El aviso queda en el segundo |
| 3 | **Mirar los otros dos** | Su carpeta de pendientes sigue **vacía** |

> El paso 3 es el caso, no un adorno. Con un solo proyecto de prueba, «llegó al de origen» y «llegó a todos» son indistinguibles.

---

### CP-004 — El arreglo que rige para todos avisa a todos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | La misma ficha, con «a **todos** los proyectos instalados» | — |
| 2 | Cerrar | Los tres reciben el aviso |

---

### CP-005 — Cerrar dos veces no duplica el aviso

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cerrar | Un aviso |
| 2 | Cerrar otra vez | **Ninguno nuevo**, y la carpeta sigue con un solo archivo |

---

### CP-006 — Lo que no se puede hacer se dice, no se rompe

| # | Caso | Resultado esperado |
|---|---|---|
| 1 | El proyecto no lleva carpeta de pendientes | No se le inventa: no recibe nada |
| 2 | El pendiente no declara proyecto de origen | No se avisa a nadie |
| 3 | El proyecto de origen no está en el registro | Se dice en la salida, con esas palabras |

> **Ninguno de los tres es una falla.** Son situaciones normales, y lo que importa es que se digan en vez de fallar en silencio o de inventar una carpeta en un repositorio ajeno.

---

### CP-007 — No escribe nada fuera de la carpeta de pendientes

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar la raíz del proyecto de mentira antes | — |
| 2 | Cerrar y volver a listar | **Idéntica** |

> Es el caso que más pesa de los ocho. Un programa que escribe en el repositorio de otro proyecto tiene que tener el alcance de una línea, y esto es lo que lo fija.

---

### CP-008 — Cerrar un pendiente sigue funcionando

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validadores/tests/` entera | Pasa, con los casos nuevos |
| 2 | `validadores/pruebas.py` entera | Igual que antes |
| 3 | `validar.py estandar` · `pendientes` · `metareglas` | Sin fallas nuevas |

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que el aviso llegue a un proyecto que no era, o que escriba fuera de `pendientes/` | Inmediato |
| **Alta** | Que se duplique, o que un cierre normal falle por el aviso | Antes de cerrar |
| **Media** | La redacción del aviso | Se reporta |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Proyectos que reciben un aviso que no era suyo | **0** |
| Archivos escritos fuera de `pendientes/` | **0** |
| Avisos duplicados al cerrar dos veces | **0** |
| Pruebas del repositorio que dejan de pasar | **0** |
| Cobertura de exigencias | 100% — 8 de 8 |

Un solo concepto: **Cumple** o **No cumple**.
