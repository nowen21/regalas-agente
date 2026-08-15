# Mapeo de nombres  ·  `[CAPA 3]`

> Plantilla. La base habla en abstracto ("catálogo", "auditoría", "permiso"). Aquí declaras **cómo se llama cada cosa en este proyecto**, para que el agente aplique la regla con el nombre real. Reemplaza los `«…»` y borra esta caja.
>
> Son dos tablas y no se pisan: la primera la lee **el agente** y admite frases y matices; la segunda la lee **un programa** y por eso tiene forma fija. Lo que ya está en la segunda no se repite en la primera.

## Conceptos de la base → nombre concreto aquí

| Concepto en la base | En este proyecto | Ejemplo / ubicación |
|---|---|---|
| **Catálogo** (`03` · D4) — dónde viven valores configurables | «tabla / mecanismo» | «…» |
| **Bifurcar por código semántico** (`03` · D4) | «cómo se resuelve el código» | «…» |
| **Prefijo de tablas nuevas** (`14` · EST2) | «prefijo o convención» | «…» |
| **Sistema de permisos** (`04` · S1) | «librería / cómo se otorgan» | «…» |
| **Estado de registro / borrado lógico** (`03` · D1) | «cómo se modela» | «…» |
| **Almacenamiento privado de archivos** (`04` · S6) | «disco / ruta / mecanismo» | «…» |
| **Especificación de módulo** (`02` · F2) | «dónde vive, qué plantilla» | «…» |
| **Framework de pruebas** (`08`) | «…» | «…» |
| **Logging** (`05`) | «librería / niveles» | «…» |
| **Migraciones** (`03` · D2) | «formato del nombre / carpeta» | «…» |

## Convenciones que un programa comprueba

> Esta es la que hace comprobables `14`·EST1, `14`·EST2, `03`·D1, `15`·IM2 y `15`·IM5: sin ella, "sigue la convención" no se puede decidir sin opinar, y esas cinco reglas se quedan en criterio del agente.
>
> **Cómo se llena.** La primera columna es la **clave**: no se cambia, no se traduce y no se reordena. La segunda es el valor, escrito como dice el vocabulario de abajo. Lo que este proyecto no quiera declarar se deja en `libre`, y el validador se salta esa parte — no inventa una convención que nadie acordó.

| Clave | Valor |
|---|---|
| `modulos.ruta` | `libre` |
| `tablas.caso` | `libre` |
| `columnas.caso` | `libre` |
| `clases.caso` | `libre` |
| `fk.sufijo` | `libre` |
| `booleanos.prefijo` | `libre` |
| `timestamps.sufijo` | `libre` |
| `permisos.formato` | `libre` |
| `auditoria.columnas` | `libre` |
| `inmutables.estados` | `libre` |
| `inmutables.anulacion` | `libre` |
| `inmutables.permiso` | `libre` |
| `legacy.ignorar` | `libre` |

**Qué se escribe en cada valor:**

| Clave | Qué declara | Cómo se escribe | Ejemplo |
|---|---|---|---|
| `modulos.ruta` | dónde vive cada módulo ([`14·EST1`](../base/14-estructura-codigo.md#est1--organiza-el-código-nuevo-por-módulo-en-ubicación-predecible)) | una ruta con `<modulo>` en el lugar del nombre, desde la raíz del repositorio | `app/Modules/<modulo>` |
| `tablas.caso` | cómo se escribe un nombre de tabla ([`14·EST2`](../base/14-estructura-codigo.md#est2--nomenclatura-consistente)) | uno de: `snake_case` · `PascalCase` · `camelCase` · `kebab-case` · `SCREAMING_SNAKE` | `snake_case` |
| `columnas.caso` | ídem para columnas | los mismos cinco | `snake_case` |
| `clases.caso` | ídem para clases | los mismos cinco | `PascalCase` |
| `fk.sufijo` | cómo termina una clave foránea | el sufijo tal cual; varios separados por coma | `_id` |
| `booleanos.prefijo` | cómo empieza una columna booleana | el prefijo tal cual; varios separados por coma | `es_, tiene_` |
| `timestamps.sufijo` | cómo termina una fecha de evento | el sufijo tal cual; varios separados por coma | `_at` |
| `permisos.formato` | la forma de un permiso ([`04·S1`](../base/04-seguridad.md#s1--autorización-en-cada-acción-sensible)) | un patrón con `<recurso>` y `<accion>` | `<recurso>.<accion>` |
| `auditoria.columnas` | qué lleva toda tabla de dominio ([`03·D1`](../base/03-datos.md#d1--toda-tabla-nueva-se-normaliza-y-lleva-auditoría)) | las columnas separadas por coma, o `mecanismo:<Nombre>` si las pone un trait, un mixin o una clase base | `usercreate_id, userupdate_id, created_at, updated_at` |
| `inmutables.estados` | los tres estados de [`15·IM2`](../base/15-registros-inmutables.md#im2--estados-y-campos-de-anulación) | los códigos reales, en orden borrador → materializado → anulado | `borrador, materializado, anulado` |
| `inmutables.anulacion` | los campos de anulación de [`15·IM2`](../base/15-registros-inmutables.md#im2--estados-y-campos-de-anulación) | las columnas de cuándo, quién y motivo | `anulado_at, anulado_por, motivo_anulacion` |
| `inmutables.permiso` | el permiso propio de anular ([`15·IM5`](../base/15-registros-inmutables.md#im5--permiso-propio-para-anular)) | el permiso con `<recurso>` en el lugar de la entidad | `<recurso>.anular` |
| `legacy.ignorar` | qué código quedó fuera de la convención y no se renombra ([`14·EST3`](../base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo)) | rutas o patrones separados por coma; lo que encaje no se revisa | `app/Legacy/*, database/migrations/2019_*` |

Qué entidades son de dominio y cuáles son inmutables **no se declara aquí**: eso es dominio, y va en la tabla de entidades de `dominio.md`, el archivo vecino de esta misma carpeta.

## Código legacy (concreta `14` · EST3)

- Elementos existentes que **no** siguen la convención y **no se renombran:** «lista o criterio». Lo que además deba saltarse el validador va en `legacy.ignorar`, arriba.
