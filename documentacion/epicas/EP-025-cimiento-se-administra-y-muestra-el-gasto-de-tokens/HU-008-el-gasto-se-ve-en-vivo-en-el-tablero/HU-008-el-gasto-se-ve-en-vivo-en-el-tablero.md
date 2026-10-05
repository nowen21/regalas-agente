# HU-008 · El gasto se ve en vivo en el tablero


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/` |
| **Tipo** | Funcional |
| **Prioridad** | Must: octava de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** un tablero con el gasto de tokens de todos los proyectos, que se actualice solo
- **Para** ver dónde se gasta (proyecto, sesión, enganche y archivo leído) y decidir qué pasar a un programa

---

## 3. Contexto y descripción

Las HU-006 y HU-007 dejan el gasto en la base de Cimiento: por la lectura de los `.jsonl` y, en vivo, por la telemetría. Falta verlo ([épica](../epica.md), CAE-03; análisis 1 del pendiente 119, punto 8).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | El tablero muestra todos los proyectos a la vez, y deja ver uno solo | Acuerdo 2 |
| RN-02 | Muestra la primera tanda de niveles: por proyecto, por sesión, por enganche y por archivo leído, más el gasto por día | Acuerdo 7; el día, del turno 31 |
| RN-03 | Al abrirlo lee lo nuevo de los `.jsonl`; después se actualiza solo con htmx, con lo que llega por telemetría | Acuerdo 9, punto 8 |
| RN-04 | Gráficas con ApexCharts; la página con Tabler | Acuerdo 5 |
| RN-05 | Los tokens de entrada cuentan la caché creada, como en `presupuesto.py`; los de enganches y archivos son estimación y así se dicen | HU-006, RN-02 y RN-06 |
| RN-06 | Lo ven los dos grupos, administrador y consulta | Acuerdo 14 |
| RN-07 | Se elige el período: hoy, 7 días o 30 días; por defecto, 7 | Propuesta del agente |

### 3.2 Supuestos

- La base ya tiene el gasto leído por la HU-006.

### 3.3 Fuera de alcance

- Los avisos por límite: HU-009.
- La segunda tanda de niveles: HU-010.

---

## 4. Criterios de aceptación

### CA-01 · El tablero muestra el gasto de todos los proyectos

**Sale de:** análisis 1 del pendiente 119, punto 8.

```gherkin
Dado una cuenta de cualquiera de los dos grupos y gasto guardado
Cuando abre «Gasto» en el menú
Entonces ve los totales, el gasto por proyecto, por día, por sesión, por enganche y por archivo leído
Y las gráficas de proyecto y de día
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos del tablero con datos de muestra.
2. Levantar Cimiento, entrar y abrir «Gasto» → se ven los totales y las gráficas con el gasto real.

**Aprobado cuando:** los números de la muestra salen en la página, con los miles con punto.

### CA-02 · Se filtra por proyecto y por período

**Sale de:** análisis 1 del pendiente 119, acuerdo 2.

```gherkin
Dado gasto de dos proyectos, de hoy y de hace 10 días
Cuando se elige un proyecto o un período
Entonces solo cuenta lo de ese proyecto y ese período
Y un proyecto o un período que no existe se ignora
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de filtro.

**Aprobado cuando:** los totales cambian según el filtro.

### CA-03 · Se actualiza solo

**Sale de:** análisis 1 del pendiente 119, punto 8.

```gherkin
Dado el tablero abierto
Cuando llega una llamada nueva
Entonces a los 10 segundos aparece, sin recargar la página
Y al abrir el tablero se lee lo nuevo de los .jsonl
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de la parte que se recarga y de la lectura al abrir.
2. Con el tablero abierto, mandar un envío de telemetría → el total sube sin recargar.

**Aprobado cuando:** la parte que htmx pide trae la llamada nueva, y abrir el tablero guarda lo nuevo del `.jsonl`.

### Criterios de aceptación transversales

- [ ] Autorización: sin cuenta, la página manda a entrar (`04`).
- [ ] Rendimiento: la parte que se recarga responde en menos de un segundo con el gasto real (`06`).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Las sumas las hace la base, no Python, salvo el gasto por día |
| RNF-02 | **Seguridad** | Solo con cuenta |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdos 2, 5, 7, 9 y 14; punto 8.

Modelo de datos afectado: ninguno; lee las tablas de la HU-006.

---

## 7. Tareas técnicas derivadas

- [ ] Las sumas del tablero.
- [ ] La página, la parte que se recarga y el menú.
- [ ] Las gráficas.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-008-tablero-en-vivo` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-008-tablero-en-vivo/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-008-tablero-en-vivo/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-008-tablero-en-vivo/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-006, HU-007 | Alto |
| Riesgo | La primera lectura de los `.jsonl` al abrir tarde | Solo lee los archivos que cambiaron |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
