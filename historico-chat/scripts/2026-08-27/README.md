# Programas de un solo uso · 2026-08-27

Los veinte programas que el agente escribió el 2026-08-27, en la jornada de la `HU-021`. **No se vuelven a correr**: llevan dentro la ruta de la máquina donde corrieron, y escriben sobre texto que ya cambió.

De qué sesión salen: [2026-08-22 · sesion-6](../../2026-08-22-sesion-6.md), que cruzó varios días.

> **Ocho de los veinte llegaron tarde al repositorio.** Se escribieron en la carpeta temporal del sistema y se trajeron acá el mismo día, cuando el usuario preguntó por qué se seguía escribiendo afuera. Los doce últimos —los de la fase `C` de la `HU-021` y los de la `HU-022`— ya nacieron acá. Está contado en `S-057`.

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

### La fase `C` · enumerar en vez de contar

| Programa | Qué hizo |
|---|---|
| `forma_exacta.py` | El nivel, el número y **qué sigue** a cada encabezado. De ahí salió el dato que decide el diseño: de los seis títulos, **`Veredicto` a secas es el único seguido de la palabra suelta** |
| `cual_titulo_sirve.py` | Lo separó en dos listas: los seguidos de la palabra (uno, 15 veces) y los seguidos de tabla (70). **Los 70 son la tabla criterio por criterio, no el veredicto de la fase** |
| `recupera_ajustado.py` | La misma medición de `cuantas_se_recuperan.py`, con el patrón **ajustado a título exacto**. Mismo resultado —diez recuperadas, tres con «No cumple»— y comprobó además que **ninguna historia que ya tenía veredicto lo cambia** |
| `sabotaje_hu021c.py` | Los cuatro sabotajes. **El cuarto pasó en verde** y obligó a un segundo ciclo. Su guardia final tenía a su vez un defecto: buscaba «OK» en un texto que trae «OK: sin incumplimientos.», así que dio por buena una corrida con tres fallas |

**Se guardan los dos que midieron lo mismo**, el ancho y el ajustado, y no solo el bueno. La diferencia entre ellos **es** el aprendizaje: un patrón que hoy no falla por casualidad es el defecto de mañana.

### La `HU-022` · que un documento en blanco no cuente como escrito

| Programa | Qué hizo |
|---|---|
| `linea-base-moldes.py` | El **primer intento**, que no sirve: cuenta los marcadores `«…»` con un umbral. Dio 38, y **tres eran de una fase escrita y publicada media hora antes**. Se guarda porque la diferencia con el siguiente es el aprendizaje (`S-059`) |
| `linea-base-moldes-2.py` | El bueno: cruza cada documento con **su plantilla**. 577 sin ninguno, 80 con uno o dos, **7 que siguen siendo el molde** |
| `t00-arboles-de-prueba.py` | La `T-00`, corrida **antes de tocar código**: de los 2.299 literales de `pruebas.py`, **ninguno llega al corte**. Si alguno hubiera llegado, el plan cambiaba |
| `arregla-pruebas-hu022.py` | Dos arreglos en las pruebas: una que buscaba texto en `fases.py` y falló por un comentario, y ocho archivos que se quedaban abiertos |
| `sabotaje_hu022a.py` | Los seis sabotajes. **El quinto pasó en verde** — la comprobación era cierta siempre |
| `arregla-sabotaje-hu022a.py` | El guion anterior **se cayó con el código roto puesto**, y no se notó porque se corrió con `\| tail`. Acá están los dos arreglos: `try/finally` y salida limpia (`S-060`) |

**Los dos de la línea base se guardan juntos a propósito.** El malo no es basura: es la prueba de que una medida validada sobre los casos que la motivaron no dice nada sobre los demás.

## Lo que no está acá

- **Las salidas de las corridas completas** de la suite. Son salida, no programa; el veredicto queda escrito en el `resultado_pruebas.md` de cada fase. Es salida, no programa; el veredicto quedó escrito en el `resultado_pruebas.md` de la fase.
- **Dos clones enteros de la plataforma** (`limpio/` y `limpio2/`, 6.831 archivos con su `.venv`), del experimento del 2026-08-25 que comprobó que la configuración de git **no viaja al clonar**. Traerlos sería meter un entorno virtual al repositorio. Lo que valía era el resultado, y quedó escrito en la fase que lo midió.
