# -*- coding: utf-8 -*-
"""Lógica del visor: leer los documentos del estándar y consultar la memoria."""
import os, re, html, sqlite3

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB = os.environ.get("MEMORIA_DB", os.path.join(RAIZ, "memoria", "senales.db"))
SECCIONES = [("Reglas (núcleo + convenciones)", "base"),
             ("Roles / skills", "skills"),
             ("Plantillas (capa 3)", "plantillas"),
             ("Notas de diseño", "notas")]

# ---------------- Markdown mínimo ----------------
def _inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    return s

def md_to_html(md):
    L = md.split('\n'); out = []; i = 0; n = len(L)
    while i < n:
        line = L[i]
        if line.startswith('```'):
            i += 1; buf = []
            while i < n and not L[i].startswith('```'):
                buf.append(L[i]); i += 1
            i += 1; out.append('<pre>' + html.escape('\n'.join(buf)) + '</pre>'); continue
        if line.strip().startswith('|') and i + 1 < n and re.match(r'^\s*\|?[\s:|\-]+\|?\s*$', L[i+1]):
            head = [c.strip() for c in line.strip().strip('|').split('|')]; i += 2; rows = []
            while i < n and L[i].strip().startswith('|'):
                rows.append([c.strip() for c in L[i].strip().strip('|').split('|')]); i += 1
            t = '<table class="table table-sm table-bordered"><thead><tr>' + ''.join('<th>%s</th>' % _inline(h) for h in head) + '</tr></thead><tbody>'
            for r in rows:
                t += '<tr>' + ''.join('<td>%s</td>' % _inline(c) for c in r) + '</tr>'
            out.append(t + '</tbody></table>'); continue
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            lv = len(m.group(1)); out.append('<h%d>%s</h%d>' % (lv, _inline(m.group(2)), lv)); i += 1; continue
        if re.match(r'^---+\s*$', line):
            out.append('<hr>'); i += 1; continue
        if line.startswith('>'):
            buf = []
            while i < n and L[i].startswith('>'):
                buf.append(L[i].lstrip('>').strip()); i += 1
            out.append('<blockquote class="blockquote fs-6 border-start border-3 ps-3 text-body-secondary">' + ' '.join(_inline(b) for b in buf) + '</blockquote>'); continue
        if re.match(r'^\s*[-*]\s+', line):
            out.append('<ul>')
            while i < n and re.match(r'^\s*[-*]\s+', L[i]):
                out.append('<li>%s</li>' % _inline(re.sub(r'^\s*[-*]\s+', '', L[i]))); i += 1
            out.append('</ul>'); continue
        if re.match(r'^\s*\d+\.\s+', line):
            out.append('<ol>')
            while i < n and re.match(r'^\s*\d+\.\s+', L[i]):
                out.append('<li>%s</li>' % _inline(re.sub(r'^\s*\d+\.\s+', '', L[i]))); i += 1
            out.append('</ol>'); continue
        if line.strip() == '':
            i += 1; continue
        out.append('<p>%s</p>' % _inline(line)); i += 1
    return '\n'.join(out)

# ---------------- Documentos ----------------
def _items(carpeta):
    base = os.path.join(RAIZ, carpeta); items = []
    if os.path.isdir(base):
        for dirpath, _, files in os.walk(base):
            for f in sorted(files):
                if f.endswith('.md') or f.endswith('.plantilla'):
                    rel = os.path.relpath(os.path.join(dirpath, f), RAIZ).replace('\\', '/')
                    nombre = rel.split('/', 1)[1] if '/' in rel else rel
                    items.append({'nombre': nombre, 'rel': rel})
    return sorted(items, key=lambda x: x['rel'])

def listar_docs():
    return [{'titulo': t, 'items': _items(c)} for t, c in SECCIONES]

def nav(request):
    """Menú lateral con la sección del doc activo marcada como abierta."""
    activo = request.GET.get('p', '') if request.path.startswith('/doc') else ''
    secs = []
    for t, c in SECCIONES:
        items = _items(c)
        for it in items:
            it['activo'] = (it['rel'] == activo)
        secs.append({'titulo': t, 'items': items, 'abierta': any(i['activo'] for i in items)})
    return {'secciones': secs}

def leer_doc(rel):
    # Solo se sirven los documentos listados en el menú (las carpetas de SECCIONES,
    # extensiones .md/.plantilla). Bloquea rutas arbitrarias como config/settings.py o traversal.
    permitidos = {it['rel'] for sec in listar_docs() for it in sec['items']}
    if rel not in permitidos:
        return None
    p = os.path.join(RAIZ, rel)
    if not os.path.isfile(p):
        return None
    with open(p, encoding='utf-8') as f:
        return f.read()

