# Resultado de Pruebas — Fase `B-EP-002-HU-001-el-numero-repetido-se-declara`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-001-el-numero-repetido-se-declara` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el CA-01 se mide ahora contra lo que la casa sostiene. `15.4.0` sigue apareciendo dos veces y **eso no cambió**: cambió que la prueba dejó de exigir una unicidad que el registro decidió no cumplir, y pasó a exigir lo que sí se sostiene, que la repetición esté declarada. La prueba salió del fallo esperado.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la clase en verde | 5 de 5 | **5 de 5** |
| Pruebas marcadas como fallo esperado | 0 | **0** |
| Líneas tocadas del `CHANGELOG.md` | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El registro real avanza, y lo repetido está declarado

```
Ran 5 tests in 0.013s
OK
```

Las 133 entradas del registro recorridas de la más vieja a la más nueva: ningún salto mal formado, ninguna versión que baje, y la única repetición viene con su marca.

**Resultado: pasa.**

### CP-002 — El repetido que no se declara sí falla

| Secuencia | Reclamos |
|---|---|
| `1.0.0`, `1.1.0`, `1.1.0` sin marca | **1** |
| `1.0.0`, `1.1.0`, `1.1.0` con marca | **0** |

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Un detalle que cambió la comprobación

La marca de repetido está en la entrada del **2026-08-15**, y en el archivo esa entrada aparece **debajo** de la del 14. Al recorrer la secuencia de vieja a nueva, la declarada queda como la anterior del par y no como la siguiente, así que mirar solo el encabezado del segundo la daba por callada.

Se cambió a mirar los dos encabezados del par. No es un rodeo: **lo que se exige es que la repetición esté dicha donde se lee el número**, y las dos entradas comparten ese número.

Salió al ejecutar. Leyendo el código no aparecía.

### 4.2 El aviso de `validar.py versionado` sigue saliendo

```
[AVISO] CHANGELOG.md — el registro tiene 2 entradas para la 15.4.0
```

Se conserva a propósito: la prueba dice que está bien declarado, y el aviso lo mantiene a la vista en cada corrida.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/pruebas.py`, clase `NumeroDeVersion`
- Las dos entradas `15.4.0` del `CHANGELOG.md`, sin tocar
