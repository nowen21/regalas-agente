# Qué reglas del estándar son validables

Auditoría regla por regla de `base/` para decidir cuáles se pueden convertir en **validadores automáticos**. Fecha: **2026-08-05**. Alimenta el pendiente [01 · validadores de código de proyecto](../pendientes/01-validadores-de-codigo-de-proyecto.md) y su contraparte [hecho](../pendientes/hecho/validadores-y-hooks.md). Es una foto: al agregar o cambiar reglas, se revisa.

## Criterio

> Si un script puede decir **sí/no sin opinar** → **validable**.
> Si dos personas pueden discutir si se cumplió → **se queda en el `.md`** (lo interpreta el agente).

Muchas reglas validables inspeccionan el **código/esquema/config del proyecto** o corren herramientas (linter, pruebas, audit de dependencias) → **necesitan un proyecto real con `proyectos/`**; no se pueden validar "en seco" sobre el estándar.

## Conteo

| Categoría | Cuántas |
|---|---|
| ✅ **Ya son validadores** | ~53 (se sumaron `20·M15` y `02·F12`, que ya estaban construidas y no figuraban) |
| 🟡 **Validables, faltan** | ~22 (4 fuzzy o pesadas: `F2`, `F18`, `DOC7`, `DOC14`; 5 necesitan que el proyecto declare su convención/dominio; **8 de los capítulos `18` y `19`, todas contra proyecto real**; `02·F4` y `09·G9`; `00·ID8` en seco y parcial; `20·M16` sobre el catálogo del proyecto; `02·F23` necesita que el pendiente cerrado declare su fase) |
| 🔴 **No validables** (criterio humano) | ~100 (se sumaron los 6 de conducta que faltaban por escribir uno a uno, y 6 de los capítulos `18` y `19`) |

> **Puesto al día el 2026-08-16**, en la fase `A-EP-001-HU-009`. Las 33 que el validador reportaba como sin clasificar bajaron a **cero**. Quince de ellas **ya estaban clasificadas** —el registro decía «C1–C17» y el programa no lee rangos—; las otras dieciocho no aparecían de verdad.

> Actualización 2026-08-07: el capítulo `02` pasó por el molde de `M5` y por el checklist. Ninguna regla `F` nació ni se derogó, así que este registro no cambia — pero los títulos sí: `F0` es ahora *"Recorre la cadena completa"*, `F3` *"Ejecuta seguido el plan aprobado"*, `F5` *"Corre solo las suites que la fase toca"*, `F13` *"Deja la estructura base puesta antes de trabajar"* (el título de esa nota quedó viejo: en la v5.0.0 la regla dejó de detener el arranque y pasó a dejar la estructura puesta; corregido el 2026-08-18). Los ID son los de siempre.
>
> Actualización 2026-08-05: se sumaron `F12.5` (consecutivo sin huecos) y, en `trazabilidad.py`, `DOC16` (enlace bidireccional épica↔HU), `DOC12` (ORIGEN en el plan) y `DOC3/DOC11` (tabla de cierre) — sobre el árbol `documentacion/epicas/`. Después, ya contra código real (agro-system), `04·S4` (`secretos.py`: secretos incrustados) y `10·DEP2` (`dependencias.py`: lockfile versionado).

---

## ✅ Ya son validadores (HECHAS)

