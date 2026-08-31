# Resultado de Pruebas — Fase `B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la decisión del usuario está aplicada y comprobada. Lo que la fase `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` declaró en rojo el 2026-08-17 era cierto entonces, y siguió siéndolo hasta que hubo decisión: no era trabajo pendiente, era una pregunta sin responder.

| Métrica | Real |
|---|---|
| Señales activas diciendo lo contrario del recuerdo | 0 |
| La señal vieja, conservada | Sí, como `reemplazada` |
| La nueva, enlazada a la que reemplaza | Sí |

---

## 3. Resultado por caso

### CP-001 — Las dos copias ya no se contradicen

Antes:

```
S-002  activa   Terminologia: 'el agente' = Claude Code; 'el estandar' = las reglas
```

Después:

```
S-002  reemplazada  Terminologia: 'el agente' = Claude Code; 'el estandar' = las reglas
S-269  activa       reemplaza=S-002  Terminologia: el agente es Cimiento, y no es Claude Code
```

**Resultado: pasa.** La `S-269` dice lo mismo que el recuerdo, y la vieja queda con su rastro.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué este rojo no se cerraba midiendo

Es de los que pedían una decisión, no trabajo. Medirlo otra vez habría dado el mismo resultado todos los días: el dato no cambiaba, faltaba saber qué se quería hacer con él. Está en `S-085`.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- La decisión del usuario, en la transcripción del 2026-08-30
- Las cuentas del §3, tomadas sobre el árbol y la base
