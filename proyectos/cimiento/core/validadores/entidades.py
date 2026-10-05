"""`03·D1`, `15·IM2` y `15·IM5` · Lo que se le exige a una tabla de dominio.

El validador de esquema ya pide la política de borrado de toda clave foránea. Lo
que falta de D1 (auditoría, `UNIQUE` en la clave natural, índice en las claves
foráneas) y todo el capítulo 15 dependen de algo que solo el proyecto sabe:
**cuáles tablas son de dominio** y **qué entidad es inmutable**. Un `sessions` o
un `jobs` no llevan auditoría. Eso lo declara `.agente/dominio.md`, y se compara
el `CREATE` de cada tabla declarada contra eso.

  D1  · columnas de auditoría, `UNIQUE` en la clave natural, índice en cada FK.
  IM2 · la entidad inmutable tiene sus estados y sus campos de anulación.
  IM5 · la entidad inmutable tiene su permiso propio de anular.

Todo es aviso: un estado puede vivir en un catálogo, una tabla puede heredar la
auditoría de otra, y eso lo sabe una persona.
"""
import re

from ..comun import AVISO, Hallazgo
from .base import Validador
from .codigo import RecorridoDeCodigo
from .declaracion import DOMINIO, Declaracion
from .esquema import LEGIBLES, LectorDeEsquema
from .migraciones import RecorridoDeMigraciones

_UNIQUE_PHP = re.compile(r"->\s*unique\s*\(([^)]*)\)")
_UNIQUE_SQL = re.compile(r"(?i)\bUNIQUE\b(?:\s+KEY)?(?:\s+[`\"\w]+)?\s*\(([^)]*)\)")
_INDICE_PHP = re.compile(r"->\s*(?:index|unique|primary|spatialIndex|fullText)\s*\(([^)]*)\)")
_INDICE_SQL = re.compile(r"(?i)\b(?:PRIMARY\s+KEY|UNIQUE(?:\s+KEY)?|KEY|INDEX)\b(?:\s+[`\"\w]+)?\s*\(([^)]*)\)")
_FK_AUTOINDEXADA = re.compile(r"->\s*(?:foreignId|foreignUlid|foreignUuid|constrained)\s*\(")
_FK_PHP = re.compile(r"->\s*foreign\s*\(\s*['\"]([^'\"]+)")
_FK_SQL = re.compile(r"(?i)FOREIGN\s+KEY\s*\(\s*[`\"\[]?(\w+)")


def _es_php(ruta):
    return ruta.lower().endswith(".php")


def _palabras(fragmento):
    return {p.strip(" `\"'[]") for p in fragmento.split(",") if p.strip(" `\"'[]")}


def _grupos(cuerpo, ruta, php, sql):
    return [_palabras(m.group(1)) for m in (php if _es_php(ruta) else sql).finditer(cuerpo)]


def _columnas_sueltas_con(cuerpo, ruta, marca):
    """Columnas que traen la marca en su propia declaración (`->unique()`)."""
    salida = set()
    for linea in cuerpo.splitlines():
        if _es_php(ruta):
            if marca in linea:
                m = re.search(r"->\s*\w+\s*\(\s*['\"]([^'\"]+)", linea)
                if m:
                    salida.add(m.group(1))
        elif marca.strip("->()").upper() in linea.upper():
            m = re.match(r"^\s*[`\"\[]?(\w+)[`\"\]]?\s+[A-Za-z]", linea)
            if m:
                salida.add(m.group(1))
    return salida


def _codigos(columnas):
    return ", ".join("`%s`" % c for c in columnas)


