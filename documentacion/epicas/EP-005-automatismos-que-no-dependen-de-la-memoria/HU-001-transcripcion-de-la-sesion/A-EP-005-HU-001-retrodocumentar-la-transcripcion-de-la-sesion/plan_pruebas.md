# Plan de Pruebas — Fase A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El enganche no se toca.** Es lo que sostiene el registro de todas las sesiones; cambiarlo sin plan aprobado es tocar el único rastro que queda.

**Las sesiones de prueba corren contra carpeta temporal**, nunca contra `historico-chat/`: un rastro falso entre las sesiones reales es peor que no probar.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que la hora la ponga el reloj y no salga del texto del mensaje | En memoria | Sí |
| Integración | Que el archivo nazca con el primer mensaje y crezca solo | Carpeta temporal | Sí |
| Índice | Que la sesión tenga su línea, y que renombrarla la deje apuntando bien | Carpeta temporal | Sí |

**Por qué la hora se prueba sobre el programa y no sobre una sesión real.** Una sesión real da una sola hora, y esa hora coincidiría con cualquier implementación. La prueba tiene que **fallar** si alguien toma la hora del texto en vez del reloj.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | Un mensaje que **contiene** una hora escrita, para que no se confunda con la del reloj |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |
| Documento | ☑ | La constancia del defecto de la transcripción a mano |

### 3.3 Técnicas de diseño de casos

- **El mensaje que trae una hora escrita** — es el caso que distingue "la hora la pone el reloj" de "la hora sale del texto". Sin él, las dos implementaciones pasan igual.
- **La hora se comprueba por su origen, no por su formato** — el riesgo `R-02`: atar la prueba a cómo se ve escrita la fecha la rompe con el primer cambio de formato.
- **El defecto conocido, escrito como caso** — la transcripción a mano ya pasó **seis veces** con la orden escrita en el `CLAUDE.md`. Lo que falta no es otra orden: es que se note cuando vuelve a pasar. El caso comprueba que el archivo tiene un solo registro por intercambio.
- **Carpeta temporal, siempre** — arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, y las sesiones de prueba contra carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-transcripcion-de-la-sesion.md#ca-01--la-sesión-se-escribe-sola-desde-el-primer-intercambio) | [CP-001](#cp-001--el-archivo-nace-con-el-primer-mensaje-y-crece-solo) | Funcional | Crítica | Sí | ☐ |
| HU-001 | [CA-02](../HU-001-transcripcion-de-la-sesion.md#ca-02--cada-intercambio-lleva-su-hora-real) | [CP-002](#cp-002--la-hora-viene-del-reloj-no-del-texto-del-mensaje), [CP-003](#cp-003--cada-intercambio-queda-registrado-una-sola-vez) | Límites | Crítica | Sí | ☐ |
| HU-001 | [CA-03](../HU-001-transcripcion-de-la-sesion.md#ca-03--la-sesión-aparece-en-el-índice) | [CP-004](#cp-004--la-sesión-tiene-su-línea-en-el-índice-y-sobrevive-al-renombrado) | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF — que el registro no dependa de que el agente se acuerde | [CP-003](#cp-003--cada-intercambio-queda-registrado-una-sola-vez) | Documento | Alta | Parcial | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El archivo nace con el primer mensaje y crece solo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal, con su estructura de histórico vacía |
| **Datos de entrada** | Un mensaje corto, del estilo de un saludo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que la carpeta no tiene el archivo de la sesión | No lo tiene |
| 2 | Mandar el primer mensaje, aunque sea un saludo | El archivo nace, con ese mensaje |
| 3 | Comprobar que nadie tuvo que pedirlo | El enganche lo hizo solo |
| 4 | Esperar a que termine la respuesta del agente | Queda escrita al terminar |
| 5 | Comprobar que `historico-chat/` del repositorio no se tocó | Sin cambios |

**Resultado esperado final:** el registro empieza en el primer intercambio, no cuando alguien se acuerda.

---

### CP-002 — La hora viene del reloj, no del texto del mensaje

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna: se prueba el programa |
| **Datos de entrada** | Un mensaje que **contiene** una hora escrita, distinta de la real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Fijar la hora del reloj para la prueba | Queda fija y conocida |
| 2 | Pasar un mensaje que trae otra hora escrita en su texto | Se registra |
| 3 | Leer la hora del registro | Es la del reloj, no la del texto |
| 4 | Cambiar la hora del reloj y repetir | La del registro cambia con el reloj |
| 5 | Comprobar que la prueba no depende del formato de la fecha | Comprueba el origen, no cómo se ve |

**Resultado esperado final:** la hora es un dato del sistema, no una interpretación del texto.

> **El paso 2 es el que hace útil el caso.** Con un mensaje sin horas escritas, una implementación que lee el texto pasaría igual.

---

### CP-003 — Cada intercambio queda registrado una sola vez

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 y RNF |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Una sesión de prueba con varios intercambios |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mandar tres mensajes y esperar sus respuestas | Quedan tres intercambios |
| 2 | Contar los registros del archivo | Tres, ni uno más |
| 3 | Comprobar que ninguno está duplicado | Ninguno |
| 4 | Comprobar que ninguna hora es imposible o fuera de orden | Todas del reloj, en orden |
| 5 | Dejar escrito el defecto conocido: la transcripción escrita a mano por el agente | Atado al pendiente [29](../../../../../pendientes/29-la-transcripcion-se-escribio-dos-veces.md) |

**Resultado esperado final:** el duplicado que ya pasó seis veces se puede detectar contando, no releyendo.

> **Este caso convierte una orden en una comprobación.** La orden del `CLAUDE.md` estaba escrita las seis veces que el defecto ocurrió.

---

### CP-004 — La sesión tiene su línea en el índice, y sobrevive al renombrado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | La sesión de prueba y un nombre nuevo para ella |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que la sesión tiene su línea en el índice | La tiene |
| 2 | Comprobar que la línea apunta al archivo | Apunta |
| 3 | Renombrar la sesión | El archivo se mueve |
| 4 | Comprobar que la línea del índice se corrigió | Sigue apuntando bien |
| 5 | Comprobar que no quedó una línea huérfana con el nombre viejo | No quedó |

**Resultado esperado final:** el índice no se separa de la carpeta, ni siquiera al renombrar.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un intercambio no quede registrado | Inmediato. Se pierde el único rastro de la sesión |
| **Crítica** | Que la hora salga del texto del mensaje | Inmediato — es el defecto de las horas inventadas |
| **Alta** | Que un intercambio quede duplicado | Antes de cerrar; se anota contra el pendiente [29](../../../../../pendientes/29-la-transcripcion-se-escribio-dos-veces.md) |
| **Media** | Que la sesión de prueba escriba en `historico-chat/` (riesgo `R-01`) | Se detiene y se limpia: es un rastro falso entre sesiones reales |
| **Baja** | Que otra sesión esté escribiendo en el índice (riesgo `R-03`) | Se relee antes de escribir |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Intercambios registrados fuera de la carpeta temporal | **0** |
| Registros duplicados | **0** |
| Horas que no vienen del reloj | **0** |
| Líneas huérfanas en el índice | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
