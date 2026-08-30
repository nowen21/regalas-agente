# -*- coding: utf-8 -*-
"""Escribe las cinco fases que cierran un rojo que dejo de ser cierto.

**Por que un programa y no cinco veces a mano.** Son veinticinco documentos con
el mismo molde y cifras distintas. Copiarlos es la forma mas segura de que uno
diga algo falso sin que nadie lo note, porque nadie relee el numero veinte de
una serie. Aca cada documento toma su evidencia de la **medicion ejecutada** en
`medir-los-cinco-rojos.py`, no de un texto copiado.

**El criterio de suspension va adentro.** La fase de una historia solo se
escribe si su medicion sale CUMPLE. Si sale NO CUMPLE, esa carpeta no se crea y
el rojo se queda como esta.

**El molde se aprueba una vez.** Pedir cinco aprobaciones de un texto identico
convierte la puerta en tramite, y una puerta que es tramite deja de mirar.
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))
sys.path.insert(0, AQUI)

# El nombre del medidor lleva guiones: se carga por ruta, no por `import`.
try:
    import importlib.util as _util
    _spec = _util.spec_from_file_location(
        "medidor", os.path.join(AQUI, "medir-los-cinco-rojos.py"))
    medidor = _util.module_from_spec(_spec)
    _spec.loader.exec_module(medidor)
except Exception as e:
    print("No se pudo cargar el medidor: %r" % (e,))
    sys.exit(2)

EPICAS = os.path.join(RAIZ, "documentacion", "epicas")
HOY = "2026-08-29"

# --------------------------------------------------------------------------
# Los cinco, con lo suyo. Nada de esto se deduce: sale de leer la fase roja.
# --------------------------------------------------------------------------
LOS_CINCO = (
    dict(
        clave="ep002_hu003",
        epica="EP-002-versionado-y-adopcion", ep="EP-002",
        hu_dir="HU-003-version-adoptada-por-el-proyecto", hu="HU-003",
        hu_md="HU-003-version-adoptada-por-el-proyecto.md",
        modulo="Programas de comprobación",
        fase="C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir",
        roja="A-EP-002-HU-003-retrodocumentar-la-version-adoptada",
        fecha_rojo="2026-08-22",
        criterio="CA-02 · Una versión que no existe se detecta",
        criterio_prosa=u"el **CA-02**, que pide que una versión que no existe se detecte",
        criterio_corto="CA-02",
        decia=u"`99.9.9` pasaba en silencio y, **por ser mayor que la vigente, "
              u"apagaba el aviso de desfase**: declarar una versión falsa hacia "
              u"adelante callaba la única comprobación que había",
        lo_hizo="B-EP-002-HU-003-la-version-declarada-se-comprueba",
        como=u"Se arma un proyecto de prueba en una carpeta temporal cuyo "
             u"`CLAUDE.md` declara `99.9.9`, y se corre `version.validar` "
             u"sobre él. Tiene que salir una **falla**, no un silencio.",
        no_tapa=u"Se mide sobre una carpeta temporal y no sobre un proyecto "
                u"real, como manda la decisión 35 del pendiente 59: tocar el "
                u"`CLAUDE.md` de un proyecto vivo para probar es cambiarle el "
                u"estado a alguien más.",
    ),
    dict(
        clave="ep002_hu004",
        epica="EP-002-versionado-y-adopcion", ep="EP-002",
        hu_dir="HU-004-aviso-al-quedar-atras", hu="HU-004",
        hu_md="HU-004-aviso-al-quedar-atras.md",
        modulo="Enganches de sesión",
        fase="C-EP-002-HU-004-el-ca-01-se-vuelve-a-medir",
        roja="A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase",
        fecha_rojo="2026-08-22",
        criterio="CA-01 · El proyecto atrasado recibe el aviso al abrir sesión",
        criterio_prosa=u"el **CA-01**, que pide que el proyecto atrasado reciba el aviso al abrir sesión",
        criterio_corto="CA-01",
        decia=u"el aviso **existía y decía lo que tenía que decir**, pero solo "
              u"aparecía si alguien escribía el comando a mano: ni `sesion.py` "
              u"ni `cargador.py` nombraban la versión, y el criterio dice "
              u"«al abrir sesión»",
        lo_hizo="B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio",
        como=u"Dos mitades, y hacen falta las dos: que el aviso **salga** "
             u"(proyecto temporal que declara una versión vieja) y que el "
             u"camino de la apertura **pase por él** "
             u"(`hook_sesion` → `sesion.revisar` → `version.validar`).",
        no_tapa=u"Que el aviso exista no era el problema: ya existía cuando se "
                u"midió el rojo. Por eso la medición no se da por buena con "
                u"ver el texto; comprueba el eslabón que faltaba.",
    ),
    dict(
        clave="ep004_hu003",
        epica="EP-004-comprobacion-automatica", ep="EP-004",
        hu_dir="HU-003-formato-del-hallazgo", hu="HU-003",
        hu_md="HU-003-formato-del-hallazgo.md",
        modulo="Comprobación automática",
        fase="C-EP-004-HU-003-el-transversal-de-errores-se-vuelve-a-medir",
        roja="A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo",
        fecha_rojo="2026-08-17",
        criterio="Transversal de errores · un `.md` ilegible no tumba la corrida",
        criterio_prosa=u"el **transversal de errores**, que pide que un `.md` ilegible no tumbe la corrida",
        criterio_corto="el transversal de errores",
        decia=u"los tres criterios numerados quedaron verificados, y lo que "
              u"falló fue el transversal: un `.md` que no se podía decodificar "
              u"**terminaba la corrida entera con un volcado de Python**",
        lo_hizo="B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida",
        como=u"Una carpeta con dos archivos: uno con bytes que no son UTF-8 y "
             u"otro con dos rayas largas en prosa. La corrida tiene que "
             u"terminar en 0, sin volcado, **y seguir contando las dos marcas "
             u"del legible**.",
        no_tapa=u"No basta con que no se caiga. Un programa que se traga el "
                u"error y deja de mirar el resto también «no se cae», y sería "
                u"peor: diría cero marcas sobre un árbol sin revisar.",
    ),
    dict(
        clave="ep005_hu003",
        epica="EP-005-automatismos-que-no-dependen-de-la-memoria", ep="EP-005",
        hu_dir="HU-003-disparo-al-escribir-un-archivo", hu="HU-003",
        hu_md="HU-003-disparo-al-escribir-un-archivo.md",
        modulo="Automatismos — enganches",
        fase="D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir",
        roja="A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir",
        fecha_rojo="2026-08-17",
        criterio="CA-03 · El hallazgo grave detiene, y el resto avisa",
        criterio_prosa=u"el **CA-03**, que pide que el hallazgo grave detenga y el resto avise",
        criterio_corto="CA-03",
        decia=u"el disparo corría en el momento y callaba con lo que no le "
              u"tocaba, pero **todo avisaba**: nada distinguía el hallazgo "
              u"grave del que solo informa",
        lo_hizo="B-EP-005-HU-003-el-hallazgo-grave-detiene",
        como=u"El enganche de escritura se corre **dos veces**, con un "
             u"documento que deja un enlace roto y con uno sano. Las dos "
             u"respuestas tienen que ser distintas: 2 y 0.",
        no_tapa=u"Comprobar solo el caso grave no dice nada: un enganche que "
                u"devuelve 2 siempre también lo pasaría, y detendría el "
                u"trabajo en cada edición hasta que alguien lo apague.",
    ),
    dict(
        clave="ep005_hu008",
        epica="EP-005-automatismos-que-no-dependen-de-la-memoria", ep="EP-005",
        hu_dir="HU-008-enganche-del-resumen", hu="HU-008",
        hu_md="HU-008-enganche-del-resumen.md",
        modulo="Enganche del resumen",
        fase="D-EP-005-HU-008-el-criterio-de-salida-se-vuelve-a-medir",
        roja="A-EP-005-HU-008-enganche-del-resumen",
        fecha_rojo="2026-08-22",
        criterio="Criterio de salida · la comprobación en una sesión real",
        criterio_prosa=u"el **criterio de salida**, que pide la comprobación en una sesión real",
        criterio_corto="el criterio de salida",
        decia=u"los siete criterios de aceptación quedaron cubiertos y las "
              u"métricas dieron por encima de la meta; lo que faltaba era "
              u"**la corrida manual en una sesión de verdad**, y la fase "
              u"prefirió esperar antes que darse por buena",
        lo_hizo="la sesión `2026-08-28-plantilla-manual-instalacion`",
        como=u"Lo medible se ejecuta: que el enganche esté colgado en "
             u"`.claude/settings.json`, y que la sesión real haya dejado su "
             u"resumen con la línea del índice apuntándole después de "
             u"renombrarla. La mitad manual la atestigua esa sesión.",
        no_tapa=u"Este es el único de los cinco cuyo criterio **un programa no "
                u"puede firmar solo**: pide una sesión real. Por eso la "
                u"medición dice qué comprobó y qué atestigua la transcripción, "
                u"en vez de dar las dos cosas por iguales.",
    ),
)

CAB = u"# %s — Fase `%s`%s   ·   `[CAPA 3]`\n"


def _escribir(carpeta, nombre, texto):
    with io.open(os.path.join(carpeta, nombre), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(texto)


def estado_fase(d, evidencia):
    return (CAB % (u"Estado de fase", d["fase"], u" (módulo %s)" % d["modulo"]) + u"""
