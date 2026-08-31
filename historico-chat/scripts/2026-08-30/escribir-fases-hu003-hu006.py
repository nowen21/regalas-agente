# -*- coding: utf-8 -*-
"""Escribe las fases B de EP-001 HU-003 y EP-006 HU-006, y pone las historias al dia.

Las dos cierran por decision del usuario del 2026-08-30. Son los dos ultimos
rojos de los trece con que arranco la sesion.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")

CASOS = [
    dict(
        epica="EP-001-cuerpo-de-reglas-heredable", ep="EP-001",
        hu_dir="HU-003-nucleo-que-no-se-sobrescribe",
        hu_md="HU-003-nucleo-que-no-se-sobrescribe.md", hu="HU-003",
        modulo=u"Cuerpo de reglas",
        fase="B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa",
        roja="A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado",
        fecha_rojo="2026-08-22",
        criterio=u"CA-02, la clave no queda en claro",
        estado_viejo=u"| **Estado** | Pendiente |",
        estado_nuevo=u"| **Estado** | Terminada — el CA-02 se cerró en la fase `B`: se tapa la clave que va con su nombre, y la que se dice dentro de una frase queda declarada como límite |",
        fila_cubre=u"CA-02",
        fila_estado=u"tres de seis formas se tapan, que son las que llevan la clave junto a su nombre. Las otras tres quedan declaradas como límite, con su motivo. Declara reemplazar el veredicto de la fase `A`",
        que_decia=u"de seis formas de escribir una clave, **tres se enmascaran y tres no**. Las tres que no son las que dicen la clave dentro de una frase normal: «mi clave es Patito2026»",
        decision=u"**No se tapa la clave dicha dentro de una frase, y queda declarado.** Lo decidió el usuario el 2026-08-30.",
        porque=u"""**Por qué no se intenta.** Para tapar «mi clave es Patito2026» habría que suponer que la palabra que sigue a «clave» es la clave. Con esa misma suposición se tapa «la clave del asunto es que el proceso sirva», que es una frase corriente.

**Y el daño de tapar de más no es un falso positivo:** es que un enmascarado que estorba se apaga. Apagado no tapa ninguna de las seis, así que intentar tapar tres más pone en riesgo las tres que hoy sí se tapan.

**Lo que sí queda cubierto**, medido ejecutándolo: las tres formas en que la clave va pegada a su nombre, que son las que salen de un archivo de configuración, de un registro o de un comando pegado. Son las que aparecen sin que nadie las escriba a propósito.

**Lo que queda descubierto, dicho sin adorno:** si alguien escribe su clave dentro de una frase, queda escrita. La defensa ahí no es el programa: es `00·N6`, que prohíbe escribirla.""",
        metricas=[(u"Formas con la clave pegada a su nombre, tapadas", u"3 de 3"),
                  (u"Frases corrientes que se tapan de más", u"0 de 5"),
                  (u"Formas dentro de una frase, tapadas", u"0 de 3, y es lo decidido")],
        caso_titulo=u"CP-001 — Qué tapa y qué no, ejecutado",
        caso_cuerpo=u"""Corrido sobre las seis formas:

| Lo que entra | Sale |
|---|---|
| `API_KEY=supersecreto123456` | tapado |
| `password: MiClave123456` | tapado |
| `la contraseña: Patito2026` | tapado |
| `mi clave es Patito2026` | **intacto**, y es lo decidido |
| `el token es abc123xyz789` | **intacto**, y es lo decidido |
| `usa la contraseña Patito2026 para entrar` | **intacto**, y es lo decidido |

Y la contraprueba, que es la que sostiene la decisión: cinco frases corrientes
salen **intactas**, entre ellas `la clave del asunto es que el proceso sirva` y
`API_KEY=os.environ['X']`. Ninguna se tapa de más.

