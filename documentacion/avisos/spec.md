# Especificación del módulo Avisos  ·  `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Módulo** | Avisos |
| **Funcionalidades que cubre** | [`F-029`](../../cvds/analisis-requisitos/inventario-funcionalidades.md) avisar lo que se desvía · [`F-030`](../../cvds/analisis-requisitos/inventario-funcionalidades.md) reportar cómo va cada proyecto |
| **Épica** | [EP-020](../epicas/EP-020-lo-que-se-desvia-se-avisa/epica.md) |
| **Estado** | Aprobada el 2026-09-01 |
| **Versión del estándar** | 37.2.1 |

---

## 1. Propósito y alcance

**Que enterarse no dependa de ir a mirar**, y que comparar proyectos no engañe.

**Entra:** los avisos de lo que se desvió, callar uno a propósito, y el reporte de cómo va cada proyecto.

**No entra:** arreglar lo que se avisa, y mandarlo por correo.

---

## 2. Contexto — qué hay hoy

Todo lo que hace falta ya está escrito: las fases dicen cuándo se tocaron, las historias dicen si tienen fase, el inventario dice qué se construyó sin verificar. **Son más de doscientos archivos**, y por eso nadie los lee.

Medido acá el 2026-09-01: **3 historias sin ninguna fase** y **28 funcionalidades construidas sin verificar**.

---

## 3. Supuestos, dependencias y preguntas abiertas

| # | Qué | Tipo |
|---|---|---|
| 1 | Las fases traen su `estado-fase.md` con la última actualización | Supuesto |
| 2 | El inventario trae la columna de verificado | Supuesto |
| 3 | **El estándar nunca le puso fecha a una deuda** | **Restricción declarada**, y por eso «vencida» se define acá |
| 4 | Cuántos días son «vencida» depende del proyecto | Se puede cambiar al pedirlo; el número de fábrica son 30 |

---

## 4. Reglas de negocio

| ID | Regla |
|---|---|
| `RN-1` | **Todo aviso dice qué lo disparó y dónde mirar.** El que no puede decirlo no se emite |
| `RN-2` | Los avisos salen de lo que más duele a lo que menos |
| `RN-3` | Un aviso atendido no vuelve: porque su causa desapareció, o porque se calló dejando escrito el porqué |
| `RN-4` | **Cuando la lista se recorta, se dice** |
| `RN-5` | El reporte lleva encima la definición de cada columna |
| `RN-6` | **Un proyecto sin datos aparece así, no en cero** |

---

## 5. Modelo de datos

**Ninguna entidad.** Todo se calcula al pedirlo: `DA-01`.

| Elemento | Dónde |
|---|---|
| Lo que dispara un aviso | Las fases, las historias y el inventario del proyecto |
| Lo callado a propósito | `.agente/avisos-atendidos.md`, en el proyecto |

### 5.1 Por qué lo callado también es texto

Porque callar un aviso es una decisión, y una decisión que solo vive en la base de la plataforma **no viaja con el repositorio**. Quien clone el proyecto vería otra vez el aviso que ya se había resuelto no atender, sin saber que alguien lo pensó.

---

## 6. Comportamiento y flujos

### 6.1 Las tres clases de aviso

| Clase | Qué la dispara | Por qué duele |
|---|---|---|
| **Fase detenida** | Una fase sin cerrar que lleva más de 30 días sin tocarse | Es trabajo empezado que nadie retoma |
| **Historia sin fase** | Una HU escrita sin ninguna carpeta de fase | Se pidió algo y no se construyó |
| **Terminado sin comprobar** | Una funcionalidad construida que sigue sin verificarse | Se dice que está hecho y nadie lo comprobó |

**Son tres y no quince**, y eso es la decisión: *demasiados avisos se vuelven ruido, y el ruido se ignora completo*.

### 6.2 Lo que no se cuenta

**Una fase que no dice desde cuándo lleva quieta no se da por vencida.** No se sabe, y no saber tiene su propio nombre: sale en el reporte, en su columna, aparte de la deuda.

