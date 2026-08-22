# Plan de Pruebas — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-013 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Ninguna fase cerrada se reabre.** Lo que la comparación destape sobre trabajo viejo se anota; corregirlo está fuera de alcance.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Comparación de archivos | Que un archivo tocado y no declarado se avise | Carpeta temporal con su control de versiones | Sí |
| Comparación de criterios | Que un criterio sin caso y un caso sin criterio se avisen | Carpetas temporales | Sí |
| Lectura | Si los pasos ejecutados fueron los del plan de pruebas | Tres fases cerradas de este repositorio | No |
| Robustez del formato | Cuántos de los planes existentes se pueden leer | Este repositorio | Parcial |

**De dónde salen los archivos tocados.** Del control de versiones. **No** de una lista escrita a mano: esa lista es justamente lo que el programa viene a reemplazar.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | Los CA-01 y CA-02, con su defecto sembrado |
| Robustez | ☑ | Formatos del §2.1 que el programa no entienda |
| Criterio humano | ☑ | El CA-03, si la duda 2 lo declara así |

### 3.3 Técnicas de diseño de casos

- **Avisar, no fallar, ante un formato desconocido** — los planes existentes llenan la tabla del §2.1 de varias formas. Fallar dejaría el repositorio en rojo por un formato viejo, y entonces nadie correría el programa.
- **Medir la legibilidad antes de confiar en el aviso** — el riesgo `R-01`: primero se mide **sobre los planes que hay** cuántos se pueden leer. Si son pocos, el aviso no significa nada.
- **Declarar que algo no se comprueba es un resultado** — el CA-03 compara prosa contra prosa. Si no es comprobable, se registra así en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md); dejarlo como pendiente indefinido no cierra la fase.
- **El par tocado / declarado** — sin el segundo lado, el caso pasaría con un programa que avisa por todo archivo tocado.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el subcomando nuevo sobre este repositorio y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-013 | [CA-01](../HU-013-comparar-el-plan-con-lo-hecho.md#ca-01--avisa-el-archivo-tocado-que-el-plan-no-declara) | [CP-001](#cp-001--el-archivo-tocado-y-no-declarado-se-avisa-el-declarado-no), [CP-002](#cp-002--el-programa-avisa-en-vez-de-fallar-ante-un-formato-que-no-entiende) | Negativa | Crítica | Sí | ☐ |
| HU-013 | [CA-02](../HU-013-comparar-el-plan-con-lo-hecho.md#ca-02--avisa-el-caso-y-el-criterio-que-no-cuadran) | [CP-003](#cp-003--el-criterio-sin-caso-y-el-caso-sin-criterio-se-avisan) | Negativa | Alta | Sí | ☐ |
| HU-013 | [CA-03](../HU-013-comparar-el-plan-con-lo-hecho.md#ca-03--avisa-el-caso-cuyos-pasos-no-son-los-del-plan) | [CP-004](#cp-004--los-pasos-ejecutados-contra-los-del-plan-en-tres-fases-cerradas) | Criterio humano | Alta | No | ☐ |
| HU-013 | RNF — que la comparación no dependa de la memoria de nadie | [CP-001](#cp-001--el-archivo-tocado-y-no-declarado-se-avisa-el-declarado-no) | Funcional | Alta | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El archivo tocado y no declarado se avisa; el declarado, no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-013 / CA-01 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 1 resuelta: contra qué se comparan los archivos tocados |
| **Datos de entrada** | Una fase de mentira con su plan, y una rama que toca archivos declarados y no declarados |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tocar solo archivos que el plan declara | No sale aviso |
| 2 | Tocar un archivo que el plan **no** declara | Sale el aviso, y nombra el archivo |
| 3 | Agregarlo al §2.1 del plan y volver a correr | Deja de avisar |
| 4 | Comprobar que la lista de tocados salió del control de versiones | No se le pidió a nadie que la escribiera |

**Resultado esperado final:** [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) deja de depender de que quien implementa se acuerde.

> **El paso 1 es el que da valor al 2.** Sin él, el caso pasaría con un programa que avisa por cada archivo tocado.

---

### CP-002 — El programa avisa en vez de fallar ante un formato que no entiende

| Campo | Valor |
|---|---|
| **HU / CA** | HU-013 / CA-01 |
| **Tipo** | Robustez |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los planes de trabajo que hay en el repositorio, con sus distintas formas de §2.1 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre todos los planes del repositorio | Corre hasta el final, sin excepción |
| 2 | Contar cuántos §2.1 se pudieron leer y cuántos no | Sale la cuenta, con su fecha |
| 3 | Comprobar que los que no se pudieron leer **avisan**, no fallan | Avisan |
| 4 | Comprobar que el aviso dice qué no pudo leer | Lo dice |
| 5 | Anotar la proporción legible | Si es baja, el aviso del CA-01 no significa nada todavía |

**Resultado esperado final:** se sabe cuánto vale el aviso antes de confiar en él.

---

### CP-003 — El criterio sin caso y el caso sin criterio se avisan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-013 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un plan de pruebas con un criterio sin caso, y otro con un caso que no cuelga de ningún criterio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el plan con el criterio sin caso | Sale el aviso, y nombra el criterio |
| 2 | Correr sobre el plan con el caso suelto | Sale el aviso, y nombra el caso |
| 3 | Correr sobre un plan completo | No sale ninguno |
| 4 | Anotar la cuenta de avisos de `F18` que hay hoy en el repositorio | Queda la línea base, con su fecha |

**Resultado esperado final:** la matriz de trazabilidad deja de revisarse a ojo.

---

### CP-004 — Los pasos ejecutados contra los del plan, en tres fases cerradas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-013 / CA-03 |
| **Tipo** | Criterio humano |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna. Es lectura, y no depende de las dudas |
| **Datos de entrada** | Tres fases cerradas, con su `plan_pruebas.md` y su `resultado_pruebas.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Por cada fase, poner los pasos del plan y los del resultado lado a lado | Quedan comparables |
| 2 | Decidir a mano si el resultado ejecutó lo que el plan decía | Cada fase con su veredicto |
| 3 | Anotar la diferencia que aparezca, con la fase | Queda citable; reabrir lo cerrado está fuera de alcance |
| 4 | Decidir si un programa podría hacer esta comparación | Sale una respuesta, fundada en lo que costó hacerla a mano |
| 5 | Registrar esa decisión en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) | Queda escrita, comprobable o no |

**Resultado esperado final:** el CA-03 queda decidido, aunque la decisión sea que no se puede comprobar con un programa.

> **El paso 4 sale del 2 a propósito.** Decidir si algo es automatizable después de hacerlo a mano vale más que decidirlo antes.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el programa falle ante un §2.1 con formato viejo | Inmediato — dejaría el repositorio en rojo y nadie lo correría |
| **Alta** | Que la mayoría de los §2.1 no se puedan leer (riesgo `R-01`) | Se mide y se dice: el aviso del CA-01 no vale hasta que la proporción suba |
| **Media** | Que la comparación delate incumplimientos de `F8` en fases cerradas (riesgo `R-02`) | Se anota. Reabrir lo cerrado está fuera de alcance |
| **Media** | Que el CA-03 quede sin decidir (riesgo `R-03`) | Es la duda 2; el registro admite declarar que algo no es comprobable |
| **Baja** | Avisos de `F18` en fases viejas | Se cuentan como línea base |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Corridas que fallan por un formato desconocido | **0** |
| Proporción de §2.1 legibles | Medida y anotada, con su fecha |
| Fases cerradas modificadas | **0** |
| Listas de archivos escritas a mano | **0** — salen del control de versiones |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
