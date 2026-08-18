# Hecho · Los enlaces de las plantillas apuntan al estándar, no a `../base/`

Origen: pendiente 34.

| | |
|---|---|
| **Quién lo reportó** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/01-los-enlaces-a-las-reglas-nacen-rotos.md` — **avisado el 2026-08-16**. Queda abierto allá hasta que corran el instalador y comprueben |
| **De quién era el defecto** | Del estándar. El proyecto no tocó nada: reportó y siguió con lo suyo |

Cerrado el 2026-08-16, versión **20.0.1**.

## ⚠️ El proyecto comprobó y no está — 2026-08-16

`shopnest-mesa` corrió el instalador y comprobó, que era lo que se le pidió. **El enlace sigue roto.** En su `.agente/stack-instalacion.md`, línea 25, el marcador entró literal:

```
([`02·F13`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F13-…md))
```

Las plantillas quedaron bien —eso sí se hizo—, pero el instalador no reemplaza el marcador al copiar ese archivo dentro del proyecto. Y `enlaces.py`, que en el paso 3 aprendió a resolver el marcador sin llenar contra la raíz, ahora **calla** el enlace en vez de reportarlo. Un aviso ruidoso se cambió por un fallo mudo, que para el proyecto que reportó es peor que como estaba.

Lo que falta está en el [pendiente 40](el-instalador-rellena-los-marcadores.md) —que además encontró que son **tres** los puntos de copia sin rellenar, no uno— y en el [41](el-marcador-se-resuelve-contra-el-estandar.md), que es la pregunta de qué debe hacer `enlaces.py` con un marcador sin llenar dentro de un proyecto. Este archivo se queda acá porque lo suyo —las 22 plantillas— sí se hizo; lo que no se hizo se sigue allá.

---

## Qué era

Las plantillas citan sus reglas con enlace, como pide `20·M15`, y el destino era relativo: `../base/…`. Dentro de este repositorio abre. Pero la plantilla no se queda acá: el instalador la copia dentro de un proyecto, y allá `../base/` es la carpeta que está **encima** del proyecto — nunca el estándar.

Cada proyecto nacía con las citas rotas. En `shopnest-mesa` fueron catorce solo contando el `CLAUDE.md`, los cuatro de `.agente/` y el índice de la memoria. El daño real no eran los enlaces: `hook_md.py` quedaba siempre en rojo, y un aviso que siempre suena se deja de leer — se perdieron fallas reales durante media sesión.

## Qué se hizo

**1 · Los 91 enlaces de las 22 plantillas** pasan de `](../base/` a `](«RUTA-ESTANDAR»/base/`. El marcador ya existía y lo resuelve [`instalar.py · _rellenos()`](../../validadores/instalar.py) contra `RAIZ`, la carpeta donde corre el estándar. No queda escrito a mano en ningún lado: si el estándar se muda, basta reinstalar desde la carpeta nueva.

**2 · [`plantillas.py`](../../validadores/plantillas.py) no necesitó nada.** El pendiente pedía comprobar que no contara el `«…»` de un enlace como hueco sin llenar. No lo cuenta.

**3 · [`enlaces.py`](../../validadores/enlaces.py) sí.** El pendiente decía «en principio el validador la comprueba sin cambios; confirmarlo con una prueba antes de darlo por hecho». La prueba dijo que no: **87 enlaces quedaron dados por rotos**, porque acá el marcador está sin llenar y no resuelve contra nada. Ahora el validador lo conoce — sin llenar, apunta a la raíz del repositorio.

**4 · `CHANGELOG.md` y `VERSION`** — 20.0.1, PARCHE.

## Lo que la prueba corrigió del pendiente

- Eran **91** enlaces en **22** plantillas, no 77 en 21. La cuenta creció entre que se escribió el pendiente y que se ejecutó.
- El paso 3 daba por bueno lo que había que comprobar. Comprobarlo era el trabajo.

## El límite

La ruta que entra al archivo es la de la máquina donde se instaló, y los documentos generados dentro de `documentacion/` e `historico-chat/` **sí se versionan**. En otra máquina ese enlace no abre. No empeora nada —hoy no abre en ninguna—, pero tampoco lo resuelve del todo. Si algún día molesta, la salida es que el instalador reescriba también esos archivos al correr en la máquina nueva.

## El aviso de vuelta

**Escrito el 2026-08-16** en `shopnest-mesa`: su pendiente 01 y la fila de su README dicen que la corrección está hecha, con qué opción se eligió —la 2, que era la que ellos recomendaban—, qué falta de su lado —correr el instalador y comprobar— y el aviso de que el parche local puede quedar mezclado con los enlaces nuevos.

Queda **abierto allá** hasta que lo comprueben. Eso es lo correcto: el aviso no cierra el pendiente del proyecto, lo desbloquea.

**Lo mandó una persona acordándose**, que es el paso 6 que el [pendiente 36](../36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md) todavía no automatiza.
