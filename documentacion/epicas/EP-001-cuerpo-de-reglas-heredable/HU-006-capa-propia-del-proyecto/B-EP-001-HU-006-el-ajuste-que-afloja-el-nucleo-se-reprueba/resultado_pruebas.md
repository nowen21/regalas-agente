# Resultado de Pruebas — Fase `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el CA-03 se ejecutó por primera vez. Falló, se construyó la comprobación que faltaba, y ahora el caso malo se reprueba y el bueno pasa. El rojo de la fase `A` era cierto el 2026-08-17 y siguió siéndolo hasta hoy: nadie lo había podido provocar.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| Casos comprobados leyendo en vez de corriendo | 0 | **0** |
| Pruebas nuevas en verde | 2 | **2** |

---

## 3. Resultado por caso

### CP-001 — La regla que afloja una blindada se reprueba

**Antes de construir nada**, con el catálogo que declara «afloja `N2`» y «deroga `N6`»:

```
hallazgos: 0
```

**Después**, sobre el mismo catálogo:

```
[FALLA] .agente/reglas-proyecto.md:3 — `P1` declara que afloja `N2`, que está
        `[BLINDADA]` — M7 lo prohíbe: un ajuste del proyecto endurece el
        núcleo, nunca lo afloja
[FALLA] .agente/reglas-proyecto.md:9 — `P2` declara que deroga `N6`, que está
        `[BLINDADA]` — M7 lo prohíbe: un ajuste del proyecto endurece el
        núcleo, nunca lo afloja
```

**Resultado: pasa.**

### CP-002 — La regla que endurece una blindada pasa

Con un catálogo cuyo respaldo dice «concreta `N4`» y «concreta `C11`»:

```
hallazgos: 0
```

**Resultado: pasa.** Endurecer sigue siendo legítimo.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Qué no promete esta comprobación

Se mira **el verbo con que la regla declara su respaldo**. Un proyecto que contradiga el núcleo sin decirlo sigue sin detectarse, y eso queda escrito en el comentario del código. Prometer más sería el defecto que esta casa llama veredicto falso: enseña a ignorar los veredictos.

### 4.2 El estándar contra sus propias meta-reglas

`validar.py metareglas` sigue en «OK: sin incumplimientos» después del cambio.

---

## 5. Defectos encontrados

**Ninguno nuevo.** El defecto era el que la fase venía a medir.

---

## 6. Evidencias

- `validadores/metareglas.py`, `_afloja_una_blindada` y su uso en `validar_catalogo`
- `validadores/pruebas.py`, clase `ElAjusteDelProyectoNoAflojaElNucleo`
- La corrida: `Ran 2 tests in 0.097s — OK`
