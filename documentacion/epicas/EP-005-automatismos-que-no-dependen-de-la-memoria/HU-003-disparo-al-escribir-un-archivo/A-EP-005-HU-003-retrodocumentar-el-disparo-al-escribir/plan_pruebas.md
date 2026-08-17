# Plan de Pruebas — Fase A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El enganche se mide, no se cambia.** El CA-03 se responde levantando qué hace hoy: ajustar el enganche que corre en **cada escritura** sin plan aprobado es riesgoso.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que la función que decide si el archivo le toca devuelva lo correcto | En memoria | Sí |
| Integración | Que al escribir un documento con enlace roto llegue el aviso | Carpeta temporal | Sí |
| Medición | Qué hace hoy el enganche con una falla y con un aviso | Carpeta temporal | No |

**Por qué se prueba la función que decide y no el disparo.** El riesgo `R-02`: atar la prueba a la herramienta que dispara la vuelve frágil. La función que decide está separada a propósito.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | El CA-02: el silencio ante lo que no le toca |
| Límites | ☑ | Documento de otra carpeta, y archivo que no es documento |
| Medición | ☑ | El CA-03, que hoy está a medias |

### 3.3 Técnicas de diseño de casos

- **El silencio pesa igual que el disparo** — un enganche que habla de más se apaga, y apagado no dispara nada. El CA-02 tiene tanta prioridad como el CA-01.
- **Silencio comprobado, no supuesto** — el caso verifica que el enganche **corrió** y no dijo nada, no que no corrió.
- **Casos en carpeta temporal** — escribir un enlace roto en el repositorio lo dejaría en rojo y estorbaría a las demás sesiones.
- **El CA-03 se mide antes de decidir** — se levanta qué hace hoy con una falla y con un aviso, y se compara contra lo que la HU pide. Si falta, se escribe qué falta: es un resultado, no un fracaso (riesgo `R-01`).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y los casos contra carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-01](../HU-003-disparo-al-escribir-un-archivo.md#ca-01--al-escribir-un-archivo-corre-la-comprobación) | [CP-001](#cp-001--el-documento-con-enlace-roto-produce-el-aviso-en-el-momento) | Funcional | Alta | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-disparo-al-escribir-un-archivo.md#ca-02--lo-que-no-le-toca-se-ignora-en-silencio) | [CP-002](#cp-002--lo-que-no-le-toca-se-ignora-y-el-enganche-corrió-igual) | Negativa | Alta | Sí | ☐ |
| HU-003 | [CA-03](../HU-003-disparo-al-escribir-un-archivo.md#ca-03--el-hallazgo-grave-detiene-el-resto-avisa) | [CP-003](#cp-003--qué-hace-hoy-con-una-falla-y-con-un-aviso) | Medición | Crítica | No | ☐ |
| HU-003 | RNF — que el enganche no se vuelva ruido | [CP-002](#cp-002--lo-que-no-le-toca-se-ignora-y-el-enganche-corrió-igual) | Negativa | Alta | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El documento con enlace roto produce el aviso en el momento

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal con la estructura que el enganche revisa |
| **Datos de entrada** | Un documento con un enlace a un archivo que no existe |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento con el enlace roto | El aviso llega en el momento, no en la corrida siguiente |
| 2 | Comprobar que el aviso dice cuál es el enlace y dónde | Lo dice |
| 3 | Arreglar el enlace y volver a escribir | No llega aviso |
| 4 | Comprobar que la escritura se completó en los dos casos | El documento quedó escrito |

**Resultado esperado final:** el defecto se arregla en el momento, mientras el contexto todavía está.

---

### CP-002 — Lo que no le toca se ignora, y el enganche corrió igual

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un archivo que no es documento, y un documento fuera de la carpeta revisada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el archivo que no es documento | No reporta nada |
| 2 | Comprobar que el enganche **corrió** y decidió callar | Corrió: el silencio es una decisión |
| 3 | Comprobar que no falló | Sin excepción |
| 4 | Escribir un documento fuera de la carpeta revisada | Tampoco dispara |
| 5 | Escribir uno dentro de la carpeta | Ahora sí: la diferencia es dónde está |

**Resultado esperado final:** el enganche no se vuelve ruido, y su silencio no es un programa que no llegó a mirar.

> **El paso 5 es el que da valor a los cuatro anteriores.** Sin él, el caso pasaría con un enganche desconectado.

---

### CP-003 — Qué hace hoy con una falla y con un aviso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Tipo** | Medición |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un enlace roto —que la línea de comandos trata como falla— y un índice desactualizado —que trata como aviso— |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Provocar el enlace roto y anotar qué hace el enganche | Queda anotado: si detiene, si avisa, si solo devuelve el detalle |
| 2 | Provocar el índice desactualizado y anotar qué hace | Queda anotado |
| 3 | Comparar los dos comportamientos entre sí | Se ve si el enganche distingue o trata todo igual |
| 4 | Comparar con lo que hace la línea de comandos con los mismos dos casos | Se ve la diferencia |
| 5 | Escribir qué le falta al enganche para cumplir el CA | Queda propuesto, no hecho |

**Resultado esperado final:** el CA-03 queda con su veredicto medido y, si no se cumple, con la lista de lo que falta.

> **Medir antes de cambiar.** El enganche corre en cada escritura: tocarlo sin saber qué hace es la forma de romper el flujo de todas las sesiones.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el enganche falle al escribir un archivo que no le toca | Inmediato — bloquearía toda escritura |
| **Alta** | Que no dispare al escribir un documento con enlace roto | Inmediato. El CA-01 queda en «No» |
| **Alta** | Que el CA-03 quede sin cumplir (riesgo `R-01`) | Se escribe qué falta y se propone: es un resultado, no un fracaso |
| **Media** | Que la prueba dependa de la herramienta que dispara (riesgo `R-02`) | Se prueba la función que decide, separada a propósito |
| **Baja** | Que otra sesión esté tocando `validadores/pruebas.py` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 3 de 3 |
| Archivos del repositorio dejados en rojo por la prueba | **0** |
| Escrituras bloqueadas por un fallo del enganche | **0** |
| Comportamiento del enganche ante falla y ante aviso | Medido y escrito |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
