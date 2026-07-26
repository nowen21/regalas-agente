# Visor del estándar y de la memoria

App local (Django + Bootstrap 5 + AdminLTE 4) para **leer todo lo que hace el agente** y **ver lo que guarda en la memoria** (`senales.db`).

Es una herramienta compañera, no parte del estándar agnóstico. Corre en tu máquina y lee los archivos y la base **reales**.

## Requisitos

- Python 3.11+ y Django 5 (`pip install -r requirements.txt`).
- **Funciona sin internet:** Bootstrap 5, AdminLTE 4, los iconos y Chart.js están incluidos en `visor/static/vendor/`.

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

## Notas

- Es **solo lectura** de la memoria (registrar señales se hace con `memoria/memoria.py`).
- La base de memoria (`memoria/senales.db`) y la base interna de Django (`interfaz/_visor.sqlite3`) no se versionan.
