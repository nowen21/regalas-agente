# Visor del estándar y de la memoria

App local (Django + Bootstrap 5 + AdminLTE 4) para **leer todo lo que hace el agente** y **ver lo que guarda en la memoria** (`senales.db`).

Es una herramienta compañera, no parte del estándar agnóstico. Corre en tu máquina y lee los archivos y la base **reales**.

## Requisitos

- Python 3.11+ y Django 5 (`pip install -r requirements.txt`).
- Conexión a internet la primera vez (Bootstrap y AdminLTE se cargan por CDN).

## Cómo se corre

```
python interfaz/manage.py runserver
```

Luego abrir **http://127.0.0.1:8000** en el navegador.

- Para usar otra base de memoria: `MEMORIA_DB=/ruta/a/senales.db python interfaz/manage.py runserver`.

## Qué muestra

- **Inicio** — resumen (cuántas reglas, roles, plantillas, notas y señales hay).
- **Menú izquierdo** — las reglas base, los roles/skills, las plantillas y las notas, renderizadas.
- **Memoria** — las señales guardadas, con **búsqueda por palabra** (FTS5) y **filtro por scope y tipo**.

## Notas

- Es **solo lectura** de la memoria (registrar señales se hace con `memoria/memoria.py`).
- La base de memoria (`memoria/senales.db`) y la base interna de Django (`interfaz/_visor.sqlite3`) no se versionan.
