import os, json, math
from urllib.parse import urlencode
from django.shortcuts import render
import csv
from django.http import Http404, JsonResponse, HttpResponse
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from . import core


def senal_detalle(request):
    s = core.get_senal(request.GET.get('id', ''))
    if not s:
        raise Http404('Señal no encontrada')
    return render(request, 'visor/_senal_detalle.html', {'s': s})


@csrf_exempt
def crear_senal(request):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)
    campos = ['tipo', 'titulo', 'what', 'why', 'where', 'learned', 'scope', 'autor', 'reemplaza']
    sid, err = core.registrar_senal({k: request.POST.get(k, '') for k in campos})
    if err:
        return JsonResponse({'ok': False, 'error': err}, status=400)
    return JsonResponse({'ok': True, 'id': sid})


def export_senales(request):
    q = request.GET.get('q', '').strip()
    scope = request.GET.get('scope', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    orden = request.GET.get('orden', '').strip()
    direccion = request.GET.get('dir', 'desc').strip()
    res = core.consultar_senales(q, scope, tipo, pagina=1, por_pagina=10 ** 9,
                                 orden=orden or None, direccion=direccion)
    resp = HttpResponse(content_type='text/csv; charset=utf-8')
    resp['Content-Disposition'] = 'attachment; filename="senales.csv"'
    resp.write('﻿')  # BOM para que Excel abra los acentos bien
    w = csv.writer(resp)
    w.writerow(['id', 'tipo', 'scope', 'estado', 'titulo', 'what', 'why', 'where', 'learned', 'reemplaza', 'creada', 'autor'])
    if res:
        for r in res['filas']:
            w.writerow([r.get('id'), r.get('tipo'), r.get('scope'), r.get('estado'), r.get('titulo'),
                        r.get('what'), r.get('why'), r.get('where_'), r.get('learned'),
                        r.get('reemplaza'), r.get('creada'), r.get('autor')])
    return resp


def panel(request):
    r = core.resumen_memoria()
    ctx = {'r': r, 'db': core.DB}
    if r and not r.get('vacia'):
        ctx['tipos_labels'] = json.dumps([x['tipo'] for x in r['por_tipo']])
        ctx['tipos_data'] = json.dumps([x['n'] for x in r['por_tipo']])
        labels = (['organizacion (repisa)'] if r['org'] else []) + [p['scope'] for p in r['proyectos']]
        data = ([r['org']] if r['org'] else []) + [p['n'] for p in r['proyectos']]
        valores = (['organizacion'] if r['org'] else []) + [p['scope'] for p in r['proyectos']]
        ctx['scope_labels'] = json.dumps(labels)
        ctx['scope_data'] = json.dumps(data)
        ctx['scope_values'] = json.dumps(valores)
    return render(request, 'visor/panel.html', ctx)


def home(request):
    conteo = core.contar_docs()
    mem = core.consultar_senales('', '', '', por_pagina=1)
    iconos = {"Reglas (núcleo + convenciones)": "bi-shield-check",
              "Roles / skills": "bi-diagram-3",
              "Plantillas (capa 3)": "bi-ui-checks-grid",
              "Notas de diseño": "bi-journal-text"}
    kpis = [{'n': v, 'label': t, 'icon': iconos.get(t, 'bi-file-earmark')} for t, v in conteo.items()]
    kpis.append({'n': mem['total'] if mem else 0, 'label': 'Señales en memoria', 'icon': 'bi-hdd-stack'})
    return render(request, 'visor/home.html', {'kpis': kpis})


def doc(request):
    rel = request.GET.get('p', '')
    md = core.leer_doc(rel)
    if md is None:
        raise Http404('Documento no encontrado')
    nombre = rel.split('/', 1)[1] if '/' in rel else rel
    return render(request, 'visor/doc.html', {'nombre': nombre, 'contenido': mark_safe(core.md_to_html(md))})


def memoria(request):
    q = request.GET.get('q', '').strip()
    scope = request.GET.get('scope', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    try:
        pagina = int(request.GET.get('pag', '1'))
    except ValueError:
        pagina = 1
    orden = request.GET.get('orden', '').strip()
    direccion = request.GET.get('dir', 'desc').strip()
    res = core.consultar_senales(q, scope, tipo, pagina=pagina, orden=orden or None, direccion=direccion)
    sc, tp = core.scopes_y_tipos()
    ctx = {'q': q, 'scope': scope, 'tipo': tipo, 'scopes': sc, 'tipos': tp,
           'tipos_todos': core.TIPOS, 'no_db': res is None, 'db': core.DB,
           'orden': res['orden'] if res else None, 'direccion': res['direccion'] if res else '',
           'cols': [('id', 'ID', '6rem'), ('tipo', 'Tipo', ''), ('scope', 'Scope', ''), ('estado', 'Estado', '')]}
    if res is not None:
        por = res['por_pagina']
        paginas = max(1, math.ceil(res['total'] / por))
        pag = min(res['pagina'], paginas)
        ctx.update({
            'filas': res['filas'], 'total': res['total'],
            'pagina': pag, 'paginas': paginas,
            'desde': (pag - 1) * por + (1 if res['total'] else 0),
            'hasta': (pag - 1) * por + len(res['filas']),
            'prev': pag - 1, 'next': pag + 1,
            'tiene_prev': pag > 1, 'tiene_next': pag < paginas,
            'rango': range(max(1, pag - 2), min(paginas, pag + 2) + 1),
            # querystring de filtros + orden (sin 'pag') para los enlaces de página
            'qs': urlencode({k: v for k, v in {'q': q, 'scope': scope, 'tipo': tipo,
                                               'orden': res['orden'] or '', 'dir': res['direccion']}.items() if v}),
        })
    # AJAX: solo la tabla (filtro dinámico, sin recargar la página)
    if request.GET.get('parcial') and res is not None:
        return render(request, 'visor/_memoria_tabla.html', ctx)
    return render(request, 'visor/memoria.html', ctx)
