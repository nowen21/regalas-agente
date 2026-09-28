# Postmortem · «título del incidente»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

Se escribe tras un incidente relevante ([`19·OB5`](«RUTA-ESTANDAR»/base/19-observabilidad-y-operacion.md#ob5--postmortem-sin-culpa)). **Sin culpa:** el foco es el sistema y el proceso, no la persona. El objetivo es que no vuelva a pasar, no señalar a nadie.

- **Fecha del incidente:** «…»
- **Detectado por:** «alerta / usuario / otro»
- **Duración:** «…»
- **Severidad:** «alta / media / baja»

## Qué pasó

> Cuenta el incidente de principio a fin, sin causas ni culpables.

«Resumen en 2-3 líneas, entendible por alguien que no estuvo.»

## Impacto

> Mide el daño que dejó el incidente.

«A quién y a qué afectó: usuarios, datos, dinero, reputación. Con números si se puede.»

## Línea de tiempo

> Ordena por hora lo que pasó, desde que empezó hasta que se resolvió.

| Hora | Evento |
|---|---|
| «hh:mm» | «empezó / se detectó / acción / se resolvió» |

## Causa raíz

> Es lo que hizo posible el incidente, buscado en el sistema y en el proceso.

«Por qué pasó de verdad: no «fallo humano», sino qué del sistema o del proceso lo permitió (los "5 por qué" ayudan). Incluir la causa que dejó que llegara a producción.»

## Qué contuvo el daño / qué lo agravó

> Separa lo que ayudó de lo que estorbó durante la respuesta. Si algo no aplica, se escribe «Nada».

«Qué ayudó a detectarlo o limitarlo, y qué lo hizo peor o más lento de resolver.»

## Acciones para que no vuelva

> Son los cambios que salen del incidente, cada uno con su tipo, su responsable y su estado. La lección se registra además como señal ([`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), tipo `error-resuelto` / `aprendizaje`) y las acciones se abren como deuda (`deuda-tecnica`), para que la memoria y el backlog las tengan.

| Acción | Tipo (prevención / detección / mitigación) | Responsable | Estado |
|---|---|---|---|
| «…» | «…» | «…» | «abierta» |
