# HU-021 · El estándar se puede desinstalar de un proyecto


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-021 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/herramientas/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien instaló el estándar en un proyecto
- **Quiero** quitarlo con una orden
- **Para** dejar el proyecto sin enganches de Cimiento y sin perder nada propio

---

## 3. Contexto y descripción

`python validadores/instalar.py «ruta» --aplicar` pone enganches de git y de Claude Code, copias selladas, la integración continua, carpetas y el registro, y en el propio estándar programa la lectura del consumo y la telemetría. No hay cómo quitarlo ([análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 4, punto 6; [`02·F30`](../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | `instalar.py «ruta» --desinstalar` quita los enganches de git (los archivos con la marca del instalador y `core.hooksPath`) y los de Claude Code (las entradas que llaman al adaptador), sin tocar los ajenos | Punto 6 |
| RN-02 | Quita lo mecánico que puso la instalación: la copia del stack, la plantilla sellada del `CLAUDE.md`, la integración continua de Cimiento y las carpetas base que siguen vacías | Punto 6 |
| RN-03 | Saca el proyecto de `plantillas/proyectos.md` y lo desactiva en Cimiento: no se borra, su gasto sigue siendo historia | Punto 6; modelo `Proyecto` |
| RN-04 | En el propio estándar, quita además la tarea programada de la lectura del consumo y las variables de la telemetría | Punto 6 |
| RN-05 | Deja lo propio del proyecto: `CLAUDE.md`, los cuatro archivos de `.agente/`, `historico-chat/`, la memoria, `documentacion/versiones/`, las líneas del `.gitignore` y `core.longpaths` | Punto 6 |
| RN-06 | Sin `--aplicar`, dice qué quitaría y no toca nada | Como el instalador |

### 3.2 Supuestos

- Lo quitado se reconoce por la marca del instalador o por la ruta del adaptador.

### 3.3 Fuera de alcance

- Desinstalar desde la interfaz de Cimiento.

---

## 4. Criterios de aceptación

### CA-01 · Quitar lo que puso la instalación

**Sale de:** análisis 3 del pendiente 119, punto 6.

```gherkin
Dado un proyecto con el estándar instalado y un enganche ajeno en git y en Claude Code
Cuando se corre instalar.py con --desinstalar y --aplicar
Entonces no quedan enganches de Cimiento, ni la copia del stack, ni la integración continua de Cimiento
Y los enganches ajenos siguen
Y el proyecto sale del registro y queda inactivo en Cimiento
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_desinstalar` desde `proyectos/cimiento/` → pasan los casos de quitar.

**Aprobado cuando:** instalar y desinstalar dejan los enganches como estaban antes.

### CA-02 · Lo propio se queda

**Sale de:** análisis 3 del pendiente 119, punto 6.

```gherkin
Dado un proyecto con CLAUDE.md, .agente/, historico-chat/ y carpetas con contenido
Cuando se desinstala
Entonces todo eso sigue igual
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_desinstalar` → pasan los casos de lo que se queda.

**Aprobado cuando:** esos archivos no cambian.

### CA-03 · Simular y repetir

**Sale de:** análisis 3 del pendiente 119, punto 6.

```gherkin
Dado un proyecto instalado
Cuando se desinstala sin --aplicar, o dos veces
Entonces la simulación no toca nada
Y la segunda vez no hay nada que quitar
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_desinstalar` → pasan los casos de simulación y repetición.

**Aprobado cuando:** los archivos quedan iguales.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Integridad** | Nada que no puso la instalación se borra |

---

## 6. Diseño y referencias

Documento funcional: [análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), punto 6.

---

## 7. Tareas técnicas derivadas

- [x] `Desinstalador`, con cada contraria de `Instalador`.
- [x] `--desinstalar` en la orden y `--baja` en `manage.py registrar`.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-021-desinstalar` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-021-desinstalar/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-021-desinstalar/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-021-desinstalar/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Borrar algo del proyecto | Solo se quita lo marcado o lo que llama al adaptador |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 3 del pendiente 119 |
