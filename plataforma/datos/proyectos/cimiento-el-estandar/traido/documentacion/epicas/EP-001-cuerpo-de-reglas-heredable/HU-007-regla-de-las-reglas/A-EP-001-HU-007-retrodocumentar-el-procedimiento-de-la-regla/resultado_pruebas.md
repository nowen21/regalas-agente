# Resultado de Pruebas — Fase A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Ejecución caso por caso

### CA-01 · Una regla nueva se enruta al capítulo correcto

[`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) y [`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md) lo exigen, y la fila 1 del checklist lo comprueba.

**Caso real de hoy:** la decisión 6 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) enrutó «quién sube la versión» al capítulo `02` y no al `09`, con el motivo escrito: es un paso del flujo, no del control de versiones.

**Resultado del criterio: Cumple.**

### CA-02 · Una regla atada a un stack no entra

[`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) lo exige, y **se comprueba sola**: `_fila5_tecnologia` de `metareglas.py` recorre las reglas buscando nombres de lenguaje, framework, motor, nube o herramienta.

Corrido el 2026-08-22 sobre el cuerpo entero: **sin incumplimientos**. Y la [fase A de HU-005](../../HU-005-convenciones-de-ingenieria/A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas/resultado_pruebas.md) lo confirmó por el otro lado, mostrando la misma regla cumplida en dos stacks opuestos.

**Resultado del criterio: Cumple**, y con comprobación automática.

### CA-03 · Una regla que exige dos cosas se parte antes de entrar

[`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) pide **una sola exigencia** por regla, y el checklist lo mira.

**Caso real:** las reglas `F4.1` a `F4.5` existen justamente porque `F4` se partió. Los identificadores con punto son la huella del criterio aplicándose.

**Resultado del criterio: Cumple.**

### CA-04 · Se sabe qué reglas llevan más tiempo sin que nadie las revise

Existe el programa: `validar.py vigencia`. Corrido hoy:

```
[AVISO] base — 249 de 249 reglas no dicen cuándo se revisó si siguen sirviendo
        Las del sello más antiguo: F4.1, F4.2, F4.3, F4.4, F4.5
```

**Sabe ordenarlas, y no tiene qué ordenar.** El sello que las 249 llevan responde por **la forma** —que la regla cumple su molde— y no por si el problema que evita todavía existe. O sea que la respuesta a «cuáles llevan más tiempo sin revisar» es hoy «las 249, todas por igual».

**Resultado del criterio: No cumple.** El programa está; el dato que necesita, no.

### CA-05 · Una regla validable no se automatiza hasta que se sepa que sirve

[`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) obliga a responder si un script puede decir sí o no sin opinar, y [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) guarda la respuesta de las 175: ~54 ya son validadores, ~22 validables pendientes, ~99 criterio humano.

**Y esta jornada dio el caso de por qué el criterio importa:** dos veces se escribió una comprobación y hubo que rehacerla porque reprobaba lo que estaba bien. La primera reprobó [`planteamiento.md`](../../../../../planteamiento.md); la segunda, 110 planes de pruebas. Las dos se corrigieron **antes** de dejarlas, midiendo.

**Resultado del criterio: Cumple.**

### CA-06 · Lo que se pidió dos veces no se pierde entre sesiones

[`01·C10`](../../../../../base/01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla) lo exige, y existe el molde [`plantillas/candidatas-a-regla.md`](../../../../../plantillas/candidatas-a-regla.md) donde se anotan.

**Resultado del criterio: Cumple.**

---

## 2. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Alta** | El sello de una regla responde por su forma, no por si sigue haciendo falta. `vigencia` sabe ordenar por antigüedad y las 249 tienen la misma antigüedad de revisión: ninguna. El CA-04 no se puede cumplir hasta que exista un sello de **utilidad**, distinto del de forma | **Abierto** |
| D-02 | Baja | El conteo de `reglas-validables.md` va con `~` y nadie comprueba que cuadre. Ya anotado en la fase de EP-004 · HU-001 | **Abierto**, ya reportado allá |

---

## 3. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, se enruta al capítulo correcto | `M13`, `M2`, fila 1 del checklist, y la decisión 6 de hoy | Cumple |
| CA-02, una regla atada a un stack no entra | `M3` con comprobación automática, corrida limpia | Cumple |
| CA-03, la que exige dos cosas se parte | `M5`, y las cinco `F4.n` como huella | Cumple |
| CA-04, se sabe cuáles llevan más sin revisar | `validar.py vigencia`: 249 de 249 sin dato | **No cumple** |
| CA-05, no se automatiza hasta saber que sirve | `M9`, las 175 clasificadas, y dos comprobaciones corregidas hoy antes de dejarlas | Cumple |
| CA-06, lo pedido dos veces no se pierde | `01·C10` y su molde | Cumple |

---

## 4. Veredicto de la fase

**Concepto:** No cumple.

**Justificación:** cinco de seis criterios cumplen, con reglas propias y en dos casos con comprobación automática. El CA-04 no: el programa que debería responderlo está construido y **no tiene con qué responder**, porque el único sello que llevan las reglas dice si cumplen su molde, no si el problema que evitaban sigue existiendo.

**Qué falta para que cumpla:** decidir si el sello de vigencia es un dato aparte del de forma, y si lo es, cómo se llena. Es decisión del usuario y no la toma esta fase.

---

## 5. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El enrutado y el molde | `20·M13`, `20·M2`, `20·M5` y el checklist |
| EV-02 | La agnosia comprobada sola | `validar.py metareglas`, limpio |
| EV-03 | Las 249 sin sello de utilidad | `validar.py vigencia` |
| EV-04 | Las 175 clasificadas | `validadores/reglas-validables.md` |

---

## 6. Ciclos anteriores

Ninguno.
