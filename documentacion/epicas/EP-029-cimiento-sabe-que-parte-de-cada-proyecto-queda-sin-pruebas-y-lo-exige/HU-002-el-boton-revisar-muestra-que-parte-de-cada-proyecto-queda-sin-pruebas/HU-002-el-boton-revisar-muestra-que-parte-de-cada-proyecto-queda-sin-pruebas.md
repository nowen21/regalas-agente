# HU-002 · El botón «Revisar» muestra qué parte de cada proyecto queda sin pruebas

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/pruebas/` y la entrada del menú |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien administra los proyectos desde Cimiento
- **Quiero** dar clic en «Revisar» y ver qué partes de cada proyecto no tienen pruebas
- **Para** saber dónde están los huecos sin entrar a cada proyecto

---

## 3. Contexto y descripción

Ningún proyecto mide qué parte de su programa queda sin pruebas. Sale del [análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), puntos 4, 5, 6 y 11 de «Lo que se tiene que hacer», y del análisis 2, acuerdo 2 (el plan lista antes las migraciones).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cimiento reconoce el lenguaje por los archivos del proyecto: `manage.py` es Django; `artisan` con `composer.json` es Laravel; `angular.json` es Angular; `pyproject.toml`, `setup.py` o `requirements.txt` sin `manage.py` es Python (acuerdo 1) |
| RN-02 | Python y Django se revisan con coverage.py, Laravel con PHPUnit y PCOV, Angular con `ng test --code-coverage` (acuerdo 4) |
| RN-03 | Un proyecto de otro lenguaje queda «sin medición», con un mensaje que lo explica, y la revisión no falla (acuerdo 4) |
| RN-04 | Si falta la herramienta o el proyecto no se puede correr, la revisión queda «falló» con un mensaje que dice qué hacer, en palabras sencillas (acuerdo 8) |
| RN-05 | La revisión arranca con el botón «Revisar» o con la orden `manage.py revisar_pruebas`, que hacen lo mismo (acuerdo 11) |
| RN-06 | La revisión corre aparte, sin dejar la página esperando; mientras corre, la página dice «Revisando» (acuerdo 11, R-01 de la épica) |
| RN-07 | Una página muestra todos los proyectos registrados, uno por fila, con su última revisión y si está al día, vencida o nunca se hizo (acuerdos 3 y 5) |
| RN-08 | Solo quien administra puede revisar o borrar una revisión |
| RN-09 | La contraria de guardar una revisión es borrarla (`02·F30`) |

### 3.2 Supuestos

- El proyecto trae su propio Python en `.venv` o `venv`, como los proyectos Django que ya administra Cimiento.

### 3.3 Fuera de alcance

- Poner la herramienta en el proyecto (HU-003) y las pruebas de navegador (HU-005).

---

## 4. Criterios de aceptación

### CA-01 · Cimiento reconoce el lenguaje de cada proyecto

**Sale de:** análisis 1 del pendiente 141, punto 4

```gherkin
Dado un proyecto con manage.py, otro con artisan y composer.json, otro con angular.json y otro sin ninguno
Cuando Cimiento los revisa
Entonces reconoce Django, Laravel, Angular y ninguno
Y el que no reconoce queda «sin medición», con su mensaje, sin fallar
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-02 · La revisión guarda qué parte quedó sin pruebas

**Sale de:** puntos 4 y 5

```gherkin
Dado un proyecto Django
Cuando se corre la revisión
Entonces queda guardada con la herramienta, el porcentaje y cada archivo con sus líneas sin pruebas
Y si falta la herramienta queda «falló» con un mensaje que dice qué hacer
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-03 · El botón y la orden de consola arrancan la revisión

**Sale de:** punto 5

```gherkin
Dado quien administra, en la página de revisiones
Cuando da clic en «Revisar» de un proyecto
Entonces la revisión arranca aparte y la página dice «Revisando»
Y la orden manage.py revisar_pruebas hace la misma revisión
Y quien no administra no puede revisar
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-04 · Una página muestra todos los proyectos

**Sale de:** puntos 6 y 11

```gherkin
Dado dos proyectos registrados, uno revisado hace 2 días y otro nunca
Cuando se abre «Revisión de pruebas» desde el menú
Entonces cada proyecto sale en su fila, con su lenguaje, su última revisión y si está al día o nunca se revisó
Y el detalle de un proyecto muestra sus archivos con menos pruebas primero
Y una revisión se puede borrar
```

**Cómo validarlo:** correr `manage.py test core.pruebas core.inicio core.ayuda` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Usabilidad** | Mensajes, botones y ayuda sin términos técnicos (`00·ID7`) |
| RNF-02 | **Rendimiento** | La página no espera la revisión; la revisión se corta a los 30 minutos |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| Modelo de datos afectado | `PruebasDelProyecto` gana `revisando_desde` |
| Diseño de pantallas | La guía de diseño de pantallas y el patrón de tablas de la EP-028·HU-006 |

---

## 7. Tareas técnicas derivadas

- [x] Reconocer el lenguaje y revisar con su herramienta.
- [x] La orden de consola y el arranque aparte.
- [x] La página, su detalle, el menú y la ayuda.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-002-revisar-y-su-pagina` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-029-HU-002-revisar-y-su-pagina/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-002-revisar-y-su-pagina/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-002-revisar-y-su-pagina/resultado_pruebas.md) | Cumple; falta el commit |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La HU-001: el estado y las revisiones | Sin ella no hay dónde guardar |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Depende solo de la HU-001 |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Se ven los huecos de todos los proyectos |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django con la herramienta simulada |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 141 |
