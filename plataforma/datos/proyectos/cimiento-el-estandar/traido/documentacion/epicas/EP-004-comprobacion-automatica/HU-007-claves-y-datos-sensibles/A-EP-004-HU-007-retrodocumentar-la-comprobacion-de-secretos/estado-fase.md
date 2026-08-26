# Estado de fase — Fase A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos (módulo Comprobación automática)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos` |
| **Módulo** | Comprobación automática — [`secretos.py`](../../../../../validadores/secretos.py) y [`versionado.py`](../../../../../validadores/versionado.py) |
| **Épica / HU / origen** | [EP-004](../../epica.md) · [HU-007](../HU-007-claves-y-datos-sensibles.md) · retro-documentación, fila de HU-007 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8, con la trazabilidad cerrada.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 5 tareas, las 5 hechas | ☑ |
| 7 | Pruebas | [`resultado_pruebas.md`](resultado_pruebas.md) con veredicto **Cumple** | ☑ |
| 8 | Cierre documental | [`funcionalidad_implementada.md`](funcionalidad_implementada.md), §8 de la HU y fila del inventario 48 | ☑ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** §2.7 no dejó dudas abiertas.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3, y los dos transversales |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | 1 — `D-02`, que el plan declaró cobertura completa sin contar los transversales. `D-01` se corrigió acá |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) de esta fase |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | **Hecha** | Caso de la clave armada — CP-001 |
| T-02 | **Hecha** | Caso del archivo que no debe versionarse — CP-002 |
| T-03 | **Hecha** | Caso del ejemplo que no es clave — CP-003 |
| T-04 | **Hecha** | Levantar del programa la lista de lo que cuenta como ejemplo — CP-004 |
| T-05 | **Hecha** | Correr, escribir el resultado y cerrar la trazabilidad |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Las claves de la prueba se arman y no se copian de ninguna parte, ni de una ya rotada: una clave real en el repositorio es una clave filtrada | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El caso del falso positivo pesa igual que los dos aciertos: un detector con falsos positivos se apaga, y entonces no detecta nada | §2.6 del plan |
| Lo que se le escape al detector se anota, no se amplía de paso: ampliarlo cambia qué falla en todos los proyectos | §2.6 del plan |
| La lista de lo que cuenta como ejemplo se levanta **del programa**, y la prueba falla si documento y programa dejan de coincidir | Riesgo `R-03` y CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |

---

## 3. Pendiente / preguntas abiertas

- **La aprobación del plan.** Es lo único que falta para arrancar.
- **La limpieza se comprueba, no se supone** (riesgo `R-01`): cada caso verifica que la carpeta temporal se borró y que ninguna cadena quedó en el árbol.
- **Si aparecen falsos positivos en el repositorio** (riesgo `R-02`): se anotan. Ajustar el detector se propone aparte.

---

## 4. Si se bloqueó

No se bloqueó. Está detenida en la etapa 9 esperando la autorización del commit, que es la puerta normal.
