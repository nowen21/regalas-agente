# HU-016 · Cerrar y reabrir una fase, y separar los cambios por sesión, son funcionalidades de Cimiento


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-016 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/herramientas/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien construye con el estándar
- **Quiero** cerrar y reabrir una fase, y separar lo de cada sesión antes de un commit, con órdenes de Cimiento
- **Para** no escribir un guion casi igual cada vez, y que lo único escrito a mano sea lo que un programa no sabe

---

## 3. Contexto y descripción

El 2026-10-05 las fases de las HU-006 a HU-010 se cerraron con cinco guiones casi iguales, y lo de cada sesión se separó con otro guion ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 6). El [análisis 3](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md) le sumó la contraria: reabrir la fase (acuerdo 2).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | `manage.py cerrar_fase «carpeta»` escribe lo que sale del plan y del plan de pruebas: el estado de la fase, y el resultado y la funcionalidad con sus casos y criterios. Lo que un programa no sabe queda como `«…»` | Análisis 2, acuerdo 6 |
| RN-02 | Mientras quede un `«…»` en esos tres documentos, la fase no se cierra: dice dónde falta | Análisis 2, acuerdo 6 |
| RN-03 | Sin marcas pendientes, cierra: marca la matriz del plan de pruebas, escribe el cierre del plan, pone la fila de la fase en la HU y deja «Terminada» la HU y su fila en la épica cuando todas sus fases lo están | Análisis 2, acuerdo 6 |
| RN-04 | Con `--pruebas «orden»`, corre las pruebas antes de cerrar; si fallan, no cierra | Análisis 2, acuerdo 6: «la corrida de las pruebas» |
| RN-05 | `manage.py reabrir_fase «carpeta» --motivo «…»` deshace el cierre: la estación vuelve a 8, la matriz y las filas vuelven a «En curso», el motivo queda en el estado y en el plan, y el resultado suma un ciclo nuevo por llenar | Análisis 3, acuerdo 2 |
| RN-06 | `manage.py cambios_por_sesion` lista lo que cambió cada sesión según el registro de `historico-chat/.tocado/`. Con una sesión y `--preparar`, prepara para el commit solo lo de ella; lo que tocaron dos sesiones lo nombra y no lo prepara. `--soltar` deshace la preparación | Análisis 2, acuerdo 6; análisis 3, acuerdo 2 |
| RN-07 | Sin `--aplicar`, las tres órdenes dicen qué harían y no tocan nada | Como el andamio |

### 3.2 Supuestos

- La fase la creó el andamio y sus planes están llenos.

### 3.3 Fuera de alcance

- Hacer el commit: se sigue preguntando aparte.
- Hacerlo desde la interfaz.

---

## 4. Criterios de aceptación

### CA-01 · Cerrar una fase

**Sale de:** análisis 2 del pendiente 119, acuerdo 6.

```gherkin
Dado una fase con su plan y su plan de pruebas llenos, y sus documentos de cierre en plantilla
Cuando se corre cerrar_fase con --aplicar
Entonces el estado, el resultado y la funcionalidad quedan escritos con sus casos y criterios
Y lo que un programa no sabe queda marcado con «…», y la orden dice dónde
Y cuando se llenan y se corre otra vez, la fase queda cerrada en el plan, la HU y la épica
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_fase` desde `proyectos/cimiento/` → pasan los casos de cerrar.

**Aprobado cuando:** la HU y la épica dicen «Terminada» solo después de llenar las marcas.

### CA-02 · Reabrir una fase

**Sale de:** análisis 3 del pendiente 119, acuerdo 2.

```gherkin
Dado una fase cerrada
Cuando se corre reabrir_fase con un motivo y --aplicar
Entonces la estación vuelve a 8 y la HU y la épica dicen «En curso»
Y el motivo queda en el estado y en el plan
Y el resultado suma un ciclo con marcas por llenar, así que no se vuelve a cerrar sin llenarlo
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_fase` → pasan los casos de reabrir.

**Aprobado cuando:** cerrar y reabrir dejan la HU y la épica como estaban antes de cerrar.

### CA-03 · Separar los cambios por sesión

**Sale de:** análisis 2 del pendiente 119, acuerdo 6.

```gherkin
Dado dos sesiones con archivos cambiados, uno de ellos tocado por las dos
Cuando se corre cambios_por_sesion con una sesión y --preparar --aplicar
Entonces queda preparado para el commit solo lo de esa sesión
Y el archivo compartido se nombra y no se prepara
Y --soltar deja el área de preparación como estaba
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_cambios` → pasan los casos en un repositorio temporal.

**Aprobado cuando:** `git diff --cached` muestra solo lo de la sesión.

### CA-04 · Lo que no se puede hacer se dice

**Sale de:** análisis 2 del pendiente 119, acuerdo 6.

```gherkin
Dado una carpeta que no es una fase, unas pruebas que fallan, o una orden sin --aplicar
Cuando se corre la orden
Entonces no se toca nada
Y se dice por qué, o qué se haría
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_fase core.herramientas.tests_cambios` → pasan los casos de rechazo y simulación.

**Aprobado cuando:** los archivos quedan iguales.

### Criterios de aceptación transversales

- [x] Idempotencia: correr dos veces cerrar o reabrir no duplica filas ([`03·D6`](../../../../base/03-datos.md#d6--concurrencia-e-idempotencia)).
- [x] No regresión: la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Integridad** | Lo que ya está escrito a mano en el resultado y la funcionalidad no se sobrescribe |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 6, y [análisis 3](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 2. Modelos de lo que se escribe: los guiones `historico-chat/scripts/2026-10-05/cerrar_hu_006.py` a `cerrar_hu_010.py` y `clasificar_cambios_de_la_sesion.py`.

---

## 7. Tareas técnicas derivadas

- [x] Cerrar y reabrir una fase.
- [x] Separar los cambios por sesión.
- [x] Las órdenes de `manage.py`.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-016-cerrar-reabrir-y-separar` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-016-cerrar-reabrir-y-separar/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-016-cerrar-reabrir-y-separar/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-016-cerrar-reabrir-y-separar/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Sobrescribir lo escrito a mano | Solo se escribe un documento que sigue en plantilla |
| Riesgo | Preparar para el commit lo de otra sesión | Lo compartido no se prepara |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde los análisis 2 y 3 del pendiente 119 |
