# Funcionalidad implementada — Fase «B-EP-007-HU-001-prepara-su-propia-salida»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho al final**. El plan dice qué se iba a hacer y no se toca; esto dice qué se hizo.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-007-HU-001-prepara-su-propia-salida` |
| **Épica / HU** | [EP-007](../../epica.md) · [HU-001](../HU-001-instalar-con-una-linea.md) |
| **Versión publicada** | [21.2.1](../../../../../CHANGELOG.md) — 2026-08-16 |
| **De dónde salió** | [Pendiente 45](../../../../../pendientes/hecho/instalar-prepara-su-propia-salida.md) |

---

## 1. Qué hace ahora que antes no hacía

`instalar()` prepara su propia salida antes de imprimir nada.

| Antes | Ahora |
|---|---|
| Solo `main()` preparaba la consola. Un programa que llamara a `instalar()` directamente se moría al imprimir el primer `→` | `instalar()` la prepara al entrar. Se puede llamar desde otro programa sin saber nada de esto |

Desde la línea de comandos no cambia nada: `main()` la sigue preparando, porque imprime antes de llamar a `instalar()`.

---

## 2. Dónde quedó

| Archivo | Qué cambió |
|---|---|
| [`validadores/instalar.py`](../../../../../validadores/instalar.py) | Una línea al entrar a `instalar()` |
| [`validadores/tests/test_instalar_reparar.py`](../../../../../validadores/tests/test_instalar_reparar.py) | La clase `PreparaSuPropiaSalida`, y se quitó el rodeo que la fase anterior había puesto |
| [`validadores/docs/instalar.md`](../../../../../validadores/docs/instalar.md) | Dice que `instalar()` prepara su salida |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) | La 21.2.1 |

---

## 3. Qué se probó

Dos casos, los dos ✅ — el detalle en [`resultado_pruebas.md`](resultado_pruebas.md).

El caso arma una salida en `cp1252` que no perdona lo que no cabe, y comprueba primero que esa salida rechaza la `→`. Después instala una vez, sube la versión del estándar para que los sellos queden viejos —que es la corrida que sí imprime flechas— y recién ahí corre con la consola pobre.

**El caso nació mal y el propio plan lo destapó.** En su primera versión instalaba en carpeta vacía, y esa corrida nunca imprime una flecha: pasaba en verde con el arreglo revertido. Lo encontró el CP-002, que existe justamente para obligar a ver fallar la prueba antes de confiar en ella.

---

## 4. Qué quedó fuera, y dónde vive

| Qué | Dónde |
|---|---|
| Los demás validadores | No se revisaron. Si alguno tiene el mismo hueco, es otro pendiente |
| La especificación del módulo de instalación | Deuda heredada de la fase [`A`](../A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md) (§10, `B-02`) |

---

## 5. Lo que esta fase deja aprendido

- **Una prueba de robustez que nunca se vio fallar no se sabe si comprueba algo.** Acá el escenario no reproducía el defecto, y el único motivo por el que se supo es que el plan obligaba a verla en rojo.
- **Un programa que sabe imprimir tiene que saber preparar su salida.** Delegarlo en quien lo llame es pedirle al de afuera que conozca las tripas del de adentro.
- **Un pendiente cerrado no se reabre.** Este defecto nació en [validadores-y-hooks](../../../../../pendientes/hecho/validadores-y-hooks.md) y se destapó en [poner-al-dia-lo-ya-instalado](../../../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md); fue a un pendiente nuevo que cita a los dos.
