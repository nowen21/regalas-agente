# Despliegue: ¿qué se entregó, y cómo se instala?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo se pone a andar el sistema donde se usa, cómo se vuelve atrás si falla, y qué se entregó con qué evidencia. La prueba de que está bien escrito es que **alguien que no estuvo en el desarrollo pueda instalarlo siguiendo el texto**.

> Plantilla. Se llena antes del primer despliegue y se actualiza en cada entrega. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / EN CURSO / ENTREGADO»** («AAAA-MM-DD»).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Lo construido, con su veredicto por criterio | Pruebas | «…» |
| Los defectos abiertos y cuáles bloquean | Pruebas | «…» |
| Los requisitos no funcionales que se comprueban en producción | Análisis | «…» |

## 2. Dónde corre, y cómo se llega

| Ambiente | Para qué sirve | Quién puede desplegar ahí | En qué se diferencia de producción |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 3. La instalación desde cero

> **Se escribe para quien no estuvo.** Cada paso, literal y verificable, con lo que se debe ver cuando sale bien. El detalle vive en el manual; acá queda el resumen y quién lo probó.

| # | Paso | Cómo se sabe que salió bien |
|---|---|---|
| 1 | «…» | «…» |

**Probada desde cero por «quién», el «AAAA-MM-DD», en «dónde».**

## 4. Los datos

| Qué se define | Cómo queda |
|---|---|
| Respaldo antes de tocar nada | «Qué se respalda, dónde y quién comprueba que sirve» |
| Migración | «Qué cambia en los datos que ya existen, y cómo se comprueba» |
| Qué pasa si la migración falla a mitad | «…» |

## 5. Cómo se vuelve atrás

> **Un despliegue sin vuelta atrás escrita no es un despliegue: es una apuesta.** Se prueba antes, no cuando hace falta.

| Si falla | Cómo se revierte | Cuánto demora | Qué se pierde |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

## 6. Qué se le dice a quien usa

| Qué se comunica | A quién | Cuándo | Dónde queda |
|---|---|---|---|
| Qué trae esta versión, en su idioma | «…» | «…» | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) |
| Qué deja de funcionar, si algo deja | «…» | «Antes, nunca después» | «…» |
| A quién reclamar si algo sale mal | «…» | «…» | «…» |

## 7. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual de instalación | [plantillas/ciclo-vida-proyectos/17-manual-de-instalacion.md](../../ciclo-vida-proyectos/17-manual-de-instalacion.md) | Quien instala | «…» |
| Notas de versión | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) | Quien usa | «…» |
| Acta de entrega y aceptación | [plantillas/ciclo-vida-proyectos/20-acta-de-entrega.md](../../ciclo-vida-proyectos/20-acta-de-entrega.md) | Cliente, se firma | «…» |
| Lista de comprobación del despliegue | [plantillas/checklist-despliegue.md](../../checklist-despliegue.md) | Quien despliega | «…» |

## 8. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Desplegar | el respaldo esté hecho y comprobado | «…» |
| Desplegar | la vuelta atrás esté escrita y probada | «…» |
| Dar por entregado | el acta esté firmada con su evidencia | «…» |

## 9. La decisión de cierre

**«Se entrega / No se entrega»**, decidido por «quién» el «AAAA-MM-DD».

«Qué se entregó, qué quedó fuera de esta entrega, y qué queda pendiente para la siguiente.»
