# Funcionalidad implementada — Fase «A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-004](../HU-004-control-del-mensaje-de-cambio.md) |
| **Versión** | sin cambio — nada se construyó: ya estaba |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

**Ya estaba construido. Lo que esta fase hizo fue comprobar que funciona y dejarlo escrito.**

- [`validadores/commits.py`](../../../../../validadores/commits.py) revisa el mensaje: asunto vacío, asunto sin contenido, la línea en blanco entre asunto y cuerpo, el largo y la firma de la herramienta.
- [`.githooks/commit-msg`](../../../../../.githooks/commit-msg) lo llama y **corta el commit** cuando falla.

Comprobado por el camino real: `ajustes` y un mensaje con `Co-Authored-By` salen con **código 1**, y el enganche corta.

---

## 2. Una decisión mía era falsa, y la prueba estaba en la sesión

La duda 39 preguntaba si el disparo va como enganche de la herramienta o del control de versiones. La decidí como *«enganche de la herramienta, porque el del control de versiones no corre cuando el agente escribe»*.

**Es falso.** Cada commit de esta sesión imprimió su línea de comprobación: el enganche del control de versiones **sí corre cuando el agente commitea**. Diecisiete commits de evidencia, delante todo el día.

**Y la decisión correcta es la contraria, por un motivo mejor:** el enganche del control de versiones corta el commit **venga de donde venga** — del agente, de una terminal, de otra herramienta. El de la herramienta solo cubriría al agente.

---

## 3. Lo que no cubre

**El enganche se quita con una línea** (`git config --unset core.hooksPath`), y es correcto que se pueda. Pero significa que **nadie comprueba que siga puesto**: el instalador lo deja, y de ahí en adelante nadie mira.
