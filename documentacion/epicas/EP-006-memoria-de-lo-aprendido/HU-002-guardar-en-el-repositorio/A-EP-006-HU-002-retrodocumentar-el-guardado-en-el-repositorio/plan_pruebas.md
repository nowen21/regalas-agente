# Plan de Pruebas — Fase A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**La memoria no se mueve en esta fase.** El límite de la base binaria se **mide y se propone**: decidir por cuenta propia dónde vive lo aprendido es peor que el límite mismo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Historial | Que un recuerdo nuevo se vea como texto en el historial | Este repositorio | No |
| Medición | Qué se puede y qué no se puede leer del historial de la base de señales | Copia de la base | No |
| Índice | Que la carpeta y el índice coincidan en los dos sentidos | Este repositorio | Sí |
| Uso | Que por el índice se llegue al recuerdo buscado | Este repositorio | No |

**Por qué el índice se prueba en los dos sentidos.** Una línea sin archivo es un índice que miente, y eso ya pasó con otros índices del repositorio.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Trazabilidad | ☑ | Los dos CA |
| Documento | ☑ | El índice completo |
| Medición | ☑ | El límite de la base binaria |
| Usabilidad | ☑ | Llegar al recuerdo sin abrir los otros |

### 3.3 Técnicas de diseño de casos

- **El cruce en los dos sentidos** — archivo sin línea y línea sin archivo.
- **La propuesta se escribe como propuesta** — el riesgo `R-02`: exportar las señales a texto **no se decide acá**. Se escribe qué deja cada salida y se espera.
- **Se mide sobre una copia** — el riesgo `R-03`: la base puede cambiar durante la medición si la sesión guarda una señal.
- **El índice se usa, no solo se cuenta** — el CA-02 se cierra **buscando** un recuerdo por el índice y llegando a él sin abrir los otros. Un índice completo pero inútil cumple el conteo y no el criterio.
- **La forma de los recuerdos no se cambia** — unificarla con la de las señales es justo lo que [HU-005](../../HU-005-separar-aprendizaje-de-preferencia/HU-005-separar-aprendizaje-de-preferencia.md) dice que no se debe hacer.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera, y la medición sobre una copia de la base.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-guardar-en-el-repositorio.md#ca-01--lo-guardado-vive-en-el-repositorio-y-se-ve-en-el-historial) | [CP-001](#cp-001--el-recuerdo-nuevo-se-ve-como-texto-en-el-historial), [CP-002](#cp-002--qué-se-puede-leer-del-historial-de-la-base-de-señales) | Trazabilidad | Crítica | Parcial | ☐ |
| HU-002 | [CA-02](../HU-002-guardar-en-el-repositorio.md#ca-02--hay-un-índice-que-dice-de-qué-trata-cada-cosa) | [CP-003](#cp-003--la-carpeta-y-el-índice-coinciden-en-los-dos-sentidos), [CP-004](#cp-004--por-el-índice-se-llega-al-recuerdo-sin-abrir-los-otros) | Documento | Alta | Parcial | ☐ |
| HU-002 | RNF — que lo aprendido se pueda revisar | [CP-002](#cp-002--qué-se-puede-leer-del-historial-de-la-base-de-señales) | Medición | Crítica | No | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El recuerdo nuevo se ve como texto en el historial

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un recuerdo nuevo escrito en la carpeta de recuerdos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el recuerdo | Queda como archivo de texto |
| 2 | Mirar el historial | Se ve qué se agregó, línea por línea |
| 3 | Cambiar una línea del recuerdo | El historial muestra exactamente qué cambió |
| 4 | Comprobar que se puede revisar sin herramientas extra | Se puede |

**Resultado esperado final:** los recuerdos cumplen el CA sin discusión.

---

### CP-002 — Qué se puede leer del historial de la base de señales

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 y RNF |
| **Tipo** | Medición |
| **Prioridad** | Crítica |
| **Precondiciones** | Copia de la base, para que no cambie durante la medición |
| **Datos de entrada** | El historial de [`memoria/senales.db`](../../../../../memoria/esquema.sql) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar una señal en la copia | La base cambia |
| 2 | Mirar el historial de ese cambio | Se anota qué se ve: si dice cuál señal se agregó o solo que el archivo cambió |
| 3 | Intentar responder «qué se aprendió ese día» usando solo el historial | Se anota si se puede o no |
| 4 | Escribir el límite con lo medido, no con lo supuesto | Queda escrito |
| 5 | Proponer las salidas —exportar a texto junto a la base, o declararlo como límite— **sin decidir** | Queda como propuesta, con lo que deja cada una |

**Resultado esperado final:** el CA-01 queda con su mitad cumplida y su mitad medida, y la decisión en manos del usuario.

> **Este caso no arregla nada a propósito.** Cambiar dónde vive la memoria es una decisión de fondo.

---

### CP-003 — La carpeta y el índice coinciden en los dos sentidos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | La carpeta de recuerdos y su índice |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar los archivos de recuerdo | Sale un número, con su fecha |
| 2 | Comprobar que cada uno tiene su línea en el índice | Todos |
| 3 | Comprobar que cada línea del índice tiene su archivo | Todas |
| 4 | Listar los que fallen en cualquiera de los dos sentidos | Se anotan |
| 5 | Corregir el índice, que es un archivo del repositorio | Se corrige: no rompe nada |

**Resultado esperado final:** el índice no miente ni por exceso ni por defecto.

---

### CP-004 — Por el índice se llega al recuerdo sin abrir los otros

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Usabilidad |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-003 corrido |
| **Datos de entrada** | Tres temas que están cubiertos por algún recuerdo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Por cada tema, buscar en el índice cuál recuerdo lo trata | Se llega a uno |
| 2 | Contar cuántos archivos hubo que abrir para encontrarlo | Uno |
| 3 | Comprobar que el índice dice **de qué trata**, no qué exige | Lo dice: el índice no reemplaza leer el archivo |
| 4 | Anotar el tema que no se pueda ubicar por el índice | Queda como hueco del índice |

**Resultado esperado final:** el índice sirve para encontrar, que es para lo que está.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la propuesta de exportar las señales se ejecute sin aprobación (riesgo `R-02`) | Inmediato. Se movería la memoria sin decisión del usuario |
| **Alta** | Que el índice tenga líneas sin archivo (riesgo `R-01`) | Se anota y se corrige el índice: es un archivo del repositorio y no rompe nada |
| **Media** | Que del historial de la base no se pueda leer nada | Es el hallazgo esperado: queda medido y propuesto |
| **Media** | Que la base cambie durante la medición (riesgo `R-03`) | Se mide sobre una copia |
| **Baja** | Temas sin recuerdo ubicable por el índice | Se anotan como huecos |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Recuerdos sin línea en el índice | **0** |
| Líneas del índice sin archivo | **0** |
| Señales exportadas o movidas en esta fase | **0** |
| Archivos que hubo que abrir para ubicar un tema | 1 |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
