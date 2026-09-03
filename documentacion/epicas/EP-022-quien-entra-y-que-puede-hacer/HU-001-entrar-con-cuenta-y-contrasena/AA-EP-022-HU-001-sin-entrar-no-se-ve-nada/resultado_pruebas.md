# Resultado de Pruebas — Fase `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Ninguna pantalla responde sin haber entrado.** Los tres criterios cumplen.

La prueba que lo sostiene **no usa una lista escrita a mano: recorre las rutas del propio enrutador.** Una lista a mano se queda corta el día que alguien agregue una pantalla, y ese es exactamente el día en que hay que enterarse.

**Y catorce pruebas de otros módulos se pusieron en rojo al hacer el cambio.** No fue un defecto: fue la comprobación. Aprobaban con nombres como «Ing. José» y «quien sea», texto libre que la plataforma aceptaba.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | **Todas las rutas del enrutador** · lo abierto contado · los estáticos · una ruta que no existe todavía | ✅ |
| CP-002 | Lleva a donde se iba · el mensaje único · la contraseña ni en la respuesta ni en claro · salir | ✅ |

**11 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en el código.** Lo que sí apareció, y vale contarlo: **catorce pruebas de otros módulos quedaron en rojo**, todas por la misma razón —aprobaban o pedían pantallas con un nombre inventado—. Eran la señal de que el cambio funcionaba.

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Sin entrar no se ve nada | CP-001 | ✅ Cumple |
| CA-02 · Lleva a donde se iba | CP-002 | ✅ Cumple |
| CA-03 · El mensaje no distingue | CP-002 | ✅ Cumple |

**3 de 3.**

---

## 6. Concepto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |

---

## 7. Las dos baterías completas

| Batería | Pruebas | Resultado |
|---|---|---|
| La plataforma | 610 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **Alguien intentando entrar muchas veces.** No hay límite ni demora, y ninguna prueba lo mira.
- **Que la contraseña que alguien elija sea buena.** Se exige mínimo ocho, y nada más.
- **Que la plataforma aguante estar en un servidor.** Tener cuentas lo vuelve posible; no lo vuelve probado.
