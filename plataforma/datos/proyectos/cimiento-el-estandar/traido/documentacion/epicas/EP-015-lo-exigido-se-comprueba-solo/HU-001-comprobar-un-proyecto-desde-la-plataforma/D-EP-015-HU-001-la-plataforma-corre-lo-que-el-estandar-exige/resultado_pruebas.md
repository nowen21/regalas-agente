# Resultado de Pruebas — Fase `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige` |
| **HU** | [HU-001 Comprobar un proyecto desde la plataforma](../HU-001-comprobar-un-proyecto-desde-la-plataforma.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **13** |

**Este repositorio, comprobado desde la plataforma:**

| | Cuánto |
|---|---|
| Comprobaciones corridas | **32** |
| Con fallas | 1 |
| Fallas reportadas, con archivo y línea | 2 |
| **Cuánto tardó** | **116,9 segundos** |
| Archivos modificados | **0** |
| Dependencias nuevas | **0** |

**Las dos fallas que salieron eran reales**, y del propio trabajo de esta fase: dos enlaces a documentos que todavía no existían. La funcionalidad encontró un incumplimiento verdadero en su primera corrida.

---

## 2. Ejecución caso por caso

### CP-001 — Un proyecto que cumple pasa

El veredicto dice cuántas comprobaciones corrieron: **32**. Sin ese número no se sabría si miró algo, y por eso va siempre, cumpla o no.

**Resultado: pasa.**

### CP-002 — Uno que no cumple es rechazado, con archivo y línea

```
No cumple. 2 falla(s):
  documentacion/comprobaciones/spec.md:107
      enlace roto: .../D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige/estado-fase.md
```

Cada falla trae la ruta con su número de línea. **Un aviso no cuenta como falla**: el estándar los marca distinto y acá se respeta esa diferencia.

**Resultado: pasa.**

### CP-003 — Sin el estándar, no hay veredicto

**El caso que decide la fase.**

| Entrada | Salió |
|---|---|
| Una carpeta sin `base/` | Se dice que no hay contra qué comprobar |
| Una carpeta que ya no está | Se dice |
| Un proyecto que no está registrado | Se dice |

En los tres, **ni «cumple» ni «no cumple»**. Un proyecto sin el estándar no está en verde: está sin comprobar.

**Resultado: pasa.**

### CP-004 — Comprobar no modifica nada

Retrato de la carpeta antes y después: idéntico. El módulo solo lee.

**Resultado: pasa.**

### CP-005 — Cero comprobaciones es rojo

| Veredicto | Cumple |
|---|---|
| 0 corridas, 0 fallas | **No** |
| 32 corridas, 0 fallas | Sí |
| 32 corridas, 1 falla | No |
| No se pudo comprobar | No |

**Resultado: pasa.**

---

## 3. Los 116,9 segundos, y qué se hace con eso

El plan pidió medir el tiempo y escribirlo, fuera el que fuera. **Son casi dos minutos**, y es el bloqueo `B-01` de esta fase.

**Qué se puede decir hoy:** para pedirlo cuando uno quiere saber si un proyecto está bien, dos minutos se aguantan. Para pedirlo cada vez que se guarda un archivo, no.

**Qué no se puede decir todavía:** si eso alcanza. La respuesta depende de dónde se enchufe, y hoy no está enchufado en ninguna parte. **Queda declarado, sin pendiente**, para que quien lo enchufe lo decida con el número delante y no lo descubra después.

**El `B-01` queda abierto y dicho.**

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las 2 fallas reportadas | Reales: dos enlaces a documentos que no existían todavía |
| Que la salida no traiga credenciales | Pasa por el tapador antes de mostrarse |
| Que la carpeta no cambiara | No cambió |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| CA-01 | CP-001, §1 | **Cumple** |
| CA-02 | CP-002, §1 | **Cumple** |
| CA-03 | CP-003 | **Cumple** |
| CA-04 | CP-004 | **Cumple** |
| CA-05 | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| El veredicto con archivo y línea | Hecho |
| Distinguir «sin comprobar» de «no cumple» | Hecho, y es lo que decide la fase |
| Correrlo sobre este repositorio | Hecho: **32 comprobaciones, 116,9 s** |
| El tiempo escrito, sea el que sea | **Escrito, y declarado como lo que hay que vigilar** |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

La plataforma ya dice si un proyecto cumple lo que las reglas exigen, sin entrar a él, y lo dice con el archivo y la línea. **No duplica ni una comprobación:** le pide al estándar que corra las suyas, que es la tercera vez que la plataforma usa esa forma.

**Lo que la fase encontró de verdad:** dos enlaces rotos de su propio trabajo, en la primera corrida.

**Y lo que queda dicho sin resolver:** los 116,9 segundos. Se aguantan para pedirlo a mano; no para pedirlo seguido. Quien lo enchufe en algún sitio tendrá que decidirlo con el número delante.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 13 pruebas del módulo | `plataforma/nucleo/comprobaciones/tests.py` |
| EV-02 | La corrida sobre este repositorio | §1 y §2 |

**Las dos baterías:** 733 pruebas del estándar y 328 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