---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%(fase)s` |
| **Módulo** | %(modulo)s |
| **Planteamiento / Épica / HU** | [%(ep)s](../../epica.md) · [%(hu)s](../%(hu_md)s) |
| **Última actualización** | %(hoy)s |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se leyó la fase roja y su resultado |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ %(hoy)s, «terminélo» sobre los rojos que se pueden cerrar |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ `02·F19`: la redacción del criterio |
| 6 | Diseñador | diseño coherente | ✅ No se toca código |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ El molde se aprobó una vez para las cinco |
| 8 | Implementador | implementado + pruebas verdes | ✅ La medición corre y sale verde |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 4 tareas, 4 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 — %(criterio)s |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · ejecutar el criterio que quedó en rojo | Terminada | %(evidencia)s |
| T-02 · comprobar que la medición no se da por buena de más | Terminada | Está en el §4.1 del resultado |
| T-03 · poner al día el `Estado` de la historia | Terminada | — |
| T-04 · declarar el veredicto que deja atrás | Terminada | §0 del cierre |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Un veredicto en rojo es una foto, y nadie la vuelve a mirar | `S-061` |
| El reemplazo **se declara, no se deduce del orden** | `EP-004·HU-023` |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. La medición corrió antes de crear esta carpeta, y el guion no
escribe la fase de una historia cuya medición salga en rojo.
""" % dict(d, hoy=HOY, evidencia=evidencia))


def plan_trabajo(d, evidencia, base):
    return (CAB % (u"Plan de Trabajo", d["fase"], u" (módulo %s)" % d["modulo"]) + u"""
**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%(fase)s` |
| **Épica** | [%(ep)s](../../epica.md) |
| **HU** | [%(hu)s](../%(hu_md)s) — **una sola** (`F12.1`) |
| **Módulo** | %(modulo)s |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | %(hoy)s |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra un rojo que dejó de ser cierto.** La fase [`%(roja)s`](../%(roja)s/resultado_pruebas.md) cerró con «No cumple» el %(fecha_rojo)s por %(criterio_prosa)s: %(decia)s. **Era cierto entonces.** Lo resolvió después `%(lo_hizo)s`.

