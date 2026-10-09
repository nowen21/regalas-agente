# HU-006 · El visor viejo `interfaz/` sale del estándar

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `interfaz/`, `.claude/settings.json` y `anatomia/` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** que el visor viejo `interfaz/` salga del repositorio
- **Para** que Cimiento sea el único programa del estándar y la revisión de pruebas lo revise a él

---

## 3. Contexto y descripción

`interfaz/` es el visor que reemplazó Cimiento: no cambia desde el 2026-08-22, y por estar antes en las carpetas la revisión de pruebas tomaba ese programa en vez de Cimiento. Sale del [análisis 4 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md), punto 2 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se borra `interfaz/` entera, con su Python (acuerdo 1) |
| RN-02 | Se quitan sus menciones en `.claude/settings.json` y en `anatomia/` (acuerdo 1) |
| RN-03 | Las fases cerradas, `CHANGELOG.md`, `cvds/` y `documentacion/senales.md` quedan como están: son historia (acuerdo 1, `20·M11`) |

### 3.2 Supuestos

- Nada en uso depende de `interfaz/`: ningún `.py` vivo la nombra.

### 3.3 Fuera de alcance

- Cambiar documentos de fases cerradas.

---

## 4. Criterios de aceptación

### CA-01 · `interfaz/` ya no existe y nada vivo la nombra

**Sale de:** análisis 4 del pendiente 141, punto 2

```gherkin
Dado el repositorio del estándar
Cuando se busca interfaz/
Entonces la carpeta no existe
Y ni .claude/settings.json ni anatomia/ la nombran
Y el estándar se reconoce como un solo programa: Cimiento
```

**Cómo validarlo:** correr `manage.py test core.pruebas.tests_un_programa` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Reversibilidad** | Se recupera de git |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 4 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] Borrar `interfaz/` y quitar sus menciones.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-006-sin-interfaz` | CA-01 | (vacío) | [plan_trabajo.md](A-EP-029-HU-006-sin-interfaz/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-006-sin-interfaz/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-006-sin-interfaz/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Ninguna | | |

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
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | El estándar se revisa a sí mismo |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Prueba de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 4 del pendiente 141 |
