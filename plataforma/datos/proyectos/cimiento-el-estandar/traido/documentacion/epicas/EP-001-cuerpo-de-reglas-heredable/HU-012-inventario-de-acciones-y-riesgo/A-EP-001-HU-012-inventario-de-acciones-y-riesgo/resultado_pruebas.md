# Resultado de Pruebas — Fase A-EP-001-HU-012: inventario de acciones y riesgo

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| CA | Caso | Veredicto |
|---|---|---|
| **CA-01** · la lista cubre todo | CP-001, CP-002 | ✅ **Pasa** |
| **CA-02** · cada clase con nivel y ejemplo | CP-003, CP-004, CP-005 | ✅ **Pasa** |
| **CA-03** · dos riesgos distintos no piden lo mismo | CP-006 | ✅ **Pasa** |
| **CA-04** · lo no nombrado se trata como lo peor | CP-007 | ✅ **Pasa** |
| Transversal · límites | CP-008 | ✅ **Pasa** |
| Transversal · no regresión | CP-009 | ✅ **Pasa** — con una corrección, §3 |
| No regresión general | — | ✅ `tests/` **322 · OK** · `pruebas.py` 357 · `estandar` limpio |

**23 casos automatizados** en [validadores/tests/test_las_acciones_tienen_su_riesgo.py](../../../../../validadores/tests/test_las_acciones_tienen_su_riesgo.py).

---

## 2. Lo que quedó

**12 clases de acción:** 3 🟢 se deshacen solas · 4 🟡 con trabajo · 5 🔴 no se deshacen.

**La diferencia que hacía falta:** un plan aprobado cubre 🟢 y 🟡 de corrido, y **nunca 🔴**. Eso se pide aparte, cada vez, aunque estuviera escrito en el plan.

Y quedó nombrado lo que antes no lo estaba: **borrar algo que no está en el control de versiones es 🔴**, no 🟡 — no hay de dónde recuperarlo, y nadie se entera hasta que hace falta. Hasta hoy caía en `N1` junto con cambiarle una coma a un README.

---

## 3. Tres defectos que salieron de construirlo

**El anexo se escribió primero y el validador después**, como decía el plan. Los tres los cazó la máquina, no la lectura.

### 3.1 · «En masa» no era una clase

Estaba en la tabla con el nivel **«el de su clase, subido un nivel»**, que no es un nivel. El validador la reportó por fuera de la escala.

**Es un modificador, no una clase**, y salió de la tabla a su propia sección. La escala es cerrada justamente para esto: una fila cuyo nivel es una fórmula **no se puede comparar con ninguna otra**, y comparar es para lo que existe el anexo.

### 3.2 · Una fila con dos niveles pasó la primera comprobación

`Tocar el control de versiones` decía *«🔴 para `push` y reescritura · 🟡 el resto»*. El validador lo dio por bueno: **miraba si había *algún* nivel de la escala, no si había *uno***.

Son dos clases sin partir. Se partieron —**guardar** es 🟡, **publicar o reescribir la historia** es 🔴— y la comprobación se endureció. Hay un caso que lo fija.

### 3.3 · El recuento de huérfanas buscaba en el archivo entero

`CP-002` borra una clase a propósito para comprobar que se reporta. **No se reportaba**: el nombre seguía apareciendo en otra sección —la de las masivas la usa de ejemplo— y la búsqueda miraba todo el texto.

**Sin este caso, «cero huérfanas» habría significado que el programa no busca nada.** Ahora busca en los nombres de las clases.

---

## 4. `CP-009` cazó un cambio real, y por eso se afinó

El caso dice que esta fase **no puede cambiar el núcleo**, y falló: se le había puesto a [`00-nucleo-blindado.md`](../../../../../base/00-nucleo-blindado.md) el enlace al anexo — que el propio plan pedía en su `T-06`.

**El plan y la prueba se contradecían, y se resolvió leyendo el criterio**, no eligiendo cuál ganaba. La historia dice *«`N1` a `N6` siguen vigentes tal como están»*: lo que protege es **el texto de las seis reglas**, no el archivo. Una nota encima de `N1` que dice «este anexo organiza y no cambia nada» no altera ninguna vigencia.

El caso ahora compara **las seis reglas** contra lo guardado. Sigue fallando si se toca una línea de ellas.

---

## 5. Lo que no se comprueba, y está declarado

**Que la clasificación sea la acertada.** Que borrar un archivo no versionado merezca 🔴 y no 🟡 es un juicio, y se discute leyendo.

Está en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) como parcial, que es lo que [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) pide: **una comprobación honesta sobre lo que no cubre vale más que una que finge cubrirlo todo**.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4, más los dos transversales |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 — con tres correcciones dentro del ciclo |
