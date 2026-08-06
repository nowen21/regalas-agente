# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo.

---

## 1.0.0 — 2026-08-06

Primera versión sellada del estándar. Línea base: núcleo blindado (`00`), conducta y flujo (`01`–`02`), buenas prácticas (`03`–`17`), plantillas de capa 3, memoria por señales con vigencia y ciclo de deuda, y la capa de validadores automáticos + hooks.

A partir de aquí, cada cambio de `base/` o `plantillas/` suma una entrada con su tipo.
