# Pendiente · `validar.py secretos` se revisa a sí mismo y reporta sus rutas como del proyecto

**Reportado desde:** el proyecto **`rni-dp`** (`C:/DesarrollosClaude/dp`), el 2026-08-18, al intentar
comprobar que no quedaran secretos en su repositorio.

## Qué pasa

Corrido desde la raíz de ese proyecto, `validar.py secretos` reporta **10 fallas y 8 avisos**. Las 18
apuntan a rutas bajo `C:/DesarrollosClaude/dp/validadores/`.

**Esa carpeta no existe en el proyecto.** Los archivos que reporta —`pruebas.py`, `secretos.py`,
`tests/test_la_clave_no_llega_al_historico.py`— son **los del propio estándar**, en
`C:/Ing. Jose/ia/agente/validadores/`. El recorrido los alcanza y **antepone la raíz del proyecto** a
rutas que no le pertenecen.

Comprobado en el proyecto:

```
$ ls -d validadores
ls: cannot access 'validadores': No such file or directory

$ git ls-files validadores/
(vacío)
```

Y lo que encuentra son **secretos falsos puestos a propósito**: los datos de prueba de
`test_la_clave_no_llega_al_historico.py`, que existe justamente para comprobar que el detector detecta.

## Por qué importa

**Un validador que siempre falla deja de servir para detectar lo nuevo.** Y aquí lo que se deja de ver
son credenciales: si alguien deja una clave en el código de un proyecto, se pierde entre 18 fallas que
nadie lee porque «siempre están».

En `rni-dp` esto **bloquea el cierre de un pendiente de seguridad** —que las claves de ejemplo estén
publicadas—, porque la herramienta con la que se comprobaría no distingue lo suyo de lo ajeno.

## Qué habría que arreglar

Dos cosas, y la segunda importa aunque se haga la primera:

1. **El recorrido debe quedarse dentro de la raíz que recibe**, y no alcanzar la carpeta desde donde
   corre el validador.
2. **Los datos de prueba del propio detector deberían estar exentos.** Un archivo que existe para
   comprobar que el detector detecta va a disparar el detector siempre; si algún día el estándar se
   valida a sí mismo, vuelve el mismo ruido con otra ruta.

## Regla que esto toca

`04·S4` / `N6`. El validador que la hace cumplir es el que hoy no se puede leer.

---

**Nota sobre cómo se enlaza esto de vuelta.** El proyecto lo anotó en su
`documentacion/pendientes/65-el-validador-de-secretos-se-revisa-a-si-mismo.md` **sin enlazar por número
a este archivo**: ya pasó dos veces —con los pendientes 24 y 27 de ese proyecto— que un pendiente del
estándar se archivó con nombre, el número desapareció y el enlace murió sin que nadie se enterara.


---

# Cómo cerró — 2026-08-18

**Las dos cosas que pedía, y la causa no era ninguna de las dos que se sospechaban.**

## La causa: el valor por defecto, no el recorrido

El recorrido nunca salió de su raíz. **Lo que estaba mal era en qué raíz arrancaba.**

`--raiz` caía en `RAIZ`, que es la carpeta del **propio estándar** —se calcula desde `__file__`—. Correr `validar.py secretos` sin `--raiz` revisaba el estándar **desde cualquier sitio**, y devolvía un informe que decía haber revisado.

Ahora los **22 subcomandos que dicen «carpeta del proyecto»** arrancan donde está parado quien los corre. Los que revisan el estándar siguen apuntando a `RAIZ`: ahí sí es lo correcto.

**Y esto no era solo de `secretos`.** Los otros veintiuno tenían el mismo defecto y nadie lo había notado, porque casi siempre se corren desde el propio estándar y ahí las dos raíces coinciden.

## Los datos de prueba del detector, exentos

Nueve de las diez fallas eran las claves falsas de `test_la_clave_no_llega_al_historico.py`, que existen **para comprobar que el detector detecta**.

**Se nombran una por una, no por carpeta.** Exceptuar `tests/` entero dejaría ciego al detector sobre todo lo que se escriba ahí mañana — que es exactamente el agujero por el que se cuela una clave real. Hay un caso de prueba que fija que una clave de verdad sigue saliendo.

## Lo que decía el reporte y hay que subrayar

> *Un validador que siempre falla deja de servir para detectar lo nuevo. Y aquí lo que se deja de ver son credenciales.*

Es la tercera vez hoy que aparece el mismo principio, y en tres sitios distintos: acá, en el ancla de `M1` —*«un control apagado es peor que ninguno porque figura como cubierto»*— y en la decisión de que `brevedad` mida en vez de detener.

## Comprobado

**8 casos** en [`validadores/tests/test_el_validador_no_revisa_lo_ajeno.py`](../../validadores/tests/test_el_validador_no_revisa_lo_ajeno.py), incluidos los dos que importan: que desde una carpeta cualquiera **no** salgan los archivos del estándar, y que una clave real siga reportándose.

`validar.py secretos` sobre el estándar: **0 fallas**.
