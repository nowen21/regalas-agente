# Cimiento

La aplicación Django donde se junta lo que hace Cimiento. Hoy es la base del proyecto, sin módulos: cada uno se agrega en `core/` cuando su historia de usuario se aprueba.

## Cómo se levanta

Todos los pasos se corren en esta carpeta.

| Paso | Orden |
|---|---|
| 1 · Crear el ambiente | `python -m venv .venv` |
| 2 · Entrar al ambiente (Windows) | `.venv\Scripts\activate` |
| 2 · Entrar al ambiente (Linux o Mac) | `source .venv/bin/activate` |
| 3 · Instalar lo que necesita | `pip install -r requirements/local.txt` |
| 4 · Copiar la configuración de la máquina | copiar `.env.example` como `.env` y llenarlo |
| 5 · Crear la base | `python manage.py migrate` |
| 6 · Levantar | `python manage.py runserver` |

Abrir `http://127.0.0.1:8000/admin/` en el navegador. Si aparece la entrada del administrador de Django, quedó.

## Cómo está organizado

| Carpeta | Qué guarda |
|---|---|
| `config/` | La configuración: `settings/base.py` (lo común) y `settings/local.py` (lo del equipo de desarrollo), las rutas y los puntos de entrada |
| `core/` | Los módulos: uno por carpeta, cada uno una aplicación de Django con su modelo, sus vistas, sus pruebas y sus migraciones |
| `requirements/` | Las dependencias: `base.txt`, `local.txt` y `lock.txt` con las versiones exactas |
| `static/` · `templates/` | Lo propio del proyecto para el navegador |

La estructura es la de `plantillas/estructura-proyecto-django.md` del estándar.

## Cómo se prueba

```
python manage.py test core
```
