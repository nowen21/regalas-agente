# Planteamiento — «Nombre del módulo / épica»   ·   `[CAPA 3]`

> **Qué es este archivo.** El **planteamiento de entrada** de un desarrollo: la necesidad y sus restricciones (pasos 0–3 del flujo [`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)). Es el **insumo** del agente, no la especificación ni una orden de entregar código.
>
> **Cómo usarlo.**
> 1. Copiar esta plantilla al proyecto como `prompts/<slug>-planteamiento.md` (un planteamiento por módulo/épica).
> 2. Reemplazar los `«…»` y borrar las secciones que no apliquen.
> 3. Borrar este recuadro.
>
> **Regla de oro.** El planteamiento responde **QUÉ se necesita y QUÉ no se negocia**. El **CÓMO y el CUÁNDO** (alcance, HU, especificación, plan, orden, entrega) los pone el estándar. En cuanto un planteamiento dice "dame el código de X", dejó de ser planteamiento y choca con el flujo ([`02·F2`](../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md) sin especificación no hay código · [`02·F4`](../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) sin plan aprobado no hay código).

**Encuadre para el agente:** este documento es el planteamiento de entrada. El agente sigue el flujo del estándar — análisis ([`02·F1`](../base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md)) → alcance (`proponer-alcance`) → épica/HU ([`13·DOC15`](../base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md)) → especificación ([`02·F2`](../base/02-flujo-de-trabajo/reglas/F2-sin-spec-acordada-no-hay-codigo.md)) → plan aprobado ([`02·F4`](../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) → implementación. **No generar código hasta que el plan esté aprobado.**

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Nombre del proyecto** | «Cómo se llama el proyecto. Es el nombre con que lo van a nombrar todos los documentos que salgan de acá, así que se decide una vez y no se cambia sin plan» |
| **Qué cubre este encargo** | «Todo el proyecto, o el módulo o la épica a la que corresponde» |
| **Fecha** | «AAAA-MM-DD» |

## 1. Necesidad — en una frase

«Qué quiere resolver el negocio, en lenguaje de negocio, sin detalle técnico.»

## 2. Contexto

«Situación actual, problema que se resuelve, quién lo usa hoy, antecedentes.»

> Si el punto de partida (un solo usuario, corre en local, etc.) **no** es un límite del diseño, decláralo: "esto es el punto de partida, no un tope — no recortar estructura apoyándose en ello".

## 3. Objetivo y criterio de éxito

- **Objetivo:** «qué se logra cuando esto esté hecho».
- **Criterio de éxito:** «cómo se sabe, de forma medible, que se logró».

## 4. Alcance esperado (acota expectativas)

- **Qué SÍ se pide:** «capacidades que entran».
- **Qué NO se pide / fuera de alcance:** «lo que explícitamente queda afuera».

> El alcance **formal** se acuerda en la estación `proponer-alcance`. Esto es solo el borde inicial para que el agente no asuma de más.

## 5. Restricciones técnicas (si el proyecto las fija)

«Stack obligatorio, motor de BD, versiones, integraciones. Para los datos ya verificados del entorno (versiones, puertos, rutas), remitir a `.agente/stack.md` — no repetirlos aquí para no tener dos versiones que se contradigan.»

## 6. Requerimientos funcionales

Numerados. Uno por capacidad. Marcar el central si hay uno.

1. «Requerimiento…»
2. «Requerimiento…  ← REQUISITO CENTRAL» (si aplica)

## 7. Restricciones no negociables

Reglas duras que el diseño debe cumplir sí o sí (seguridad, privacidad, decisiones de arquitectura ya tomadas).

- «Restricción…»

## 8. Casos borde a considerar

Lo que el agente debe contemplar aunque no sea el camino feliz.

- «Encoding raro, archivos enormes, permisos, concurrencia, entradas inválidas…»

## 9. Referencias

- «Mockups, documentos funcionales, prompts previos, especificaciones de módulos con los que convive.»

## 10. Épicas derivadas

> Trazabilidad hacia abajo: se completa **a medida** que el planteamiento se descompone en épicas ([`02·F0`](../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) paso 4). Normalmente **1**; un planteamiento grande puede dar varias. Cada épica apunta de vuelta a este planteamiento (`epica.md §1`).

| Épica | Título | Estado |
|---|---|---|
| EP-«NNN» | «…» | Propuesta / Aprobada / En curso / Completada |

---

> **No incluir en un planteamiento** (lo pone el estándar, no tú): sección "Formato de respuesta" que pida código completo · "Actúa como desarrollador senior…" (la identidad ya está en `00`) · el orden de implementación · la entrega esperada. Si aparece algo de eso, es señal de que el planteamiento se convirtió en orden y va a chocar con el flujo.
