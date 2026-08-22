# 14 · Estructura del código y nomenclatura  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-027](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-027-el-capitulo-14-estructura-del-codigo-y-nomenclatura/HU-027-el-capitulo-14-estructura-del-codigo-y-nomenclatura.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

Dónde vive cada archivo y cómo se nombra, para que cualquiera lo encuentre donde espera. La capa 3 declara los nombres concretos (namespaces, prefijos, convenciones del lenguaje).

---

## EST1 · Organiza el código nuevo por módulo, en ubicación predecible

Cada elemento nuevo (modelo, componente, servicio, prueba, vista) vive en una ubicación **predecible** según su módulo y tipo. Todo el módulo en un lugar, no disperso.
Así: se localiza cualquier archivo por convención; borrar un módulo es borrar una carpeta; un dev nuevo abre la carpeta y ve el dominio de un vistazo.

```
INCORRECTO: archivos de un módulo dispersos por carpetas globales según tipo
CORRECTO:   el módulo agrupado en una ubicación predecible
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.3.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

La fila **5** pasa aunque el cuerpo nombre «modelo, componente, servicio, prueba, vista»: son tipos de elemento, no tecnología. Ningún lenguaje, motor ni herramienta aparece.

La fila **10** pasa raspando —317 caracteres de 320—. Queda dicho para que quien la edite sepa que no hay margen.

Las **14 a 16** son N/A: no declara dependencia en ninguna de las tres formas de [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), así que la 15 tampoco aplica, y no tiene excepción.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## EST2 · Nomenclatura consistente

**Una sola convención por tipo de elemento** —tablas, columnas, clases, archivos, permisos—, aplicada igual en todos: eso hace que el nombre se **adivine** sin buscarlo. Cortos, con significado por contexto, sin repetir lo que la ubicación ya dice.

```
INCORRECTO: booleano "es_socio_principal_del_grupo_familiar"
CORRECTO:   "es_principal" — el contexto de la tabla ya aclara

INCORRECTO: dejar autogenerar el índice en una tabla de nombre largo → excede el límite
CORRECTO:   pasar un nombre corto y explícito
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Mirada el 2026-08-18 para partirla, y no hizo falta: sobraba, no faltaba.** Lo que la hacía parecer dos reglas era el consejo sobre los **límites de longitud del motor** —que además nombraba tecnología, lo que [`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no admite en la base—. **No era una exigencia: era una advertencia práctica**, y se fue.

**Lo que queda es una sola cosa:** una convención por tipo, aplicada igual. Los nombres cortos y sin repetir la ubicación no son otra exigencia — son **cómo se ve** que la convención está bien elegida.

Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**Reprueba tres filas seguidas, y las tres dicen lo mismo: son tres reglas metidas en una.**

- **Fila 9 · una sola exigencia.** Hay tres, y se pueden cumplir por separado, que es la prueba que la fila propone: *(a)* una sola convención por tipo de elemento, *(b)* nombres cortos con significado por contexto, *(c)* respetar los límites de longitud del motor. Un proyecto puede tener la primera impecable y la tercera no.
- **Fila 10 · cuerpo de 1 a 4 líneas.** Mide **398 caracteres** y el molde da 320. No cabe porque son tres.
- **Fila 8 · el título manda.** «Nomenclatura consistente» no es imperativo, y no puede serlo mientras cubra tres exigencias distintas. Las otras dos del capítulo sí lo son: *Organiza...*, *Respeta...*.

**Partirla es un cambio de regla y no se hace acá.** Va al [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), y no es solo redacción: dos IDs nuevos, y [validadores/reglas-validables.md](../validadores/reglas-validables.md) ya la cita partida en dos —`14·EST2` (longitud) y `14·EST2` (resto)—, señal de que el corte llevaba tiempo pidiéndose.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## EST3 · Respeta el legacy — la convención es para lo nuevo

Las convenciones aplican a lo **nuevo**. El código existente que no las sigue **no se renombra ni se mueve** solo para ordenar: sale del alcance ([`01·C3`](01-conducta.md#c3--quédate-en-tu-tarea)). Migrar legacy es tarea **propia y acordada**, no efecto colateral.

```
INCORRECTO: mover y renombrar legacy "de paso" mientras hago otra cosa
CORRECTO:   crear lo nuevo con la convención; dejar el legacy intacto salvo tarea explícita
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.3.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se recortó en esta misma pasada**, quitando dos motivos del porqué («rompe referencias, infla el diff») y dejando el que delimita: sale del alcance. No cambia qué exige la regla.

Reprobaba **por tres caracteres** —323 de 320— con la medida de entonces, que cobraba el marcado de los enlaces. Desde el 2026-08-18 se mide lo que se lee y el cuerpo cuenta **222**: habría pasado sin tocarla. El recorte se queda igual, porque lo que se quitó era porqué y el porqué no va en la regla.

La fila **14** es N/A y conviene decir por qué: la regla nombra a [`01·C3`](01-conducta.md#c3--quédate-en-tu-tarea) como el motivo de que mover legacy salga del alcance. Eso es una razón, no una de las tres dependencias que [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) admite.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `01` C3 (alcance), `07` Q1/Q2 (imitar al vecino, nombres claros), `03` D1 (tablas/columnas), `13` (migrar legacy es tarea documentada).
