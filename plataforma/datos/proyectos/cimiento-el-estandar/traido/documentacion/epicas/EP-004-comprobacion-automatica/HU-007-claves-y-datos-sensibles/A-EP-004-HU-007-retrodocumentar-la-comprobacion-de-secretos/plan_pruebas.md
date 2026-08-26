# Plan de Pruebas — Fase A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Ninguna clave real entra a este repositorio, ni siquiera rotada.** Las cadenas de la prueba se **arman**, se usan en carpeta temporal y se borran. Una clave real versionada es una clave filtrada ([`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Acierto | Que la clave incrustada y el archivo que no debe versionarse se reporten | Carpeta temporal | Sí |
| Falso positivo | Que un ejemplo de documentación y un dato de prueba **no** se reporten | Carpeta temporal | Sí |
| Inventario | Que la lista de lo que hoy se considera ejemplo salga del programa y no de la memoria | Este repositorio | Parcial |

**Por qué el falso positivo pesa igual que los dos aciertos.** Un detector con falsos positivos se apaga, y un detector apagado no detecta nada. El CA-03 es tan crítico como el CA-01.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Seguridad | ☑ | Los tres CA |
| Negativa | ☑ | El CA-03: lo que **no** debe reportarse |
| Límites | ☑ | El ejemplo que se parece más a una clave real |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Cadenas armadas, nunca copiadas** — arriba. Ni siquiera una clave vieja ya rotada.
- **Limpieza comprobada, no supuesta** — el riesgo `R-01`: después de cada caso, la prueba **comprueba** que la carpeta temporal se borró y que nada quedó en el árbol. Que la fase que previene filtraciones filtre algo sería el defecto más caro posible.
- **El ejemplo más difícil** — el caso del CA-03 usa el ejemplo que **más se parece** a una clave real, no uno obviamente inofensivo. Un caso fácil no prueba nada de la discriminación.
- **La lista se levanta del programa** — el riesgo `R-03`: lo que hoy se considera ejemplo se lee de [`secretos.py`](../../../../../validadores/secretos.py), y la prueba falla si el documento y el programa dejan de coincidir.
- **Lo que se escape se anota** — ampliar el detector cambia qué falla en todos los proyectos; se propone, no se hace de paso.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, más `validar.py secretos` y `validar.py versionado` sobre las carpetas temporales y sobre este repositorio.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | [CA-01](../HU-007-claves-y-datos-sensibles.md#ca-01--una-clave-escrita-en-el-código-se-reporta) | [CP-001](#cp-001--la-clave-armada-se-reporta-con-archivo-y-línea) | Seguridad | Crítica | Sí | ☐ |
| HU-007 | [CA-02](../HU-007-claves-y-datos-sensibles.md#ca-02--un-archivo-que-no-debe-guardarse-se-reporta) | [CP-002](#cp-002--el-archivo-de-configuración-con-secretos-se-reporta-al-versionarlo) | Seguridad | Crítica | Sí | ☐ |
| HU-007 | [CA-03](../HU-007-claves-y-datos-sensibles.md#ca-03--un-ejemplo-no-se-confunde-con-una-clave) | [CP-003](#cp-003--el-ejemplo-y-el-dato-de-prueba-no-se-reportan), [CP-004](#cp-004--la-lista-de-lo-que-cuenta-como-ejemplo-sale-del-programa) | Negativa | Crítica | Sí | ☐ |
| HU-007 | RNF — que nadie apague el detector por ruido | [CP-003](#cp-003--el-ejemplo-y-el-dato-de-prueba-no-se-reportan) | Negativa | Alta | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La clave armada se reporta, con archivo y línea

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal fuera del árbol del repositorio |
| **Datos de entrada** | Varias cadenas con forma de credencial, **armadas para la prueba**, de formatos distintos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir las cadenas armadas en archivos de la carpeta temporal | Quedan escritas |
| 2 | Correr `validar.py secretos` sobre la carpeta | Todas se reportan |
| 3 | Comprobar que cada hallazgo trae archivo y línea | Todos |
| 4 | Borrar la carpeta temporal | Se borra |
| 5 | Comprobar que ninguna cadena quedó en el árbol del repositorio | Ninguna |

**Resultado esperado final:** la clave incrustada se detecta, y la prueba no deja rastro.

> **El paso 5 no es formalidad.** Que la fase que previene filtraciones filtre una cadena sería el defecto más caro que puede cometer.

---

### CP-002 — El archivo de configuración con secretos se reporta al versionarlo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal con control de versiones propio |
| **Datos de entrada** | Un archivo de configuración con secretos armados |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner el archivo bajo control de versiones en la carpeta temporal | Queda versionado |
| 2 | Correr `validar.py versionado` | Sale el hallazgo, y nombra el archivo |
| 3 | Sacarlo del control de versiones y volver a correr | No sale hallazgo |
| 4 | Borrar la carpeta temporal y comprobar la limpieza | No queda rastro |

**Resultado esperado final:** lo que no debe guardarse se detecta al guardarlo.

> **El paso 3 es el que da valor al 2.** Sin él, el caso pasaría con un programa que reporta todo archivo de configuración.

---

### CP-003 — El ejemplo y el dato de prueba no se reportan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un ejemplo de documentación y un dato de prueba, elegidos por **parecerse lo más posible** a una clave real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el ejemplo de documentación | Queda escrito |
| 2 | Correr `validar.py secretos` | **No** se reporta |
| 3 | Escribir el dato de prueba, con la forma acordada sin secretos literales | Queda escrito |
| 4 | Correr | **No** se reporta |
| 5 | Correr sobre este repositorio y contar los falsos positivos que aparezcan | Se anotan; ajustar el detector se propone aparte |

**Resultado esperado final:** el detector distingue, y por eso nadie tiene motivo para apagarlo.

> **Los datos se eligen por difíciles a propósito.** Un ejemplo obviamente inofensivo no prueba nada de la discriminación.

---

### CP-004 — La lista de lo que cuenta como ejemplo sale del programa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | [`validadores/secretos.py`](../../../../../validadores/secretos.py) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer del programa qué formatos reconoce y qué considera ejemplo | Queda la lista |
| 2 | Escribirla en el resultado, diciendo que salió del programa | Queda con su origen |
| 3 | Comprobar que documento y programa coinciden | Coinciden |
| 4 | Dejar la comprobación como prueba, para que falle si se separan | Queda automatizada |

**Resultado esperado final:** la lista no envejece en silencio.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una cadena de prueba quede en el árbol del repositorio (riesgo `R-01`) | Inmediato. Se detiene la fase y se limpia |
| **Crítica** | Que una clave incrustada no se reporte | Inmediato. El CA-01 queda en «No» |
| **Alta** | Que aparezcan falsos positivos en el repositorio (riesgo `R-02`) | Se anotan. Ajustar el detector se propone aparte: cambia qué falla en todos los proyectos |
| **Media** | Que la lista de formatos reconocidos y el programa no coincidan (riesgo `R-03`) | La prueba lo detecta y se corrige el documento |
| **Baja** | Formatos de credencial que el detector no reconoce | Se anotan. Ampliarlo se propone |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Claves reales usadas | **0** |
| Cadenas de prueba que quedaron en el repositorio | **0** |
| Falsos positivos en el repositorio | Todos anotados |
| Formatos de credencial probados | Al menos 3, todos detectados |
| Pruebas de la suite | Las de la línea base, más las nuevas, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
