# HU-009 · Se avisa cuando un enganche o un archivo pesa demasiado


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/enganches/`, `proyectos/cimiento/core/consumo/lector.py` |
| **Tipo** | Funcional |
| **Prioridad** | Should: novena de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** que el agente sepa, con el mensaje siguiente, que un enganche o un archivo leído pasó el límite de su proyecto
- **Para** decidir a tiempo si ese enganche o ese archivo se achica, se parte o se pasa a un programa

---

## 3. Contexto y descripción

El tablero de la HU-008 muestra qué enganches y qué archivos pesan más, pero solo si alguien lo mira. El aviso por tramo de consumo (`EP-005·HU-014`) ya le llega al agente con cada mensaje, sin detener nada. Este aviso va por el mismo camino, con los límites que cada proyecto tiene en el registro de la HU-003 ([épica](../epica.md); análisis 1 del pendiente 119, acuerdo 10 y punto 9).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Con cada mensaje se revisa el turno anterior: lo que agregó cada enganche y lo que ocupó cada archivo leído | Acuerdo 10 |
| RN-02 | Pasa el límite el que estima más tokens que el límite de su proyecto: por enganche y por archivo, en el registro | Acuerdo 10, HU-003 |
| RN-03 | Cada exceso se avisa una vez: el turno anterior se mide una sola vez, sin guardar estado, como el tramo | `EP-005·HU-014` |
| RN-04 | Avisa, no detiene. El enganche siempre sale con código 0 | `hook_presupuesto.py` |
| RN-05 | Un proyecto sin registro, o sin base de Cimiento, usa los límites por defecto: 2000 y 10 000 | Propuesta del agente: el aviso es informativo y no debe callarse |
| RN-06 | Los límites se leen sin Django, como los niveles del freno | `EP-025·HU-005` |

### 3.2 Supuestos

- En el `.jsonl`, el mensaje del usuario es una línea `user` con texto, escrita antes de lo que agregan los enganches de `UserPromptSubmit` (verificado el 2026-10-05 en la sesión `c3d82767`).

### 3.3 Fuera de alcance

- Marcar los excesos en el tablero.
- Detener la acción: el nivel de una regla lo decide la HU-004.

---

## 4. Criterios de aceptación

### CA-01 · Lo que pasa el límite se avisa con el mensaje siguiente

**Sale de:** análisis 1 del pendiente 119, punto 9.

```gherkin
Dado un turno en el que un enganche agregó más tokens que el límite del proyecto, o se leyó un archivo más grande que su límite
Cuando el usuario manda el mensaje siguiente
Entonces el agente recibe un aviso con el enganche o el archivo, los tokens estimados y el límite
Y lo que no pasó el límite no aparece
```

**Cómo validarlo:**
1. Correr las pruebas de `core.enganches.tests_limites` → pasan los casos con una transcripción de muestra.

**Aprobado cuando:** el aviso nombra solo lo que pasó el límite.

### CA-02 · Cada exceso se avisa una vez

**Sale de:** análisis 1 del pendiente 119, acuerdo 10.

```gherkin
Dado un exceso ya avisado
Cuando llega otro mensaje sin que el turno anterior tenga excesos
Entonces no hay aviso
```

**Cómo validarlo:**
1. Correr las pruebas de `core.enganches.tests_limites` → pasa el caso de dos turnos.

**Aprobado cuando:** el segundo mensaje no trae aviso.

### CA-03 · Los límites son los del proyecto

**Sale de:** análisis 1 del pendiente 119, acuerdo 10.

```gherkin
Dado un proyecto registrado con límites propios
Cuando se revisa su turno
Entonces se usan sus límites
Y sin registro o sin base se usan los de por defecto
```

**Cómo validarlo:**
1. Correr las pruebas de `core.enganches.tests_limites` → pasan los casos de límites.
2. Con un límite bajo en el registro de este proyecto, mandar un mensaje → llega el aviso.

**Aprobado cuando:** el límite del aviso es el del registro.

### Criterios de aceptación transversales

- [ ] Errores: sin base, sin transcripción o con una línea rota, el enganche sale con 0 y no detiene nada (`05`).
- [ ] No regresión: el aviso por tramo sigue igual; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Sin arrancar Django: una consulta a MariaDB por mensaje |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdo 10 y punto 9.

Modelo de datos afectado: ninguno; lee los límites del registro.

---

## 7. Tareas técnicas derivadas

- [ ] El lector separa el turno anterior.
- [ ] Los límites del proyecto, sin Django.
- [ ] El aviso en `presupuesto.py` y en `hook_presupuesto.py`.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-009-avisos-por-limite` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-009-avisos-por-limite/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-009-avisos-por-limite/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-009-avisos-por-limite/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-003, HU-006 | Alto |
| Riesgo | Claude Code cambie el orden de las líneas | La separación del turno vive en el lector, con su prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
