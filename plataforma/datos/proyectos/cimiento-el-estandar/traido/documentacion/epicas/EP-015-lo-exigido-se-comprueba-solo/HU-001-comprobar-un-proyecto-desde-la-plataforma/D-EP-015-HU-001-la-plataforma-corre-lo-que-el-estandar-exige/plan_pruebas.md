# Plan de Pruebas — Fase `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-comprobar-un-proyecto-desde-la-plataforma.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el veredicto sale **con archivo y línea**, que un proyecto sin el estándar **no recibe veredicto**, y que cero comprobaciones no es verde.

### 1.2 Alcance

**Entra:** el puente hacia el punto de entrada del estándar, la lectura de su resumen y de sus fallas, y la distinción entre no cumplir y no poderse comprobar.

**No entra:** si las comprobaciones del estándar reconocen lo que deben. Eso se prueba allá, con sus 733 pruebas.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las seis decisiones técnicas |
| [documentacion/comprobaciones/spec.md](../../../../comprobaciones/spec.md) | Las `RN-1` a `RN-6` y la §5.1 |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La detección previa | Proyecto que no existe · carpeta que ya no está · sin el estándar |
| El resumen | Que se lean los dos números |
| Las fallas | Que salgan con archivo y línea, y que un aviso no cuente como falla |
| El veredicto | Cero, con fallas, sin fallas, y no se pudo |
| La carpeta | **Que no cambie** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Un proyecto sin el estándar no puede recibir veredicto, y cero no puede ser verde |
| De lectura | Lo que el estándar imprime, leído tal como lo imprime |
| **Sobre lo real** | Este repositorio, con el tiempo medido |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | **«Sin comprobar» y «no cumple» son cosas distintas**, y confundirlas hace que nadie mire el rojo |
| Crítica | CP-005 | Cero comprobaciones en verde es un silencio que se lee como éxito |
| Alta | CP-001, CP-002 | El veredicto y su ubicación |
| Media | CP-004 | Que no modifique nada |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/comprobaciones/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La especificación del módulo, con su §5.1.
- La vuelta de la columna, resuelta.

### 4.2 Criterios de salida

- Los cinco casos ejecutados.
- **Este repositorio comprobado, con el tiempo escrito**, sea el que sea.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **un proyecto sin el estándar recibe veredicto**. Ahí la funcionalidad diría que algo cumple sin haberlo mirado, que es peor que no tenerla.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — cumple, y dice cuántas | CP-001 | De sistema |
| CA-02 — con archivo y línea | CP-002 | De sistema |
| CA-03 — sin el estándar, lo dice | CP-003 | Que **no** pase |
| CA-04 — no modifica nada | CP-004 | Que **no** pase |
| CA-05 — cero es rojo | CP-005 | De partición |

---

## 6. Casos de prueba

### CP-001 — Un proyecto que cumple pasa

- El veredicto dice que cumple **y cuántas comprobaciones corrieron**.
- Sin el número no se sabe si miró algo.

### CP-002 — Uno que no cumple es rechazado, con archivo y línea

- Cada falla trae la ruta con su número de línea, tal como el estándar la reporta.
- **Un aviso no cuenta como falla:** son cosas distintas y el estándar las marca distinto.
- Varias fallas salen todas.

### CP-003 — Sin el estándar, no hay veredicto

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Una carpeta sin `base/` | Se dice que no hay contra qué comprobar |
| Una carpeta que ya no está | Se dice |
| Un proyecto que no está registrado | Se dice |

En los tres, **ni «cumple» ni «no cumple»**.

### CP-004 — Comprobar no modifica nada

- Retrato de la carpeta antes y después: idéntico.

### CP-005 — Cero comprobaciones es rojo

- Un veredicto con cero corridas y cero fallas **no cumple**.
- Con comprobaciones y sin fallas, cumple.
- Con fallas, no cumple.
- Lo que no se pudo comprobar, tampoco cumple.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales, y este repositorio para la medición. No aplican usuarios.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si las comprobaciones del estándar reconocen lo que deben.** Eso vive allá, con sus 733 pruebas. Acá se prueba que la plataforma las corra y lea bien lo que responden.

**Y no se prueba con un proyecto ajeno.** El único conectado es este repositorio.

---

## 8. Herramientas

El corredor de la plataforma y el punto de entrada del estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un proyecto sin el estándar recibe veredicto · cero comprobaciones sale en verde |
| **Alta** | Una falla sale sin su ubicación · la salida muestra una credencial |
| **Media** | El tiempo no se reporta |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-09-01.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Objetivo |
|---|---|
| Comprobaciones corridas sobre este repositorio | **El número escrito** |
| Cuánto tarda | **El número escrito**, sea el que sea |
| Proyectos sin el estándar que reciben veredicto | **Cero** |
| Archivos modificados al comprobar | **Cero** |

### 12.2 Dónde se miden

Sobre este repositorio, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con carpetas de mentiras | Se corre sobre este repositorio, con sus 32 comprobaciones |
| Dar por bueno el tiempo sin medirlo | Se mide, y el número va escrito aunque sea malo |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ Autorizada la épica entera el 2026-09-01 |
