# -*- coding: utf-8 -*-
"""Fase B de la HU-007: plan de trabajo, plan de pruebas, estado de la fase y su fila en la HU."""
import glob
import io
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU_DIR = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-007-*"))[0]
HU_DOC = "HU-007-nada-se-escribe-fuera-del-plan-aprobado.md"
FASE = "B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar"
D = os.path.join(HU_DIR, FASE)
P103 = "../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/"
HU_REL = "documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-007-nada-se-escribe-fuera-del-plan-aprobado/" + HU_DOC

PLAN = """# Plan de Trabajo · Fase `{f}` (módulo `validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{f}` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-007](../{hu}), una sola (`F12.1`) |
| **Módulo** | `validadores/`, `adaptadores/claude-code/` |
| **Especificación del módulo** | El CA-02 de la HU-007, en sus capas 1 y 2 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): segunda de tres fases de la HU-007. Sale del punto 26 del [análisis 1]({p}analisis-1.md) (acuerdos 18, 44 y 46), del punto 1 del [análisis 8]({p}analisis-8.md) (acuerdos 1, 2 y 3) y del punto 3 del [análisis 10]({p}analisis-10.md) (acuerdo 6). La capa 3, el commit, quedó en la fase `A`; la capa 4 y el contrato de cada adaptador van en la fase `C`.

**Carencias que cierra** (`02·F14` Q3): el freno solo mira la herramienta de escritura y solo frena lo que sale del proyecto; no compara con el plan, no ve la consola, el segundo plano ni lo que publica, y nadie anota el hallazgo.

**Aprobación** (`02·F4`): pendiente.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-007 | Estado |
|---|---|
| CA-02 · El freno detiene lo que no está en el plan ni autorizado, por cualquier canal | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que antes de cada acción el freno detenga lo que no está en el plan de la fase en curso ni lo autoriza una regla, por cualquier canal; que después de cada orden de consola compare lo que cambió con el plan; y que al detener anote el hallazgo y mande volver al análisis.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-02 (capa 1) | Antes de actuar: herramienta de escritura, consola, segundo plano, instalaciones, procesos que quedan corriendo y lo que se publica | Enganche y programa | Alta |
| CA-02 (capa 2) | Después de cada orden de consola: lo que cambió en git contra el plan | Enganche y programa | Media |
| CA-02 (fase activa) | La fase en curso decide contra qué se compara | Programa | Baja |

**Fuera de alcance:** la integración continua y el contrato de cada adaptador (fase `C`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 50.0.0:

- `adaptadores/claude-code/hook_antes.py` corre antes de `Write`, `Edit`, `MultiEdit` y `NotebookEdit`, y solo detiene la escritura que sale de la carpeta del proyecto. No ve la consola ni el segundo plano.
- `validadores/acuerdos.py` ya dice qué fases están en curso; `validadores/autorizado.py` dice qué regla autoriza una ruta, y `validadores/plan_vs_hecho.py` lee las rutas exactas del plan y su aprobación.
- Ningún programa anota hallazgos; el resumen de la sesión lo encuentra `hook_resumen.py` por la marca de sesión de la transcripción.
- Las HU, las épicas y los pendientes se escriben fuera de una fase, y ninguna regla autoriza escribirlos: ni `13·DOC15`, ni `13·DOC16`, ni `02·F23` traen la línea «Autoriza escribir».
- Los análisis 9 y 10 mandaron corregir cosas «de una y sin fase»; sus filas de «Lo que se tiene que hacer» no nombran las rutas que tocan.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/freno.py` | Nuevo | Programa | Clasifica la acción, saca sus destinos, decide si se permite y anota el hallazgo |
| `adaptadores/claude-code/hook_antes.py` | Modificar | Enganche | Capa 1, sobre toda acción |
| `adaptadores/claude-code/hook_despues.py` | Nuevo | Enganche | Capa 2, después de cada orden de consola |
| `validadores/instalar.py` | Modificar | Instalador | El enganche de antes sobre toda acción y el de después sobre la consola |
| `base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md`, `base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md`, `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | Modificar | Regla | Su línea «Autoriza escribir» y su sello |
| `plantillas/analisis.md` | Modificar | Plantilla | La fila que se hace «de una y sin fase» nombra sus rutas exactas |
| `validadores/tests/test_el_freno.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | El programa nuevo |
| `{hurel}` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 51.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| El freno compara con el plan de la fase en curso | Todo proyecto con la versión nueva | Fuera de una fase en curso solo deja lo que una regla autoriza |
| `hook_antes.py` corre sobre toda acción | Todo proyecto, al reinstalar | El de hoy sigue frenando lo que sale del proyecto |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El freno corre antes de toda acción y la clasifica por su efecto: escribe, borra, ejecuta o publica | Mirar solo la herramienta de escritura | Una regla rige en todas partes, no solo donde un programa la mira | Análisis 8, acuerdos 1 y 3 |
| Compara con la fase en curso: antes de aprobarse su plan, deja solo los documentos de la fase y lo que una regla autoriza; aprobado, también lo que el plan declara; sin fase en curso, solo lo autorizado | Comparar solo cuando hay plan aprobado | Así lo acordó el usuario | Análisis 10, acuerdo 6 |
| No frena lo que una regla autoriza, leído por `autorizado.py` | Una lista aparte | Cada entrada cita la regla que la autoriza | Análisis 1, acuerdo 46 |
| `13·DOC15`, `13·DOC16` y `02·F23`, que mandan escribir la HU, la épica y el pendiente, suman su línea «Autoriza escribir» | Frenarlos hasta que haya una fase | Lo que una regla manda hacer no se frena, y su entrada se agrega en el mismo cambio | Análisis 1, acuerdo 46 |
| Lo que un análisis aprobado manda hacer «de una y sin fase» no se frena: mientras ese análisis está prendido, el freno deja pasar las rutas exactas que nombra su fila, y la plantilla del análisis pide nombrarlas | Exigir una fase para todo | El usuario ya lo autorizó en el análisis; falta que un programa lo pueda leer | Propuesta del agente |
| Al detener, anota el hallazgo en el resumen de la sesión y el mensaje dice que la ejecución vuelve al análisis | Solo detener | El hallazgo detiene y vuelve al análisis | Análisis 1, acuerdos 18 y 44 |
| En la consola lee la orden: redirecciones, órdenes que crean, copian, mueven o borran, y las de git que descartan cambios; resuelve la ruta real antes de comparar (`..`, `~`, variables y enlaces) | Comparar el texto de la orden tal cual | Las rutas que engañan hacen creer que algo queda adentro | Análisis 8, acuerdo 3 |
| Detiene la corrida en segundo plano, la instalación de paquetes, la configuración global y el proceso que queda corriendo después del turno | Dejarlos pasar | Escriben fuera del proyecto o actúan sin que nadie mire | Análisis 8, acuerdo 3 |
| Lo que se publica fuera del proyecto se pregunta cada vez | Dejarlo pasar | Publicar no se deshace | Análisis 8, acuerdo 3 |
| La capa 2 compara lo que cambió en git con una foto tomada justo antes de la orden, guardada en `.git/` | Comparar todo lo que está sin guardar | Lo que ya estaba cambiado, por ejemplo de otra sesión, no lo hizo esta orden | Propuesta del agente |
| Antes de correr pruebas no hay un paso aparte: la orden pasa por la capa 1, y lo que escribió la revisa la capa 2 | Un paso que compare todo antes de las pruebas | Con la capa 2 después de cada orden, lo escrito antes de las pruebas ya quedó comparado | Propuesta del agente |
| Lo que un programa escribe por dentro fuera del proyecto no se ve; queda declarado en el contrato del adaptador | Prometer que se ve | Leyendo la orden no se puede saber | Análisis 8, acuerdo 3 |
| La versión sube a 51.0.0, MAYOR | MENOR | El agente deja de poder escribir fuera del plan | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Las dos que había las resuelve el acuerdo 46 del análisis 1: el freno solo detiene lo que no está autorizado en ninguna parte.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Antes de actuar | Solo la escritura fuera del proyecto | Toda acción, contra el plan de la fase en curso y lo autorizado | `02·F8`, `04·S9` |
| Después de actuar | Nada | Lo que cambió en git contra el plan | `02·F8` |
| Hallazgo del freno | Nadie lo anota | Queda en el resumen de la sesión | `13·DOC22` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-02 · El freno detiene lo que no está en el plan ni autorizado, por cualquier canal

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `freno.py`: qué permite la fase en curso; la ruta real; los destinos de una orden de consola; lo que nunca se deja (segundo plano, instalaciones, configuración global, procesos que quedan corriendo); qué herramienta publica | `validadores/freno.py` | CA-02 | Lo usan los dos enganches | 3 h | Ninguna | CP-001 a CP-003 |
| T-02 | `freno.py` anota el hallazgo en el resumen de la sesión: qué pasó y por qué importa | `validadores/freno.py` | CA-02 | El resumen de cada sesión | 1 h | T-01 | CP-005 |
| T-03 | Sumar la línea «Autoriza escribir» a `13·DOC15` (las HU), `13·DOC16` (las épicas) y `02·F23` (los pendientes), con sus sellos contra 51.0.0, y regenerar el mapa de tareas | Las tres reglas de la tabla 2.1 | CA-02 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-001 |
| T-04 | La plantilla del análisis pide que la fila «de una y sin fase» nombre sus rutas exactas; `freno.py` las deja pasar mientras ese análisis está prendido | `plantillas/analisis.md`, `validadores/freno.py` | CA-02 | Los análisis nuevos | 1 h | T-01 | CP-001 |
| T-05 | `hook_antes.py` corre sobre toda acción: detiene lo no permitido, pregunta lo que se publica, y al detener anota el hallazgo; toma la foto de git antes de cada orden de consola | `adaptadores/claude-code/hook_antes.py` | CA-02 | Toda acción del agente | 1,5 h | T-02 | CP-001 a CP-003, CP-005 |
| T-06 | `hook_despues.py`: después de cada orden de consola compara lo que cambió con la foto y avisa el hallazgo | `adaptadores/claude-code/hook_despues.py` | CA-02 | Toda orden de consola | 1 h | T-05 | CP-004 |
| T-07 | El instalador pone el enganche de antes sobre toda acción y el de después sobre la consola | `validadores/instalar.py` | CA-02 | Todo proyecto, al reinstalar | 0,3 h | T-06 | CP-001 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Escribir los casos del plan de pruebas; el programa en el mapa del sitio; la fila de la fase en la HU; subir a 51.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_el_freno.py`, `anatomia/mapa-del-sitio.md`, `{hurel}`, `CHANGELOG.md`, `VERSION` | CA-02 | Todo proyecto adopta la versión | 1 h | T-01 a T-07 | CP-001 a CP-006 |

## 4. Secuencia de ejecución

T-01 a T-04; después T-05, T-06 y T-07; al final T-08, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-02 | Intentar escribir fuera del plan con la herramienta, la consola, un programa y en segundo plano; escribir algo autorizado; escribir código con el plan sin aprobar | CP-001 a CP-005 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba con git en una carpeta temporal, con una épica, una HU, una fase en curso con su plan, y reglas que autorizan escribir.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y reinstalar.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 51.0.0 con el instalador, que pone los dos enganches. Desde ahí, el agente solo escribe lo que el plan de la fase en curso declara o lo que una regla autoriza.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F8`, `02·F9`, `04·S9`, `04·S10`, `00·N1`, `13·DOC22`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el freno detenga una lectura | Las órdenes que no escriben pasan; la prueba cubre las de lectura más comunes |
| Que una orden escriba por una forma que el freno no reconoce | La capa 2 la ve después, dentro del proyecto |
| Que un error del freno detenga el trabajo | Si algo falla adentro, deja pasar y lo avisa |

## 11. Definition of Done

- [ ] CA-02, en sus capas 1 y 2, con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 51.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.

**Hallazgos al ejecutar:** se anota al cerrar.
"""

