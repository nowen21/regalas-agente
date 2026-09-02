# Resultado de Pruebas — Fase `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** las cinco historias que se contaban como «no dicen si cumplen» lo decían. El lector reconoce ahora las dos formas que faltaban, y la cuenta de mudas queda en cero sin que ninguna fase cambie de «No cumple» a «Cumple».

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la clase en verde | 35 | **35** |
| Fases que pasan de «No cumple» a «Cumple» | 0 | **0** |
| Historias sin veredicto | 0 | **0**, eran 5 |

---

## 3. Resultado por caso

### CP-001 y CP-002 — Las dos formas que faltaban

Antes y después, sobre el árbol real:

```
antes:    109 cumplen ·  0 no cumplen ·  5 sin veredicto
después:  114 cumplen ·  0 no cumplen ·  0 sin veredicto
```

Las cinco, leídas una por una:

| Fase | Cómo lo escribe | Ahora se lee |
|---|---|---|
| `A-EP-003-HU-001-marca-de-espacio-por-llenar` | `## 6. Concepto final` | Cumple |
| `A-EP-003-HU-009-modelo-del-resumen-de-sesion` | `## 6. Concepto final` | Cumple |
| `A-EP-003-HU-010-glosario-de-la-terminologia` | `**Concepto: Cumple.**` | Cumple |
| `A-EP-005-HU-015-el-portero-del-contenido-externo` | `**Concepto: Cumple.**` | Cumple |
| `A-EP-005-HU-016-el-lector-de-la-traza` | `**Concepto: Cumple.**` | Cumple |

**Resultado: pasan.**

### CP-003 — La tabla de criterios no se toma por el veredicto

Un resultado con la tabla de criterios en «Cumple» y el veredicto de la fase en
«No cumple» devuelve `(0, 1, 0)`.

**Resultado: pasa.** Es la prueba que sostiene a las otras dos: sin ella,
ampliar el lector sería aflojarlo.

```
Ran 35 tests in 2.701s
OK
```

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Cuatro fases para el mismo lector, y cada una encontró lo que la anterior no miró

Vale dejarlo dicho porque es un patrón, no una casualidad:

| Fase | Qué agregó | Qué no había mirado |
|---|---|---|
| `A` | Que la cuenta mire el veredicto | — |
| `B` | La palabra sola bajo el encabezado | Contó las formas que ya sabía buscar |
| `C` | El mismo encabezado sin «de la fase» | La `B` dijo «39 sin encabezado» y eran 2 |
| `D` | Los dos puntos dentro de la negrita, y el título «Concepto» | Las cinco que quedaban, que nadie había abierto |

**Lo que se repite es la forma de equivocarse:** contar lo que el programa ya
sabe reconocer y llamar «otra cosa» a todo lo demás, sin abrirlo. Las cinco de
esta fase se resolvieron leyéndolas una por una, que es lo que ninguna de las
tres anteriores hizo con las que le quedaban.

### 4.2 No se tocó ninguno de los cinco resultados

Son fases cerradas. Se corrige quien lee, no lo leído (`20·M11`).

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/fases.py`, los patrones `_VEREDICTO` y `_VEREDICTO_CONCEPTO_TITULO`
- `validadores/pruebas.py`, clase `LaCuentaMiraElVeredicto`
- El guion que listó las mudas: `historico-chat/scripts/2026-08-30/medir-lo-que-queda.py`
