# Plan de Trabajo — Fase B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente (módulo Instalador — el andamio)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos, y cómo se comprueba cada criterio antes de darlo por cumplido. Se aprueba antes de tocar nada. El requisito vive en la HU; las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente` |
| **Épica** | [EP-007 Instalación y actualización](../../epica.md) |
| **HU** | [HU-003 Crear la estructura de carpetas del trabajo](../HU-003-estructura-de-carpetas.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Instalador — el andamio |
| **Especificación del módulo** | N/A: la HU es la especificación (`02·F2`, como en la fase A) |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio del estándar trabaja sobre su rama principal, con el commit autorizado aparte |

**ORIGEN:** ✨ **Funcionalidad nueva.** Sale del [pendientes/hecho/el-andamio-levanta-la-historia-y-el-pendiente.md](../../../../../pendientes/hecho/el-andamio-levanta-la-historia-y-el-pendiente.md), que sale de preguntar cómo gastar menos: lo mecánico de la cadena lo puede hacer un programa.

**CA de la HU que cubre esta fase:**

| CA de HU-003 que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-003-estructura-de-carpetas.md#ca-04--la-historia-y-el-pendiente-nacen-con-su-esqueleto-y-sus-índices-puestos) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el andamio acepte dos unidades más, `hu` y `pendiente`, y deje el archivo desde su plantilla con los marcadores de contenido intactos y **las filas de los índices puestas en los dos sentidos**. Sin escribir contenido, como hoy con la fase.

**Fuera de alcance:**

- Redactar la historia o el pendiente: el criterio sigue siendo de quien escribe.
- Crear épicas: una épica nace pocas veces y con conversación.
- Decidir en qué sección temática del índice del backlog va el pendiente: el andamio lo deja en una sección «Sin agrupar», y moverlo es criterio.

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Leído el 2026-08-20:

- [validadores/andamio.py](../../../../../validadores/andamio.py): `crear(raiz, epica, hu, descripcion)` para la fase; `siguiente_consecutivo()` lee lo que hay en vez de contar; `main()` con tres argumentos posicionales.
- [validadores/pendientes.py](../../../../../validadores/pendientes.py) `proximo_libre(proyecto)`: el número siguiente del backlog; lo usa `validar.py pendientes`.
- [plantillas/ciclo-vida-proyectos/04-HU.md](../../../../../plantillas/ciclo-vida-proyectos/04-HU.md): `HU-000`, `«Épica padre»` y el resto con `«…»`. No hay plantilla para el pendiente propio del estándar: `pendiente-reportado.md` es el de un proyecto; la ficha que usan los pendientes 60 a 70 es la misma (Estado · Historia de usuario · De dónde sale · Proyecto de origen · El problema · Por qué importa · Qué falta · El límite · Cómo se sabrá que cerró).
- `documentacion/epicas/EP-005/epica.md` §9 tiene cuatro columnas (ID, Título, Prioridad, Estimación); la plantilla trae seis. El andamio lee la cabecera real.
- `pendientes/README.md`: secciones temáticas `###` con tablas de cuatro columnas, y el mapa «Ningún pendiente vive suelto» con una fila por historia.
- `documentacion/epicas/EP-005/README.md` y los README de HU: tabla `Qué | De qué se trata` con enlaces `DOC14`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/andamio.py` | Modificar | `crear_hu()`, `crear_pendiente()`, `siguiente_hu()`, las filas de índice; `main()` con los modos `hu` y `pendiente`, y el de fase intacto |
| `plantillas/pendiente.md` | Nuevo | El molde del pendiente propio del estándar, con la ficha que ya usan los últimos once |
| `plantillas/README.md` | Modificar | La fila del molde nuevo |
| `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` | Nuevo | Los casos |
| `CHANGELOG.md` · `VERSION` | Modificar | Entra en la 27.2.0; el molde nuevo es lo que la hace MENOR |

### 2.2 Matriz de dependencias del refactor

No aplica porque no cambia el contrato de ningún código existente: lo que ya llamaba a estos programas sigue llamándolos igual.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica porque no hay servicio: son programas de línea de comandos que corren en la máquina de quien trabaja.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica porque no hay interfaz: el resultado se ve como texto en la consola o en la sesión.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Un molde `plantillas/pendiente.md` | Escribir la ficha dentro del andamio | El andamio no escribe contenido; la forma del pendiente es un molde como los demás, y hoy se copiaba a mano del anterior |
| La fila del backlog va a una sección «Sin agrupar» al final de «Abiertos» | Pedir la sección por argumento | Agrupar es criterio; el andamio deja la fila donde no estorba y quien escribe la mueve |
| El número de columnas del §9 se lee de la cabecera real | Asumir las seis de la plantilla | EP-005 tiene cuatro; escribir seis rompería la tabla |
| Los tres modos en un solo programa | Tres programas | Es el mismo trabajo a tres alturas de la cadena, y el andamio ya es el que se pide por nombre |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Todo lo que el plan afirma se leyó en el código el 2026-08-20.

## 3. Desglose de tareas por criterio de aceptación

### CA-04 — en la HU: [CA-04](../HU-003-estructura-de-carpetas.md#ca-04--la-historia-y-el-pendiente-nacen-con-su-esqueleto-y-sus-índices-puestos)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `plantillas/pendiente.md` y su fila en el README de plantillas | Plantilla | 0,25 h | — | EV-01 |
| T-02 | `crear_hu()`: número siguiente, carpeta, documento desde `HU.md`, README de la HU, fila en el §9 de la épica y en su README | Validador | 1 h | — | EV-01 |
| T-03 | `crear_pendiente()`: número de `pendientes.proximo_libre`, archivo desde el molde, fila en el backlog y en el mapa de historias | Validador | 1 h | T-01 | EV-01 |
| T-04 | `main()` con los tres modos, sin cambiar la llamada de la fase | Validador | 0,25 h | T-02, T-03 | EV-01 |
| T-05 | Los casos, sobre una copia temporal del árbol | Prueba | 1 h | T-04 | EV-01 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-02 → T-04 → T-05. **Paralelizable:** T-01 y T-03 con T-02.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo detiene la ejecución y amplía el plan con el OK del usuario.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| [CA-04](../HU-003-estructura-de-carpetas.md#ca-04--la-historia-y-el-pendiente-nacen-con-su-esqueleto-y-sus-índices-puestos) | Casos sobre una copia temporal: la historia, el pendiente, las filas en los dos sentidos, y los tres validadores limpios | EV-01 | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite | `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` |

## 6. Datos y ambiente de prueba

Una copia temporal de `plantillas/`, de una épica real y de `pendientes/README.md`, para que los índices reales tengan contra qué compararse sin tocarse.

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Se revierte el commit. El modo de fase no cambia de llamada, así que nada instalado se entera.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12

No aplica a los proyectos instalados: el andamio corre en el repositorio donde vive la cadena. Entra en la **27.2.0 (MENOR)**.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md); `13·DOC15` y `13·DOC16` (la historia se parte de la plantilla central) y `13·DOC17` (cada carpeta con su README).

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Dos sesiones pidiendo número a la vez (`20·M18`) | Números repetidos | El número se lee del disco en el momento de escribir, como hace `siguiente_consecutivo` | Abierto por diseño |
| B-02 | Que el índice del backlog tenga una forma que el programa no encuentre | La fila no entra | Si no encuentra la sección, la crea antes del mapa; con caso | Abierto |

## 11. Definition of Done

- [ ] CA-04 verificado con evidencia
- [ ] `validadores/tests/` y `validadores/pruebas.py` en verde
- [ ] Mapa del sitio al día (el molde nuevo)
- [ ] Señal registrada
- [ ] Listo para el commit único del día, que el usuario autoriza aparte

## 12. Seguimiento diario

N/A: el trabajo lo lleva una sola persona y el avance va en el `estado-fase.md` §1.2.

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
