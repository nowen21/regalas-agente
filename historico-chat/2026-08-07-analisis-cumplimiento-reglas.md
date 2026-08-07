# 2026-08-07 — Análisis de cumplimiento de todas las reglas contra `20-meta-reglas`

## Conversación

### 1 · Usuario — hora no registrada
> # Prompt
>
> Cree una carpeta llamada **`analisis`**. Dentro de ella, genere un documento en formato **Markdown (.md)** que contenga el análisis de todas las reglas existentes en el agente, tomando como referencia las reglas definidas en **`20-meta-reglas`**.
>
> ## Objetivo
>
> Validar que todas las reglas del agente cumplan con los estándares, principios y lineamientos establecidos en **`20-meta-reglas`**, identificando fortalezas, incumplimientos y oportunidades de mejora.
>
> ## Actividades
>
> * Analizar todas las reglas existentes en el agente.
> * Evaluar cada regla contra los criterios definidos en **`20-meta-reglas`**.
> * Verificar que cada regla cumpla con el estándar establecido.
> * Identificar reglas incompletas, ambiguas, redundantes o que no se ajusten al estándar.
> * Detectar inconsistencias entre reglas.
> * Identificar reglas que deban unificarse, dividirse, complementarse o eliminarse.
> * Proponer las mejoras necesarias para que todas las reglas sean consistentes con el modelo definido en **`20-meta-reglas`**.
>
> ## Para cada regla analizada indicar, como mínimo:
>
> * Nombre de la regla.
> * Ubicación.
> * Estado de cumplimiento.
> * Meta-regla(s) utilizada(s) para la validación.
> * Criterios evaluados.
> * Hallazgos encontrados.
> * Incumplimientos identificados.
> * Recomendaciones de mejora.
> * Prioridad de la corrección (Alta, Media o Baja).
>
> ## Entregable
>
> Generar un informe de análisis que sirva como evidencia del nivel de cumplimiento del estándar de reglas del agente y como plan de trabajo para corregir las desviaciones encontradas.
>
> El objetivo es que todas las reglas del agente mantengan una estructura homogénea, sean coherentes entre sí y cumplan completamente con los estándares definidos en **`20-meta-reglas`**.

**Agente** — 2026-08-07 08:46:20

Se leyeron los 23 archivos de norma de `base/` (capítulos 00–20, más las fuentes únicas `F12/base.md`, `F13/base.md` y el anexo `estructura-regla.md`), y se contrastaron contra `validadores/reglas-validables.md`, `CHANGELOG.md` y `VERSION`.

**Archivos creados:**

- `analisis/base-2026-08-07-cumplimiento-meta-reglas.md` — el informe.
- `analisis/README.md` — índice de la carpeta y nomenclatura (`<ámbito>-AAAA-MM-DD-<tema>.md`, el patrón de `13·DOC6`).

**Resultado del conteo:** 170 reglas (+13 subpartes `F12.N` = 183 identificadores).

| Estado | Reglas | % |
|---|---|---|
| ✅ Cumple | 48 | 28 % |
| 🟡 Cumple con observaciones | 69 | 41 % |
| ❌ Incumple | 53 | 31 % |

**Diagnóstico de fondo:** el estándar está bien diseñado y desigualmente aplicado. Las 13 meta-reglas cubren lo que tienen que cubrir; el problema es de fecha — el capítulo 20 nació en 1.3.0 y las 157 reglas anteriores nunca se revisaron contra él. Ninguno de los 22 hallazgos pone en duda **qué** exige el estándar: todos son de forma (dónde está escrito, cuántas veces, con qué molde, si un programa puede comprobarlo).

**Los cinco hallazgos que mandan:**

1. **`estructura-regla.md` diseca `F0`, publica la versión corregida completa, y nadie la aplicó.** `F0` sigue con sus 36 líneas, título nominal y excepción sin `autoriza`. Hoy conviven dos textos de `F0` y ninguno declara cuál manda — rompe `M2` en el peor sitio posible.
2. **Existe una cuarta forma de dependencia que `M7` no declara.** El bloque `**Encadenamiento:**` aparece 22 veces en 5 capítulos y es hoy la forma dominante. `M7` solo admite `extiende` / `depende de` / `deroga`. Como consecuencia, su prohibición de ciclos no es comprobable — y `F4.4`↔`F4.5` es un ciclo declarado en prosa.
3. **Cuatro reglas escondidas:** `CQ1`–`CQ4` usan `###`. `estructura-regla.md` nombra exactamente ese error: *"con tres, la regla se esconde: no sale en la lista y el programa que las revisa no la ve"*.
4. **`M8` se contradice con `N1`:** `M8` dice que las `[BLINDADA]` no admiten excepciones; `N1` es blindada y tiene una escrita. Por `M6` paso 6, eso es defecto del estándar y se reporta. El fondo es de vocabulario: `M8` no distingue *excepción* de *condición de autorización*, que es lo que las cuatro blindadas realmente declaran.
5. **`M9` incumplida para 27 reglas:** los capítulos 18, 19 y 20 no aparecen en `reglas-validables.md`, ni como validables ni como no validables.

