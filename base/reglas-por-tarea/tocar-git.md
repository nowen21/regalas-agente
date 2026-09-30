# Reglas de la tarea `tocar-git`

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## N1 · Ningún cambio de estado sin aprobación explícita `[BLINDADA]`
Ningún cambio de estado se hace **sin que el usuario lo apruebe**. Aprobar un plan vale para **todo lo que ese plan dice**, sin volver a pedirlo paso a paso — salvo lo **irreversible**, que se pide cada vez ([`acciones-y-riesgo.md`](../00-identidad-y-rol/acciones-y-riesgo.md)).
```
INCORRECTO: se corrige el archivo «que igual era obvio» y después se avisa
CORRECTO:   se dice qué se va a cambiar y se espera
```

Fuente: [00·N1](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)

## N2 · Control de versiones solo bajo pedido `[BLINDADA]`
Nunca **commit** ni **push** por iniciativa propia. Solo cuando el usuario lo pide.
La autorización es de **un solo uso**: no cubre la siguiente operación ni la próxima sesión.
```
INCORRECTO: termino un cambio y hago commit "para guardarlo"
CORRECTO:   reporto que está listo y espero el pedido de commit
```

Fuente: [00·N2](../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)

## N3 · No romper cosas para pasar un obstáculo `[BLINDADA]`
Ante un obstáculo (hook, test rojo, validación), reporta y propón el arreglo. Prohibido sin permiso: saltar hooks (`--no-verify`), borrar o silenciar el test que falla, forzar lo que el sistema rechaza.
```
INCORRECTO: el hook falla → uso --no-verify
CORRECTO:   reporto por qué falló y propongo el arreglo real
```

Fuente: [00·N3](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)

## C12 · No agregues calificativos al nombre del artefacto
El nombre de un artefacto en archivos, documentos y commits es **el que el usuario dijo, sin adornar**. Los adjetivos con que describió el estilo o el alcance no son parte del identificador.
Adornarlo produce nombres distintos entre versiones, y después no se encuentra.
```
INCORRECTO: usuario dice "hazme el módulo de aportes de manera completa" → archivo "aportes-completo.md"
CORRECTO:   archivo "aportes.md" · el "completo" es la calidad de ejecución, no parte del nombre
```

