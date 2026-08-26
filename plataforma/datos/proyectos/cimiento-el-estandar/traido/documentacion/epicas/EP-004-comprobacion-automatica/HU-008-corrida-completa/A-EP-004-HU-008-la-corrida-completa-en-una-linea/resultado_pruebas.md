# Resultado de Pruebas — Fase A-EP-004-HU-008-la-corrida-completa-en-una-linea

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-008-la-corrida-completa-en-una-linea` |
| **HU** | [HU-008 Corrida completa](../HU-008-corrida-completa.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) |
| **Ambiente** | El repositorio del estándar en `main`, versión 31.6.0 |

### 0.1 La duda que la detenía

**¿La corrida completa incluye linter, pruebas y audit, que son lentos?** **No.** Es la decisión 23 del pendiente 59, y el propio pendiente anotaba que ya estaba decidida al construirlo: `validar.py` nunca los llamó desde otro subcomando. Lo que faltaba era **escribirlo**, y ahora está escrito en el programa, con el motivo de cada exclusión a la vista de quien corra la línea.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 5 del plan, 7 escritos | 7 | 7 | 0 |

## 2. Ejecución caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · cada subcomando sigue corriendo por separado | que la corrida los **llame** y no los rehaga | ✅ Aprobado |
| CP-002 · una línea corre todo lo que aplica | 31 comprobaciones en una orden | ✅ Aprobado |
| CP-003 · lo que queda fuera dice por qué | sin motivo, «no corrió» se lee como «no hacía falta» | ✅ Aprobado |
| CP-004 · un subcomando nuevo entra solo | **el caso que decide** | ✅ Aprobado: la lista sale del propio analizador, no de una lista a mano |
| CP-005 · la corrida termina con un resumen único | leer 31 resúmenes es lo que se vino a evitar | ✅ Aprobado |
| CP-006 · el código de salida refleja la peor | sin eso no sirve en integración continua | ✅ Aprobado |
| CP-007 · el subcomando está en la ayuda | lo que no se ve, no se corre | ✅ Aprobado |

## 3. La corrida real, que es la evidencia

```
$ python validadores/validar.py todo
…
== Corrida completa · . ==
  (fuera: linter — corre la herramienta del proyecto y tarda; va aparte)
  (fuera: suite — corre la suite del proyecto y tarda; va aparte)
  (fuera: audit — sale a la red a preguntar por vulnerabilidades; va aparte)
  (fuera: plantilla — necesita que le digan qué documento revisar)
  (fuera: commit — necesita el mensaje del commit)
  (fuera: traza — necesita la transcripción de una sesión)
  (fuera: temas — escribe un archivo cuando se le pide `--aplicar`)
  (fuera: checklist · versiones · version — miden un proyecto instalado; acá estamos en el estándar)
31 comprobación(es) corridas · 0 con fallas
```

## 4. Defectos encontrados, y los tres que la primera corrida destapó

**La primera corrida terminó con tres fallas, y las tres eran ciertas:**

1. **`amarre`** — `guardian_version.py`, `sitio.py` y `temas.py`, nacidos hoy, no estaban en el mapa de qué se queda si mañana el agente es otro. **Se clasificaron.** Es exactamente para lo que ese mapa tiene su comprobación.
2. **`checklist`** y **`versiones`** — decían que al estándar le falta estar instalado como proyecto. **No es deuda: es que la pregunta no aplica.** El estándar no es un proyecto que herede el estándar. Se dejan fuera cuando la carpeta revisada **es** el estándar, con el motivo escrito.

**Sin la corrida completa, esas tres habrían seguido invisibles**, porque nadie corre `amarre` a mano después de agregar un módulo.

## 5. Veredicto de la fase

**Cumple.** Siete casos de siete.

| Criterio | Veredicto |
|---|---|
| CA-01 · una línea dice cómo está el proyecto | ✅ Cumple |
| CA-02 · cada comprobación sigue corriendo por separado | ✅ Cumple |
| Transversal · lo que no corre dice por qué | ✅ Cumple |
