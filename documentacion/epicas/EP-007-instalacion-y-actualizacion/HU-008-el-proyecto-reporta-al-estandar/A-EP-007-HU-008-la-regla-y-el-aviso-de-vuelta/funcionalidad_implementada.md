# Funcionalidad implementada — Fase A-EP-007-HU-008

| Campo | Valor |
|---|---|
| **Cierra** | El [pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md](../../../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md) |
| **Fecha de cierre** | 2026-08-18 |
| **Veredicto** | **Cumple** — [resultado_pruebas.md](resultado_pruebas.md) §4 |
| **Versión** | 23.7.0 (**MENOR**) |

## Qué hay ahora que antes no había

### 1 · La regla

**[`02·F24` · El defecto del estándar se reporta, no se corrige](../../../../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md)**, con su checklist en **CUMPLE**.

Un proyecto que encuentra un defecto del estándar no lo toca: abre un pendiente allá **nombrando el proyecto de origen**, otro acá diciendo que espera esa corrección, y sigue con lo suyo. El de acá queda abierto hasta que llegue el aviso.

**Va al capítulo `02` y no a la épica de instalación.** Lo que gobierna es un paso del flujo —qué hace el agente cuando lo que hay que arreglar no es suyo—; la instalación es por dónde viaja el aviso, no de qué trata la regla.

**Y resuelve un choque que estaba abierto:** [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) manda parar y proponer lo que se descubre fuera del criterio de aceptación, y no decía qué hacer cuando lo descubierto es del estándar. Era el hueco anotado en el punto 8 del [pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).

### 2 · Las dos plantillas

[plantillas/pendiente-reportado.md](../../../../../plantillas/pendiente-reportado.md) y [plantillas/pendiente-de-seguimiento.md](../../../../../plantillas/pendiente-de-seguimiento.md), **cada una nombrando a la otra**, porque uno sin el otro es la mitad que ya falló: el 2026-08-15 se anotó solo acá y el estándar no se enteró en un día; el 16 se anotó solo allá y se cerró el del proyecto, perdiendo el seguimiento en el acto de traspasarlo.

### 3 · El aviso de vuelta — la mitad que nadie tenía

`cerrar.py` escribe el aviso en el repositorio de cada proyecto al que le toca, leyendo de la ficha del pendiente a quién avisar y de [plantillas/proyectos.md](../../../../../plantillas/proyectos.md) dónde vive.

**Escribe un archivo de pendiente y nada más. Nunca toca código**, y hay una prueba que compara la raíz del proyecto antes y después. Es idempotente: cerrar dos veces no duplica.

### 4 · La comprobación

`validar.py pendientes` reporta el pendiente que dice venir de un proyecto sin nombrar cuál — casilla vacía o con el marcador sin llenar. **Los 34 del backlog pasan sin tocar ninguno**, que es la señal de que la regla describe lo que ya se hacía bien.

## Lo que se supo

**El paso 6 hecho a mano se olvida, y hay tres pruebas.** Los cierres de los enlaces de las plantillas, del renombre del resumen y del registro de versión quedaron sin aviso. Dos los espera `shopnest-mesa` y uno `dp`, y ninguno lo sabe.

**No se mandan hacia atrás:** inventar hoy un aviso sobre una corrección de hace dos días es escribir una fecha falsa. Se anota cuáles son y quién los espera.

## Lo que queda abierto

**Que el proyecto compruebe el aviso no lo hace nadie.** El aviso llega solo; abrirlo, verificar y cerrar el pendiente de seguimiento sigue dependiendo de que alguien lo lea. Es el riesgo `B-03` del plan, y la mitad de `F24` que ningún programa de acá puede ver — el pendiente del otro lado vive en otro repositorio.

**Y falta avisarles.** Al cerrar este pendiente hay que avisarle a **todos los proyectos instalados**, no solo a `shopnest-mesa`: la regla los rige a todos.
