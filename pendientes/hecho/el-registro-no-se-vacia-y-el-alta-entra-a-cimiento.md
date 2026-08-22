# Pendiente · `plantillas/proyectos.md` se vacía solo y el checklist reprueba el «registro» de proyectos que sí están en Cimiento

**Estado:** cerrado el 2026-08-22 (el mismo día), versión 30.5.0 · anotado 2026-08-22.

| | |
|---|---|
| **Historia de usuario** | EP-007 (instalación) — secuela del [75](los-proyectos-se-administran-desde-cimiento.md): el `.md` pasó a ser generado y el checklist sigue leyendo solo el `.md` |
| **Proyecto de origen** | **gestion de servicios tecnologicos** · `C:\Ing. Jose\Escom\Especialización en ciberseguridad\MODULO 2. SEGURIDAD DE DATOS\gestion de servicios tecnologicos` |
| **Su pendiente de seguimiento** | `pendientes/esperando-correccion-registro-proyectos-md.md` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a **todos los instalados** — cualquier proyecto reprueba «registro» cuando el `.md` se regenera vacío; la lista está en el registro de Cimiento (`interfaz/proyectos/`) |

## El problema

Desde el 75, la fuente de verdad de los proyectos es el registro de Cimiento y `plantillas/proyectos.md` **se genera** desde él (`interfaz/cimiento/proyectos/core.py` · `exportar()`). Pero el checklist (`validadores/checklist.py` · `_registro`, líneas 222-227) y el instalador (`instalar.py` · `instalar_registro`) siguen leyendo **solo el `.md`**. Cuando el `.md` queda sin filas, el proyecto reprueba «registro» aunque esté en Cimiento con ruta, scope y stack correctos.

Y el `.md` **queda vacío solo**: en la sesión del 2026-08-22 se regeneró con las 10 filas desde Cimiento y minutos después (00:31:37) volvió a quedar en 456 bytes — solo la cabecera. Pasó tres veces en la misma sesión. La única función que escribe ese archivo es `exportar()`, que vuelca lo que ve en la base configurada (`config/settings/base.py` → MySQL `cimiento` en `127.0.0.1:3307`). No se identificó qué proceso la dispara entre mensaje y mensaje ni por qué ve cero proyectos activos.

## Cómo se reproduce

Proyecto `gestion de servicios tecnologicos`, estándar v30.3.0:

1. `python validadores/validar.py checklist --raiz "<proyecto>"` → `[FALTA] registro`.
2. `interfaz/.venv/Scripts/python.exe manage.py shell -c "from cimiento.proyectos.models import Proyecto; print(Proyecto.objects.filter(activo=True).count())"` → `10`, y el proyecto está (id 6, scope `proyecto:gestion-servicios-tecnologicos`).
3. `core.exportar()` → escribe las 10 filas; el checklist pasa a `14 de 14`.
4. Minutos después, sin tocar nada, `proyectos.md` vuelve a tener 0 filas y el checklist reprueba otra vez.

Efecto colateral: `instalar.py --aplicar`, al no ver la fila, **anota una provisional** con slug calculado (`gestion-de-servicios-tecnologicos`, distinto del real) y stack «por detectar»; si alguien la "corrige" a mano se pierde en la siguiente exportación.

## Por qué importa

Falso negativo permanente: el agente, obedeciendo al estándar, anuncia en cada respuesta una instalación incompleta que no lo es, y gasta la sesión intentando repararla (esta vez, tres intentos). Un validador que reprueba lo que está bien enseña a ignorar sus veredictos — mismo daño que el [72](../72-el-checklist-compara-los-enganches-sensible-a-mayusculas-de-la-unidad.md).

## Qué falta

1. **Encontrar qué vacía el `.md`**: qué proceso llama a `exportar()` fuera de la interfaz (enganche, servidor corriendo, otra sesión) y contra qué base corre (¿otro `DB_NAME`/entorno sin variables → base distinta y vacía?). Mientras no se sepa, toda regeneración es temporal.
2. **Que el checklist y el instalador lean el registro de Cimiento**, no el `.md` — es la deuda declarada al cerrar el 75 («el instalador todavía escribe sus altas en el `.md`»). Con eso el `.md` deja de ser un punto de falla.
3. Mientras tanto, lo barato: que `exportar()` **no escriba cero filas** si la base devuelve vacío cuando el archivo tenía filas (o que avise), para que un fallo de conexión no borre la lista.

## Cómo cerró

**Se encontró qué lo vaciaba: las pruebas de la propia interfaz.** Las vistas del registro llaman `exportar()`; las pruebas llamaban a las vistas con la base de pruebas (vacía después de una baja), y `exportar()` volcaba esa base sobre el archivo real. Las tres veces coinciden con tres corridas de `manage.py test` en la sesión del estándar. No era otro proceso ni otra base: era el estándar pisándose el pie.

Tres correcciones, con prueba cada una (9 de 9 en verde), y el registro real con sus 10 filas después de correrlas:

1. **Ninguna prueba toca el registro real**: todas corren con el `.md` apuntando a una carpeta temporal.
2. **`exportar()` se niega a vaciar**: si el registro devuelve cero activos y el archivo tenía filas, lanza `RegistroVacio` y no escribe; la pantalla lo dice en vez de borrar.
3. **El alta del instalador entra al registro de Cimiento**: nace `manage.py registrar` y `instalar.py` lo llama cuando la interfaz está instalada (con `.venv` y base); si no, vuelve al `.md` y la interfaz lo importa después. Con esto cierra también la deuda declarada al cerrar el 75.

El checklist sigue leyendo el `.md`, que ahora es confiable: lo genera el registro, nada lo vacía por accidente y el instalador ya no lo escribe a mano. Queda la señal S-019 con la lección: toda prueba que escriba, escribe en temporal; todo exportador se niega a vaciar lo que tenía contenido.

## El límite

Cubre solo el registro de proyectos (componente «registro» del checklist). No toca la estructura de la interfaz ni el contenido del registro, que están bien.
