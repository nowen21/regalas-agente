# Plan de Trabajo — Fase F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta (módulo Importación)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta` |
| **Épica** | [EP-010 Lo escrito entra a la plataforma](../../epica.md) |
| **HU** | [HU-002 Reportar lo no reconocido](../HU-002-reportar-lo-no-reconocido.md), una sola |
| **Módulo** | Importación |
| **Especificación** | [documentacion/importacion/spec.md](../../../../importacion/spec.md), aprobada el 2026-08-25 |
| **Versión del producto** | 1, fase F de ocho. **La última** |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que lo que no entró se pueda volver a mirar sin traer otra vez.

**Qué entra.** El reporte de lo no reconocido como documento guardado, con su fecha, enlazado desde el registro de auditoría, y visible desde la pantalla del proyecto.

**Qué no entra.** Adivinar la forma de lo no reconocido, que la especificación descarta. Corregir esos documentos, que es del usuario.

## 2. Análisis previo: línea base verificada

**Tres de los cuatro criterios ya están construidos y probados por la fase E.** Se comprobó antes de planear, que es la disciplina que las fases C, E y G dejaron:

| Qué pide la historia | Qué hay hoy | Qué falta |
|---|---|---|
| `CA-01` lo no reconocido se lista con su ruta y se dice cuántos | La pantalla lo muestra; lo prueba `CP-003` de la fase E | Nada del cálculo. Falta que **quede guardado** |
| `CA-02` no entra, y su archivo de origen no cambia | Lo prueban `CP-003` y `CP-009` de la fase E | Nada |
| `CA-03` si todo se reconoció, se dice | Lo prueba `CP-004` de la fase E | Nada |
| **Transversal: el reporte queda guardado con la acción de traer** | **Nada** | Todo. Es la fase |

### Por qué el transversal importa más de lo que parece

Al traer este repositorio, el registro de auditoría quedó así:

```
994 documento(s) reconocido(s), 1 sin reconocer
```

**Dice cuántos quedaron afuera. No dice cuáles.** Para saber que ese uno era `cvds/cumplimiento.md` hay que volver a traer el proyecto entero.

Eso choca con dos cosas escritas:

- **El propósito de la auditoría**, que es poder demostrar meses después qué pasó. Un número sin nombres no demuestra nada.
- **`RN-4` del módulo**, que dice que nada se pierde en silencio. No se pierde en la pantalla, pero sí en el registro, que es lo que queda.

### La decisión, y por qué no la otra

**El usuario eligió el 2026-08-25 que el reporte sea un documento propio**, guardado en la carpeta del proyecto dentro de la plataforma, con su fecha, y enlazado desde el registro de auditoría.

**La alternativa era meter la lista completa dentro del registro de auditoría.** Se descartó por dos razones:

1. Hoy este repositorio deja **una** ruta sin reconocer. Un proyecto que siga el estándar a medias puede dejar cientos, y el registro de auditoría quedaría ilegible justo cuando más falta hace.
2. Ya está decidido, desde la especificación de Auditoría, que **el registro guarda la acción y no el contenido**. El reporte es contenido.

**Qué se gana además.** El reporte queda como texto que se abre con cualquier editor, y **dos reportes de fechas distintas se pueden comparar** para ver qué se corrigió entre una traída y otra.

**Qué ya está construido y se usa tal cual.** El almacén, la auditoría con su comprobante, y el `Hallazgo` de la fase E, que ya calcula la lista de lo no reconocido.

### 2.1 Archivos que se crean o modifican

`plataforma/nucleo/importacion/` y sus plantillas.

