# Plan de Trabajo — Fase C-EP-005-HU-001-el-historico-se-busca-por-tema

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-001 Transcripción de la sesión](../HU-001-transcripcion-de-la-sesion.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-005-HU-001-el-historico-se-busca-por-tema` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-001 Transcripción de la sesión](../HU-001-transcripcion-de-la-sesion.md), una sola |
| **Módulo** | Histórico de sesiones, sus índices |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** El histórico tenía índice por fecha y nombre; este agrega el que faltaba, por tema.

**De dónde sale:** el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), anotado el 2026-08-14: «una sesión trata varios temas y por el título no se encuentran»

**CA que cubre:** el criterio de la historia sobre que la próxima sesión encuentre lo que la anterior dejó.

## 1. Objetivo y alcance

**Objetivo:** poder buscar en el histórico **por tema** y no solo por fecha o por título de sesión.

**El problema estaba medido:** la sesión del 2026-08-21 tocó siete asuntos distintos, y su nombre solo dice uno. Con 59 resúmenes, encontrar «dónde se decidió esto» era abrir uno por uno.

**Los temas ya estaban escritos.** Cada resumen abre sus hallazgos con `### H-N · lo que pasó`, y ese título **es** el tema. No hizo falta inventar una clasificación ni pedirle a nadie que etiquete nada: se recogen los 345 que ya existían.

**Generado, no escrito a mano**, porque este índice crece en cada sesión: escrito a mano envejecería más rápido que cualquier otro mapa del repositorio.

**Fuera de alcance:**

- **Agrupar temas parecidos.** Decidir que dos hallazgos hablan de lo mismo es leer; el índice junta, no clasifica.
- **Generarlo solo en cada sesión.** Hoy se corre a mano o al cerrar; enganchar el disparo es otra fase, y por [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) primero conviene ver si el índice se usa.
- **Indexar la transcripción.** Es la conversación entera; lo que dice qué dejó cada sesión son los resúmenes.

## 2. Análisis previo, línea base verificada

| Qué se verificó | Resultado |
|---|---|
| ¿Cuántos resúmenes hay? | **59**, del 2026-08-06 al 2026-08-22 |
| ¿Cuántos hallazgos escritos? | **345** |
| ¿Cuántos resúmenes no dejaron ninguno? | **6**, y eso también es un dato |
| ¿Qué forma tienen? | `### H-N · tema`, uniforme en los 59 |

### 2.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| [`validadores/temas.py`](../../../../../validadores/temas.py) | Nuevo: recoge los hallazgos, genera el índice y dice si quedó atrás |
| [`validadores/validar.py`](../../../../../validadores/validar.py) | Gana el subcomando `temas`, con `--aplicar` |
| [`validadores/tests/test_el_historico_se_busca_por_tema.py`](../../../../../validadores/tests/test_el_historico_se_busca_por_tema.py) | Nuevo: siete casos |
| [`historico-chat/resumenes/indice-tematico.md`](../../../../../historico-chat/resumenes/indice-tematico.md) | Nuevo: generado, 345 hallazgos |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |

### 2.2 Las trece preguntas, en corto

| # | Respuesta |
|---|---|
| 1-3 | Un índice temático generado del histórico; lo usa quien busca por qué se decidió algo |
| 4-5 | §1; fuera quedan agrupar temas y enganchar el disparo |
| 6-8 | No hay datos ni interfaz: lee `.md` y escribe uno |
| 9 | §2.1 |
| 10 | `python validadores/validar.py temas --aplicar`, y el archivo queda junto a los resúmenes |
| 11 | No aplica porque escribe un solo archivo del propio repositorio |
| 12 | No aplica porque no cambia ninguna norma |
| 13 | [plan_pruebas.md](plan_pruebas.md) |

### 2.3 Dudas por resolver

**Ninguna abierta.** Que fuera generado y no a mano lo decidió el pendiente 33 con su evidencia.

## 3. Tareas

| # | Tarea | Estado |
|---|---|---|
| T-01 | Escribir `temas.py`: recoger, generar, y decir si quedó atrás | ☑ |
| T-02 | Enchufarlo como subcomando con `--aplicar` | ☑ |
| T-03 | Escribir los siete casos, con el de la generación estable | ☑ |
| T-04 | Generar el índice del repositorio | ☑ |
| T-05 | Correr todo y versionar | ☑ |

## 4. Riesgos

| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que el archivo cambie en cada corrida y ensucie el control de versiones | `CP-05`: generar dos veces sobre lo mismo da un archivo idéntico |
| B-02 | Que detenga una corrida por estar desactualizado | Es **aviso**, nunca falla: un índice atrasado informa mal, no rompe nada |
| B-03 | Que alguien lo edite a mano y pierda su trabajo | La cabecera del propio archivo lo dice: se genera, y el próximo generado pisa lo escrito |
