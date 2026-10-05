# Cimiento

La aplicación Django donde se junta lo que hace Cimiento. Guarda en MariaDB y sus pantallas usan Tabler, htmx y ApexCharts. Cada módulo se agrega en `core/` cuando su historia de usuario se aprueba.

## Cómo se levanta

Hace falta MariaDB prendida. Todos los pasos se corren en esta carpeta. Instalar el estándar hace los pasos 3, 5 y 6 por su cuenta.

| Paso | Orden |
|---|---|
| 1 · Crear el ambiente | `python -m venv .venv` |
| 2 · Entrar al ambiente (Windows) | `.venv\Scripts\activate` |
| 2 · Entrar al ambiente (Linux o Mac) | `source .venv/bin/activate` |
| 3 · Instalar lo que necesita | `pip install -r requirements/local.txt` |
| 4 · Copiar la configuración de la máquina | copiar `.env.example` como `.env` y llenarlo, con la conexión a MariaDB |
| 5 · Instalar lo de las pantallas | `npm ci` |
| 6 · Crear la base y sus tablas | `python manage.py preparar_base` |
| 7 · Crear la primera cuenta | `python manage.py createsuperuser` |
| 8 · Levantar | `python manage.py runserver` |

Las demás cuentas se crean con `python manage.py crear_cuenta --usuario «nombre» --grupo administrador` o `--grupo consulta`; la contraseña se pide dos veces y no se muestra. El grupo consulta solo mira; el administrador, o un superusuario, cambia.

Abrir en el navegador `http://127.0.0.1:«PUERTO del .env»/` y entrar con la cuenta. Si aparece el menú lateral con «Inicio» y la línea que dice a qué base está conectado, quedó. Si MariaDB está apagada, la página lo dice.

**El gasto de tokens llega en vivo mientras Cimiento está prendido.** La instalación del estándar le dice a Claude Code que mande cada llamada a `http://127.0.0.1:«PUERTO del .env»/v1/logs`, así que Cimiento tiene que levantarse con `runserver` sin número, en ese puerto. Lo que llegue con Cimiento apagado lo recupera `python manage.py leer_consumo`, que la instalación programa una vez al día.

## Cómo está organizado

| Carpeta | Qué guarda |
|---|---|
| `config/` | La configuración: `settings/base.py` (lo común) y `settings/local.py` (lo del equipo de desarrollo), las rutas y los puntos de entrada |
| `core/` | Los módulos: uno por carpeta, cada uno una aplicación de Django con su modelo, sus vistas, sus pruebas y sus migraciones |
| `requirements/` | Las dependencias: `base.txt`, `local.txt` y `lock.txt` con las versiones exactas |
| `package.json` | Lo que las pantallas usan en el navegador, con `package-lock.json` y las versiones exactas |
| `static/` · `templates/` | Lo propio del proyecto para el navegador |

La estructura es la de `plantillas/estructura-proyecto-django.md` del estándar.

## Cómo se prueba

```
python manage.py test core
```