| Regla | Validador | Comprueba |
|---|---|---|
| `G2` | `commits.py` | asunto con contenido, línea en blanco, idioma |
| `G3` | `versionado.py` | no versionar secretos/artefactos/config local (por nombre) |
| `04·S4` · `00·N6` | `secretos.py` | secretos incrustados en el código (claves, tokens, `password="…"`) |
| `10·DEP2` | `dependencias.py` | lockfile del ecosistema presente y versionado |
| `09·G4` | `rama.py` | rama dedicada (no la principal) y al día con ella |
| `03·D2` | `migraciones.py` | cada migración declara su reversión (multi-stack por detección) |
| `03·D1` (FK) · `03·D3` · `14·EST2` (longitud) | `esquema.py` | FK con política; `NOT NULL` nuevo sin default; identificador sobre el límite |
| `05·E1` · `05·E5` | `errores.py` | capturas de error vacías; secretos en logs (multi-lenguaje) |
| `06·R2` (`SELECT *`) · `06·R1` | `rendimiento.py` | traer solo lo necesario; consulta en bucle (N+1) |
| `04·S3` · `04·S5` | `seguridad.py` | concatenación SQL/shell; asignación masiva; flags de cookie |
| `07·Q3` | `calidad.py` | funciones demasiado largas |
| `08·T4` · `08·T3` | `aislamiento.py` | BD efímera; orden aleatorio; fuentes flaky |
| `09·G6` | `ci.py` | existe pipeline de CI que corre pruebas y linter |
| `10·DEP4` · `11·CFG2` | `versionado.py` | carpeta instalada no versionada; `.env` real ignorado + molde |
| `07·Q6` | `herramientas.py` (`linter`) | corre el linter/formateador del stack |
| `08·T5` | `herramientas.py` (`suite`) | corre la suite de pruebas del stack |
| `10·DEP3` · `04·S7` | `herramientas.py` (`audit`) | corre el audit de vulnerabilidades del stack (misma herramienta) |
| `G8` | `commits.py` | sin atribución de herramienta |
| `F13` | `sesion.py` | existe la carpeta `proyectos/` |
| `C18` | `sesion.py` | sync `CLAUDE.md` ↔ plantilla central |
| `C19` | `recuerdos.py` · `checklist.py` | la memoria vive en `historico-chat/memory/`; el almacén de la herramienta, vacío |
| `F12.1/2/3/4/5/6/7/11/12/13` | `fases.py` | jerarquía épica→HU→fase · id único · nomenclatura · consecutivo sin huecos · ruta física |
| `DOC16` · `DOC12` · `DOC3/DOC11` | `trazabilidad.py` | enlace bidireccional épica↔HU · ORIGEN en el plan · tabla de cierre |
| `F0` · `F14` · `F17` | `flujo.py` | cada fase tiene sus padres (épica/HU) · el plan trae las 13 preguntas · sin incertidumbre |
| [`02·F22`](../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) | `version.py` (`validar_fase`) · `flujo.py` | ninguna regla derogada entre la versión que el proyecto declara y la vigente; se cobra donde hay fases. Falta el filtro fino: si la derogada era una `*opt-in*` que el proyecto nunca encendió, hoy igual la cuenta |
| `DOC1` · `DOC8` · `DOC10` · `DOC13` · `DOC15` | `plantillas.py` | completitud contra su plantilla (cierre, análisis, reglas, catálogo, HU) |
| `DOC17` | `enlaces.py` | cada carpeta del árbol lleva su `README.md` y lista lo que cuelga de ella |
| [`13·DOC22`](../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) (existencia) | `resumen.py` · `hook_resumen.py` | el resumen existe, se mueve con la transcripción, y se avisa qué le falta |
| `16·CQ1` | `plantillas.py` | completitud de `marco-normativo.md` |
| `DOC14` (resolución de enlaces) | `enlaces.py` | enlaces `.md` resuelven |
| **completitud de plantillas** | `plantillas.py` | marcadores sin llenar, secciones ausentes |
| **enlaces/índices** | `enlaces.py` | enlaces rotos, índices desactualizados |

---

**Dos que ya estaban construidas y no figuraban** (agregadas el 2026-08-16):

| Regla | Validador | Comprueba |
|---|---|---|
| `20·M15` | `enlaces.py` | que toda cita a otra regla lleve su enlace; reporta «la cita X no lleva enlace» |
| `02·F12` | `fases.py` | la nomenclatura de la fase, que no se repita el consecutivo, que declare la épica y la historia donde está guardada, y su ruta física |

## 🟡 Validables, faltan (PENDIENTE)

> Casi todas requieren un **proyecto real con `proyectos/`** (marcado 🔶). Las "en seco" (sobre el estándar) son escasas.

### Flujo y trazabilidad (`02`, `13·DOC`)

