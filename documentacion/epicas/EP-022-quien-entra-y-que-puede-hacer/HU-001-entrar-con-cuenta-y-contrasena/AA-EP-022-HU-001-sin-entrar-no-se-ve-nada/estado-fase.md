# Estado de fase — Fase `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` (módulo Acceso)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` |
| **Módulo** | Acceso |
| **Planteamiento / Épica / HU** | [documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/epica.md](../../epica.md) · [documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/HU-001-entrar-con-cuenta-y-contrasena/HU-001-entrar-con-cuenta-y-contrasena.md](../HU-001-entrar-con-cuenta-y-contrasena.md) |
| **Última actualización** | 2026-09-01 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ Ni un `login_required` en todo el código |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ 2026-09-01: la épica entera, de una |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-022 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ 2026-09-01 |
| 5 | Escritor de especificación | 👤 especificación aprobada | ☑ [documentacion/acceso/spec.md](../../../../acceso/spec.md) |
| 6 | Diseñador | diseño coherente | ☑ Middleware: una pantalla nueva nace protegida |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ 2026-09-01 |
| 8 | Implementador | implementado + pruebas verdes | ☑ 11 pruebas nuevas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ |
| 10 | Crítico | sin hallazgos graves | ☑  |
| 11 | Cierre documental + señales | docs y señales al día | ☑ |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | N/A: la plataforma corre en la máquina del usuario |

> **Catorce pruebas de otros módulos se pusieron en rojo con este cambio.** No era un defecto: era la comprobación de que funcionaba.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Terminada | `auth` instalada |
| T-02 | Terminada | El guardián |
| T-03 | Terminada | La pantalla de entrar |
| T-04 | Terminada | La orden de crear cuentas |
| T-05 | Terminada | Quién entró en la barra |
| T-06 | Terminada | Las pruebas de antes, entrando |
| T-07 | Terminada | 11 pruebas |

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| Un guardián por vista se olvida; uno por middleware hace que lo nuevo nazca protegido | [`S-125`](../../../../senales.md) |
| Una prueba de rutas escrita a mano se queda corta justo el día que hace falta | [`S-125`](../../../../senales.md) |

---

## 3. Pendiente / preguntas abiertas

- **No hay límite de intentos** ni demora entre uno y otro. Con la plataforma en una máquina no expuesta, quien puede intentar ya está adentro; en un servidor, hay que mirarlo.
- **Las cuentas se pierden si se borra la base.** Es lo segundo que no se reconstruye, junto con las aprobaciones.
- **La contraseña solo exige ocho caracteres.**

---

## 4. Si se bloqueó

No se bloqueó.