# ---------------- Memoria ----------------
def _con():
    return sqlite3.connect('file:%s?mode=ro' % DB, uri=True)

def _fts_query(q):
    """Convierte la búsqueda del usuario en términos FTS5 seguros.

    Extrae solo palabras (ignora símbolos como - + " que rompen la sintaxis
    FTS5) y las une como prefijos. Así 'git add -A' → '"git"* "add"* "a"*'
    en vez de reventar con OperationalError.
    """
    toks = re.findall(r'\w+', q, re.UNICODE)
    return ' '.join('"%s"*' % t.lower() for t in toks) if toks else None

def consultar_senales(q, scope, tipo, pagina=1, por_pagina=25):
    """Devuelve una PÁGINA de señales (no todas): {filas, total, pagina, por_pagina}.
    Pagina a nivel SQL (LIMIT/OFFSET) para no cargar todo cuando hay muchas."""
    if not os.path.exists(DB):
        return None
    con = _con(); con.row_factory = sqlite3.Row
    try:
        fts = _fts_query(q) if q else None
        if fts:
            desde = "FROM senales_fts f JOIN senales s ON s.rowid=f.rowid WHERE senales_fts MATCH ?"
            params = [fts]; pfx = "s."; order = " ORDER BY bm25(senales_fts)"; sel = "SELECT s.*"
        else:
            desde = "FROM senales WHERE 1=1"; params = []; pfx = ""; order = " ORDER BY rowid DESC"; sel = "SELECT *"
        if scope:
            desde += " AND %sscope = ?" % pfx; params.append(scope)   # exacto: evita que 'organizacion' traiga 'organizacion-beta'
        if tipo:
            desde += " AND %stipo = ?" % pfx; params.append(tipo)
        total = con.execute("SELECT COUNT(*) " + desde, params).fetchone()[0]
        paginas = max(1, -(-total // por_pagina))     # techo de total/por_pagina
        pagina = min(max(1, pagina), paginas)          # clamp antes de consultar
        offset = (pagina - 1) * por_pagina
        filas = [dict(r) for r in con.execute(sel + " " + desde + order + " LIMIT ? OFFSET ?",
                                              params + [por_pagina, offset]).fetchall()]
        return {'filas': filas, 'total': total, 'pagina': pagina, 'por_pagina': por_pagina}
    except sqlite3.OperationalError:
        return {'filas': [], 'total': 0, 'pagina': pagina, 'por_pagina': por_pagina}
    finally:
        con.close()

def scopes_y_tipos():
    if not os.path.exists(DB):
        return [], []
    con = _con()
    try:
        sc = [r[0] for r in con.execute("SELECT DISTINCT scope FROM senales ORDER BY scope")]
        tp = [r[0] for r in con.execute("SELECT DISTINCT tipo FROM senales ORDER BY tipo")]
        return sc, tp
    except sqlite3.OperationalError:
        return [], []
    finally:
        con.close()

def contar_docs():
    return {t: len(_items(c)) for t, c in SECCIONES}

def resumen_memoria():
    """Datos agregados de la memoria para el panel."""
    if not os.path.exists(DB):
        return None
    from collections import Counter
    con = _con(); con.row_factory = sqlite3.Row
    try:
        rows = [dict(r) for r in con.execute("SELECT rowid, * FROM senales ORDER BY rowid").fetchall()]
    except sqlite3.OperationalError:
        return {'vacia': True}
    finally:
        con.close()

    total = len(rows)
    activas = sum(1 for r in rows if r['estado'] == 'activa')
    por_tipo = Counter(r['tipo'] for r in rows)
    por_scope = Counter(r['scope'] for r in rows)
    org = sum(v for k, v in por_scope.items() if k == 'organizacion')
    proyectos = {k: v for k, v in sorted(por_scope.items()) if k != 'organizacion'}
    recientes = list(reversed(rows))[:6]
    return {
        'vacia': total == 0,
        'total': total,
        'activas': activas,
        'otras': total - activas,
        'n_tipos': len(por_tipo),
        'n_proyectos': len(proyectos),
        'org': org,
        'por_tipo': [{'tipo': k, 'n': v} for k, v in por_tipo.most_common()],
        'proyectos': [{'scope': k, 'n': v} for k, v in proyectos.items()],
        'recientes': recientes,
    }
