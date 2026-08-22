# Resultado de Pruebas — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado` |
| **HU** | [HU-013 Comparar el plan con lo hecho](../HU-013-comparar-el-plan-con-lo-hecho.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión, del pendiente 59 |
|---|---|
| ¿contra qué se comparan los archivos tocados? | **Contra el commit del que salió la fase** (decisión 22): la rama arrastra trabajo ajeno y lo sin guardar cambia mientras se mira |
| ¿el `CA-03` se intenta comprobar o se declara criterio humano? | **Criterio humano** (decisión 10): comparar los pasos ejecutados con los escritos exige leer los dos textos y decidir si dicen lo mismo con otras palabras. Queda declarado en [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 del plan, 11 escritos | 11 | 11 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el archivo tocado y no declarado se avisa; el declarado, no | el corazón del `CA-01` | ✅ Aprobado |
| CP-002 · el formato que no se entiende se avisa, no se supone | tres casos: sin sección, sin plan, sin commit de origen | ✅ Aprobado |
| CP-003 · el criterio sin caso y el plan de pruebas sin casos se avisan | el `CA-02` | ✅ Aprobado, y con el criterio cubierto **se calla** |
| CP-004 · los documentos de la propia fase no cuentan | **el caso que decide** | ✅ Aprobado |
| CP-005 · nunca detiene | un archivo de más puede ser un descubrimiento aprobado | ✅ Aprobado |

## 3. La primera corrida encontró un incumplimiento del propio trabajo de hoy

**Y es el mejor argumento a favor de la herramienta.** Corrida sobre la fase del conteo por regla, cerrada media hora antes:

```
$ python validadores/validar.py plan --fase …/A-EP-004-HU-009-… --desde HEAD~1
[AVISO] validadores/conteo.py — lo tocó la fase y su plan no lo declara
[AVISO] validadores/docs/conteo.md — lo tocó la fase y su plan no lo declara
[AVISO] validadores/tests/test_el_conteo_por_regla.py — lo tocó la fase y su plan no lo declara
```

**Los tres son ciertos.** Ese plan, escrito el 2026-08-17, declaraba tocar `validadores/comun.py`, `validar.py`, `pruebas.py` y dos documentos: daba por hecho que el conteo viviría dentro de `validar.py`. Al construirlo se vio que era mejor un módulo propio, con su contrato y su archivo de pruebas, **y eso amplió el plan sin escribirlo**, que es exactamente lo que [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) prohíbe hacer en silencio.

**Queda dicho acá y no se disimula.** La decisión de separar el módulo fue buena; lo que faltó fue anotarla en el plan antes de ejecutar. Es el primer hallazgo real de este validador y es sobre quien lo escribió.

## 4. Sobre los otros trece avisos del repositorio

La corrida completa sobre las 113 fases con plan deja **13 avisos de criterios sin caso**, casi todos en fases viejas cuyo plan de pruebas nombra los criterios de otra forma. No se corrigieron acá: son de sus propias fases, y arreglarlos de paso sería repetir el defecto que esta misma fase acaba de encontrar.

## 5. Veredicto

**Cumple.** Once casos de once, y el `CA-03` declarado como criterio humano con su motivo escrito.
