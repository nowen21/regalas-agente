# Resultado de Pruebas — Fase B-EP-005-HU-003-el-hallazgo-grave-detiene

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos están en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-003-el-hallazgo-grave-detiene` |
| **HU** | [HU-003 Disparo al escribir un archivo](../HU-003-disparo-al-escribir-un-archivo.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md) |
| **Ambiente** | Un proyecto de mentira en carpeta temporal, con el enganche real |

### 0.1 Por qué esta corrida se hizo por el camino real

No se llamó a la función: **se corrió el enganche como lo corre la herramienta**, con su JSON por la entrada estándar y mirando su código de salida. Es la única forma de comprobar lo que la fase promete, porque lo que detiene no es el hallazgo: es el código 2 que la herramienta interpreta.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 |

## 2. Ejecución caso por caso

| Caso | Qué se hizo | Resultado |
|---|---|---|
| CP-001 · la falla detiene | escribir un `.md` con un enlace roto y correr el enganche | ✅ **código 2**, y el mensaje nombra el archivo, la línea y el enlace que no resuelve |
| CP-002 · el aviso no detiene | escribir un `.md` sano y correr el enganche | ✅ **código 0**, sin una línea de salida |
| CP-003 · el archivo queda entero | releer el archivo después de que el enganche lo rechazara | ✅ el contenido está intacto: el enganche **no escribe ni revierte nada** |
| CP-004 · los dos transversales que ya pasaban | que sin JSON válido y con un archivo fuera del proyecto no haga nada | ✅ los dos siguen en 0 |

**La salida literal del CP-001:**

```
La edición dejó enlaces rotos:
  [FALLA] …/docs/roto.md:3 — enlace roto: no-existe.md
```

## 3. Qué quedó comprobado, y qué precedente deja

**Lo grave detiene, lo demás no.** El enganche mira solo los hallazgos de severidad falla; un aviso no cambia el código de salida. Eso es lo que la fase venía a asegurar, y de paso contesta con un caso real la pregunta que el pendiente 59 hacía en cuatro sitios distintos: **detiene lo que se comprueba sin criterio**.

**Y detener no es romper.** El archivo escrito por el agente se queda como está; lo que hace el enganche es devolverle el problema al modelo para que lo corrija. Un enganche que revirtiera la escritura sería mucho más difícil de confiar.

## 4. Defectos encontrados

**Ninguno.** El único límite que vale anotar es de alcance: el enganche mira **enlaces e índices**, no todo lo que podría estar mal en un `.md`. Ampliarlo sin medir el ruido sería el camino conocido para que alguien lo apague.

## 5. Veredicto de la fase

**Cumple.** Cuatro casos de cuatro.

| Criterio | Veredicto |
|---|---|
| Un documento con un incumplimiento grave no se puede dejar así | ✅ Cumple |
| Detenerlo no rompe nada | ✅ Cumple |