Fuente: [01·C12](../01-conducta.md#c12--no-agregues-calificativos-al-nombre-del-artefacto)

## S4 · Guarda los secretos fuera del código y rota el que se expuso
Las claves, credenciales y tokens viven en la **configuración de entorno**, fuera del código; el archivo de entorno real no se versiona, solo su plantilla sin valores; y un secreto expuesto por accidente se **rota**: no basta borrarlo (depende de [`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).
```
INCORRECTO: const API_KEY = "sk-live-abc123"
CORRECTO:   leerla de la configuración de entorno; el valor real no se versiona
```

Fuente: [04·S4](../04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)

## G1 · Commits atómicos, un solo propósito
Un commit = un cambio coherente (una feature, un fix, un refactor). No mezcles cosas sin relación. Debe poder revertirse solo, sin arrastrar lo ajeno.
```
INCORRECTO: un commit "varios cambios" con feature + fix + reformateo
CORRECTO:   uno por la feature, otro por el fix, otro por el formateo
```

Fuente: [09·G1](../09-git.md#g1--commits-atómicos-un-solo-propósito)

## G2 · Mensajes que explican qué y por qué
Primera línea breve e imperativa; si hace falta, un cuerpo con el **por qué** (el qué ya está en el diff). En el idioma del proyecto ([`01·C8`](../01-conducta.md#c8--habla-el-idioma-del-proyecto)).
```
INCORRECTO: "cambios", "fix", "wip"
CORRECTO:   "Corrige el saldo cuando hay documentos anulados

            Se sumaban al total; ahora se excluyen en la consulta."
```

Fuente: [09·G2](../09-git.md#g2--mensajes-que-explican-qué-y-por-qué)

## G3 · Deja fuera del control de versiones los secretos y lo generado
Al archivo de exclusión (`.gitignore`): **secretos** (claves, tokens, entorno real — [`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)), **datos sensibles/reales**, **artefactos generados** (dependencias, compilados, cachés, logs), **config local** de máquina/editor. Se versiona una **plantilla de ejemplo** sin valores.
```
INCORRECTO: commitear el archivo de entorno con la clave de producción
CORRECTO:   ignorar el real; versionar solo la plantilla sin secretos
```

Fuente: [09·G3](../09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado)

## G4 · Trabaja en ramas, integra limpio
El trabajo va en una **rama** dedicada (salvo que la capa 3 diga otra cosa). Mantenla al día con la principal. La rama principal queda siempre **funcional**.
```
INCORRECTO: se trabaja directo sobre la principal «porque es un cambio chico»
CORRECTO:   rama para el cambio, al día con la principal, y la principal
            siempre en verde
```

Fuente: [09·G4](../09-git.md#g4--trabaja-en-ramas-integra-limpio)

## G5 · No reescribas historia compartida ni fuerces sin necesidad
Reescribir historia (rebase, enmienda, purga) y **push forzado** solo sobre historia no compartida, o con acuerdo explícito si ya es pública (afecta a quien la clonó). Cada una requiere autorización ([`00·N2`](../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)). No fuerces con banderas destructivas ([`00·N3`](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
```
INCORRECTO: rechazan el push → hago push --force por mi cuenta
CORRECTO:   reporto el rechazo, explico la causa y espero decisión
```

Fuente: [09·G5](../09-git.md#g5--no-reescribas-historia-compartida-ni-fuerces-sin-necesidad)

## G6 · Las pruebas y el linter corren solos en cada cambio propuesto
La suite y el linter corren en un **entorno reproducible que no depende de que alguien se acuerde**, sobre cada cambio propuesto, y la rama principal no admite lo que no está en verde.
```
INCORRECTO: «las corrí en mi máquina y pasaban» → se integra
CORRECTO:   corren solas sobre el cambio propuesto, y si algo falla no entra
```

Fuente: [09·G6](../09-git.md#g6--las-pruebas-y-el-linter-corren-solos-en-cada-cambio-propuesto)

## G11 · Lo que corre en tu máquina complementa, no reemplaza
El enganche local es una ayuda para no mandar lo evidente, **no la comprobación**: no la sustituye y no se salta ([`00·N3`](../00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)). Lo que el entorno automático no puede cubrir queda como comprobación manual escrita ([`08·T4`](../08-pruebas.md#t4--protege-los-datos-reales-al-probar)).
```
INCORRECTO: se salta el enganche local «porque el pipeline igual lo va a revisar»
CORRECTO:   se arregla lo que el enganche señaló, y el pipeline vuelve a mirarlo
```

Fuente: [09·G11](../09-git.md#g11--lo-que-corre-en-tu-máquina-complementa-no-reemplaza)

## G7 · Todo commit se muestra al usuario y se aprueba antes de ejecutarlo
Antes de confirmar y de publicar, el agente **muestra el mensaje completo y los archivos afectados** y **espera aprobación explícita**. Primero se lee, después se aprueba, y recién ahí se ejecuta.
Aceptar el cambio **no** autoriza a guardarlo: son dos permisos ([`00·N2`](../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)).
```
INCORRECTO: hago el cambio y en el mismo paso hago commit/push · "ya que estaba, lo subí"
CORRECTO:   hago el cambio → muestro el mensaje + los archivos → espero "sube / aprobado" → recién ahí commit/push
```

Fuente: [09·G7](../09-git.md#g7--todo-commit-se-muestra-al-usuario-y-se-aprueba-antes-de-ejecutarlo)

## G8 · El cuerpo del commit abre con la idea del usuario
El cuerpo arranca con **lo que el usuario quiso**, y después con lo que hizo el agente. El origen del cambio es la necesidad, no la ejecución: quien lea el historial mañana busca el porqué.
```
INCORRECTO: «Se agregó validación en el servicio y se actualizaron 3 pruebas.»
CORRECTO:   «Pediste que no se pudiera cerrar una venta sin cliente. Va la
            validación en el servicio, con sus tres casos.»
```

Fuente: [09·G8](../09-git.md#g8--el-cuerpo-del-commit-abre-con-la-idea-del-usuario)

## G10 · El commit no se firma con la herramienta
El mensaje no lleva **ninguna marca de con qué se escribió**: ni coautoría de la herramienta, ni línea de «generado con», ni firma de agente. Quién hizo el commit ya lo dice el propio control de versiones (extiende [`09·G8`](../09-git.md#g8--el-cuerpo-del-commit-abre-con-la-idea-del-usuario)).
```
INCORRECTO: al final del mensaje, una línea que declara la herramienta como coautora
CORRECTO:   el mensaje termina en lo último que había que contar del cambio
```

Fuente: [09·G10](../09-git.md#g10--el-commit-no-se-firma-con-la-herramienta)

## G9 · La historia de usuario es la unidad del commit
Lo de una historia —documento, fases, código— va en un commit que **no toca otra**, y lo que aún no tiene historia espera a tenerla (concreta a [`G1`](../09-git.md#g1--commits-atómicos-un-solo-propósito)).
Excepción: lo que no es de ninguna historia sube con la primera que lo necesite.
Comprobable: un commit que toca dos carpetas de HU distintas se detecta comparando rutas.
```
INCORRECTO: un commit con HU-002, HU-003 y las épicas que todavía no
            tienen historias escritas
CORRECTO:   un commit por historia; la épica sin historias espera a tenerlas
```

Fuente: [09·G9](../09-git.md#g9--la-historia-de-usuario-es-la-unidad-del-commit)

## DEP4 · No versiones lo instalado
Las dependencias instaladas (carpetas de paquetes, binarios) no van al control de versiones ([`09·G3`](../09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado)): se reconstruyen del manifiesto + lockfile. Versiona la **declaración**, no el **resultado**.
```
INCORRECTO: commitear la carpeta de dependencias instaladas
CORRECTO:   versionar manifiesto + lockfile; ignorar la carpeta instalada
```

Fuente: [10·DEP4](../10-dependencias.md#dep4--no-versiones-lo-instalado)

## CFG2 · El entorno real no se versiona; sí una plantilla
El archivo con valores reales está **ignorado** ([`09·G3`](../09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado)). Se versiona una **plantilla de ejemplo** con todas las variables **sin valores**, y se documenta qué es cada una y cuáles son obligatorias.
```
INCORRECTO: versionar el archivo de entorno con las claves reales
CORRECTO:   versionar la plantilla vacía; el real queda en cada entorno
```

Fuente: [11·CFG2](../11-configuracion-entornos.md#cfg2--el-entorno-real-no-se-versiona-sí-una-plantilla)
