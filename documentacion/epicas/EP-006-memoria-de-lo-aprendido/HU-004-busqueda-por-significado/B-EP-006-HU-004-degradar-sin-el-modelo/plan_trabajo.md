# Plan de Trabajo — Fase B-EP-006-HU-004-degradar-sin-el-modelo (módulo Memoria)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-004](../HU-004-busqueda-por-significado.md); las pruebas, en el `plan_pruebas.md` de esta fase.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-006-HU-004-degradar-sin-el-modelo` |
| **Épica** | [EP-006 Memoria de lo aprendido](../../epica.md) |
| **HU** | [HU-004 Buscar por significado con un modelo local y opcional](../HU-004-busqueda-por-significado.md) — una sola (`F12.1`) |
| **Complementa** | [`A-EP-006-HU-004`](../A-EP-006-HU-004-retrodocumentar-la-busqueda-por-significado/resultado_pruebas.md), que cerró en **No cumple** |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/B-EP-006-HU-004-degradar-sin-el-modelo` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐞 **Defecto**, y es el más grave de los que dejó la sesión del 2026-08-17. Con `numpy` y `model2vec` instalados y **el modelo ausente**, `cmd_search` termina con `LocalEntryNotFoundError` y **no devuelve nada** — se cae la búsqueda entera, incluida la parte léxica, que no necesita ni modelo ni red.

**CA de la HU que cubre esta fase**

| CA de HU-004 | Qué exige | Estado tras la fase A |
|---|---|---|
| [CA-02](../HU-004-busqueda-por-significado.md#ca-02--sin-el-modelo-la-búsqueda-sigue-funcionando) | **Sin el modelo**, la búsqueda por palabra funciona igual, y se dice que la otra no está | **En «No».** Sin las **librerías** sí; sin el **modelo**, se cae entera |
| Transversal · Privacidad | El contenido no sale de la máquina en ningún momento | **En «No».** El contenido no sale, pero cargar el modelo **abre una conexión** al repositorio remoto |

**Por qué una sola fase para los dos.** Los dos viven en el mismo punto —cómo se carga el modelo— y el arreglo del primero pasa por tocar `_cargar()`, que es donde está el segundo. Partirlos daría dos fases sobre la misma función.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que faltar el modelo degrade a búsqueda por palabra en vez de tumbarlo todo, y que cargarlo no salga a la red.

**Fuera de alcance:**

- **Mejorar la precisión.** La fase A midió que de cinco resultados dos sirven; cambiar eso es otra cosa.
- **Descargar el modelo automáticamente.** Si no está, se degrada y se dice — no se instala nada a espaldas de nadie.
- **La búsqueda por palabra.** Ya funciona y no se toca.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 leyendo `memoria/semantica.py` y corriendo el caso.

**Lo que ya existe:** `disponible()`, que comprueba que `numpy` y `model2vec` **importen**; el camino que degrada a léxica cuando devuelve `False`, con su aviso «semántica no instalada»; y la prueba en rojo esperado `test_con_dependencias_pero_sin_el_modelo_la_busqueda_no_se_cae`.

**Lo que no existe:**

1. **Que alguien compruebe que el modelo carga.** `disponible()` mira las librerías y nada más.
2. **Una red alrededor de la carga.** `cmd_search` llama a `semantica.indexar(con)` sin atrapar nada.
3. **El modo sin conexión al cargar.** `StaticModel.from_pretrained` consulta el repositorio del modelo cada vez.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `memoria/semantica.py` | Modificar | `_cargar()` en modo sin conexión; `disponible()` pasa a comprobar también que el modelo cargue, y recuerda el resultado |
| `memoria/memoria.py` | Modificar | `cmd_search` atrapa el fallo de la parte semántica y sigue con la léxica, diciéndolo |
| `memoria/pruebas.py` | Modificar | Destapar la prueba en rojo, y sumar el caso de la red cortada al cargar |
| `…/B-EP-006-HU-004-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-004-busqueda-por-significado.md` | Modificar | §8 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | La fila de HU-004 vuelve a quedar completa |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

`semantica.disponible()` la llaman `cmd_search` y las pruebas. **Cambiar qué comprueba cambia su significado**: pasa de «están las librerías» a «se puede buscar por significado», que es lo que quien la llama siempre quiso saber. `indexar()` y `buscar()` no cambian de firma.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica: es un programa de línea de comandos sobre una base local. **Lo que sí cambia es que deja de haber salida a la red**, que es la mitad del objetivo.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

`python memoria/memoria.py search "…"`. No cambia; cambia qué pasa cuando el modelo falta.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `disponible()` comprueba que el modelo **cargue**, no solo que las librerías importen | Dejarla como está y atrapar el error más arriba | Quien la llama pregunta «¿puedo buscar por significado?». Que responda que sí y después reviente es la causa exacta del defecto |
| El resultado se recuerda: se comprueba **una vez** por proceso | Comprobar en cada búsqueda | Cargar el modelo cuesta 5 s; hacerlo dos veces para preguntar lo mismo pagaría el precio dos veces |
| El modo sin conexión se fija al cargar, no con una variable de entorno global | Pedirle al usuario que exporte `HF_HUB_OFFLINE` | Una herramienta que exige configuración manual es defecto del estándar, no del usuario |
| Si el modelo falta, se **degrada y se dice** | Descargarlo | Instalar algo sin que nadie lo pida es lo contrario de opt-in |

### 2.7 Dudas por resolver antes de escribir

Ninguna. El escenario está reproducido, la causa medida y la prueba escrita.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-02 — Sin el modelo, la búsqueda sigue funcionando

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | `disponible()` comprueba que el modelo cargue, y recuerda el resultado | `memoria/semantica.py` | 2,0 |
| T-02 | `cmd_search` atrapa el fallo de la parte semántica, sigue con la léxica y lo dice | `memoria/memoria.py` | 1,5 |
| T-03 | Destapar `test_con_dependencias_pero_sin_el_modelo_la_busqueda_no_se_cae` | `memoria/pruebas.py` | 0,5 |
| T-04 | Caso: con el modelo ausente, la búsqueda devuelve lo mismo que la léxica **y avisa** | `memoria/pruebas.py` | 1,5 |

### Transversal · Privacidad — El contenido no sale de la máquina

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Cargar el modelo en modo sin conexión | `memoria/semantica.py` | 1,5 |
| T-06 | Caso: con el socket cortado —no caído, **cortado**— indexar y buscar funcionan igual | `memoria/pruebas.py` | 2,0 |

### Cierre

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 7 tareas · 10,5 horas.**

---

## 4. Secuencia de ejecución

T-05 primero: fijar el modo sin conexión cambia cómo falla la carga, y T-01 tiene que atrapar ese fallo. Después T-01 y T-02, que son el arreglo. T-03 y T-04 destapan y completan; T-06 comprueba la privacidad con el arreglo puesto. T-07 cierra.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| Exigencia | Método de verificación | Evidencia |
|---|---|---|
| CA-02 | Apuntar el modelo a uno inexistente y buscar: tiene que responder por palabra y avisar | T-03, T-04 |
| Transversal · Privacidad | Cortar el socket y comprobar que indexar y buscar funcionan sin intentar salir | T-06 |
| No regresión | Con el modelo presente, la búsqueda híbrida sigue dando lo mismo | T-07 |

---

## 6. Datos y ambiente de prueba

Bases temporales. **No se desinstala nada y no se borra la caché del modelo**: el escenario se arma apuntando `MEMORIA_MODELO` a uno que no existe. Desinstalar rompería el entorno de quien corre la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Lo que cambia es cómo se decide si hay semántica; deshacerlo devuelve el comportamiento anterior —incluido el defecto— y no deja datos que restaurar.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Ninguna base necesita migración. El cambio es **puro comportamiento**, y va en la dirección segura: donde antes se caía, ahora responde.

**Un proyecto que hoy funciona no nota nada:** si el modelo está, la búsqueda híbrida sigue igual.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`00·N6`](../../../../../base/00-nucleo-blindado.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`05·E1`](../../../../../base/05-errores-y-logging.md), [`08·T4`](../../../../../base/08-pruebas.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que comprobar la carga en `disponible()` haga lenta la primera búsqueda de cada proceso | Se nota al arrancar | Ya se pagaba: cargar el modelo cuesta 5 s la primera vez. Lo que se agrega es que se pague **una** vez y se recuerde | Abierto |
| R-02 | Que el modo sin conexión impida descargar el modelo la primera vez, en una máquina nueva | Nadie puede instalarlo | Se descarga con la orden `indexar`, que es explícita, o con la herramienta del modelo. La **búsqueda** no descarga nada | Abierto |
| R-03 | Que atrapar el fallo esconda un error distinto del que se busca | Se tapa un defecto real | Se atrapa el fallo **de la carga**, no cualquier excepción, y se dice en el aviso qué pasó | Abierto |
| R-04 | Que otra sesión esté tocando `memoria/` | Se mezcla el versionado | Se guarda solo lo propio | Abierto |

---

## 11. Definition of Done

- [ ] Con el modelo ausente, la búsqueda responde por palabra y **avisa** que el significado no está.
- [ ] Con el socket cortado, indexar y buscar funcionan igual.
- [ ] Con el modelo presente, la búsqueda híbrida da lo mismo que antes.
- [ ] La prueba de fallo esperado queda en verde **sin la marca**.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §8 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: es una fase de una sola sesión, y su avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
