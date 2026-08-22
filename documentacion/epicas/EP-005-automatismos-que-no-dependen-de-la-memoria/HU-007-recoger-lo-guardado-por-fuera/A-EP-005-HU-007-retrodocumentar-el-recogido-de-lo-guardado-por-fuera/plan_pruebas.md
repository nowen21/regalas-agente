# Plan de Pruebas — Fase A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Condición de arranque, no negociable.** Las pruebas usan un **almacén local de mentira** en carpeta temporal. El almacén real tiene los recuerdos del usuario, y una prueba no lo toca (riesgo `R-01`).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Que el recuerdo del almacén local aparezca en el repositorio | Carpeta temporal | Sí |
| Vaciado | Que el almacén local quede sin el texto **ni un puntero** | Carpeta temporal | Sí |
| Colisión | Que un recuerdo que ya existe en el repositorio no se sobrescriba | Carpeta temporal | Sí |

**Por qué el CA-02 se prueba con contenido distinto.** Pisar es **sobrescribir contenido**. Con el mismo texto en los dos lados, un programa que pisa y uno que no dan el mismo resultado y el caso no prueba nada.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Colisión | ☑ | Mismo nombre, contenido distinto |
| Límites | ☑ | Almacén vacío, y almacén con varios recuerdos a la vez |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Almacén de mentira, siempre** — arriba.
- **El vaciado incluye el puntero** — `01·C19` no pide solo que el texto se mueva: pide que el almacén quede **vacío**, ni el texto ni un puntero. Dos versiones del mismo recuerdo terminan diciendo cosas distintas, y la que manda es la que nadie puede leer.
- **La colisión se observa antes de decidir** — el riesgo `R-02`: el caso anota **qué hace hoy** el programa ante dos recuerdos con el mismo nombre. Si está mal resuelto, se propone; perder un recuerdo es grave y merece su propia fase.
- **Nada se cambia en el recogido** — cambiar el programa sin saber qué hace puede perder un recuerdo.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el enganche contra almacenes de mentira en carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | [CA-01](../HU-007-recoger-lo-guardado-por-fuera.md#ca-01--lo-guardado-por-fuera-se-recoge-al-abrir-sesión) | [CP-001](#cp-001--el-recuerdo-del-almacén-local-aparece-en-el-repositorio), [CP-002](#cp-002--el-almacén-local-queda-vacío-ni-el-texto-ni-un-puntero) | Funcional | Crítica | Sí | ☐ |
| HU-007 | [CA-02](../HU-007-recoger-lo-guardado-por-fuera.md#ca-02--nada-se-pisa) | [CP-003](#cp-003--el-recuerdo-que-ya-existe-en-el-repositorio-no-se-sobrescribe), [CP-004](#cp-004--dos-recuerdos-con-el-mismo-nombre-y-contenido-distinto) | Colisión | Crítica | Sí | ☐ |
| HU-007 | RNF — que recoger no sea destruir | [CP-003](#cp-003--el-recuerdo-que-ya-existe-en-el-repositorio-no-se-sobrescribe) | Colisión | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El recuerdo del almacén local aparece en el repositorio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Almacén local **de mentira** en carpeta temporal |
| **Datos de entrada** | Un recuerdo puesto en ese almacén |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner el recuerdo en el almacén de mentira | Queda ahí |
| 2 | Abrir la sesión | El recuerdo aparece en la carpeta del repositorio |
| 3 | Comprobar que el contenido llegó completo | Palabra por palabra |
| 4 | Comprobar que tiene su línea en el índice | La tiene |
| 5 | Probar con varios recuerdos a la vez | Llegan todos |

**Resultado esperado final:** lo que se guardó por fuera termina donde se puede revisar y versionar.

---

### CP-002 — El almacén local queda vacío: ni el texto ni un puntero

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | El almacén de mentira después del recogido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mirar el almacén después de recoger | No tiene el texto del recuerdo |
| 2 | Buscar un puntero, un enlace o una referencia al archivo del repositorio | No hay ninguno |
| 3 | Abrir la sesión otra vez | No vuelve a recoger nada: no quedó nada que recoger |
| 4 | Comprobar que el recuerdo del repositorio sigue intacto | Intacto |

**Resultado esperado final:** hay una sola versión del recuerdo, y es la que se puede leer y revisar ([`01·C19`](../../../../../base/01-conducta.md)).

> **El paso 2 no es exceso.** Un puntero dejado atrás es la segunda versión del recuerdo, y es la que nadie va a mantener.

---

### CP-003 — El recuerdo que ya existe en el repositorio no se sobrescribe

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 y RNF |
| **Tipo** | Colisión |
| **Prioridad** | Crítica |
| **Precondiciones** | Almacén de mentira, y un recuerdo ya escrito en el repositorio de prueba |
| **Datos de entrada** | El mismo nombre en los dos lados, con **contenido distinto** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar el contenido del recuerdo que está en el repositorio | Queda la línea base |
| 2 | Poner en el almacén uno con el mismo nombre y otro contenido | Queda puesto |
| 3 | Correr el recogido | Se anota qué hace |
| 4 | Comparar el recuerdo del repositorio contra la línea base | **No se sobrescribió** |
| 5 | Comprobar que el del almacén no se perdió | No se perdió: quedó en algún lado y se sabe dónde |

**Resultado esperado final:** recoger no destruye lo que el usuario ya escribió.

> **El paso 5 es tan importante como el 4.** Ni pisar el del repositorio ni tirar el del almacén: los dos son recuerdos del usuario.

---

### CP-004 — Dos recuerdos con el mismo nombre y contenido distinto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Tipo** | Colisión |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-003 corrido |
| **Datos de entrada** | La situación del CP-003, mirada en detalle |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar exactamente qué hizo el programa con los dos | Queda escrito: renombró, avisó, dejó uno, o algo más |
| 2 | Comparar contra lo que el CA-02 pide | Se ve si coincide |
| 3 | Si no coincide, anotarlo como hallazgo | Queda propuesto, no corregido |
| 4 | Comprobar que ningún recuerdo desapareció en ninguna variante | Ninguno |
| 5 | Probar también con el almacén vacío | Ni error ni ruido |

**Resultado esperado final:** se sabe qué hace hoy el recogido ante un choque, y si está mal, queda propuesto con su propia fase.

> **No se cambia el recogido acá.** Perder un recuerdo es grave, y arreglar esto merece su propio plan (riesgo `R-02`).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la prueba toque el almacén real de la máquina (riesgo `R-01`) | Inmediato. Se detiene y se restaura: es un recuerdo del usuario |
| **Crítica** | Que el recogido sobrescriba un recuerdo del repositorio | Inmediato. El CA-02 queda en «No» |
| **Crítica** | Que un recuerdo desaparezca en el choque | Inmediato — es la pérdida que la HU quiere evitar |
| **Alta** | Que el almacén quede con un puntero | El CA-01 queda a medias: son dos versiones del mismo recuerdo |
| **Media** | Que el choque esté mal resuelto hoy (riesgo `R-02`) | Se anota y se propone con su propia fase |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Recuerdos del almacén real tocados | **0** |
| Recuerdos perdidos en las pruebas | **0** |
| Punteros dejados en el almacén local | **0** |
| Comportamiento ante el choque de nombres | Medido y escrito |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