**Segundo bloque, deuda estructural:** seis pares dicen lo mismo en dos capítulos — `F5`≡`T5` (ejemplo idéntico palabra por palabra), `F6`≡`DOC1`, `F7`≡`DOC3` (ejemplo idéntico), `S7`≡`DEP3`, `DP8`≡`OB6`, y `DOC11` repite entera la tabla de `DOC3` que dice extender.

**Un detalle que revela el método:** `estructura-regla.md` usa `[GATE DE ARRANQUE]` de `F13` como su ejemplo de "inventarse una etiqueta", y `F13` sigue con la marca. Igual que con `F0`: el diagnóstico estaba escrito, con la solución al lado, y el paso que faltó fue aplicarlo.

**Otros hallazgos** (los 22 están en §4 del informe): `base/` nombra tecnologías y rutas reales de un proyecto (`DOC14` con `GitHub`/`VSCode`/`documentacion/prompts/erp/...`, `S11` con `destroy()`/`SoftDeletes`, `D8` con código de un stack); el capítulo 16 se declara opt-in y su Parte A dice "siempre aplica", mientras Parte B prohíbe hardcodear el marco que `CQ3` y `CQ4` hardcodean; `DOC10` cita `P28` —regla de capa 3— desde capa 2, que es la dependencia hacia arriba que `M7` prohíbe; `C14` atribuye a `C1` un texto que `C1` no tiene; 34 reglas rompen "una sola exigencia" (cuatro se autodeclaran múltiples: `F4.5`, `S11`, `T7`, `G8`); `F4.3` tiene 78 líneas sin abrir subcarpeta; 13 de 15 excepciones no dicen quién autoriza; los capítulos 18 y 19 no tienen ni un solo ejemplo; hay 10 formas distintas de escribir la misma cita; el `CHANGELOG` registra el capítulo 20 como `00 · Meta-reglas`.

**Plan de corrección — 5 olas:**

| Ola | Qué | Versión |
|---|---|---|
| 1 | Arreglar las meta-reglas primero (`M8`, `M7`, `M5`, `M4`, `M2`, `M13`) | 1.3.1 PARCHE + 1.4.0 MENOR |
| 2 | Contradicciones y reglas escondidas (`CQ`, cap. 16, `F0`, `F13`, `C14`, `DOC10`) | 1.4.0 MENOR |
| 3 | Consolidar los duplicados — estrena `M11` (derogar, no borrar) | 2.0.0 MAYOR |
| 4 | Agnosticismo, partición de reglas múltiples, excepciones completas, títulos | 2.1.0 MENOR |
| 5 | `validadores/metareglas.py` — valida `M3`, `M4`, `M5`, `M7`, `M9` en seco sobre `base/` | 2.2.0 MENOR |

La Ola 1 va primero porque sin ella cada corrección posterior se hace contra una norma que se contradice. La Ola 5 es la que más importa a largo plazo: sin validador, este informe caduca en la próxima tanda de reglas — que es exactamente lo que `M9` previene cuando dice *"una regla validable que nadie valida es una regla que no se cumple"*.

**Dos decisiones quedaron para el usuario, sin tocar nada:**

1. **`F12`** — su archivo declara *"Texto literal del usuario, 2026-08-03. No se reescribe, no se resume y no se interpreta."* Esa congelación es decisión del usuario y se respeta, pero hoy es una excepción **no escrita** al molde, y `M8` dice que ante una excepción no escrita se pausa y se pregunta. Dos vías: (a) `M5` incorpora la figura de "texto congelado del usuario" con su condición, límite y quién autoriza; (b) las 13 partes se envuelven en el molde `## F12.N · …` **sin tocar una palabra del texto**.
2. **`estructura-regla.md`** — está escrito en registro coloquial (*"Dos gatitos, siempre dos"*, *"como el número de la camiseta"*), y la Higiene del capítulo 20 exige *"imperativo, corto, técnico y sin adornos"*, con `17·I4` reservando el registro sencillo al usuario final. Además `M13` manda los instructivos de mantenimiento del estándar a `CLAUDE.md`, y este archivo se autodescribe como instructivo. Dos vías: se queda en `base/20-meta-reglas/` y se reescribe en registro técnico, o se mueve y el registro coloquial queda legítimo. La segunda decisión condiciona a la primera.

