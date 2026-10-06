# HU-027 · La pantalla se entera en el momento de lo que guarda el vigilante

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-027 |
| **Épica / Feature** | [EP-025 — Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/consumo/` y `core/ayuda/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien revisa el gasto de tokens
- **Quiero** que la pantalla «Gasto» muestre lo nuevo en cuanto el vigilante lo guarda
- **Para** ver el gasto en vivo, como se acordó, sin relojes ni recargar

---

## 3. Contexto y descripción

La pantalla preguntaba cada 10 segundos, y ese intervalo no salía de ningún acuerdo. Sale del [análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdos 4 y 7. **Reemplaza el criterio CA-03 de la [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero/HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md)** («a los 10 segundos aparece»): ahora aparece cuando el vigilante lo guarda.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cuando el vigilante guarda algo nuevo, le avisa a Cimiento «hay datos nuevos» |
| RN-02 | Cimiento pasa el aviso a cada pantalla «Gasto» abierta, por SSE |
| RN-03 | La pantalla vuelve a pedir la franja y la pestaña abierta, que leen la base; nunca lee los `.jsonl` |
| RN-04 | Ningún intervalo pide datos; con Cimiento apagado el aviso se pierde sin daño |
| RN-05 | El aviso solo se acepta desde la misma máquina |

### 3.2 Supuestos

- Cimiento corre con `runserver`, que atiende cada conexión en su propio hilo.

### 3.3 Fuera de alcance

- Que las tablas no se reordenen mientras se leen.

---

## 4. Criterios de aceptación

### CA-01 · Lo nuevo aparece sin recargar y sin intervalos

**Sale de:** análisis 1 del pendiente 124, puntos 10 y 11 de «Lo que se tiene que hacer»

```gherkin
Dado la pantalla «Gasto» abierta
Cuando una línea nueva entra a un .jsonl y el vigilante la guarda
Entonces la pantalla se actualiza sola, tomando los datos de la base
Y el código no tiene ningún intervalo de espera
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `.venv/Scripts/python manage.py test core.consumo.tests_en_vivo`.
2. Con Cimiento y el vigilante prendidos, abrir «Gasto», trabajar en una sesión de Claude Code y mirar la hora de la franja → resultado esperado: cambia sola.
- Aprobado cuando las pruebas pasan y la franja cambia sin oprimir nada.

### CA-02 · El aviso solo llega desde la misma máquina

**Sale de:** análisis 1 del pendiente 124, punto 10 de «Lo que se tiene que hacer»

```gherkin
Dado la ruta del aviso
Cuando llega un aviso desde otra máquina, o por GET
Entonces se rechaza y no se avisa a nadie
```

**Cómo validarlo:**
1. Correr `manage.py test core.consumo.tests_en_vivo`.
- Aprobado cuando las pruebas de la ruta del aviso pasan.

### CA-03 · La ayuda dice que se actualiza sola

**Sale de:** análisis 1 del pendiente 124, punto 10 de «Lo que se tiene que hacer»

```gherkin
Dado la ayuda de «Gasto»
Cuando se lee
Entonces dice que lo nuevo aparece solo en cuanto el vigilante lo guarda
```

**Cómo validarlo:**
1. Correr `manage.py test core.ayuda`.
- Aprobado cuando la prueba de la sección pasa.

### Criterios de aceptación transversales

- [x] Autorización: los eventos piden cuenta; el aviso no la pide pero solo acepta la misma máquina.
- [x] No regresión: `core.consumo` y `core.ayuda` en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Sin bibliotecas nuevas: `EventSource` del navegador |
| RNF-02 | **Rendimiento** | Con Cimiento apagado, el vigilante no se demora más de 2 segundos por aviso |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdo 7 |
| Contrato de API | `POST /gasto/aviso/` (local, sin cuerpo, 204) y `GET /gasto/eventos/` (`text/event-stream`, evento `gasto`) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Avisos en memoria, ruta del aviso y ruta de eventos.
- [ ] El vigilante avisa al guardar algo nuevo.
- [ ] La pantalla escucha los eventos.
- [ ] La ayuda.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-025-HU-027-aviso-y-eventos`](A-EP-025-HU-027-aviso-y-eventos/) | CA-01, CA-02 | | [plan_trabajo](A-EP-025-HU-027-aviso-y-eventos/plan_trabajo.md) | [plan_pruebas](A-EP-025-HU-027-aviso-y-eventos/plan_pruebas.md) | | En curso |
| [`B-EP-025-HU-027-la-ayuda-en-vivo`](B-EP-025-HU-027-la-ayuda-en-vivo/) | CA-03 | CA-01 | [plan_trabajo](B-EP-025-HU-027-la-ayuda-en-vivo/plan_trabajo.md) | [plan_pruebas](B-EP-025-HU-027-la-ayuda-en-vivo/plan_pruebas.md) | | Sin empezar |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-025 (el vigilante guarda en el aviso) y HU-026 (la pantalla en partes) | Alto, ya cumplidas |
| Riesgo | Una conexión de eventos que el navegador cierra queda esperando hasta el próximo aviso | Al llegar el aviso, escribir falla y la conexión termina |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Pruebas de las dos fases pasando
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Sus dependencias ya están |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Cumple el «en vivo» acordado |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 124 |