| Regla | Qué comprobaría el script | Por qué falta |
|---|---|---|
| `F2` | ¿código de fase sin especificación referenciado? | cruzar el código con su especificación; es el más pesado |
| `F18` | cada intervención del plan referencia un CA | mapear intervención→CA dentro del plan (fuzzy) |
| [`02·F21`](../base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) | que un archivo nuevo no traiga un incumplimiento que ya está anotado en `pendientes/` | necesita saber qué comprueba cada pendiente; hoy eso está en prosa |
| [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) | que todo pendiente marcado hecho nombre la HU y la fase donde se construyó | el pendiente cerrado no declara esa referencia en un sitio fijo; hay que fijarlo en la plantilla del pendiente antes de poder leerlo |
| `DOC7` | cruce bidireccional A↔B en §Historial cruzado | narrativa de complemento entre fases (fuzzy) |
| `DOC14` (formato) | link de 2 partes: texto=ruta absoluta | forzarlo marca los links de texto descriptivo (alto FP) |
| [`13·DOC19`](../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) | toda plantilla marca sus huecos `«…»` y ninguna usa otra marca | se valida en seco sobre `plantillas/`; lo construye EP-004 |
| [`13·DOC20`](../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) | un documento entregado no conserva ningún `«…»` | necesita saber qué documento se da por terminado, y eso hoy no está declarado |
| [`13·DOC21`](../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) | ninguna sección de un documento queda con su marca puesta en vez de `N/A` | va con [`13·DOC20`](../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md): el mismo recorrido distingue hueco sin llenar de sección no aplicable |
| [`13·DOC22`](../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) (contenido) | que el resumen traiga hallazgos de verdad y no solo el molde | reconocer un hallazgo es criterio; el programa solo ve si hay alguno |
| [`13·DOC23`](../base/13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md) (existencia) | que el proyecto tenga su glosario y que no esté vacío | un programa ve si el documento existe y si tiene entradas; que la definición se entienda, no |

### Meta-reglas (`20`) — se validan **en seco**, sobre el propio estándar

No necesitan proyecto: leen `base/`. Son las más rentables del conjunto y hoy no existe ninguna. Alimentan un validador `metareglas.py` pendiente.

| Regla | Qué comprobaría el script |
|---|---|
| `M3` | ninguna regla de `base/` nombra lenguaje, framework, motor, nube ni ruta de un proyecto real (lista negra + revisión de rutas) |
| `M4` | ID único, prefijo exclusivo del capítulo y registrado, consecutivo sin reutilizar |
| `M5` | encabezado `##`, marca de la lista cerrada, presencia del ejemplo, tamaño del cuerpo |
| `M7` | toda dependencia declarada apunta a un ID que existe · sin ciclos · ninguna de capa 2 sobre una `[BLINDADA]` |
| `M9` | toda regla de `base/` aparece clasificada en este archivo |
| `M10` | `CHANGELOG.md` y `VERSION` suben juntos — ya lo hace `version.py`, falta atarlo a la regla |
| `M14` | toda regla trae su bloque de checklist, con resultado y versión contra la que se aplicó |

`M14` es **parcial**: que la regla haya recorrido de verdad los nueve pasos no lo decide un script, pero la **presencia y el resultado** del bloque sí.

`M16` es del mismo capítulo pero **no se valida en seco** (🔶): el catálogo vive en el proyecto. El script abre `reglas-proyecto.md`, comprueba que cada `P` trae su **Respaldo** y que el ID citado existe en `base/`. Que el criterio citado sea de verdad el que la `P` concreta lo decide quien lee.

### Redacción (`00·ID8`) — se valida **en seco**, sobre los `.md` que se entregan

| Regla | Qué comprobaría el script | Por qué falta |
|---|---|---|
| `00·ID8` (parte mecánica) | las marcas que se ven sin entender el texto: raya larga como inciso, comillas curvas mezcladas con rectas, punto medio fuera de una cita `NN·ID`, emojis en documento formal, espacio antes del `%`, y las muletillas de lista cerrada (*«no solo… sino también»*, *«Es importante destacar que»*, *«Cabe señalar que»*) | hay que decidir sobre qué archivos corre y dejar fuera bloques de código y citas; el resto de la regla (estructura, tono, contraste de registro) es criterio humano |