No se ejecutó ninguna corrección: el pedido fue el informe.

### 2 · Usuario — hora no registrada
> cree carpeta de identidad-y-rol

**Agente** — 2026-08-07 09:23:46

Hecho, siguiendo el patrón que ya usa `20-meta-reglas/`: el capítulo entero pasa a su carpeta con `base.md` dentro.

```
base/00-identidad-y-rol.md  →  base/00-identidad-y-rol/base.md
```

Se movió con `git mv`, así que el historial del archivo se conserva. **El texto no cambió** — solo dónde vive.

**Riesgo detectado antes de mover, y arreglado.** `validadores/cargador.py` decidía qué reglas van **literales en cada turno** por el **nombre del archivo**:

```python
if os.path.basename(rel).startswith(NUCLEO):   # NUCLEO = ("00-", "01-")
```

Con el capítulo en carpeta, el nombre pasa a ser `base.md`, que no empieza por `00-`. La identidad habría caído al índice y el agente arrancaría **sin saber quién es**, en silencio y sin señal. Ahora la comprobación mira el **primer tramo de la ruta**:

```python
if rel.split("/")[0].startswith(NUCLEO):
```

Así un capítulo del núcleo carga igual viva en archivo suelto o en carpeta. Comprobado ejecutando el cargador: siguen literales `00-identidad-y-rol/base.md`, `00-nucleo-blindado.md` y `01-conducta.md`, y el resto (23 archivos) sigue solo en índice. La identidad ahora carga **primera**, antes del núcleo, que es el orden correcto: preámbulo antes que capa 1.

**Referencias actualizadas** (las tres que nombraban la ruta vieja):

- `README.md:43` — era un enlace markdown real; se habría roto.
- `base/20-meta-reglas/base.md:15` — la tabla de `M1` (dónde vive el preámbulo).
- `anatomia/mapa-del-sitio.md:40` — el árbol del repo.

Las menciones de `02-flujo-de-trabajo.md` (líneas 15, 16, 42) dicen `` `00-identidad` `` sin ruta ni enlace: siguen válidas. Aparte, el informe de la sesión anterior ya las marcó como hallazgo **H-22** — `F0` las cita en la columna "Dónde está la regla" de un capítulo que **no tiene ninguna regla con ID**. Eso no se tocó: es corrección de la Ola 2, no de este movimiento.

**Versionado** (`M10`, no opcional): `VERSION` 1.3.0 → **1.3.1**, entrada **PARCHE** en `CHANGELOG.md` — no cambia qué se exige, solo dónde vive el texto.

**Comprobación:** `python validadores/validar.py estandar` → `OK: sin incumplimientos`. En la primera corrida salió un enlace roto, pero era del informe de la sesión anterior (una línea que citaba como ejemplo el enlace a añadir en `M5`, con ruta relativa a `base/20-meta-reglas/`, no a `analisis/`); se reescribió para que apunte de verdad.

La carpeta queda con `base.md` solo. Si la idea es desarrollar el capítulo —darle reglas con ID, que hoy no tiene— los anexos entran al lado, como `estructura-regla.md` en `20-meta-reglas/`. Aviso de un efecto del cargador: **todo** `.md` que se ponga en esa carpeta se cargará literal en cada turno, porque el primer tramo empieza por `00-`. Para un anexo largo eso pesa; si se llega a ese caso, conviene decidir entonces si el anexo va ahí o fuera.

## Abierto

- Decisión del usuario sobre `F12` (texto congelado) y sobre `estructura-regla.md` (registro y ubicación). Hasta que responda, la Ola 2 queda incompleta.
- Aprobación para ejecutar las olas 1 y 2, que sí pueden arrancar sin esas dos respuestas.
- Qué contenido llevará `base/00-identidad-y-rol/` ahora que tiene carpeta: hoy es preámbulo sin reglas con ID, y `F0` lo cita como si las tuviera (H-22).
- **Sin subir:** el movimiento de `base/00-identidad-y-rol/`, el arreglo de `cargador.py` y sus referencias (`README.md`, `20-meta-reglas/base.md`, el árbol de `anatomia/`), más `CHANGELOG.md` y `VERSION` 1.3.1. El usuario pidió subir todo **menos** lo que dependa de los cambios en `base/`; ese conjunto queda en el árbol de trabajo esperando su turno.
