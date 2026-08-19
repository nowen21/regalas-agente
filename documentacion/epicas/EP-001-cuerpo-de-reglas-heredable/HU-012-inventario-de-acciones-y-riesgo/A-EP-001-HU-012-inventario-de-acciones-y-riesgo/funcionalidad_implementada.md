# Funcionalidad implementada — Fase «A-EP-001-HU-012-inventario-de-acciones-y-riesgo»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-012-inventario-de-acciones-y-riesgo` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-012](../HU-012-inventario-de-acciones-y-riesgo.md) |
| **Versión** | 23.15.0 |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

**La lista de lo que el agente puede hacer, con lo que cuesta deshacer cada cosa:** [`base/00-identidad-y-rol/acciones-y-riesgo.md`](../../../../../base/00-identidad-y-rol/acciones-y-riesgo.md).

**12 clases**, en tres niveles: 3 se deshacen solas, 4 con trabajo, **5 no se deshacen**.

Y su comprobación, [`validadores/acciones.py`](../../../../../validadores/acciones.py), dentro de `validar.py acciones`.

---

## 2. Lo que cambia en la práctica

Hasta hoy [`00·N1`](../../../../../base/00-nucleo-blindado.md) pedía aprobación para **todo** cambio de estado. Cambiarle una coma a un README y borrar un archivo que no está en el control de versiones pedían lo mismo.

> **Un control parejo no protege más: protege menos.** Cuando la misma exigencia cubre lo trivial y lo grave, se aprueba **en bloque** — y entonces también quedó aprobado lo grave.

**Ahora un plan aprobado cubre lo que se deshace y lo que cuesta deshacer, y nunca lo que no se deshace.** Eso se pide aparte, cada vez, aunque estuviera escrito en el plan.

**Y quedó nombrado lo que no lo estaba:** borrar algo **no versionado** es del nivel más alto. No hay de dónde recuperarlo, y nadie se entera hasta que hace falta.

---

## 3. El núcleo no cambió, y hay una prueba que lo vigila

`N1` a `N6` siguen letra por letra como estaban. **La lista los organiza, no los reemplaza** — cada clase cita la regla del núcleo que la cubre, y ninguna inventa exigencia nueva sobre lo ya blindado.

`CP-009` compara el texto de las seis contra lo guardado, y **cazó un cambio real** durante la construcción. Está contado en el [`resultado_pruebas.md`](resultado_pruebas.md) §4.

---

## 4. Lo que salió de construirlo

**Tres defectos, y los tres los cazó la máquina, no la lectura.** Están en la §3 del resultado. El que más enseña:

`CP-002` borra una clase a propósito para ver si se reporta — y **no se reportaba**, porque la búsqueda miraba el archivo entero y el nombre seguía en otra sección. **Sin ese caso, «cero huérfanas» habría significado que el programa no busca nada.**

---

## 5. Lo que no hace

- **No dice si la clasificación es la acertada.** Eso se discute leyendo, y está declarado como parcial en `reglas-validables.md`.
- **No aplica la clasificación a los enganches.** Es otra fase.
- **No cambia ninguna regla.** Ni la puede cambiar: hay una prueba que lo impide.
