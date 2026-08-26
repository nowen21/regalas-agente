# Plan de Pruebas — «Fase A-EP-007-HU-007: la revisión ve la cadena»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-007-la-revision-ve-la-cadena` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, en la orden de resolver los ocho pendientes `P1` |
| **Estado** | Aprobado |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Correr la revisión entera sobre proyectos de mentira y leer el punto nuevo | Carpeta temporal | Sí |

**Por qué la revisión entera y no la función sola.** Lo que falló en `shopnest-mesa` no fue una comprobación: fue el **resumen** diciendo «13 de 13, instalación completa». Eso solo se ve corriendo el conjunto.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los `CA-01` y `CA-02` |
| Límites | ☑ | Proyecto recién instalado, sin código y sin planteamiento |
| No regresión | ☑ | Que los trece puntos anteriores sigan comprobándose igual |

### 3.3 Técnicas de diseño de casos

- **El caso real** — un proyecto con código y sin ningún planteamiento, que es lo que pasó.
- **Prueba de la prueba** — se quita el punto de la lista y el caso tiene que ponerse rojo.
- **Espejo** — se comprueba también contra **este mismo repositorio**, y se escribe el resultado salga lo que salga.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/tests/` entera.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | [CP-001](#cp-001--la-cadena-vacía-se-nombra-y-se-dice-cómo-se-arregla) | Funcional | Alta | Sí | ☐ |
| HU-007 | CA-02 | [CP-002](#cp-002--el-punto-se-apaga-al-escribir-el-planteamiento) | Funcional | Alta | Sí | ☐ |
| HU-007 | CA-01 · límites | [CP-003](#cp-003--la-épica-solo-se-exige-si-hay-código) | Límites | Media | Sí | ☐ |
| HU-007 | CA-01 · prueba de la prueba | [CP-004](#cp-004--el-caso-se-pone-rojo-si-se-quita-el-punto) | Verificación | Alta | No — a mano, una vez | ☐ |

**Cobertura:** 2 de 2 CA = 100%.

---

## 6. Casos de prueba

### CP-001 — La cadena vacía se nombra, y se dice cómo se arregla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Proyecto de mentira con `prompts/` vacía y código en `proyectos/` |
| **Datos de entrada** | La ruta del proyecto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar el proyecto | El punto de la cadena sale como faltante |
| 2 | Leer su detalle | Dice que no hay ningún planteamiento en `prompts/` |
| 3 | Leer cómo se arregla | Dice que lo escribe el agente, no el instalador |
| 4 | Leer el resumen de la revisión | **No** dice «instalación completa» |

**Resultado esperado final:** lo que antes pasaba en verde, ahora se nombra.

> **El paso 4 es el que importa.** Un punto que falta y un resumen que sigue diciendo «completo» es peor que no comprobar nada.

---

### CP-002 — El punto se apaga al escribir el planteamiento

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Las del CP-001 |
| **Datos de entrada** | Un archivo de planteamiento en `prompts/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el planteamiento y una épica | El proyecto ya recorre el principio de la cadena |
| 2 | Revisar otra vez | El punto de la cadena ya no aparece entre los faltantes |

**Resultado esperado final:** el silencio significa que la cadena arrancó.

---

### CP-003 — La épica solo se exige si hay código

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 · límites |
| **Tipo** | Límites |
| **Prioridad** | Media |
| **Precondiciones** | Proyecto recién instalado: `proyectos/` vacía |
| **Datos de entrada** | Un planteamiento, sin ninguna épica |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar con planteamiento y sin código | El punto no aparece: nadie construyó nada todavía |
| 2 | Poner código en `proyectos/` y revisar | Ahora sí aparece, pidiendo la épica |

**Resultado esperado final:** se pide la cadena cuando hay algo construido, no el primer día.

---

### CP-004 — El caso se pone rojo si se quita el punto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 · verificación del propio caso |
| **Tipo** | Verificación manual, una sola vez |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 pasó |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quitar el punto de la lista de componentes | Queda como estaba antes de la fase |
| 2 | Correr la suite de la fase | El CP-001 se pone rojo |
| 3 | Devolverlo y correr todo | Verde otra vez |

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la revisión deje de comprobar alguno de los trece que ya miraba | Inmediato |
| **Alta** | Que el resumen siga diciendo «completo» con el punto faltando | Inmediato — es el defecto que se vino a cerrar |
| **Media** | Que el punto salga en un proyecto recién instalado, sin código | Antes de cerrar |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de CA | 100% — los 2 con caso |
| Casos ejecutados | 4 de 4 |
| Pruebas del repositorio en verde | Las 29 de hoy, más las nuevas |
| Puntos de la revisión | 13 → **14** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
