# Resultado de Pruebas — Fase A-EP-005-HU-004: el control del mensaje de cambio

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos ejecutados

Se corrieron por el camino real: `validar.py commit --archivo`, que es lo que el enganche llama.

| Mensaje | Qué dio | Código |
|---|---|:--:|
| `ajustes` | **FALLA** — «asunto sin contenido: `ajustes` — G2 pide qué y por qué» | **1** |
| `Arregla el enlace` + `Co-Authored-By: …` | **FALLA** — «el mensaje incluye Co-Authored-By — G8 no firma con la herramienta» | **1** |
| Un mensaje con asunto y cuerpo | Sin incumplimientos | 0 |

| CA | Veredicto |
|---|---|
| **CA-01** · un mensaje sin contenido no pasa | ✅ **Pasa** |
| **CA-02** · el rastro de la herramienta se detecta | ✅ **Pasa** |
| **Detiene, no solo avisa** (decisión 8 del [59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md)) | ✅ **Pasa** — código 1, y el enganche corta con `|| exit 1` |

---

## 2. Ya estaba construido, y esta fase lo comprobó

La fase era de retro-documentación, y lo que había que averiguar era **si de verdad funcionaba**. Funciona:

- [`validadores/commits.py`](../../../../../validadores/commits.py) comprueba asunto vacío, asunto sin contenido, la línea en blanco entre asunto y cuerpo, el largo, y la firma de la herramienta.
- [`.githooks/commit-msg`](../../../../../.githooks/commit-msg) lo llama y **corta el commit** si falla.
- El enganche se activa con `git config core.hooksPath .githooks`, y en este repositorio está activo.

---

## 3. Una decisión mía era falsa, y esta sesión tiene la prueba

**La duda 39 preguntaba si el disparo va como enganche de la herramienta o del control de versiones**, y hoy la decidí así:

> *«Enganche de la herramienta. El del control de versiones no corre cuando el agente escribe.»*

**Es falso, y la prueba está en esta misma sesión.** Cada commit de hoy imprimió su línea de comprobación —`== Mensaje de .git/COMMIT_EDITMSG ==`— porque el enganche del control de versiones **sí corre cuando el agente commitea**. Son diecisiete commits de evidencia.

**La decisión correcta es la contraria**, y por un motivo que la vuelve mejor: el enganche del control de versiones corta el commit **venga de donde venga** — del agente, de una terminal o de otra herramienta. El de la herramienta solo cubriría al agente.

> **Decidí sin mirar, teniendo la evidencia delante todo el día.** Es el mismo defecto que vengo documentando en otros: la respuesta estaba en el repositorio y el trabajo era encontrarla.

---

## 4. Lo que queda abierto · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**El enganche se puede desactivar con una línea:** `git config --unset core.hooksPath`. Está escrito en el propio archivo, y es correcto que se pueda — pero significa que **nada garantiza que esté puesto** en un proyecto instalado. El instalador lo deja; que siga ahí, no lo comprueba nadie.

---

## 5. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 |
| **Defectos abiertos aceptados** | uno: que el enganche se pueda quitar y nadie lo note |
| **Ciclos** | 1 |
