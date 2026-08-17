# Funcionalidad implementada — Fase «A-EP-007-HU-006-poner-al-dia-lo-ya-instalado»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho al final**, para no tener que reconstruirlo leyendo el plan y el resultado de pruebas por separado. El plan dice qué se iba a hacer y no se toca; esto dice qué se hizo.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-007-HU-006-poner-al-dia-lo-ya-instalado` |
| **Épica / HU** | [EP-007](../../epica.md) · [HU-006](../HU-006-poner-al-dia.md) |
| **Versión publicada** | [21.2.0](../../../../../CHANGELOG.md) — 2026-08-16 |
| **De dónde salió** | Pendientes 42 y 44, reportados por `shopnest-mesa` → [hecho](../../../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md) |

---

## 1. Qué hace ahora que antes no hacía

**Un proyecto ya instalado se pone al día corriendo el instalador.** Sin banderas, sin editar nada a mano.

| Antes | Ahora |
|---|---|
| Una copia mal escrita se quedaba así para siempre, porque su sello coincidía con la plantilla central y el instalador ni la abría | Toda copia que ya existe pasa por `_reparar_marcadores`: se le rellenan los huecos que quedaron crudos y no se toca nada más |
| Si el estándar subía de versión sin cambiarle ninguna plantilla al proyecto, no se escribía registro y la revisión reprobaba `versiones` — sin salida | Subir de versión es por sí solo motivo de registro. El proyecto llega a 13 de 13 |
| El texto de ayuda decía «Escribe un registro cada vez que algo cambia de huella», que es lo que el instalador ya había hecho | Dice que corriendo el instalador queda el registro que falte, y por qué dos motivos se escribe |

---

## 2. Dónde quedó

| Archivo | Qué cambió |
|---|---|
| [`validadores/instalar.py`](../../../../../validadores/instalar.py) | `_reparar_marcadores` nuevo; lo usan `instalar_stack`, `instalar_agente_config` y `_refrescar_sello`. `registrar_version` registra también por subida de versión, y exime a la carpeta del propio estándar |
| [`plantillas/stack-instalacion.md`](../../../../../plantillas/stack-instalacion.md) | El texto de arreglo de la fila `versiones` |
| [`validadores/tests/test_instalar_reparar.py`](../../../../../validadores/tests/test_instalar_reparar.py) | La suite de esta fase, 6 casos |
| [`validadores/tests/test_instalar_marcadores.py`](../../../../../validadores/tests/test_instalar_marcadores.py) | Apunta el registro central a una copia desechable — ampliación del plan aprobada por el usuario |
| [`validadores/docs/instalar.md`](../../../../../validadores/docs/instalar.md) | La función nueva, el motivo doble del registro y el orden de la instalación |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) | La 21.2.0 |

---

## 3. Qué se probó

Seis casos, todos ✅ — el detalle en [`resultado_pruebas.md`](resultado_pruebas.md).

Los cinco automáticos corren contra una **copia desechable del estándar**, porque dos de ellos necesitan editarle una plantilla y subirle la versión, y eso no se hace sobre el estándar de verdad ([`00·N4`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

El sexto lo ejecutó **`shopnest-mesa`**, que es quien reportó los dos defectos: corrió el instalador con la 21.2.0 y comprobó que el enlace de la línea 25 abre y que llegó a 13 de 13. Verificado además desde acá leyendo sus archivos, sin escribir nada en su proyecto.

**Los dos defectos que salieron eran de la prueba, no del cambio:** un caso que ensuciaba un archivo que no citaba al estándar, y `instalar()` reventando al imprimir una flecha sin que nadie hubiera preparado la salida.

---

## 4. Qué quedó fuera, y dónde vive

| Qué | Dónde |
|---|---|
| La especificación del módulo de instalación | Deuda heredada de la fase [`A-EP-007-HU-001`](../../HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md) (§10, `B-02`) |
| Que `instalar()` prepare su propia salida en vez de depender de `main()` | Reportado al usuario; sin pendiente todavía |
| Que el aviso al proyecto de origen salga solo | [Pendiente 36](../../../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md). Esta fase volvió a avisar a mano: es su tercera prueba |

---

## 5. Lo que esta fase deja aprendido

- **Dos pendientes que son el mismo defecto se cierran en una sola fase.** El 42 y el 44 eran la misma decisión de `instalar.py` vista por dos puertas; separarlos habría dejado dos parches.
- **«Al día» contra la plantilla no significa «bien escrito».** Son dos preguntas distintas, y el instalador solo hacía una.
- **El veredicto de un arreglo del instalador no lo da el instalador.** Lo dio `checklist` en el CP-004, y lo dio el proyecto que reportó en el CP-006.
- **Una prueba que necesita que el estándar cambie se hace contra una copia desechable.** De paso deja de ensuciar el registro central, que era lo que la suite anterior venía haciendo sin que nadie lo mirara.
