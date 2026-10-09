# HU-004 · Cada proyecto consulta su configuración en Cimiento y la copia local desaparece

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/proyectos/`, su ayuda y el instalador |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra los proyectos desde Cimiento
- **Quiero** que la configuración de cada proyecto viva solo en Cimiento
- **Para** que nadie lea una copia vieja creyendo que es la de verdad

---

## 3. Contexto y descripción

Cimiento escribe `.agente/configuracion.md` en cada proyecto cada vez que cambia un ajuste, y ningún programa la lee: los enganches ya consultan la base. Sale del [análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), punto 9 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cimiento deja de escribir `.agente/configuracion.md` (acuerdo 10) |
| RN-02 | La que ya existe en un proyecto se borra al volver a instalar Cimiento en él (acuerdo 10) |
| RN-03 | La ayuda deja de nombrar la copia (acuerdo 8) |

### 3.2 Supuestos

- Ningún programa lee la copia: se verificó en el análisis 1.

### 3.3 Fuera de alcance

- Cambiar cómo los enganches leen la base: ya la consultan.

---

## 4. Criterios de aceptación

### CA-01 · Cimiento ya no escribe la copia

**Sale de:** análisis 1 del pendiente 141, punto 9

```gherkin
Dado un proyecto registrado
Cuando se guarda su configuración o la configuración común
Entonces en su carpeta no aparece .agente/configuracion.md
Y la ayuda no la nombra
```

**Cómo validarlo:** correr `manage.py test core.proyectos core.ayuda` → resultado esperado: los casos pasan.

### CA-02 · Volver a instalar borra la copia vieja

**Sale de:** punto 9

```gherkin
Dado un proyecto con .agente/configuracion.md de antes
Cuando se vuelve a instalar Cimiento en él
Entonces el archivo ya no está
```

**Cómo validarlo:** correr `manage.py test core.proyectos` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Nada que lea la configuración cambia: los enganches siguen leyendo la base |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] Quitar `copia.py` y sus llamadas.
- [x] Borrar la copia vieja al instalar.
- [x] La ayuda y las pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-004-sin-copia-local` | CA-01, CA-02 | (vacío) | [plan_trabajo.md](A-EP-029-HU-004-sin-copia-local/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-004-sin-copia-local/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-004-sin-copia-local/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La HU-001: la configuración nueva ya vive en la base | Ninguno |

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
| **V**aliosa | Sí | Nadie lee datos viejos |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 141 |
