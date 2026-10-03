# -*- coding: utf-8 -*-
"""Fase B de la HU-007: resultado de las pruebas, lo implementado, el estado y la fila en la HU."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU_DIR = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-007-*"))[0]
HU_DOC = "HU-007-nada-se-escribe-fuera-del-plan-aprobado.md"
FASE = "B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar"
D = os.path.join(HU_DIR, FASE)
P109 = ("../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/"
        "pendientes/109-las-pruebas-del-freno-describen-el-freno-viejo/pendiente.md")

RESULTADO = """# Resultado de Pruebas · Fase `{f}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `{f}` |
| **HU** | [HU-007](../{hu}) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-03 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `2dad127` más los cambios de la fase, versión 51.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-02 | Alta | `test_el_freno.py` (6 pruebas) y `test_nada_fuera_del_plan.py` (5 de lo autorizado) | Sin aprobar el plan pasan solo los documentos de la fase; aprobado, lo que declara; sin fase en curso, lo autorizado, incluida la HU; lo que el análisis prendido manda hacer de una pasa; afuera, también con `..`, se detiene; solo la regla vigente autoriza; el instalador pone el freno sobre toda acción | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `test_el_freno.py` (3 pruebas) | Redirigir, copiar o borrar fuera del plan se detiene; el segundo plano, instalar paquetes, la configuración global y el proceso que queda corriendo se detienen; lo que solo lee pasa | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `test_el_freno.py` (1 prueba) | La herramienta que publica se pregunta; la de lectura pasa | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-02 | Alta | `test_el_freno.py` (1 prueba) en un repositorio de git temporal | Después de la orden, avisa el archivo no declarado; no cuenta el que ya estaba cambiado ni el declarado | Aprobado | EV-01 | Ninguno |
| CP-005 | CA-02 | Alta | `test_el_freno.py` (2 pruebas) | El resumen suma el hallazgo una sola vez, antes del cierre; el enganche detiene y dice que se vuelve al análisis | Aprobado | EV-02 | Ninguno |
| CP-006 | RNF-06 | Media | `validar.py flujo` | Ninguna tarea sin su criterio | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 6 casos en el plan, 6 acá.

**Qué salió distinto de lo esperado:**

- El H-14: una prueba de la fase `A` contaba exactamente diez reglas. El análisis 11 la cambió por reglas de ejemplo y el plan pasó a su versión 2.
- El H-15: fallan tres pruebas de la EP-005 que describen el freno viejo. No afectan esta fase; su pendiente es el [109]({p109}).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Marcas de `00·ID8` en lo que escribió la fase | `validar.py marcas --preparados` | Ninguna nueva |
| 2 | Coherencia del estándar, mapa de tareas y origen | `validar.py estandar`, `tareas` y `origen` | Sin fallas |
| 3 | Que los programas que cambió la fase sigan andando | Las 114 pruebas del instalador, el análisis y los acuerdos | Pasan |

## 4. Defectos encontrados

Ninguno en esta fase.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-02, capas 1 y 2 | CP-001 a CP-005 | Aprobado | Sí |
| RNF-06 | CP-006 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 6 de 6 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple. Espera la aprobación del usuario.

**Justificación:** el CA-02, en sus capas 1 y 2, y el RNF-06 tienen sus casos ejecutados y aprobados. Las pruebas de la fase pasan: 13 de `test_el_freno.py` y 16 de `test_nada_fuera_del_plan.py`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa, enganches e instalador | `validadores/freno.py`, `validadores/autorizado.py`, `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py`, `validadores/instalar.py` |
| EV-02 | Pruebas, reglas y plantilla | `validadores/tests/test_el_freno.py`, `validadores/tests/test_nada_fuera_del_plan.py`, `13·DOC15`, `13·DOC16`, `02·F23`, `plantillas/analisis.md` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-03 | 6 | 0 | Primera ejecución |
"""

FUNCIONALIDAD = """# Funcionalidad implementada · Fase `{f}` (módulo `validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{f}` |
| **Módulo** | `validadores/` y `adaptadores/claude-code/` |
| **Especificación del módulo** | El CA-02 de la [HU-007](../{hu}), en sus capas 1 y 2 |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-007 (CA-02, capas 1 y 2) |
| **Fecha de cierre** | 2026-10-03 |
| **Versión del estándar al cerrar** | 51.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Antes de toda acción, el freno detiene lo que no está en el plan de la fase en curso ni lo autoriza una regla vigente, por cualquier canal: la herramienta de escritura, la consola, el segundo plano, las instalaciones y los procesos que quedan corriendo; lo que se publica se pregunta. Después de cada orden de consola compara lo que cambió en git. Al detener, anota el hallazgo en el resumen de la sesión.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-02, capa 1: antes de actuar | Programa y enganche | `validadores/freno.py`, `adaptadores/claude-code/hook_antes.py` | ✅ | CP-001 a CP-003, CP-005 |
| CA-02, capa 2: después de actuar | Programa y enganche | `validadores/freno.py`, `adaptadores/claude-code/hook_despues.py` | ✅ | CP-004 |
| Lo autorizado: reglas vigentes, HU, épica y pendiente | Programa y reglas | `validadores/autorizado.py`, `13·DOC15`, `13·DOC16`, `02·F23` | ✅ | CP-001 |
| La instalación | Instalador | `validadores/instalar.py` | ✅ | CP-001 |

