# Plan de Pruebas — Fase B-EP-006-HU-003-la-busqueda-dice-donde-esta   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso** — y en este molde, eso incluye los **transversales**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-006-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-006-HU-003-la-busqueda-dice-donde-esta` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> **Este plan cuenta los transversales.** La fase A de esta misma HU declaró «cobertura 100%» sin contarlos, y fue el defecto que arrastraron las 51 fases de la sesión del 2026-08-17. Acá tienen su fila y su caso.

**Condición de arranque.** Todo corre sobre **bases temporales**, y cada caso comprueba que `memoria/senales.db` quedó intacta.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Salida | Que la línea traiga la ubicación cuando la hay, y quede limpia cuando no | Base temporal | Sí |
| Recursos | Que ningún camino deje la base tomada | Base temporal | Sí |
| Regresión | Que lo que la fase A dejó en verde siga en verde | Base temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-01, en su mitad que faltaba |
| Límites | ☑ | La señal sin `where_`, y la búsqueda sin resultados |
| Recursos | ☑ | La conexión que no se cerraba |
| No regresión | ☑ | Las 16 pruebas que la fase A dejó en verde |

### 3.3 Técnicas de diseño de casos

- **Se destapan las pruebas que ya existen, no se escriben otras.** Las dos están escritas contra el criterio y describen el defecto; quitarles la marca es lo que convierte el rojo esperado en verde real. Escribir pruebas nuevas y borrar las viejas dejaría sin comprobar que el arreglo es **el que faltaba**.
- **El caso de la señal sin `where_` va aparte.** Sin él, el arreglo podría dejar un paréntesis vacío en cada línea de las señales que no lo tienen, y la prueba del caso feliz pasaría igual.
- **El cierre se prueba borrando el archivo**, no leyendo el código: en Windows no se puede borrar lo que está tomado, y así el descuido se ve en vez de deducirse.
- **Base temporal siempre**, con la huella de la real comparada en cada caso.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-busqueda-por-palabra.md#ca-01--se-busca-por-palabra-y-aparece-dónde-está) | [CP-001](#cp-001--la-búsqueda-dice-dónde-está-la-señal), [CP-002](#cp-002--la-señal-sin-ubicación-sale-limpia) | Funcional | Crítica | Sí | ☐ |
| HU-003 | RNF · Inocuidad | [CP-003](#cp-003--ningún-camino-deja-la-base-tomada) | Recursos | Alta | Sí | ☐ |
| HU-003 | **Transversal · Privacidad** | [CP-004](#cp-004--transversal-de-privacidad-el-contenido-no-sale-de-la-máquina) | Seguridad | Crítica | Sí | ☐ |
| HU-003 | **Transversal · Límites** | [CP-005](#cp-005--transversal-de-límites-la-memoria-vacía-y-el-término-imposible) | Límites | Alta | Sí | ☐ |
| HU-003 | No regresión | [CP-006](#cp-006--lo-que-la-fase-a-dejó-en-verde-sigue-en-verde) | Regresión | Crítica | Sí | ☐ |

**Cobertura:** el CA que la fase cubre, su RNF, **los dos transversales** y la no regresión = 100%.

---

## 6. Casos de prueba

### CP-001 — La búsqueda dice dónde está la señal

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / CA-01 |
| **Tipo** | Funcional · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con una señal guardada con `--where` |
| **Datos de entrada** | Una señal con `where_ = infra/redis.conf:12` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la palabra que la trae | Devuelve la señal |
| 2 | Comprobar que la línea trae la ubicación | Trae `infra/redis.conf:12` |
| 3 | Comprobar que sigue trayendo id, tipo, alcance y título | Los cuatro, sin perderse |
| 4 | Comprobar que la base real no se tocó | Intacta |

**Resultado esperado final:** el resultado alcanza para abrir lo que se encontró, que es como el CA-01 se da por aprobado.

> **Es la prueba de la fase A, destapada.** Si al quitarle la marca no pasa, el arreglo no era el que faltaba.

---

### CP-002 — La señal sin ubicación sale limpia

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / CA-01 |
| **Tipo** | Límites · **Prioridad** Alta |
| **Precondiciones** | Base temporal con una señal **sin** `where_` |
| **Datos de entrada** | Una señal guardada sin `--where` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la palabra que la trae | Devuelve la señal |
| 2 | Comprobar que **no** hay paréntesis vacíos ni separador suelto | La línea termina en el título |
| 3 | Buscar con las dos —una con ubicación y otra sin— | Cada una sale como le toca |

**Resultado esperado final:** agregar el dato a las que lo tienen no ensucia la salida de las que no.

> **Sin este caso, el CP-001 pasaría con un arreglo que deja `()` en la mitad de las líneas.** Una señal sin `where_` es normal: el criterio de `13·DOC5` no lo exige.

---

### CP-003 — Ningún camino deja la base tomada

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / RNF · Inocuidad |
| **Tipo** | Recursos · **Prioridad** Alta |
| **Precondiciones** | Base temporal con al menos una señal |
| **Datos de entrada** | Una búsqueda que encuentra y otra que no |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar algo que **no** está | Imprime «(sin señales relevantes)» |
| 2 | Borrar el archivo de la base | Se puede borrar |
| 3 | Repetir con una búsqueda que **sí** encuentra | Se puede borrar igual |
| 4 | Correr la clase entera **sin** `ignore_cleanup_errors` | Ninguna carpeta temporal queda sin borrar |

**Resultado esperado final:** los dos caminos de salida cierran lo que abrieron.

> **El paso 4 es el que cierra el defecto de verdad.** Mientras la clase necesite `ignore_cleanup_errors` para pasar, el descuido sigue ahí y solo está tapado.

---

### CP-004 — Transversal de privacidad: el contenido no sale de la máquina

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / **Transversal · Privacidad** |
| **Tipo** | Seguridad · **Prioridad** Crítica |
| **Precondiciones** | Base temporal con una señal |
| **Datos de entrada** | Una búsqueda léxica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cortar el socket, de forma que cualquier conexión falle | Queda cortado |
| 2 | Buscar | Encuentra igual |
| 3 | Comprobar que el arreglo no agregó ninguna salida a la red | Ninguna |

**Resultado esperado final:** agregar la ubicación a la salida no cambia que todo ocurre en la máquina.

> **Se prueba cortando la red, no leyendo el código:** si algo intentara salir, la prueba falla en vez de pasar callada.

---

### CP-005 — Transversal de límites: la memoria vacía y el término imposible

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / **Transversal · Límites** |
| **Tipo** | Límites · **Prioridad** Alta |
| **Precondiciones** | Una base temporal vacía, y otra con señales |
| **Datos de entrada** | Términos vacíos y de solo signos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en una memoria **vacía** | Responde sin error |
| 2 | Buscar con el término vacío, con espacios y con solo signos | Los tres dicen que el término está vacío, sin reventar |
| 3 | Comprobar que ninguno de los dos caminos deja la base tomada | No la dejan |

**Resultado esperado final:** los bordes siguen definidos después del arreglo.

---

### CP-006 — Lo que la fase A dejó en verde sigue en verde

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / No regresión |
| **Tipo** | Regresión · **Prioridad** Crítica |
| **Precondiciones** | La suite de la memoria |
| **Datos de entrada** | Las 16 pruebas que la fase A dejó pasando |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la clase `BusquedaPorPalabra` entera | Todas en verde |
| 2 | Comprobar que **no queda ningún `expectedFailure`** en la clase | Ninguno |
| 3 | Correr `memoria/pruebas.py` completa | Verde, con los fallos esperados que quedan de otras fases |

**Resultado esperado final:** el arreglo no rompió los acentos, los filtros, lo archivado ni la sincronía del índice.

> **El paso 2 es el que dice que la fase cerró.** Si queda una marca, es que uno de los dos defectos sigue ahí.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la prueba toque la base real | Inmediato. Se detiene y se restaura |
| **Alta** | Que al destapar una prueba siga en rojo | El arreglo no era el que faltaba: se diagnostica y se escribe qué salió |
| **Media** | Que la línea quede ilegible con rutas largas (riesgo `R-01`) | Se anota con la salida a la vista y se decide |
| **Baja** | Que otra sesión esté tocando `memoria/` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — el CA, el RNF, **los dos transversales** y la no regresión |
| Casos ejecutados | 6 de 6 |
| Pruebas con `expectedFailure` en la clase, al cerrar | **0** |
| Carpetas temporales que no se borran | **0**, sin `ignore_cleanup_errors` |
| Señales de la base real modificadas | **0** |
| Pruebas de la fase A que dejan de pasar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