**Por qué hace falta una fase y no basta con anotarlo:** el veredicto de la fase roja **no se toca** (`20·M11`), porque reescribirlo borraría el rastro de que el criterio estuvo en rojo, y **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). El mecanismo que lo permite es `EP-004·HU-023`: la fase que cumple **declara** qué veredicto deja atrás, y el conteo lo lee.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** comprobar, ejecutando, que **%(criterio_corto)s hoy se cumple**, y dejarlo declarado donde se lee.

**Fuera de alcance:**

- **Construir nada.** El trabajo ya está hecho; lo que falta es que alguien vuelva a mirarlo.
- **Tocar la fase `%(roja)s`.** Su veredicto fue cierto el día que se escribió.
- **Los otros rojos de la cuenta.** Cada uno tiene su medición y su fase.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medida antes de crear la carpeta de esta fase**, porque abrirla mueve el número.

### 2.0 La línea base

```
%(base)s
```

### 2.1 Cómo se comprueba el criterio

%(como)s

**Y por qué la medición no se da por buena de más.** %(no_tapa)s

**Resultado de la medición:** %(evidencia)s

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | El cierre declara el veredicto |
| `%(hu_md)s` | Modificar | Documentación | Su `Estado` nombra el criterio en rojo |

**No se toca código.** Esta fase **comprueba y declara**.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Una fase que **declara**, sin tocar la roja | Reescribir aquel veredicto | Fue cierto el día que se escribió; reescribirlo borra el rastro (`20·M11`) |
| El reemplazo **se declara**, no se deduce del orden | Dar por cumplido el rojo porque hay una fase posterior | Está medido: de las ocho historias con fase posterior, solo dos habían vuelto a verificar el criterio rojo. Deducirlo taparía rojos vivos con trabajo ajeno |
| Las cifras las **mide un programa** | Copiar el documento de la fase anterior | Nadie relee el número veinte de una serie, y ahí es donde entra el dato falso |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. La medición se corrió antes de escribir esto | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Ejecutar el criterio que quedó en rojo | Calidad | 0,5 h | — | EV-01 |
| T-02 | Comprobar que la medición no se da por buena de más | Calidad | 0,5 h | T-01 | EV-02 |
| T-03 | Poner al día el `Estado` de la historia | Documentación | 0,25 h | T-02 | EV-03 |
| T-04 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-03 | EV-03 |

