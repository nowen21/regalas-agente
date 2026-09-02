# Plan de Pruebas — Fase `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../HU-001-buscar-en-lo-conversado.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que lo conversado se encuentra por una palabra suya, que el índice se rehace desde el texto, que ninguna credencial queda en él, y —lo más importante— que **indexar no toca ni un archivo del histórico**.

### 1.2 Alcance

**Entra:** partir la transcripción en turnos, indexar, buscar, rehacer, y los dos silencios que hay que distinguir.

**No entra:** contar y agrupar lo repetido (`F-034`), ni la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas y los tres riesgos |
| [documentacion/medicion/spec.md](../../../../medicion/spec.md) | La excepción declarada a `DA-01` y el diccionario de las dos entidades |
| [plataforma/nucleo/seguridad/claves.py](../../../../../plataforma/nucleo/seguridad/claves.py) | El molde del puente hacia el estándar |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `historico.turnos` | Que reconozca los dos lados, en orden, y que **no invente** cuando no hay marcas |
| El puente | Que lea con la función del estándar, y que reviente si no la encuentra |
| Indexar | Sesión con mensajes · archivo ilegible · archivo sin marcas · carpeta que no existe · ruta perdida |
| Buscar | Palabra dicha · palabra nunca dicha · los dos lados de la conversación |
| Rehacer | Que vuelva completo, y que indexar dos veces no duplique |
| **El histórico** | Que no cambie **ningún** archivo |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Es el `CA-04`: se compara la carpeta entera, archivo por archivo, antes y después |
| **De partición** | Las cinco formas en que un archivo puede no ser lo que se espera |
| **De silencio** | «No encontré» y «no hay nada indexado» devuelven lo mismo y no significan lo mismo |
| **Sobre datos reales** | El histórico de este repositorio, que es volumen real: 329 archivos |
| **De no regresión** | Las dos baterías: la del estándar, porque se tocó `historico.py`, y la de la plataforma |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-004 | **Si indexar toca el histórico, se corrompe la única fuente** |
| Crítica | CP-005 | Una credencial en el índice es lo que `00·N6` no perdona |
| Alta | CP-001, CP-002 | Encontrar lo dicho y rehacer el índice |
| Media | CP-003, CP-006, CP-007 | Lo que sale mal, los dos silencios, y el volumen real |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/medicion/tests.py` y `validadores/tests/test_la_transcripcion_se_parte_en_turnos.py`. Y **las dos baterías completas**: la de la plataforma porque se agrega una aplicación, y la del estándar porque se toca `historico.py`.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados, y la especificación del módulo aprobada.
- El proyecto de este repositorio ya conectado a la plataforma.

### 4.2 Criterios de salida

- Los siete casos ejecutados.
- El histórico real indexado, con su cuenta y su tiempo escritos.
- **Cero archivos del histórico cambiados**, medido archivo por archivo.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **cambia un solo archivo del histórico**. No hay medio cumplimiento posible en ese criterio: la transcripción es la única fuente, se versiona, y un archivo tocado por un indexador es un daño que no se ve hasta que alguien lee.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| [CA-01](../HU-001-buscar-en-lo-conversado.md#ca-01--lo-conversado-se-encuentra-por-una-palabra-suya) | CP-001 | De partición |
| [CA-02](../HU-001-buscar-en-lo-conversado.md#ca-02--el-índice-se-puede-borrar-y-rehacer) | CP-002 | De recuperación |
| Lo que sale mal | CP-003 | De partición |
| [CA-04](../HU-001-buscar-en-lo-conversado.md#ca-04--indexar-no-toca-el-histórico) | CP-004 | **Que NO pase** |
| [CA-03](../HU-001-buscar-en-lo-conversado.md#ca-03--ninguna-credencial-queda-en-lo-indexado) | CP-005 | De seguridad |
| Transversal | CP-006 | De silencio |
| Volumen real | CP-007 | De rendimiento |

---

## 6. Casos de prueba

### CP-001 — Lo conversado se encuentra, y se ve en qué mensaje

- **Precondición:** un proyecto de mentiras con una sesión de dos turnos.
- **Acción:** indexar y buscar una palabra que se dijo.
- **Resultado esperado:** un resultado, que dice **quién** lo dijo, **qué** dijo y **de qué sesión** es.
- **Y los dos lados:** también se encuentra lo que dijo el agente. `F-034` va a contar sobre los dos.

### CP-002 — El índice se borra entero y vuelve completo

- **Acción:** indexar, borrar todo, rehacer.
- **Resultado esperado:** la misma cuenta de sesiones y de mensajes.
- **Y dos veces no duplica:** indexar el mismo proyecto dos veces deja una sola sesión.
- **Y una sesión que creció queda completa:** se le agrega un turno al archivo y al reindexar aparecen los dos.

### CP-003 — Lo que sale mal se dice

| Entrada | Se espera |
|---|---|
| Un archivo que no es UTF-8 | Se reporta **nombrándolo**, y el resto se indexa igual |
| Un archivo sin marcas de turno | Una sesión con cero mensajes. Cero es un dato, no un silencio |
| Un proyecto sin `historico-chat/` | Cuenta en cero, sin reventar |
| Un proyecto con la ruta perdida | Se dice, con la ruta que se buscó |
| `README.md` dentro del histórico | No se indexa: no es una sesión |

### CP-004 — Indexar no toca el histórico

- **Acción:** retratar la carpeta —nombre, tamaño y huella del contenido de **cada** archivo—, indexar, y volver a retratar.
- **Resultado esperado:** los dos retratos, idénticos.
- **Se retrata el contenido y no la fecha:** un programa puede reescribir el mismo texto y dejar la fecha igual. La huella no se deja engañar.
- **Y sobre el histórico de verdad**, no solo sobre uno de mentiras.

### CP-005 — Ninguna credencial queda en lo indexado

- **Acción:** pasarle a todo lo indexado el detector de secretos del estándar.
- **Resultado esperado:** ninguna credencial. Si aparece algo con forma de clave, se mira una por una y se dice qué era.
- **Se usa el detector del estándar y no una lista propia:** una lista escrita acá daría por limpio lo que no conozca.

### CP-006 — Los dos silencios se distinguen

- **Acción:** buscar algo que no se dijo, con índice lleno y con índice vacío.
- **Resultado esperado:** dos mensajes distintos. «No hay nada indexado» y «no encontré» devuelven la misma lista vacía y no significan lo mismo.

### CP-007 — Volumen real

- **Acción:** indexar el histórico de este repositorio y medir cuánto tarda.
- **Resultado esperado:** el número queda escrito, sea el que sea. Es el riesgo `B-01` del plan, y se cierra con un dato, no con una impresión.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La plataforma en esta máquina. Las pruebas automáticas usan carpetas temporales que ellas mismas borran; la corrida final usa el histórico real.

### 7.2 Datos de prueba

Transcripciones escritas por la propia prueba, con el mismo formato que el enganche escribe.

### 7.3 Usuarios de prueba

No aplica.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**El histórico real no es un dato de prueba: es la fuente.** Se lee, y el `CP-004` comprueba que quede intacto. Ninguna prueba escribe dentro de `historico-chat/`.

**Y no se reproduce una sesión escrita por fuera del enganche.** Si algún día una conversación no pasa por ahí, no se indexa y nadie se entera. Está declarado como supuesto en la historia; esta fase no lo resuelve.

---

## 8. Herramientas

El corredor de pruebas de Django y `unittest`. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un archivo del histórico cambia · una credencial queda indexada |
| **Alta** | Un archivo se salta en silencio · el índice no se rehace completo |
| **Media** | Los dos silencios se dicen igual |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` y se arregla en la fase si cabe en su alcance.

### 9.3 Contenido mínimo de un reporte

Qué se corrió, con qué entrada, qué salió y qué se esperaba.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Después |
|---|---|---|
| Formas de buscar en lo conversado | ninguna | una orden |
| Sesiones indexadas | 0 | lo que haya |
| Archivos del histórico cambiados al indexar | — | **0** |
| Cuánto tarda indexar lo acumulado | sin medir | queda escrito |

### 12.2 Dónde se miden

`resultado_pruebas.md` §2, con la salida del guion que las mide.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por buena la promesa de no tocar nada mirando solo la fecha | Se compara la huella del contenido, archivo por archivo |
| Dar por limpio lo indexado con una lista de claves propia | Se usa el detector del estándar |
| Probar solo con transcripciones inventadas | El `CP-004` y el `CP-007` corren sobre el histórico real |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-31 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
