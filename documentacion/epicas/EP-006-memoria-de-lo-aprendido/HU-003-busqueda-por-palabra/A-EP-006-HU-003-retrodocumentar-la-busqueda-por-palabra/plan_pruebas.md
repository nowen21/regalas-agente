# Plan de Pruebas — Fase A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Condición de arranque.** Las pruebas corren sobre una **base temporal**. La base real tiene el aprendizaje del proyecto.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Búsqueda | Que la palabra buscada devuelva la señal y diga dónde está | Base temporal | Sí |
| Acentos | Que encuentre igual con acentos y sin ellos | Base temporal | Sí |
| Filtros | Que tipo y alcance devuelvan solo lo que corresponde | Base temporal | Sí |
| Sincronía | Que el índice de texto completo esté al día con la tabla | Base temporal | Sí |

**Por qué se prueba la sincronía y no solo el resultado.** Un índice desincronizado **responde**: responde mal, y eso es peor que no responder. El caso lo detecta agregando una señal y buscándola enseguida.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Límites | ☑ | Acentos, y la señal archivada |
| Integridad | ☑ | El índice contra la tabla |
| Negativa | ☑ | La archivada **no** aparece, y sigue existiendo |

### 3.3 Técnicas de diseño de casos

- **La señal recién guardada** — el caso de sincronía agrega una señal y la busca de inmediato. Si el índice no se actualizó, la búsqueda calla y el defecto queda a la vista.
- **Con acento y sin acento, en los dos sentidos** — se busca la palabra acentuada esperando la sin acentuar y al revés. Un índice que solo normaliza en una dirección pasaría la mitad de los casos.
- **La archivada existe y no aparece** — el caso comprueba las dos cosas: que la búsqueda no la devuelva y que la señal **siga en la base**. Archivar no es borrar.
- **Base temporal siempre** — arriba, y cada caso comprueba que la base real quedó intacta.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera, sobre bases temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-busqueda-por-palabra.md#ca-01--se-busca-por-palabra-y-aparece-dónde-está) | [CP-001](#cp-001--la-palabra-buscada-devuelve-la-señal-con-su-ubicación), [CP-002](#cp-002--encuentra-igual-con-acentos-y-sin-ellos) | Funcional | Alta | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-busqueda-por-palabra.md#ca-02--se-puede-filtrar-por-tipo-y-por-alcance) | [CP-003](#cp-003--los-filtros-de-tipo-y-alcance-devuelven-solo-lo-que-corresponde), [CP-004](#cp-004--la-señal-archivada-no-aparece-y-sigue-existiendo) | Funcional | Alta | Sí | ☐ |
| HU-003 | RNF — que la búsqueda no dependa de instalar nada | [CP-005](#cp-005--el-índice-está-al-día-y-nada-se-instaló) | Integridad | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La palabra buscada devuelve la señal, con su ubicación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Base temporal con señales de prueba |
| **Datos de entrada** | Una palabra que aparece en una señal y no en las otras |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la palabra | Devuelve la señal que la tiene |
| 2 | Comprobar que dice dónde está: archivo o área | Lo dice |
| 3 | Buscar una palabra que no está en ninguna | No devuelve nada, sin error |
| 4 | Comprobar que la base real no se tocó | Intacta |

**Resultado esperado final:** buscar sirve para llegar, no solo para saber que algo existe.

---

### CP-002 — Encuentra igual con acentos y sin ellos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Base temporal con una señal cuya palabra clave lleva acento |
| **Datos de entrada** | La palabra acentuada y la misma sin acentuar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la palabra **sin** acento | Devuelve la señal que la tiene acentuada |
| 2 | Buscar la palabra **con** acento | Devuelve la señal que la tiene sin acentuar |
| 3 | Comprobar que los dos resultados son el mismo conjunto | Lo son |

**Resultado esperado final:** el acento no decide si se encuentra lo que se guardó.

> **Los dos sentidos importan.** Un índice que normaliza solo al guardar, o solo al buscar, pasa la mitad de los casos.

---

### CP-003 — Los filtros de tipo y alcance devuelven solo lo que corresponde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Base temporal con señales de varios tipos y alcances |
| **Datos de entrada** | Señales de al menos dos tipos y dos alcances |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar sin filtro | Devuelve todas las que coinciden |
| 2 | Filtrar por un tipo | Devuelve solo las de ese tipo |
| 3 | Filtrar por un alcance | Devuelve solo las de ese alcance |
| 4 | Combinar los dos filtros | Devuelve la intersección |
| 5 | Filtrar por un tipo que no tiene señales | Devuelve vacío, sin error |

**Resultado esperado final:** los filtros acotan, y el vacío es un resultado válido.

---

### CP-004 — La señal archivada no aparece, y sigue existiendo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Base temporal con una señal marcada como archivada |
| **Datos de entrada** | Una señal archivada y otra vigente con la misma palabra |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar la palabra | Devuelve la vigente |
| 2 | Comprobar que la archivada **no** aparece | No aparece |
| 3 | Comprobar que la archivada **sigue en la base** | Sigue: archivar no es borrar |
| 4 | Desarchivarla y buscar otra vez | Ahora aparece |

**Resultado esperado final:** lo que dejó de aplicar no estorba, y no se pierde.

> **El paso 3 es el que separa archivar de borrar.** Con solo el paso 2, un programa que borra pasaría el caso.

---

### CP-005 — El índice está al día, y nada se instaló

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / RNF |
| **Tipo** | Integridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Base temporal recién creada |
| **Datos de entrada** | Una señal nueva, guardada durante la prueba |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar una señal nueva | Entra a la tabla |
| 2 | Buscarla de inmediato | Aparece: el índice se actualizó solo |
| 3 | Modificar su texto y buscar por la palabra nueva | Aparece |
| 4 | Borrar la señal y buscar | Ya no aparece |
| 5 | Comprobar que no hizo falta instalar nada para todo lo anterior | Nada instalado |

**Resultado esperado final:** la búsqueda funciona con lo que la base ya trae, y el índice no se queda atrás.

> **Un índice desincronizado responde mal**, y eso es peor que no responder (riesgo `R-01`).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la prueba toque la base real (riesgo `R-02`) | Inmediato. Se detiene y se restaura |
| **Crítica** | Que el índice quede desincronizado (riesgo `R-01`) | Se anota y se propone el arreglo: responder mal es peor que no responder |
| **Alta** | Que una señal archivada aparezca en la búsqueda | El CA-02 queda en «No» |
| **Alta** | Que archivar borre la señal | Inmediato — se pierde aprendizaje |
| **Media** | Que el acento cambie el resultado | Antes de cerrar |
| **Baja** | Que otra sesión esté tocando `memoria/pruebas.py` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Señales de la base real modificadas | **0** |
| Señales perdidas al archivar | **0** |
| Diferencias de resultado por acentos | **0** |
| Herramientas que hubo que instalar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
