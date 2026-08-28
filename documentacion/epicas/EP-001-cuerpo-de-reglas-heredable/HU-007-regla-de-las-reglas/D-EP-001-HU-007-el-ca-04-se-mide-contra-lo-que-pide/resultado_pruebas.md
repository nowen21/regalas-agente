# Resultado de Pruebas — Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el `CA-04` pide **tres cosas** y las tres se cumplen, comprobadas corriendo `vigencia.py` y no citando a nadie.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 5 de 5 | 5 de 5 |
| Exigencias del criterio comprobadas | 3 de 3 | **3 de 3** |
| **Mediciones heredadas de la fase `A`** | 0 | **0** |
| Archivos que cambian al correrlo | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — Se obtiene la lista

```
251 reglas · 251 sin revisar de fondo · 0 con fecha

REGLA    REVISADA     SELLO DE     FALLA HOY
```

Cubre **las 251**, y lo dice en su propia salida.

### CP-002 — La lista dice cuándo y cuántos

| Lo que el criterio nombra | Columna |
|---|---|
| Cuándo se revisó | **`REVISADA`** |
| Cuántos incumplimientos produce hoy | **`FALLA HOY`** |

**Se comprueban por separado** en vez de dar por buena «la tabla».

### CP-003 — Está ordenada de la más vieja a la más nueva

**25 sellos leídos en el orden en que salen, y la secuencia no retrocede.** Las que no tienen sello van primero, que es lo correcto: son las que más llevan.

**Es el único caso que podía fallar de verdad.** Que la lista exista es fácil de ver; que esté ordenada es lo que el criterio exige y lo que nadie mira.

### CP-004 — El programa avisa, no corrige

Correrlo **no cambia ningún archivo**, comprobado contra el estado del repositorio antes y después.

### CP-005 — La ausencia de fechas es deliberada

El procedimiento lo dice en una línea:

> *«Arranca ausente en todas las reglas, a propósito. Ponérsela de una vez a las doscientas habría sido escribir doscientas fechas que no responden por ninguna revisión: el sello vacío que este documento viene a evitar.»*

Y el `CA-04`, leído entero, **no pide reglas revisadas** en ninguna parte.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué la fase `A` se equivocó

Su `CA-04` pide que **se sepa qué reglas llevan más tiempo sin revisarse**. Cerró en rojo citando *«249 de 249 sin dato»* — **una cifra que el criterio no menciona**.

**La lista existía, estaba ordenada y decía las dos cosas.** Lo que no existía era el trabajo de revisar, que es otra historia y ni siquiera es deuda: el procedimiento dice que arranca así a propósito.

**Es el segundo veredicto del día que mide algo de al lado**, y el primero —`EP-003·HU-002`— falló exactamente igual: encontró un hueco real y lo cobró en la factura equivocada.

### 4.2 Y el agente lo repitió, sabiéndolo

**Este trabajo se recomendó tres veces** como «la deuda de las 250 reglas», sin abrir el criterio ni el procedimiento. Se cayó en la primera lectura, y lo que obligó a leerlo fue **ir a ejecutarlo**.

`S-063` — *un veredicto puede estar mal el día que se escribe—* se había escrito **dos horas antes**. Nombrarlo no evitó repetirlo. Está en `S-069`.

### 4.3 El hallazgo de la fase `A` se conserva

Que **nadie hubiera revisado ninguna regla de fondo** era cierto, y sigue siéndolo. Lo que se corrige es dónde se cobra: **no es un incumplimiento del `CA-04`**, es trabajo por hacer cuando el usuario lo decida.

Y hay un dato que ese rojo tapaba: **la columna «falla hoy» está vacía en todas**. El procedimiento dice que ese número se lee en las dos direcciones — *«una regla vieja que no ha fallado nunca hay que mirarla por el motivo contrario: puede que ya nadie la esté aplicando»*.

### 4.4 Rastros

Ninguno. No se editó ningún documento para probar.

### 4.5 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Defectos encontrados

**Ninguno propio.** El único hallazgo es sobre el veredicto de la fase `A`, y está en el §4.1.

---

## 6. Evidencias

- La salida de `python validadores/vigencia.py`, con sus 251 reglas y sus columnas
- El `CA-04` transcrito palabra por palabra en el §2.1 del [plan de trabajo](plan_trabajo.md)
- El guion que lo midió, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
