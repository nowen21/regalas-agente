# Plan de Pruebas — Fase A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-017 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El programa cuenta y no escribe.** No edita el tablero del pendiente [48](../../../../../pendientes/48-inventario-hu.md): un programa que edita el backlog pisa lo que otra sesión esté escribiendo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que el total sea el número de carpetas de HU del árbol | Este repositorio | Sí |
| Funcional | Que la línea diga total, completas e incompletas | Carpetas temporales | Sí |
| Límites | Que la HU con dos fases y los dos bordes se cuenten bien | Carpetas temporales | Sí |
| Comparación | Cuál era la diferencia entre la cuenta del programa y la del tablero | Este repositorio | Parcial |

**Qué cuenta como completa.** La HU cuyas fases tienen sus cinco documentos — el mismo criterio del tablero. Cambiarlo haría que los dos números no se puedan comparar, que es justamente para lo que sirven.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los cuatro CA |
| Límites | ☑ | La HU con dos fases, la épica sin HU, la carpeta HU sin su archivo |
| No regresión | ☑ | Que contar no cambie el código de salida |
| Comparación | ☑ | La cuenta del programa contra la del tablero |

### 3.3 Técnicas de diseño de casos

- **Se cuenta donde ya se recorre** — el programa que ya camina el árbol es el que cuenta. Recorrerlo dos veces da dos verdades el día que uno de los dos se quede viejo.
- **Contar no falla** — el riesgo `R-02`: la línea informa y no agrega hallazgos. Un total alto no puede dejar el proyecto en rojo, o el conteo se vuelve un castigo y se saca.
- **Los bordes que ya se dan** — la épica sin HU y la carpeta HU sin su archivo no son hipótesis: [`flujo.py`](../../../../../validadores/flujo.py) ya tiene avisos para el padre que falta.
- **La HU con dos fases, con un documento quitado** — es el caso real de [EP-005 · HU-008](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md). Se prueba quitando un documento de **una** de las dos y viendo que la HU deja de contar completa.
- **La corrida manda sobre el tablero** — el riesgo `R-01`: cuando los dos números no coincidan, el del programa es el bueno, y el resultado anota cuál era la diferencia el día que se midió.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y `validar.py fases` sobre este repositorio y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-017 | [CA-01](../HU-017-inventario-de-hu-sin-fase.md#ca-01--la-corrida-dice-el-total-las-completas-y-las-incompletas) | [CP-001](#cp-001--la-línea-dice-total-completas-e-incompletas) | Funcional | Alta | Sí | ☐ |
| HU-017 | [CA-02](../HU-017-inventario-de-hu-sin-fase.md#ca-02--el-total-coincide-con-las-carpetas-que-hay) | [CP-002](#cp-002--el-total-es-el-número-de-carpetas-de-hu-del-árbol) | Funcional | Crítica | Sí | ☐ |
| HU-017 | [CA-03](../HU-017-inventario-de-hu-sin-fase.md#ca-03--una-hu-con-dos-fases-cuenta-como-completa-solo-si-las-dos-lo-están) | [CP-003](#cp-003--la-hu-con-dos-fases-cuenta-completa-solo-si-las-dos-lo-están) | Límites | Alta | Sí | ☐ |
| HU-017 | [CA-04](../HU-017-inventario-de-hu-sin-fase.md#ca-04--caso-borde-la-épica-sin-hu-y-la-carpeta-hu-sin-su-archivo) | [CP-004](#cp-004--la-épica-sin-hu-y-la-carpeta-hu-sin-su-archivo) | Límites | Alta | Sí | ☐ |
| HU-017 | RNF — que la cuenta no vuelva a perderse | [CP-005](#cp-005--contar-no-cambia-el-código-de-salida-y-la-diferencia-queda-anotada) | No regresión | Media | Sí | ☐ |

**Cobertura:** 4 de 4 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La línea dice total, completas e incompletas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-017 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un árbol con dos HU: una con su fase completa y otra sin ella |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el árbol de dos HU | Sale la línea de resumen |
| 2 | Leer los tres números | Total 2, completas 1, incompletas 1 |
| 3 | Comprobar que completas más incompletas es el total | Suma exacta |
| 4 | Completar la segunda y volver a correr | Total 2, completas 2, incompletas 0 |

**Resultado esperado final:** el resumen dice cuántas HU, no cuántos avisos.

---

### CP-002 — El total es el número de carpetas de HU del árbol

| Campo | Valor |
|---|---|
| **HU / CA** | HU-017 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las carpetas de HU del árbol | Sale un número |
| 2 | Correr y leer el total del resumen | Coincide con el paso 1 |
| 3 | Agregar una carpeta de HU en una copia y volver a correr | El total sube en uno, sin tocar nada más |
| 4 | Comparar contra el número que dice el tablero del pendiente [48](../../../../../pendientes/48-inventario-hu.md) | Se anota la diferencia, con la fecha |

**Resultado esperado final:** el total deja de desincronizarse, porque sale de contar y no de recordar.

> **El paso 3 es el que prueba que cuenta.** Un total escrito a mano coincidiría con el paso 2 y fallaría acá.

---

### CP-003 — La HU con dos fases cuenta completa solo si las dos lo están

| Campo | Valor |
|---|---|
| **HU / CA** | HU-017 / CA-03 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Copia del árbol, con la HU que tiene dos fases |
| **Datos de entrada** | [EP-005 · HU-008](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md), que tiene dos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr con las dos fases completas | La HU cuenta como completa |
| 2 | Quitar un documento de **una** de las dos fases | Queda incompleta esa fase |
| 3 | Correr otra vez | La HU **deja** de contar como completa |
| 4 | Devolver el documento y correr | Vuelve a contar completa |

**Resultado esperado final:** una HU no está terminada por la mitad de sus fases.

---

### CP-004 — La épica sin HU y la carpeta HU sin su archivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-017 / CA-04 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Una épica sin ninguna HU, y una carpeta de HU sin su archivo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre la épica sin HU | La corrida no se rompe, y la cuenta no se altera |
| 2 | Correr sobre la carpeta de HU sin su archivo | Se cuenta como **incompleta**, no se ignora |
| 3 | Comprobar que la suma sigue cuadrando en los dos casos | Cuadra |
| 4 | Comprobar que ninguno de los dos produce una excepción | Ninguno |

**Resultado esperado final:** los bordes que ya se dan en el árbol no rompen la cuenta ni la falsean.

> **El paso 2 importa.** Ignorar la carpeta sin archivo bajaría el total y haría parecer que hay menos trabajo del que hay.

---

### CP-005 — Contar no cambia el código de salida, y la diferencia queda anotada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-017 / RNF |
| **Tipo** | No regresión |
| **Prioridad** | Media |
| **Precondiciones** | El número de pruebas de la suite anotado antes |
| **Datos de entrada** | Este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el código de salida de `validar.py fases` antes del cambio | Queda la línea base |
| 2 | Aplicar el cambio y correr | El código de salida es el mismo, aunque el total de incompletas sea alto |
| 3 | Correr la suite completa | Ninguna prueba que pasaba, falla |
| 4 | Anotar la diferencia entre la cuenta del programa y la del tablero | Queda escrita, con la fecha |

**Resultado esperado final:** contar informa, no castiga, y hay contra qué comparar la próxima vez.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el total no coincida con las carpetas del árbol | Inmediato. El CA-02 queda en «No» y el número no sirve |
| **Alta** | Que contar cambie el código de salida (riesgo `R-02`) | Inmediato — un total alto dejaría el proyecto en rojo y el conteo se sacaría |
| **Media** | Que una HU con dos fases cuente completa con una sola terminada | Antes de cerrar |
| **Media** | Que la cuenta del programa y la del tablero no coincidan (riesgo `R-01`) | La corrida manda; se anota la diferencia con su fecha |
| **Baja** | Que se lea como que la HU resuelve el pendiente 48 (riesgo `R-03`) | El README de la fase lo dice: esto cuenta, no llena |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 4 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Diferencia entre el total y las carpetas del árbol | **0** |
| Cambios en el código de salida por contar | **0** |
| Archivos del tablero editados por el programa | **0** |
| Diferencia contra el tablero | Anotada, con su fecha |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
