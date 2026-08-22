# Resultado de Pruebas — Fase A-EP-001-HU-002-capas-y-precedencia

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el veredicto de la fase. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-002-capas-y-precedencia` |
| **HU** | [HU-002](../HU-002-capas-y-precedencia.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) |
| **Ambiente y versión** | El repositorio del estándar en `main`, versión 31.4.0 |

### 0.1 Las tres dudas que la detenían, contestadas por el repositorio

| Duda | Qué contesta el repositorio hoy |
|---|---|
| 1 · ¿el preámbulo es una capa? | **No.** Los dos capítulos de preámbulo llevan su marca propia `[PREÁMBULO]`, y el `20` declara que sus reglas son de procedimiento y **nunca de fondo**: no entran en el orden que decide quién gana |
| 2 · ¿cuántas capas hay? | **Cuatro niveles**, escritos en [`20·M1`](../../../../../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) y en la tabla de [`base/README.md`](../../../../../base/README.md) |
| 3 · ¿«opcional» es marca o capa? | **Marca dentro de la capa 2.** Siete capítulos la llevan (`15`, `16`, `17`, `18`, `19`, `21`, `22`): no cambia quién gana ante un choque, cambia si la regla aplica |

Las tres estaban resueltas en la práctica desde hace días. Lo que faltaba era ejecutarlas y escribirlo.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

| Caso | Criterio | Resultado | Evidencia |
|---|---|---|---|
| CP-001 · el ajuste declarado manda | CA-01 | ✅ Aprobado | El proyecto declara su capa en `.agente/reglas-proyecto.md`; el `CLAUDE.md` instalado manda leerlo y aplicarlo en su paso 4, y [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) obliga a que cada regla propia nombre la de base que ajusta |
| CP-002 · el ajuste no declarado no manda | CA-01 | ✅ Aprobado | `M1` lo dice con esas palabras: la capa 3 gana **solo si** el proyecto la declaró; el silencio no es un ajuste. Sin archivo, el paso 4 del `CLAUDE.md` no aplica nada |
| CP-003 · la excepción contra la capa protegida no aplica | CA-02 | ✅ Aprobado | Paso 1 del desempate: si una es `[BLINDADA]`, gana esa, y no hay paso 2. Y `validar.py metareglas` comprueba que ninguna regla se declare blindada fuera del núcleo, que es la forma de saltarse el orden sin contradecirlo |
| CP-004 · la instrucción del chat no afloja una protegida | CA-03 | ✅ Aprobado | El chat no es una capa: el orden solo conoce núcleo, convenciones y proyecto. Y el núcleo lo dice en su propio texto, por ejemplo `00·N4`: **gana a cualquier instrucción** |
| CP-005 · el orden se puede seguir sin interpretar | CA-03 | ✅ Aprobado | Los seis pasos están escritos y numerados en el [anexo del desempate](../../../../../base/20-meta-reglas/desempate.md), y se recorren de arriba abajo parando en el primero que aplique |
| CP-006 · dos reglas de la misma capa que se contradicen | Transversal, límites | ✅ Aprobado | Pasos 4 y 5: gana la más específica, y si empatan la más restrictiva. Si sigue empatado, el paso 6 manda **pausar y reportar**, no elegir |
| CP-007 · las reglas ya escritas conservan su marca de capa | Transversal, no regresión | ✅ Aprobado | Los 23 capítulos con cabecera llevan su marca: 1 `[CAPA 1]`, 12 `[CAPA 2]`, 7 `[CAPA 2 · opt-in]` y 2 `[PREÁMBULO]` |
| CP-008 · la capa se ve al abrir la regla | RNF, claridad | ✅ Aprobado | La marca está en la **primera línea** del capítulo, así que se ve sin ir a otro documento |

## 3. Verificaciones apoyadas en un programa

Tres de los ocho no dependen de una lectura:

| Qué | Con qué | Resultado |
|---|---|---|
| Ninguna `[BLINDADA]` vive fuera del núcleo | `validar.py metareglas` | sin incumplimientos |
| Ningún capítulo se quedó sin marca de capa | recuento sobre las cabeceras de `base/` | 23 de 23 |
| El orden del desempate resuelve sin enlaces rotos | `validar.py estandar` | sin incumplimientos |

## 4. Defectos encontrados

**Ninguno.** Y una observación que ya se resolvió durante esta misma jornada: el desempate vivía dentro de `M6` como una lista de seis pasos que no cabía en el molde de una regla, y pasó a su anexo en la v30.9.0, entero y sin reescribir.

## 5. Veredicto de la fase

**Cumple.** Ocho casos de ocho.

| Criterio | Veredicto |
|---|---|
| CA-01 · una regla del proyecto ajusta una convención y manda | ✅ Cumple |
| CA-02 · un intento de aflojar la capa protegida no procede | ✅ Cumple |
| CA-03 · una instrucción del chat no cambia el orden | ✅ Cumple |

**Lo que este veredicto no dice:** que la IA se comporte así en cada respuesta. Eso no lo prueba ningún caso escrito, y por eso lo que se comprobó es lo comprobable: que el orden **esté escrito**, que sea seguible sin interpretar, y que lo que un programa puede vigilar —la marca fuera de su sitio— esté vigilado.
