# Despliegue: ¿qué se entregó, y cómo se instala?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo se pone a andar el sistema donde se usa, cómo se vuelve atrás si falla, y qué se entregó con qué evidencia. La prueba de que está bien escrito es que alguien que no estuvo en el desarrollo pueda instalarlo siguiendo el texto.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> Plantilla. Se llena antes del primer despliegue y se actualiza en cada entrega. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra.
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta.

> Lo que va dentro de cada `«…»` se redacta en el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza. Si en una celda va más de una cosa, se escribe como lista: una por renglón, con `<br>` entre ellas y viñeta al empezar. Separarlas con puntos medios en un solo párrafo las vuelve ilegibles.

> El documento se escribe desde la propuesta, no desde lo que ya está construido. Lo que existe sirve para saber qué se conserva y qué se rehace, nunca para fijar el alcance. La prueba: si se borra mentalmente lo construido y el documento sigue siendo cierto, está bien escrito.

**Estado: «BORRADOR / EN CURSO / ENTREGADO»** («AAAA-MM-DD»).

## 1. Qué entra a esta etapa

> Es lo que la etapa recibe de pruebas: lo construido con su veredicto, la aceptación del usuario y los defectos abiertos.

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Lo construido, con su veredicto por criterio | Pruebas | «…» |
| La aceptación del usuario | Pruebas | «…» |
| Los defectos abiertos y cuáles bloquean | Pruebas | «…» |

## 2. Cuándo, quién y con qué aviso

> Fija el momento del despliegue, quién lo hace y a quién se avisa antes.

| Qué se define | Cómo queda |
|---|---|
| Fecha y hora del despliegue | «Y por qué esa: cuándo hay menos gente usando» |
| Cuánto tiempo estará fuera de servicio | «…» |
| Quién ejecuta, quién autoriza y quién acompaña | «…» |
| A quién se avisa, y con cuánta anticipación | «…» |
| Hasta qué hora se puede cancelar sin costo | «…» |

## 3. Dónde corre, y cómo se llega

> Lista los ambientes donde corre el sistema y dice cómo entra la versión nueva en producción.

| Ambiente | Para qué sirve | Quién puede desplegar ahí | En qué se diferencia de producción |
|---|---|---|---|
| «…» | «…» | «…» | «…» |

**Cómo se entra en producción:** «De un golpe, por grupos de usuarios, en paralelo con el sistema viejo, o dejando la versión nueva al lado y cambiando el interruptor. Cuál, y por qué esa.»

## 4. La instalación desde cero

> Resume los pasos para instalar el sistema desde cero, escritos para quien no estuvo en el desarrollo: cada uno literal y verificable, con lo que se debe ver cuando sale bien. El detalle vive en el manual de instalación; acá queda el resumen y quién lo probó.

| # | Paso | Cómo se sabe que salió bien |
|---|---|---|
| 1 | «…» | «…» |

**Probada desde cero por «quién», el «AAAA-MM-DD», en «dónde».**

## 5. Lo que se comprueba antes de tocar producción

> Es la lista que se recorre entera y se marca antes de desplegar. Lo que no se marcó no se hizo. Sirve sobre todo el día en que todo esté apurado, que es cuando se olvida lo importante.

| # | Qué se comprueba | ¿Listo? |
|---|---|---|
| 1 | Respaldo hecho, y restaurado en otro lado para saber que sirve | «…» |
| 2 | La vuelta atrás está escrita y probada | «…» |
| 3 | Las credenciales del ambiente están puestas, y no en el código | «…» |
| 4 | Los defectos que bloquean están cerrados | «…» |
| 5 | Hay quien responda durante el despliegue | «…» |

## 6. Los datos

> Dice cómo se respaldan y se migran los datos que ya existen, y qué pasa si la migración falla.

| Qué se define | Cómo queda |
|---|---|
| Respaldo antes de tocar nada | «Qué se respalda, dónde y quién comprueba que sirve» |
| Migración | «Qué cambia en los datos que ya existen, y cómo se comprueba» |
| Cómo se ensaya la migración antes | «Con una copia de los datos reales, y midiendo cuánto demora» |
| Qué pasa si falla a mitad | «…» |

