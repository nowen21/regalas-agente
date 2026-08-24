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
| La aceptación del usuario | Pruebas | «…» |
| Los defectos abiertos y cuáles bloquean | Pruebas | «…» |

## 2. Cuándo, quién y con qué aviso

| Qué se define | Cómo queda |
|---|---|
| Fecha y hora del despliegue | «Y por qué esa: cuándo hay menos gente usando» |
| Cuánto tiempo estará fuera de servicio | «…» |
| Quién ejecuta, quién autoriza y quién acompaña | «…» |
| A quién se avisa, y con cuánta anticipación | «…» |
| Hasta qué hora se puede cancelar sin costo | «…» |

## 3. Dónde corre, y cómo se llega

| Ambiente | Para qué sirve | Quién puede desplegar ahí | En qué se diferencia de producción |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

**Cómo se entra en producción:** «De un golpe, por grupos de usuarios, en paralelo con el sistema viejo, o dejando la versión nueva al lado y cambiando el interruptor. Cuál, y por qué esa.»

## 4. La instalación desde cero

> **Se escribe para quien no estuvo.** Cada paso, literal y verificable, con lo que se debe ver cuando sale bien. El detalle vive en el manual; acá queda el resumen y quién lo probó.

| # | Paso | Cómo se sabe que salió bien |
|---|---|---|
| 1 | «…» | «…» |

**Probada desde cero por «quién», el «AAAA-MM-DD», en «dónde».**

## 5. Lo que se comprueba antes de tocar producción

> La lista se recorre entera y se marca. Lo que no se marcó, no se hizo: **la lista es para el día en que todo esté apurado**, que es cuando se olvida lo importante.

| # | Qué se comprueba | ¿Listo? |
|---|---|---|
| 1 | Respaldo hecho, y restaurado en otro lado para saber que sirve | «…» |
| 2 | La vuelta atrás está escrita y probada | «…» |
| 3 | Las credenciales del ambiente están puestas, y no en el código | «…» |
| 4 | Los defectos que bloquean están cerrados | «…» |
| 5 | Hay quien responda durante el despliegue | «…» |

## 6. Los datos

| Qué se define | Cómo queda |
|---|---|
| Respaldo antes de tocar nada | «Qué se respalda, dónde y quién comprueba que sirve» |
| Migración | «Qué cambia en los datos que ya existen, y cómo se comprueba» |
| Cómo se ensaya la migración antes | «Con una copia de los datos reales, y midiendo cuánto demora» |
| Qué pasa si falla a mitad | «…» |

## 7. Cómo se vuelve atrás

> **Un despliegue sin vuelta atrás escrita no es un despliegue: es una apuesta.** Se prueba antes, no cuando hace falta.

| Si falla | Cómo se revierte | Cuánto demora | Qué se pierde | Quién decide revertir |
|---|---|---|---|---|
| «…» | «…» | «…» | «…» | «…» |

## 8. Lo que se comprueba apenas queda arriba

> No es repetir las pruebas: es confirmar que lo que ya se probó también funciona **ahí**, con los datos y las credenciales de producción.

| Qué se comprueba | Quién | En cuánto tiempo |
|---|---|---|
| «Entra un usuario real» | «…» | «…» |
| «La operación más usada termina bien» | «…» | «…» |
| «Los avisos de error llegan a donde deben» | «…» | «…» |

## 9. Qué se le dice a quien usa, y qué se le enseña

| Qué se comunica | A quién | Cuándo | Dónde queda |
|---|---|---|---|
| Qué trae esta versión, en su idioma | «…» | «…» | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) |
| Qué deja de funcionar, si algo deja | «…» | «Antes, nunca después» | «…» |
| Capacitación: quién la recibe y con qué material | «…» | «…» | «…» |
| A quién reclamar si algo sale mal | «…» | «…» | «…» |

## 10. El acompañamiento de los primeros días

| Qué se define | Cómo queda |
|---|---|
| Cuánto dura el acompañamiento reforzado | «…» |
| Quién atiende, y en qué horario | «…» |
| Qué se mira de cerca esos días | «…» |
| Cuándo se considera estable y pasa a operación normal | «…» |

## 11. La entrega a quien lo va a operar

| Qué se entrega | A quién | ¿Recibido? |
|---|---|---|
| Manual técnico y de operación | «Quien opera» | «…» |
| Accesos y credenciales, por el canal seguro | «…» | «…» |
| Qué vigilar y qué hacer cuando falla | «…» | «…» |
| Defectos conocidos y deuda declarada | «…» | «…» |

## 12. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual de instalación | [plantillas/ciclo-vida-proyectos/17-manual-de-instalacion.md](../../ciclo-vida-proyectos/17-manual-de-instalacion.md) | Quien instala | «…» |
| Notas de versión | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) | Quien usa | «…» |
| Acta de entrega y aceptación | [plantillas/ciclo-vida-proyectos/20-acta-de-entrega.md](../../ciclo-vida-proyectos/20-acta-de-entrega.md) | Cliente, se firma | «…» |
| Manual técnico y de operación | [plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md](../../ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md) | Quien opera | «…» |
| Lista de comprobación del despliegue | [plantillas/checklist-despliegue.md](../../checklist-despliegue.md) | Quien despliega | «…» |
| Plan de vuelta atrás | Sección 7 de este documento | Quien despliega y quien opera | «…» |

## 13. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Desplegar | el respaldo esté hecho y comprobado | Sección 5 de este documento |
| Desplegar | la vuelta atrás esté escrita y probada | Sección 7 de este documento |
| Desplegar | la lista de la sección 5 esté marcada entera | «…» |
| Dar por entregado | el acta esté firmada con su evidencia | «…» |
| Dar por entregado | quien opera haya recibido lo de la sección 11 | «…» |

## 14. La decisión de cierre

**«Se entrega / No se entrega»**, decidido por «quién» el «AAAA-MM-DD».

«Qué se entregó, qué quedó fuera de esta entrega, y qué queda pendiente para la siguiente.»
