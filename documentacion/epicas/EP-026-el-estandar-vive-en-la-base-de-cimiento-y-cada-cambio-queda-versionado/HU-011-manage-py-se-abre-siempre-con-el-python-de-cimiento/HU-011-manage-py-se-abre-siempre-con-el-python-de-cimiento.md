# HU-011 · `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-011 |
| **Épica / Feature** | [EP-026 · El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/manage.py` |
| **Tipo** | Bug |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja con Cimiento desde cualquier proyecto
- **Quiero** que `manage.py` funcione sin importar con qué Python se abra
- **Para** que la orden de leer las reglas desde la base no falle

---

## 3. Contexto y descripción

El aviso de cada sesión manda a leer las reglas con `python "…/proyectos/cimiento/manage.py" ver_estandar <ruta>` (`cargador.py:68`; también `recuperar.py:319`). Ese `python` es el del computador, que no tiene el conector de MySQL, y la consulta falla. Cimiento usa su propio Python 3.11.9, en `proyectos/cimiento/.venv/`, y con ese funciona. Con el Python de Cimiento, las tildes salen dañadas en la consola de Windows. Sale del [análisis 1 del pendiente 145](../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-1.md), acuerdos 1 y 2, punto 1 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Si `manage.py` se abre con un Python que no es el de `proyectos/cimiento/.venv/` y ese existe, se vuelve a abrir con él, con los mismos argumentos, y devuelve lo mismo que devuelva esa segunda vez |
| RN-02 | Si ya se abrió con el Python de `.venv`, o si `.venv` no existe, sigue con el que lo abrió |
| RN-03 | La salida y los errores se escriben en UTF-8, para que las tildes salgan bien |

### 3.2 Supuestos

- El Python de Cimiento está en `.venv/Scripts/python.exe` (Windows) o en `.venv/bin/python` (Linux y Mac).

### 3.3 Fuera de alcance

- Cambiar el texto del aviso: con `manage.py` corregido, el comando del aviso funciona tal como está.

---

## 4. Criterios de aceptación

### CA-01 · Abierto con el Python del computador, la consulta responde

**Sale de:** análisis 1 del pendiente 145, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado que Cimiento tiene su Python en .venv
Cuando se corre manage.py con otro Python
Entonces manage.py se vuelve a abrir con el de .venv
Y la orden termina sin error
```

**Cómo validarlo:** correr `manage.py test core.comun.tests_arranque` → resultado esperado: el caso que abre `manage.py` con otro Python pasa.

### CA-02 · Sin `.venv`, o ya abierto con él, no se vuelve a abrir

**Sale de:** análisis 1 del pendiente 145, «Dónde más puede pasar»

```gherkin
Dado que .venv no existe, o que manage.py ya corre con el Python de .venv
Cuando se abre manage.py
Entonces sigue con el Python que lo abrió
```

**Cómo validarlo:** correr `manage.py test core.comun.tests_arranque` → resultado esperado: los dos casos pasan.

### CA-03 · Las tildes salen bien

**Sale de:** análisis 1 del pendiente 145, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado un texto con tildes
Cuando manage.py lo escribe en la consola
Entonces sale en UTF-8
```

**Cómo validarlo:** correr `manage.py test core.comun.tests_arranque` → resultado esperado: el caso pasa. Además, correr `python proyectos/cimiento/manage.py ver_estandar base/01-conducta/palabras-clave.md` → resultado esperado: la regla sale con «capítulo» bien escrito.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Funciona en Windows, Linux y Mac |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 145](../../../../historico-chat/resumenes/2026-10-08/pendientes/145-manage-py-usa-el-python-de-cimiento/analisis-1.md) |
| Lo mismo, ya resuelto | `python_de_la_plataforma` en `core/herramientas/corredor.py` |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] `manage.py` busca su Python y se vuelve a abrir con él.
- [x] `manage.py` escribe en UTF-8.
- [x] Pruebas en `core/comun/tests_arranque.py`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-011-manage-py-busca-su-python` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-026-HU-011-manage-py-busca-su-python/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-011-manage-py-busca-su-python/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-011-manage-py-busca-su-python/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que `manage.py` se vuelva a abrir sin fin | Solo se vuelve a abrir si el Python que corre no es el de `.venv`; la segunda vez ya lo es |

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
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Las sesiones vuelven a leer las reglas |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Un archivo y sus pruebas |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 145 |