CPS = [
    ("CP-001", "Herramienta de escritura", "T-01, T-03 y T-05 terminadas",
     "Una fase en curso con plan sin aprobar y luego aprobado; una regla que autoriza el resumen",
     [("Sin aprobar el plan, escribir el plan de pruebas de la fase", "Pasa"),
      ("Sin aprobar el plan, escribir un archivo de código", "Se detiene"),
      ("Con el plan aprobado, escribir un archivo que declara", "Pasa"),
      ("Con el plan aprobado, escribir uno que no declara", "Se detiene"),
      ("Sin fase en curso, escribir el resumen de la sesión y luego un archivo de código", "El resumen pasa y el código se detiene"),
      ("Sin fase en curso, escribir una HU", "Pasa: la autoriza `13·DOC15`"),
      ("Con un análisis prendido cuya fila «de una y sin fase» nombra un archivo, escribirlo", "Pasa"),
      ("Escribir fuera del proyecto, también con `..` o `~`", "Se detiene"),
      ("Leer el enganche que pone el instalador", "Corre sobre toda acción")]),
    ("CP-002", "Consola", "T-01 y T-03 terminadas", "La misma fase, con el plan aprobado",
     [("Redirigir la salida a un archivo que el plan no declara", "Se detiene"),
      ("Copiar, mover o borrar un archivo que el plan no declara", "Se detiene"),
      ("Correr una orden en segundo plano", "Se detiene"),
      ("Instalar un paquete global o cambiar la configuración global de git", "Se detiene"),
      ("Dejar un proceso corriendo después del turno", "Se detiene"),
      ("Una orden que solo lee, como `git status`", "Pasa")]),
    ("CP-003", "Lo que se publica", "T-01 y T-03 terminadas", "Una herramienta que publica fuera del proyecto",
     [("Usarla", "El freno pregunta antes de actuar")]),
    ("CP-004", "Después de actuar", "T-04 terminada", "Un archivo ya cambiado antes de la orden",
     [("Un programa escribe por dentro un archivo que el plan no declara", "Avisa el hallazgo"),
      ("Escribe uno que el plan declara", "No avisa nada"),
      ("El archivo que ya estaba cambiado antes de la orden", "No cuenta")]),
    ("CP-005", "El hallazgo queda anotado", "T-02 y T-03 terminadas", "Una sesión con su transcripción y su resumen",
     [("El freno detiene una escritura", "El resumen suma el hallazgo con qué pasó y por qué importa, y el mensaje dice que se vuelve al análisis")]),
    ("CP-006", "Cada tarea cita su criterio", "Fase terminada", "Ninguno",
     [("Correr `validar.py flujo` y leer el plan", "Ninguna tarea sin su criterio")]),
]

