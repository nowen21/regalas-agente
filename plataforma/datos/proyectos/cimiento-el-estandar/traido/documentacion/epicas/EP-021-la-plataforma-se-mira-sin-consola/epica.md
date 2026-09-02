# EP-021 — La plataforma se mira sin consola

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-021 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulos** | Avisos, Ciclo de vida, Comprobaciones, Aprobaciones, Memoria |
| **Versión del producto** | 5 |
| **Funcionalidades que cubre** | Ninguna nueva. **Completa la mitad de pantalla** de `F-012`, `F-016`, `F-021`, `F-024`, `F-029` y `F-030` |
| **Estado** | Terminada el 2026-09-02: su historia cumple |
| **Fecha de apertura** | 2026-09-02 |

---

## 2. Resumen ejecutivo

Que lo que la plataforma sabe se pueda mirar sin abrir una consola.

## 3. Problema y oportunidad

**Trece módulos, y solo dos con pantalla.** Proyectos e Importación. Los otros once responden por orden de consola, y varias de sus fichas piden explícitamente pantalla: `F-012`, `F-024`, `F-029` y `F-030` dicen «Pantalla y lógica» en su casilla de qué necesita construirse.

**Y la consola no resuelve el problema que estas funcionalidades vinieron a resolver.** La ficha de `F-029` pide *que enterarse no dependa de ir a mirar*: una orden de consola sigue pidiendo ir a mirar, solo que a otro lado. La de `F-012` dice que sirve *para ver todas las fases a la vez*, y doscientas líneas en una terminal no se ven a la vez. La de `F-024` es la más clara: *hoy solo el agente ve lo que recuerda*.

## 4. Objetivo y propuesta de valor

Cerrar la mitad que falta de seis funcionalidades ya construidas.

**Beneficios esperados:**

- Un tablero donde se ve cómo va cada proyecto y qué se salió de lo acordado.
- Las 216 fases de un proyecto, con su estación y su puerta pendiente, en una sola pantalla.
- Lo comprobado, lo aprobado y lo recordado, sin escribir una orden.

## 5. Alcance

**Dentro:** cinco pantallas de solo mirar.

| Pantalla | Dónde | Qué muestra |
|---|---|---|
| `P-03` Tablero | `/tablero/` | El avance y la deuda de cada proyecto, y los avisos |
| `P-04` Fases | `/proyecto/<id>/fases/` | La estación de cada fase y qué le falta |
| `P-05` Funcionalidades | `/proyecto/<id>/funcionalidades/` | Qué está comprobado, y de dónde sale |
| `P-06` Aprobaciones | `/proyecto/<id>/aprobaciones/` | Qué está aprobado y qué caducó |
| `P-07` Memoria | `/proyecto/<id>/memoria/` | Qué recuerda el agente |

**Fuera:**

- **Cambiar algo desde la pantalla.** Aprobar, corregir un recuerdo, abrir una fase y dar de baja son cambios de estado, y `00·N1` los quiere con su confirmación. Siguen por consola.
- **Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén.** Seis módulos siguen sin pantalla, y queda declarado.

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Mira |
| El agente | Nada: estas pantallas son para el usuario |

## 7. Criterios de aceptación de la épica

- Las cinco pantallas responden, y se llega a ellas sin escribir la dirección.
- **Una pantalla vacía dice que está vacía**, y por qué.
- **Ninguna convierte un «no se sabe» en un cero.**
- Cada una dice **qué no muestra**.
- Un proyecto que no existe da 404, no una pantalla rota.

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Pantallas que se ven en blanco cuando no hay datos | **Cero** |
| «No se sabe» escritos como cero | **Cero** |
| Pantallas que no dicen qué dejan por fuera | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-ver-el-estado-sin-abrir-la-consola/HU-001-ver-el-estado-sin-abrir-la-consola.md) | Ver el estado sin abrir la consola | La pantalla de `F-012`, `F-016`, `F-021`, `F-024`, `F-029` y `F-030` | **Terminada el 2026-09-02** |

## 10. Consideraciones técnicas

**Ninguna lógica nueva.** Las cinco pantallas llaman a lo que los módulos ya calculan; si alguna necesitara lógica propia, sería lógica en dos lugares.

**Nada que salga a la red**, como la pantalla que ya existía: la plataforma tiene que servir sin conexión.

**Y las advertencias viajan con la pantalla, no aparte.** La definición de cada columna, el «vencida es un número puesto acá», el «no son todos los documentos»: van impresos donde se leen los datos. Una advertencia que vive en otro archivo no se lee.

## 11. Dependencias

Depende de `EP-019` y `EP-020`, que son las que calculan lo que estas pantallas muestran, y de la pantalla de proyectos, desde donde se llega a cuatro de las cinco.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que una pantalla vacía se lea como una falla** | Cada una dice que está vacía y por qué |
| **Que una pantalla dé a entender que muestra todo** | Cada una dice qué deja por fuera |
| Que un «no se sabe» se escriba como cero | Sale como «sin datos», o como «no lo dice» |
| Que la lógica se duplique en la vista | Las vistas no calculan: piden |

## 13. Supuestos y restricciones

**Supuestos:** que el proyecto está conectado y sus documentos se pueden leer.

**Restricciones:** solo mirar; nada sale a la red; seis módulos siguen sin pantalla.

## 14. Hoja de ruta

Cierra la versión 5, después de `EP-019` y `EP-020`.

## 15. Definition of Ready

- ☑ `EP-019` y `EP-020` cerradas.
- ☑ Medido: trece módulos, dos con pantalla.
- ☑ Las cinco especificaciones que decían «sin pantalla» identificadas.

## 16. Definition of Done

- ☑ La historia cerrada, con veredicto por criterio.
- ☑ Comprobado que lo vacío se dice.
- ☑ Comprobado que ninguna escribe cero donde no se sabe.
- ☑ Las cinco §7 de las especificaciones puestas al día.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-02 | **Terminada**: las cinco pantallas construidas y probadas el mismo día |
| 2026-09-02 | Nace de una pregunta del usuario —«qué sigue»— y de medir que once de trece módulos no tenían pantalla |
