# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo.

---

## 2.0.0 — 2026-08-07

**MAYOR** · `⚠ obliga a migrar`. Un proyecto al día tiene que correr el instalador **una vez**.

Nada de lo que un proyecto hereda del estándar puede quedarse viejo. Antes se intentaba detectar comparando títulos de sección y fechas de archivo, y las dos cosas fallan: un paso nuevo **dentro** de una sección que ya existía no cambia ningún título, y la fecha miente en cuanto alguien clona el repositorio o edita el archivo por cualquier motivo.

- **El sello.** `CLAUDE.md`, `historico-chat/README.md` y `.agente/stack-instalacion.md` llevan al final `<!-- huella: … · estandar X.Y.Z -->` con la huella de **la plantilla contra la que se sincronizaron** —no la del archivo local, que cada proyecto llena con lo suyo—. Cualquier cambio de la plantilla rompe la coincidencia, venga por dentro o por fuera del documento.
- **Quedar viejo reprueba.** Era AVISO y el componente pasaba igual: un proyecto con el `CLAUDE.md` viejo figuraba como instalación completa.
- **El registro.** Cada actualización deja un `.md` en `documentacion/versiones/`: desde cuándo el proyecto usa esa versión, qué componentes se actualizaron con su huella antes y después, qué aplicó el instalador y qué quedó pendiente. Va en `documentacion/` y no en `.agente/` porque `.agente/` está en el `.gitignore`, y saber bajo qué versión cerró cada fase tiene que poder mirarse desde cualquier copia del repositorio. Componente nuevo del stack: `versiones`.
- **El número de versión deja de reprobar.** Al proyecto no le interesan todos los cambios del estándar, solo los que tiene que aplicar: que declare `1.8.0` con el central en `2.0.0` no obliga a nada por sí solo, y dejarlo en rojo por eso es ruido que enseña a ignorar la alerta. El desfase se informa al margen; `version` ahora solo exige que la versión adoptada esté **declarada**, porque sin ella no hay con qué sellar una fase cerrada.

**Cómo se migra** — la línea de siempre, la del paso 6:

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

Deja los sellos puestos y escribe el primer registro. Hasta que se corra, `claude-md`, `historico` y `stack-instalacion` salen en rojo: no porque el proyecto esté mal, sino porque todavía no declara contra qué versión se sincronizó.

Detrás: `validadores/versiones.py` (nuevo — sellos, comparación y registro), `checklist.py`, `instalar.py`, `validar.py versiones` para verlo a mano, y 19 pruebas nuevas (180 en total).

## 1.6.0 — 2026-08-07

**MENOR.** Ningún proyecto que herede el estándar tiene que hacer nada: la exigencia nueva recae sobre quien escribe reglas **del estándar**.

**El checklist respondido queda dentro del capítulo, en dos piezas.** En 1.5.0 la sección decía lo contrario —que no se persistía copia por regla, para no inflar `base/`—. Se cambia por una razón que pesa más: **que una auditoría posterior no vuelva a analizar lo ya verificado**. La regla cuyo sello dice `CUMPLE` contra la versión vigente se salta; el trabajo se concentra en las que no lo traen o lo traen anulado. Sin esto, cada auditoría reevalúa el catálogo entero desde cero.

Dos piezas, y cada una donde sirve:

1. **El instrumento — `base/20-meta-reglas/checklist.md`, archivo nuevo.** El checklist **es estándar**, así que vive con las meta-reglas, al lado de su `base.md` y como fuente única (`M2`): las 20 filas con su meta-regla y su criterio de aprobado, cómo se decide el resultado, el molde de cómo se aplica, la regla de caducidad, y qué filas puede decidir un script (once) y cuáles piden leer la regla (nueve).
2. **La evaluación — dentro de cada regla.** Al final de su archivo, como `###`: el veredicto, contra qué versión y en qué fecha, el resultado por bloque, las `N/A` justificadas, y **el enlace al instrumento** — para que quien abra una regla suelta sepa de dónde sale esa evaluación. No repite las 20 filas (`M5`).

- `base/20-meta-reglas/base.md` — la sección del checklist queda en resumen + enlace, como ya hacen `F12` y `F13` con sus fuentes únicas.
- `base/00-identidad-y-rol/reglas/` — las seis reglas quedan evaluadas: 16 ✅ · 0 ❌ · 4 N/A · **CUMPLE**.
- `base/00-identidad-y-rol/base.md` — el capítulo lo dice y enlaza el instrumento.