**Faltantes / diferimientos:** la capa 4 y el contrato de cada adaptador van en la fase `C`.

### 2.2 Plan de trabajo → ejecución

Las 10 tareas de la versión 2 del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase y las de los programas que cambió.
- Defectos abiertos que se aceptaron: ninguno. Las tres pruebas de la EP-005 que describen el freno viejo quedan en el [pendiente 109]({p109}).

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Los dos enganches corren solos una vez que el instalador los pone. La fila de un análisis que se hace «de una y sin fase» nombra sus rutas exactas para que el freno las deje pasar.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La capa 2 compara con una foto tomada antes de cada orden, guardada en `.git/` | Lo que ya estaba cambiado, por ejemplo de otra sesión, no lo hizo esa orden | Por escribir |

## 6. Deuda técnica y pendientes generados

El [pendiente 109]({p109}), en la HU-023 de EP-005.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `anatomia/mapa-del-sitio.md`: el programa nuevo.
- [x] `base/mapa-de-tareas.md`, regenerado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 51.0.0 con el instalador.
"""


def cambiar(p, pares):
    t = io.open(p, encoding="utf-8").read()
    for a, b in pares:
        assert t.count(a) == 1, (p, a)
        t = t.replace(a, b)
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)


def main():
    for nombre, molde in (("resultado_pruebas.md", RESULTADO), ("funcionalidad_implementada.md", FUNCIONALIDAD)):
        io.open(os.path.join(D, nombre), "w", encoding="utf-8", newline="\n").write(molde.format(f=FASE, hu=HU_DOC, p109=P109))
    cambiar(os.path.join(D, "estado-fase.md"), [
        ("**Estación actual:** 8, implementador. **Última puerta pasada:** 7.", "**Estación actual:** 12, commit. **Última puerta pasada:** 11."),
        ("| 8 | Implementador | implementado + pruebas verdes | ☐ |", "| 8 | Implementador | implementado + pruebas verdes | ☑ Las 10 tareas; las pruebas de la fase pasan |"),
        ("| 9 | Verificador | trazabilidad sin faltantes | ☐ |", "| 9 | Verificador | trazabilidad sin faltantes | ☑ `flujo` y `origen` sin fallas |"),
        ("| 10 | Crítico | sin hallazgos graves | ☐ |", "| 10 | Crítico | sin hallazgos graves | ☑ H-14 resuelto por el análisis 11; H-15 en el pendiente 109 |"),
        ("| 11 | Cierre documental + señales | docs y señales al día | ☐ |", "| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado de pruebas, cierre, HU y registro de cambios |"),
        ("**Hechas:** 9 de 10 (todas menos la T-08, de cierre).", "**Hechas:** 10 de 10."),
        ("| **Concepto** | Sin ejecutar |", "| **Concepto** | Cumple |"),
        ("| **CA cumplidos** | 0 de 1 |", "| **CA cumplidos** | 1 de 1, en sus capas 1 y 2 |"),
        ("Ninguna. El H-15 no afecta al plan en curso: su pendiente, el 109, vive en la HU-023 de EP-005, y la fase sigue.\n",
         "- Que el usuario apruebe la fase y autorice el commit.\n"),
    ])
    p = os.path.join(D, "plan_pruebas.md")
    t = io.open(p, encoding="utf-8").read()
    t = t.replace(" | ☐ |\n", " | ☑ |\n")
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
    cambiar(os.path.join(HU_DIR, HU_DOC), [
        ("[pruebas](%s/plan_pruebas.md) | Pendiente | Planes aprobados; en ejecución |" % FASE,
         "[pruebas](%s/plan_pruebas.md) | [resultado](%s/resultado_pruebas.md) | Cumple; espera la aprobación |" % (FASE, FASE))])


if __name__ == "__main__":
    main()
