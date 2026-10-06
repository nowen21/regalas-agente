# Resultado de Pruebas · Fase A-EP-001-HU-040-c29-nombra-la-base-de-cimiento   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-040-c29-nombra-la-base-de-cimiento` |
| **HU** | [HU-040](../HU-040-c29-reconoce-la-base-de-cimiento.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, sobre el commit `fb8c767` con los cambios de la fase sin guardar, versión 55.1.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**[CA-01](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-01--la-regla-nombra-la-base-de-cimiento) con [CP-001](plan_pruebas.md#cp-001--la-regla-dice-repositorio-o-base-de-datos-del-agente), que la regla diga dónde va lo que la herramienta deja afuera**

**El problema que resuelve:** sin esto, guardar el gasto en la base incumple `01·C29`, y leerlo de afuera también.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `base/01-conducta.md` en `## C29` | El título no cambió | Línea 1048: «## C29 · Guarda dentro del repositorio todo lo del agente y del proyecto», igual que antes |
| 2 | Leer el cuerpo | Dice «en el repositorio o en la base de datos del agente» y que lo que no se corrige en su origen se trae a esa base en cuanto aparece, con las claves tapadas | Dice «vive en el repositorio o en la base de datos del agente» y «si no se deja, se trae a esa base en cuanto aparece, sin claves (`00·N6`), y se lee de allá» |
| 3 | Leer el ejemplo | Un INCORRECTO y un CORRECTO sobre el registro que la herramienta borra | Está el par nuevo: el tablero que lee el almacén que se borra al mes, y el proceso que lo trae a la base |
| 4 | Leer el checklist | En CUMPLE contra 55.1.0 y cita el acuerdo 5 | Línea 1072: «contra **v55.1.0**, el **2026-10-06**»; la nota «Lo que cambió en v55.1.0» enlaza el análisis 1 del pendiente 124, acuerdo 5 |

**Cómo se verificó que la pareja cumple:** el paso 2 decide: es el texto que pide RN-01 y RN-02. El paso 1 asegura que ningún enlace al ancla se rompió, y el 4 cubre RNF-01.

**[CA-02](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-02--la-regla-pasa-sus-comprobaciones) con [CP-002](plan_pruebas.md#cp-002--los-validadores-del-estándar-pasan) y [CP-003](plan_pruebas.md#cp-003--la-versión-sube-a-5510), que la regla pase sus comprobaciones y quede versionada**

**El problema que resuelve:** una regla que no pasa el molde o que cambia sin versión deja a los proyectos sin saber qué cambió.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `python validadores/validar.py metareglas` | Sin fallas | `0 falla(s), 4 aviso(s)`; ninguno nombra `C29` |
| 2 | Correr `python validadores/validar.py estandar` | Sin fallas nuevas por esta fase | `OK: sin incumplimientos.` |
| 3 | Abrir `VERSION` | Dice 55.1.0 | `55.1.0` |
| 4 | Abrir `CHANGELOG.md` | La primera entrada es 55.1.0, MENOR, y nombra `01·C29` | «## 55.1.0 — 2026-10-06», MENOR, con `01·C29` |

**Cómo se verificó que la pareja cumple:** el paso 1 decide el molde. En la primera corrida dio un aviso para `C29`: el cuerpo medía 469 caracteres y el molde da 320. Se acortó y la segunda corrida ya no lo nombra (§8).

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01, RNF-01 | Crítica | 2026-10-06 | Lectura de `## C29` en `base/01-conducta.md`: cuerpo con «repositorio o base de datos del agente», par de ejemplo nuevo, checklist contra v55.1.0 | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Alta | 2026-10-06 | `validar.py metareglas`: 0 fallas, sin aviso de `C29`; `validar.py estandar`: sin incumplimientos | Aprobado | EV-03 | DEF-01, corregido |
| CP-003 | CA-02 | Alta | 2026-10-06 | `VERSION` dice 55.1.0 y `CHANGELOG.md` abre con 55.1.0 MENOR que nombra `01·C29` | Aprobado | EV-02 | — |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** nada en el ciclo final.

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las copias de `C29` en `reglas-por-tarea/` quedaron iguales a la regla | `git diff base/reglas-por-tarea/correr-comando.md` después de `mapa_tareas.py` | Igual al cuerpo nuevo |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | El cuerpo de `C29` pasaba el largo del molde | CP-002 | Baja | Corregido | Este documento, §8 |

**Defectos abiertos que se aceptan y por qué:** ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-01--la-regla-nombra-la-base-de-cimiento) | CP-001 | Aprobado | Sí |
| [CA-02](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-02--la-regla-pasa-sus-comprobaciones) | CP-002, CP-003 | Aprobados | Sí |
| RNF-01 | CP-001 | Aprobado | Sí |

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100 % | 3 de 3 | Sí |
| Casos críticos y altos ejecutados | Plan §5 | 100 % | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios y el requisito no funcional tienen sus casos aprobados, y el único defecto quedó corregido en la misma ejecución.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Texto de la regla | `base/01-conducta.md`, `## C29` |
| EV-02 | Versión | `VERSION`, `CHANGELOG.md` |
| EV-03 | Salida de validadores | §2 de este documento |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 3 | 0 | En la primera corrida de CP-002, `metareglas` avisó que el cuerpo de `C29` medía 469 caracteres; se acortó a la medida y se volvió a correr |
