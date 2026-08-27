# Programas de un solo uso · 2026-08-27

Los diez programas que el agente escribió el 2026-08-27, en la jornada de la `HU-021`. **No se vuelven a correr**: llevan dentro la ruta de la máquina donde corrieron, y escriben sobre texto que ya cambió.

De qué sesión salen: [2026-08-22 · sesion-6](../../2026-08-22-sesion-6.md), que cruzó varios días.

> **Ocho de los diez llegaron tarde al repositorio.** Se escribieron en la carpeta temporal del sistema y se trajeron acá el mismo día, cuando el usuario preguntó por qué se seguía escribiendo afuera. Los dos últimos —los que midieron las formas del veredicto— ya nacieron acá. Está contado en `S-057`.

## Qué hizo cada uno

### La `HU-021` · que la cuenta distinga lo terminado de lo cumplido

| Programa | Qué hizo |
|---|---|
| `sabotaje_hu021.py` | Los seis sabotajes de la fase `A`. Uno destapó que el `CA-04` no tenía comprobación automática |
| `sabotaje_hu021b.py` | Los cuatro de la fase `B`, **cazados los cuatro al primer intento**. El tercero es el que importa: comprueba que agregar una forma de leer el veredicto no borre las dos que ya servían |
| `quienes.py` | Dice **cuáles** son las historias que no cumplen y las que no dicen si cumplen. El validador da tres números y ningún nombre |

### El resumen de la sesión, que iba nueve hallazgos atrás

| Programa | Qué hizo |
|---|---|
| `hallazgos.py` | Escribió `H-35` a `H-43`: los dos patrones de error, el vocabulario de estados, las cinco señales de sabotaje y cierre, y las dos fases de la `HU-021` |
| `cierre.py` | Reescribió la sección «¿se puede cerrar la sesión?», que declaraba cerrados hallazgos que no lo estaban |
| `cierre2.py` | La puso al día otra vez, cuando el pendiente 88 pasó de «falta escribirlo» a escrito |

### El pendiente 88

| Programa | Qué hizo |
|---|---|
| `indice88.py` | Le abrió su sección en el índice de `pendientes/` |
| `ruta88.py` | Anotó por qué todavía no tiene historia: tiene tres salidas y la decisión es del usuario |

### Medir las formas del veredicto **de verdad**, y no las que ya se reconocían

| Programa | Qué hizo |
|---|---|
| `formas_veredicto.py` | Enumeró **todos** los encabezados que mencionan «veredicto» en los 130 resultados. Aparecieron `Veredicto de la fase` (91), **`Veredicto` a secas (36)** y **`Veredicto final` (4)**. La fase `B` había declarado tres formas y «39 sin encabezado»: **sin encabezado hay 2** |
| `cuantas_se_recuperan.py` | Midió qué pasaría aceptando cualquier encabezado que empiece por «Veredicto». **Diez de las quince historias mudas sí lo dicen**, y tres de ellas dicen «No cumple» |

**Los dos nacieron de haber afirmado sin medir.** La fase `B` contó las formas que ya sabía buscar y llamó «sin encabezado» a todo lo demás, que es `04·R4` — la misma regla que esa fase venía a hacer cumplir.

## Lo que no está acá

- **`suite.txt`**, 59 KB con la corrida completa de las 425 pruebas. Es salida, no programa; el veredicto quedó escrito en el `resultado_pruebas.md` de la fase.
- **Dos clones enteros de la plataforma** (`limpio/` y `limpio2/`, 6.831 archivos con su `.venv`), del experimento del 2026-08-25 que comprobó que la configuración de git **no viaja al clonar**. Traerlos sería meter un entorno virtual al repositorio. Lo que valía era el resultado, y quedó escrito en la fase que lo midió.
