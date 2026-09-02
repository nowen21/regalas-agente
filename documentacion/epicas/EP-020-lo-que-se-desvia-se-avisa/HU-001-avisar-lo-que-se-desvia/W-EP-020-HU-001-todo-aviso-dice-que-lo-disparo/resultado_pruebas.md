# Resultado de Pruebas — Fase `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md).

---

## 1. Identificación de la ejecución

| Campo | Valor |
|---|---|
| **Fase** | `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutor** | Ing. José Dúmar Jiménez Ruíz |
| **Ambiente** | La máquina del usuario · Windows · carpetas temporales |
| **Versión del estándar** | 37.2.1 |

---

## 2. Resumen ejecutivo

**Los avisos salen, cada uno dice qué lo disparó y dónde mirar, y lo atendido no vuelve.** Los tres criterios cumplen.

**Y en su primera corrida contra datos reales encontró algo que nadie veía.** Entre las historias sin fase salieron **cinco carpetas vacías** de un `EP-018` con otro nombre, sobrantes de un plan anterior de la misma jornada. Se habían buscado antes sin éxito: `git status` no las mostraba, `grep` sobre todo el repositorio no daba nada, y una lectura byte a byte de todos los archivos tampoco. **No aparecían en ningún archivo porque no había ningún archivo.** Solo las ve algo que recorre el disco.

---

## 3. Casos ejecutados

| Caso | Qué comprobó | Resultado |
|---|---|---|
| CP-001 | Las tres clases, con su disparador y su destino · el orden por gravedad | ✅ |
| CP-002 | **Callado a mano y arreglado por su causa: ninguno vuelve** · el cero se dice | ✅ |
| CP-003 | El tiempo, el tope, la fase terminada y la que no dice desde cuándo | ✅ |

**13 pruebas nuevas.** Ninguna quedó en rojo al cerrar.

---

## 4. Defectos encontrados

**Ninguno en esta fase.** Lo que apareció no fue un defecto del código sino un hallazgo del repositorio: las cinco carpetas vacías, que se quitaron con `rmdir` —que se niega si adentro hay algo, y esa negativa es la comprobación.

---

## 5. Cobertura de los criterios de aceptación

| CA | Caso | Concepto |
|---|---|---|
| CA-01 · Una deuda vencida se avisa | CP-001 | ✅ Cumple |
| CA-02 · Cada aviso dice qué y dónde | CP-001 | ✅ Cumple |
| CA-03 · Lo atendido no vuelve | CP-002 | ✅ Cumple |

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
| La plataforma | 552 | ✅ En verde |
| El estándar | 733 | ✅ En verde |
| Los validadores | 32 | ✅ Sin fallas |

---

## 8. Lo que esta ejecución NO comprueba

- **A partir de cuántos avisos la gente deja de leer.** Es el modo en que esta funcionalidad fracasa, y ninguna prueba lo mide.
- **Si los 30 días son el número correcto.** Depende del proyecto, y por eso se puede cambiar al pedirlo.
