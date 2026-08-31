# Resultado de Pruebas — Fase `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la regla existe, cumple su molde, no fija ningún idioma, y el modelo de manual de instalación la cita en vez de repetirla. El de manual de usuario queda declarado y sin tocar, por una razón que se explica en el §4.2.

| Métrica | Meta | Real |
|---|---|---|
| Incumplimientos de meta-reglas | 0 | **0** |
| Idiomas nombrados en el cuerpo | 0 | **0** |
| Caracteres del cuerpo, leídos | 320 o menos | **300** |
| Archivos de otra sesión tocados | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — La regla existe y cumple su molde

```
== El estándar contra sus meta-reglas · . ==
OK: sin incumplimientos.
```

Con la regla contada entre las del capítulo, su bloque de checklist aplicado y su clasificación puesta.

**Resultado: pasa.**

### CP-002 — No fija un idioma

El cuerpo dice «la variedad del idioma que usa el proyecto». No nombra ningún idioma ni ningún país. Un proyecto que trabaje en otro idioma la cumple igual, y esa es la condición para que el estándar siga siendo heredable.

**Resultado: pasa.**

### CP-003 — Los modelos citan en vez de repetir

| Modelo | Estado |
|---|---|
| Manual de instalación | Cita la regla con su enlace, y conserva **lo propio de un manual**: que lo que aparece en pantalla se copie tal cual, aunque diga «usted» |
| Manual de usuario | **Sin tocar**, y declarado |

**Resultado: pasa a medias**, y la mitad que falta no es trabajo pendiente sino un archivo ajeno.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué una norma dentro de un documento modelo no alcanza

**Solo la hereda quien llene ese modelo.** Estaba escrita como la regla once de dos manuales, así que todo lo demás que el agente entrega quedaba sin ella, y la convención se aplicaba copiándola a mano de una plantilla. Lo que se copia a mano se copia distinto.

El caso que lo destapó fue simple: el usuario pidió que un documento se escribiera así y no hubo regla que citar.

### 4.2 El modelo de manual de usuario no se tocó, y no es olvido

Tiene cambios sin guardar de otra sesión. Editarlo habría metido trabajo ajeno en este commit, que es exactamente el defecto que esta casa persigue desde el día de las 712 líneas. Queda anotado en el `§3` del estado de la fase.

### 4.3 Lo que la regla deja fuera, dicho acá

La ortografía y la gramática. El anexo de marcas las nombra como pendientes suyas, y son otra regla: una cosa es cómo se conjuga y otra si el texto está bien escrito. Prometer las dos con una sola regla sería prometer lo que no se comprueba.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- `base/00-identidad-y-rol/reglas/ID10-…md`, con su checklist aplicado
- `validadores/reglas-validables.md`, con qué mitad se comprueba
- `plantillas/manual-instalacion.md`, citando la regla
- `CHANGELOG.md` `37.0.0` y `VERSION`
