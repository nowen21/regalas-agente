# HU-022 · Un pendiente cerrado se puede reabrir


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-022 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/herramientas/cerrar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene el backlog del estándar
- **Quiero** reabrir un pendiente que se cerró antes de tiempo
- **Para** no moverlo a mano ni dejar enlaces rotos

---

## 3. Contexto y descripción

`cerrar.py` mueve un pendiente a `pendientes/hecho/`, arrastra sus enlaces y deja su fila del índice como hecha. No hay cómo deshacerlo ([análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 4, punto 7). Es la contraria que pide [`02·F30`](../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | `cerrar.py reabrir «número» --motivo «…» --fecha «…»` devuelve el pendiente de `hecho/` a `pendientes/«número»-«nombre».md`, arrastrando sus enlaces en los dos sentidos, como al cerrar | Punto 7 |
| RN-02 | Su fila del índice vuelve a abierta: el número sin tachar y el enlace sin la marca de hecho | Punto 7 |
| RN-03 | El pendiente dice que se reabrió, cuándo y por qué; si decía «**Estado:** hecho», pasa a «reabierto» | Propuesta del agente |
| RN-04 | El aviso de vuelta que se mandó al cerrar no se deshace: ya pudo leerse; la orden lo dice | Propuesta del agente (`02·F30`, excepción) |
| RN-05 | Sin `--aplicar`, dice qué haría y no toca nada | Como `cerrar.py` |

### 3.2 Supuestos

- El pendiente se cerró con `cerrar.py`, y su fila del índice tiene la forma de hecho.

### 3.3 Fuera de alcance

- Los pendientes de la forma nueva (una carpeta con su `pendiente.md`): no se cierran con una orden, su estado se calcula de su análisis.

---

## 4. Criterios de aceptación

### CA-01 · Reabrir con sus enlaces y su fila

**Sale de:** análisis 3 del pendiente 119, punto 7.

```gherkin
Dado un pendiente cerrado con cerrar.py, citado desde otro documento
Cuando se corre reabrir con su número, un motivo y --aplicar
Entonces vuelve a pendientes/ con su número
Y quien lo citaba apunta a la ruta nueva, sin enlaces rotos
Y su fila del índice queda abierta
Y el pendiente dice que se reabrió y por qué
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_reabrir` desde `proyectos/cimiento/` → pasan los casos de reabrir.

**Aprobado cuando:** cerrar y reabrir dejan las citas y la fila como estaban antes de cerrar.

### CA-02 · Lo que no se puede reabrir se dice

**Sale de:** análisis 3 del pendiente 119, punto 7.

```gherkin
Dado un número que no está cerrado, un destino que ya existe o la orden sin --aplicar
Cuando se corre reabrir
Entonces no se toca nada
Y se dice por qué, o qué se haría
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_reabrir` → pasan los casos de rechazo y simulación.

**Aprobado cuando:** los archivos quedan iguales.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Integridad** | Ningún enlace queda roto |

---

## 6. Diseño y referencias

Documento funcional: [análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), punto 7.

---

## 7. Tareas técnicas derivadas

- [x] `reabrir` en `CerradorDePendientes`, y su modo en `main`.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-022-reabrir-con-sus-enlaces` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-022-reabrir-con-sus-enlaces/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-022-reabrir-con-sus-enlaces/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-022-reabrir-con-sus-enlaces/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Romper enlaces al mover | Se usa el mismo `mover` que cierra |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 3 del pendiente 119 |
