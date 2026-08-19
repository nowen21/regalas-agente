# 10 · Dependencias de terceros  ·  `[CAPA 2]`

Cada dependencia es código ajeno que heredas: sus bugs, vulnerabilidades, mantenimiento y licencia. La capa 3 declara el gestor de paquetes y las herramientas de auditoría.

---

## DEP1 · Agregar una dependencia es una decisión

Antes de sumar una librería: ¿la necesito o lo resuelvo con lo que ya tengo? ¿Está **mantenida** y es confiable? ¿Su **licencia** es compatible? ¿Cuánto **peso** y cuántas transitivas arrastra? Es una decisión funcional: el agente la **propone**, no la mete por su cuenta ([`01·C4`](01-conducta.md#c4--no-decidas-por-tu-cuenta)).

```
INCORRECTO: sumar una librería pesada para formatear una fecha en un solo lugar
CORRECTO:   resolverlo con la utilidad estándar
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

El análisis del 2026-08-07 en [analisis/base-2026-08-07-cumplimiento-meta-reglas.md](../analisis/base-2026-08-07-cumplimiento-meta-reglas.md) ya la daba por cumplida, y se revisó fila por fila antes de sellar. Coincide.

La fila **9** pasa aunque el cuerpo haga cuatro preguntas —necesidad, mantenimiento, licencia, peso—: no son cuatro exigencias sino **el contenido de la decisión** que la regla pide tomar antes de sumar la librería. La exigencia es una: que la decisión se tome y se proponga.

La remisión a [`01·C4`](01-conducta.md#c4--no-decidas-por-tu-cuenta) dice **quién** decide, y eso es una razón, no una de las tres dependencias de [`20·M7`](20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md). Las filas **14 a 16** son N/A.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DEP2 · Versiones fijadas y reproducibles

Fija versiones con el **lockfile** del ecosistema y **versiónalo**: todos (y producción) instalan lo mismo. No dependas de "la última" flotante. Actualiza **deliberado**, revisando cambios.

```
INCORRECTO: no versionar el lockfile → cada máquina instala versiones distintas
CORRECTO:   versionarlo → instalación idéntica en todos lados
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía ya en el análisis del 2026-08-07 y sigue cumpliendo. Está clasificada y con validador escrito —`dependencias.py`—, así que la fila **18** pasa con programa detrás y no solo con el registro.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DEP3 · Audita vulnerabilidades y mantén al día

Revisa **vulnerabilidades conocidas** con la herramienta del ecosistema. No dejes una dependencia con vulnerabilidades sin resolver. Quedarse muy atrás vuelve caro e inseguro actualizar después.

```
INCORRECTO: la auditoría reporta una vulnerabilidad alta y se anota «para la
            próxima», porque actualizar rompe dos pruebas
CORRECTO:   se arreglan las dos pruebas y se actualiza; si de verdad no se
            puede, queda escrito qué la mitiga y hasta cuándo
```

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ❌ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 16 ✅ · 1 ❌ · 3 N/A.**

**Fila 11 · sin texto prestado.** «Revisa vulnerabilidades conocidas con la herramienta del ecosistema» es [`04·S7`](04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas----derogada-en-23170--ver-10dep3) dicha otra vez. La enlaza **y** la repite, y la fila pide enlazar **en vez de** copiar.

**Y el arreglo no está acá.** El análisis del 2026-08-07 fue explícito: *«duplica `04·S7`; **`DEP3` es el dueño correcto**»*. Una vulnerabilidad de una dependencia es un asunto de dependencias, y el capítulo `04` la trata de prestado. Lo que corresponde es **derogar `04·S7`** y que este capítulo reciba el tema — no recortar `DEP3` para que deje de parecerse.

Eso es un cambio en **otro capítulo**, y va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**La fila 12 reprobaba también y se corrigió en esta pasada:** no tenía ejemplo. El que se agregó es el error de verdad —anotar «para la próxima» porque actualizar rompe dos pruebas—, y **no cambia qué exige la regla**.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DEP4 · No versiones lo instalado

Las dependencias instaladas (carpetas de paquetes, binarios) no van al control de versiones ([`09·G3`](09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado)): se reconstruyen del manifiesto + lockfile. Versiona la **declaración**, no el **resultado**.

```
INCORRECTO: commitear la carpeta de dependencias instaladas
CORRECTO:   versionar manifiesto + lockfile; ignorar la carpeta instalada
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía ya en el análisis del 2026-08-07.

La fila **11** pasa aunque nombre a [`09·G3`](09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado): `G3` dice qué no se versiona en general y esta dice **qué se versiona en su lugar** —la declaración, no el resultado—. Es la parte propia, no una copia. La misma distinción que salva a [`11·CFG2`](11-configuracion-entornos.md#cfg2--el-entorno-real-no-se-versiona-sí-una-plantilla) y que hunde a `DEP3`.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## DEP5 · Aísla la dependencia que puede cambiar

Una dependencia central y sustituible (cliente de pago, proveedor de correo) se **encapsula** detrás de una interfaz propia, en vez de esparcir llamadas directas. Cambiar de proveedor toca un punto, no cien. No lo sobre-apliques a utilidades estables y ubicuas.

```
INCORRECTO: el cliente del proveedor de correo llamado desde quince sitios;
            cambiar de proveedor toca los quince
CORRECTO:   un envío propio por delante; cambiar de proveedor toca ese
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. **No cambia qué exige la regla.**

La fila **9** pasa: el «no lo sobre-apliques a utilidades estables» no es una segunda exigencia sino **el límite** de la primera. Una regla que dice cuándo aplicarse y no dice cuándo no, se aplica a todo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `04` S7 (vulnerabilidades), `09` G3 (no versionar lo instalado), `01` C4 (se consulta), `11` (instalación reproducible).
