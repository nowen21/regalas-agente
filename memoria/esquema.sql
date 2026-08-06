-- Esquema de la memoria por señales (SQLite + FTS5).
-- Backend opcional del estándar. Una sola base central; el campo `scope`
-- separa lo de cada proyecto de lo compartido (organizacion).
-- El estándar define QUÉ son las señales; esta es UNA forma de guardarlas.

CREATE TABLE IF NOT EXISTS senales (
  rowid     INTEGER PRIMARY KEY,
  id        TEXT UNIQUE NOT NULL,                 -- S-001, S-002…
  tipo      TEXT NOT NULL,                        -- decision, error-resuelto, patron, aprendizaje,
                                                  -- alternativa-descartada, supuesto, restriccion,
                                                  -- pregunta-abierta, gotcha, deuda-tecnica
  titulo    TEXT NOT NULL,
  what      TEXT,
  why       TEXT,
  where_    TEXT,                                 -- archivo:linea o area
  learned   TEXT,
  scope     TEXT NOT NULL DEFAULT 'proyecto',     -- organizacion | proyecto:<slug> | modulo:<slug>
  estado    TEXT NOT NULL DEFAULT 'activa',       -- activa | reemplazada | revertida | archivada
  reemplaza TEXT,                                 -- id de la señal que reemplaza
  creada    TEXT NOT NULL,                        -- ISO date de creación
  revisada  TEXT,                                 -- ISO date de última revisión (vigencia)
  autor     TEXT
);
-- estado: solo 'activa' aparece en `search`. 'archivada' = podada (fuera de
-- búsqueda, pero se conserva; nunca se borra). 'reemplazada'/'revertida' = ya
-- existían. `revisada` marca la vigencia: una señal sin revisar hace meses se
-- muestra atenuada. En bases previas, la migración agrega `revisada` y la
-- rellena con `creada` (ver memoria.py · cmd_init).

-- Índice de texto completo (FTS5), contenido externo sincronizado por triggers.
CREATE VIRTUAL TABLE IF NOT EXISTS senales_fts USING fts5(
  titulo, what, why, learned, tipo, scope,
  content='senales', content_rowid='rowid',
  tokenize='unicode61 remove_diacritics 2'       -- ignora acentos (factura ≈ facturá)
);

-- Mantener el índice al día
CREATE TRIGGER IF NOT EXISTS senales_ai AFTER INSERT ON senales BEGIN
  INSERT INTO senales_fts(rowid, titulo, what, why, learned, tipo, scope)
  VALUES (new.rowid, new.titulo, new.what, new.why, new.learned, new.tipo, new.scope);
END;
CREATE TRIGGER IF NOT EXISTS senales_ad AFTER DELETE ON senales BEGIN
  INSERT INTO senales_fts(senales_fts, rowid, titulo, what, why, learned, tipo, scope)
  VALUES ('delete', old.rowid, old.titulo, old.what, old.why, old.learned, old.tipo, old.scope);
END;
CREATE TRIGGER IF NOT EXISTS senales_au AFTER UPDATE ON senales BEGIN
  INSERT INTO senales_fts(senales_fts, rowid, titulo, what, why, learned, tipo, scope)
  VALUES ('delete', old.rowid, old.titulo, old.what, old.why, old.learned, old.tipo, old.scope);
  INSERT INTO senales_fts(rowid, titulo, what, why, learned, tipo, scope)
  VALUES (new.rowid, new.titulo, new.what, new.why, new.learned, new.tipo, new.scope);
END;
