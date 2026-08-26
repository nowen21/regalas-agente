# Resultado de Pruebas — Fase B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado, y de ahí sale el veredicto. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida` |
| **HU** | [HU-003 Formato del hallazgo](../HU-003-formato-del-hallazgo.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) |
| **Ambiente y versión** | El repositorio del estándar en `main`, versión 31.4.0, Windows, Python 3.11 |

### 0.1 Esta fase sí había que construirla

A diferencia de otras del pendiente 59, acá no había nada hecho: `comun.leer` abría con `open(ruta, encoding="utf-8")` **sin red**, y su propio contrato decía que *«si el archivo no existe, la lectura falla y el error sube al que llamó»*. Se construyeron las ocho tareas del plan.

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados |
|---|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 |

## 2. Ejecución caso por caso

| Caso | Qué comprueba | Resultado | Evidencia |
|---|---|---|---|
| CP-001 · la lectura tolera los cuatro casos | archivo bueno, ausente, sin permisos y mal codificado | ✅ Aprobado | `test_errores_el_archivo_que_no_se_puede_leer_no_vuelca_la_excepcion`, que estaba marcada como fallo esperado y hoy **pasa destapada** |
| CP-002 · la corrida sigue y reporta lo demás | un archivo roto no se lleva los hallazgos ya encontrados | ✅ Aprobado | `test_errores_la_corrida_sigue_y_reporta_lo_demas`: sobre un árbol con uno roto y uno sano, se anota **uno solo** y el otro se lee entero |
| CP-003 · el hallazgo dice cuál es | la ruta y el motivo, no un volcado | ✅ Aprobado | «no es UTF-8 (byte b'\xed' en la posición 3) — se leyó reemplazando lo que no se entiende, así que lo que se diga de este archivo puede estar incompleto» |
| CP-004 · los casos de la batería siguen pasando | no regresión sobre `comun.leer`, que usan casi todos | ✅ Aprobado | `366 pruebas`, con una sola falla y **es de otro pendiente**: ver §4 |

## 3. Lo que se construyó, y por qué así

**Dos salidas malas y una buena.** Reventar se lleva los hallazgos ya encontrados; leer reemplazando y callar convierte un archivo roto en uno que parece sano. Se hacen las dos cosas: **la corrida sigue y el archivo queda anotado**, y `reportar` lo agrega solo, así que ningún validador tiene que acordarse de pedirlo.

**El aviso se borra cuando el archivo se arregla:** una lectura buena quita la anotación previa. Sin eso, un archivo corregido seguiría reportándose en la misma corrida.

**Y `pendientes.py` recuperó lo suyo:** tenía su propia lectura tolerante con un comentario que decía, con todas las letras, que la escribió porque `comun.leer` reventaba y que esperaba esta fase. Ya usa la común.

## 4. Defectos encontrados

**Ocho pruebas estaban en rojo desde antes, y no por esta fase.** Citaban rutas de moldes que se movieron el 2026-08-21 al crear `plantillas/ciclo-vida-proyectos/`: `planes/trabajo.md`, `HU.md`, `epica.md` y las demás. Reventaban con el error de lectura, así que **el arreglo de esta fase las convirtió de error en fallo** y las dejó a la vista. Se corrigieron las rutas, que es lo que faltaba.

**Y una queda en rojo a propósito:** `test_la_cuenta_del_programa_coincide_con_la_del_inventario_escrito` compara el recuento del programa (101 HU, 51 completas) con los números escritos a mano en el [pendiente 48](../../../../../pendientes/48-inventario-hu.md) (78, 47, 31). **El 48 es uno de los dos que el usuario excluyó** de la orden de resolver pendientes, así que no se toca. Queda dicho para que nadie lo lea como una falla nueva de esta fase.

## 5. Veredicto de la fase

**Cumple.** Cuatro casos de cuatro.

| Criterio | Veredicto |
|---|---|
| Transversal de errores · el archivo ilegible da un mensaje entendible y no un volcado | ✅ Cumple |
| No regresión · los demás validadores siguen funcionando | ✅ Cumple |

**Lo que hace fuerte al veredicto:** la prueba que lo comprueba llevaba días escrita y marcada como fallo esperado. No se escribió para acompañar al arreglo: el arreglo se hizo contra una prueba que ya decía que fallaba.
