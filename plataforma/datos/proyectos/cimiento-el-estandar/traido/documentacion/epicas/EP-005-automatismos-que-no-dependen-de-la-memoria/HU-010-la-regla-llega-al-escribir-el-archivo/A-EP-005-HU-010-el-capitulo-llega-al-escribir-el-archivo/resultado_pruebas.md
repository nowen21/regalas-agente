# Resultado de Pruebas — Fase A-EP-005-HU-010: las reglas relacionadas llegan al escribir

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| CA | Veredicto |
|---|---|
| **CA-01** · al escribir llegan las reglas relacionadas | ✅ **Pasa** |
| **CA-02** · no se repite en la misma sesión | ✅ **Pasa** — y otra sesión sí lo recibe |
| **CA-03** · lo que no le toca no dispara nada | ✅ **Pasa** — silencio |
| Nunca detiene | ✅ **Pasa** — sale con 0 en los tres casos |
| No regresión | ✅ **Pasa** — `tests/` **222 · OK** · `pruebas.py` 357 · `estandar` limpio |

**14 casos automatizados** en [validadores/tests/test_llegan_las_reglas_relacionadas.py](../../../../../validadores/tests/test_llegan_las_reglas_relacionadas.py).

---

## 2. El caso que da origen a todo, comprobado

Al tocar `02·F2`, lo primero que llega es esto:

```
**Las que dependen de lo que está tocando.** Si cambia lo que dicen, estas se rompen sin avisar:
  `00·ID3` — No des por entregado un cambio hasta que cumpla su especificación…
  `00·ID5` — Seis cosas quedan fuera por definición del rol…
  `02·F0`  — Todo desarrollo recorre planteamiento → épica → HU → especificación → plan → código…
  `02·F4`  — Cada plan de trabajo se redacta junto a su plan de pruebas…
  `13·DOC3`— Antes de cerrar, revisa ítem por ítem…
```

**`02·F0` sale tercera.** Es la regla con la que se chocó hoy al escribir una frase en `F2` — la relación estaba escrita, en el texto de la propia `F2`, y nadie la miró.

---

## 3. El `CA-01` cambió antes de construir, y por qué

Decía *«llega completo el capítulo del flujo de trabajo»*. Se cambió a **las reglas relacionadas**, y hay dos motivos medidos:

| | |
|---|---:|
| El capítulo `02` entero | **98 KB** |
| Una regla | ~2 KB |

**No es un problema de cuánto pesa: es de qué contesta.** El volcado obliga a encontrar la relación uno mismo, que es exactamente lo que falla. La consulta la pone delante.

**Y hay una diferencia que decide:** el capítulo completo solo trae a los vecinos del mismo capítulo. De las cinco reglas que dependen de `F2`, **tres viven en otros capítulos** — `00·ID3`, `00·ID5` y `13·DOC3`. El volcado no las habría traído.

> El cambio del criterio se devolvió al usuario antes de tocar nada, porque por [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) la redacción del CA es la especificación, y una decisión tomada en un pendiente no puede cambiarla de costado.

---

## 4. El límite, escrito en un caso

**Una relación que nadie declaró no se encuentra.** `20·M17` se relaciona con `00·ID7` —las dos hablan de escribir para que se entienda— y **no sale**: esa relación solo se argumentó en el sello, nunca en el cuerpo de la regla.

**No es un defecto del programa: es el precio de que las relaciones se escriban a mano.** Y hace que [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) y [`20·M15`](../../../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) dejen de ser trámite: **son lo que hace la consulta posible.**

Está fijado en un caso de prueba para que se vea, en vez de descubrirse el día que algo no aparezca.

---

## 5. Lo que queda abierto · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**La marca de «ya avisé» vive en la carpeta temporal cuando el proyecto no tiene `.agente/`** — que es el caso del propio estándar, porque no se instala a sí mismo. Funciona, pero significa que al reiniciar la máquina el aviso vuelve. Se aceptó: repetirlo una vez cuesta menos que perderlo.

**Y no cubre el otro lado del choque:** que dos reglas digan cosas contrarias sin citarse. Eso solo lo ve quien lee.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | dos: la relación no declarada, y el choque entre reglas que no se citan |
| **Ciclos** | 1 |
