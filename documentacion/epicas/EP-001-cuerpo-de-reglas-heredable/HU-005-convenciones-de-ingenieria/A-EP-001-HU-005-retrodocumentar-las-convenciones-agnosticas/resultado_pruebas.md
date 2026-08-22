# Resultado de Pruebas — Fase A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |
| **Proyectos de prueba** | **AgroSystem** (Laravel + Livewire + Spatie, PHP sobre MariaDB) y **RNI** (Angular en el frente, Python en el fondo) |

---

## 1. Lo que había que verificar del plan antes de ejecutarlo

La fase anterior de esta jornada mostró que estos planes, escritos el 2026-08-17, traen la línea base envejecida. Se comprobó la de este antes de correr nada:

| Lo que el plan daba por cierto | Hoy |
|---|---|
| «La comprobación automática de la fila 5 no se puede correr» | **Falso.** `validar.py metareglas` existe desde el pendiente 53, y `_fila5_tecnologia` es justamente esa comprobación |
| «Los capítulos opt-in son del `15` al `19`» | **Incompleto.** Hoy son siete: `15`, `16`, `17`, `18`, `19`, `21` y `22` |
| «El CA-01 se afirma por la forma de la regla, no porque alguien lo haya probado en dos proyectos» | **Cierto**, y es lo que esta fase viene a resolver |
| «Nadie revisó el cuerpo entero buscando el mismo tema en dos capítulos» | **Cierto** |

---

## 2. Ejecución caso por caso

### CA-01 · Una convención sirve igual en dos proyectos de lenguajes distintos

**La prueba no es de forma, es de uso.** Se tomó la misma regla de base y se miró qué escribió cada proyecto en su capa 3, en el mismo campo del mismo molde:

| Regla de base | AgroSystem (PHP · Laravel · MariaDB) | RNI (Angular · Python) |
|---|---|---|
| `14·EST2`, nombres de tabla | `snake_case` plural con prefijo `erp_`, máximo 40 caracteres por el límite de índices de MariaDB | Sin prefijo, **MAYÚSCULA**, español, plural: `ROLES`, `PERMISOS` |
| `14·EST2`, claves foráneas | sufijo `_id` | — |
| `14·EST2`, booleanos | prefijo `es_` o `requiere_` | — |
| `14·EST1`, organización de módulos | por módulos de Laravel | Fondo por capas (`routers`/`services`/`schemas`/`models`); frente por `features/` |
| `03·D1`, auditoría | columnas de auditoría del proyecto | `usuario_creacion`, `fecha_crea`, `usuario_modifica`, `fecha_modifica` |
| `04·S1`, permisos | Spatie | RBAC propio: `PermisosEnum` más `RBACMiddleware` |
| `08`, pruebas | herramientas de PHP | `pytest` en el fondo, Karma y Jasmine en el frente |
| `15`, registros inmutables | — | **No activado**, opt-in apagado el 2026-07-25 |

**Ninguna de esas reglas cambió para que cada proyecto pudiera cumplirla.** Lo que cambia son los valores que cada uno declara en `.agente/mapeo-nombres.md`, que es el mecanismo previsto.

**Y la otra mitad, la de forma, ahora sí se comprueba sola:** `python validadores/validar.py metareglas` corre `_fila5_tecnologia` sobre las 84 reglas y devuelve **sin incumplimientos**. Ninguna nombra lenguaje, framework, motor, nube ni herramienta.

**Resultado del criterio: Cumple.**

### CA-02 · Un tema no aparece en dos capítulos

Nadie había revisado el cuerpo entero. Se hizo con las palabras del título de cada regla, comparando solo pares de **capítulos distintos**:

- **84 reglas leídas.**
- **4 pares** con dos o más palabras significativas en común.
- De esos cuatro, **tres son temas distintos que comparten palabras**: `02·F23` con `13·DOC15` («historia», «usuario»), y `13·DOC10` con `20·M10` y con `20·M16` («regla», «registra», «proyecto»).
- **Uno era el mismo tema de verdad:** `02·F6` «persiste el trabajo y las decisiones» y `13·DOC1` «persiste el trabajo de cada unidad».

**Y ese ya estaba resuelto, de la forma que el estándar prescribe.** `02·F6` está **derogada desde la 4.0.0** y su cabecera dice a dónde se fue: *«Lo que exigía lo exige `13·DOC1`, dueño del tema documentación (`M2`)»*.

O sea que el único solape real del cuerpo se detectó y se cerró por derogación, sin borrar nada, que es lo que `M11` manda.

**Resultado del criterio: Cumple.**

### CA-03 · Una convención que solo sirve a cierto tipo de proyecto queda marcada como opcional

Siete capítulos llevan la marca opt-in en su cabecera: `15` registros inmutables, `16` cumplimiento y calidad, `17` interfaz, `18` despliegue e infraestructura, `19` observabilidad y operación, `21` automatización de procesos y `22` sistemas que aprenden de datos.

**Y la marca hace algo, no es decorativa:** RNI declara en su capa 3 que el `15` está **no activado, opt-in apagado el 2026-07-25**. Un proyecto real lo apagó y lo dejó escrito con su fecha.

**Resultado del criterio: Cumple.**

---

## 3. Verificaciones manuales

Los dos proyectos se leyeron en su máquina, en las rutas que declara el registro. No se escribió nada en ninguno de los dos: esta fase solo lee, y escribir en un proyecto real está prohibido por la decisión 35 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md).

---

## 4. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | Baja | El plan daba por incorrible la comprobación de la fila 5, construida cinco días antes | **Cerrado** al comprobarlo |
| D-02 | Baja | El plan lista cinco capítulos opt-in; hoy son siete | **Cerrado**, anotado arriba |
| D-03 | Media | El barrido de solapes se hizo por las palabras del título, no por lo que cada regla exige. Encuentra el mismo tema con nombres parecidos; no encontraría el mismo tema con nombres distintos | **Abierto**, y se dice para que nadie lea el «Cumple» del CA-02 como más de lo que es |

---

## 5. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01 | La misma regla cumplida con valores distintos en dos stacks, más las 84 reglas sin una sola tecnología nombrada | Cumple |
| CA-02 | Barrido de las 84 reglas por pares de capítulos distintos: 4 candidatos, 1 real, ya derogado hacia su dueño | Cumple |
| CA-03 | Siete capítulos marcados, y uno apagado de verdad por un proyecto real | Cumple |

## 5.1 Lo que el plan exigía

Se cumplió, con dos cosas que el plan no podía saber: la comprobación de la fila 5 ya existía, y los capítulos opt-in son siete y no cinco.

**Lo que este resultado no dice** está en el D-03: el barrido de solapes mira nombres, no exigencias. Dos reglas que exijan lo mismo con títulos distintos se le escapan. Se deja escrito porque un «Cumple» que se lea de más es peor que un «No cumple».

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios quedaron verdes con evidencia de dos proyectos reales de stacks distintos, y el único solape de tema que existe en el cuerpo ya estaba cerrado por derogación. El alcance de lo comprobado en el CA-02 queda declarado en §5.1.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Las capas 3 de los dos proyectos | `.agente/mapeo-nombres.md` de AgroSystem y de RNI |
| EV-02 | Ninguna regla nombra tecnología | `python validadores/validar.py metareglas` |
| EV-03 | El barrido de solapes | §2, CA-02 |
| EV-04 | La derogación del único solape real | `base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md` |

---

## 8. Ciclos anteriores

Ninguno: la fase estaba aprobada desde el 2026-08-17 y nunca se había ejecutado.
