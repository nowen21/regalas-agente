# Pendiente · Las plantillas enlazan una carpeta `base/` que el proyecto no tiene

**Estado:** abierto · anotado 2026-08-16 · sale de instalar el estándar en `shopnest-mesa` ([pendiente 01 de ese proyecto](../../../../DesarrollosClaude/personales/shopnest-mesa/pendientes/01-los-enlaces-a-las-reglas-nacen-rotos.md), cerrado allá al traspasarlo acá).

## El problema

Las plantillas citan sus reglas con enlace, como pide `M15`. El destino es relativo: `../base/…`.

```
la estructura base ([`02·F13`](../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md))
```

Dentro de este repositorio ese enlace abre. Pero la plantilla no se queda acá: el instalador la copia dentro de un proyecto, y ahí `../base/` es la carpeta que está encima del proyecto. Nunca hay una `base/` en ese sitio — el estándar vive donde diga `RAIZ`, que es otro árbol.

Resultado: **cada proyecto nace con enlaces rotos**, y no son pocos. En `shopnest-mesa` fueron catorce, solo contando `CLAUDE.md`, los cuatro de `.agente/` y el índice de la memoria.

## Por qué importa

El enganche `hook_md.py` revisa los enlaces en cada edición de un `.md` del proyecto. Con esos catorce quedaba **siempre en rojo**, y un aviso que siempre suena se deja de leer: en `shopnest-mesa` se perdieron fallas reales durante media sesión por eso.

Y hay un choque de fondo: `M15` obliga a que toda cita a una regla lleve su enlace. En un proyecto, cumplirla significa escribir a propósito un enlace que no abre.

## Qué falta

**El marcador ya existe y ya es una variable de un solo sitio.** Las plantillas tienen `«RUTA-ESTANDAR»`, y el instalador lo resuelve en [`instalar.py · _rellenos()`](../validadores/instalar.py) a partir de `RAIZ` — la carpeta donde está corriendo el propio estándar. No está escrito a mano en ninguna parte: si el cimiento se muda, basta correr la instalación desde la carpeta nueva y todos los proyectos quedan al día solos.

Falta usarlo en los enlaces:

**1 · Las 21 plantillas** — reemplazar `](../base/` por `](«RUTA-ESTANDAR»/base/`. Son 77 enlaces:

| Plantilla | Enlaces | Plantilla | Enlaces |
|---|---|---|---|
| [`funcionalidad-implementada.md`](../plantillas/funcionalidad-implementada.md) | 16 | [`brief.md`](../plantillas/brief.md) | 4 |
| [`checklist-despliegue.md`](../plantillas/checklist-despliegue.md) | 9 | [`CLAUDE.md.plantilla`](../plantillas/CLAUDE.md.plantilla) | 4 |
| [`mapeo-nombres.md`](../plantillas/mapeo-nombres.md) | 8 | [`HU.md`](../plantillas/HU.md) | 4 |
| [`reglas-proyecto.md`](../plantillas/reglas-proyecto.md) | 5 | [`retrodocumentacion.md`](../plantillas/retrodocumentacion.md) | 3 |
| [`sesion.md`](../plantillas/sesion.md) | 5 | `ADR`, `cierre-analisis`, `fase`, `memoria`, `postmortem` | 2 c/u |

Y con uno cada una: `catalogo-modulos.md`, `epica.md`, `estado-fase.md`, `mapa-dependencias.md`, `marco-normativo.md`, `plantilla-spec-modulo.md`, `stack-instalacion.md`.

**2 · Comprobar [`plantillas.py`](../validadores/plantillas.py)** — si el validador de plantillas cuenta un `«…»` dentro de un enlace como hueco sin llenar, hay que enseñarle que este no lo es. Puede que no haya nada que tocar.

**3 · Comprobar [`enlaces.py`](../validadores/enlaces.py)** — el destino pasa a ser una ruta absoluta de Windows (`C:/…/base/…`). `os.path.join` la resuelve bien, así que en principio el validador la comprueba contra el disco sin cambios. Confirmarlo con una prueba antes de darlo por hecho.

**4 · `CHANGELOG.md` y `VERSION`** — es un cambio de plantillas y el estándar se versiona a sí mismo.

## Las otras dos salidas, y por qué no

Se plantearon tres y la decisión fue la ruta absoluta por marcador. Queda escrito por qué, para no volver a discutirlo:

- **Citar por ID sin enlace.** Es el parche que quedó puesto en `shopnest-mesa` y funciona, pero obliga a acotar `M15` y a quitar 77 enlaces que dentro de este repositorio sí abren.
- **Que el validador resuelva `../base/…` contra la ruta declarada en el `CLAUDE.md` del proyecto.** Callaría al validador sin arreglar el enlace: el humano que haga clic sigue sin llegar a ninguna parte.

## El límite

La ruta que entra al archivo es la de la máquina donde se instaló. Los archivos generados dentro de `documentacion/` y `historico-chat/` **sí se versionan**, así que esa ruta viaja al repositorio y en otra máquina el enlace no abre. No empeora nada —hoy no abre en ninguna—, pero tampoco lo resuelve del todo. Si algún día molesta, la salida es que el instalador reescriba también esos archivos al correr en la máquina nueva.
