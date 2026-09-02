# Plan de Pruebas — Fase `B-EP-002-HU-003-la-version-declarada-se-comprueba`   ·   `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó y se cerró el 2026-08-22 y **este documento se quedó siendo la plantilla en blanco**: 363 líneas de molde con 36 marcadores sin reemplazar. Lo destapó la [HU-022](../../../EP-004-comprobacion-automatica/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md).
>
> **No se inventa nada.** Los casos salen del [resultado_pruebas.md](resultado_pruebas.md), que sí se escribió y documenta qué entró y qué salió en cada uno, y de las 10 pruebas que quedaron en el repositorio. **Lo que no se puede reconstruir —qué se pensó antes de ejecutar— no se escribe**, y se dice acá en vez de rellenarlo.

---

## 1. Propósito y alcance

Comprobar que **la versión que un proyecto declara se contrasta contra algo**. Antes no: un número inventado pasaba, y **si era mayor que la vigente apagaba el aviso de desfase** — la comprobación se apagaba sola y quien la apagaba no se enteraba.

**Entra:** que la versión declarada exista en el registro de cambios, que coincida con el último registro de `documentacion/versiones/`, y que el mensaje nombre los dos números cuando difieren.

**No entra:** decidir **qué hacer** cuando las dos difieren. Eso es del usuario; lo que se pedía es que se vea.

---

## 2. Estrategia

**Unitario** sobre proyectos de mentira, y **de sistema** sobre dos proyectos reales: una copia temporal manipulada y `shopnest-mesa` sin tocar.

**La mitad de los casos son de lo que NO debe pasar**, y es deliberado: una comprobación que reprueba de más se apaga a la semana, y entonces no queda nada.

---

## 3. Casos de prueba

| Caso | Qué entra | Qué debe salir |
|---|---|---|
| **CP-001** · versión que no existe | `99.9.9` declarada | Falla, **y dice que no está en el registro** |
| **CP-002** · declarada distinta del historial | declara `1.0.0`, historial dice `2.0.0` | Falla, **y nombra las dos** |
| **CP-003** · proyecto al día | declara la vigente | Silencio |
| **CP-004** · proyecto atrasado | declara una anterior | **Avisa, no falla** |
| **CP-005** · sin historial de adopciones | proyecto recién instalado | **No** falla |
| **CP-006** · sin registro de cambios legible | no se sabe qué versiones existen | **No** acusa a nadie |
| **CP-007** · el último registro es el mayor | `9.0.0` y `10.0.0` | Gana `10.0.0`, **no el último alfabético** |

**El `CP-007` es el que menos se ve venir.** Ordenar versiones como texto pone `9.0.0` después de `10.0.0`, y con eso la comprobación acusaría a un proyecto al día.

**Los `CP-005` y `CP-006` son los que sostienen la comprobación:** un proyecto recién instalado y un repositorio sin registro legible **no son incumplimientos**, y tratarlos como tales haría que nadie volviera a correr esto.

---

## 4. Criterio de aprobación

- Los siete casos, ejecutados.
- **La comprobación corrida sobre un proyecto real sin tocarlo**, no solo sobre ejemplos escritos para la ocasión.
- La suite en verde.

---

## 5. Qué se ejecutó, y con qué resultado

Está en el [resultado_pruebas.md](resultado_pruebas.md). En corto: los siete casos pasaron, la suite `test_la_version_adoptada_se_comprueba` dio **10 pruebas en verde**, y sobre `shopnest-mesa` apareció una contradicción real que llevaba **dos días sin que nadie la viera** — declaraba `27.2.0` con su historial en `28.0.0`.

---

## 6. Herramientas y datos

`unittest`, y dos proyectos reales: una copia temporal manipulada y `shopnest-mesa` sin modificar. **Ninguna prueba usa credenciales** (`00·N6`).

---

## 7. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | **Retrodocumentado.** La fase cerró el 2026-08-22 sin este documento |
