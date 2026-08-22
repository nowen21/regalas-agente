# Visor del estándar y de la memoria

App local (Django + Bootstrap 5 + AdminLTE 4) para **leer todo lo que hace el agente** y **ver lo que guarda en la memoria** (`senales.db`).

Es una herramienta compañera, no parte del estándar agnóstico. Corre en tu máquina y lee los archivos y la base **reales**.

## Requisitos

- Python 3.11+. Entorno propio del proyecto, como manda la estructura estándar: `python -m venv interfaz/.venv` y `interfaz/.venv/Scripts/pip install -r interfaz/requirements/lock.txt` (las versiones exactas; `local.txt` para trabajar sobre la base).
- Estáticos de terceros (una sola vez, tras clonar): `python interfaz/descargar_estaticos.py` — los trae pineados por versión y huella SHA-256 a `terceros/`, que no se versiona y que `collectstatic` junta con lo propio de `static/` (`plantillas/estructura-proyecto-django.md`: nada de terceros en el repositorio). **Después de eso funciona sin internet.**
- Migraciones (una sola vez): `python interfaz/manage.py migrate`.

## Cómo está armado

Sigue [plantillas/estructura-proyecto-django.md](../plantillas/estructura-proyecto-django.md), la misma estructura que el estándar le exige a cualquier proyecto Django:

```
interfaz/
├── .venv/ · .env ................ no se versionan
├── .env.example · manage.py
├── requirements/ ................ base.txt · local.txt · lock.txt
├── config/ ...................... settings/ (base.py · local.py) · urls.py · wsgi.py · asgi.py
├── static/cimiento/ ............. SOLO lo propio (visor.css)
├── terceros/ .................... Bootstrap, AdminLTE, iconos, Chart.js (los trae descargar_estaticos.py; no se versiona)
├── staticfiles/ ................. lo que junta collectstatic (no se versiona)
├── templates/ ................... base.html, la plantilla de todo el proyecto
└── cimiento/ .................... el paquete con los módulos, uno por carpeta
    ├── visor/ ................... lee el estándar y la memoria
    └── proyectos/ ............... el registro de proyectos y su medición
```

## Cómo se corre

```
python interfaz/manage.py runserver
```

Luego abrir **http://127.0.0.1:8000** en el navegador.

- Para usar otra base de memoria: `MEMORIA_DB=/ruta/a/senales.db python interfaz/manage.py runserver`.

## Qué muestra

- **Inicio** — resumen (cuántas reglas, roles, plantillas, notas y señales hay).
- **Menú izquierdo** — las reglas base, los roles/skills, las plantillas y las notas, renderizadas.
- **Memoria** — tabla paginada de señales, con **filtro dinámico** (búsqueda por palabra FTS5 + scope + tipo, sin botón), **detalle** al hacer clic en una fila, y **registro** de señales nuevas desde la web.
- **Modo oscuro** — botón en la barra superior (se recuerda).
- **Proyectos** — el registro de los proyectos que usan el estándar: registrar, editar, dar de baja y **medir** (el expediente del ciclo de cada uno, con `validar.py expediente`). Es la fuente de verdad; `plantillas/proyectos.md` se genera desde acá y el instalador lo sigue leyendo.

## Notas

- Es **solo lectura** de la memoria (registrar señales se hace con `memoria/memoria.py`).
- La base de memoria (`memoria/senales.db`) y la base interna de Django (`interfaz/_visor.sqlite3`) no se versionan.
