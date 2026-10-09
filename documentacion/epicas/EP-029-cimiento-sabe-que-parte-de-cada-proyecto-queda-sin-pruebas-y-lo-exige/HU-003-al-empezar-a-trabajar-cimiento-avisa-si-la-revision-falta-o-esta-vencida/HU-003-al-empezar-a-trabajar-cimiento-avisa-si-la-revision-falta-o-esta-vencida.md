# HU-003 · Al empezar a trabajar, Cimiento avisa si la revisión falta o está vencida

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/pruebas/`, el aviso de arranque, el enganche de commit, el instalador y el desinstalador |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja en un proyecto que administra Cimiento
- **Quiero** que al empezar a trabajar Cimiento me avise si la revisión de pruebas falta o está vencida, y que el instalador deje puesta la herramienta que revisa
- **Para** no acumular partes sin pruebas sin darme cuenta

---

## 3. Contexto y descripción

Nada obliga hoy a revisar las pruebas. Sale del [análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), puntos 7, 8 y 11 de «Lo que se tiene que hacer»; su plan sigue la R-19 de los análisis 2 y 3.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Al empezar a trabajar, Cimiento compara las opciones del proyecto con su última revisión, leyendo su base sin arrancar Django (acuerdos 7 y 11) |
| RN-02 | Avisa si falta la herramienta que revisa, si nunca se revisó o si la última revisión pasó los días elegidos (acuerdo 11) |
| RN-03 | Con «nada», no avisa. Con «solo avisar», avisa y deja seguir. Con «no dejar guardar», además el commit se rechaza hasta revisar (acuerdo 11) |
| RN-04 | Sin base o sin registro, no avisa ni detiene: el proyecto no administrado no tiene nada que cumplir |
| RN-05 | El instalador pone la herramienta que revisa: en Python y Django instala coverage.py en el Python del proyecto si le falta; en Laravel y Angular comprueba que esté y, si falta, dice qué hacer (acuerdo 7) |
| RN-06 | El desinstalador quita solo lo que puso Cimiento (`02·F30`) |
| RN-07 | Los avisos se entienden sin saber del tema (acuerdo 8) |

### 3.2 Supuestos

- La instalación corre en la máquina donde están el proyecto y la base de Cimiento.

### 3.3 Fuera de alcance

- PCOV: es una extensión de PHP que no se instala sola; se dice cómo instalarla.

---

## 4. Criterios de aceptación

### CA-01 · El aviso al empezar a trabajar

**Sale de:** análisis 1 del pendiente 141, puntos 7 y 11

```gherkin
Dado un proyecto registrado con «solo avisar» y 7 días
Cuando su última revisión fue hace 12 días
Entonces al empezar a trabajar sale «La última revisión de pruebas fue hace 12 días. Toca hacer otra»
Y si nunca se revisó, o le falta la herramienta, sale el aviso que corresponde
Y con «nada», o sin registro, no sale ninguno
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-02 · «No dejar guardar» rechaza el commit

**Sale de:** punto 7

```gherkin
Dado un proyecto con «no dejar guardar» y la revisión vencida
Cuando se revisa lo que entra en el commit
Entonces la revisión de pruebas sale como falla y el commit se rechaza
Y con «solo avisar» sale como aviso y el commit pasa
```

**Cómo validarlo:** correr `manage.py test core.pruebas core.herramientas.tests_validar` → resultado esperado: los casos pasan.

### CA-03 · El instalador pone la herramienta y el desinstalador quita la suya

**Sale de:** punto 8

```gherkin
Dado un proyecto Django sin coverage.py en su Python
Cuando se instala Cimiento en él
Entonces se instala coverage.py y la base dice que tiene la parte que revisa y que la puso Cimiento
Y al desinstalar se quita, porque la puso Cimiento
Y si el proyecto ya la tenía, al desinstalar se deja
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | El aviso lee la base en una sola conexión, sin Django |
| RNF-02 | **Disponibilidad** | Sin base, el aviso se calla y el commit pasa |
| RNF-03 | **Usabilidad** | Avisos en palabras sencillas (`00·ID7`) |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| Modelo de datos afectado | `PruebasDelProyecto` gana `instalada_por_cimiento` |

---

## 7. Tareas técnicas derivadas

- [x] El aviso sin Django y su lugar en el arranque.
- [x] La comprobación del commit.
- [x] Poner y quitar la herramienta.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-003-aviso-commit-e-instalacion` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-029-HU-003-aviso-commit-e-instalacion/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-003-aviso-commit-e-instalacion/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-003-aviso-commit-e-instalacion/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Las HU-001 y HU-002: las opciones y las revisiones | Sin ellas no hay qué comparar |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Depende de las HU-001 y HU-002 |
| **N**egociable | Sí | |
| **V**aliosa | Sí | La revisión deja de depender de que alguien se acuerde |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django con la base y las órdenes simuladas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 141 |
