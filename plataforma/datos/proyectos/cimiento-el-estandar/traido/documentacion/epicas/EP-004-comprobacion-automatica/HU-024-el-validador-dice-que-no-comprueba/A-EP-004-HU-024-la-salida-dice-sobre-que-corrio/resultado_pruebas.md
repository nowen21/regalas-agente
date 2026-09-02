# Resultado de Pruebas — Fase `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios se cumplen, y la frase del alcance sale de lo que la corrida recorrió, no de un texto escrito aparte.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas en verde | 5 | **5** |
| Frases escritas a mano en vez de derivadas | 0 | **0** |

---

## 3. Resultado por caso

### La corrida real, sobre este repositorio

```
0 falla(s), 746 aviso(s).
Alcance: se recorrió `base/`, `plantillas/` (189 archivos), que es lo que viaja
a los proyectos.
Y no se cuenta lo que hay que leer para verlo: el español de otra parte, la
estructura demasiado pareja, el tono, y el contraste con lo escrito antes.
```

### Y sobre un árbol sin nada en su alcance

```
OK: sin incumplimientos.
Alcance: no se miró ningún archivo: en `base/`, `plantillas/` no hay ninguno
que revisar.
```

**Los dos ceros ya no se leen igual**, que era todo el defecto.

### Las cinco pruebas

```
Ran 5 tests in 0.087s
OK
```

**La que sostiene a las otras es la `CP-002`:** un archivo de `documentacion/`
**con una marca** no se reporta, y la frase dice que no se miró. Es exactamente
el cero que el 2026-08-30 se leyó como aprobado y terminó publicado en el cuerpo
de un commit.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué el número va en la frase

Nombrar la carpeta no alcanza: «se recorrió `base/`» es cierto también cuando no
había un solo archivo. El número es lo que separa «miré y no hay» de «no había
qué mirar», y es el que hace que la frase no pueda escribirse de antemano.

### 4.2 Lo que esta fase no promete

El alcance sigue siendo `base/` y `plantillas/`. Ampliarlo es una decisión
aparte, y lo que cambia acá es que **deja de ser invisible**.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `validadores/marcas.py`, `alcance()` y el conteo de `validar()`
- `validadores/validar.py`, `cmd_marcas`
- `validadores/tests/test_el_validador_dice_sobre_que_corrio.py`
