import os, json
from django.shortcuts import render
from django.http import Http404
from django.utils.safestring import mark_safe
from . import core


def panel(request):
    r = core.resumen_memoria()
    ctx = {'r': r, 'db': core.DB}
    if r and not r.get('vacia'):
        ctx['tipos_labels'] = json.dumps([x['tipo'] for x in r['por_tipo']])
        ctx['tipos_data'] = json.dumps([x['n'] for x in r['por_tipo']])
        labels = (['organizacion (repisa)'] if r['org'] else []) + [p['scope'] for p in r['proyectos']]
        data = ([r['org']] if r['org'] else []) + [p['n'] for p in r['proyectos']]
        ctx['scope_labels'] = json.dumps(labels)
        ctx['scope_data'] = json.dumps(data)
    return render(request, 'visor/panel.html', ctx)


def home(request):
    conteo = core.contar_docs()
    senales = core.consultar_senales('', '', '')
    iconos = {"Reglas (núcleo + convenciones)": "bi-shield-check",
              "Roles / skills": "bi-diagram-3",
              "Plantillas (capa 3)": "bi-ui-checks-grid",
              "Notas de diseño": "bi-journal-text"}
    kpis = [{'n': v, 'label': t, 'icon': iconos.get(t, 'bi-file-earmark')} for t, v in conteo.items()]
    kpis.append({'n': len(senales) if senales else 0, 'label': 'Señales en memoria', 'icon': 'bi-hdd-stack'})
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
    filas = core.consultar_senales(q, scope, tipo)
    sc, tp = core.scopes_y_tipos()
    return render(request, 'visor/memoria.html', {
        'q': q, 'scope': scope, 'tipo': tipo,
        'filas': filas, 'scopes': sc, 'tipos': tp,
        'no_db': filas is None, 'db': core.DB,
    })