## 7. Cómo se vuelve atrás

> Dice cómo se revierte cada falla posible, cuánto demora, qué se pierde y quién decide. La vuelta atrás se escribe y se prueba antes del despliegue, no cuando hace falta.

| Si falla | Cómo se revierte | Cuánto demora | Qué se pierde | Quién decide revertir |
|---|---|---|---|---|
| «…» | «…» | «…» | «…» | «…» |

## 8. Lo que se comprueba apenas queda arriba

> Confirma que lo ya probado también funciona en producción, con sus datos y sus credenciales. No repite las pruebas.

| Qué se comprueba | Quién | En cuánto tiempo |
|---|---|---|
| «Entra un usuario real» | «…» | «…» |
| «La operación más usada termina bien» | «…» | «…» |
| «Los avisos de error llegan a donde deben» | «…» | «…» |

## 9. Qué se le dice a quien usa, y qué se le enseña

> Dice qué se le comunica a quien usa el sistema, cuándo, dónde queda escrito y cómo se le capacita.

| Qué se comunica | A quién | Cuándo | Dónde queda |
|---|---|---|---|
| Qué trae esta versión, en su idioma | «…» | «…» | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) |
| Qué deja de funcionar, si algo deja | «…» | «Antes, nunca después» | «…» |
| Capacitación: quién la recibe y con qué material | «…» | «…» | «…» |
| A quién reclamar si algo sale mal | «…» | «…» | «…» |

## 10. El acompañamiento de los primeros días

> Define el soporte reforzado de los primeros días después del despliegue y cuándo termina.

| Qué se define | Cómo queda |
|---|---|
| Cuánto dura el acompañamiento reforzado | «…» |
| Quién atiende, y en qué horario | «…» |
| Qué se mira de cerca esos días | «…» |
| Cuándo se considera estable y pasa a operación normal | «…» |

## 11. La entrega a quien lo va a operar

> Lista lo que recibe quien va a operar el sistema y si ya lo recibió.

| Qué se entrega | A quién | ¿Recibido? |
|---|---|---|
| Manual técnico y de operación | «Quien opera» | «…» |
| Accesos y credenciales, por el canal seguro | «…» | «…» |
| Qué vigilar y qué hacer cuando falla | «…» | «…» |
| Defectos conocidos y deuda declarada | «…» | «…» |

## 12. Los entregables de esta etapa, y a quién van

> Lista los documentos que produce la etapa, el molde de cada uno, a quién van y en qué estado están.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual de instalación | [plantillas/ciclo-vida-proyectos/17-manual-de-instalacion.md](../../ciclo-vida-proyectos/17-manual-de-instalacion.md) | Quien instala | «…» |
| Notas de versión | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) | Quien usa | «…» |
| Acta de entrega y aceptación | [plantillas/ciclo-vida-proyectos/20-acta-de-entrega.md](../../ciclo-vida-proyectos/20-acta-de-entrega.md) | Cliente, se firma | «…» |
| Manual técnico y de operación | [plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md](../../ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md) | Quien opera | «…» |
| Lista de comprobación del despliegue | [plantillas/checklist-despliegue.md](../../checklist-despliegue.md) | Quien despliega | «…» |
| Plan de vuelta atrás | Sección 7 de este documento | Quien despliega y quien opera | «…» |

## 13. Las puertas de esta etapa

> Son las condiciones que deben cumplirse antes de desplegar y antes de dar por entregado, cada una con la regla o la sección que la exige.

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Desplegar | el respaldo esté hecho y comprobado | Sección 5 de este documento |
| Desplegar | la vuelta atrás esté escrita y probada | Sección 7 de este documento |
| Desplegar | la lista de la sección 5 esté marcada entera | «…» |
| Dar por entregado | el acta esté firmada con su evidencia | «…» |
| Dar por entregado | quien opera haya recibido lo de la sección 11 | «…» |

## 14. La decisión de cierre

> Registra el veredicto de la entrega, quién lo dio y cuándo.

**«Se entrega / No se entrega»**, decidido por «quién» el «AAAA-MM-DD».

«Qué se entregó, qué quedó fuera de esta entrega, y qué queda pendiente para la siguiente.»
