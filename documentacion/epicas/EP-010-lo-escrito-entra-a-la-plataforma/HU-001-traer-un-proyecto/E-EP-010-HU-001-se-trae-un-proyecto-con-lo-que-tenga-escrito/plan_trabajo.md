# Plan de Trabajo — Fase E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito (módulo Importación)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito` |
| **Épica** | [EP-010 Lo escrito entra a la plataforma](../../epica.md) |
| **HU** | [HU-001 Traer un proyecto](../HU-001-traer-un-proyecto.md), una sola |
| **Módulo** | Importación |
| **Especificación** | [documentacion/importacion/spec.md](../../../../importacion/spec.md), aprobada el 2026-08-25 |
| **Versión del producto** | 1, fase E de ocho |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Traer a la plataforma la documentación que un proyecto ya tiene escrita, para empezar a gobernarlo sin rehacer su historia.

**Qué entra.** Recorrer la documentación del ciclo de vida del proyecto, reconocer cada documento por su molde, mostrar qué se va a traer **antes** de traerlo, y traerlo copiando. Y decir qué carpetas no se miraron.

**Qué no entra.** El reporte detallado de lo no reconocido, que es la fase F. Transformar lo que no tiene forma conocida. Tocar el proyecto de origen.

## 2. Análisis previo: línea base verificada

**La incertidumbre de esta fase se midió antes de planearla, y dejó de ser incertidumbre.** La especificación decía que no se sabía cuánta documentación se iba a reconocer, y que se sabría probando. Se probó, contando sobre el repositorio real:

| Dónde | Archivos | Reconocidos por su molde | Sin reconocer |
|---|---:|---:|---:|
| `documentacion/` | 969 | 966 | 3 |
| Todo el resto del proyecto | 590 | 50 | 540 |
| **Total** | **1559** | **1016 (65,2%)** | **543** |

**El 65,2% engaña, y por eso se partió el conteo.** Dentro de `documentacion/` el reconocimiento es del **99,7%**. Fuera de ahí cae a casi nada, y tiene explicación: `base/`, `plantillas/`, `historico-chat/` y `pendientes/` no son documentación del ciclo de vida. Son el cuerpo de reglas, los moldes, las conversaciones y el backlog. Otra cosa.

**Qué se decidió con eso.** El usuario eligió el 2026-08-25 que traer recorra **solo la documentación del ciclo de vida**, y que el reporte diga **qué carpetas no miró y por qué**. La alternativa era recorrer el proyecto entero, y el reporte habría salido con 540 líneas la primera vez: honesto y a la vez inútil, porque el ruido esconde los tres casos que sí importan.

**Los tres que no se reconocen en `documentacion/`, y qué son:**

| Archivo | Qué es | Tiene molde en el estándar |
|---|---|---|
| `senales.md` | El documento de señales del proyecto | Sí, `plantillas/senales.md` |
| `resultado_pruebas_2.md` | El resultado de un **segundo ciclo** de pruebas de una fase | Sí, el mismo molde de resultado |
| `2026-08-14-15.0.0.md` | Un registro de adopción de versión | Sí, `documentacion/versiones/` |

Los tres se agregan a la lista de moldes en esta fase: no son casos raros, son moldes que faltaban en la lista.

**Qué ya está construido y se usa tal cual.** El almacén con su comprobante, la auditoría, y el registro de proyectos con su carpeta de documentación.

### 2.1 Archivos que se crean o modifican

Archivos nuevos dentro de `plataforma/nucleo/importacion/`, y sus plantillas. Se modifican `config/settings/base.py` y `config/urls.py` para dar de alta el componente y sus rutas.

**Nada de esta fase escribe dentro de la carpeta del proyecto de origen.** Es `RN-1` de la especificación, y el caso de «que NO pase» del plan de pruebas.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Se recorre solo la documentación del ciclo de vida | Recorrer el proyecto entero | Decidido por el usuario el 2026-08-25, con el conteo a la vista: recorrer todo dejaba un reporte de 540 líneas donde los 3 casos reales se pierden |
| El reporte dice **qué carpetas no se miraron** | Callar lo que se saltó | `RN-4` de la especificación: nada se pierde en silencio. Saltarse carpetas sin decirlo es perder en silencio con otro nombre |
| El documento se reconoce por **su nombre y su ubicación** | Reconocerlo leyendo su contenido | El estándar fija los nombres de los documentos del ciclo (`02·F12.13`), así que el nombre **es** la forma. Adivinar por contenido es más frágil y más caro, y adivinar mal ensucia lo que sí sirve |
| Se copia el contenido, no se enlaza al archivo de origen | Guardar solo la ruta | La especificación §12 lo decide: si el proyecto se mueve o se borra, lo traído tiene que seguir sirviendo |
| Traer dos veces no duplica: se compara por su ruta de origen | Comparar por contenido | `RN-3`. La ruta dentro del proyecto es lo que identifica al documento; el contenido cambia cuando alguien lo edita, y seguiría siendo el mismo documento |
| Antes de traer se muestra qué se va a traer, y se confirma | Traer y avisar después | Es un cambio de estado (`00·N1`), y trae cientos de documentos de una vez |
| Si falla a mitad, no queda nada de esa pasada | Dejar lo que alcanzó a entrar | La especificación §6. Media importación es peor que ninguna: nadie sabe qué falta |

