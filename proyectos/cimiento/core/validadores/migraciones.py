"""`03·D2` · Migraciones reversibles, y el recorrido de migraciones que usan los demás.

Lo comprobable sin criterio es que exista la **reversión**; que funcione de
verdad es otra cosa. Cada convención se reconoce por su extensión y su contenido:

  Laravel/PHP     `function up` exige `function down`.
  Alembic/Python  `def upgrade` exige `def downgrade`.
  Django/Python   `RunPython`/`RunSQL` exigen `reverse_code`/`reverse_sql`.
  Rails/Ruby      `def change`, o `def up` con `def down`.
  Node (js/ts)    `up` exige `down`.
  Pares SQL       `X.up.sql` exige `X.down.sql`.

Todo es aviso: una migración puede ser irreversible a propósito y estar documentada.
"""
import os
import re

from ..comun import AVISO, Git, Hallazgo
from .base import Validador

_CARPETAS = ("/migrations/", "/migrate/", "/versions/")
_EXTENSIONES = (".php", ".py", ".rb", ".js", ".ts", ".mjs", ".cjs", ".sql")
_SALTAR = re.compile(r"(^|/)(vendor|node_modules)/")


class RecorridoDeMigraciones:
    """Las migraciones versionadas de un proyecto. Estaba escrito tres veces:
    en este validador, en el de esquema y en el de entidades."""

    def __init__(self, proyecto, archivos):
        self.proyecto = proyecto
        self.lector = archivos

    @staticmethod
    def es_candidata(ruta):
        """¿Tiene pinta de migración, por su carpeta o por ser mitad de un par `.up/.down.sql`?"""
        r = ruta.lower()
        if _SALTAR.search(r):
            return False
        if r.endswith((".up.sql", ".down.sql")):
            return True
        return any(c in "/" + r for c in _CARPETAS) and r.endswith(_EXTENSIONES)

    def migraciones(self, extensiones=None):
        """`(ruta mostrada, ruta en su repositorio, texto, hermanos)` de cada migración.

        `hermanos` son los nombres de archivo de la misma carpeta, para los pares SQL.
        """
        for repo in self.proyecto.repositorios():
            prefijo = self.proyecto.prefijo_de(repo)
            candidatas = [a for a in Git(repo).versionados() if self.es_candidata(a)]
            por_carpeta = {}
            for a in candidatas:
                por_carpeta.setdefault(os.path.dirname(a), set()).add(os.path.basename(a))
            for a in candidatas:
                if extensiones and os.path.splitext(a.lower())[1] not in extensiones:
                    continue
                yield (prefijo + a, a, self.lector.leer(os.path.join(repo, a)),
                       por_carpeta[os.path.dirname(a)])

    def hay_fuera_de(self, extensiones):
        """¿Hay migraciones en un formato que no está en `extensiones`?"""
        return any(os.path.splitext(a.lower())[1] not in extensiones
                   for repo in self.proyecto.repositorios()
                   for a in Git(repo).versionados() if self.es_candidata(a))


class MigracionesReversibles(Validador):
    """Avisa de las migraciones que no declaran cómo revertirse."""

    nombre = "migraciones"
    regla = "03·D2"
    descripcion = "migraciones reversibles"

    def validar(self):
        if not self.proyecto.repositorios():
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        return [Hallazgo(AVISO, mostrada, 0, motivo)
                for mostrada, ruta, texto, hermanos in RecorridoDeMigraciones(self.proyecto, self.archivos).migraciones()
                for motivo in [self.motivo(ruta, texto, hermanos)] if motivo]

    @staticmethod
    def motivo(ruta, texto, hermanos=()):
        """Por qué esta migración no declara su reversión, o `None`."""
        base = os.path.basename(ruta)
        bajo = base.lower()
        ext = os.path.splitext(bajo)[1]
        if bajo.endswith(".up.sql"):
            pareja = base[:-len(".up.sql")] + ".down.sql"
            return None if pareja in hermanos else "falta el archivo de reversión `%s` (D2)" % pareja
        if bajo.endswith(".down.sql"):
            return None                             # la pareja la evalúa el `.up`
        if ext == ".py":
            if "django.db" in texto or "from django" in texto:
                faltan = []
                if "RunPython(" in texto and "reverse_code" not in texto:
                    faltan.append("RunPython sin reverse_code")
                if "RunSQL(" in texto and "reverse_sql" not in texto:
                    faltan.append("RunSQL sin reverse_sql")
                return "migración Django no reversible: %s (D2)" % ", ".join(faltan) if faltan else None
            if re.search(r"def\s+upgrade\b", texto):
                return None if re.search(r"def\s+downgrade\b", texto) else "Alembic: `upgrade` sin `downgrade` (D2)"
            return None
        if ext == ".rb":
            if re.search(r"def\s+change\b", texto):
                return None
            if re.search(r"def\s+up\b", texto) and not re.search(r"def\s+down\b", texto):
                return "Rails: `up` sin `down` ni `change` (D2)"
            return None
        if ext == ".php":
            if re.search(r"function\s+up\b", texto) and not re.search(r"function\s+down\b", texto):
                return "`up` sin `down` (D2)"
            return None
        if ext in (".js", ".ts", ".mjs", ".cjs"):
            up = re.search(r"exports\.up|function\s+up\b|\bup\s*[:(=]", texto)
            down = re.search(r"exports\.down|function\s+down\b|\bdown\s*[:(=]", texto)
            return "`up` sin `down` (D2)" if up and not down else None
        return None