**Resultado: pasa.**""",
        decision_tabla=[
            (u"No se tapa la clave dicha dentro de una frase",
             u"Ampliar el enmascarado a la frase",
             u"Habría que suponer que la palabra siguiente a «clave» es la clave, y con eso se tapa «la clave del asunto es que sirva»"),
            (u"El límite se escribe, no se calla",
             u"Cerrar el criterio sin nombrarlo",
             u"Un criterio que se da por cumplido escondiendo lo que no cubre es la mentira optimista que esta cuenta existe para impedir"),
        ],
        deuda=[(u"La clave dicha dentro de una frase queda en claro",
                u"**Abierta y declarada**, con su motivo. La defensa ahí es `00·N6`, no el programa")],
        rutas="../../../../../",
    ),
    dict(
        epica="EP-006-memoria-de-lo-aprendido", ep="EP-006",
        hu_dir="HU-006-sacar-del-almacen-local",
        hu_md="HU-006-sacar-del-almacen-local.md", hu="HU-006",
        modulo=u"Memoria",
        fase="B-EP-006-HU-006-se-lleva-todo-y-el-almacen-queda-vacio",
        roja="A-EP-006-HU-006-retrodocumentar-el-vaciado-del-almacen-local",
        fecha_rojo="2026-08-22",
        criterio=u"CA-01, el almacén local queda vacío",
        estado_viejo=u"| **Estado** | En curso — CA-02, RNF y transversales cumplidos; el CA-01 falla en un punto |",
        estado_nuevo=u"| **Estado** | Terminada — el CA-01 se cerró en la fase `B`: el programa se lleva todo y el almacén queda vacío |",
        fila_cubre=u"CA-01",
        fila_estado=u"el programa que trae los archivos al repositorio se lleva todos, no solo los `.md`, y el almacén local queda vacío como exige `01·C19`. Declara reemplazar el veredicto de la fase `A`",
        que_decia=u"el almacén estaba vacío y el programa lo vaciaba, pero fallaba el paso 5: `sueltos()` devuelve **todo** archivo, así que un `config.json` de la herramienta terminaría en `historico-chat/memory/` como si fuera un recuerdo",
        decision=u"**Se lleva todo.** Lo decidió el usuario el 2026-08-30.",
        porque=u"""**Por qué manda `01·C19` tal como está escrita.** Exige que el almacén local quede **vacío**, y eso es lo que se sostiene: lo que queda ahí es lo que se pierde. La carpeta de la herramienta no la mira nadie, no se versiona y desaparece con la máquina.

**El costo de la otra salida era peor.** Si el programa dejara ahí lo que no es recuerdo, `revisar()` reprobaría para siempre por un archivo que nadie va a mover, y un reclamo que no se puede cerrar se aprende a ignorar.

**Y el archivo de más no se pierde de vista:** un `config.json` en `historico-chat/memory/` se ve, se lee y se borra cuando estorbe. Uno olvidado en una carpeta de la herramienta, no.""",
        metricas=[(u"Archivos que quedan en el almacén después de recoger", u"0"),
                  (u"Pruebas de la clase en verde", u"6 de 6"),
                  (u"Pruebas marcadas como fallo esperado", u"0, eran 1")],
        caso_titulo=u"CP-001 — Se lleva todo, y el almacén queda vacío",
        caso_cuerpo=u"""Con un almacén que tiene `algo.md` y `config.json`, corrido el programa:

```
almacén local:  []
repositorio:    algo.md, config.json
```

```
Ran 6 tests in 0.122s
OK
```

La prueba pasó de estar marcada como fallo esperado a comprobar lo decidido, y
afirma las dos mitades: que el almacén queda vacío, y que lo que no es recuerdo
también se trae **y por eso se ve**.

**Resultado: pasa.**""",
        decision_tabla=[
            (u"Se lleva todo", u"Que el programa distinga y deje lo que no es recuerdo",
             u"Lo que queda en el almacén es lo que se pierde: esa carpeta no la mira nadie y no se versiona"),
            (u"`01·C19` no se toca", u"Precisarla a «ningún recuerdo queda en el almacén»",
             u"Aflojarla dejaría vivo el caso que la regla existe para evitar"),
            (u"La prueba comprueba las dos mitades", u"Comprobar solo que el almacén quedó vacío",
             u"Un programa que borrara el almacén sin traer nada también lo dejaría vacío"),
        ],
        deuda=[(u"Al repositorio puede entrar un archivo que no es recuerdo",
                u"**Abierta y declarada.** Se ve y se borra cuando estorbe, que es la diferencia con dejarlo afuera")],
        rutas="../../../../../",
    ),
]


def w(D, nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


for c in CASOS:
    D = os.path.join(EPICAS, c["epica"], c["hu_dir"], c["fase"])
    if not os.path.isdir(D):
        os.makedirs(D)

    w(D, "estado-fase.md", u"""# Estado de fase — Fase `{fase}` (módulo {modulo})   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {modulo} |
| **Planteamiento / Épica / HU** | [{ep}](../../epica.md) · [{hu}](../{hu_md}) |
| **Última actualización** | 2026-08-30 |

---

## 1. En qué estación va

