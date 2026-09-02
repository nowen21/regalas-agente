# Resultado de Pruebas — Fase `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** la regla existe, cumple su molde y está clasificada diciendo qué mitad no es comprobable. El criterio transversal de privacidad pedía que la exigencia estuviera escrita, y ahora lo está.

| Métrica | Meta | Real |
|---|---|---|
| Filas del checklist en ❌ | 0 | **0** |
| Caracteres del cuerpo | 320 o menos | **303** |
| Incumplimientos de `metareglas` | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — La regla no existía

Buscando dato personal, credencial, clave y secreto en `13·DOC5`: **cero menciones**. La regla dice qué se registra como señal y no dice qué no.

**Resultado: pasa.**

### CP-002 — La regla nueva cumple su molde

```
== El estándar contra sus meta-reglas · . ==
OK: sin incumplimientos.
```

**Resultado: pasa.**

### CP-003 — El versionado queda consistente

```
0 falla(s), 1 aviso(s).
```

El único aviso es el de la `15.4.0` duplicada, reconocido en el registro desde el 2026-08-15.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El cuerpo se midió antes de escribirlo

303 caracteres para un molde de 320. **No es un detalle de forma:** a `04·S18` le pasó lo contrario el 2026-08-27, nació con 360 y su checklist declaraba «CUMPLE» en las veinte filas. Se firmó sin medirlo.

### 4.2 La regla no declara depender de `N6`

`20·M7` prohíbe que algo extienda o derogue una `[BLINDADA]`. `S19` **nombra** a `00·N6` para decir qué ya está cubierto, y no declara dependencia. La comprobación que lo caza es la misma que se construyó hoy para las reglas de proyecto.

### 4.3 Lo que la regla no promete

La clave sí se puede cazar con un programa; el dato personal no, sin decidir qué nombre propio es de una persona y cuál de un módulo. Queda escrito en el registro de validables, y no como una promesa a medias.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- [`base/04-seguridad.md`](../../../../../base/04-seguridad.md), regla `S19`
- [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md)
- `CHANGELOG.md` `36.0.0` y `VERSION`
