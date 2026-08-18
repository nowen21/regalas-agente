# Plan de Pruebas — Fase B-EP-006-HU-004-degradar-sin-el-modelo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso** — y en este molde, eso incluye los **transversales**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-006-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-006-HU-004-degradar-sin-el-modelo` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

**Condición de arranque.** Bases temporales. **No se desinstala nada ni se borra la caché del modelo:** el escenario se arma apuntando `MEMORIA_MODELO` a uno que no existe.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Degradación | Que faltar el modelo no tumbe nada | Base temporal, modelo apuntado a uno inexistente | Sí |
| Red | Que cargar y buscar no salgan a la red | Base temporal, socket cortado | Sí |
| No regresión | Que con el modelo presente todo siga igual | Base temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-02 |
| Límites | ☑ | Modelo ausente, librerías ausentes, y las dos cosas |
| Seguridad | ☑ | El transversal de privacidad |
| Rendimiento | ☑ | Que comprobar la carga se pague una vez |
| No regresión | ☑ | La búsqueda híbrida con el modelo presente |

### 3.3 Técnicas de diseño de casos

- **Los dos escenarios se prueban por separado**, porque la fase A demostró que no son el mismo: «sin las librerías» funciona y «sin el modelo» se cae. Un solo caso los habría confundido otra vez.
- **La red se corta, no se simula caída.** Con un fallo de conexión, la caché local responde y el caso pasaría aunque el programa saliera a la red. **Cortar el socket hace que salir sea un fallo de la prueba.** Es la diferencia que la fase A descubrió a golpes.
- **El modelo ausente se simula apuntando a uno inexistente**, no borrando la caché: borrarla rompería el entorno de quien corre la prueba y obligaría a descargar 8 MB para volver a pasarla.
- **Se comprueba que avisa, no solo que no se cae.** Degradar en silencio es peor: el usuario cree que buscó por significado.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | [CA-02](../HU-004-busqueda-por-significado.md#ca-02--sin-el-modelo-la-búsqueda-sigue-funcionando) | [CP-001](#cp-001--sin-el-modelo-la-búsqueda-responde-por-palabra-y-lo-dice), [CP-002](#cp-002--los-tres-escenarios-de-ausencia) | Funcional | Crítica | Sí | ☐ |
| HU-004 | **Transversal · Privacidad** | [CP-003](#cp-003--transversal-de-privacidad-nada-sale-a-la-red) | Seguridad | Crítica | Sí | ☐ |
| HU-004 | **Transversal · Rendimiento** | [CP-004](#cp-004--transversal-de-rendimiento-la-comprobación-se-paga-una-vez) | Rendimiento | Media | Sí | ☐ |
| HU-004 | RNF · Degradación | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-004 | No regresión | [CP-005](#cp-005--con-el-modelo-presente-todo-sigue-igual) | Regresión | Crítica | Sí | ☐ |

**Cobertura:** el CA que la fase cubre, su RNF, **los dos transversales** y la no regresión = 100%.

---

## 6. Casos de prueba

### CP-001 — Sin el modelo, la búsqueda responde por palabra y lo dice

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-004 / CA-02 · RNF Degradación |
| **Tipo** | Funcional · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con señales; `MEMORIA_MODELO` apuntado a uno inexistente |
| **Datos de entrada** | Una búsqueda normal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar sin pedir modo léxico | **Responde**, no se cae |
| 2 | Comparar con lo que devuelve el modo léxico explícito | Lo mismo |
| 3 | Comprobar que **avisa** que el significado no está disponible | Lo avisa |
| 4 | Comprobar que la base real no se tocó | Intacta |

**Resultado esperado final:** faltar el modelo cuesta el significado, no la memoria.

> **El paso 3 es tan importante como el 1.** Degradar en silencio es peor que caerse: el usuario cree que buscó por significado y no encontró nada, cuando en realidad no buscó.

---

### CP-002 — Los tres escenarios de ausencia

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-004 / CA-02 · Transversal de límites |
| **Tipo** | Límites · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con señales |
| **Datos de entrada** | Los tres escenarios |

**Pasos**

| # | Escenario | Resultado esperado |
|---|---|---|
| 1 | **Sin las librerías** (`disponible()` apagado) | Responde por palabra y avisa «semántica no instalada» |
| 2 | **Con librerías, sin el modelo** | Responde por palabra y avisa que el modelo no está |
| 3 | **Con librerías y con modelo** | Búsqueda híbrida |
| 4 | En los tres, comprobar el código de salida | Cero en los tres |

**Resultado esperado final:** los tres escenarios están definidos y ninguno tumba nada.

> **Son tres, no dos.** La fase A los trató como uno y por eso el defecto pasó: el plan solo escribió el escenario 1, que funciona.

---

### CP-003 — Transversal de privacidad: nada sale a la red

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-004 / **Transversal · Privacidad** |
| **Tipo** | Seguridad · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con señales, y el modelo presente |
| **Datos de entrada** | Indexar y buscar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cortar el socket, de forma que **conectarse sea un fallo de la prueba** | Queda cortado |
| 2 | Cargar el modelo | Carga, del disco |
| 3 | Indexar las señales | Indexa |
| 4 | Buscar por significado | Encuentra |
| 5 | Comprobar que ninguno de los tres intentó salir | Ninguno |

**Resultado esperado final:** el contenido no sale, y **el programa tampoco**.

> **La diferencia con el caso de la fase A.** Aquel cortaba la red haciendo fallar la conexión, y el `hub` degradaba a la caché: el caso pasaba **aunque el programa saliera**. Este hace que salir sea el fallo. Es la única forma de comprobar «ninguna conexión» en vez de «funciona sin red».

---

### CP-004 — Transversal de rendimiento: la comprobación se paga una vez

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-004 / **Transversal · Rendimiento** |
| **Tipo** | Rendimiento · **Prioridad** Media |
| **Precondiciones** | Base temporal con señales, modelo presente |
| **Datos de entrada** | Varias búsquedas seguidas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Preguntar dos veces si hay semántica | La segunda no vuelve a cargar el modelo |
| 2 | Medir la primera búsqueda y las siguientes | La primera puede tardar; las siguientes no |
| 3 | Anotar los dos tiempos, con su fecha | Quedan escritos |

**Resultado esperado final:** comprobar que el modelo carga no se paga en cada búsqueda.

> **La línea base de la fase A:** 5,02 s la primera, 0,009 s las siguientes. Si la segunda sube, el recuerdo del resultado no está funcionando.

---

### CP-005 — Con el modelo presente, todo sigue igual

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-004 / No regresión |
| **Tipo** | Regresión · **Prioridad** Crítica |
| **Precondiciones** | Base temporal, modelo presente |
| **Datos de entrada** | Las consultas de la fase A |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar con palabras distintas a las de la señal | La encuentra, como en la fase A |
| 2 | Comprobar que la híbrida no pierde lo que la léxica encontraba | No pierde nada |
| 3 | Correr `memoria/pruebas.py` completa | Verde |
| 4 | Comprobar que **no queda ningún `expectedFailure`** en la clase `BusquedaPorSignificado` | Ninguno |

**Resultado esperado final:** el arreglo no cambió lo que ya funcionaba.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que atrapar el fallo esconda un error distinto (riesgo `R-03`) | Inmediato. Se atrapa el de la carga, no cualquiera, y el aviso dice qué pasó |
| **Crítica** | Que la prueba toque la base real | Inmediato. Se detiene y se restaura |
| **Alta** | Que el modo sin conexión impida descargar el modelo la primera vez (riesgo `R-02`) | Se comprueba que `indexar` —que es explícito— sí pueda, y se escribe cómo se instala |
| **Media** | Que la segunda búsqueda tarde como la primera (riesgo `R-01`) | El recuerdo del resultado no funciona: se diagnostica |
| **Baja** | Que otra sesión esté tocando `memoria/` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — el CA, el RNF, **los dos transversales** y la no regresión |
| Casos ejecutados | 5 de 5 |
| Escenarios de ausencia que tumban la búsqueda | **0** de 3 |
| Escenarios que degradan **sin avisar** | **0** |
| Conexiones a la red al cargar, indexar y buscar | **0** |
| Segunda búsqueda, contra la primera | Que no se note |
| Pruebas con `expectedFailure` en la clase, al cerrar | **0** |
| Modelos descargados o borrados durante la prueba | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
