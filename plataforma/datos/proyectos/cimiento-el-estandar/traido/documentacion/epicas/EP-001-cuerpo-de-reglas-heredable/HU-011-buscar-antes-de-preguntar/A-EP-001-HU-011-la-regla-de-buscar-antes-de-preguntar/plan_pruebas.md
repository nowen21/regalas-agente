# Plan de Pruebas — Fase A-EP-001-HU-011: la regla de buscar antes de preguntar

**Para qué sirve este documento.** Dice **con qué casos se comprueba** que lo escrito hace lo que la HU pidió. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-011 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente — el usuario |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Documental | Que la regla cumpla el molde y el checklist | Sí, en las once filas que un programa cuenta |
| Lectura | Que cubra los tres CA de la HU | No: es criterio |
| Regresión | Que agregar una regla no rompa ninguna corrida | Sí |

**El entregable es texto, y eso cambia qué se puede probar.** Que la regla se cumpla en una sesión futura no se puede comprobar hoy — lo que se comprueba es que **esté bien escrita, quepa, no choque y esté clasificada**. Confundir las dos cosas sería declarar probado lo que solo está escrito.

### 3.2 Técnicas

- **Contraste contra el propio checklist**, que es la especificación ya escrita: veinte filas, once de ellas contables por programa.
- **Lectura contra cada CA de la HU**, uno por uno, sin dar ninguno por evidente.
- **Comparación antes/después** de las corridas que ya existían.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py estandar`, `validar.py metareglas`, `citas.py` en simulación, y las dos suites del repositorio.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| CA-01 · lo escrito no se pregunta | [CP-001](#cp-001--la-regla-cubre-los-tres-ca) | ☐ |
| CA-02 · lo no escrito sí se pregunta | [CP-001](#cp-001--la-regla-cubre-los-tres-ca) | ☐ |
| CA-03 · la contradicción se muestra | [CP-001](#cp-001--la-regla-cubre-los-tres-ca) | ☐ |
| `M14` · nace con su checklist | [CP-002](#cp-002--el-checklist-de-las-veinte-filas) | ☐ |
| `M5` · cabe en el molde | [CP-003](#cp-003--cabe-en-el-molde) | ☐ |
| `M4` · el identificador está libre | [CP-004](#cp-004--el-identificador-no-estaba-tomado) | ☐ |
| `M9` · clasificada | [CP-005](#cp-005--queda-clasificada-con-su-motivo) | ☐ |
| No regresión | [CP-006](#cp-006--ninguna-corrida-se-rompió) | ☐ |

**Cobertura:** 6 de 6 exigencias con caso = 100%, transversales incluidas.

---

## 6. Casos de prueba

### CP-001 — La regla cubre los tres CA

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el cuerpo contra el CA-01 | Dice que lo ya decidido no se pregunta, y que se sigue citando dónde |
| 2 | Contra el CA-02 | Dice que si no está se pregunta, y que se diga dónde se buscó |
| 3 | Contra el CA-03 | **Este es el que hay que mirar con cuidado:** la regla no lo nombra aparte |

> **El paso 3 puede fallar y hay que decidirlo, no darlo por bueno.** El CA-03 —mostrar la contradicción cuando lo escrito choca con lo pedido— no está dicho con esas palabras. Si el veredicto es que no queda cubierto, se anota y **no se ajusta el CA para que encaje**.

---

### CP-002 — El checklist de las veinte filas

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aplicar las veinte filas y escribir el bloque | Resultado **CUMPLE**, con su conteo |
| 2 | Correr `validar.py metareglas` y buscar `C23` | No la reporta |

---

### CP-003 — Cabe en el molde

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir el cuerpo con el programa | ≤ 320 caracteres |
| 2 | Si se pasa, recortar y volver a medir | Cabe, y lo que se quitó es porqué, no exigencia |

> **Se mide con el programa y no a ojo.** Es el defecto que apareció seis veces hoy al revisar el análisis del 2026-08-07.

---

### CP-004 — El identificador no estaba tomado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los identificadores del capítulo `01` | El mayor es `C22` |
| 2 | Comprobar que `C23` no existe en ninguna parte | No existe |

> No es trámite: al sellar el capítulo `09` se vio que el número que un análisis reservaba para partir `G8` ya estaba ocupado por una regla nacida después.

---

### CP-005 — Queda clasificada con su motivo

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `C23` en `reglas-validables.md` | Está, en la lista que le toca |
| 2 | Leer el motivo | Dice **por qué** es validable a medias, no solo que lo es |

---

### CP-006 — Ninguna corrida se rompió

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validar.py estandar` | Sin incumplimientos |
| 2 | `citas.py` en simulación | 0 enlazadas · 0 reparadas |
| 3 | Las dos suites | Igual que antes |

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que la regla choque con otra del capítulo, o que el identificador estuviera tomado | Inmediato |
| **Alta** | Que un CA quede sin cubrir | Se anota y se decide; **no se ajusta el CA** |
| **Media** | Que no quepa | Se recorta el porqué |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Filas del checklist en ❌ | **0** |
| Caracteres del cuerpo | ≤ 320 |
| Corridas que cambian de resultado | **0** |
| CA cubiertos | 3 de 3, o dicho cuál no |

Un solo concepto: **Cumple** o **No cumple**.
