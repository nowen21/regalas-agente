# Plan de Pruebas — Fase A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-014 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-014` · [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md), `CA-01` y `CA-02` |
| **Fecha** | 2026-08-21 |
| **Elaborado por** | El agente, por orden del usuario |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Formato proporcional a una sola fase: secciones 3, 5, 6, 9 y 12. El entregable es un documento; las pruebas son conteo, recorrido de enlaces y comparación contra el material de partida.

---

## 3. Estrategia de pruebas

Un solo nivel: **aceptación sobre el documento**, con el adjunto del pendiente 73 (`73-adjunto-guia-desarrollo-profesional.md`, borrado al cerrar; el historial de git lo conserva) como línea base de contenido (es la copia literal de lo que el usuario aprobó en el proyecto de origen). Tres comprobaciones: que no falte nada transversal, que no sobre nada del origen, y que cada punto quede anclado al cuerpo normativo. Los enlaces los comprueba `validar.py estandar`, que ya revisa todo enlace del repositorio.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md) | [CA-01](../HU-014-la-guia-de-entrada-del-estandar.md#ca-01--la-guía-existe-en-el-estándar-completa-y-enlazada-al-cuerpo-normativo) | [CP-001](#cp-001--completa-enlazada-y-sin-restos-del-origen) | Aceptación | Crítica | Parcial (enlaces) | ☐ |
| [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md) | [CA-02](../HU-014-la-guia-de-entrada-del-estandar.md#ca-02--la-guía-llega-a-los-herederos-y-se-encuentra-sin-saber-que-existe) | [CP-002](#cp-002--viaja-se-encuentra-y-no-engorda-el-arranque) | Aceptación | Alta | Parcial (techo) | ☐ |

**Cobertura:** 2 de 2 exigencias = 100%. Los RNF de la HU (legibilidad, neutralidad) se juzgan dentro de CP-001, pasos 3 y 4.

---

## 6. Casos de prueba

### CP-001 — Completa, enlazada y sin restos del origen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-014 / CA-01 |
| **Tipo** | Aceptación — contenido |
| **Prioridad** | Crítica |
| **Precondiciones** | `base/guia-de-entrada.md` escrito (T-01) |
| **Datos de entrada** | El adjunto del pendiente 73 como línea base |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar en la guía nueva los pasos del ciclo | 10, los mismos del adjunto |
| 2 | Contar las cualidades del producto | 9, las mismas del adjunto |
| 3 | Recorrer los enlaces: cada paso y cada cualidad apunta a su regla, capítulo o patrón | Ninguno sin ancla; `validar.py estandar` sin enlaces rotos en el archivo |
| 4 | Buscar restos del proyecto de origen (rutas de `matematica`, su tabla de correspondencia, su stack) | No hay ninguno; el texto es agnóstico (`20·M3`) |
| 5 | Comparar contra el adjunto sección por sección | Nada transversal se perdió (incluida la frase que resume) |

**Resultado esperado final:** la guía dice lo mismo que aprobó el usuario, en versión del estándar y anclada a él.

---

### CP-002 — Viaja, se encuentra y no engorda el arranque

| Campo | Valor |
|---|---|
| **HU / CA** | HU-014 / CA-02 |
| **Tipo** | Aceptación — integración |
| **Prioridad** | Alta |
| **Precondiciones** | CP-001 aprobado |
| **Datos de entrada** | La carpeta `base/`, el README de `base/`, el mapa del sitio y el arranque del cargador |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que la guía está dentro de `base/` | Viaja con la carpeta, sin tocar el instalador |
| 2 | Abrir el README de `base/` | La nombra, con una línea que dice para quién es |
| 3 | Abrir el mapa del sitio | Tiene su fila |
| 4 | Correr el armado del cargador (o su prueba del techo) | El texto de apertura no crece: la guía no está entre los archivos numerados que carga |

**Resultado esperado final:** quien hereda la recibe, quien busca la encuentra, y el arranque queda igual.

---

## 9. Gestión de defectos

Un caso que no dé lo esperado se registra en el `resultado_pruebas.md` §4; la fase no cierra con defecto crítico o alto abierto. Si falta contenido, se completa la guía (es el entregable de esta fase, no una regla sellada); si un enlace no tiene destino porque la norma no existe, eso **no** se resuelve creando la norma: se anota y se propone (`02·F20`).

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | CA con caso / CA totales | 100% (2 de 2) |
| Casos ejecutados | Ejecutados / diseñados | 100% (2 de 2) |
| Tasa de aprobación | Aprobados / ejecutados | 100% |

El resultado vive en el `resultado_pruebas.md` de la fase.
