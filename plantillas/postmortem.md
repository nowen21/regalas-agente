# Postmortem — «título del incidente»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

Se escribe tras un incidente relevante ([`19·OB5`](«RUTA-ESTANDAR»/base/19-observabilidad-y-operacion.md#ob5--postmortem-sin-culpa)). **Sin culpa:** el foco es el sistema y el proceso, no la persona. El objetivo es que **no vuelva a pasar**, no señalar a nadie.

- **Fecha del incidente:** «…» · **detectado por:** «alerta / usuario / …» · **duración:** «…»
- **Severidad:** «alta / media / baja»

## Qué pasó

«Resumen en 2-3 líneas, entendible por alguien que no estuvo.»

## Impacto

«A quién y a qué afectó: usuarios, datos, dinero, reputación. Con números si se puede.»

## Línea de tiempo

| Hora | Evento |
|---|---|
| «hh:mm» | «empezó / se detectó / acción / se resolvió» |

## Causa raíz

«Por qué pasó de verdad — no "fallo humano", sino qué del sistema o del proceso lo permitió (los "5 por qué" ayudan). Incluir la causa que dejó que llegara a producción.»

## Qué contuvo el daño / qué lo agravó

«Qué ayudó a detectarlo o limitarlo, y qué lo hizo peor o más lento de resolver.»

## Acciones para que no vuelva

| Acción | Tipo (prevención / detección / mitigación) | Responsable | Estado |
|---|---|---|---|
| «…» | «…» | «…» | «abierta» |

> Registrar la lección como señal ([`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md), tipo `error-resuelto` / `aprendizaje`) y abrir las acciones como deuda (`deuda-tecnica`) para que la memoria y el backlog las tengan.
