# HU-020 · Lo que crea el andamio se puede quitar


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-020 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/herramientas/andamio.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must: primera del análisis 3 |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja con el estándar
- **Quiero** quitar una HU, una fase o un pendiente que el andamio creó, con todo lo que creó junto
- **Para** corregir un error sin tocar archivos a mano y sin perder trabajo escrito

---

## 3. Contexto y descripción

El 2026-10-05 el andamio creó una HU con el número equivocado. No había cómo quitarla, el freno bloqueó borrar la carpeta y hubo que hacerlo a mano ([análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdos 1 y 4, punto 5).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | `andamio quitar «carpeta»` quita una HU, una fase o un pendiente, con lo que el andamio creó junto: las filas de la HU en la épica y en el índice de la épica | Acuerdo 4 |
| RN-02 | Si lo que hay es idéntico a lo que el andamio crearía, se borra | Acuerdo 4 |
| RN-03 | Si cambió algo, se archiva en `_archivo/` de la misma carpeta padre, y la fila apunta ahí con «(archivada)»; el número no se vuelve a usar | Acuerdo 4; propuesta del agente para dónde se archiva |
| RN-04 | Sin `--aplicar`, dice qué haría y no toca nada, como el resto del andamio | Andamio |
| RN-05 | Una HU con fases dentro no se quita: primero se quitan sus fases | Propuesta del agente |

### 3.2 Supuestos

- La carpeta la creó el andamio, con sus plantillas actuales.

### 3.3 Fuera de alcance

- Quitar desde la interfaz: se puede sumar después.

---

## 4. Criterios de aceptación

### CA-01 · Lo que sigue siendo plantilla se borra con sus filas

**Sale de:** análisis 3 del pendiente 119, punto 5.

```gherkin
Dado una HU, una fase o un pendiente recién creados por el andamio, sin cambios
Cuando se corre andamio quitar con su carpeta y --aplicar
Entonces la carpeta ya no existe
Y la épica y su índice quedan como estaban antes de crearla
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_andamio` → pasan los casos de quitar plantilla.

**Aprobado cuando:** la épica queda igual a como estaba antes de crear.

### CA-02 · Lo que tiene trabajo se archiva

**Sale de:** análisis 3 del pendiente 119, acuerdo 4.

```gherkin
Dado una HU con su texto cambiado
Cuando se quita
Entonces la carpeta pasa a _archivo/ con todo su contenido
Y su fila en la épica apunta ahí, con «(archivada)»
Y la siguiente HU no reusa su número
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_andamio` → pasan los casos de archivar.

**Aprobado cuando:** nada se pierde y el número queda tomado.

### CA-03 · Lo que no se puede quitar se dice

**Sale de:** análisis 3 del pendiente 119, acuerdo 4.

```gherkin
Dado una HU con fases, una carpeta que no creó el andamio, o el comando sin --aplicar
Cuando se corre andamio quitar
Entonces no se toca nada
Y se dice por qué, o qué se haría
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_andamio` → pasan los casos de rechazo y simulación.

**Aprobado cuando:** los archivos quedan iguales.

### Criterios de aceptación transversales

- [x] No regresión: crear con el andamio sigue igual; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Integridad** | Lo que tiene contenido nunca se borra |

---

## 6. Diseño y referencias

Documento funcional: [análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdos 1 y 4, punto 5.

---

## 7. Tareas técnicas derivadas

- [x] El andamio arma en memoria lo que crearía, para comparar.
- [x] `quitar`, con borrar o archivar y sus filas.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-020-quitar-con-sus-filas` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-020-quitar-con-sus-filas/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-020-quitar-con-sus-filas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-020-quitar-con-sus-filas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que se borre algo con trabajo | Solo se borra lo idéntico a la plantilla; lo demás se archiva |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 3 del pendiente 119 |