`ID8` es **parcial**, como `M14`: las marcas de palabra y tipografía las cuenta un script; que el documento no suene a máquina lo decide quien lo lee.

### Necesitan que el proyecto **declare** su convención o dominio

No son mecánicas "en seco": hace falta que el proyecto declare, en `.agente/`,
contra qué comparar (su convención de estructura/nombres, qué entidades son
inmutables, qué tablas llevan auditoría). Sin esa declaración, dos personas
pueden discutir si se cumplen → hoy las interpreta el agente.

| Regla | Qué comprobaría | Necesita |
|---|---|---|
| `03·D1` (resto) | columnas de auditoría + `UNIQUE` + índices en lo que se filtra | qué tablas son de dominio (no framework) |
| `14·EST1` | módulos en su ubicación | la convención de estructura declarada |
| `14·EST2` (resto) | nombres siguen la convención | la convención de nombres declarada |
| `15·IM2` | tres estados + campos de anulación en el esquema | qué entidades son inmutables |
| `15·IM5` | permiso "anular" separado de "eliminar" | qué entidades son inmutables |
| `18·DP1` | que el despliegue esté descrito en un archivo versionado, no en instrucciones sueltas | un proyecto con despliegue |
| `18·DP2` | que exista la definición de infraestructura en el repositorio | un proyecto con infraestructura propia |
| `18·DP4` | que la configuración por entorno no viaje dentro del artefacto | saber qué es artefacto en ese stack |
| `18·DP6` | que exista el checklist de despliegue | un proyecto con despliegue |
| `18·DP7` | que la aplicación exponga su punto de salud | saber cuál es su punto de entrada |
| `19·OB1` | que los registros salgan estructurados y con identificador de correlación | un proyecto con registros |
| `19·OB3` | que los objetivos de servicio y las alertas vivan en un archivo versionado | un proyecto que los tenga |
| `19·OB4` | que exista el runbook de lo que se opera | un proyecto en operación |

**Estas ocho entraron el 2026-08-16** con los capítulos `18` y `19`. Ninguna se puede comprobar sobre el estándar en seco: **todas necesitan un proyecto real**, así que van con el pendiente 01.

### Validables, y lo que les falta es construirlas

| Regla | Qué comprobaría | Qué falta |
|---|---|---|
| `02·F4` | que la fase tenga su plan de trabajo **y** su plan de pruebas | que existan ya se comprueba; **la aprobación explícita no**, y esa es la mitad que importa. Hoy no queda escrita en ningún archivo que un programa pueda leer |
| `09·G9` | que el mensaje del commit nombre la historia de usuario a la que pertenece | decidir si se exige el identificador en el asunto o en el cuerpo, y agregarlo a `commits.py` |

---

## 🔴 No validables (se quedan en el `.md` — criterio humano)

