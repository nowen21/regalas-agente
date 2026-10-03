# Plan de Trabajo · Fase `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple` (módulo `plantillas/`, `validadores/` y `base/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), una sola (`F12.1`) |
| **Módulo** | `plantillas/`, `validadores/`, `base/` |
| **Especificación del módulo** | Los CA-01, CA-03 y CA-04 de la HU-007 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): primera de tres fases de la HU-007. Sale de los puntos 25, 27 y 31 de «Lo que se tiene que hacer» del [análisis 1](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) (conclusiones 44, 46 y 47). El criterio del freno en cuatro capas se reparte en las fases `B` (antes y después de actuar) y `C` (la integración continua y el contrato de cada adaptador), como lo pide su texto.

**Carencias que cierra** (`02·F14` Q3): el plan acepta descripciones y carpetas en vez de rutas, no dice quién lo aprobó, el commit no se compara con el plan, y nada sabe qué autorizan las reglas.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-02, con la versión 47.0.0.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-02 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-007 | Estado |
|---|---|
| CA-01 · El plan solo acepta rutas exactas y dice quién lo aprobó | ☐ |
| CA-03 · El commit se rechaza si trae archivos no declarados | ☐ |
| CA-04 · La lista de lo autorizado incluye las reglas de cada proyecto | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el plan diga con rutas exactas qué toca y quién lo aprobó, que cada regla que autoriza escribir algo lo diga en una línea que un programa lee, y que el commit que trae un archivo que ni el plan ni una regla autorizan se rechace.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La plantilla pide rutas exactas y la aprobación; el validador rechaza la fila que no es ruta exacta | Plantilla y validador | Media |
| CA-03 | El enganche de antes del commit rechaza el archivo que el plan no declara ni una regla autoriza | Validador e instalador | Media |
| CA-04 | Lo que autorizan las reglas de `base/` y las propias del proyecto se lee de sus líneas «Autoriza escribir» | Regla y programa | Media |

