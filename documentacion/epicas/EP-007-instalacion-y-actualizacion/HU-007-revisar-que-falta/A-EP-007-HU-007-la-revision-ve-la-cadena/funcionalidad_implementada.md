# Funcionalidad implementada — Fase «A-EP-007-HU-007-la-revision-ve-la-cadena»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-007-HU-007-la-revision-ve-la-cadena` |
| **Épica / HU** | [EP-007](../../epica.md) · [HU-007](../HU-007-revisar-que-falta.md) |
| **Versión del estándar** | 22.1.0 → **23.0.0** (MAYOR) |
| **Fecha de cierre** | 2026-08-16 |

---

## 1. Qué quedó funcionando

**La revisión pasa de 13 puntos a 14.** El nuevo, `cadena`, mira si el proyecto arrancó por donde `02·F0` manda: al menos un planteamiento en `prompts/`, y una épica en `documentacion/epicas/` si ya hay código en `proyectos/`.

Un proyecto sin planteamiento dice ahora «13 de 14» y nombra qué le falta, en vez de «13 de 13, instalación completa».

**Es el único punto de la lista que el instalador no instala**, y su columna lo dice con todas las letras. No es un olvido: el planteamiento lo escribe el agente con lo que el usuario quiere, y el instalador no pregunta. Dejar la plantilla con los marcadores crudos sería peor, porque parecería un planteamiento y la revisión lo daría por cumplido. **Lo que faltaba no era dejarlo puesto: era decir que falta.**

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`plantillas/stack-instalacion.md`](../../../../../plantillas/stack-instalacion.md) | La fila del punto y la nota de por qué uno de los catorce no se instala |
| [`validadores/checklist.py`](../../../../../validadores/checklist.py) | `_cadena()` y su entrada en el mapa de comprobaciones |
| [`validadores/tests/test_checklist_cadena.py`](../../../../../validadores/tests/test_checklist_cadena.py) | **Nuevo.** Tres casos |
| [`validadores/tests/test_instalar_reparar.py`](../../../../../validadores/tests/test_instalar_reparar.py) | Ampliación de plan: su `CP-004` exigía cero faltantes después de instalar |
| [`validadores/docs/checklist.md`](../../../../../validadores/docs/checklist.md) | El punto nuevo y por qué existe |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · `VERSION` | 23.0.0 |

---

## 3. Cómo se comprueba

```
python -m unittest discover -s validadores/tests
```

32 pruebas, 32 en verde. Los tres casos nuevos están en `LaRevisionVeLaCadena`, y se vieron fallar a propósito quitando la fila del punto de la lista de componentes.

---

## 4. Qué quedó fuera

- **Comprobar la cadena hacia abajo** —que cada historia tenga fase y cada fase su plan—: ya lo mira `flujo.py`.
- **Detener el trabajo.** El aviso avisa; la `RN-06` de la historia lo prohíbe.
- **Escribir el planteamiento de este repositorio**, que reprueba su propio punto nuevo. Es decidir qué es este proyecto, no una tarea de código.

---

## 5. Por qué es MAYOR

Un proyecto al día **tiene que hacer dos cosas nuevas**: correr el instalador una vez —la huella del stack cambió al cambiar la lista— y escribir su planteamiento si no lo tiene. Que el resultado sea un aviso y no un bloqueo no lo vuelve opcional.
