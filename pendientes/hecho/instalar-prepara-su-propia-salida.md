# Hecho · El instalador prepara su propia salida

Origen: pendiente 45, abierto y cerrado el 2026-08-16, versión **21.2.1**.

| | |
|---|---|
| **Dónde nació** | En [validadores-y-hooks](validadores-y-hooks.md) — el commit `4000f40`, que trajo `preparar_salida()` y el instalador de línea de comandos. Ahí se decidió que la salida la prepara `main()`, y nadie más |
| **Dónde se destapó** | En [poner-al-dia-lo-ya-instalado](poner-al-dia-lo-ya-instalado.md), como su `DEF-02` |
| **Por qué no se reabrió el cerrado** | Un pendiente cerrado queda sellado con la versión bajo la que cerró. Lo que aparece después va en uno nuevo, que cita a los dos |
| **Dónde se construyó** | Fase [`B-EP-007-HU-001-prepara-su-propia-salida`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/) |

## Cómo cerró

`instalar()` llama a `preparar_salida()` al entrar. Una línea. `main()` la sigue llamando también, porque imprime antes de llegar a `instalar()`.

**Lo que costó fue la prueba, no el arreglo.** El primer caso instalaba en una carpeta vacía y pasaba en verde **con el arreglo revertido**: esa corrida nunca imprime una flecha, porque la flecha sale al refrescar un sello que ya existía. Lo destapó el caso que obliga a ver fallar la prueba antes de confiar en ella. El caso quedó así: instalar, subir la versión del estándar para que los sellos queden viejos, y recién entonces correr con una consola que no admite la flecha — comprobando además que esa corrida sí la imprimió.

**Lo que quedó fuera:** los demás validadores no se revisaron. Si alguno tiene el mismo hueco, es otro pendiente.

## Qué pasa

`validadores/instalar.py` imprime su avance con tildes y con una flecha `→`. La consola de Windows, tal como arranca, no sabe mostrar esos caracteres: cuando le llega uno, el programa **se muere ahí mismo** — no por la instalación, sino por intentar escribir en pantalla.

Para eso existe `preparar_salida()`, en `validadores/comun.py`: pone la consola en un modo que sí los admite. Su propia explicación lo dice — *«La consola de Windows no siempre es UTF-8; evita que un acento rompa todo»*.

**Pero solo la llama `main()`**, o sea únicamente cuando alguien corre el instalador desde la línea de comandos. Si otro programa llama a `instalar()` directamente, nadie preparó la consola y revienta.

## Cómo se destapó

Escribiendo la prueba de la fase `A-EP-007-HU-006`. La prueba llama a `instalar()` como biblioteca, y al llegar al paso de sellado —que imprime `sin sello → a1b2c3d4e5f6`— salió:

```
UnicodeEncodeError: 'charmap' codec can't encode character '→'
```

Se rodeó haciendo que la prueba llamara a `preparar_salida()` ella misma. **El rodeo tapa el síntoma:** la próxima prueba, o el próximo programa que llame al instalador, se vuelve a encontrar con lo mismo y tiene que acordarse.

## Por qué importa

Poco, y conviene decirlo: desde la línea de comandos no pasa nunca. El daño es que **cada quien que use el instalador como biblioteca tiene que saber un detalle que no es suyo**. Un programa que sabe imprimir tiene que saber preparar su salida; delegarlo en quien lo llame es pedirle al de afuera que conozca las tripas del de adentro.

Es de los baratos: una línea.

## Qué falta

Que `instalar()` prepare su propia salida, y que una prueba lo compruebe forzando una consola que no admite esos caracteres — sin eso, la prueba pasa en verde en cualquier consola moderna y no prueba nada.

## Cómo se supo que cerró

Un programa llama a `instalar()` con la salida puesta en una codificación que no admite la flecha, y la instalación termina sin reventar. Está automatizado en [`validadores/tests/test_instalar_reparar.py`](../../validadores/tests/test_instalar_reparar.py), clase `PreparaSuPropiaSalida`.
