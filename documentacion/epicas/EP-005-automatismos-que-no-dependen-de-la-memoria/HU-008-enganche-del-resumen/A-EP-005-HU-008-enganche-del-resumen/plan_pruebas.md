# Plan de Pruebas — Fase A-EP-005-HU-008-enganche-del-resumen

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ninguna exigencia quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el [resultado_pruebas.md](resultado_pruebas.md). La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-008 |
| **Versión** | 1.1 — la 1.0 se aprobó el 2026-08-14; la 1.1 agrega los casos de la corrida 2, al reabrirse la fase |
| **Alcance del plan** | Fase `A-EP-005-HU-008-enganche-del-resumen` |
| **Fecha** | 2026-08-14 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Estado** | Borrador |

> **Proporcionalidad.** Una sola fase: se llenan las secciones 3, 5, 6, 9 y 12, como manda la plantilla.

---

## 3. Estrategia de pruebas

Acá sí hay código, así que la mayor parte se automatiza. Lo que no se puede automatizar es lo que decide si el enganche sirve: **que el aviso se lea como ayuda y no como ruido**.

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitarias | Que `resumen.py` arme la ruta, cree el archivo y lea los hallazgos | Carpetas temporales | Sí |
| Integración | Que los dos enganches hagan lo suyo con un proyecto de prueba completo | Carpetas temporales | Sí |
| Regresión | Que el renombrado siga funcionando para la transcripción | Carpetas temporales | Sí |
| Manual | Que el aviso no moleste | Una sesión real | No |

**Tipos que aplican:** funcional, usabilidad y rendimiento (lo que suma al arranque). No aplican seguridad, migración de datos ni recuperación.

**Triangulación ([`08·T7`](../../../../../base/08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos)):** "la sesión produjo algo" se comprueba por dos caminos independientes, el commit y el cambio en `base/` o `plantillas/`. Los dos tienen que dar lo mismo sobre el mismo proyecto de prueba.

**Alcance de la corrida automatizada ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):** la suite de `validadores/pruebas.py` y `validar.py estandar`. No se corre nada más.

---

## 5. Matriz de trazabilidad

