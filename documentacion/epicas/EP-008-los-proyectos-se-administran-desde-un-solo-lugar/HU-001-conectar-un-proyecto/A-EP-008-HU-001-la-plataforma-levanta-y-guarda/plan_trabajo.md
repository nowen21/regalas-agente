# Plan de Trabajo — Fase A-EP-008-HU-001-la-plataforma-levanta-y-guarda (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-008-HU-001-la-plataforma-levanta-y-guarda` |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../../epica.md) |
| **HU** | [HU-001 Conectar un proyecto](../HU-001-conectar-un-proyecto.md) — una sola |
| **Módulo** | Proyectos |
| **Especificación** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), aprobada el 2026-08-25 |
| **Versión del producto** | 1, fase A de siete |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que la plataforma levante en la máquina del usuario y sea capaz de guardar y leer: la base sobre la que se construye todo lo demás.

**Qué entra.** El arranque de la aplicación, el almacenamiento en texto, el índice local reconstruible, y una comprobación de que lo guardado se puede volver a leer.

**Qué no entra.** Registrar un proyecto, que es la fase B. Ninguna pantalla más allá de lo mínimo para saber que la plataforma está viva.

## 2. Análisis previo — línea base verificada

**Qué se leyó antes de escribir.** La especificación del módulo Proyectos, el modelo de datos y las doce decisiones de arquitectura.

**Qué existe hoy que se parece.** En este repositorio hay una aplicación local que muestra documentos y lee una base de datos. **No es la plataforma**, y decidir si se aprovecha o se empieza de cero es la duda abierta de la sección 2.7.

### 2.1 Archivos que se crean o modifican

Archivos nuevos, en una carpeta propia de la plataforma. **Nada de esta fase toca `interfaz/`, ni la carpeta de un proyecto administrado, ni el cuerpo de reglas actual.** Lo que existe se conserva funcionando mientras la plataforma nueva no lo reemplace.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Se construye con Django, siguiendo [plantillas/estructura-proyecto-django.md](../../../../../plantillas/estructura-proyecto-django.md) | Solo lo que trae el lenguaje, sin marco | Decidido por el usuario el 2026-08-25: es el marco que ya conoce, y trae resueltas las pantallas que llegan en la versión 2 |
| La base del marco es el **índice**, no la fuente | Dejar que el marco guarde la verdad, como es su costumbre | `DA-01`. Es el error que tiene hoy la aplicación de `interfaz/`, y el que se vino a corregir |
| La base es un archivo local, sin servicio que levantar | La base que usa hoy `interfaz/`, que corre aparte | `DA-03` y `RNF-08` |
| Lo que se guarda queda como texto, y el índice se reconstruye | Guardar solo en base de datos | `DA-01`: el respaldo es el repositorio, no un volcado |
| El índice se puede borrar y rehacer sin perder nada | Que el índice sea la fuente | `RNF-04`: perder la base no pierde información |
| La aplicación no sale a la red | Cualquier servicio externo | `RNF-03` y `DA-03` |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | Cómo se resolvió |
|---|---|---|
| 1 | ¿Se construye sobre la aplicación local que ya existe, o desde cero? | **Desde cero**, decidido por el usuario el 2026-08-25, con lo que hay a la vista |
| 2 | ¿Qué base local se usa? | Una base en archivo, sin servicios que levantar. Queda resuelta por la 1: al empezar de cero, no se arrastra la que existía |

**Qué se encontró antes de decidir la 1.** La aplicación de `interfaz/` tiene 34 archivos y 838 líneas, con un módulo de proyectos ya construido: modelo con nombre, ruta, alcance, stack, activo y notas, más importar, exportar y un comando para registrar. Dos cosas chocan con lo aprobado: su base corre como servicio aparte, contra `DA-03` y `RNF-08`; y **la fuente está invertida**, porque la verdad vive en la base y el archivo de texto se genera desde ella, cuando `DA-01` pide lo contrario.

**Por qué se decidió empezar de cero, aun así.** Lo escrito sirve como referencia de qué se necesita, pero adaptarlo obligaba a invertir su fuente y a cambiarle la base, que es casi reescribirlo con la carga de lo viejo encima. Lo que existe queda donde está: esta fase no lo toca ni lo borra.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Resolver las dos dudas de la sección 2.7 | ✅ Resueltas el 2026-08-25, con su porqué escrito |
| 2 | Levantar la aplicación en la máquina, sin red | La plataforma responde |
| 3 | Guardar y leer un dato de prueba, en texto | Lo guardado se lee después de reiniciar |
| 4 | Construir el índice local y su reconstrucción | Borrar el índice y rehacerlo sin perder nada |
| 5 | Escribir cómo se levanta desde cero | Los pasos, probados en limpio |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5. La tarea 1 es una puerta: sin ella, las demás se harían dos veces.

## 5. Verificación de criterios de aceptación

Esta fase no cierra ningún criterio de `HU-001` por sí sola: construye la base sobre la que la fase B los cumple. Lo que sí verifica:

| Qué | Cómo |
|---|---|
| La plataforma levanta sin red | Se corre con la máquina desconectada |
| Lo guardado sobrevive al reinicio | Se guarda, se apaga, se vuelve a abrir |
| El índice se reconstruye | Se borra la base y se rehace desde el texto |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Datos de mentira creados y borrados por la prueba. Ninguna credencial real.

## 7. Reversión

Se descarta la rama de la fase. Nada de lo que hace esta fase toca proyectos, reglas ni documentación existente.

## 8. Producción y migración

No aplica: no hay datos previos de la plataforma.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Proyectos está aprobada |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `01·C7` ante dos lecturas, preguntar | Las dos dudas de la sección 2.7 detienen la fase |
| `03·D` datos | El índice es reconstruible; la fuente es texto |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que reutilizar lo que existe salga más caro que empezar de cero | Se mira antes de decidir, y queda escrito qué se encontró |
| 2 | Que la base local elegida no sirva para lo que viene | Se prueba la reconstrucción del índice en esta misma fase |
| 3 | Que la fase crezca más allá de una jornada | Si pasa, se parte: levantar y guardar por un lado, índice por otro |

## 11. Definition of Done

- ☐ Las dos dudas resueltas y escritas.
- ☐ La plataforma levanta sin red.
- ☐ Lo guardado se lee después de reiniciar.
- ☐ El índice se borra y se reconstruye sin perder nada.
- ☐ Escrito cómo se levanta desde cero, probado en limpio.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los cinco puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md).
