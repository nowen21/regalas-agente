# EP-020 — Lo que se desvía se avisa

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-020 |
| **Producto** | Cimiento, plataforma de gestión de proyectos |
| **Módulo** | Avisos |
| **Versión del producto** | 5, según [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) |
| **Funcionalidades que cubre** | `F-029`, `F-030` |
| **Estado** | Terminada el 2026-09-01: sus dos historias cumplen |
| **Fecha de apertura** | 2026-09-01 |

---

## 2. Resumen ejecutivo

Que enterarse de lo que se salió de lo acordado no dependa de ir a mirar, y que comparar proyectos no engañe.

## 3. Problema y oportunidad

**Todo lo que hace falta saber ya está escrito, y nadie lo lee.** Las fases dicen cuándo se tocaron por última vez, las historias dicen si tienen fase, y el inventario dice qué se construyó sin verificar. Son doscientos archivos.

**Medido acá el 2026-09-01:** 3 historias escritas sin ninguna fase que las construya, y **28 funcionalidades construidas que siguen sin verificarse**.

**Y comparar tiene su propia trampa**, escrita en la ficha de `F-030`: *«comparar proyectos distintos con la misma medida engaña si no se dice qué mide»*.

## 4. Objetivo y propuesta de valor

Que lo que se desvía **salga solo**, ordenado por lo que más duele, y que el reporte diga qué está midiendo.

**Beneficios esperados:**

- Enterarse sin ir a buscar.
- Cada aviso dice qué lo disparó y dónde mirar.
- Comparar proyectos con la misma medida, y con la medida escrita al lado.

## 5. Alcance

**Dentro:**

- Los avisos de lo que se desvió (`F-029`).
- El reporte de cómo va cada proyecto (`F-030`).

**Fuera:**

- **Arreglar lo que se avisa.** El aviso señala; arreglar es otra cosa.
- Mandar el aviso por correo o por notificación.
- La pantalla.

**Alcance funcional, ítem por ítem**

| Funcionalidad | Qué entrega | Versión |
|---|---|---|
| `F-029` Avisar lo que se desvía | Los avisos, de lo que más duele a lo que menos | 5 |
| `F-030` Reportar cómo va cada proyecto | El reporte, con la misma medida y la medida escrita | 5 |

## 6. Usuarios y actores

| Actor | Qué hace acá |
|---|---|
| El usuario | Lee, decide y calla lo que decide callar |
| El módulo Ciclo de vida | Aporta en qué estación va cada fase |
| El módulo Proyectos | Aporta qué proyectos hay conectados |

## 7. Criterios de aceptación de la épica

- Una deuda vencida se avisa.
- **Cada aviso dice qué lo disparó y dónde mirar.**
- **Un aviso atendido no vuelve a aparecer.**
- Se ve el avance de cada proyecto con la misma medida.
- Se ve la deuda declarada y la vencida, separadas.
- **Un proyecto sin datos aparece así, no en cero.**

## 8. Métricas de éxito

| Qué se mide | Meta |
|---|---|
| Avisos que no dicen qué los disparó | **Cero** |
| Avisos atendidos que vuelven | **Cero** |
| Columnas del reporte sin definición al lado | **Cero** |

## 9. Historias de usuario

| HU | Título | Funcionalidad | Estado |
|---|---|---|---|
| [HU-001](HU-001-avisar-lo-que-se-desvia/HU-001-avisar-lo-que-se-desvia.md) | Avisar lo que se desvía | `F-029` | **Terminada el 2026-09-01** |
| [HU-002](HU-002-reportar-como-va-cada-proyecto/HU-002-reportar-como-va-cada-proyecto.md) | Reportar cómo va cada proyecto | `F-030` | **Terminada el 2026-09-01** |

## 10. Consideraciones técnicas

**Módulo nuevo:** Avisos, con [especificación](../../avisos/spec.md) aprobada el 2026-09-01.

**Sin entidad en la base.** Todo aviso se calcula al pedirlo, leyendo lo que ya está escrito; y lo que el usuario decide callar se escribe en su proyecto, en `.agente/avisos-atendidos.md`. Callar en la base, sin rastro en el repositorio, sería el aviso que nadie sabe que existió.

**Hubo que definir «vencida», porque el estándar nunca le puso fecha a una deuda.** Acá quiere decir *sin moverse hace más de 30 días*, que es lo único que el texto sabe: la última vez que alguien tocó el `estado-fase.md`. Sale escrito en el reporte, para que nadie lo lea como un vencimiento acordado.

## 11. Dependencias

Depende de `EP-019` —de ahí sale en qué estación va cada fase— y de `EP-008`, que dice qué proyectos hay.

## 12. Riesgos

| Riesgo | Qué se hace |
|---|---|
| **Que demasiados avisos se vuelvan ruido** | Tres clases, no quince; y un aviso que no puede decir qué lo disparó no se emite |
| Que un aviso atendido vuelva | Se calla por su causa, o a mano dejando escrito el porqué |
| **Que comparar proyectos engañe** | Cada columna sale con su definición debajo, siempre |
| Que un proyecto sin datos parezca el peor | Sale como «sin datos», y de últimas |

## 13. Supuestos y restricciones

**Supuestos:** que las fases y el inventario están escritos como el estándar pide.

**Restricciones:** el aviso señala, no arregla; nada se guarda en la base; lo callado deja rastro en el repositorio.

## 14. Hoja de ruta

Versión 5, después de `EP-019`.

## 15. Definition of Ready

- ☑ Las dos funcionalidades están en el inventario, con su ficha.
- ☑ `EP-019` cerrada: de ahí sale la estación de cada fase.
- ☑ El módulo Avisos, con [especificación](../../avisos/spec.md) aprobada.

## 16. Definition of Done

- ☑ Las dos historias cerradas, con veredicto por criterio.
- ☑ Comprobado que todo aviso dice qué lo disparó y dónde mirar.
- ☑ Comprobado que lo atendido no vuelve.
- ☑ Comprobado que sin datos no es cero.

## 17. Bitácora de cambios

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Terminada**: las dos historias construidas y probadas el mismo día. En su primera corrida contra datos reales encontró cinco carpetas vacías que ni git ni una búsqueda de texto veían |
| 2026-09-01 | Nace del inventario aprobado, para cubrir las dos funcionalidades de Avisos |
