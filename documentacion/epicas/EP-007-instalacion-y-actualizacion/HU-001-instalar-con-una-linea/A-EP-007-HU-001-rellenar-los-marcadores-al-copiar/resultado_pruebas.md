# Resultado de Pruebas — Fase «A-EP-007-HU-001-rellenar-los-marcadores-al-copiar»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-007-HU-001-rellenar-los-marcadores-al-copiar` |
| **HU** | [HU-001 — Instalar con una línea](../HU-001-instalar-con-una-linea.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 21.0.0 · carpetas temporales desechables |

**Con qué se corre:**

```
python -m unittest discover -s validadores/tests
```

**Decisión que el plan no declaraba:** no hay pytest instalado ni prueba alguna en el repositorio, así que se usó `unittest`, de la biblioteca estándar de Python. Es lo que sostiene el requisito de autonomía de la épica —correr sin internet y sin instalar nada—, y no obliga a nadie a preparar la máquina antes.

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 2 | 2 | 0 | 0 |
| 2 | 4 | 4 | 4 | 0 | 0 | 0 |

Cada caso corre **dos veces**, una por cada carpeta de prueba: la de nombre normal y la de nombre con espacio y tilde (el CP-004). Por eso `unittest` reporta 6 pruebas y no 4.

**Casos no ejecutados y por qué:** ninguno.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — que lo que el instalador sabe llenar llegue lleno

**El problema que resuelve:** si un marcador viaja crudo al proyecto, la cita a una regla no abre. Es exactamente lo que reportó `shopnest-mesa`, y lo que hacía que la instalación se declarara completa con un documento a medias adentro.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Situarse en `c:\Ing. Jose\ia\agente` | El repositorio responde | Sobre `VERSION` 21.0.0 |
| 2 | Crear una carpeta temporal vacía con `tempfile.mkdtemp` | La carpeta existe y no tiene nada | `C:\Users\...\Temp\cimiento-4bltwr97\proyecto de prueba`, vacía |
| 3 | Correr `instalar.instalar(nombre, ruta, aplicar=True)` | Termina sin preguntar nada | Terminó: «Instalación del agente completa — 13 de 13» |
| 4 | Listar los `.md` que quedaron dentro | Sale la lista, con el `CLAUDE.md`, el stack, los 4 de `.agente/` y el índice de memoria | Salieron los 8 esperados |
| 5 | Buscar en cada uno los marcadores de `_rellenos()` | Ninguno los contiene | **Ciclo 1: 65 líneas marcadas.** Ciclo 2: ninguna |
| 6 | Borrar la carpeta temporal | Queda borrada | Borrada |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que decide, y en el ciclo 1 salió rojo — pero no por el defecto que la fase venía a arreglar. El criterio del plan §2.6 decía «que no quede **ningún** `«…»`», y eso mezcla dos huecos distintos: el que llena el instalador y el que llena el proyecto después. Las 65 líneas eran de los 4 archivos de `.agente/`, que llegan con huecos **a propósito** —a qué se dedica el negocio, quién usa el sistema— y que nadie puede responder desde afuera. Se pausó la ejecución, se reportó al usuario y **él aprobó corregir el criterio** ([`02·F8`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)): la prueba comprueba ahora solo los marcadores de `_rellenos()`, que es la lista de lo que el instalador se comprometió a llenar. Al salir de esa lista y no de una escrita a mano, sigue cubriendo el marcador que se agregue mañana, que era el motivo de la decisión original.

El paso 4 no es de adorno: sin él, una instalación que no escribiera nada pasaría el paso 5 con cero marcadores y el caso quedaría verde sin haber instalado nada.

### CA-01 · CP-002 — que el enlace instalado abra la regla

**El problema que resuelve:** que la ruta esté escrita no prueba que lleve a alguna parte. Un enlace a una carpeta que no existe se ve igual de bien en el texto.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar en una carpeta temporal y **no** borrarla | Queda el proyecto instalado | `C:\Users\...\Temp\cimiento-manual-fbg0pas_\proyecto de prueba` |
| 2 | Abrir `.agente/stack-instalacion.md` y sacar sus enlaces a `.md` | Sale al menos uno | 1 enlace |
| 3 | Comprobar en disco si el destino existe | Existe | `ABRE C:/Ing. Jose/ia/agente/base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md` |
| 4 | Repetir con **todos** los `.md` del proyecto instalado | Ninguno roto | 19 enlaces revisados, **0 rotos** |
| 5 | Borrar la carpeta temporal | Queda borrada | Borrada |

**Cómo se verificó que la pareja cumple:** el paso 3 es el que cierra el reporte del proyecto — ese enlace, el de `F13` en el `stack-instalacion.md`, es literalmente el que llegó roto y el que motivó el pendiente 40. El paso 4 amplía a los 19 enlaces del proyecto entero, porque arreglar uno y romper otro sería el mismo defecto con otra cara. La comprobación se hace mirando el disco, que es una fuente distinta de la que escribió el archivo.

### CA-02 · CP-003 — que reinstalar no cambie lo que ya estaba bien

**El problema que resuelve:** una instalación que se pisa a sí misma borra lo que el proyecto ya había llenado. La instalación corre al abrir cada sesión, así que pasaría todos los días.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Instalar en una carpeta temporal vacía | Termina | «13 de 13» |
| 2 | Guardar el contenido de cada `.md` instalado | Queda el registro del antes | 8 archivos guardados |
| 3 | Correr la instalación otra vez sobre la misma carpeta | Termina sin preguntar | Terminó; todos los pasos dijeron «ya estaba» o «ya estaba al día» |
| 4 | Comparar archivo por archivo contra el registro del paso 2 | Ninguno cambió | Ninguno cambió |
| 5 | Buscar otra vez los marcadores de `_rellenos()` | Ninguno | Ninguno |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide. El 5 va aparte a propósito: un archivo podría quedar igual y traer el marcador desde la primera corrida, así que «no cambió» y «no tiene huecos» son dos cosas distintas y se comprueban por separado.

### RNF Compatibilidad · CP-004 — que la ruta con espacios y tildes se escriba entera

**El problema que resuelve:** el repositorio del estándar vive en `c:\Ing. Jose\ia\agente`, con espacio y con tilde. Si el relleno se rompiera con eso, se rompería en la máquina donde se desarrolla y nadie lo notaría hasta instalar en otra parte.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear la carpeta temporal `proyecto de prueba ñ` | La carpeta existe | Existe |
| 2 | Correr los tres casos anteriores sobre ella | Dan lo mismo que en la carpeta de nombre normal | Los tres dieron igual |
| 3 | Leer la ruta que quedó escrita en un archivo instalado | Está completa, con su espacio y su tilde | `C:/Ing. Jose/ia/agente/base/...`, entera |

**Cómo se verificó que la pareja cumple:** el caso se implementó heredando la clase de los otros tres y cambiándole solo el nombre de la carpeta, así que corre exactamente las mismas comprobaciones. Si el nombre influyera, alguna de las tres saldría distinta.

### La prueba no es vacía

Una prueba que pasa siempre no comprueba nada. Se le devolvió a `instalar` el comportamiento viejo —`_rellenar` devolviendo el texto tal cual— y se corrió el CP-001:

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Reemplazar `_rellenar` en memoria por una que no rellena | El defecto queda puesto, sin tocar el repositorio | Reemplazada |
| 2 | Correr el CP-001 | Se pone rojo y nombra los marcadores | Rojo: `CLAUDE.md:12 — «RUTA-ESTANDAR»` y 11 más |

Sin este paso, el «aprobado» del CP-001 no distingue entre «el arreglo funciona» y «la prueba no mira nada».

**Correspondencia con el plan:** 4 casos en el plan, 4 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** en el ciclo 1, el CP-001 y el CP-003 fallaron por el criterio mal escrito, no por el código. Está explicado arriba y en §4 como `DEF-01`.

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-08-16 | Instalación completa en `…\cimiento-4bltwr97\proyecto de prueba`; se buscaron los 17 marcadores de `_rellenos()` en los 8 `.md` copiados: 0 apariciones | Aprobado | EV-01 | DEF-01 (ciclo 1) |
| CP-002 | CA-01 | Crítica | 2026-08-16 | 19 enlaces `.md` del proyecto instalado resueltos contra el disco; el de `F13` del `stack-instalacion.md` abre en `C:/Ing. Jose/ia/agente/base/…` | Aprobado | EV-03 | — |
| CP-003 | CA-02 | Alta | 2026-08-16 | Segunda corrida sobre la misma carpeta: los 8 archivos idénticos byte a byte, 0 marcadores | Aprobado | EV-02 | DEF-01 (ciclo 1) |
| CP-004 | RNF Compat. | Alta | 2026-08-16 | Los tres casos repetidos sobre `proyecto de prueba ñ`: mismo resultado | Aprobado | EV-01 | — |

---

## 3. Verificaciones manuales  ·  [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el enlace del `stack-instalacion.md` instalado lleve a la regla | Instalando en carpeta temporal y resolviendo el destino contra el disco | **Abre.** Es el enlace que el proyecto reportó roto |
| 2 | Que ningún otro enlace del proyecto instalado quede roto | Recorriendo los 19 enlaces `.md` de los 8 archivos | 0 rotos |
| 3 | Que la prueba se ponga roja con el defecto puesto | Reemplazando `_rellenar` en memoria y corriendo el CP-001 | Se pone roja y nombra cada marcador |

**Lo que no se verificó:** hacer clic desde un editor. Se comprobó que el archivo destino existe, que es lo que decide si el clic llega; que el editor lo abra depende del editor, no del estándar.

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | El criterio del plan mezclaba el hueco que llena el instalador con el que llena el proyecto | CP-001, CP-003 | Alta | Corregido | Acá, §2, y en la corrección de la prueba aprobada por el usuario |

**Defectos abiertos que se aceptan y por qué:** ninguno.

**El DEF-01 no era del código, era del plan.** Vale la pena que quede escrito: la fase se detuvo, se reportó y el usuario aprobó cambiar el criterio antes de tocarlo. Cambiarlo en silencio para que la prueba pasara habría dejado un criterio que nadie acordó.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01 — Una línea deja el proyecto listo](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | CP-001, CP-002 | Los 8 archivos copiados llegan sin marcadores del instalador y sus 19 enlaces abren | **Sí** |
| [CA-02 — Correrla dos veces no rompe nada](../HU-001-instalar-con-una-linea.md#ca-02--correrla-dos-veces-no-rompe-nada) | CP-003 | La segunda corrida deja los 8 archivos idénticos | **Sí** |
| RNF — Compatibilidad (rutas con espacios y tildes) | CP-004 | Mismo resultado en la carpeta con espacio y tilde | **Sí** |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 3 de 3 con caso | Sí |
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| Archivos instalados con marcador del instalador | Plan §12 | 0 | 0 | Sí |
| Corrida quirúrgica, no la suite entera | Plan §3.5 | Solo lo de la fase | Solo `validadores/tests/` | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los dos criterios de aceptación y el requisito no funcional quedaron verdes con evidencia, en la segunda ejecución. El enlace concreto que un proyecto reportó roto ahora abre, y los otros 18 del proyecto instalado también. La prueba que faltaba existe, corre sola y se comprobó que se pone roja si el defecto vuelve.

**Qué falta para que cumpla:** nada. Queda pendiente el cierre documental y el `CHANGELOG`, que son estaciones posteriores, no criterios.

**Lo que esta fase no arregla, y está declarado:** los 4 archivos de `.agente/` no se pisan una vez creados, así que un proyecto instalado **antes** de este cambio conserva sus marcadores crudos. Es el riesgo `B-01` del plan y se avisa en el `CHANGELOG`.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de `python -m unittest discover -s validadores/tests` | `Ran 6 tests in 1.583s · OK` |
| EV-02 | Comparación antes/después de la segunda corrida | Dentro del CP-003, en `test_instalar_marcadores.py` |
| EV-03 | Recorrido de los 19 enlaces del proyecto instalado | `enlaces .md revisados: 19 | rotos: 0` |
| EV-04 | Corrida con el defecto reintroducido | `el instalador dejó marcadores suyos sin llenar: CLAUDE.md:12 — «RUTA-ESTANDAR»` (+11) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-16 | 2 | 2 | Primera ejecución. El CP-001 y el CP-003 fallaron por el criterio del plan, que daba por defecto los huecos que el proyecto llena después |
| 2 | 2026-08-16 | 4 | 0 | Con el criterio corregido y aprobado: se comprueban solo los marcadores de `_rellenos()` |
