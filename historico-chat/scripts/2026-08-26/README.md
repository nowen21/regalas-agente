# Programas de un solo uso · 2026-08-26

Los catorce programas que el agente escribió el 2026-08-26, cerrando fases atrasadas y corrigiendo lo que se había afirmado sin leer. **No se vuelven a correr**: llevan dentro la ruta de la máquina donde corrieron, y escriben sobre texto que ya cambió.

De qué sesión salen: [2026-08-22 · sesion-6](../../2026-08-22-sesion-6.md), que cruzó varios días.

> **Estos catorce llegaron tarde al repositorio.** Se escribieron en la carpeta temporal del sistema y se trajeron el 2026-08-27, cuando el usuario preguntó por qué se seguía escribiendo afuera. Está contado en `S-057`.

## Qué hizo cada uno

### El inventario que dejó de mantenerse a mano

| Programa | Qué hizo |
|---|---|
| `sabotaje_hu019.py` | Los sabotajes de la `HU-019`, adentro del estándar |
| `sabotaje_hu020.py` · `cerrar_hu020.py` | Los de la `HU-020` —lo mismo, en lo que el estándar reparte— y su cierre |
| `hallazgos_hu019.py` | Cerró `H-27` y escribió `H-29`, `H-30` y `H-31` en el resumen |
| `hallazgos_hu020.py` | Cerró `H-31` y escribió `H-32`, `H-33` y `H-34` |

### El tope de ruta de Windows

| Programa | Qué hizo |
|---|---|
| `sabotaje_hu009.py` · `cerrar_hu009.py` | Los sabotajes de la `HU-009` y su cierre, que también cerró el `H-28` |

### El vocabulario del estado

| Programa | Qué hizo |
|---|---|
| `ampliar_hu012.py` | El alcance de la `HU-012` creció y se tradujo, con aprobación del usuario |
| `sabotaje_hu012.py` · `cerrar_hu012.py` | Sus sabotajes y su cierre |
| `normalizar_estados.py` | Normalizó el campo `Estado` de las historias. **Cambia la palabra, no la frase**: varias traen texto útil detrás, y su corrida en seco destapó que la primera versión perdía el punto final en 19 documentos |

### Lo que se afirmó sin haber leído

| Programa | Qué hizo |
|---|---|
| `corregir_hu010.py` | Corrigió los cinco documentos que citaban la `EP-001 HU-010` como abierta. Había cerrado el 2026-08-18 en `febcaf3`, **diciendo que no hacía falta regla nueva** |
| `senal_hu010.py` | Escribió `S-048` y reescribió el `H-34`, que decía lo contrario |

### Las seis fases que llevaban cuatro días sin cerrar

| Programa | Qué hizo |
|---|---|
| `cerrar_seis.py` | Marcó su estación y su estado. **No inventa nada**: la estación pasa a cerrada porque el documento existe y está en git |
