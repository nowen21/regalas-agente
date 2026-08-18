# Hecho · Poner al día un proyecto que ya estaba instalado

Origen: pendientes 42 y 44. Se cerraron **juntos** porque son el mismo defecto.

| | |
|---|---|
| **Quién los reportó** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Sus pendientes de seguimiento** | `pendientes/01-los-enlaces-a-las-reglas-nacen-rotos.md` y `pendientes/06-el-checklist-se-queda-en-12-de-13.md` — **avisados el 2026-08-16**, y los dos ya cerrados allá tras comprobar con la v21.2.0 |
| **De quién era el defecto** | Del estándar. El proyecto reportó y siguió con lo suyo |
| **Dónde se construyó** | Fase [`A-EP-007-HU-006-poner-al-dia-lo-ya-instalado`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/) |

Cerrados el 2026-08-16, versión **21.2.0**.

## Qué eran

**El 42.** La [21.1.0](../../CHANGELOG.md) arregló los tres puntos donde el instalador copiaba sin rellenar los huecos. Pero la huella con la que decide si hay trabajo sale del molde central, no del archivo copiado: el molde no cambió, así que a los proyectos ya instalados les dijo «ya estaba al día» y no los tocó. Reinstalar no reparaba, y no había bandera que forzara.

**El 44.** El registro de `documentacion/versiones/` se escribía solo si alguna huella cambiaba. Cuando el estándar subía de versión sin tocar ningún molde del proyecto, el instalador decía «nada que registrar» y la revisión decía «falta el registro». El proyecto quedaba en 12 de 13 para siempre, con el aviso de instalación incompleta sonando en cada mensaje — y la única salida era editar a mano un archivo que dice que no se edita a mano.

**Por qué son el mismo.** Los dos son el instalador decidiendo si hay trabajo por una huella, y quedándose corto cuando la huella no cambia.

## Qué se hizo

| Pendiente | Salida elegida | Descartadas |
|---|---|---|
| 42 | Toda copia que ya existe pasa por `_reparar_marcadores`: rellena en el sitio lo que quedó crudo y no toca nada más | La bandera `--forzar` y calcular la huella del archivo copiado |
| 44 | Subir de versión es por sí solo motivo de registro | Que la revisión dejara de reprobar |

Además se corrigió el texto de ayuda de la fila `versiones`, que decía «Escribe un registro cada vez que algo cambia de huella» — o sea, mandaba hacer lo que el instalador ya había hecho.

**Lo que no se toca.** `_rellenar` solo conoce los huecos que el instalador sabe calcular. Un hueco que llena el proyecto —`«motor»`, `«manual / pipeline»`— sale intacto, y hay un caso de prueba que cuenta los huecos antes y después para comprobarlo.

## Cómo se sabe que quedó

Seis casos de prueba en [`validadores/tests/test_instalar_reparar.py`](../../validadores/tests/test_instalar_reparar.py), todos en verde. Los cinco automáticos corren contra una copia desechable del estándar, para poder editarle un molde y subirle la versión sin tocar el de verdad.

**El sexto lo corrió `shopnest-mesa`**, que es quien reportó los dos defectos: instaló la v21.2.0, comprobó que el enlace de su línea 25 abre y que llegó a 13 de 13, y cerró sus dos pendientes. Vale más así — el que reporta es el que dice si el defecto desapareció.

**Se le avisó el 2026-08-16**, y de paso se le corrigió una conclusión: había entendido que el 42 cerró «de rebote», porque en la misma versión cambió la huella de la plantilla del stack, y que *«un proyecto ya instalado solo se repara si la plantilla cambia de huella»*. No es así: `_reparar_marcadores` repara sin que cambie ninguna huella, y hay un caso que lo comprueba ensuciando una copia **sin tocarle el sello**.

**Que el aviso haya salido a mano sigue siendo el [pendiente 36](el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md)**, y este caso es su tercera prueba: el arreglo bajó con la versión antes que el aviso, y el proyecto lo descubrió solo.