### 2.7 Dudas por resolver antes de escribir

Ninguna. La única que había —**qué se recorre**— se midió y la decidió el usuario el 2026-08-25, y quedó escrita arriba con su conteo.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Reconocer los documentos del ciclo por su molde | La lista de moldes, con los tres que faltaban |
| 2 | Recorrer la documentación del proyecto y decir qué se encontró | El recuento: cuántos de cada tipo, y cuántos sin reconocer |
| 3 | Mostrar qué se va a traer, y pedir confirmación | La pantalla, con el recuento y las carpetas que no se miran |
| 4 | Traer lo reconocido, copiando | Los documentos quedan en la plataforma, con su tipo y su origen |
| 5 | No duplicar al traer dos veces | La segunda pasada dice qué ya estaba |
| 6 | Que una falla a mitad no deje nada | Se descarta lo de esa pasada |
| 7 | Traer este mismo repositorio, y medir | El caso real, con sus números escritos |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6 → 7. La 7 va al final porque es la prueba de fuego: si el módulo no puede con este repositorio, no puede con nada.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-1` lo que sigue un molde queda adentro con su tipo | Se trae un proyecto de mentira con documentos de varios tipos |
| `CA-2` el proyecto de origen queda intacto | Se compara su carpeta archivo por archivo |
| `CA-3` traer dos veces no duplica | Se trae dos veces y se cuenta |
| `CA-4` lo no reconocido queda listado con su ruta | Se trae un proyecto con documentos que no siguen ningún molde |
| `CA-5` nada se transforma sin que el usuario lo diga | Se comprueba que lo traído dice lo mismo que el original |
| `CA-6` si todo se reconoció, se dice | Se trae un proyecto donde todo tiene molde |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Proyectos de mentira creados y borrados por la prueba.

**El caso real es este repositorio**, y se trae de verdad. No es un conejillo: traer no lo modifica, y eso lo comprueba el caso de «que NO pase» contando sus archivos antes y después.

## 7. Reversión

Se descarta la rama de la fase. Lo traído vive en `datos/proyectos/`, y borrarlo no toca ningún proyecto de origen, porque nunca se escribió en ellos.

## 8. Producción y migración

No aplica: no hay documentación traída todavía.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Importación está aprobada |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `00·N1` ningún cambio de estado sin aprobación | Se muestra qué se va a traer y se confirma |
| `01·C7` ante dos lecturas, preguntar | La única duda se midió y la decidió el usuario antes de escribir |
| `04·R4` no afirmar sobre lo que no se leyó | El reporte dice qué carpetas **no** se miraron |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que traer mil documentos sea lento o se quede sin memoria | Es la tarea 7. Se mide con el repositorio real, que es el caso más grande que hay |
| 2 | Que reconocer por nombre deje pasar un documento con el nombre correcto y otra forma adentro | Se acepta a sabiendas: el estándar fija los nombres, así que el nombre es la forma. Si aparece un caso, se declara como deuda |
| 3 | Que una falla a mitad deje media importación | Es la tarea 6, y su caso de prueba |
| 4 | Que el usuario confirme sin leer, porque son cientos de documentos | La pantalla muestra el **recuento por tipo**, no la lista entera. Un número por tipo se lee; mil líneas no |

## 11. Definition of Done

- ☐ Los documentos del ciclo se reconocen por su molde, incluidos los tres que faltaban.
- ☐ Se muestra qué se va a traer antes de traerlo, con las carpetas que no se miran.
- ☐ Lo reconocido queda adentro, con su tipo y su origen, diciendo lo mismo que el original.
- ☐ Traer dos veces no duplica.
- ☐ Una falla a mitad no deja nada de esa pasada.
- ☐ El proyecto de origen queda intacto, comprobado archivo por archivo.
- ☐ Traído este mismo repositorio, con sus números escritos.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los siete puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md).