---

## 7. Interfaz

Órdenes de consola. **Sin pantalla todavía**, como el resto de los módulos de esta etapa.

---

## 8. Permisos y autorización

La misma confianza del resto: quien corre la orden es el usuario en su máquina.

---

## 9. Marco normativo

`03·DA-01` (el texto es la verdad) · el capítulo `06` por el tiempo de respuesta · las señales [`S-107`](../senales.md), [`S-110`](../senales.md) y [`S-113`](../senales.md), que son las tres formas en que un aviso engaña.

---

## 10. Plan de pruebas

| Qué | Cuántas |
|---|---|
| Las tres clases, con qué las disparó y dónde mirar | 5 |
| Lo atendido no vuelve | 3 |
| El ruido se controla | 5 |
| El reporte dice qué mide | 3 |
| Sin datos no es cero | 4 |
| **Total** | **20** |

---

## 11. Criterios de aceptación

| ID | Criterio | Estado |
|---|---|---|
| CA-01 | Una deuda vencida se avisa | ☑ |
| CA-02 | Cada aviso dice qué lo disparó y dónde mirar | ☑ |
| CA-03 | Un aviso atendido no vuelve a aparecer | ☑ |
| CA-04 | Se ve el avance de cada proyecto con la misma medida | ☑ |
| CA-05 | Se ve la deuda declarada y la vencida | ☑ |
| CA-06 | Un proyecto sin datos aparece así, no en cero | ☑ |

---

## 12. Decisiones tomadas

| Decisión | Por qué |
|---|---|
| **Tres clases de aviso, no quince** | El ruido se ignora completo, y entonces también lo que importaba |
| **Un aviso que no puede decir qué lo disparó no se emite** | Un aviso sin causa obliga a buscarla, y nadie busca |
| **«Vencida» son 30 días sin moverse** | El estándar nunca le puso fecha a una deuda. Se declara en el reporte |
| **Lo callado se escribe en el proyecto** | Una decisión que no viaja con el repositorio se pierde al clonarlo |
| **Sin datos no es cero** | Cero dice «va mal»; sin datos dice «no se sabe» — `S-107` |
| **Cada columna sale con su definición** | Comparar con la misma medida engaña si no se dice qué mide |
| **Si recorta, lo dice** | Un tope callado se lee como «eso es todo lo que hay» — `S-113` |

---

## 13. Trazabilidad

| Funcionalidad | Historia | Fase que lo construye |
|---|---|---|
| `F-029` | [HU-001 Avisar lo que se desvía](../epicas/EP-020-lo-que-se-desvia-se-avisa/HU-001-avisar-lo-que-se-desvia/HU-001-avisar-lo-que-se-desvia.md) | [W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo](../epicas/EP-020-lo-que-se-desvia-se-avisa/HU-001-avisar-lo-que-se-desvia/W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo/estado-fase.md), cerrada el 2026-09-01 |
| `F-030` | [HU-002 Reportar cómo va cada proyecto](../epicas/EP-020-lo-que-se-desvia-se-avisa/HU-002-reportar-como-va-cada-proyecto/HU-002-reportar-como-va-cada-proyecto.md) | [X-EP-020-HU-002-sin-datos-no-es-cero](../epicas/EP-020-lo-que-se-desvia-se-avisa/HU-002-reportar-como-va-cada-proyecto/X-EP-020-HU-002-sin-datos-no-es-cero/estado-fase.md), cerrada el 2026-09-01 |

---

## 14. Cruces con otros módulos

| Módulo | Cómo se cruzan |
|---|---|
| [Ciclo de vida](../ciclo-de-vida/spec.md) | De ahí sale en qué estación va cada fase y desde cuándo |
| [Proyectos](../proyectos/spec.md) | Dice qué proyectos hay conectados y dónde viven |
| [Comprobaciones](../comprobaciones/spec.md) | El aviso de «terminado sin comprobar» señala justo lo que ese módulo verifica |

---

## 15. Cambios después de aprobada

Ninguno todavía.
