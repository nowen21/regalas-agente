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
    p = os.path.normpath(os.path.join(RAIZ, rel))
    if not p.startswith(RAIZ) or not os.path.isfile(p):
        return None
    with open(p, encoding='utf-8') as f:
        return f.read()

# ---------------- Memoria ----------------
def _con():
    return sqlite3.connect('file:%s?mode=ro' % DB, uri=True)

def consultar_senales(q, scope, tipo):
    if not os.path.exists(DB):
        return None
    con = _con(); con.row_factory = sqlite3.Row
    try:
        if q:
            sql = ("SELECT s.* FROM senales_fts f JOIN senales s ON s.rowid=f.rowid "
                   "WHERE senales_fts MATCH ?"); params = [q]; pfx = "s."; order = " ORDER BY bm25(senales_fts)"
        else:
            sql = "SELECT * FROM senales WHERE 1=1"; params = []; pfx = ""; order = " ORDER BY rowid DESC"
        if scope:
            sql += " AND %sscope LIKE ?" % pfx; params.append(scope + '%')
        if tipo:
            sql += " AND %stipo = ?" % pfx; params.append(tipo)
        return [dict(r) for r in con.execute(sql + order, params).fetchall()]
    except sqlite3.OperationalError:
        return []
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
