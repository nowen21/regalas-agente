# Plan de Trabajo — Fase B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-011 Dónde termina el estándar](../HU-011-donde-termina-el-estandar.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-011 Dónde termina el estándar](../HU-011-donde-termina-el-estandar.md), una sola |
| **Módulo** | Comprobaciones del repositorio, los mapas de `anatomia/` |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📝 **Modifica la fase `A`**, que hizo lo mismo con el otro mapa de `anatomia/`: el del amarre a la herramienta. Este cubre el que faltaba.

**De dónde sale:** el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), donde quedó preguntado si el mapa del sitio se comprueba o se actualiza a mano

**CA que cubre:** el `CA-03` de la historia, que pide que lo escrito sobre la anatomía del repositorio no envejezca en silencio.

## 1. Objetivo y alcance

**Objetivo:** que una carpeta nueva del repositorio no pueda quedarse fuera del mapa del sitio sin que nadie se entere.

**La decisión era mano o programa, y se eligió programa** por lo que ya había pasado con el otro mapa: `anatomia/` estuvo fuera de la tabla del `CLAUDE.md` hasta el 2026-08-18, y nadie lo notó porque un mapa desactualizado **se lee igual de bien**; simplemente miente por omisión.

**Y la primera corrida lo confirmó:** cuatro carpetas existían sin estar en el mapa (`adaptadores/`, `analisis/`, `documentacion/`, `evals/`) y una que el mapa nombraba ya no existe (`diplomado-ia/`). El mapa decía que el repositorio tenía doce carpetas y tiene dieciséis.

**Fuera de alcance:**

- **Comprobar que la descripción sea la acertada**, o que la carpeta esté en la zona correcta. Eso es un juicio y se lee; acá se comprueba que **esté nombrada**.
- **El segundo nivel del árbol.** Una carpeta nueva dentro de `base/` la reportan los índices de capítulo, que ya existen.
- **Los archivos sueltos de la raíz.** Un archivo nuevo en la raíz es raro y se ve; una carpeta nueva se pierde.

## 2. Análisis previo, línea base verificada

| Qué se verificó | Resultado |
|---|---|
| ¿Había un precedente construido? | **Sí:** [`amarre.py`](../../../../../validadores/amarre.py) hace exactamente esto con el mapa del amarre, y se reusa su forma: dos lados, falla y aviso |
| ¿Cuántas carpetas tiene el repositorio? | **16** de primer nivel, sin contar lo local y lo generado |
| ¿Cuántas nombraba el mapa? | **12.** Faltaban cuatro y sobraba una |
| ¿Qué queda fuera por diseño? | `.git`, `.venv`, `__pycache__`, `terceros`, `node_modules` y demás: no viajan ni se versionan |

### 2.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| [`validadores/sitio.py`](../../../../../validadores/sitio.py) | Nuevo: las dos formas de envejecer del mapa, más el recuento |
| [`validadores/validar.py`](../../../../../validadores/validar.py) | Gana el subcomando `sitio` |
| [`validadores/tests/test_el_mapa_del_sitio_no_envejece.py`](../../../../../validadores/tests/test_el_mapa_del_sitio_no_envejece.py) | Nuevo: siete casos |
| [`anatomia/mapa-del-sitio.md`](../../../../../anatomia/mapa-del-sitio.md) | Se pone al día con lo que la primera corrida encontró |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |

### 2.2 Las trece preguntas, en corto

| # | Respuesta |
|---|---|
| 1-3 | Una comprobación que mantiene honesto el mapa del sitio; la usa quien mantiene el estándar |
| 4-5 | §1; fuera quedan la calidad de la descripción y el segundo nivel |
| 6-8 | No hay datos ni interfaz: lee carpetas y un `.md` |
| 9 | §2.1 |
| 10 | `python validadores/validar.py sitio`, y en la ayuda del programa |
| 11 | No aplica porque solo lee |
| 12 | No aplica porque no cambia ninguna norma |
| 13 | [plan_pruebas.md](plan_pruebas.md) |

### 2.3 Dudas por resolver

**Ninguna abierta.** La única que había, mano o programa, la resolvió el pendiente 33 con su evidencia.

## 3. Tareas

| # | Tarea | Estado |
|---|---|---|
| T-01 | Escribir `sitio.py` con los dos lados y el recuento | ☑ |
| T-02 | Enchufarlo como subcomando de `validar.py` | ☑ |
| T-03 | Escribir los siete casos de prueba | ☑ |
| T-04 | Poner al día el mapa con lo que la primera corrida encontró | ☑ |
| T-05 | Correr todo y versionar | ☑ |

## 4. Riesgos

| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que reporte siempre y termine apagado | El caso `CP-04` exige que, nombrada la carpeta, se calle. Es el caso que decide |
| B-02 | Que confunda una carpeta local con una del estándar | La lista de lo que queda fuera se escribe una por una, no por patrón ancho |
| B-03 | Que un nombre parecido cuente por la carpeta real | `CP-07`: `mis-plantillas/` no cuenta como `plantillas/` |