**Backlog que esto abre:** las otras 164 reglas de `base/` quedan **sin sellar**. No es incumplimiento retroactivo —`M10` dice que un cambio de norma no reabre lo cerrado— pero sí es la cola de trabajo: hasta que una regla se selle, sigue entrando en cada auditoría. Se salda por capítulos, no de una vez.

## 1.5.1 — 2026-08-07

**PARCHE** (redacción y una justificación que había quedado falsa; no cambia qué se exige).

Se aplicó el checklist recién agregado a las seis reglas de `00 · Identidad y rol`. **En la primera pasada ninguna cumplía.** El resultado quedó dentro de cada regla, en [`base/00-identidad-y-rol/reglas/`](base/00-identidad-y-rol/reglas/).

- `base/20-meta-reglas/base.md` — la tabla de `M1` describía el preámbulo como *"No: describe, no exige"*. Desde que el capítulo tiene reglas (`ID1`–`ID6`, v1.4.0) esa frase era falsa, y las seis reglas chocaban con `M1` — la fila 17 del checklist. La columna es **¿Se ajusta?**: la respuesta sigue siendo **No** y la precedencia no cambia; lo que se corrigió es la justificación, que ahora dice *"un proyecto no redefine quién es el agente ni el molde de las reglas"*.
- `base/00-identidad-y-rol/reglas/` — `ID1` y `ID6` repetían texto de `01·C14` y de `20·M1` además de enlazarlo (fila 11, `M5` sin texto prestado): ahora difieren en vez de reformular. `ID1`–`ID4` pasaron de tercera persona descriptiva a presente imperativo, que es lo que pide `M5`. `ID5` gana el enlace a `00·N2`, de donde sale que la autorización sea de un solo uso.

Sigue disponible, y es decisión pendiente del usuario, la otra vía para el choque: que el capítulo deje de ser preámbulo y pase a **capa 2**. Eso sí movería la precedencia, y por eso no se tomó por cuenta propia.

## 1.5.0 — 2026-08-07

**MENOR** (aditivo: agrega una comprobación, no cambia ninguna exigencia existente).

- `base/20-meta-reglas/base.md` — sección nueva **«Checklist de la regla — qué cumple y qué no»**, entre el procedimiento de alta y la higiene del conjunto. Veinte filas agrupadas en cinco bloques (dónde va · cómo se identifica · cómo está escrita · cómo se relaciona · qué obliga fuera de su texto), cada una con su meta-regla y su criterio de aprobado, y un resultado al final que dice **CUMPLE** o **NO CUMPLE**.

El criterio de resultado es binario a propósito: una sola fila en ❌ y la regla no se publica. No hay "cumple parcial" — una regla a medias es la que después nadie sabe si rige. Solo cuatro filas admiten `N/A` (ejemplo, dependencias, ciclos y excepción), y siempre con motivo escrito.

Por qué ahí y no en `estructura-regla.md`: el checklist verifica `M1`–`M13` completas, y el anexo solo desarrolla `M5`. Además no cabía dentro de `M5`, que exige cuerpo de una a cuatro líneas.

La sección deja anotado cuáles de las veinte filas puede decidir un script solo (once) y cuáles piden leer la regla (nueve). Esa división es la especificación del validador de meta-reglas que falta.

## 1.4.0 — 2026-08-07

**MENOR** (aditivo: reglas nuevas en un capítulo que no las tenía; nada de lo que ya se cumplía deja de valer).

El capítulo del preámbulo se ajusta al capítulo 20: deja de ser prosa y pasa a tener reglas con identificador.

- `base/00-identidad-y-rol/reglas/` — seis reglas nuevas, **una por archivo**, nombradas `<PREFIJO><n>-<título>`: `ID1` criterio de desarrollador senior · `ID2` registro técnico sin adornos · `ID3` qué cuenta como entregado · `ID4` el ciclo completo de entender a documentar · `ID5` el borde del rol (seis cosas fuera por definición) · `ID6` los roles por etapa no cambian la precedencia.
- `base/00-identidad-y-rol/base.md` — pasa a ser el capítulo con el índice enlazado a las seis. El texto que antes era prosa suelta queda repartido en las reglas; lo que ya decía otro capítulo se enlaza en vez de repetirse (`20·M5`).
- `base/20-meta-reglas/estructura-regla.md` — el prefijo **`ID`** se registra en la tabla de letras ocupadas, como exige `M4` antes de estrenar un prefijo.
- `validadores/reglas-validables.md` — `ID1`–`ID6` clasificadas (criterio humano, `M9`). `ID3` se anota como caso parcial: sus cuatro condiciones ya se validan por separado; lo que no se valida es la conjunción.

