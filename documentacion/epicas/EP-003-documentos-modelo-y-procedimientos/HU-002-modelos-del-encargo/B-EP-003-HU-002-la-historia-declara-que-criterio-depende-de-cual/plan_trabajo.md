# Plan de Trabajo — Fase B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-002 Modelos del encargo](../HU-002-modelos-del-encargo.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual` |
| **Épica** | [EP-003 Documentos modelo y procedimientos](../../epica.md) |
| **HU** | [HU-002 Modelos del encargo](../HU-002-modelos-del-encargo.md), una sola |
| **Módulo** | Moldes del ciclo de vida, el de la historia de usuario |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📝 **Modifica la fase `A`**, que retrodocumentó los moldes del encargo: este agrega al de la historia una columna que no tenía.

**De dónde sale:** el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), abierto desde el 2026-08-07

**CA que cubre:** el `CA-01` de la historia, que pide que los moldes del encargo digan lo que hay que llenar.

## 1. Objetivo y alcance

**Objetivo:** que una historia pueda decir **qué criterio no se puede comprobar mientras otro no esté cumplido**, sin inventar una sección nueva.

**El hueco, medido el 2026-08-07:** la tabla de fases de la plantilla dice qué CA cubre cada fase, pero no si un CA depende de otro. Sin eso, dos fases se ordenan al revés y el error aparece al probar, cuando ya se construyó.

**Por qué columna y no sección.** Una sección nueva la paga toda historia, incluidas las que no tienen ninguna dependencia. Una columna vacía no cuesta nada de llenar y se ve de un vistazo junto a la fase que le importa.

**Fuera de alcance:**

- **Comprobar la dependencia con un programa.** Que el orden declarado sea el correcto exige leer los dos criterios; por [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), primero tiene que cumplirse a mano.
- **Rellenar la columna en las 101 historias ya escritas.** La columna se llena cuando la historia se toca; ninguna queda mal por tenerla vacía.

## 2. Análisis previo, línea base verificada

| Qué se verificó | Resultado |
|---|---|
| ¿La plantilla ya tenía dónde decirlo? | **No.** Su §8 tiene fase, CA que cubre, los tres enlaces y el estado |
| ¿Alguna regla lo exige? | **No**, y no se agrega ninguna: la columna es del molde, no una exigencia nueva |
| ¿Rompe las historias ya escritas? | **No.** Una tabla con una columna menos sigue siendo válida; se completa al tocarla |

### 2.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| [`plantillas/ciclo-vida-proyectos/04-HU.md`](../../../../../plantillas/ciclo-vida-proyectos/04-HU.md) | La tabla de §8 gana la columna «Depende de», con una fila de ejemplo que la usa y la frase que dice cómo se llena |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |

### 2.2 Las trece preguntas, en corto

| # | Respuesta |
|---|---|
| 1-3 | Una columna en el molde de la historia, para declarar dependencia entre criterios; la usa cualquier proyecto que herede las plantillas |
| 4-5 | §1; fuera quedan el validador y el relleno hacia atrás |
| 6-8 | No hay datos ni interfaz: el entregable es un molde |
| 9 | §2.1 |
| 10 | En `plantillas/ciclo-vida-proyectos/`, que el instalador copia |
| 11 | No aplica porque no hay ejecución ni permisos |
| 12 | No aplica porque nada obliga a migrar: la columna vacía es válida |
| 13 | [plan_pruebas.md](plan_pruebas.md) |

### 2.3 Dudas por resolver

**Ninguna abierta.** La única que había, si entraba a la plantilla, la decidió el usuario al ordenar resolver el pendiente 33.

## 3. Tareas

| # | Tarea | Estado |
|---|---|---|
| T-01 | Agregar la columna a la tabla de §8, con su fila de ejemplo | ☑ |
| T-02 | Escribir cómo se llena: con criterios, no con fases, y vacía si no hay dependencia | ☑ |
| T-03 | Correr las pruebas y versionar | ☑ |

## 4. Riesgos

| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que se llene con fases en vez de criterios, que es lo que ya dice la primera columna | La frase de abajo lo dice con esas palabras, y la fila de ejemplo muestra un CA, no una fase |
| B-02 | Que se vuelva obligatoria de hecho y llene de ruido las historias simples | Queda escrito que vacía es correcto |
