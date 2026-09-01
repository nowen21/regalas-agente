# Plan de Trabajo — Fase `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` (módulo Comprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` |
| **Épica** | [EP-015](../../epica.md) |
| **HU** | [HU-001 Comprobar un proyecto desde la plataforma](../HU-001-comprobar-un-proyecto-desde-la-plataforma.md) — **una sola** (`F12.1`) |
| **Módulo** | Comprobaciones |
| **Especificación del módulo** | [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md), aprobada el 2026-09-01 |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-020`, la primera de Comprobaciones. **Desbloquea la vuelta de la columna** entre `F-008`, `F-022` y `F-020`.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01. Las puertas 2 a 7 se pasaron con esa autorización.

**CA de la HU que cubre esta fase:**

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| CA-01 — Un proyecto que cumple pasa | ☑ |
| CA-02 — Uno que no cumple es rechazado, con archivo y línea | ☑ |
| CA-03 — Apuntada a algo que no le corresponde, lo dice | ☑ |
| CA-04 — Comprobar no modifica nada | ☑ |
| CA-05 — Cero comprobaciones corridas es rojo | ☑ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que se pida el veredicto de un proyecto desde la plataforma y salga con el archivo y la línea de lo que no cumple.

**No se escriben comprobaciones.** Se le pide al estándar que corra las suyas. Duplicarlas dejaría dos versiones que se separan, y la vieja daría por bueno lo que la nueva rechaza. Es la tercera vez que la plataforma usa esta forma: ya lo hace con el reconocedor de credenciales y con el que parte una conversación en turnos.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Cumple, y dice cuántas corrieron | Funcional | Media |
| CA-02 | No cumple, con archivo y línea | Funcional | Media |
| CA-03 | **Sin el estándar, no hay veredicto** | Funcional | **Alta** |
| CA-04 | No modifica nada | Funcional | Baja |
| CA-05 | **Cero es rojo** | Funcional | Baja |

**Fuera de alcance:**

- Corregir lo que encuentra, y escribir comprobaciones nuevas.
- Fijar el estado de una funcionalidad (`F-021`) y la puerta de publicación (`F-022`).
- Pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:**

| Pieza | Qué aporta |
|---|---|
| `validadores/validar.py` | El punto de entrada, con `todo --raiz <carpeta>` |
| `plataforma/nucleo/proyectos/models.py` | `ruta_codigo`, dónde vive cada proyecto |
| `plataforma/nucleo/seguridad/claves.py` | Tapa la salida antes de mostrarla |
| `validadores/corredor.py` | El molde: correr el punto de entrada de la otra parte en un proceso aparte |

**Lo verificado el 2026-09-01:**

| Qué se comprobó | Resultado |
|---|---|
| Comprobaciones que tiene el estándar | **32** |
| Sitios donde la plataforma las corría | **Ninguno** |
| Cómo reporta el estándar su resumen | `N comprobación(es) corridas · M con fallas` |
| Cómo reporta cada falla | `[FALLA] archivo:línea` y el motivo |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/comprobaciones/core.py` | Nuevo | Servicio | El puente y el veredicto |
| `plataforma/nucleo/comprobaciones/apps.py` | Nuevo | Config | |
| `plataforma/nucleo/comprobaciones/management/commands/comprobar.py` | Nuevo | Orden | Pedirlo desde la consola |
| `plataforma/nucleo/comprobaciones/tests.py` | Nuevo | Prueba | Los cinco CA |
| `plataforma/config/settings/base.py` | Modificar | Config | `nucleo.comprobaciones` en la lista |
| `documentacion/comprobaciones/spec.md` | Nuevo | Especificación | Módulo nuevo |

**Ninguna entidad y ninguna migración:** el veredicto se calcula al pedirlo.

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo. Usa `proyectos` y `seguridad`, y no los modifica.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Se corre el punto de entrada en un proceso aparte** | Importar los módulos del estándar | Es como se corren de verdad. Importarlos da un número que nadie más obtiene, y ata la plataforma a los adentros del estándar |
| **«Sin comprobar» es una respuesta propia** | Devolver rojo | Confundirla con «no cumple» hace que nadie mire los rojos de verdad |
| **Cero comprobaciones es rojo** | Tratarlo como verde | Una corrida que no comprobó nada y termina bien es un silencio que se lee como éxito |
| **La salida se tapa antes de devolverla** | Mostrarla tal cual | Trae fragmentos de los archivos del proyecto, y uno puede traer una clave |
| **El veredicto no se guarda** | Guardarlo en la base | El proyecto cambia y el veredicto envejece sin avisar (`DA-01`) |
| **El resumen se lee del texto que el estándar imprime** | Pedirle una salida en otro formato | Habría que cambiar el estándar. Su resumen ya es estable y está probado |

### 2.7 Dudas por resolver antes de codificar

Ninguna. La vuelta de la columna se resolvió antes de abrir la épica.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Comprobar que el proyecto exista y tenga el estándar | Servicio | 1 h | — | CA-03 | EV-01 |
| T-02 | Correr el punto de entrada en un proceso aparte | Servicio | 2 h | T-01 | CA-01 | EV-01 |
| T-03 | Leer el resumen y las fallas, con archivo y línea | Servicio | 2 h | T-02 | CA-02 | EV-01 |
| T-04 | Tapar la salida antes de devolverla | Servicio | 1 h | T-03 | — | EV-01 |
| T-05 | El veredicto, con «cero es rojo» adentro | Servicio | 1 h | T-03 | CA-05 | EV-01 |
| T-06 | La orden de consola | Orden | 1 h | T-05 | Todos | EV-02 |
| T-07 | Las pruebas de los cinco CA | Test | 2 h | T-06 | Todos | EV-01 |
| T-08 | **Correrlo sobre este repositorio y medir cuánto tarda** | Medición | 1 h | T-06 | CA-01, CA-02 | EV-02 |

**Total estimado:** 11 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-06 → T-08.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Sobre este repositorio: que diga cuántas corrieron | EV-02 | 2026-09-01 | ☑ |
| CA-02 | Con un enlace roto real, mirar que salga la ruta y la línea | EV-02 | 2026-09-01 | ☑ |
| CA-03 | Con una carpeta sin `base/` registrada como proyecto | EV-01 | 2026-09-01 | ☑ |
| CA-04 | Retrato de la carpeta antes y después | EV-01 | 2026-09-01 | ☑ |
| CA-05 | Un veredicto de cero comprobaciones | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/comprobaciones/tests.py` |
| EV-02 | La corrida sobre este repositorio | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para las pruebas automáticas, y **este repositorio** para la medición. El módulo solo lee, así que no puede dañar nada.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: no escribe. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), y [`08`](../../../../../base/08-pruebas.md) por lo de que cero no es verde.
- Producto: `DA-01`, y las `RN-1` a `RN-6` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que tarde tanto que nadie lo pida** | Alto | Se mide sobre este repositorio y **el número queda escrito**, sea el que sea | Abierto hasta T-08 |
| B-02 | Que un proyecto sin el estándar dé un veredicto falso | **Alto** | Se detecta antes de correr | Cerrado por diseño |
| B-03 | Que la salida traiga una credencial | Alto | Se tapa antes de devolverla | Cerrado |
| B-04 | Que el estándar cambie su resumen y esto deje de leerlo | Medio | Si no aparece el resumen, se dice que no se pudo comprobar en vez de suponer que cumple | Cerrado |

---

## 11. Definition of Done

- [x] Los cinco CA verificados con evidencia
- [x] Este repositorio comprobado, **con el tiempo medido**
- [x] Comprobado que no modifica nada
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
