# HU-011 · El gasto llega a la base en cuanto Claude Code lo escribe


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-011 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/instalar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mira el gasto de tokens en Cimiento
- **Quiero** que lo que hace cualquier sesión llegue a la base en el momento
- **Para** ver el tablero en vivo sin que abrirlo tenga que leer los registros

---

## 3. Contexto y descripción

El gasto llegaba en vivo solo por la telemetría, que no trae enganches y solo la mandan las sesiones abiertas después de activarla; el `.jsonl` se leía al abrir el tablero y una vez al día ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 1, puntos 2, 3 y 15).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | `manage.py vigilar_consumo` queda corriendo: se despierta cuando cambia un `.jsonl` de un proyecto activo (`watchdog`) y guarda lo nuevo con el lector y el guardado que ya existen | Punto 2 |
| RN-02 | Al arrancar lee desde donde quedó cada archivo, y vuelve a leer cada minuto la lista de proyectos activos | Punto 2 |
| RN-03 | Guarda su número de proceso, y `vigilar_consumo --parar` lo detiene por él | Punto 2; `04·S10` |
| RN-04 | La instalación lo arranca al iniciar sesión en Windows y quita la tarea diaria; la desinstalación lo detiene y lo quita | Punto 2; `02·F30` |
| RN-05 | «Gasto» deja de leer los `.jsonl` al abrirse: solo consulta la base | Punto 3 |
| RN-06 | El plan de la fase de la HU-006 cita `04·S10` como lo que es: el proceso que queda corriendo guarda su número para cerrarlo por él | Punto 15 |

### 3.2 Supuestos

- Windows avisa los cambios de archivos de `~/.claude/projects/`.

### 3.3 Fuera de alcance

- Otros sistemas: se dice cómo arrancarlo a mano.

---

## 4. Criterios de aceptación

### CA-01 · Lo nuevo se guarda cuando cambia el archivo

**Sale de:** análisis 2 del pendiente 119, punto 2.

```gherkin
Dado un proyecto activo con su carpeta de Claude Code
Cuando un .jsonl de esa carpeta cambia
Entonces el vigilante guarda lo nuevo sin duplicar
Y un archivo de un proyecto que no está activo no se lee
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_vigilante` desde `proyectos/cimiento/` → pasan los casos de guardar.

**Aprobado cuando:** la base tiene las llamadas del archivo cambiado.

### CA-02 · Se arranca, se detiene y se instala

**Sale de:** análisis 2 del pendiente 119, punto 2.

```gherkin
Dado el vigilante corriendo
Cuando se pide --parar
Entonces el proceso de su número se detiene y el archivo del número se borra
Y la instalación lo pone a arrancar al iniciar sesión y quita la tarea diaria
Y la desinstalación lo quita
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_vigilante` y `python -m unittest core.herramientas.tests_desinstalar` → pasan los casos de arrancar y quitar.

**Aprobado cuando:** no queda el proceso ni el archivo de arranque.

### CA-03 · El tablero solo consulta la base

**Sale de:** análisis 2 del pendiente 119, punto 3.

```gherkin
Dado el tablero de «Gasto»
Cuando se abre
Entonces no lee ningún .jsonl
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_vigilante` → pasa el caso del tablero.

**Aprobado cuando:** abrir el tablero no llama al lector.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Lo escrito llega a la base en menos de 5 segundos |
| RNF-02 | **Dependencias** | `watchdog` con versión fijada en `requirements/base.txt` y en `lock.txt` (`10·DEP2`) |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 1.

---

## 7. Tareas técnicas derivadas

- [x] El vigilante y su orden.
- [x] La instalación y la desinstalación.
- [x] El tablero sin lectura.
- [x] La cita del plan de la HU-006.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-011-el-vigilante` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-011-el-vigilante/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-011-el-vigilante/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-011-el-vigilante/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | `watchdog` | Medio |
| Riesgo | Que el proceso quede vivo sin saberlo | Guarda su número y se detiene por él |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 2 del pendiente 119 |