**Estación actual:** 12 · Commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ✅ Se ejecutó el criterio, no se leyó |
| 2 | Proponente · alcance | 👤 alcance aprobado | ✅ 2026-08-30 |
| 3 | Escritor de épica | 👤 épica aprobada | ✅ Ya existía |
| 4 | Escritor de historia | 👤 HUs aprobadas | ✅ Ya existía |
| 5 | Escritor de especificación | 👤 especificación aprobada | ✅ La decisión del usuario, en esta sesión |
| 6 | Diseñador | diseño coherente | ✅ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ✅ |
| 8 | Implementador | implementado + pruebas verdes | ✅ |
| 9 | Verificador | trazabilidad sin faltantes | ✅ 3 tareas, 3 con resultado |
| 10 | Crítico | sin hallazgos graves | ✅ |
| 11 | Cierre documental + señales | docs y señales al día | ✅ |
| 12 | Commit | 👤 autorizado | ☐ **Pendiente de autorización** |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1, el {criterio} |
| **CA en "No"** | Ninguno |
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) §2 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 · ejecutar el criterio y su contraprueba | Terminada | — |
| T-02 · aplicar la decisión del usuario | Terminada | — |
| T-03 · declarar el veredicto que deja atrás | Terminada | §0 del cierre |

**Hechas:** 3 de 3. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Este rojo no se cerraba midiendo: pedía una decisión del usuario | `S-085` |

---

## 3. Pendiente / preguntas abiertas

- **La autorización del commit**, que se pide aparte.

---

## 4. Si se bloqueó

No se bloqueó. Estuvo ocho días esperando una decisión que no era del que ejecuta.
""".format(**c))

    w(D, "plan_trabajo.md", u"""# Plan de Trabajo — Fase `{fase}` (módulo {modulo})   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Épica** | [{ep}](../../epica.md) |
| **HU** | [{hu}](../{hu_md}), **una sola** (`F12.1`) |
| **Módulo** | {modulo} |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el {criterio}**, que dejó la fase [`{roja}`](../{roja}/resultado_pruebas.md) en «No cumple» el {fecha_rojo}, porque {que_decia}.

{decision}

**Este rojo no se cerraba midiendo.** Medirlo otra vez daba el mismo resultado todos los días: el dato no cambiaba, faltaba saber qué se quería hacer con él.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** aplicar la decisión, comprobarla ejecutando, y dejar escrito qué queda cubierto y qué no.

**Fuera de alcance:** los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
107 cumplen, 2 no cumplen, 5 sin veredicto
```

### 2.1 Por qué la decisión es esta

{porque}

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `{hu_md}` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
{tabla_decisiones}

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Ejecutar el criterio y su contraprueba | Calidad | 0,5 h | — | EV-01 |
| T-02 | Aplicar la decisión del usuario | Implementación | 0,5 h | T-01 | EV-02 |
| T-03 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-02 | EV-02 |

**Total estimado:** 1,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

La contraprueba de la `T-01` no es adorno: es la que sostiene la decisión.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| {criterio} | Ejecutar el criterio con su contraprueba | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas y valores de prueba que la propia prueba arma y borra. Ninguna
credencial real (`00·N6`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `01·C4`, decidir no es del que ejecuta. Es lo que tuvo detenida esta historia.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `20·M11`, lo publicado no se reescribe: se deja atrás.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Cerrar el criterio escondiendo lo que no cubre | Es la mentira optimista que esta cuenta existe para impedir | El límite queda escrito en el cierre | Cerrado |
| B-02 | Que el agente decidiera esto por su cuenta | Es `01·C4` | Se esperó la decisión | Cerrado |

---

## 11. Definition of Done

- [x] El criterio y su contraprueba, ejecutados
- [x] La decisión, aplicada
- [x] El límite, escrito
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
""".format(tabla_decisiones="\n".join(
        u"| %s | %s | %s |" % t for t in c["decision_tabla"]), **c))

    w(D, "plan_pruebas.md", u"""# Plan de Pruebas — Fase `{fase}`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar el {criterio} con la decisión del usuario aplicada, ejecutándolo.

### 1.2 Alcance

**Dentro:** el criterio y su contraprueba.

**Fuera:** los otros criterios de la historia, que ya estaban en verde.

### 1.3 Documentos de referencia

- [{hu}](../{hu_md})
- [Resultado de la fase A](../{roja}/resultado_pruebas.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| El criterio, con la decisión aplicada | Es lo que la fase viene a cerrar |
| Su contraprueba | Sin ella, el criterio pasaría con cualquier cosa |

---

## 3. Estrategia de pruebas

De ejecución. Nada se afirma leyendo el código.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La decisión del usuario, escrita.

### 4.2 Criterios de salida

- El criterio pasa, y la contraprueba también.
- Ninguna prueba de la clase queda marcada como fallo esperado.

### 4.3 Criterios de suspensión y reanudación

Si la contraprueba fallara, la fase se detiene: significaría que aplicar la
decisión rompió algo que ya funcionaba.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| {criterio} | CP-001 |

---

## 6. Casos de prueba

### {caso_titulo}

| Campo | Valor |
|---|---|
| **HU / CA** | {hu} / {criterio} |
| **Tipo** | De ejecución |
| **Prioridad** | **Crítica** |
| **Resultado esperado** | Que lo ejecutado coincida con lo que la decisión dice que debe pasar, y que la contraprueba siga en pie |

---

## 7. Datos y ambientes de prueba

Lo que la propia prueba arma y borra. Ninguna credencial real (`00·N6`).

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos comprobados leyendo en vez de corriendo | **0** |
| Pruebas marcadas como fallo esperado | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30, con la decisión del usuario.
""".format(**c))

    w(D, "resultado_pruebas.md", u"""# Resultado de Pruebas — Fase `{fase}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `{fase}` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la decisión está aplicada y comprobada ejecutando. Lo que la