class TablasDeDominio(Validador):
    """Revisa la auditoría, la unicidad, los índices y la inmutabilidad declarados."""

    nombre = "entidades"
    regla = "03·D1, 15·IM2, 15·IM5"
    descripcion = "auditoría, unicidad e inmutabilidad de las tablas de dominio"

    def validar(self):
        d = Declaracion.leer(self.proyecto, self.archivos)
        if not d.tablas_de_dominio():
            return [Hallazgo(AVISO, self.proyecto.raiz, 0,
                             "el proyecto no declara sus entidades en `%s`: el resto de D1 y todo 15 "
                             "se quedan en criterio del agente" % DOMINIO)]
        migraciones = RecorridoDeMigraciones(self.proyecto, self.archivos)
        creadas = self.creaciones(d, migraciones)
        hallazgos = []
        # Si no se pudo leer ninguna migración y las hay en otro formato, no hay
        # contra qué comparar: se dice una vez y no se acusa tabla por tabla.
        a_ciegas = not creadas and migraciones.hay_fuera_de(LEGIBLES)
        if a_ciegas:
            hallazgos.append(Hallazgo(
                AVISO, self.proyecto.raiz, 0,
                "las migraciones de este proyecto no están en un formato que se pueda leer (%s): "
                "no se comprueba si las tablas declaradas existen, ni su auditoría, unicidad ni "
                "índices. **No es que falten**: es que no se pueden mirar desde acá" % ", ".join(LEGIBLES)))
        for entidad in d.tablas_de_dominio():
            creada = creadas.get(entidad.tabla.lower())
            if not creada:
                if not a_ciegas:
                    hallazgos.append(Hallazgo(AVISO, self.proyecto.ruta(DOMINIO), 0,
                                              "`%s` declara la tabla `%s` y ninguna migración la crea"
                                              % (entidad.nombre, entidad.tabla)))
                continue
            mostrada, cuerpo, linea, ruta = creada
            aviso = lambda mensaje: Hallazgo(AVISO, mostrada, linea, mensaje)
            hallazgos += [aviso(m) for m in self._auditoria(entidad, cuerpo, ruta, d)]
            hallazgos += [aviso(m) for m in self._unicidad(entidad, cuerpo, ruta)]
            hallazgos += [aviso(m) for m in self._indices(entidad, cuerpo, ruta)]
            if entidad.inmutable:
                hallazgos += [aviso(m) for m in self._inmutable(entidad, cuerpo, ruta, d)]
        hallazgos += self._permisos(d)
        return hallazgos

    @staticmethod
    def creaciones(d, migraciones):
        """`{tabla: (ruta mostrada, cuerpo, línea, ruta en su repositorio)}` de cada `CREATE`."""
        salida = {}
        for mostrada, ruta, texto, _ in migraciones.migraciones(LEGIBLES):
            if not d.ignorado(mostrada):
                for tabla, cuerpo, linea in LectorDeEsquema.tablas_creadas(ruta, texto):
                    salida[tabla.lower()] = (mostrada, cuerpo, linea, ruta)
        return salida

    @staticmethod
    def _auditoria(entidad, cuerpo, ruta, d):
        declarado = d.convencion("auditoria.columnas")
        if not declarado:
            return []
        if declarado.lower().startswith("mecanismo:"):
            marca = declarado.split(":", 1)[1].strip()
            if marca and marca.lower() in cuerpo.lower():
                return []
            return ["la tabla `%s` es de dominio y no usa `%s`, el mecanismo de auditoría declarado (D1)"
                    % (entidad.tabla, marca)]
        columnas = {n.lower() for n, _ in LectorDeEsquema.columnas_de(cuerpo, ruta)}
        faltan = [c for c in d.lista("auditoria.columnas") if c.lower() not in columnas]
        return ["la tabla `%s` es de dominio y le faltan columnas de auditoría: %s (D1)"
                % (entidad.tabla, _codigos(faltan))] if faltan else []

    @staticmethod
    def _unicidad(entidad, cuerpo, ruta):
        if not entidad.clave_natural:
            return []
        grupos = _grupos(cuerpo, ruta, _UNIQUE_PHP, _UNIQUE_SQL)
        grupos += [{c} for c in _columnas_sueltas_con(cuerpo, ruta, "->unique(")]
        grupos += [{c} for c in _columnas_sueltas_con(cuerpo, ruta, "UNIQUE")]
        clave = {c.lower() for c in entidad.clave_natural}
        if any(clave <= {x.lower() for x in g} for g in grupos):
            return []
        return ["la clave natural de `%s` (%s) no tiene `UNIQUE` en la tabla `%s` (D1)"
                % (entidad.nombre, _codigos(entidad.clave_natural), entidad.tabla)]

    @staticmethod
    def _indices(entidad, cuerpo, ruta):
        fks = {m.group(1) for m in (_FK_PHP if _es_php(ruta) else _FK_SQL).finditer(cuerpo)}
        if not fks:
            return []
        indexadas = set()
        for g in _grupos(cuerpo, ruta, _INDICE_PHP, _INDICE_SQL):
            indexadas |= {x.lower() for x in g}
        if _es_php(ruta):
            # `foreignId()` y `constrained()` crean el índice solos: pedirlo otra
            # vez sería pedir un índice duplicado.
            for linea in cuerpo.splitlines():
                if _FK_AUTOINDEXADA.search(linea):
                    m = re.search(r"['\"]([^'\"]+)['\"]", linea)
                    if m:
                        indexadas.add(m.group(1).lower())
        faltan = sorted(f for f in fks if f.lower() not in indexadas)
        return ["en `%s`, la clave foránea %s no tiene índice — D1 pide índice en lo que se filtra"
                % (entidad.tabla, _codigos(faltan))] if faltan else []

    @staticmethod
    def _inmutable(entidad, cuerpo, ruta, d):
        mensajes = []
        estados = d.lista("inmutables.estados")
        if estados:
            vistos = [e for e in estados if re.search(r"['\"]" + re.escape(e) + r"['\"]", cuerpo)]
            if not vistos:
                mensajes.append("`%s` es inmutable y en el esquema de `%s` no aparece ninguno de los "
                                "estados declarados (%s) — IM2. Si el estado sale de un catálogo, no aplica"
                                % (entidad.nombre, entidad.tabla, ", ".join(estados)))
            elif len(vistos) < len(estados):
                mensajes.append("`%s` es inmutable y le faltan estados en `%s`: %s — IM2 pide los tres"
                                % (entidad.nombre, entidad.tabla, ", ".join(e for e in estados if e not in vistos)))
        anulacion = d.lista("inmutables.anulacion")
        if anulacion:
            columnas = {n.lower() for n, _ in LectorDeEsquema.columnas_de(cuerpo, ruta)}
            faltan = [c for c in anulacion if c.lower() not in columnas]
            if faltan:
                mensajes.append("`%s` es inmutable y a `%s` le faltan campos de anulación: %s "
                                "(IM2: cuándo, quién y por qué)" % (entidad.nombre, entidad.tabla, _codigos(faltan)))
        return mensajes

    def recursos_con_permiso(self, patron, d):
        """Los recursos que ya tienen su permiso escrito en el código, según el patrón.

        El marcador se reemplaza sobre lo ya escapado, sin suponer cómo quedó:
        desde Python 3.7 `re.escape` no escapa los ángulos, y el reemplazo dejaba
        de ocurrir en silencio (`EP-004·HU-010`).
        """
        if "<recurso>" not in patron:
            return set()
        regex = re.compile(re.escape(patron).replace(re.escape("<recurso>"), r"([\w.-]+)"))
        return {m.group(1).lower()
                for ruta, texto in RecorridoDeCodigo(self.proyecto, self.archivos).archivos()
                if not d.ignorado(ruta)
                for m in regex.finditer(texto)}

    def _permisos(self, d):
        patron = d.convencion("inmutables.permiso")
        if not (patron and d.inmutables()):
            return []
        con_permiso = self.recursos_con_permiso(patron, d)
        return [Hallazgo(AVISO, self.proyecto.ruta(DOMINIO), 0,
                         "`%s` es inmutable y no se encuentra su permiso `%s` en el código "
                         "(IM5: anular lleva permiso propio)"
                         % (e.nombre, patron.replace("<recurso>", e.nombre.lower())))
                for e in d.inmutables() if not ({e.nombre.lower(), e.tabla.lower()} & con_permiso)]
