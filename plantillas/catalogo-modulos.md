# Catálogo de módulos — «Proyecto»   ·   `[CAPA 3]`

> Índice **vivo** de alto nivel ([`13·DOC13`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)): **qué módulos tiene el proyecto y qué hace cada uno**. Se consulta al inicio de cada unidad de trabajo ([`02·F1`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md)) y **cada módulo nuevo se registra antes de cerrar** la unidad que lo crea (obligatorio, no se pregunta). Distinto del mapa de dependencias ([`13·DOC9`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md), detalle técnico interno). La capa 3 declara su ruta (ej. `documentacion/modulos.md` o `.agente/dominio.md`). Reemplaza los `«…»` y borra esta caja.

---

| Módulo | Prefijo de rutas / namespace | Descripción (1–2 líneas) | Estado | Especificación | Entidades principales |
|---|---|---|---|---|---|
| `«módulo»` | `«/prefijo»` | «qué hace y a quién sirve» | activo / en desarrollo / scaffold / deprecado | «enlace al especificación» | `«Entidad1, Entidad2»` |

---

**Qué cuenta como módulo nuevo** (se registra aquí): prefijo de rutas propio o dominio funcional autónomo con permisos propios · submódulo con semántica y especificación separados.

**Qué NO cuenta:** una fase de un módulo existente · un fix o refactor interno · un componente hijo reutilizable dentro de un módulo ya registrado.
