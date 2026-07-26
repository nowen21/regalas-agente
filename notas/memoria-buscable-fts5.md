# Memoria buscable con SQLite + FTS5 (backend opcional)

> Cómo hacer **buscables** las señales cuando el archivo `senales.md` se queda corto (muchas señales). Es un **backend opcional de capa 3**: el estándar define *qué* son las señales ([`memoria-por-senales.md`](memoria-por-senales.md)); SQLite+FTS5 es *una* forma de guardarlas y recuperarlas. Archivo y SQLite son **intercambiables**; se elige según volumen.

## Por qué

Guardar es la mitad fácil; **recuperar la señal relevante** es la difícil. Con pocas señales, leer el archivo alcanza. Con cientos, no: no cabe en el contexto. FTS5 permite pedir "traeme las señales que tienen que ver con X" y recibir las relevantes con ranking — **sin dependencias externas** (SQLite viene incluido).

## Esquema (listo para usar)

```sql
-- Tabla real de señales
CREATE TABLE senales (
  id        TEXT PRIMARY KEY,          -- S-001, S-002…
  tipo      TEXT NOT NULL,             -- decision, error-resuelto, patron, aprendizaje…
  titulo    TEXT NOT NULL,
  what      TEXT, why TEXT, where_ TEXT, learned TEXT,
  scope     TEXT,                      -- modulo:X / proyecto / organizacion
  estado    TEXT DEFAULT 'activa',     -- activa / reemplazada / revertida
  reemplaza TEXT,                      -- id de la señal que reemplaza
  creada    TEXT, autor TEXT
);

-- Índice de texto completo (FTS5) sincronizado con la tabla
CREATE VIRTUAL TABLE senales_fts USING fts5(
  titulo, what, why, learned, tipo, scope,
  content='senales', content_rowid='rowid'
);
```

## Consultas típicas

```sql
-- Buscar señales relevantes a un tema, activas, ordenadas por relevancia (BM25)
SELECT s.id, s.tipo, s.titulo
FROM senales_fts f JOIN senales s ON s.rowid = f.rowid
WHERE senales_fts MATCH 'facturacion OR iva OR anulacion'
  AND s.estado = 'activa'
ORDER BY bm25(senales_fts)
LIMIT 5;

-- Solo un tipo (p. ej. gotchas del módulo actual)
SELECT id, titulo FROM senales
WHERE tipo = 'gotcha' AND scope = 'modulo:facturacion' AND estado = 'activa';
```

## Cómo se usa (el hábito de recuperación)

- **Antes de trabajar** en un tema, consultar la memoria por sus palabras clave y traer las señales activas relevantes (recencia + relevancia). Es la extensión natural de `02`·F1 a las señales.
- **Al cerrar**, registrar las señales nuevas (`13`·DOC5).
- **Supersesión:** al reemplazar una decisión, insertar la nueva con `reemplaza=S-vieja` y marcar la vieja `estado='reemplazada'` — no borrar (rastro).

## Migración desde el archivo

El `senales.md` se puede importar a la tabla una vez (cada entrada → una fila). Desde ahí, el archivo puede seguir como export legible o retirarse.

## Límite

FTS5 busca por **palabra** (léxico): "factura" no encuentra "recibo" aunque sean parecidos. Para búsqueda por **significado** (semántica) hacen falta embeddings → esa es la capa **entre proyectos con MCP** (pieza externa). FTS5 es el punto medio: recuperación real, local, cero dependencias.

## Dónde encaja

- Es **capa 3**: un proyecto con muchas señales lo activa; los demás siguen con `senales.md`.
- El estándar permanece agnóstico: las skills que registran/consultan memoria hablan de "señales", no de SQLite.
- Relacionado: [`memoria-por-senales.md`](memoria-por-senales.md), [`compactacion-mata-decisiones.md`](compactacion-mata-decisiones.md).
