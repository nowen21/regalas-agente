# Plan de Trabajo — Fase B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-005 No pisar lo escrito](../HU-005-no-pisar-lo-escrito.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-005 No pisar lo escrito](../HU-005-no-pisar-lo-escrito.md), una sola |
| **Módulo** | Instalador del estándar, los documentos heredados |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📝 **Modifica la fase `A`**, que retrodocumentó el «no pisar lo escrito»: esta agrega la otra mitad, que es completar sin pisar.

**De dónde sale:** el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), donde estaba dicho así: «el mecanismo replica y el texto que lo explica no»

**CA que cubre:** el `CA-01` de la historia, que pide que instalar sobre algo escrito no borre nada.

## 1. Objetivo y alcance

**Objetivo:** que el `README` heredado del histórico reciba lo que la plantilla del estándar haya sumado, sin pisar una línea de lo que el proyecto escribió.

**El defecto era asimétrico y por eso costaba verlo.** El `CLAUDE.md` de cada proyecto sí recibía las secciones nuevas del estándar, con un mecanismo aditivo que ya existía desde `01·C18`; el `README.md` del histórico, no: si ya existía, el instalador solo le refrescaba el sello.

**La consecuencia:** un proyecto instalado en julio se quedaba con el texto de julio para siempre. Y no se notaba, porque el archivo existe, se lee bien y dice cosas ciertas; solo que dice **menos** de lo que el estándar ya sabe.

**No hubo que inventar el mecanismo:** `_completar_secciones` ya estaba escrito y probado para el `CLAUDE.md`. Lo que faltaba era usarlo en el otro archivo.

**Fuera de alcance:**

- **Los demás documentos heredados** (`.agente/`, el índice de la memoria). Se completan si aparece la misma necesidad; hoy no hay evidencia de que se haya perdido nada por ahí.
- **Reordenar o corregir** lo que el proyecto escribió. Aditivo significa que se agrega al final y nada más.

## 2. Análisis previo, línea base verificada

| Qué se verificó | Resultado |
|---|---|
| ¿Existía el mecanismo? | **Sí**, `_completar_secciones`, usado por `instalar_claude_md` desde `01·C18` |
| ¿Qué hacía el instalador con el README del histórico? | Si existía, **solo refrescaba el sello**; el texto se quedaba como estaba |
| ¿Cómo reconoce una sección? | Por su encabezado `##` o menor; el `#` del título no cuenta, porque lleva el nombre del proyecto y nunca coincide |

### 2.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| [`validadores/instalar.py`](../../../../../validadores/instalar.py) | `instalar_historico` completa el README con lo que la plantilla sumó, y lo reporta |
| [`validadores/tests/test_instalar_agrega_al_readme_heredado.py`](../../../../../validadores/tests/test_instalar_agrega_al_readme_heredado.py) | Nuevo: seis casos |
| [`plantillas/historico-chat.md`](../../../../../plantillas/historico-chat.md) | Gana la sección que contesta qué manda cuando el histórico y lo acordado se contradicen |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |

### 2.2 Las trece preguntas, en corto

| # | Respuesta |
|---|---|
| 1-3 | Que el instalador complete el README heredado; lo usa cualquier proyecto instalado |
| 4-5 | §1; fuera quedan los demás heredados y cualquier reescritura |
| 6-8 | No hay datos ni interfaz: es un archivo de texto del proyecto |
| 9 | §2.1 |
| 10 | Corre solo al instalar o reinstalar; no hay que pedirlo |
| 11 | No aplica porque escribe en el proyecto donde se corre, con la autorización de correr el instalador |
| 12 | No aplica porque nada obliga: el proyecto recibe lo nuevo la próxima vez que instale |
| 13 | [plan_pruebas.md](plan_pruebas.md) |

### 2.3 Dudas por resolver

**Ninguna abierta.** La decisión de hacerlo igual que con el `CLAUDE.md` salió del propio pendiente 33.

## 3. Tareas

| # | Tarea | Estado |
|---|---|---|
| T-01 | Usar el mecanismo aditivo en `instalar_historico` y reportar qué agregó | ☑ |
| T-02 | Escribir los seis casos de prueba, con el que protege lo escrito por el proyecto | ☑ |
| T-03 | Escribir en la plantilla qué manda cuando el histórico y lo acordado se contradicen | ☑ |
| T-04 | Correr todo y versionar | ☑ |

## 4. Riesgos

| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que al completar se pise lo del proyecto | `CP-02` es el caso que decide: lo escrito por el proyecto sigue ahí, palabra por palabra |
| B-02 | Que reescriba en cada corrida y ensucie el control de versiones | `CP-03`: sin novedad, el archivo queda byte por byte igual |
| B-03 | Que agregue el título sin su texto | `CP-04`: la sección llega con su cuerpo |
