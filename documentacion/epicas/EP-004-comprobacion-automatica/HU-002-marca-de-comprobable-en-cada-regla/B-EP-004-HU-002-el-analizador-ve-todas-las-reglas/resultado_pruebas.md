# Resultado de Pruebas — Fase `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-002-el-analizador-ve-todas-las-reglas` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

**La fase estuvo detenida trece días en la estación 4**, con su plan escrito y sin aprobar. La aprobación llegó el 2026-08-30.

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el analizador reconoce ahora las reglas escritas un nivel más abajo, y al verlas encontró lo que se buscaba: las cuatro del capítulo 16 nunca habían pasado su checklist. Se les aplicó, y el capítulo quedó dentro del molde.

| Métrica | Meta | Real |
|---|---|---|
| Reglas que el analizador ve | todas | **256**, eran 252 |
| Reglas del capítulo 16 visibles | 4 | **4** |
| Identificadores contados dos veces | 0 | **0** |
| Pruebas de la clase en verde | todas | **9 de 9** |
| Pruebas marcadas como fallo esperado | 0 | **0**, era 1 |

---

## 3. Resultado por caso

### CP-001 — El analizador ve las reglas escritas con `###`

Antes: `CQ1` a `CQ4` no aparecían en la lista de reglas. Después, las cuatro aparecen y el total pasa de 252 a 256.

**Resultado: pasa.**

### CP-002 — Y no cuenta como regla lo que solo la nombra

**Este es el caso que casi se pierde.** Al ensanchar el analizador sin más, `M19` empezó a contarse **dos veces**: una en su propio archivo, donde la regla vive, y otra en una sección del anexo de meta-reglas que solo la nombra. El programa reclamaba un identificador repetido que no existe.

Lo que separa una cosa de la otra es que el identificador es único: **un título de nivel bajo cuyo identificador ya se definió arriba es un eco, no una definición**. Y hay que mirarlo en una pasada previa sobre todo el árbol, porque en el orden de los archivos el eco se lee **antes** que la regla.

| Identificador | Veces contado |
|---|---|
| `M19` | 1 |
| `CQ1` a `CQ4` | 1 cada una |

**Resultado: pasa.**

### CP-003 — Lo que apareció al verlas

Las cuatro reglas nuevas a la vista traían, cada una, dos defectos que nadie había podido reclamar:

| Defecto | Cuántas |
|---|---|
| Escritas con `###` donde el molde pide `##` | 4 de 4 |
| Sin su bloque de checklist | 4 de 4 |
| Sin el ejemplo de lo incorrecto y lo correcto | 1 (`CQ3`) |

**No estaban mal clasificadas: no existían para el programa.** El capítulo salía en verde por el mismo motivo por el que pasaría un examen que no se corrige.

**Resultado: pasa**, y lo encontrado se corrigió en esta misma fase por decisión del usuario.

### CP-004 — La fila 18 detiene

Que toda regla diga si se puede comprobar con un programa pasó de avisar a detener. Con las 256 clasificadas, la corrida sigue en «sin incumplimientos».

**Resultado: pasa.**

### CP-005 — La derogada sigue exenta

Con más reglas a la vista y la fila 18 detenida, se comprueba que a una regla derogada no se le reclama nada: dejó de regir, y pedirle que declare si se comprueba sería pedirle cuentas a lo que ya no se aplica.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué el capítulo 16 se arregló acá y no en otra fase

El plan de esta fase no declaraba tocar `base/`: decía **listar** lo que apareciera, sin clasificarlo. Al aparecer, lo que había eran cuatro reglas fuera del molde, y dejarlas así habría dejado el cuerpo de reglas reclamando cuatro fallas sin dueño. **El usuario decidió el 2026-08-30 corregirlas en esta misma fase**, y por eso el archivo del capítulo entra en los archivos tocados.

### 4.2 Lo que se corrigió, y lo que no

Se corrigió la forma: el nivel del título, el ejemplo que le faltaba a una, y el bloque de checklist de las cuatro. **No se tocó lo que exigen**, que es lo que las haría cambiar de versión mayor.

---

## 5. Defectos encontrados

Los tres del `CP-003`, todos cerrados en esta fase.

---

## 6. Evidencias

- `validadores/metareglas.py`, la pasada previa que distingue la regla de su eco
- `base/16-cumplimiento-y-calidad.md`, con las cuatro reglas dentro del molde
- `validadores/pruebas.py`, clase `ClasificacionDeCadaRegla`: 9 pruebas, 9 en verde
- El guion que arregló el capítulo: `historico-chat/scripts/2026-08-30/arreglar-el-capitulo-16.py`
