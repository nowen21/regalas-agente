# Plan de Pruebas — Fase A-EP-005-HU-011-donde-termina-el-estandar   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-011 · **Fecha** 2026-08-18 |
| **Aprobado por** | Sin aprobar — va con el [`plan_trabajo.md`](plan_trabajo.md) |

## 3. Estrategia

**Lo que se comprueba:** que ninguna pieza quede fuera del mapa, por los dos lados — la que existe y no está nombrada, y la que está nombrada y ya no existe.

**Lo que NO se comprueba, y se declara:** **si la clasificación es la correcta**. Que `pruebas.py` sea «pruebas *de* los adaptadores» y no adaptador es un juicio, y se lee. El programa comprueba que **esté clasificada**.

## 5. Trazabilidad

| CA | Casos |
|---|---|
| `CA-01` · toda pieza tiene su columna | CP-001, CP-002 |
| `CA-02` · cada amarrada dice qué se pierde | CP-003 |
| `CA-03` · el mapa se queda viejo y se nota | CP-004, CP-005, CP-006 |

## 6. Casos

### CP-001 — Las 53 piezas están en el mapa
- **Esperado:** ninguna sin nombrar. Hoy son 53; el número lo dice el programa, no el plan.

### CP-002 — El recuento del programa coincide con el del mapa
- **Esperado:** iguales. **Si difieren, el mapa miente aunque esté completo** — es el riesgo `R-01`.

### CP-003 — Cada pieza amarrada dice qué se pierde
- **Esperado:** ninguna fila de la tabla de amarradas sin su columna de consecuencia.

### CP-004 — Una pieza nueva sin clasificar se reporta
1. Crear `validadores/zzz_prueba.py` con una marca de herramienta, sobre una copia.
2. Correr la comprobación.
- **Esperado:** la reporta por su nombre. **Es el criterio literal de la historia.**

### CP-005 — Clasificarla la calla
1. Agregarla al mapa. 2. Volver a correr.
- **Esperado:** no reporta nada. **Sin este caso, CP-004 podría pasar con un programa que reporta siempre.**

### CP-006 — Una pieza que el mapa nombra y ya no existe se reporta
1. Borrar de la copia un archivo que el mapa nombra.
- **Esperado:** lo reporta. **El mapa envejece por los dos lados**, y la historia solo nombra uno.

## 9. Criterio de la corrida

**Pasa** si los seis pasan y las dos suites quedan en verde.

**No pasa** si CP-005 falla: un programa que reporta siempre no distingue nada, y sería peor que no tenerlo — se apagaría a la semana.