- **`20` meta-reglas:** `M1`, `M2`, `M6`, `M8`, `M11`, `M12`, `M13` — enrutar, desempatar, decidir si una excepción está completa o si dos reglas dicen lo mismo es criterio: dos personas pueden discutir el resultado.
- **`00` identidad y rol:** ID1, ID2 (derogada en 6.0.0), ID3, ID4, ID5, ID6, ID7, ID9 — postura, registro y borde del rol: qué cuenta como "criterio de senior" o como texto "que lo entienda quien no sabe del tema" lo discute una persona, no un script. `ID9` (decir lo mismo en menos palabras) tampoco: contar renglones es fácil, pero decidir cuál sobra exige entender qué cambia la decisión del que lee. `ID3` es la excepción parcial: sus cuatro condiciones ya las validan por separado `08·T5`, `02·F7` y `13·DOC1`; lo que no se valida es la conjunción.
- **`00` núcleo:** N1, N2, N3, N4, N5, N6.
- **`02·F24`** (el defecto del estándar se reporta) es validable y su programa está escrito: `cruces.py` comprueba que un pendiente que dice venir de un proyecto lo **nombre**. Lo que no puede ver es si el pendiente del otro lado existe —vive en otro repositorio— ni si el aviso de vuelta llegó.
- **`01`:** `C1`, `C2`, `C3`, `C4`, `C5`, `C6`, `C7`, `C8`, `C9`, `C10`, `C11`, `C12`, `C13`, `C14`, `C15`, `C16`, `C17` (todas menos `C18`), `C20`, `C21`, `C22` y `C23`. **Se escriben una por una y no como rango:** hasta el 2026-08-16 decían «C1–C17» y el programa que comprueba `M9` no lee rangos, así que quince reglas figuraban como sin clasificar estando clasificadas. `C22` (el comando rechazado se corrige, la orden sigue en pie) se cumple sobre lo que el agente hace **después** de un rechazo, que no queda en ningún archivo: ningún script puede ver si retomó el encargo o lo abandonó. `C21` (pedir el dato que falte antes de arrancar) se cumple sobre el mensaje del usuario en el chat, y ningún script lee el chat. `C23` (buscar antes de preguntar) es **validable a medias y por eso está acá**: que el agente haya buscado no lo puede ver ningún programa, pero que la respuesta traiga su cita, sí — y esa mitad queda pendiente de escribirse. `C20` (traducir el término de otro idioma) tiene una parte mecánica que ya cubre la lista de marcadores de `00·ID8` —el léxico de España y los calcos del inglés, que son lista cerrada—, pero decidir si una palabra tiene traducción usada, o si la explicación de la primera vez alcanza, es criterio.
- **`02`:** `F1`, `F3`, `F5`, `F6`, `F7`, `F8`, `F9`, `F10`, `F11`, `F15`, `F16`, `F19`, `F20` · `F12.8`, `F12.9`, `F12.10`.
- **`03`:** D4, D5, D6, D7, D8.
- **`04`:** S1, S2, S6, S8, S9, S10, S11.
- **`05`:** E2, E3, E4.
- **`06`:** R3, R4, R5, R6.
- **`07`:** Q1, Q2, Q4, Q5, Q7.
- **`08`:** T1, T2, T6, T7.
- **`09`:** `G1`, `G5`, `G7`.
- **`10`:** DEP1, DEP5.
- **`11`:** CFG1, CFG3, CFG4.
- **`12`:** PR1, PR2, PR3, PR4, PR5 (toda la capa de privacidad es juicio).
- **`13`:** DOC2, DOC4, DOC5, DOC6, DOC9, DOC18 (que el mapa se haya actualizado **en el mismo cambio** exige leer el diff y entender qué cambió).
- **`14`:** EST3.
- **`15`:** IM1, IM3, IM4.
- **`16`:** CQ2, CQ3, CQ4, Parte B.
- **`17`:** `I1`, `I2`, `I3`, `I4`, `I5`, `I6`.
- **`18` despliegue (opt-in):** `DP3` (que el artefacto promovido sea el mismo se decide mirando el proceso, no un archivo), `DP5` (que el plan de vuelta sirva lo dice quien lo lee) y `DP8` (correr contra producción lo autoriza una persona, y eso pasa fuera del repositorio).
- **`19` observabilidad (opt-in):** `OB2` (qué le duele al usuario es criterio de producto), `OB5` (que un postmortem sea sin culpa lo juzga quien lo lee) y `OB6` (operar en vivo lo hace una persona).

> **Los capítulos `18` y `19` entraron a este registro el 2026-08-16**, en la fase `A-EP-001-HU-009`. Nacieron después de la foto del 2026-08-05 y no aparecían ni una vez, ni siquiera para decir que no se validan. Ser **opt-in no exime**: `20·M9` no exceptúa a las reglas opcionales, y no clasificarlas es lo que las volvió invisibles.

---

## Conclusión

Sobre el **estándar solo** ya está todo lo validable, y la mayor parte de lo que vive en los proyectos también — ~50 reglas, todo multiproyecto: leen el código, corren la herramienta del stack, o revisan la documentación de flujo (fases, plan, padres, completitud contra plantilla). Quedan **~9**: 4 son fuzzy o pesadas (`F2` cruzar código↔especificación, `F4.4`, `DOC7`, `DOC14`), y 5 necesitan que el proyecto **declare su convención/dominio** en `.agente/` (`EST1`, resto de `EST2`, `D1`-resto, `IM2`, `IM5`) — sin esa declaración las interpreta el agente.