PRUEBAS = """# Plan de Pruebas · Fase `{f}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU007-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-007: CA-02, capas 1 y 2 |
| **Fecha** | 2026-10-03 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Pendiente |
| **Estado** | Borrador |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El freno antes y después de actuar, y el hallazgo anotado | Claude | Proyecto de prueba con git en una carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-02 |
| Seguridad | ☑ | Nada se escribe fuera del proyecto ni del plan |

### 3.3 Técnicas de diseño de casos

- Partición por canal: herramienta de escritura, consola, segundo plano, publicación y programa que escribe por dentro; y por estado de la fase: sin aprobar, aprobada y sin fase.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_el_freno.py`; las de los programas que cambia: las del instalador y las del enganche de antes; `validar.py estandar`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
{mat}

**Cobertura:** 1 de 1 criterio de esta fase, en sus capas 1 y 2, y el RNF-06.

## 6. Casos de prueba

{casos}

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Algo fuera del plan pasa, o algo permitido se detiene | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios y RNF con caso / criterios y RNF de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
"""


def escribir(nombre, texto):
    os.makedirs(D, exist_ok=True)
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8", newline="\n") as s:
        s.write(texto)


def plan_pruebas():
    filas, casos = [], []
    for cp, titulo, pre, datos, pasos in CPS:
        ca = "RNF-06" if cp == "CP-006" else "CA-02"
        tipo = "Trazabilidad" if cp == "CP-006" else "Funcional"
        prioridad = "Media" if cp == "CP-006" else "Alta"
        filas.append("| HU-007 | %s | %s | %s | %s | %s | ☐ |" % (ca, cp, tipo, prioridad, "Parcial" if cp == "CP-006" else "Sí"))
        tabla = "\n".join("| %d | %s | %s |" % (i, a, b) for i, (a, b) in enumerate(pasos, 1))
        casos.append("### %s · %s\n\n| Campo | Valor |\n|---|---|\n| **HU / CA** | HU-007 / %s |\n"
                     "| **Precondiciones** | %s |\n| **Datos de entrada** | %s |\n\n"
                     "| # | Acción | Resultado esperado |\n|---|---|---|\n%s" % (cp, titulo, ca, pre, datos, tabla))
    escribir("plan_pruebas.md", PRUEBAS.format(f=FASE, mat="\n".join(filas), casos="\n\n".join(casos)))