**Nada de esta fase escribe dentro de la carpeta del proyecto de origen.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| El reporte es un documento guardado, no una fila del registro | Meter la lista en el registro de auditoría | Decidido por el usuario el 2026-08-25, con las dos razones de arriba |
| El reporte se escribe **siempre**, también cuando no quedó nada afuera | Escribirlo solo cuando hay algo que reportar | Un reporte que dice «no quedó nada» es una afirmación con fecha. Su ausencia no distingue entre «salió perfecto» y «no se corrió» |
| Cada traída escribe su propio reporte, con su fecha en el nombre | Sobrescribir uno solo | Poder comparar dos traídas es la mitad del valor: muestra qué se corrigió |
| El reporte se escribe **con el comprobante de la auditoría** | Escribirlo aparte | Es un documento que la plataforma guarda; pasa por el mismo camino que todo lo demás |
| El registro de auditoría **enlaza** el reporte por su ruta | Repetir la lista en los dos sitios | Dos copias de lo mismo se separan. El registro dice dónde mirar |
| El reporte dice también **qué carpetas no se miraron** | Solo lo no reconocido | Es la otra mitad de lo que no entró, y hoy solo se ve en la pantalla |

### 2.7 Dudas por resolver antes de escribir

Ninguna. La única que había se midió y la decidió el usuario antes de escribir el plan.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Escribir el reporte de una traída como documento, con su fecha | El archivo, legible sin la plataforma |
| 2 | Que el reporte diga lo no reconocido, con su ruta, y cuántos son | El contenido |
| 3 | Que diga también qué carpetas no se miraron, y por qué | La otra mitad |
| 4 | Que se escriba también cuando no quedó nada afuera | El reporte que dice que salió limpio |
| 5 | Enlazarlo desde el registro de auditoría | El registro dice dónde está |
| 6 | Verlos desde la pantalla del proyecto | La lista de reportes, del más nuevo al más viejo |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-01` lo no reconocido se lista con su ruta y cuántos son | Se trae un proyecto con documentos sin molde y se lee el reporte |
| `CA-02` no entra y el origen no cambia | Ya probado en la fase E; se vuelve a comprobar acá con el reporte de por medio |
| `CA-03` si todo se reconoció, se dice | Se trae un proyecto limpio y se lee su reporte |
| Transversal: el reporte queda guardado | Se trae, se cierra todo, y se vuelve a mirar el reporte sin traer otra vez |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Proyectos de mentira creados y borrados por la prueba. El caso real vuelve a ser este repositorio, que hoy deja **una** ruta sin reconocer.

## 7. Reversión

Se descarta la rama de la fase. Los reportes viven en `datos/`, y borrarlos no toca ningún proyecto.

## 8. Producción y migración

Las traídas anteriores a esta fase no tienen reporte. **No se inventa uno hacia atrás**: el reporte dice lo que se encontró en una traída concreta, y fabricarlo después sería afirmar sobre algo que no se observó. Basta con volver a traer.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Importación está aprobada |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `04·R4` no afirmar sobre lo que no se leyó | No se fabrican reportes de traídas pasadas |
| `20·M12` buscar antes de crear | Tres de los cuatro criterios ya estaban; por eso la sección 2 lo dice antes de planear |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que la fase parezca hecha porque tres de cuatro criterios ya estaban | Se declaró en la sección 2, y el plan de pruebas comprueba **los cuatro**, no solo el que falta |
| 2 | Que los reportes se acumulen sin límite | Uno por traída. Hoy no estorba; si algún día son cientos, se decide qué hacer y queda como deuda |
| 3 | Que el reporte y el registro digan cosas distintas | El registro no repite la lista: la enlaza. Una sola fuente |

## 11. Definition of Done

- ☐ Cada traída escribe su reporte, con su fecha, legible sin la plataforma.
- ☐ El reporte dice lo no reconocido con su ruta, y cuántos son.
- ☐ El reporte dice qué carpetas no se miraron, y por qué.
- ☐ Se escribe también cuando no quedó nada afuera, diciéndolo.
- ☐ El registro de auditoría enlaza el reporte.
- ☐ Los reportes se ven desde la pantalla del proyecto.
- ☐ Se puede volver a mirar un reporte sin traer otra vez.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los siete puntos de la sección 11 tengan veredicto. **Con ella cierra la versión 1**, así que el documento de cierre dice también qué quedó de la versión entera.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md).
