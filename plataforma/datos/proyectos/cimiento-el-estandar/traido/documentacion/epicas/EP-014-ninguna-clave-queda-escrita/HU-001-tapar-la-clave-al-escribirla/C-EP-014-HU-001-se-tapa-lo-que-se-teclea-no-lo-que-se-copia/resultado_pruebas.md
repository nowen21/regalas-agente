# Resultado de Pruebas — Fase `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia` |
| **HU** | [HU-001 Tapar la clave al escribirla](../HU-001-tapar-la-clave-al-escribirla.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre los documentos guardados de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **13** |

**Los documentos de este repositorio, revisados:**

| | Cuánto |
|---|---|
| Documentos revisados | **1 002** |
| Parecen traer credenciales | **7 documentos, 21 fragmentos** |
| De esos 21, claves de verdad | **Ninguna** |
| **Documentos alterados** | **0** |
| Caminos que escriben, declarados | **6 de 6** |
| Caminos que tapan | 2: auditoría y el que teclea |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Una clave tecleada al llenar queda tapada

Llenar un hueco con `password: "inventada123"` deja en el archivo el nombre de la variable y **no** la clave. Lo mismo sin comillas. Un texto sin claves se escribe idéntico: tapar no cambia lo que no era una clave.

**Resultado: pasa.**

### CP-002 — Se dice cuántas se taparon

Con una clave vuelve uno; con texto limpio, cero. **Tapar en silencio dejaría al usuario creyendo que escribió otra cosa**, y lo que se guardó ya no es lo que tecleó.

**Resultado: pasa.**

### CP-003 — Lo importado no se altera

**El caso que decide la fase.**

Un documento con una clave de ejemplo escrita se guarda tal cual, se lee tal cual, y revisarlo lo encuentra **sin tocarlo**.

**Resultado: pasa.**

### CP-004 — Lo que no se tapa se dice

Sobre los 1 002 documentos guardados:

```
Documentos revisados: 1002
Parecen traer credenciales: 7 documento(s), 21 fragmento(s).

    6  .../D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/resultado_pruebas.md
    5  .../A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/resultado_pruebas.md
    4  .../B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa/resultado_pruebas.md
    ...
```

**Los siete son documentos de fases que hablan del tapador.** Tres de ellos son las fases que lo construyeron. Sus «claves» son los casos de prueba escritos.

**Resultado: pasa.**

### CP-005 — Sin enmascarador no se escribe

Con la ruta de validadores apuntando a una carpeta que no existe, tapar **revienta**. No devuelve el texto tal cual, que es lo que convertiría una protección en un adorno.

**Resultado: pasa.**

---

## 3. La medición que recortó el alcance antes de construir

El plan puso primero la medición, y fue la que fijó qué se hace:

| Si taparan los seis caminos | Resultado |
|---|---|
| Documentos que cambiarían | **7** |
| Fragmentos que se taparían | **21** |
| Cuántos eran claves de verdad | **Ninguna** |

Los 21 viven en documentos que **hablan del tapador**. Taparlos habría corrompido la documentación del propio tapador, **en silencio y sin vuelta atrás**.

Es el tercer caso de la misma familia en esta sesión: un documento que habla de algo parece contenerlo. Con los espacios por llenar se podía recontar; **acá se habría perdido el texto**.

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Los 7 documentos que la orden nombra | Los 7 traen claves inventadas escritas como ejemplo |
| Que ninguno cambiara | Ninguno |
| Los seis caminos que escriben | Los seis declarados en la §5.1 de la especificación |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-001-tapar-la-clave-al-escribirla.md#ca-01--una-clave-tecleada-al-llenar-un-hueco-queda-tapada) | CP-001 | **Cumple** |
| [CA-02](../HU-001-tapar-la-clave-al-escribirla.md#ca-02--se-dice-que-se-tapó) | CP-002 | **Cumple** |
| [CA-03](../HU-001-tapar-la-clave-al-escribirla.md#ca-03--lo-importado-no-se-altera) | CP-003, §3 | **Cumple** |
| [CA-04](../HU-001-tapar-la-clave-al-escribirla.md#ca-04--lo-que-no-se-tapa-se-dice) | CP-004 | **Cumple** |
| [CA-05](../HU-001-tapar-la-clave-al-escribirla.md#ca-05--sin-enmascarador-no-se-escribe) | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Medir antes de construir | Hecho, y **recortó el alcance** |
| Tapar en el camino que teclea | Hecho |
| Contar sin tocar | Hecho: 7 documentos, 21 fragmentos, **cero alterados** |
| Declarar los seis caminos | Hecho, en la §5.1 de la especificación |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

`F-031` deja de estar construida a medias: de un camino que tapaba se pasó a **los dos que teclean**, y los otros cuatro quedan declarados con su razón. Lo que se escribe se tapa; lo que ya existía entra como está y se dice.

**Lo que la medición evitó:** tapar los seis caminos habría alterado 7 documentos reales sin vuelta atrás, y ninguno de los 21 fragmentos era una clave.

**Y lo que esta fase no puede decir:** si el reconocedor reconoce todo lo que hay que reconocer. Eso vive en el estándar, con sus pruebas.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 13 pruebas del módulo | `plataforma/nucleo/seguridad/tests.py` |
| EV-02 | La orden sobre este repositorio | §1 y §2 |

**Las dos baterías:** 733 pruebas del estándar y 315 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
