# Estado de fase · Fase `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` |
| **Módulo** | Cuerpo de reglas y `validadores/` |
| **Planteamiento / Épica / HU** | [EP-005](../../epica.md) · [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) · [pendiente 100](../../../../../pendientes/100-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Última actualización** | 2026-09-28 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son las RN-04 y RN-05 de la HU |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Versiones 1 y 2 |
| 8 | Implementador | implementado + pruebas verdes | ☑ |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑ |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | |
| T-02 | Terminada | |
| T-03 | Terminada | |
| T-04 | Terminada | 7 pruebas nuevas; 15 en total, en OK |
| T-05 | Terminada | 242 reglas leídas y clasificadas |
| T-06 | Terminada | 242 líneas puestas en 99 archivos |
| T-07 | Terminada | 252 reglas en el mapa |
| T-08 | Terminada | Solo reporta los 2 programas que de verdad faltan |
| T-09 | Terminada | |
| T-10 | Terminada | |
| T-11 | Terminada | |
| T-12 | Terminada | |
| T-13 | Terminada | |
| T-14 | Terminada | Tres ajustes al probar: tope exacto, orden y palabras genéricas |
| T-15 | Terminada | 19 casos |
| T-16 | Terminada | |

**Hechas:** 16 de 16. **Bloqueadas:** ninguna.

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| H-8 se resuelve en esta HU porque salió en ella: el usuario decidió que una HU no deja nada abierto | Ninguna todavía: queda en la HU y en el resumen de la sesión |

## 3. Pendiente / preguntas abiertas

- Construida y probada. Falta que el usuario lea el cambio y autorice el commit.

## 4. Si se bloqueó

- **Estación:** 8. **Motivo:** dependencia no vista. Al clasificar los programas del amarre apareció `validadores/recuperar.py`, que ya lleva al agente las reglas que pide cada mensaje, falla y no está conectado en este repositorio (H-9 del resumen de la sesión). **Cómo se resolvió:** el usuario eligió que la fase haga trabajar al recuperador con el mapa; el plan pasó a la versión 2 y vuelve a aprobación.
- **Hecho antes de detenerse:** T-01 a T-04 (validador, subcomando, `pre-push` y pruebas) y T-08 (la corrección del amarre), sin commit.
