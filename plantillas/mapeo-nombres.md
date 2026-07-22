# Mapeo de nombres  ·  `[CAPA 3]`

> Plantilla. La base habla en abstracto ("catálogo", "auditoría", "permiso"). Aquí declaras **cómo se llama cada cosa en este proyecto**, para que el agente aplique la regla con el nombre real. Reemplaza los `«…»` y borra esta caja.

## Conceptos de la base → nombre concreto aquí

| Concepto en la base | En este proyecto | Ejemplo / ubicación |
|---|---|---|
| **Catálogo** (`03` · D4) — dónde viven valores configurables | «tabla / mecanismo» | «…» |
| **Bifurcar por código semántico** (`03` · D4) | «cómo se resuelve el código» | «…» |
| **Auditoría** — quién creó/editó (`03` · D1) | «trait / columnas / mecanismo» | «…» |
| **Prefijo de tablas nuevas** (`14` · EST2) | «prefijo o convención» | «…» |
| **Organización de módulos** (`14` · EST1) | «namespace / carpetas» | «…» |
| **Sistema de permisos** (`04` · S1) | «librería / convención `recurso.accion`» | «…» |
| **Estado de registro / borrado lógico** (`03` · D1) | «cómo se modela» | «…» |
| **Almacenamiento privado de archivos** (`04` · S6) | «disco / ruta / mecanismo» | «…» |
| **Registros inmutables / anulación** (`15`) | «estados y método de anular» | «si aplica» |
| **Spec de módulo** (`02` · F2) | «dónde vive, qué plantilla» | «…» |
| **Framework de pruebas** (`08`) | «…» | «…» |
| **Logging** (`05`) | «librería / niveles» | «…» |

## Nomenclatura del proyecto (concreta `14` · EST2)

- **Tablas:** «convención» · **Columnas:** «convención» · **Clases:** «convención»
- **Claves foráneas:** «sufijo» · **Booleanos:** «prefijo» · **Timestamps de evento:** «sufijo»
- **Permisos:** «formato» · **Migraciones:** «formato»

## Código legacy (concreta `14` · EST3)

- Elementos existentes que **no** siguen la convención y **no se renombran:** «lista o criterio».