> Ninguna exigencia puede quedar sin al menos un caso. Los `RNF-0N` llevan su fila propia.

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) | [CP-001](#cp-001--el-archivo-nace-al-abrir-la-sesión), [CP-002](#cp-002--dos-sesiones-el-mismo-día-no-se-pisan), [CP-003](#cp-003--el-renombrado-mueve-los-dos-archivos) | Funcional | Crítica | Sí | ☐ |
| HU-008 | [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) | [CP-004](#cp-004--avisa-qué-falta-cuando-la-sesión-produjo-algo), [CP-005](#cp-005--calla-cuando-no-hay-nada-que-avisar) | Funcional | Crítica | Sí | ☐ |
| HU-008 | [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) | [CP-006](#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) | Funcional | Crítica | Sí | ☐ |
| HU-008 | [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | [CP-004](#cp-004--avisa-qué-falta-cuando-la-sesión-produjo-algo) | Usabilidad | Alta | Sí | ☐ |
| HU-008 | [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | [CP-007](#cp-007--el-aviso-no-se-repite) | Usabilidad | Alta | Sí | ☐ |
| HU-008 | [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | [CP-008](#cp-008--no-demora-el-arranque) | Rendimiento | Media | Parcial | ☐ |
| HU-008 | Transversales de la HU | [CP-009](#cp-009--no-toca-lo-escrito-no-se-mete-donde-no-lo-llaman-y-no-detiene) | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 7 de 7 exigencias cubiertas = 100%.

**Los casos de la corrida 2** ([§6.1](#61-corrida-2--los-mismos-criterios-disparados-de-verdad)), que reemplazan a los que no probaron su camino:

| Exigencia | Caso(s) | Reemplaza a | Automatizado |
|---|---|---|:--:|
| [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) | [CP-010](#cp-010--el-resumen-aparece-solo-en-una-sesión-nueva), [CP-011](#cp-011--el-instalador-deja-el-proyecto-listo), [CP-012](#cp-012--dos-sesiones-el-mismo-día-no-se-pisan), [CP-013](#cp-013--el-encabezado-no-enlaza-a-nada-que-no-exista), [CP-018](#cp-018--el-archivo-aparece-solo-en-una-sesión-real) | CP-001 y CP-002 | Sí, salvo CP-018 |
| [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) | [CP-014](#cp-014--avisa-qué-falta-cuando-la-sesión-produjo-algo) | CP-004 | Sí |
| [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) | [CP-015](#cp-015--del-propósito-se-muestra-lo-abierto-y-nada-de-otros-temas) | CP-006 | Sí |
| [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) | [CP-016](#cp-016--correr-los-dos-modos-no-pisa-ni-duplica) | CP-007 | Sí |
| Transversales | [CP-017](#cp-017--un-proyecto-sin-instalar-no-se-ve-afectado) | la parte de límites de CP-009 | Sí |

---

## 6. Casos de prueba

### CP-001 — El archivo nace al abrir la sesión

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Proyecto de prueba con carpeta de resúmenes y sin resumen de hoy |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche de `SessionStart` | Existe `resumenes/AAAA-MM-DD/<nombre>.md` |
| 2 | Abrir el archivo | Trae los campos del modelo y ningún hallazgo |
| 3 | Correr el enganche otra vez | El archivo no se pisa ni se duplica |

### CP-002 — Dos sesiones el mismo día no se pisan

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) |
| **Tipo** | Funcional — límite |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir dos sesiones el mismo día, con nombres distintos | Aparecen dos archivos en la carpeta del día |
| 2 | Mirar el primero | Sigue como estaba, sin tocar |

### CP-003 — El renombrado mueve los dos archivos

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) |
| **Tipo** | Funcional — el que puede dejar todo a medias |
| **Prioridad** | Crítica |
| **Precondiciones** | Sesión con transcripción sin tema y su resumen ya creado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `historico.py --renombrar` con un tema | La transcripción y el resumen quedan con el nombre nuevo |
| 2 | Mirar el índice del histórico | La línea apunta a los dos archivos nuevos, y ninguno de los enlaces está roto |
| 3 | Renombrar una sesión que **no** tiene resumen | No falla: renombra la transcripción y no inventa el enlace |

### CP-004 — Avisa qué falta cuando la sesión produjo algo

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) y [RNF-01](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sembrar un commit en el proyecto de prueba, con el resumen vacío | — |
| 2 | Correr el enganche de `UserPromptSubmit` | Imprime el aviso, dice que no hay ningún hallazgo y cuál es el archivo |
| 3 | Escribir un hallazgo y correrlo otra vez | No repite el primero; avisa que falta decir si la sesión se puede cerrar, y lista los hallazgos del propósito sin resolver |
| 4 | Llenar la sección de cierre y correrlo otra vez | No avisa nada |
| 5 | Repetir por el otro camino: cambiar un archivo de `base/` sin commitear | El aviso sale igual (triangulación) |
| 6 | Comprobar cuándo salió | Durante la sesión, no al cerrarla |

### CP-005 — Calla cuando no hay nada que avisar

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío) |
| **Tipo** | Funcional — negativo |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sesión que no produjo nada, resumen vacío | No avisa |
| 2 | Sesión que produjo algo, con hallazgos y la sección de cierre llena | No avisa |
| 3 | Sesión con un hallazgo abierto que **no** es de su propósito, y el cierre llena | No avisa: ese se cierra en otra sesión |

### CP-006 — Se muestra lo abierto del propósito, y nada de otros temas

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Dos temas con hallazgos abiertos, en resúmenes de días distintos, y una sesión que declara uno de los dos como propósito |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir la sesión con su propósito declarado | Se muestra el hallazgo del propósito, con su archivo y su pregunta viva |
| 2 | Mirar el hallazgo abierto del otro tema | No aparece: no es de esta sesión |
| 3 | Poner el propósito en un hallazgo de hace una semana | Aparece igual: lo que acota es el tema, no la fecha |
| 4 | Cerrarlo y abrir otra sesión con el mismo propósito | Ya no aparece |

### CP-007 — El aviso no se repite

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) |
| **Tipo** | Usabilidad |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche dos turnos seguidos con la misma condición | El aviso sale una sola vez |
| 2 | Provocar las dos condiciones a lo largo de la sesión | Salen dos avisos en total, no más |
| 3 | Mirar dónde quedó la marca | Dentro del propio resumen, no en un archivo aparte |

### CP-008 — No demora el arranque

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [RNF-03](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) |
| **Tipo** | Rendimiento |
| **Prioridad** | Media |
| **Datos de entrada** | El histórico real de este repositorio: 35 sesiones |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Medir el arranque sin el enganche nuevo | Un número de partida |
| 2 | Medirlo con el enganche | La diferencia no se nota al abrir la sesión |

> Si acá falla, lo que se cambia es cuántas sesiones hacia atrás se leen, no el criterio.

### CP-009 — No toca lo escrito, no se mete donde no lo llaman y no detiene

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / criterios transversales de la HU |
| **Tipo** | Funcional — negativo |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr los enganches sobre un resumen con hallazgos ya escritos | Ni una línea cambia |
| 2 | Correrlos en un proyecto sin carpeta de resúmenes | No hace nada y no falla |
| 3 | Correrlos sobre una carpeta sin permiso de escritura | Avisa el motivo y sale con código 0 |

---

## 6.1 Corrida 2 — los mismos criterios, disparados de verdad

> **Por qué existen estos casos.** Los de arriba se corrieron llamando por dentro a `resumen.crear()`, con la transcripción y la carpeta puestas a mano. Ese estado no ocurre nunca, así que seis de ellos no probaron nada. Un caso de esta sección **no vale, aunque pase**, si incumple alguna de estas tres:
>
> 1. **Se dispara por donde dispara el sistema:** el enganche se corre como orden del sistema operativo, con el mismo JSON que le manda Claude Code (`session_id`, `cwd`, `prompt`).
> 2. **La precondición la produce el sistema:** el proyecto se arma corriendo `instalar.py --aplicar`, y la transcripción la escribe `hook_historico.py`. El que prueba no crea carpetas ni archivos del flujo.
> 3. **El resultado escribe la orden literal y su salida**, paso a paso.

### CP-010 — El resumen aparece solo en una sesión nueva

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo). Reemplaza a [CP-001](#cp-001--el-archivo-nace-al-abrir-la-sesión) |
| **Tipo** | Funcional — el que reproduce el defecto |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal con `git init`, pasada por `instalar.py --aplicar`. Nada se crea a mano |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `hook_resumen.py --modo inicio` con `{"session_id":"s1","cwd":"<tmp>"}` | Sale con 0 y no imprime: la sesión no tiene transcripción todavía |
| 2 | `hook_historico.py --modo usuario` con el mismo `session_id` | Aparece la transcripción del día |
| 3 | `hook_resumen.py --modo aviso` con el mismo `session_id` | Aparece el resumen en la carpeta del día, y el enganche dice dónde quedó |
| 4 | Abrir el archivo | Trae el modelo, ningún hallazgo y la sección de cierre |
| 5 | Mirar el índice del día | Tiene la línea de esa sesión, una sola vez |

### CP-011 — El instalador deja el proyecto listo

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) |
| **Tipo** | Funcional — el hueco del proyecto heredero |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `instalar.py <tmp> --aplicar` sobre una carpeta nueva | Existe `historico-chat/resumenes/README.md` |

### CP-012 — Dos sesiones el mismo día no se pisan

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo). Reemplaza a [CP-002](#cp-002--dos-sesiones-el-mismo-día-no-se-pisan) |
| **Tipo** | Funcional — límite |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Repetir CP-010 con `s1` y después con `s2` | Quedan dos archivos distintos en la carpeta del día |

### CP-013 — El encabezado no enlaza a nada que no exista

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) |
| **Tipo** | Funcional — el que rompe en el proyecto heredero |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `plantillas/sesion.md` en el resumen nacido en CP-010 | No aparece |
| 2 | Seguir cada enlace del encabezado desde la carpeta del archivo | Todos llegan a un archivo que existe |

### CP-014 — Avisa qué falta cuando la sesión produjo algo

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío). Reemplaza a [CP-004](#cp-004--avisa-qué-falta-cuando-la-sesión-produjo-algo) |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En el proyecto de CP-010, escribir un archivo y hacer `git add` | El proyecto tiene un cambio preparado |
| 2 | `hook_resumen.py --modo aviso` | Avisa que el resumen no tiene ni un hallazgo |

### CP-015 — Del propósito se muestra lo abierto, y nada de otros temas

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más). Reemplaza a [CP-006](#cp-006--se-muestra-lo-abierto-del-propósito-y-nada-de-otros-temas) |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En el resumen nacido en CP-010, escribir el «viene de» apuntando a un hallazgo abierto, y dejar otro resumen con un hallazgo abierto de otro tema | Los dos existen en la carpeta del día |
| 2 | `hook_resumen.py --modo inicio` | Imprime el hallazgo del «viene de» y su pregunta viva |
| 3 | Leer la salida | El hallazgo del otro tema no aparece |

### CP-016 — Correr los dos modos no pisa ni duplica

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [RNF-02](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales). Reemplaza a [CP-007](#cp-007--el-aviso-no-se-repite) |
| **Tipo** | Funcional — concurrencia |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con un hallazgo escrito a mano en el resumen, correr los dos modos otra vez | El texto queda intacto y el índice del día no gana una línea repetida |

### CP-017 — Un proyecto sin instalar no se ve afectado

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / transversal de límites. Reemplaza esa parte de [CP-009](#cp-009--no-toca-lo-escrito-no-se-mete-donde-no-lo-llaman-y-no-detiene) |
| **Tipo** | Funcional — límite |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr los dos modos sobre una carpeta temporal vacía | Salen con 0, sin imprimir nada y sin escribir nada |

### CP-018 — El archivo aparece solo en una sesión real

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-008 / [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo) |
| **Tipo** | Manual — no se puede automatizar |
| **Prioridad** | Crítica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir una sesión nueva en este repositorio y escribir el primer mensaje | El resumen de esa sesión aparece en la carpeta del día sin que nadie lo pida |

---

## 9. Gestión de defectos

| Severidad | Qué sería, acá | Atención |
|---|---|---|
| **Crítica** | El renombrado deja el índice apuntando a un archivo que no existe · el enganche detiene la sesión · toca un hallazgo escrito | Antes de cerrar la fase |
| **Alta** | El aviso no sale cuando debería, o sale repetido | Antes de cerrar la fase |
| **Media** | El arranque se nota más lento | Se ajusta cuántas sesiones se leen |
| **Baja** | Redacción del aviso | Backlog |

Se registran en el [resultado_pruebas.md](resultado_pruebas.md), no acá.

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF + transversales) con caso / totales | 100% |
| Casos automatizados | Automatizados / diseñados | ≥ 85% |
| Avisos por sesión | Conteo | 2 como máximo, uno por cada cosa que falte |
| Enlaces rotos en el índice tras renombrar | Conteo | 0 |
| Lo que suma al arranque | Con enganche − sin enganche | Que no se note |

El resultado de medirlas va en el [resultado_pruebas.md](resultado_pruebas.md).
