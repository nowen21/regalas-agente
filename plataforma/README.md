# La plataforma: cómo se levanta desde cero

Esto es Cimiento corriendo como aplicación: la que va a administrar, documentar y auditar los proyectos. Hoy hace lo mínimo de la fase A: levanta, guarda y lee. Todo lo demás llega en las fases siguientes.

**Corre en su máquina y no sale a la red.** No hay servicio que instalar aparte, ni base de datos que levantar.

## Antes de empezar

| Qué se necesita | Cómo se comprueba |
|---|---|
| Python 3.10 o más nuevo | `python --version` |
| El repositorio clonado | Esta carpeta existe |

## Los pasos

Todos se corren **parado en esta carpeta** (`plataforma/`).

**1 · Crear el ambiente aparte.** Así lo que instale acá no le toca nada más a la máquina.

```
python -m venv .venv
```

**2 · Entrar al ambiente.**

| Sistema | Orden |
|---|---|
| Windows | `.venv\Scripts\activate` |
| Linux o Mac | `source .venv/bin/activate` |

**3 · Instalar lo que necesita.**

```
pip install -r requirements/local.txt
```

**4 · Crear el índice vacío.**

```
python manage.py migrate
```

**5 · Levantarla.**

```
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` en el navegador. Si dice **La plataforma está viva**, quedó.

## Qué quedó en la carpeta

| Qué | Para qué | ¿Va al repositorio? |
|---|---|---|
| `datos/` | **La fuente.** Todo lo que la plataforma guarda, en texto | Sí. El respaldo es el repositorio, no un volcado de la base |
| `indice.sqlite3` | El índice, para buscar rápido | No. Se rehace solo |
| `.venv/` | El ambiente de esta máquina | No |

## Si pierde el índice

No pasa nada, y esa es la idea: el índice no guarda nada que no esté ya en el texto de `datos/`.

```
python manage.py migrate
python manage.py reconstruir_indice
```

## Si quiere ponerle su propia clave de firma

La clave firma las sesiones del navegador en esta máquina. Sin ponerla, la plataforma usa una de desarrollo y funciona igual.

Copie `.env.example` como `.env` y llénela. **El archivo `.env` no entra al repositorio** (`00·N6`): una credencial no se escribe, no se registra y no se guarda.

## Comprobar que todo sirve

```
python manage.py test nucleo
```

Diez comprobaciones. Buena parte mira **lo que no debe pasar**: escribir fuera de `datos/`, o perder información al borrar el índice.

## Qué NO hace todavía

- **No conecta proyectos.** Eso es la fase B.
- **No registra lo que se hace.** Eso es la fase D.
- **No tiene pantallas.** La única ruta que existe es la que dice que está viva.