def estado():
    origen = glob.glob(os.path.join(HU_DIR, "A-EP-023-*", "estado-fase.md"))[0]
    t = io.open(origen, encoding="utf-8").read()
    t = t.replace(os.path.basename(os.path.dirname(origen)), FASE)
    pares = [
        ("(módulo `base/`, `plantillas/` y `validadores/`)", "(módulo `validadores/` y `adaptadores/claude-code/`)"),
        ("| **Módulo** | `base/`, `plantillas/` y `validadores/` |", "| **Módulo** | `validadores/` y `adaptadores/claude-code/` |"),
        ("| **Última actualización** | 2026-10-02 |", "| **Última actualización** | 2026-10-03 |"),
        ("**Estación actual:** 12, commit. **Última puerta pasada:** 11.", "**Estación actual:** 7, planificador de tareas. **Última puerta pasada:** 6."),
        ("☑ Análisis 1 y 8 del pendiente 103", "☑ Análisis 1, 8 y 10 del pendiente 103"),
        ("☑ Los análisis 1 y 8, aprobados", "☑ Los análisis 1, 8 y 10, aprobados"),
        ("| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ El 2026-10-02 |", "| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ El 2026-10-03 |"),
        ("N/A: la especificación son los CA-01, CA-03 y CA-04", "N/A: la especificación es el CA-02"),
        ("☑ Aprobados el 2026-10-02", "☐ Escritos; esperan la aprobación"),
        ("| 8 | Implementador | implementado + pruebas verdes | ☑ Las 8 tareas; las pruebas de la fase pasan |", "| 8 | Implementador | implementado + pruebas verdes | ☐ |"),
        ("| 9 | Verificador | trazabilidad sin faltantes | ☑ `flujo` sin fallas |", "| 9 | Verificador | trazabilidad sin faltantes | ☐ |"),
        ("| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |", "| 10 | Crítico | sin hallazgos graves | ☐ |"),
        ("| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado de pruebas, HU y registro de cambios |", "| 11 | Cierre documental + señales | docs y señales al día | ☐ |"),
        ("| 12 | Commit | 👤 autorizado | ✅ `34be029` |", "| 12 | Commit | 👤 autorizado | ☐ |"),
        ("**Hechas:** 8 de 8. **Bloqueadas:** ninguna.", "**Hechas:** 0 de 8. **Bloqueadas:** todas, hasta que se aprueben los planes."),
        ("| **Concepto** | Cumple |", "| **Concepto** | Sin ejecutar |"),
        ("| **CA cumplidos** | 3 de 3 |", "| **CA cumplidos** | 0 de 1 |"),
        ("## 3. Pendiente / preguntas abiertas\n\nNinguna.\n", "## 3. Pendiente / preguntas abiertas\n\n- Que el usuario apruebe el plan de trabajo y el de pruebas.\n"),
    ]
    for a, b in pares:
        assert t.count(a) == 1, a
        t = t.replace(a, b)
    escribir("estado-fase.md", t)


def fila_en_la_hu():
    p = os.path.join(HU_DIR, HU_DOC)
    s = io.open(p, encoding="utf-8").read()
    m = re.search(r"^\| \[`A-EP-023-HU-007-[^\n]*\|$", s, re.M)
    assert m
    fila = ("| [`%s`](%s/estado-fase.md) | CA-02, capas 1 y 2 | Fase `A`, HU-002 | [plan](%s/plan_trabajo.md) | "
            "[pruebas](%s/plan_pruebas.md) | Pendiente | Planes escritos, sin aprobar |" % (FASE, FASE, FASE, FASE))
    s = s[:m.end()] + "\n" + fila + s[m.end():]
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


if __name__ == "__main__":
    import sys
    escribir("plan_trabajo.md", PLAN.format(f=FASE, hu=HU_DOC, p=P103, hurel=HU_REL))
    plan_pruebas()
    estado()
    if "--sin-fila" not in sys.argv:
        fila_en_la_hu()