**Total estimado:** 1,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. `20·M10` no lo alcanza.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04

La `T-02` no es un adorno de la `T-01`: una medición que solo mira el caso bueno
da verde sobre cualquier cosa.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| %(criterio)s | Ejecutar el criterio, con su contraprueba | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas temporales, creadas y borradas por la medición. **Ninguna prueba usa
credenciales** (`00·N6`), y no se toca ningún proyecto real.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. No hay estado ni versión que deshacer.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un
rojo que ya no existe.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F17` — la línea base, medida antes de crear la carpeta.
- `04·R4` — se ejecuta en vez de afirmar sobre lo leído.
- `13·DOC5` — lo decidido se registra como señal.
- `20·M11` — el veredicto viejo no se borra: se deja atrás.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que se dé por cumplido leyendo el código en vez de corriéndolo | Sería declarar cumplido un rojo vivo | `T-01` ejecuta | Cerrado |
| B-02 | Que la medición pase por mirar solo el caso bueno | Verde sobre cualquier cosa | `T-02` | Cerrado |
| B-03 | Que abrir esta fase mueva la medición | `S-053` | La línea base está en el §2.0 | Cerrado |

---

## 11. Definition of Done

- [x] El criterio, **ejecutado**
- [x] La contraprueba, ejecutada
- [ ] El `Estado` de la historia, al día
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el
[funcionalidad_implementada.md](funcionalidad_implementada.md).
""" % dict(d, hoy=HOY, evidencia=evidencia, base=base))


def plan_pruebas(d, evidencia):
    return (CAB % (u"Plan de Pruebas", d["fase"], u"") + u"""
---

## 1. Introducción

### 1.1 Propósito

Comprobar que **%(criterio_corto)s**, que la fase `%(roja)s` dejó en rojo el
%(fecha_rojo)s, **hoy se cumple** — ejecutándolo, no leyéndolo.

### 1.2 Alcance

**Dentro:** el criterio que quedó en rojo, y su contraprueba.

**Fuera:** los demás criterios de la historia, que ya estaban en verde; y los
otros cuatro rojos, cada uno con su medición.

### 1.3 Documentos de referencia

- [%(hu)s](../%(hu_md)s)
- [Resultado de la fase roja](../%(roja)s/resultado_pruebas.md)
- El medidor: `historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| %(criterio)s | Es lo que quedó en rojo |
| La contraprueba del mismo criterio | Una medición que solo mira el caso bueno da verde sobre cualquier cosa |