fase `{roja}` declaró en rojo el {fecha_rojo} era cierto entonces y siguió
siéndolo hasta que hubo decisión: no era trabajo pendiente, era una pregunta sin
responder.

| Métrica | Real |
|---|---|
{metricas}

---

## 3. Resultado por caso

### {caso_titulo}

{caso_cuerpo}

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Lo que este criterio no cubre, dicho acá y no escondido

{limite}

### 4.2 Por qué este rojo no se cerraba midiendo

Medirlo otra vez daba el mismo resultado todos los días. El dato no cambiaba;
faltaba saber qué se quería hacer con él. Está en `S-085`.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- La decisión del usuario, en la transcripción del 2026-08-30
- La corrida del §3
""".format(**dict(c,
           metricas="\n".join(u"| %s | %s |" % t for t in c["metricas"]),
           limite=c["deuda"][0][0] + u". " + c["deuda"][0][1].replace("**", ""))))

    w(D, "funcionalidad_implementada.md", u"""# Funcionalidad implementada — Fase `{fase}` (módulo {modulo})   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{fase}` |
| **Módulo** | {modulo} |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [{hu}](../{hu_md}): el {criterio} |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `{roja}` |

> **Por qué se declara el reemplazo:** la decisión que faltaba está tomada y comprobada. Aquel rojo era cierto el {fecha_rojo}. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

La fase [`{roja}`](../{roja}/resultado_pruebas.md) cerró en rojo porque {que_decia}.

{decision}

{porque}

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| {criterio} | decisión aplicada | Este cierre | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · ejecutar el criterio y su contraprueba | ✅ | §3 del resultado |
| T-02 · aplicar la decisión | ✅ | §3 del resultado |
| T-03 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 3 tareas, 3 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
{tabla_corta}

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
{deuda}

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
""".format(**dict(c,
           tabla_corta="\n".join(u"| %s | %s |" % (t[0], t[2])
                                 for t in c["decision_tabla"]),
           deuda="\n".join(u"| %s | %s |" % t for t in c["deuda"]))))

    # La historia, al dia.
    R = os.path.join(EPICAS, c["epica"], c["hu_dir"], c["hu_md"])
    with io.open(R, encoding="utf-8") as f:
        t = f.read()
    if c["estado_viejo"] in t:
        t = t.replace(c["estado_viejo"], c["estado_nuevo"], 1)
        print("estado al dia:", c["hu"])
    sep = u"| Fase | Qué CA cubre | Estado |\n|---|---|---|\n"
    fila = (u"| [%s](%s/estado-fase.md) | %s | **Ejecutada el 2026-08-30.** "
            u"Veredicto: [**Cumple**](%s/resultado_pruebas.md#2-veredicto-de-la-fase) "
            u"— %s |\n" % (c["fase"], c["fase"], c["fila_cubre"], c["fase"],
                           c["fila_estado"]))
    if sep in t:
        t = t.replace(sep, sep + fila, 1)
        print("fila puesta:", c["hu"])
    with io.open(R, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    print("fase escrita:", c["fase"])