**Fuera de alcance:** el freno antes y después de actuar (fase `B`) y la integración continua con el contrato de cada adaptador (fase `C`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 47.0.0:

- La tabla 2.1 de `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` pide «la lista exacta de archivos», pero no prohíbe comodines, carpetas ni descripciones. La sección 0 no trae quién aprobó ni cuándo.
- `validadores/plan_vs_hecho.py` (`validar.py plan`) acepta carpetas terminadas en `/` y nombres sueltos, compara con `git diff` solo si se le da `--desde`, y solo avisa. `validadores/flujo.py` no mira la tabla 2.1.
- El enganche `pre-commit` que instala `validadores/instalar.py` (`HOOKS`) revisa secretos, artefactos y marcas; no compara lo que entra con el plan. `validadores/estacion_commit.py` ya sabe qué fases toca un commit por la carpeta de sus archivos (`fases_que_toca`).
- Ningún programa lee qué autorizan las reglas. Las reglas que autorizan escribir algo sin plan son: `13·DOC22` (la transcripción y el resumen), `13·DOC24` (el análisis), `13·DOC25` (el análisis principal), `04·S18` (los guiones de apoyo), `01·C19` (la memoria), `13·DOC5` (las señales), `20·M10` (`CHANGELOG.md` y `VERSION`), `20·M13` (el índice de pendientes), `01·C28` (el mapa de tareas que se regenera) y `02·F12` (los documentos de la propia fase).
- Las reglas propias de un proyecto viven en `.agente/reglas-proyecto.md`; solo `metareglas.py` las lee.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Plantilla | La aprobación y las rutas exactas |
| `plantillas/reglas-proyecto.md` | Modificar | Plantilla | La línea «Autoriza escribir» en la regla del proyecto |
| `base/20-meta-reglas/estructura-regla.md` | Modificar | Regla | La línea «Autoriza escribir» en el formato de toda regla |
| `base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md` | Modificar | Regla | Su línea «Autoriza escribir» |
| `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md` | Modificar | Regla | Su línea |
| `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md` | Modificar | Regla | Su línea |
| `base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md` | Modificar | Regla | Su línea |
| `base/04-seguridad.md` | Modificar | Regla | La línea de `S18` |
| `base/01-conducta.md` | Modificar | Regla | Las líneas de `C19` y `C28` |
| `base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md` | Modificar | Regla | Su línea |
| `base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md` | Modificar | Regla | Su línea |
| `base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md` | Modificar | Regla | Su línea |
| `validadores/autorizado.py` | Nuevo | Programa | Lee las líneas «Autoriza escribir» de `base/` y de `.agente/reglas-proyecto.md` |
| `validadores/flujo.py` | Modificar | Validador | Rutas exactas y aprobación del plan |
| `validadores/plan_vs_hecho.py` | Modificar | Validador | Lo preparado para el commit contra el plan y lo autorizado |
| `validadores/validar.py` | Modificar | Validador | `validar.py plan --preparados` |
| `validadores/instalar.py` | Modificar | Instalador | El enganche `pre-commit` corre la comparación |
| `validadores/tests/test_nada_fuera_del_plan.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `base/mapa-de-tareas.md` | Regenerar | Regla | Con `mapa_tareas.py` |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | El programa nuevo |
| `CHANGELOG.md` | Modificar | Versión | 48.0.0 |
| `VERSION` | Modificar | Versión | 48.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| El `pre-commit` compara con el plan | Todo commit de un proyecto con la versión nueva | Solo compara cuando el commit toca una fase cuyo plan se aprobó desde 48.0.0 |
| La tabla 2.1 exige rutas exactas | Los planes nuevos | Los planes aprobados antes no se revisan (`20·M10`) |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Lo que una regla autoriza se escribe en la propia regla, en una línea `**Autoriza escribir:**` con las rutas, junto a `**Aplica a:**`; el programa arma la lista leyéndolas | Una lista aparte que nombra las reglas | La autoriza la regla (análisis 1, turno 106 y conclusión 46); una lista aparte repetiría lo mismo en dos sitios (`20·M2`) |
| Las rutas de esa línea admiten `*` y `**`, porque una regla autoriza una clase de archivos (todos los análisis, todos los guiones) | Solo rutas exactas | La tabla del plan sí exige rutas exactas, porque nombra los archivos de una fase |
| Las reglas propias del proyecto usan la misma línea en `.agente/reglas-proyecto.md` | Otro formato | Un solo formato para `base/` y para el proyecto (conclusión 47) |
| La aprobación del plan se escribe «**Aprobación** (`02·F4`): «quién», el «AAAA-MM-DD», con la versión «X.Y.Z»» | Solo la fecha | El CA-01 pide quién y cuándo; la versión decide desde cuándo se exige lo nuevo |
| El `pre-commit` compara solo cuando el commit toca la carpeta de una fase cuyo plan se aprobó desde 48.0.0, y deja pasar lo que el plan declara, lo que una regla autoriza y los documentos de la propia fase | Comparar todo commit | Sin plan aprobado no hay contra qué comparar; los commits de análisis y HU los autorizan sus reglas |
| La versión sube a 48.0.0, MAYOR | MENOR | El commit con un archivo fuera del plan deja de entrar |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Tabla 2.1 del plan | Rutas, carpetas o descripciones | Solo rutas exactas | `02·F8` |
| Aprobación del plan | En prosa, cuando se escribe | Quién, cuándo y con qué versión | `02·F4` |
| Lo que autorizan las reglas | No lo lee nadie | Línea «Autoriza escribir» en la regla, leída por `autorizado.py` | `02·F8` |
| Commit | No se compara con el plan | Se rechaza lo no declarado ni autorizado | `02·F8` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · El plan solo acepta rutas exactas y dice quién lo aprobó

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | La sección 0 suma la fila de la aprobación (quién, cuándo, versión); la nota de la 2.1 dice que cada fila lleva una o más rutas exactas entre comillas invertidas, sin comodines, carpetas ni descripciones | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | CA-01 | Los planes nuevos | 0,3 h | Ninguna | CP-001 |
| T-02 | `flujo.py` falla, en el plan aprobado desde 48.0.0, por la fila de la 2.1 que no es solo rutas exactas y por la aprobación sin quién o sin fecha | `validadores/flujo.py` | CA-01 | Ninguno en los planes aprobados antes | 1 h | T-01 | CP-001 |

### CA-04 · La lista de lo autorizado incluye las reglas de cada proyecto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | El formato de la regla suma la línea opcional `**Autoriza escribir:**`; la plantilla de las reglas del proyecto, también | `base/20-meta-reglas/estructura-regla.md`, `plantillas/reglas-proyecto.md` | CA-04 | Todo proyecto que adopte la versión | 0,3 h | Ninguna | CP-003 |
| T-04 | Sumar la línea a las diez reglas de la 2 (`DOC22`, `DOC24`, `DOC25`, `DOC5`, `S18`, `C19`, `C28`, `M10`, `M13` y `F12`), con sus rutas; sellos contra 48.0.0; regenerar el mapa de tareas | Las reglas de la tabla 2.1 y `base/mapa-de-tareas.md` | CA-04 | Todo proyecto que adopte la versión | 1 h | T-03 | CP-003 |
| T-05 | `autorizado.py`: lee las líneas de `base/` y de `.agente/reglas-proyecto.md` y dice, para una ruta, qué regla la autoriza | `validadores/autorizado.py` | CA-04 | Lo usan el `pre-commit` y, en la fase `B`, el freno | 1 h | T-04 | CP-003 |

### CA-03 · El commit se rechaza si trae archivos no declarados

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | `validar.py plan --preparados`: para cada fase que toca el commit con plan aprobado desde 48.0.0, falla por el archivo preparado que no está en su tabla 2.1, no es un documento de la fase y ninguna regla autoriza | `validadores/plan_vs_hecho.py`, `validadores/validar.py` | CA-03 | Los commits de las fases nuevas | 1 h | T-05 | CP-002 |
| T-07 | El enganche `pre-commit` corre `validar.py plan --preparados` | `validadores/instalar.py` | CA-03 | Todo proyecto, al reinstalar | 0,3 h | T-06 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Escribir los casos del plan de pruebas; poner el programa en el mapa del sitio; subir a 48.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_nada_fuera_del_plan.py`, `anatomia/mapa-del-sitio.md`, `CHANGELOG.md`, `VERSION` | CA-01, CA-03, CA-04 | Todo proyecto adopta la versión | 1 h | T-01 a T-07 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01, T-03 y T-04; después T-05; luego T-02, T-06 y T-07; al final T-08, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer la plantilla; el validador sobre un plan con una fila que no es ruta exacta y sin aprobación | CP-001 |
| CA-03 | Un commit de prueba con un archivo que el plan no declara | CP-002 |
| CA-04 | Una regla del proyecto que autoriza un archivo; el commit que lo trae pasa | CP-003 |

## 6. Datos y ambiente de prueba

Un repositorio de git de prueba en una carpeta temporal, con una fase, su plan y reglas de prueba.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 48.0.0 con el instalador, que pone el `pre-commit` nuevo. Los planes aprobados antes no se revisan; desde esa versión, el plan lleva su aprobación con la versión y rutas exactas.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F4`, `02·F8`, `02·F12`, `20·M2`, `20·M10`, `20·M16`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el commit de un archivo que una regla sí autoriza se rechace | La prueba cubre los archivos de cada regla de la 2; lo que falte se suma a su regla |
| Que un proyecto con planes viejos quede sin poder hacer commit | Solo se comparan los planes aprobados desde 48.0.0 |

## 11. Definition of Done

- [ ] CA-01, CA-03 y CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 48.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.

**Hallazgos al ejecutar:** se anota al cerrar.