Con esto queda cerrada la primera mitad del hallazgo **H-22** del informe de `analisis/`: el capítulo que `02·F0` citaba como fuente de reglas ya tiene reglas citables. Sigue abierto que el número `00` esté compartido con el núcleo.

## 1.3.1 — 2026-08-07

**PARCHE** (no cambia qué se exige; solo dónde vive el texto).

- `base/00-identidad-y-rol.md` pasa a `base/00-identidad-y-rol/base.md`. El capítulo del preámbulo queda con carpeta propia, como `20-meta-reglas/`, para poder crecer con anexos sin inflar el archivo que se carga en cada turno. El texto no cambió.

Detrás: `validadores/cargador.py` decidía qué se carga **literal en todos los turnos** por el nombre del archivo (`00-`, `01-`). Con el capítulo en carpeta, el nombre pasa a ser `base.md` y la identidad del agente habría caído al índice — es decir, el agente arrancaría sin saber quién es. Ahora la comprobación mira el **primer tramo de la ruta**, así que un capítulo del núcleo carga igual viva en archivo suelto o en carpeta.

## 1.3.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). El histórico de sesiones deja de depender de que el agente se acuerde de escribirlo:

- Plantilla nueva: `historico-chat.md` — el `README.md` de la carpeta `historico-chat/` de cada proyecto.
- `CLAUDE.md.plantilla`: punto **2.3** (la carpeta, quién la escribe, se versiona, y cómo excluirla si el chat maneja datos sensibles) y punto **6** ampliado: el instalador es el camino por el que **toda** herramienta nueva del estándar llega al proyecto, sin pasos manuales. Si algo exige configurar a mano, es defecto del estándar.

Detrás: `validadores/hook_historico.py` (enganches `UserPromptSubmit` y `Stop`) e `instalar.py`, que los deja puestos y crea la carpeta. Un proyecto al día no tiene que hacer nada: los recibe la próxima vez que corra el paso 6.

Y el **stack de instalación**: la lista de todo lo que un proyecto debe tener para que el agente esté completo.

- Plantilla nueva: `stack-instalacion.md` — los 11 componentes, qué es cada uno y cómo se instala. Se copia a `./.agente/` de cada proyecto, sellada con la huella del original: si el estándar agrega un componente, la copia deja de coincidir y eso se reporta como actualización pendiente.
- `CLAUDE.md.plantilla`: punto **2.1** (los dos archivos que el estándar escribe en `.agente/` y no se editan a mano) y paso **8** — mientras exista `.agente/INSTALACION-INCOMPLETA.md`, el agente no está completo y debe decir qué falta en cada respuesta. No bloquea: el único gate sigue siendo `F13`.

Detrás: `validadores/checklist.py` (la comprobación de cada componente; la lista se lee de la plantilla, no se duplica en código), `hook_checklist.py` en `UserPromptSubmit`, y `validar.py checklist --raiz` para verlo a mano.

## 1.2.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Un capítulo de **preámbulo**:

- `00 · Meta-reglas` — la regla de reglas: jerarquía de cuatro niveles, organización por dominio con fuente única, orden determinista de desempate ante conflicto, formato canónico de una regla, ID estable, dependencias declaradas (`extiende` / `depende de` / `deroga`), excepciones escritas dentro de la regla, criterio de validable, versionamiento obligatorio, derogación en vez de borrado, y procedimiento para agregar una regla sin duplicar ni contradecir.

No cambia ninguna regla existente: **formaliza** las convenciones que la base ya usaba de hecho y cubre lo que no estaba escrito (desempate, dependencias, derogación, anti-duplicación).

## 1.1.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Dos capítulos **opt-in** de dominio DevOps:

- `18 · Despliegue e infraestructura` — despliegue como artefacto versionado, IaC, build-una-vez, config por entorno fuera del artefacto, release reversible, checklist de despliegue, health/readiness, y correr contra producción gateado por el usuario. Extiende `09·G6`.
- `19 · Observabilidad y operación` — logs estructurados, señales doradas + trazas, SLO/alertas como código sobre síntomas, runbooks, postmortem sin culpa. Extiende `05`.

Plantillas nuevas: `checklist-despliegue.md`, `postmortem.md`. Toggles en `CLAUDE.md.plantilla §5.1`.

## 1.0.0 — 2026-08-06

Primera versión sellada del estándar. Línea base: núcleo blindado (`00`), conducta y flujo (`01`–`02`), buenas prácticas (`03`–`17`), plantillas de capa 3, memoria por señales con vigencia y ciclo de deuda, y la capa de validadores automáticos + hooks.

A partir de aquí, cada cambio de `base/` o `plantillas/` suma una entrada con su tipo.
