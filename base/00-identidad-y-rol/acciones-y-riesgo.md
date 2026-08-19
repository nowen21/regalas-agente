# Qué puede hacer el agente, y qué cuesta deshacerlo

> Anexo del capítulo [`00 · Núcleo blindado`](../00-nucleo-blindado.md). **No es una regla**: no lleva molde de regla ni identificador propio. Organiza lo que [`N1`](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada) a [`N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada) ya exigen, y no agrega exigencia nueva sobre lo que ellas cubren.

## Por qué existe

`00·N1` pide aprobación para **todo** cambio de estado. Corregir una coma en un README y borrar un archivo que no está en el control de versiones piden hoy exactamente lo mismo.

**Un control parejo no protege más: protege menos.** Cuando la misma exigencia cubre lo trivial y lo grave, lo que ocurre en la práctica es que se aprueba **en bloque** — y entonces también quedó aprobado lo grave.

## La escala: tres niveles

| Nivel | Qué significa | Qué exige **antes** de ejecutarse |
|---|---|---|
| 🟢 **Se deshace sola** | El control de versiones la revierte sin pensar | **Nada.** Se hace y se dice en el reporte de lo hecho |
| 🟡 **Se deshace con trabajo** | Hay cómo volver atrás, pero cuesta | Se **anuncia antes** y se hace **de una en una**, nunca en bloque |
| 🔴 **No se deshace** | No hay vuelta desde el repositorio | **Aprobación de esa acción concreta** — no basta un plan aprobado que la contenga |

**La diferencia entre 🟡 y 🔴 es la que hace útil esta tabla.** Un plan aprobado cubre 🟢 y 🟡 de corrido; **nunca cubre 🔴**. Eso se pide aparte, cada vez, aunque estuviera escrito en el plan.

## Las clases de acción

| Clase | Qué incluye | Nivel | Qué pasa si sale mal | Regla del núcleo |
|---|---|:--:|---|---|
| **Leer** | Abrir cualquier archivo del repositorio o del que el usuario nombró | 🟢 | Nada: no cambia estado | — |
| **Escribir un archivo del repositorio** | Crear o editar algo versionado | 🟢 | Se revierte el commit y no queda rastro | `N1` |
| **Borrar algo versionado** | Quitar un archivo que el control de versiones conoce | 🟡 | Se recupera del historial, pero hay que saber que se borró | `N1` |
| **Borrar algo NO versionado** | Un archivo local, un temporal, algo ignorado | 🔴 | **No hay de dónde recuperarlo.** Nadie se entera hasta que hace falta | `N1` |
| **Correr un comando local** | Un guion del proyecto, una herramienta instalada | 🟡 | Puede dejar archivos o procesos a medias; se limpia a mano | [`N3`](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada) |
| **Correr algo que sale a la red** | Instalar, publicar, llamar a un servicio | 🔴 | **Salió de la máquina.** Un paquete publicado o un dato enviado no vuelve | `N6` |
| **Guardar en el control de versiones** | `commit`, cambiar de rama, preparar archivos | 🟡 | Se deshace, pero hay que saber qué commit revertir | [`N2`](../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada) |
| **Publicar o reescribir la historia** | `push`, `rebase`, `push --force` | 🔴 | **Lo publicado ya lo tiene otro**, y la historia reescrita rompe lo que otros tienen bajado | `N2` |
| **Tocar datos reales** | Migrar, borrar, transformar sobre una base con datos de verdad | 🔴 | **Los datos no vuelven.** Que la migración sea reversible no recupera lo borrado | [`N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada) |
| **Tocar la máquina fuera del repositorio** | Configuración del sistema, carpetas de otros proyectos, variables del entorno | 🔴 | Se rompe algo que el usuario usa en paralelo, y el repositorio no lo registra | `N1` · [`04·S9`](../04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) |
| **Escribir en el histórico** | La transcripción de la sesión | 🟡 | Es registro: reescribirlo borra lo que de verdad se dijo | [`15·IM1`](../15-registros-inmutables.md#im1--un-registro-materializado-es-inmutable) |
| **Escribir en la memoria** | Los recuerdos del repositorio | 🟢 | Se corrige escribiendo encima; queda en el historial | — |

## Hacer lo mismo muchas veces sube un nivel

**«En masa» no es una clase: es un modificador.** No tiene nivel propio — toma el de la clase que multiplica y le suma uno.

| Una vez | Muchas veces |
|---|---|
| Escribir un archivo · 🟢 | Reescribir trescientos · 🟡 — revisarlos uno por uno ya no es gratis |
| Borrar algo versionado · 🟡 | Borrarlo en masa · 🔴 |
| Tocar datos reales · 🔴 | 🔴, y además previsualizar ([`00·N5`](../00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)) |

**Del rojo no se sube más**, porque no hay adonde: lo que no se deshace, no se deshace más fuerte. Lo que agrega `N5` ahí es **ver antes de aplicar**.

> **Se sacó de la tabla al construirla, y lo cazó el validador.** Estaba puesta como una clase con el nivel «el de su clase, subido un nivel», que no es un nivel. La escala es cerrada justamente para que eso no pase: una fila cuyo nivel es una fórmula no se puede comparar con ninguna otra.

## Lo que esta lista no nombra

**Se trata como 🔴, se dice, y se anota.** Las tres cosas, no una:

1. **Se le aplica la exigencia del nivel más alto** — aprobación de esa acción concreta.
2. **Se dice que no está clasificada**, en el mismo mensaje en que se pide la aprobación. Quien aprueba tiene derecho a saber que está decidiendo sin tabla.
3. **Se anota para clasificarla**, en `pendientes/`, para que la próxima vez sí esté.

**Una lista sin esta cláusula deja el hueco abierto justo donde aparece lo que nadie previó**, que es de donde salen los accidentes.

## Cuando una acción cae en dos clases

**Manda la más alta.** Un guion local que además sale a la red es 🔴, no 🟡: se clasifica por lo que no se puede deshacer, no por lo que se está haciendo la mayor parte del tiempo.

## Lo que esta tabla no decide

**Si la clasificación es la acertada.** Que borrar un archivo no versionado merezca 🔴 y no 🟡 es un juicio, y se discute leyendo. Lo que un programa comprueba es que **cada clase tenga su nivel y su ejemplo**, y que ninguna quede fuera de la escala — `validar.py acciones`.
