# Catálogo de módulos · «Proyecto»   ·   `[CAPA 3]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Índice **vivo** de alto nivel ([`13·DOC13`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)): qué módulos tiene el proyecto y qué hace cada uno. Se consulta al inicio de cada unidad de trabajo ([`02·F1`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md)), y cada módulo nuevo se registra antes de cerrar la unidad que lo crea, sin preguntar. El detalle técnico interno va en el mapa de dependencias ([`13·DOC9`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)), no aquí. La capa 3 declara su ruta (por ejemplo `documentacion/modulos.md` o `.agente/dominio.md`). Reemplaza los `«…»` y borra esta caja.

---

| Módulo | Prefijo de rutas / namespace | Descripción (1-2 líneas) | Estado | Especificación | Entidades principales |
|---|---|---|---|---|---|
| `«módulo»` | `«/prefijo»` | «qué hace y a quién sirve» | activo / en desarrollo / scaffold / deprecado | «enlace al especificación» | `«Entidad1, Entidad2»` |

Cuenta como módulo nuevo, y se registra aquí, lo que tiene prefijo de rutas propio o es un dominio funcional autónomo con permisos propios, y el submódulo con semántica y especificación separadas.

No cuenta una fase de un módulo existente, un fix o refactor interno, ni un componente hijo reutilizable dentro de un módulo ya registrado.
