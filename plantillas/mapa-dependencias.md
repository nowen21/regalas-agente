# Mapa de dependencias · «Proyecto»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Artefacto vivo ([`13·DOC9`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)): la fuente autoritativa de cómo está armado el proyecto hoy. Se consulta al planificar, antes de explorar el código, y se actualiza al cerrar cada unidad de trabajo, en el mismo commit. La capa 3 declara su ruta (por ejemplo `.agente/mapa-dependencias.md` local, o versionado si el equipo lo comparte). Al llenarlo se reemplazan los `«…»` y se borran esta caja y las notas como ella.
>
> Si el mapa contradice al código real, envejeció, y se corrige.

## Modelos / entidades

> Son las entidades que guardan datos, para saber qué se rompe al cambiar una tabla.

| Entidad | Tabla / almacenamiento | Campos clave | Relaciones | Quién la consume |
|---|---|---|---|---|
| `«Entidad»` | `«tabla»` | «campos relevantes / fillable» | «1:N con X · N:M con Y» | «servicios/vistas que la usan» |

## Servicios / lógica

> Son las piezas que llevan la lógica del negocio, para saber a quién afecta cambiar una.

| Servicio | Qué hace | De qué depende (modelos, otros servicios) | Quién lo llama |
|---|---|---|---|
| `«Servicio»` | «responsabilidad» | «…» | «…» |

## Rutas / endpoints

> Son las rutas que expone el sistema y quién puede usarlas. Si no expone ninguna, se escribe «No aplica» con su motivo.

| Ruta | Destino (controlador/vista/servicio) | Control de acceso (auth + permiso) | Middleware |
|---|---|---|---|
| `«VERBO /...»` | `«destino»` | `«permiso»` | «…» |

## Componentes / UI

> Son las piezas de pantalla y de dónde sacan sus datos. Si el sistema no tiene interfaz, se escribe «No aplica» con su motivo.

| Componente | Qué consume (servicio/endpoint/datos) | Dónde se monta |
|---|---|---|
| `«Componente»` | «…» | «vista/layout» |

## Transversales

> Es lo que usan todos los módulos a la vez, y que por eso rompe en muchos sitios si cambia.

- Permisos / roles: «catálogo o fuente de verdad».
- Middleware / interceptores globales: «…».
- Layouts / plantillas base compartidas: «…».
- Utilidades reutilizadas (traits, helpers, mixins): «…».

## Pruebas

> Son las suites de prueba y de qué dependen, para saber cuáles correr cuando algo cambia.

| Suite | Qué cubre | Depende de |
|---|---|---|
| `«suite»` | «módulo/flujo» | «entidades/servicios» |
