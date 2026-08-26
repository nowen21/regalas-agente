# Plan de Pruebas — Fase B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso** — y en este molde, eso incluye los **transversales**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-004-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

**Condición de arranque.** Árboles temporales. **Ningún archivo del repositorio se rompe para probar.**

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que la lectura tolere los cuatro casos | Carpeta temporal | Sí |
| Corrida completa | Que un archivo roto no impida reportar los demás | Árbol temporal | Sí |
| No regresión | Que los 357 casos que la usan sigan pasando | Este repositorio | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Errores | ☑ | El transversal que la fase A dejó en «No» |
| Límites | ☑ | Ausente, sin permisos, mal codificado y binario |
| Funcional | ☑ | Que el hallazgo alcance, y que avise en vez de detener |
| No regresión | ☑ | La suite entera |

### 3.3 Técnicas de diseño de casos

- **Lo que se mide no es que no reviente: es que la corrida siga y reporte lo demás.** Una lectura que devuelve vacío y una corrida que igual muere más arriba no arreglan nada.
- **El archivo roto se pone junto a uno bueno con un defecto conocido.** Si al final el defecto del bueno no aparece, el roto se llevó la corrida aunque nadie viera una traza.
- **Tolerar no es callar.** Cada caso comprueba que el archivo ilegible **aparece** en la salida, con su ruta.
- **Ningún archivo del repositorio se rompe:** el árbol se arma aparte.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, porque casi toda ella usa la lectura de forma indirecta.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | **Transversal · Errores** | [CP-001](#cp-001--la-lectura-tolera-los-cuatro-casos), [CP-002](#cp-002--la-corrida-sigue-y-reporta-lo-demás) | Errores | Crítica | Sí | ☐ |
| HU-003 | **Transversal · Límites** | [CP-001](#cp-001--la-lectura-tolera-los-cuatro-casos) | Límites | Alta | Sí | ☐ |
| HU-003 | [CA-01](../HU-003-formato-del-hallazgo.md#ca-01--el-hallazgo-alcanza-para-arreglar-sin-abrir-el-programa) | [CP-003](#cp-003--el-hallazgo-del-archivo-ilegible-dice-cuál-es) | Funcional | Alta | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-formato-del-hallazgo.md#ca-02--lo-dudoso-sale-como-aviso-y-no-detiene) | [CP-003](#cp-003--el-hallazgo-del-archivo-ilegible-dice-cuál-es) | Funcional | Alta | Sí | ☐ |
| HU-003 | No regresión | [CP-004](#cp-004--los-357-casos-siguen-pasando) | Regresión | Crítica | Sí | ☐ |

**Cobertura:** los dos transversales, los dos CA que toca y la no regresión = 100%.

---

## 6. Casos de prueba

### CP-001 — La lectura tolera los cuatro casos

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / Transversales de errores y límites |
| **Tipo** | Errores · **Prioridad** Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Cinco archivos: uno que no existe, uno que no se puede abrir, uno mal codificado, uno binario y uno normal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer un archivo que no existe | Devuelve vacío, sin excepción |
| 2 | Leer uno que no se puede abrir | Devuelve vacío, sin excepción |
| 3 | Leer uno que no es UTF-8 | Devuelve texto, con los caracteres reemplazados |
| 4 | Leer uno binario | Devuelve algo, sin excepción |
| 5 | Leer uno normal | **Devuelve exactamente lo que tiene** |

**Resultado esperado final:** los cuatro bordes están definidos y el caso feliz no cambió.

> **El paso 5 es el que da valor a los cuatro anteriores.** Sin él, el caso pasaría con una lectura que devuelve vacío siempre.

---

### CP-002 — La corrida sigue y reporta lo demás

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / Transversal · Errores |
| **Tipo** | Errores · **Prioridad** Crítica |
| **Precondiciones** | Árbol temporal con su carpeta de reglas |
| **Datos de entrada** | Un documento mal codificado **y** otro bueno con un enlace roto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la comprobación del estándar sobre el árbol | Termina, sin traza de Python |
| 2 | Mirar el código de salida | No es una caída: es el que corresponda a los hallazgos |
| 3 | Buscar en la salida el **enlace roto del archivo bueno** | Aparece |
| 4 | Buscar el archivo mal codificado | Aparece, con su ruta |

**Resultado esperado final:** un archivo roto cuesta ese archivo, no la corrida.

> **El paso 3 es el caso.** Separa «no revienta» de «sirve»: si el defecto del archivo bueno no aparece, el roto se llevó la corrida aunque nadie viera una traza.

---

### CP-003 — El hallazgo del archivo ilegible dice cuál es

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / CA-01 y CA-02 |
| **Tipo** | Funcional · **Prioridad** Alta |
| **Precondiciones** | El árbol del CP-002 |
| **Datos de entrada** | La salida de esa corrida |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mirar el hallazgo del archivo ilegible | Trae su ruta |
| 2 | Comprobar que dice **por qué** no se pudo leer | Lo dice, en palabras |
| 3 | Comprobar que **no** trae un volcado técnico | No lo trae |
| 4 | Mirar la severidad | **Aviso**, no falla |
| 5 | Comprobar que el archivo leído con reemplazos lo dice | Lo dice: quien lea sabe que ese archivo no se revisó entero |

**Resultado esperado final:** el hallazgo alcanza para arreglar sin abrir el programa —el CA-01— y no detiene —el CA-02—.

---

### CP-004 — Los 357 casos siguen pasando

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / No regresión |
| **Tipo** | Regresión · **Prioridad** Crítica |
| **Precondiciones** | Este repositorio |
| **Datos de entrada** | La suite entera |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la suite de validadores | Verde |
| 2 | Comprobar que el validador de pendientes volvió a la lectura común y sus 14 casos pasan | Pasan |
| 3 | Correr la comprobación del estándar sobre este repositorio | Sin fallas nuevas |
| 4 | Comprobar que no queda ningún fallo esperado en la clase del formato del hallazgo | Ninguno |

**Resultado esperado final:** tolerar la lectura no rompió a ninguno de los que la usan.

> **El paso 2 cierra un préstamo.** El validador de pendientes nació con su propia lectura porque la común no servía; si vuelve y sus casos pasan, el arreglo sirve de verdad.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la corrida siga muriendo con un archivo roto | El arreglo no era el que faltaba: se diagnostica y se escribe |
| **Alta** | Que el archivo ilegible se salte en silencio (riesgo `R-01`) | Tolerar no es callar: se corrige antes de cerrar |
| **Media** | Que un enlace roto pase por bueno en un archivo leído con reemplazos (riesgo `R-02`) | Se anota en el aviso que ese archivo no se revisó entero |
| **Baja** | Que otra sesión esté tocando `validadores/` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los dos transversales, los dos CA que toca y la no regresión |
| Casos ejecutados | 4 de 4 |
| Corridas que mueren por un archivo roto | **0** |
| Hallazgos que se pierden por un archivo roto | **0** |
| Archivos del repositorio rotos para probar | **0** |
| Fallos esperados que queden en la clase, al cerrar | **0** |
| Pruebas de la suite que dejan de pasar | **0** de 357 |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