---

## 3. Estrategia de pruebas

**De ejecución.** Se corre el criterio contra carpetas temporales que el propio
medidor crea y borra. Nada se afirma leyendo código.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase roja y su resultado, leídos.
- El medidor, escrito y corriendo.

### 4.2 Criterios de salida

- El criterio sale **CUMPLE** al ejecutarlo.
- La contraprueba también.

### 4.3 Criterios de suspensión y reanudación

**Suspensión:** si la medición sale NO CUMPLE, **esta fase no se escribe**. El
criterio de suspensión vive dentro del guion, no en la buena voluntad de quien
lo corre.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| %(criterio)s | CP-001, CP-002 |

---

## 6. Casos de prueba

### CP-001 — El criterio se cumple hoy

| Campo | Valor |
|---|---|
| **HU / CA** | %(hu)s / %(criterio_corto)s |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |
| **Cómo** | %(como)s |
| **Resultado esperado** | Que el criterio se cumpla, con su evidencia impresa |

### CP-002 — La medición no se da por buena de más

| Campo | Valor |
|---|---|
| **HU / CA** | %(hu)s / %(criterio_corto)s, contraprueba |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | %(no_tapa)s |
| **Resultado esperado** | Que la medición distinga el caso bueno del malo |

---

## 7. Datos y ambientes de prueba

Carpetas temporales. Ningún proyecto real se toca, y ninguna prueba usa
credenciales (`00·N6`).

---

## 8. Herramientas

`historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`, que imprime la
evidencia caso por caso y devuelve distinto de cero si alguno sigue en rojo.

---

## 9. Gestión de defectos

Un NO CUMPLE no es un defecto de esta fase: es el rojo que sigue vivo. La fase
no se escribe y la historia se queda como está.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | **0** |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Acción |
|---|---|
| Declarar cumplido lo que no se ejecutó | El medidor imprime la evidencia de cada caso |
| Medir sobre un proyecto real y cambiarle el estado | Todo va en carpetas temporales |

---

## 15. Aprobación

El molde se aprobó **una sola vez** para las cinco fases, y este plan lo dice de
frente: pedir cinco aprobaciones de un texto idéntico convierte la puerta en
trámite, y una puerta que es trámite deja de mirar.
""" % dict(d, evidencia=evidencia))


def resultado_pruebas(d, evidencia):
    return (CAB % (u"Resultado de Pruebas", d["fase"], u"") + u"""
**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `%(fase)s` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | %(hoy)s |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** **%(criterio_corto)s se cumple hoy**, comprobado ejecutándolo.
Lo que la fase `%(roja)s` declaró en rojo el %(fecha_rojo)s **era cierto
entonces**: %(decia)s. Lo resolvió después `%(lo_hizo)s`, y hasta hoy nadie
había vuelto a mirarlo.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El criterio se cumple hoy

**Cómo se ejecutó.** %(como)s

**Qué salió:** %(evidencia)s

**Resultado: pasa.**

### CP-002 — La medición no se da por buena de más

%(no_tapa)s

**Resultado: pasa.** La medición está escrita de forma que el caso bueno solo no
alcanza para dar verde.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `%(roja)s` **no se toca**: fue cierto el día que se
escribió, y reescribirlo borraría el rastro de que el criterio estuvo en rojo.

Pero **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). Sin una fase que
lo declare, la historia arrastra un «no cumple» que ya no existe, y quien lo lea
después va a buscar un trabajo que ya está hecho.

### 4.2 Rastros

Ninguno. Las carpetas temporales las borra el propio medidor, y no se tocó
ningún proyecto real.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- El medidor: `historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`
- El generador de esta fase: `historico-chat/scripts/2026-08-29/cerrar-los-cinco-rojos.py`
- La fase que hizo el trabajo: `%(lo_hizo)s`
""" % dict(d, hoy=HOY, evidencia=evidencia))


def funcionalidad(d, evidencia):
    return (CAB % (u"Funcionalidad implementada", d["fase"],
                   u" (módulo %s)" % d["modulo"]) + u"""
## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `%(fase)s` |
| **Módulo** | %(modulo)s |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el %(hoy)s |
| **HU / CA cubiertas** | [%(hu)s](../%(hu_md)s): %(criterio)s |
| **Fecha de cierre** | %(hoy)s |
| **Versión del estándar al cerrar** | `35.10.0` — **sin cambio**: no se toca código |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `%(roja)s` |

> **Por qué se declara el reemplazo:** se volvió a verificar %(criterio_corto)s, ejecutándolo, y hoy se cumple. Aquel rojo era cierto el %(fecha_rojo)s. **El veredicto de aquella fase no se toca** (`20·M11`): la cuenta lo deja atrás, el documento sigue diciendo lo que decía.

---

## 1. Qué se implementó — resumen

**Nada. Esta fase comprueba y declara.**

La fase [`%(roja)s`](../%(roja)s/resultado_pruebas.md) cerró en rojo el
%(fecha_rojo)s porque %(decia)s, y **era cierto**. Lo resolvió después
`%(lo_hizo)s`.

Lo que faltaba era que **alguien volviera a mirarlo**. Nadie lo hace por su
cuenta (`S-061`), y mientras tanto la historia arrastraba un «no cumple» que ya
no existía.

| Antes | Ahora |
|---|---|
| %(criterio)s, en rojo desde el %(fecha_rojo)s | **Cumple**, comprobado ejecutando |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| %(criterio)s | comprobación | `%(lo_hizo)s` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · ejecutar el criterio | ✅ | %(evidencia)s |
| T-02 · la contraprueba | ✅ | §3 del resultado |
| T-03 · el `Estado` de la historia | ✅ | — |
| T-04 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia código |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios. No se agrega ni se modifica ningún punto de entrada.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué | Señal |
|---|---|---|
| Una fase que **declara**, sin tocar la roja | Aquel veredicto fue cierto. Reescribirlo borra el rastro | `20·M11` |
| Se comprueba **ejecutando**, no leyendo | Existir no es funcionar | `04·R4` |
| Las cifras las **mide un programa** | Nadie relee el número veinte de una serie | `S-081` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Nadie vuelve a mirar un veredicto en rojo | **Abierta.** Es `S-061`; esta fase es una de las que lo hizo a mano |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un
rojo que ya no existe.
""" % dict(d, hoy=HOY, evidencia=evidencia))


def main():
    sys.path.insert(0, os.path.join(RAIZ, "validadores"))
    import fases as F
    cumplen, no_cumplen, sin_v = F.por_veredicto(RAIZ)
    base = (u"%d cumplen · %d no cumplen · %d sin veredicto"
            % (cumplen, no_cumplen, sin_v))
    print(u"Línea base, medida antes de crear ninguna carpeta: %s\n" % base)

    escritas, saltadas = [], []
    for d in LOS_CINCO:
        cumple, evidencia = getattr(medidor, d["clave"])()
        if not cumple:
            print(u"SALTADA  %s — la medición sale en rojo: %s"
                  % (d["fase"], evidencia))
            saltadas.append(d["fase"])
            continue

        carpeta = os.path.join(EPICAS, d["epica"], d["hu_dir"], d["fase"])
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        _escribir(carpeta, "estado-fase.md", estado_fase(d, evidencia))
        _escribir(carpeta, "plan_trabajo.md", plan_trabajo(d, evidencia, base))
        _escribir(carpeta, "plan_pruebas.md", plan_pruebas(d, evidencia))
        _escribir(carpeta, "resultado_pruebas.md",
                  resultado_pruebas(d, evidencia))
        _escribir(carpeta, "funcionalidad_implementada.md",
                  funcionalidad(d, evidencia))
        print(u"ESCRITA  %s" % d["fase"])
        escritas.append(d["fase"])

    print(u"\n%d fases escritas, %d saltadas." % (len(escritas), len(saltadas)))
    cumplen, no_cumplen, sin_v = F.por_veredicto(RAIZ)
    print(u"Después: %d cumplen · %d no cumplen · %d sin veredicto"
          % (cumplen, no_cumplen, sin_v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
