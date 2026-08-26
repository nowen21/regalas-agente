# Estado de fase — Fase B-EP-004-HU-008: ningún validador termina en silencio

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-008-ningun-validador-termina-en-silencio` |
| **Módulo** | Comprobación automática (`validadores/`) |
| **Épica / HU / Pendiente** | [EP-004](../../epica.md) · [HU-008](../HU-008-corrida-completa.md) · [pendiente 53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** 9 — commit único. **Última puerta pasada:** 8.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «resuelva los p0,p1,p2,p3» | ☑ |
| 3 | Diseño del plan detallado | los dos planes escritos | ☑ |
| 4 | Pausa y presentación | presentados | ☑ |
| 5 | Aprobación del plan detallado | 👤 **ver la nota de abajo** | ☑ |
| 6 | Ejecución continua | plan implementado | ☑ |
| 7 | Pruebas | veredicto **Cumple**, ciclo 1 | ☑ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 **acá está detenida** | ☐ |
| 10 | Reporte al usuario | | ☐ |
| 11 | Publicación / despliegue | 👤 | ☐ |

**Sobre la estación 5, y que quede dicho.** El usuario pidió tres veces seguidas que se resolvieran los pendientes —«resuelva los pendientes», «resuelva 10 pendientes de una», «resuelva los p0,p1,p2,p3»— después de que el agente le planteara dos veces la puerta de aprobación. Se tomó como aprobación del alcance, no como que la puerta no exista. **Los dos planes se escribieron antes de tocar código** y están sin modificar desde entonces; lo que no hubo fue un «sí» explícito por plan.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5, transversales incluidas |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | `D-02` y `D-03`, los dos fuera del alcance declarado en el plan §1 |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §9 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | Línea base guardada y comparada con `git stash` |
| T-02 | Hecha | **33 de 45** módulos con el hueco |
| T-03 | Hecha | `comun.no_es_punto_de_entrada()` |
| T-04 | Hecha | Los 33, cada uno con su subcomando |
| T-05 | Hecha | `validar.py metareglas`, con `--catalogo` |
| T-06 | Hecha | 6 casos que leen el disco |
| T-07 | Hecha | `expectedFailure` retirado, y escrito qué no comprueba |
| T-08 | Hecha | Mismos 8 fallos y 1 error que antes; 0 nuevos |

**Hechas:** 8 de 8. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Dónde queda |
|---|---|
| Código de salida **2**, para que «no comprobé» no se confunda con «hay fallas» | Plan §2.6 y `CP-003` |
| El ayudante vive en `comun.py`: 33 copias envejecen distinto | Plan §2.6 |
| La prueba lee los módulos del disco, no de una lista | Plan §2.6 y `CP-006` |
| **No era un descuido de un archivo: era el comportamiento por omisión de 33 de 45** | [funcionalidad_implementada.md](funcionalidad_implementada.md) |
| **El reparador es peor que el validador**: `citas.py --aplicar` escribiría en `base/` lo que el 55 solo denunciaba como reporte de más | `D-03`, al pendiente 55 |

---

## 3. Pendiente / preguntas abiertas

- **El commit.** Lo autoriza el usuario aparte, y es lo único que detiene la fase.
- **Hay otra sesión escribiendo en el mismo árbol.** Sus 8 fallos y 1 error estaban antes y siguen; no se tocaron. Al commitear, solo entra lo de esta fase.

---

## 4. Si se bloqueó

No se bloqueó. La medición del `git stash` evitó el único bloqueo posible, que era confundir los fallos de la otra sesión con daño propio.
