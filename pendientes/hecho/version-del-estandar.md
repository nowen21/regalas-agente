# Hecho · Versión del estándar

Origen: pendiente 04. El estándar ya se **versiona**, cada proyecto fija la versión que sigue, y hay aviso de desfase. "El proyecto cumple el estándar" pasa a ser un hecho con fecha: *versión X, sellada tal día*.

Cerrado el 2026-08-06.

---

## Qué se hizo

- **[`VERSION`](../../VERSION)** en la raíz (`1.0.0`) y **[`CHANGELOG.md`](../../CHANGELOG.md)** con el esquema `MAYOR.MENOR.PARCHE`: MAYOR = norma que **obliga**; MENOR = aditivo que no invalida; PARCHE = redacción/ejemplos. Cada entrada marca si `⚠ obliga a migrar`.
- **Regla de retroactividad** (README · §Versión del estándar y `CLAUDE.md.plantilla` · §1): un cambio de norma **no reabre** fases ya cerradas — quedan selladas con su versión. Subir de versión es decisión explícita del usuario.
- **Fijación por proyecto:** `CLAUDE.md.plantilla` · §1 declara `Versión del estándar adoptada: X.Y.Z · sellada YYYY-MM-DD`; §3 agrega el paso de arranque que corre el aviso de desfase.
- **Validador de desfase:** `validadores/version.py` (`validar.py version --raiz <proyecto>`) compara `VERSION` con la versión que declara el `CLAUDE.md`; si el proyecto quedó atrás, **avisa** — no migra. Núcleo puro probado (6 pruebas; total 143 verdes). Contra agro-system: avisa que aún no declara versión.

## Nota

El aviso vive como paso de arranque en el `CLAUDE.md` del proyecto (y como comando). Engancharlo también al `SessionStart` (como `F13`/`C18` en `sesion.py`) es una mejora futura menor, no un pendiente aparte.
