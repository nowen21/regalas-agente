# Resultado de Pruebas — Fase A-EP-005-HU-011: dónde termina el estándar

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| CA | Caso | Veredicto |
|---|---|---|
| **CA-01** · toda pieza tiene su columna | CP-001, CP-002 | ✅ **Pasa** |
| **CA-02** · cada amarrada dice qué se pierde | CP-003 | ✅ **Pasa** |
| **CA-03** · el mapa se queda viejo y se nota | CP-004, CP-005, CP-006 | ✅ **Pasa** |
| No regresión | — | ✅ `tests/` **334 · OK** · `pruebas.py` 357 · `estandar` limpio |

**12 casos automatizados** en [validadores/tests/test_el_mapa_del_amarre_no_envejece.py](../../../../../validadores/tests/test_el_mapa_del_amarre_no_envejece.py).

---

## 2. La medición

| | |
|---|---|
| Piezas en `validadores/` | **54** |
| Amarradas a la herramienta | **18** |
| Libres | **36** — funcionan con cualquier agente, o sin ninguno |

**El adaptador de verdad son los ocho `hook_*` más `instalar.py`**, que los enchufa. El resto está amarrado por el borde y se despega con poco.

---

## 3. El hueco que `CA-03` destapó, y no era el que decía

El criterio pide que una pieza **nueva** sin clasificar se reporte. Al construirlo apareció que el mapa ya tenía el hueco **sin que hubiera pieza nueva**: nombraba las 18 amarradas una por una y las libres **solo por su total**.

**Veintiocho piezas no estaban nombradas en ningún lado.** Entraban en un número y nadie las había mirado.

Ahora las 36 van por su nombre. **Un total no es una clasificación**: es la promesa de que alguien clasificó.

---

## 4. El segundo lado, que la historia no pedía

El criterio nombra **una** forma de envejecer: la pieza que existe y el mapa no nombra.

**Hay otra:** la pieza que el mapa nombra y **ya no existe**. Un mapa que promete clasificar algo que se borró miente igual que uno al que le falta algo, y `CP-006` la fija.

---

## 5. `CP-005` es el caso que decide, y por qué

Después de clasificar la pieza, la comprobación tiene que **callarse**.

**Sin él, `CP-004` pasaría con un programa que reporta siempre.** Y uno que reporta siempre se apaga a la semana — es el patrón que apareció **cinco veces** en este repositorio: `avisar()` sin llamar, el `CP-005` del instalador con un solo registro, el detector de secretos revisando el estándar, el recuento de huérfanas buscando en todo el archivo, y este.

> **Una comprobación que pasa sin comprobar.** Es la forma de defecto más cara del repositorio, porque figura como cubierta.

---

## 6. Lo que no se comprueba, y está declarado

**Si la clasificación es la correcta.** Que `pruebas.py` sea «pruebas *de* los adaptadores» y no adaptador es un juicio, y se lee.

---

## 7. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 |
