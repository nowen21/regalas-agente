# Mapa de dependencias — «Proyecto»   ·   `[CAPA 3]`

> Artefacto **vivo** ([`13·DOC9`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md)): la fuente autoritativa de "cómo está armado esto hoy". **Se consulta al planificar** (antes de explorar el código) y **se actualiza al cerrar** cada unidad de trabajo, en el mismo commit. La capa 3 declara su ruta (ej. `.agente/mapa-dependencias.md` local, o versionado si el equipo lo comparte). Reemplaza los `«…»` y borra esta caja.
>
> **No es una foto de una fecha** — es un compromiso vivo. Si contradice al código real, el mapa envejeció: se corrige.

---

## Modelos / entidades

| Entidad | Tabla / almacenamiento | Campos clave | Relaciones | Quién la consume |
|---|---|---|---|---|
| `«Entidad»` | `«tabla»` | «campos relevantes / fillable» | «1:N con X · N:M con Y» | «servicios/vistas que la usan» |

## Servicios / lógica

| Servicio | Qué hace | De qué depende (modelos, otros servicios) | Quién lo llama |
|---|---|---|---|
| `«Servicio»` | «responsabilidad» | «…» | «…» |

## Rutas / endpoints

| Ruta | Destino (controlador/vista/servicio) | Control de acceso (auth + permiso) | Middleware |
|---|---|---|---|
| `«VERBO /...»` | `«destino»` | `«permiso»` | «…» |

## Componentes / UI

| Componente | Qué consume (servicio/endpoint/datos) | Dónde se monta |
|---|---|---|
| `«Componente»` | «…» | «vista/layout» |

## Transversales

- **Permisos / roles:** «catálogo o fuente de verdad».
- **Middleware / interceptores globales:** «…».
- **Layouts / plantillas base compartidas:** «…».
- **Utilidades reutilizadas** (traits, helpers, mixins): «…».

## Pruebas

| Suite | Qué cubre | Depende de |
|---|---|---|
| `«suite»` | «módulo/flujo» | «entidades/servicios» |
