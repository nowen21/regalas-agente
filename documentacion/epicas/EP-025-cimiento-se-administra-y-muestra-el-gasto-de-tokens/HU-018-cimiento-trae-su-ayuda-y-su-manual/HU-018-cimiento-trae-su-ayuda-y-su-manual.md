# HU-018 · Cimiento trae su ayuda y su manual


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-018 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/ayuda/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien usa las pantallas de Cimiento
- **Quiero** ayuda en cada campo, en cada pantalla y un manual completo
- **Para** usarlas sin preguntar qué hace cada cosa

---

## 3. Contexto y descripción

scilit tiene una ayuda hecha en su EP-014 (`apps/ayuda`): el «?» de cada campo con su globo, los botones de ayuda de cada pantalla, un panel a la derecha con la sección del manual y el manual completo imprimible. Cimiento no tenía ninguna ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 7, punto 14).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Lo reusable de `apps/ayuda` de scilit pasa a `core/ayuda/`: el «?» por campo con su globo, el texto corto de un botón, los botones de ayuda de una pantalla, el panel a la derecha, el manual completo imprimible | Acuerdo 7 |
| RN-02 | En desarrollo, el «?» sale en rojo si su clave no tiene texto; una prueba exige que toda clave usada tenga texto | Acuerdo 7 |
| RN-03 | Las secciones del manual se escriben para las pantallas de Cimiento con el molde del manual del estándar: para qué sirve, dónde está, qué hacer, qué debe pasar y si algo falla | Acuerdo 7 |
| RN-04 | Toda pantalla tiene su sección; una prueba lo exige para que ninguna nueva quede sin ella | Punto 14 |
| RN-05 | Sin dependencias nuevas: Cimiento no trae la fuente de íconos de scilit, y el «?» se dibuja con CSS | Propuesta del agente |

### 3.2 Supuestos

- Las pantallas usan Tabler, como scilit.

### 3.3 Fuera de alcance

- Que scilit pase a usar esta ayuda: lo hace en su propio trabajo.

---

## 4. Criterios de aceptación

### CA-01 · Ayuda en campos y pantallas

**Sale de:** análisis 2 del pendiente 119, punto 14.

```gherkin
Dado la pantalla «Configuración»
Cuando se abre
Entonces cada ajuste tiene su «?», que abre un globo con su explicación
Y debajo del título están los botones de ayuda de la pantalla
Y «Ayuda» arriba abre a la derecha la sección del manual de esa pantalla
```

**Cómo validarlo:**
1. Correr `python manage.py test core.ayuda` desde `proyectos/cimiento/` → pasan los casos de la ayuda.
2. Entrar a Cimiento, abrir «Configuración» y pulsar el «?» de «Rutas en los avisos» → se abre el globo.

**Aprobado cuando:** la página trae el «?» con su texto y el botón «Ayuda».

### CA-02 · El manual y su cobertura

**Sale de:** análisis 2 del pendiente 119, punto 14.

```gherkin
Dado el manual de Cimiento
Cuando se abre /ayuda/
Entonces trae todas las secciones, se puede imprimir
Y ninguna pantalla de Cimiento queda sin sección
Y toda clave de ayuda usada en una plantilla tiene su texto
```

**Cómo validarlo:**
1. Correr `python manage.py test core.ayuda` → pasan los casos del manual y de la cobertura.

**Aprobado cuando:** las pruebas de cobertura pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | Los textos los entiende quien no sabe del tema (`00·ID7`), en tercera persona e infinitivo (`00·ID10`) |
| RNF-02 | **Accesibilidad** | El «?» se abre con el teclado y se cierra con Esc |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 7. Origen: `C:/DesarrollosClaude/personales/scilit/proyectos/scilit/apps/ayuda/`. Molde: [manual de usuario](../../../../plantillas/manual-usuario.md).

---

## 7. Tareas técnicas derivadas

- [ ] La aplicación `core/ayuda/` con sus etiquetas, vistas y plantillas.
- [ ] Los textos y las secciones de Cimiento.
- [ ] El botón y el panel en la plantilla base; la ayuda en «Configuración» y «Suspensiones».
- [ ] Las pruebas de cobertura.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-018-la-ayuda` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-018-la-ayuda/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-018-la-ayuda/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-018-la-ayuda/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Una pantalla nueva sin sección | La prueba de cobertura falla |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 2 del pendiente 119 |
