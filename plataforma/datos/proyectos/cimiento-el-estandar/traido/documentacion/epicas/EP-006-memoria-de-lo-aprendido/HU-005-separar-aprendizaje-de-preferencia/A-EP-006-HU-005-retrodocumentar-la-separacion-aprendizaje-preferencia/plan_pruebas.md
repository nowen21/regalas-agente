# Plan de Pruebas — Fase A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Nada se mueve de sitio.** Mover un recuerdo cambia lo que rige la sesión: lo que esté en el lugar equivocado se anota y se propone.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Clasificación | Que con el criterio escrito se decida cuál va dónde | Este repositorio | No |
| Forma | Que todo recuerdo traiga sus tres partes | Lectura de la carpeta de recuerdos | Sí |
| Negativa | Que un recuerdo sin el porqué se detecte | Carpeta temporal | Sí |

**Qué se mira de las tres partes.** Que **estén**, no si el porqué convence. Lo primero es sí o no; lo segundo es criterio.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Documento | ☑ | Los dos CA |
| Negativa | ☑ | El recuerdo incompleto tiene que salir detectado |
| Límites | ☑ | El caso de borde: lo que podría ser regla del estándar y no preferencia |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **El caso de borde es la prueba del criterio** — el riesgo `R-03`: si con el criterio escrito **no se puede** decidir el caso de borde —una preferencia que aplicaría a cualquier proyecto y por tanto sería regla—, al criterio le falta texto.
- **Cinco cosas ya guardadas, no inventadas** — se clasifican cosas que están de verdad en los dos sitios. Las inventadas caen siempre del lado claro.
- **Lo que esté mal ubicado se anota** — arriba. Si además resulta que debería ser regla de `base/`, se propone: subir un recuerdo a regla lo decide el usuario, como ya pasó con dos en [EP-001 · HU-004](../../../EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/HU-004-conducta-de-la-ia.md).
- **El criterio va en el índice de la memoria, no en `base/`** — el criterio de qué es preferencia del usuario es de este repositorio. Si aplicara a cualquier proyecto sería regla, y ese es justo el caso de borde.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y la lectura de la carpeta de recuerdos.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-separar-aprendizaje-de-preferencia.md#ca-01--las-dos-cosas-se-guardan-por-separado) | [CP-001](#cp-001--cinco-cosas-guardadas-clasificadas-con-el-criterio), [CP-002](#cp-002--el-caso-de-borde-se-resuelve-con-el-criterio) | Documento | Alta | No | ☐ |
| HU-005 | [CA-02](../HU-005-separar-aprendizaje-de-preferencia.md#ca-02--la-preferencia-dice-por-qué-se-pidió) | [CP-003](#cp-003--todo-recuerdo-trae-sus-tres-partes), [CP-004](#cp-004--el-recuerdo-sin-el-porqué-se-detecta) | Negativa | Alta | Sí | ☐ |
| HU-005 | RNF — que no se confunda lo aprendido con lo pedido | [CP-002](#cp-002--el-caso-de-borde-se-resuelve-con-el-criterio) | Límites | Crítica | No | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Cinco cosas guardadas, clasificadas con el criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | El criterio escrito (T-01) |
| **Datos de entrada** | Cinco cosas ya guardadas: algunas señales y algunos recuerdos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar el criterio escrito | Queda a la vista |
| 2 | Clasificar cada una de las cinco **sin mirar dónde está** | Cada una con su veredicto |
| 3 | Comparar contra dónde está de verdad | Coinciden las cinco |
| 4 | Anotar la que no coincida, sin moverla | Queda como hallazgo |
| 5 | Si además debería ser regla de `base/`, proponerlo | Queda propuesto, no hecho |

**Resultado esperado final:** el criterio reproduce la separación que ya existe, o dice dónde no.

> **El paso 2 pide clasificar a ciegas.** Mirar dónde está primero convierte la prueba en una confirmación.

---

### CP-002 — El caso de borde se resuelve con el criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 y RNF |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El criterio escrito |
| **Datos de entrada** | Una preferencia que **aplicaría a cualquier proyecto**, no solo a este |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la preferencia de borde | Queda a la vista |
| 2 | Aplicarle el criterio | Da una respuesta concreta: recuerdo, señal o regla del estándar |
| 3 | Comprobar que la respuesta es una sola, no dos posibles | Una sola |
| 4 | Si el criterio no permite decidirlo, anotarlo | **Es hallazgo del criterio**: le falta texto |

**Resultado esperado final:** el criterio decide el caso difícil, que es el único que hace falta que decida.

---

### CP-003 — Todo recuerdo trae sus tres partes

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | El número de pruebas de la suite anotado antes |
| **Datos de entrada** | Todos los archivos de la carpeta de recuerdos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar los recuerdos | Sale un número, con su fecha |
| 2 | Por cada uno, comprobar que dice **qué se pide** | Todos |
| 3 | Comprobar que dice **por qué** | Todos |
| 4 | Comprobar que dice **cómo se aplica** | Todos |
| 5 | Listar los incompletos | Se anotan y se completan: es un cambio de texto sin riesgo |

**Resultado esperado final:** un recuerdo sirve para aplicarlo, no solo para recordar que existe.

---

### CP-004 — El recuerdo sin el porqué se detecta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un recuerdo sin el porqué, y otro completo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el recuerdo sin el porqué | Se detecta, y dice qué parte falta |
| 2 | Correr sobre el completo | No se detecta |
| 3 | Quitarle otra de las tres partes al completo | Se detecta, y nombra esa |
| 4 | Comprobar que no se juzga si el porqué **convence** | No se juzga: eso es criterio |

**Resultado esperado final:** la forma se comprueba y el contenido queda para quien lo lea.

> **El paso 4 marca el límite.** Un programa que juzgara si un porqué es bueno produciría rechazos que nadie puede corregir.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que se mueva un recuerdo de sitio sin aprobación | Inmediato: mover un recuerdo cambia lo que rige la sesión |
| **Alta** | Que el criterio no resuelva el caso de borde (riesgo `R-03`) | Falta texto: se escribe antes de cerrar |
| **Media** | Que aparezcan recuerdos que deberían ser reglas (riesgo `R-01`) | Se anotan y se proponen. Subir un recuerdo a regla lo decide el usuario |
| **Media** | Que la prueba falle con recuerdos viejos (riesgo `R-02`) | Se anotan y se completan: es un cambio de texto sin riesgo |
| **Baja** | Diferencias sobre si un porqué convence | Fuera de alcance: se mira que esté, no que persuada |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Recuerdos o señales movidos de sitio | **0** |
| Recuerdos sin sus tres partes | Todos listados |
| Casos de borde que el criterio no resuelve | **0** |
| Recuerdos que deberían ser reglas | Todos anotados y propuestos |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
