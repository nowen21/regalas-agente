# HU-005 · Cimiento corre las pruebas de navegador de cada proyecto

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/pruebas/`, el instalador y las dependencias de Cimiento |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra los proyectos desde Cimiento
- **Quiero** que la revisión corra también las pruebas que abren las pantallas en un navegador real
- **Para** saber si lo que pasa en la página después de cargarla sigue funcionando

---

## 3. Contexto y descripción

Ninguna prueba usa un navegador real. Sale del [análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), punto 10 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cimiento deja instalado Playwright, con su navegador Chromium, en su propio ambiente (acuerdo 6) |
| RN-02 | Un proyecto tiene pruebas de navegador si tiene `playwright.config` (ts, js o mjs), o archivos de prueba en Python que usan Playwright (acuerdo 6) |
| RN-03 | La revisión las corre con lo del proyecto: `npx playwright test` o el Python del proyecto, y guarda si pasaron, si fallaron o si no hay (acuerdo 6) |
| RN-04 | El resultado sale en la página de revisiones (acuerdo 6) |
| RN-05 | Escribir las pruebas de navegador es trabajo de cada proyecto (acuerdo 6) |
| RN-06 | Las versiones van exactas en las dependencias de Cimiento (`10·DEP2`) |

### 3.2 Supuestos

- Un proyecto que escribe pruebas de navegador tiene Playwright en sus propias dependencias.

### 3.3 Fuera de alcance

- Escribir pruebas de navegador para algún proyecto.

---

## 4. Criterios de aceptación

### CA-01 · La revisión corre las pruebas de navegador

**Sale de:** análisis 1 del pendiente 141, punto 10

```gherkin
Dado un proyecto con playwright.config.ts, otro Django con un archivo de prueba que usa Playwright y otro sin ninguna
Cuando se revisan
Entonces el primero corre npx playwright test y queda «pasaron» o «fallaron» con cuántas
Y el segundo corre esas pruebas con su Python y queda «pasaron» o «fallaron»
Y el tercero queda «sin pruebas de navegador»
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-02 · El resultado sale en la página

**Sale de:** punto 10

```gherkin
Dado un proyecto cuya última revisión dice «pasaron»
Cuando se abre «Revisión de pruebas»
Entonces su fila muestra «Pasaron» en la columna del navegador
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: el caso pasa.

### CA-03 · Cimiento deja instalado Playwright

**Sale de:** punto 10

```gherkin
Dado el ambiente de Cimiento sin Playwright
Cuando se instala el estándar en su propia carpeta
Entonces se instala playwright 1.63.0 y su Chromium
Y al desinstalar se quitan los navegadores de Playwright
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Dependencias** | Versiones exactas en `requirements/lock.txt` (`10·DEP2`) |
| RNF-02 | **Usabilidad** | Resultado en palabras sencillas (`00·ID7`) |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| Modelo de datos afectado | Ninguno: `Revision` ya trae `navegador` y `navegador_detalle` (HU-001) |

---

## 7. Tareas técnicas derivadas

- [x] Encontrar y correr las pruebas de navegador.
- [x] La columna de la página.
- [x] Instalar Playwright en Cimiento y su contraria.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-005-pruebas-de-navegador` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-029-HU-005-pruebas-de-navegador/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-005-pruebas-de-navegador/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-005-pruebas-de-navegador/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La HU-002: la revisión y su página | Sin ella no hay dónde correrlas |
| Riesgo | Chromium pesa varios cientos de megas | La instalación tarda más la primera vez |

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
| **I**ndependiente | Sí | Depende de la HU-002 |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Lo que corre en el navegador queda revisado |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django con las órdenes simuladas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 141 |
