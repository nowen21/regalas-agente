# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo — salvo que en el desfase haya una derogación sin adoptar, que sí detiene la fase ([`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)).

---

## 23.24.0 — 2026-08-18

**MAYOR** (nacen cuatro reglas con nombre nuevo) · **y una comprobación deja de reportar de más.**

**La regla sobre tablas nuevas pedía tres cosas a la vez** —que el dato no se repita, que quede escrito quién tocó cada fila, y que las relaciones se declaren en el propio almacén— y las tres se cumplen por separado. La de valores configurables pedía dónde guardarlos *y además* cómo compararlos.

**Y una comprobación estaba gritando.** El aviso de «este sello venció» miraba la fecha del **archivo**, así que tocar una regla vencía el sello de todas las de su capítulo: **119 avisos en una sola corrida**. Un validador que reporta ciento diecinueve cosas no lo lee nadie.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). [`03·D1`](base/03-datos.md) se parte en tres —nacen `D10`, quién tocó la fila, y `D11`, la integridad vive en el almacén— y [`03·D4`](base/03-datos.md) en dos, con `D12`: el código decide por el código del catálogo, **no por su identificador**, que es el que cambia entre entornos y hace fallar en producción lo que funcionaba al programar.

**`D11` sostiene a [`03·D9`](base/03-datos.md)**: sin la restricción declarada en el almacén, dos procesos simultáneos insertan el mismo registro por más que la aplicación lo compruebe. Se incumple con la mejor intención — *«ya lo valido yo»*.

**La comprobación del sello ahora pide las dos cosas:** que el archivo se haya tocado después del sello **y** que el cuerpo de esa regla difiera del guardado. Su propio texto ya había anticipado este paso — *«si esto produce demasiado ruido, la huella queda como el paso siguiente, ya con datos»*—, y los datos fueron 119.

Las reglas publicadas en «no cumple» bajan de 37 a **35**.

## 23.23.0 — 2026-08-18

**MAYOR** (nacen cuatro reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Cuatro reglas más separadas, y en las cuatro la mitad que se va es la que se olvida.**

Una pedía que repetir una operación no duplicara su efecto *y además* que dos operaciones simultáneas no se pisaran — que son problemas distintos: el mismo actor dos veces, o dos actores a la vez. Otra pedía que anular revirtiera todo de una vez *y además* que se avisara a quien tenía el dato ya calculado. Otra, que las pruebas corrieran solas *y además* que lo que corre en tu máquina no las reemplace. Y la del plan pedía el visto bueno *y además* dejaba claro que autorizar el arranque de una fase no es aprobar su plan.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Nacen [`03·D9`](base/03-datos.md), [`15·IM7`](base/15-registros-inmutables.md), [`09·G11`](base/09-git.md) y [`02·F25`](base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md).

**`02·F25` es la que más se incumple sin querer**, y por eso merecía nombre propio: nadie se salta la aprobación de un plan a propósito — lo que pasa es que **se toma el «arrancá con X» por el permiso de ejecutar**, y el trabajo avanza con la conciencia tranquila. `F4` dice que hace falta un visto bueno; `F25` dice cuál no cuenta.

Las reglas publicadas en «no cumple» bajan de 41 a **37**.

## 23.22.0 — 2026-08-18

**MAYOR** (nacen tres reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Tres reglas más que pedían dos cosas cada una.** Una decía cómo evitar que la entrada del usuario se cuele dentro de una instrucción *y además* qué campos puede tocar un formulario; otra, cómo guardar un archivo privado *y además* qué pasa con él cuando se da de baja a su dueño; otra, que los entornos se parezcan *y además* que lo que hace falta en producción quede escrito.

En los tres casos la segunda mitad es la que se cae sola, sin ruido: se puede tener todo bien parametrizado y aun así dejar que un formulario escriba el campo que vuelve administrador a quien lo manda.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Nacen [`04·S16`](base/04-seguridad.md) —solo se asigna lo que está declarado—, [`04·S17`](base/04-seguridad.md) —el archivo sobrevive a la baja de su dueño— y [`11·CFG5`](base/11-configuracion-entornos.md) —lo que producción necesita se escribe antes de aplicarlo—.

**[`14·EST2`](base/14-estructura-codigo.md) no se partió: le sobraba, no le faltaba.** Lo que la hacía parecer dos reglas era un consejo sobre los límites de longitud del motor, que además nombraba tecnología. **No era una exigencia, era una advertencia práctica**, y se fue. Lo que queda es una sola cosa: una convención por tipo de elemento, aplicada igual.

Las reglas publicadas en «no cumple» bajan de 45 a **41**.

## 23.21.0 — 2026-08-18

**MAYOR** (nacen cinco reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Seguimos separando reglas que decían varias cosas a la vez.** Una pedía cuatro cosas distintas sobre la seguridad de las sesiones; otra pedía validar antes de empezar *y además* no dejar el trabajo a la mitad; otra pedía llevar tres estados *y además* anotar quién anuló y por qué.

Cuando una regla pide dos cosas, se cumple la primera y la segunda se cae sin que nada lo note. Ahora cada una se puede señalar por separado.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). [`04·S5`](base/04-seguridad.md) —cuyo título *«CSRF, sesiones y transporte»* **ya las enumeraba**— se parte en cuatro: se queda con el token, y nacen `S13` (la sesión se cierra de verdad), `S14` (el dato sensible no viaja en claro) y `S15` (la contraseña se guarda irreversible y con sal). [`05·E2`](base/05-errores-y-logging.md) se parte y nace `E6` —lo que toca varios registros va en transacción—, y [`15·IM2`](base/15-registros-inmutables.md) se parte y nace `IM6` —anular deja escrito quién, cuándo y por qué—.

**`17·I3` se miró para partirla y se decidió que no**, y conviene saber por qué: sus cuatro puntos —etiqueta, contraste, teclado, color— **no son cuatro exigencias, son la definición de una**. Una interfaz con etiquetas y sin contraste no cumple «la accesibilidad mínima» a medias: no la cumple. **La prueba es si se cumplen por separado**, y acá no.

**Y [`02·F12`](base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) no se toca:** es texto literal del usuario y su propio sello ya decía que se queda reprobada hasta que él decida la vía.

Las reglas publicadas en «no cumple» bajan de 49 a **45**.

## 23.20.0 — 2026-08-18

**MAYOR** (nacen dos reglas con nombre nuevo; si tu proyecto cita alguna de las que se partieron, conviene mirarlo).

**Tres reglas decían dos cosas cada una, y por eso nadie las cumplía enteras.** Una pedía autorizar cada escritura contra datos reales *y además* contar el borrado lógico como escritura; otra pedía que el mensaje del commit abriera con la idea del usuario *y además* que no llevara firma de herramienta. Cumplir la primera mitad y olvidar la segunda pasaba sin que nada lo notara.

Ahora cada una dice una sola cosa, y se puede señalar cuál se incumplió.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Nacen [`04·S12`](base/04-seguridad.md) —el borrado lógico es una escritura— y [`09·G10`](base/09-git.md) —el commit no se firma con la herramienta—. **Las dos ya venían numeradas dentro del texto que las contenía:** `S11` decía «Regla 1» y «Regla 2», y `G8` abría con «Dos consecuencias». Los identificadores viejos siguen existiendo con la mitad que se quedaron, como manda [`20·M4`](base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md).

**Y partir sirvió para pagar una deuda vieja.** `04·S11` nombraba `SoftDeletes` y `destroy()`, lo que [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) prohíbe en la base, y su sello había decidido no corregirlo porque **el nombre del método era el argumento**: suena a borrar y escribe. Reescribirlo en concepto solo se podía al partir, y así fue. **La lista de reglas que nombran un framework vuelve a cero**, después de once días con una permitida.

**[`12·PR3`](base/12-privacidad-datos.md) no se partió: se reescribió.** No tenía dos exigencias — tenía cuatro remisiones al capítulo de seguridad y nada propio. Lo suyo estaba implícito y ahora está dicho: **el dato personal se trata como sensible aunque nadie lo haya clasificado así**, sin esperar a que el proyecto lo declare.

Las reglas publicadas en «no cumple» bajan de 52 a **49**.

## 23.19.0 — 2026-08-18

**MAYOR** (una regla del núcleo dice ahora algo que antes no decía; conviene releerla).

**Aprobar un plan aprobaba también lo que no se puede deshacer, y eso ya no vale.** La regla decía que un plan aprobado se ejecuta seguido, sin volver a pedir permiso paso a paso. Ahora dice hasta dónde: **lo irreversible se pide aparte cada vez, aunque estuviera escrito en el plan que aprobaste.**

También se escribió entera la excepción de las pruebas: el cambio sin lógica puede ir sin prueba, pero hay que decir en el plan cuál es y por qué, y eso lo aprueba el usuario — no lo decide solo quien escribe.

**El detalle.** [`00·N1`](base/00-nucleo-blindado.md) y [`08·T1`](base/08-pruebas.md) escriben su excepción en la forma que pide [`20·M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), con condición, límite y autorizador. `T1` pasa a **CUMPLE**.

**El cambio de `N1` resolvió un choque que se había creado el mismo día.** El anexo [`acciones-y-riesgo.md`](base/00-identidad-y-rol/acciones-y-riesgo.md) dice que un plan aprobado nunca cubre lo irreversible, y `N1` decía *«se ejecuta continuo»* a secas: las dos afirmaban cosas contrarias, y manda la del núcleo. Hay un caso de prueba que comprueba que sigan de acuerdo.

**Y una corrección del mismo día, que conviene leer.** Al arreglar la excepción se marcó en verde la fila 16 del checklist de `N1`, y **estaba mal**: su sello ya explicaba, desde antes, que el problema no es que la excepción esté mal escrita sino que **existe** — una regla `[BLINDADA]` con excepción deja de ser inquebrantable, que es lo contrario de lo que promete la cabecera del capítulo. Escribirla mejor la hace más explícita, no la hace desaparecer. La fila volvió a ❌ el mismo día.

## 23.18.0 — 2026-08-18

**MENOR** (una regla admite un caso que antes no admitía; nada de lo que ya cumplías deja de valer).

**Enlazar al archivo de al lado obligaba a escribir su dirección completa.** Para nombrar un documento que está en la misma carpeta había que poner una línea de unos 130 caracteres, y eso pasaba en setecientos enlaces — casi todos, documentos de un mismo trabajo citándose entre sí.

Ahora el archivo de la misma carpeta se enlaza por su nombre. El de cualquier otra sigue llevando su dirección entera.

**El detalle.** Es el [pendiente 18](pendientes/hecho/los-enlaces-del-estandar-no-cumplen-doc14.md). [`13·DOC14`](base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) gana su excepción escrita en la forma de [`20·M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), y se le vuelve a aplicar el checklist: pasa de 17 a 18 filas en verde, porque la fila 16 dejó de ser N/A.

**La excepción sale del propio texto de la regla, no de que fueran muchos.** `DOC14` pide la ruta *«para saber dónde vive sin abrirlo»*, y para el vecino ese propósito ya está cumplido. El límite es estrecho a propósito: la misma carpeta y nada más.

**Antes se había intentado al pie de la letra**, y quedó ilegible; se revirtieron 347 archivos. Esa reversión fue la que destapó que el problema no eran los enlaces sino la regla, que no había previsto el caso más común.

## 23.17.1 — 2026-08-18

**PARCHE** (deja de contarse como defecto algo que no lo era; ninguna exigencia cambia).

**La forma en que esta casa nombra sus capítulos estaba contada como si fuera un descuido.** El punto que separa el número del nombre —«09 · Control de versiones»— aparecía como una de las marcas que delatan un texto escrito por una máquina. Eran mil seiscientas, y una de ellas estaba en el índice del propio documento que las prohíbe.

Se conserva, y no como excepción sino como lo que es: la manera en que este proyecto nombra las cosas. En medio de una frase sigue contando.

**El detalle.** Del [pendiente 11](pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md). El [anexo de marcadores](base/00-identidad-y-rol/marcadores-de-ia.md) ya eximía la cita `NN·ID` por ser notación definida, y el separador de encabezado es la misma clase. **El código ya lo tenía decidido y no lo había implementado:** el comentario de [`marcas.py`](validadores/marcas.py) decía *«ni de un `A · B` de encabezado: los dos son notación definida»*, y la expresión regular solo cubría la primera mitad. El recuento baja de 16 477 a **15 485**; el punto medio, de 6 237 a **4 638**. Se exime solo en la línea de un encabezado. 6 casos nuevos.

## 23.17.0 — 2026-08-18

**MENOR** (una regla deja de regir porque otra ya decía lo mismo; no hay nada nuevo que cumplir).

**Dos reglas pedían lo mismo y se remitían la una a la otra en círculo.** Una decía «audita las vulnerabilidades de tus dependencias, el detalle está en el otro capítulo», y el otro capítulo decía «audítalas, ver la primera». Quien las leía daba la vuelta y volvía al principio.

Se queda la del capítulo de dependencias, que es de quien es el tema. La otra deja de regir y su texto se conserva, porque hay trabajo cerrado que la cita.

**El detalle.** [`04·S7`](base/04-seguridad.md) queda `[DEROGADA en 23.17.0 → ver 10·DEP3]` por [`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md), que manda derogar y no borrar. El dueño del tema es el capítulo `10` según [`20·M2`](base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md). **No se pierde ninguna exigencia:** [`10·DEP3`](base/10-dependencias.md) ya pedía las dos cosas y agrega una que `S7` no decía — que quedarse muy atrás vuelve caro e inseguro actualizar después. `DEP3` deja de remitir a `S7`, que era la otra mitad del círculo.

## 23.16.0 — 2026-08-18

**MENOR** (una comprobación más; nada nuevo que cumplir).

**Si mañana dejaras esta herramienta por otra, nadie sabía qué se cae y qué se queda.** Ahora sí: de los 54 programas del estándar, **18 hablan con la herramienta y 36 no** — esos funcionarían igual con cualquier agente, o sin ninguno.

Lo que se caería son los ocho enganches y el instalador que los enchufa. Las reglas, que son texto, se quedan enteras.

**Y el mapa no envejece en silencio**, que es lo que le pasa a todo mapa escrito a mano: si aparece un programa nuevo que no está clasificado, se dice.

**El detalle.** Es el punto 1 del [pendiente 15](pendientes/15-el-estandar-depende-de-una-sola-herramienta.md), construido como la fase [`A-EP-005-HU-011`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/A-EP-005-HU-011-donde-termina-el-estandar/README.md) con su plan aprobado. Nace [`validadores/amarre.py`](validadores/amarre.py) y el subcomando `validar.py amarre`, que reporta **por los dos lados**: la pieza que existe y el mapa no nombra, y la que el mapa nombra y ya no existe. El segundo lado no lo pedía la historia — se agregó porque un mapa que promete clasificar algo borrado miente igual que uno incompleto.

**Lo que destapó al construirlo:** el mapa ya tenía el hueco sin necesidad de pieza nueva. Nombraba las 18 amarradas una por una y las libres **solo por su total**, así que **28 piezas no estaban nombradas en ningún lado**. Ahora van las 36 por su nombre: un total no es una clasificación, es la promesa de que alguien clasificó. 12 casos en [`test_el_mapa_del_amarre_no_envejece.py`](validadores/tests/test_el_mapa_del_amarre_no_envejece.py).

## 23.15.0 — 2026-08-18

**MENOR** (una lista nueva que organiza lo que ya se exigía; ninguna regla cambia).

**Aprobar un plan aprobaba por igual cambiar una coma y borrar algo que no se puede recuperar.** Ahora no: hay una lista de lo que el agente puede hacer, ordenada por lo que cuesta deshacer cada cosa.

Lo que se deshace solo se hace y se cuenta después. Lo que cuesta deshacer se anuncia antes, de una en una. **Y lo que no se deshace se pide aparte, cada vez** — aunque estuviera escrito en un plan ya aprobado.

**El detalle.** Es el [pendiente 13](pendientes/hecho/inventario-y-riesgo-de-las-acciones-del-agente.md), construido como la fase [`A-EP-001-HU-012`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/A-EP-001-HU-012-inventario-de-acciones-y-riesgo/README.md) con su plan aprobado. Nace el anexo [`base/00-identidad-y-rol/acciones-y-riesgo.md`](base/00-identidad-y-rol/acciones-y-riesgo.md) —12 clases, 3 🟢 · 4 🟡 · 5 🔴— y su comprobación en `validar.py acciones`. **`N1` a `N6` no cambian letra**, y hay un caso que lo vigila comparando su texto contra lo guardado.

**Tres cosas quedaron nombradas como irreversibles y antes no lo estaban:** borrar un archivo que no está en el control de versiones, correr algo que sale a la red, y escribir fuera del repositorio. Las tres caían en `N1` junto con cambiar una coma.

**Y tres defectos salieron de construirlo, los tres cazados por la máquina.** El que más enseña: el caso que borra una clase a propósito para ver si se reporta **no la reportaba**, porque la búsqueda miraba el archivo entero y el nombre seguía en otra sección. Sin ese caso, «cero huérfanas» habría significado que el programa no busca nada. 23 casos en [`test_las_acciones_tienen_su_riesgo.py`](validadores/tests/test_las_acciones_tienen_su_riesgo.py).

## 23.14.0 — 2026-08-18

**MENOR** (las comprobaciones arrancan donde estás parado; si las corrías desde tu proyecto, ahora sí lo revisan a él).

**Las comprobaciones que dicen revisar tu proyecto estaban revisando otra carpeta.** Si las corrías sin decirles dónde mirar, iban a parar a la carpeta donde vive el estándar — y devolvían un informe que parecía tuyo y no lo era.

Un proyecto lo descubrió al buscar claves sueltas en su código: le salieron dieciocho, todas de archivos que ese proyecto no tiene. Ahora arrancan donde está parado quien las corre.

**El detalle.** Es el [pendiente 63](pendientes/hecho/el-validador-de-secretos-se-revisa-a-si-mismo.md), reportado por `rni-dp`. El defecto no era el recorrido sino el valor por defecto de `--raiz`, que caía en `RAIZ` —la carpeta del propio estándar, calculada desde `__file__`—. **Cambian los 22 subcomandos que dicen «carpeta del proyecto»**; los que revisan el estándar siguen apuntando a `RAIZ`. No era solo `secretos`: los otros veintiuno tenían lo mismo y nadie lo había notado, porque casi siempre se corren desde el estándar y ahí las dos raíces coinciden.

**Y una exención, con cuidado:** las claves falsas de `test_la_clave_no_llega_al_historico.py` existen para comprobar que el detector detecta, así que se saltan. **Se nombran una por una y no por carpeta** — exceptuar `tests/` entero dejaría ciego al detector sobre lo que se escriba ahí mañana. Un caso de prueba fija que una clave de verdad sigue saliendo. 8 casos nuevos.

## 23.13.2 — 2026-08-18

**PARCHE** (se escribe una decisión que ya estaba tomada; nada cambia de comportamiento).

**Una conversación que sigue pasada la medianoche queda guardada con la fecha del día en que empezó, y nadie había escrito si eso está bien.** Está bien, y ahora se dice: el archivo es de una conversación, no de un día.

Partirla en dos rompería la forma de encontrarla, así que no se parte. Cada mensaje lleva su hora real, de modo que lo que pasó después de las doce se sabe leyendo. El resumen sí se guarda en el día en que pasaron las cosas, y esa diferencia es a propósito.

**El detalle.** Es el punto 3 del [pendiente 33](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), preguntado el 2026-08-06 y sin contestar desde entonces. **La decisión ya la tomaba la máquina:** `hook_historico.py` busca la sesión por su marca `<!-- sesion: id -->`, nunca por fecha, así que partirla dejaría media conversación sin marca y la siguiente sesión no la encontraría. Faltaba escribirlo, y quedó en [`plantillas/historico-chat.md`](plantillas/historico-chat.md) y en el README de la carpeta. El caso real está a la vista: una sesión con 91 turnos de un día y 27 del siguiente.

## 23.13.1 — 2026-08-18

**PARCHE** (una comprobación más y dos correcciones de forma; nada nuevo que cumplir).

**Una regla podía declararse intocable sin estar en el capítulo de lo intocable, y nadie lo miraba.** No es que contradijera a las de arriba: es que se las saltaba, quedando por encima sin haber pasado por donde se pasa. Ahora se comprueba.

**El detalle.** Del punto 8 del [pendiente 33](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), preguntado el 2026-08-07 y sin contestar desde entonces. `validar.py metareglas` reporta cualquier regla con la marca `[BLINDADA]` fuera de [`base/00-nucleo-blindado.md`](base/00-nucleo-blindado.md) — es la única mitad de [`20·M1`](base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) que un programa puede juzgar; que un nivel no contradiga al de arriba exige leer las dos reglas. Hoy da cero.

**Y el detalle que decide si el control sirve**, que ya estaba escrito en el resumen de aquel día: la palabra aparece en prosa en seis archivos, así que se ancla al **encabezado**. *«Un validador que reporta de más se termina apagando, y un control apagado es peor que ninguno porque figura como cubierto.»* Hay un caso de prueba dedicado a eso.

También del mismo punto: el plan de la fase `A-EP-001-HU-001` declara su origen en la forma que pide `13·DOC12`, y la tabla del [`CLAUDE.md`](CLAUDE.md) §3 ganó la fila de `anatomia/`.

## 23.13.0 — 2026-08-18

**MENOR** (una comprobación más que se puede correr; no cambia nada de lo que se exige).

**Pedir «menos es más» siete veces en tres días no hizo que las respuestas se acortaran.** Cada vez se anotaba el caso, y anotarlo no cambiaba nada: al final el registro era el sustituto de cumplir.

Lo que faltaba no era otro recordatorio, era un número. Ahora se puede medir cuánto ocupa lo que el agente contesta, y mirarlo al cerrar la sesión. **No detiene nada y no dice qué respuesta estuvo mal** — decir cuál palabra sobra sigue siendo cosa de quien lee.

**El detalle.** Es el [pendiente 58](pendientes/hecho/nada-hace-cumplir-id9.md), reportado por `shopnest-mesa`, con su salida 3: medir y no bloquear. Nace [`validadores/brevedad.py`](validadores/brevedad.py) y el subcomando `validar.py brevedad`, que lee la transcripción que ya escribe el enganche del histórico y reporta **la mediana por sesión** — no el máximo, porque una respuesta larga suele estar justificada y lo que señala un problema es que la mitad lo sean. Las otras dos salidas se descartaron con motivo: rebotar la respuesta obliga a leer la versión larga primero, e inyectar la regla en cada mensaje es lo que ya falló siete veces.

**Y hay un motivo que no estaba en el pendiente:** [`reglas-validables.md`](validadores/reglas-validables.md) ya declaraba que `ID9` no se puede comprobar con un programa. Un enganche que rebotara estaría afirmando lo contrario; uno que cuenta hace justo lo que esa declaración permite. Por eso la declaración quedó ahí y no en el cuerpo de la regla: meterla dentro la habría hecho más larga, **incumpliendo `ID9` al escribir cómo se comprueba `ID9`**. 21 casos en [`test_la_brevedad_se_mide.py`](validadores/tests/test_la_brevedad_se_mide.py).

## 23.12.2 — 2026-08-18

**PARCHE** (cuatro reglas dicen lo mismo en menos palabras; nada de lo que exigen cambia).

**Cuatro reglas venían con su explicación pegada y no se leían.** Una usaba mil doscientos caracteres para decir algo que cabe en cuatro líneas. Ahora la regla dice qué hay que hacer, y el detalle —qué carpetas quedan fuera, por qué autorizar un archivo no autoriza a su carpeta— vive aparte, enlazado.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), las cuatro que fallaban **solo** la fila 10: [`04·S9`](base/04-seguridad.md) 1 278 → 290 —su inventario de rutas se fue a [`notas/rutas-fuera-del-proyecto.md`](notas/rutas-fuera-del-proyecto.md)—, [`04·S10`](base/04-seguridad.md) 1 029 → 307, [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) 564 → 309 y [`05·E4`](base/05-errores-y-logging.md) 419 → 282. Las cuatro pasaron a **CUMPLE**: las reglas reprobadas bajan de 58 a **54**.

**Dos cosas que salieron de hacerlo.** `S10` no necesitó anexo: sus cinco viñetas eran la misma exigencia dicha cinco veces, más una lista de comandos concretos que por [`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) no debía estar en la base. Y `E4` tampoco: sus cuatro viñetas explicaban cuándo usar cada nivel de registro con un ejemplo, y el nombre del nivel ya lo dice.

## 23.12.1 — 2026-08-18

**PARCHE** (dos reglas dicen lo mismo en menos palabras; no cambia nada de lo que exigen).

**Dos reglas sobre datos venían con su explicación pegada y no se leían.** Una medía casi dos mil caracteres para decir algo que cabe en cinco líneas. Ahora la regla dice qué hay que hacer, y el porqué —por qué la gente se equivoca y qué se rompe cuando lo hace— vive aparte, enlazado.

**El detalle.** Del [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). [`03·D8`](base/03-datos.md) pasó de 1 962 a 292 caracteres —su porqué quedó en [`notas/pertenencia-y-autoria.md`](notas/pertenencia-y-autoria.md)— y [`03·D5`](base/03-datos.md) de 640 a 304, ganando además su excepción escrita en la forma que pide [`20·M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md). Las dos pasaron a **CUMPLE**: las reglas reprobadas bajan de 60 a 58.

**Y un efecto que conviene saber antes de tocar otra:** cambiarle el título a una regla le mueve el ancla, y las citas a esa ancla quedan rotas **sin que `validar.py estandar` diga nada**. Lo destapó `citas.py` al querer reescribir dos capítulos que citaban a `D8` por su título viejo.

## 23.12.0 — 2026-08-18

**MENOR** (la instalación deja una carpeta más; ningún proyecto tiene que hacer nada).

**Cuando el estándar corregía algo que un proyecto había reportado, el aviso de vuelta llegaba a uno de nueve.** Los otros ocho no tenían dónde recibirlo, y nadie se enteraba de que se había perdido.

Ahora la instalación deja puesta la carpeta del backlog, y los proyectos que ya estaban la reciben la próxima vez que se pongan al día. Y si aun así un aviso no puede llegar, se dice a quién no llegó en vez de callarlo.

**El detalle.** Es el [pendiente 61](pendientes/hecho/el-aviso-de-vuelta-llega-a-uno-de-nueve.md), con sus tres decisiones tomadas por el usuario. `pendientes/` entró a `CARPETAS_BASE` de [`instalar.py`](validadores/instalar.py) y a [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md), a la que se le volvió a aplicar el checklist. `cerrar.avisar()` devuelve ahora dos listas —lo entregado y lo que no— y `cerrar.py` imprime la segunda con el motivo. **No se le inventa la carpeta a ningún repositorio ajeno**, que era la decisión de fondo: lo que cambió es que el silencio se acabó. 9 casos nuevos en [`test_aviso_de_vuelta.py`](validadores/tests/test_aviso_de_vuelta.py).

## 23.11.2 — 2026-08-18

**PARCHE** (cambia una palabra; nada de lo que se exige cambia).

**El estándar usaba una palabra del oficio que nunca definió.** Llamaba «corrida» a ejecutar las pruebas, y quien no es del gremio no sabía si eso es una prueba, un grupo de pruebas o un día entero de trabajo. De eso dependía cómo se llena una columna del informe de pruebas.

Ahora dice «ejecución». El verbo se queda: *«las pruebas se corren»* se entiende bien y no se tocó.

**El detalle.** Es el [pendiente 26](pendientes/hecho/corrida-y-ejecucion-en-el-estandar.md), decidido por el usuario. Cambian ocho archivos de `base/` y `plantillas/`, incluida la entrada «Alcance de corrida» del [glosario](base/glosario.md) y el texto de [`02·F5`](base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), a la que se le volvió a aplicar el checklist porque editar una regla anula su sello — la fila 4 sigue en ❌ por el mismo motivo de antes, ajeno a la redacción. Queda a propósito *«la numeración corrida entre sesiones»* de [`plantillas/sesion.md`](plantillas/sesion.md): ahí la palabra significa otra cosa.

## 23.11.1 — 2026-08-18

**PARCHE** (se arregla un defecto de la instalación; no cambia nada de lo que se exige).

**Poner al día un proyecto pedía hacerlo dos veces, y dejaba una anotación de más.** La instalación escribía su constancia y, en la misma corrida, decía que faltaba escribirla. Al correrla otra vez —como el propio mensaje pedía— escribía una segunda constancia, vacía, siete segundos después de la primera.

La causa era cómo se ordenaban esas anotaciones: se comparaban como texto, y así la versión «23.10.0» quedaba antes que la «23.5.0», porque el uno va antes que el cinco. Leyendo la vieja como la última salían las dos cosas a la vez. Ahora se comparan como números.

**El detalle.** Es el [pendiente 62](pendientes/hecho/el-instalador-pide-una-segunda-pasada.md), reportado por `shopnest-mesa` al subir del `23.5.0` al `23.11.0` el mismo día. `versiones.registros()` ordenaba por `(fecha, sufijo)` y dejaba la versión fuera del criterio; con los dos registros del mismo día empataban y el desempate caía en el orden alfabético del nombre. De ahí salían los dos síntomas: el checklist leía la versión vieja como «última» y pedía el registro, y `registrar_version` creía que la versión había subido y escribía otro.

Se reabrió la fase [`A-EP-007-HU-006`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/README.md) en vez de abrir una nueva, con su ciclo 3 y 15 casos en [`test_el_registro_de_version_no_se_duplica.py`](validadores/tests/test_el_registro_de_version_no_se_duplica.py).

**Por qué pasó las pruebas la primera vez:** el caso que lo cubría montaba **un** solo registro, y con uno no hay orden que equivocar. El caso estaba bien escrito; el montaje no alcanzaba.

## 23.11.0 — 2026-08-18

**MENOR** (una regla nueva sobre cómo trabajar; ningún proyecto tiene que cambiar nada).

**Trabajar con dos ventanas abiertas sobre lo mismo hacía perder trabajo.** Cada una anotaba el número de la versión cuando empezaba, no cuando terminaba, y como las dos empezaban con el mismo número las dos escribían el mismo. Pasó cuatro veces en tres archivos distintos, y una de esas veces se perdió una anotación entera.

Ahora la norma es mirar el dato justo antes de escribirlo, no al empezar. Eso quita de encima la pregunta de si hay alguien más trabajando: si se mira en el momento, no hace falta saberlo.

**El detalle.** Nace [`20·M18`](base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md) —*lo compartido se lee un instante antes de escribirlo*—, que extiende a [`M10`](base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): `M10` ya pedía que el cambio, su entrada y la subida fueran en el mismo movimiento, pero no decía **cuándo** se lee lo que se va a escribir. Es el [pendiente 22](pendientes/hecho/dos-sesiones-versionando-a-la-vez.md), cerrado como la fase [`A-EP-002-HU-006`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/README.md) con sus dos criterios en cumple. La comprobación es [`validadores/numeracion.py`](validadores/numeracion.py), dentro de `validar.py versionado`, con 19 casos.

**Lo que destapó la simulación:** el cruce se rompe de dos maneras y solo una deja rastro. Si al resolver el choque se conservan las dos entradas queda un número repetido, que se ve; si se conserva una, **falta una entrada y no se ve**. Por eso el registro tiene dos `15.4.0` —marcadas, no renumeradas: un proyecto pudo haberla adoptado— y por eso la regla vale más que su validador, que solo llega después.

## 23.10.0 — 2026-08-18

**PARCHE** — se anotó que una regla ya existente cubría un caso que parecía sin resolver. **Ninguna regla cambió de texto.**

La duda era: cuando lo que se construye no es un programa sino un documento, ¿hay que escribir además un papel aparte que explique qué se va a hacer? Resulta que el estándar ya lo contestaba, y hacía meses: **lo que la historia dice que hay que lograr es ese papel.** Nadie lo había buscado.

Se intentó agregarlo como regla nueva y salió mal: lo escrito chocaba con otra regla del mismo capítulo. Se devolvió todo a como estaba.

**El detalle.** Es el [pendiente 20](pendientes/hecho/cuando-la-historia-hace-de-especificacion.md), cerrado citando [`02·F19`](base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) —*«la redacción del CA es la especificación funcional»*, desde la v3.1.0— en vez de escribir nada. La frase que se había agregado a [`02·F2`](base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) chocaba con [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), que prohíbe fusionar eslabones de la cadena; `F2` volvió a su texto y a su sello originales. Lo destapó una pregunta del usuario, no una comprobación — y de ahí salió la fase [`A-EP-005-HU-010`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo/), que hace llegar las reglas relacionadas al escribir.

## 23.9.0 — 2026-08-18

**MENOR** — las entradas de este archivo empiezan ahora explicando, en dos frases y sin palabras raras, qué cambió y por qué. Los nombres de archivo y las referencias internas siguen estando, pero más abajo.

Se cambió porque se le mostró una entrada vieja a quien no había seguido el trabajo y no entendió nada. No era una entrada mala: se revisaron las 83 y **ninguna** se entendía sin conocer el proyecto por dentro. Setenta y cuatro empezaban nombrando un archivo.

Las 83 anteriores se quedan como están. Reescribirlas es otro trabajo y no corre prisa; lo que corría prisa era que la próxima naciera legible.

**El detalle.** Nace [`20·M17`](base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), con su checklist en CUMPLE, y `validar.py metareglas` avisa cuando la entrada de la versión vigente abre con un identificador de regla, una ruta o jerga de la casa. Sale del `CA-03` de [EP-002 · HU-002](documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/HU-002-registro-de-cambios.md), que exige justamente eso y nunca se había comprobado con un lector de verdad.

---

## 23.8.0 — 2026-08-18

**MENOR** — los nombres de los roles estaban en inglés y ahora están en español: Explorer pasa a Explorador, Designer a Diseñador, y así con trece. La palabra «spec» pasa a «especificación».

Se cambió porque el estándar exige escribir en español todo lo que tenga traducción usada, y estos nombres se habían quedado sin traducir. Un proyecto al día no tiene que hacer nada: lo que cambia es cómo se llaman las cosas.

**El detalle.** Lo pide [`01·C20`](base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica), y eran **211 apariciones en 39 archivos**.

| Antes | Ahora |
|---|---|
| Explorer · Proposer · Designer | Explorador · Proponente · Diseñador |
| Épica Writer · HU Writer · Spec Writer | Escritor de épica · de historia · de especificación |
| Task Planner · Implementer · Verifier | Planificador de tareas · Implementador · Verificador |
| Reviewer · Orchestrator · Researcher | Crítico · Orquestador · Investigador |
| spec | especificación |

**Cuatro archivos cambiaron de nombre**, con sus citas arrastradas por `cerrar.mover`: `02·F2`, `13·DOC3`, `13·DOC6` y la plantilla de especificación de módulo. [`00·ID6`](base/00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md) se reselló, porque editar el texto de una regla anula su checklist.

**Queda uno a propósito:** la carpeta `skills/generar-spec-modulo/`. El nombre de una skill es cómo se la invoca, así que renombrarla cambia comportamiento y no solo texto.

---

## 23.7.5 — 2026-08-18

**PARCHE** — diez reglas que solo sobraban de largo caben ahora en el molde. **Ninguna cambia lo que exige.**

### Diez de una sola pasada, y por qué se podían hacer juntas

De las 70 reglas en NO CUMPLE, **quince fallan solo la fila 10** —el cuerpo de cuatro líneas de [`20·M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)— y diez de esas son puro exceso de explicación: no hay que partirlas, ni derogarlas, ni decidir nada.

**Es el único trabajo grande del [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) que no depende de una decisión.**

| Regla | Antes | Después |
|---|---:|---:|
| [`01·C13`](base/01-conducta.md#c13--preguntas-de-análisis-van-en-chat-abierto-no-en-formulario-cerrado) | 802 | **306** |
| [`09·G9`](base/09-git.md#g9--la-historia-de-usuario-es-la-unidad-del-commit) | 552 | **319** |
| [`01·C19`](base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) | 533 | **317** |
| `01·C12` · `01·C11` | 462 · 461 | **269** · **278** |
| [`04·S1`](base/04-seguridad.md#s1--autorización-en-cada-acción-sensible) · `04·S2` | 437 · 349 | **311** · **295** |
| `09·G7` · `17·I1` · `03·D3` | 421 · 395 · 378 | **270** · **293** · **306** |

Reglas en NO CUMPLE: **70 → 60**.

### Lo que sobra casi siempre es el porqué, y la regla ya lo decía

En **ocho de las diez** lo que se fue era razonamiento — por qué sobre-verificar molesta, por qué el formulario cerrado empobrece la respuesta, por qué lo que no se versiona se pierde. La fila 10 lo dice ella misma: *si no cabe, o son dos reglas o se está contando el porqué, que va a `notas/`*. **El diagnóstico acertó ocho de diez veces.**

### El bloque de ejemplo era espacio gratis y nadie lo usaba

La fila 10 mide **solo el cuerpo**. Un ejemplo largo no cuesta nada; una enumeración en el cuerpo cuesta todo. Y aun así las reglas más largas tenían ejemplos cortos — `01·C12` llevaba tres ejemplos de adjetivo **en el cuerpo** teniendo su bloque justo debajo.

**La forma de acortar sin perder nada estaba disponible desde el principio.**

### Nada se perdió, y se comprobó punto por punto

Los tres puntos de `D3`, los tres de `S1`, los cuatro de `S2`, los tres estados de `I1`, los tres criterios de `C13`. **Y ninguna excepción se tocó** — es lo único de una regla que no se puede resumir sin cambiar qué permite.

**Cada sello dice de cuánto a cuánto y qué texto salió**, para que quien lea dentro de un año sepa si lo que falta se perdió o se movió.

### Lo que **no** se tocó, de las quince

`03·D8`, `04·S9` y `04·S10` tienen dentro **un procedimiento**, no una explicación: es el caso de anexo. `05·E4` ya tenía decidido que su escala se va a un anexo, y `02·F13` se reescribió hace días.

**`04·S9` tiene además un motivo propio:** es **el único modelo de excepción completa del cuerpo** —condición, límite y autorizador—, y acortarla de paso entre otras nueve es la forma de perderlo.

**Y queda una deuda dicha:** el porqué que se sacó **no se escribió en `notas/`**. No se perdió —los sellos dicen qué salió de cada regla— pero no está donde `M5` manda.

Fase: [`E-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/E-EP-001-HU-009-las-que-solo-sobraban-de-largo/).

---

## 23.7.4 — 2026-08-18

**PARCHE** — dos reglas enlazaban a su vecina **y además la copiaban**. Se quedan con lo suyo; **ninguna exigencia desaparece del cuerpo**.

### El defecto se leía como diligencia

[`20·M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) pide que lo que ya dice otra regla esté **enlazado en vez de copiado**. [`07·Q7`](base/07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) y [`12·PR4`](base/12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes) hacían las dos cosas: **el enlace estaba puesto** y el texto repetido debajo.

Por eso duraron. Un enlace delante de un texto repetido se lee como cuidado, no como duplicación: **cumplían la mitad que se ve.**

| Regla | Se fue | Quedó |
|---|---|---|
| `07·Q7` | el criterio de alcance, que es [`01·C3`](base/01-conducta.md#c3--quédate-en-tu-tarea) | `C3` como motivo enlazado, y decirlo para su tarea |
| `12·PR4` | lo de logs, que es [`05·E5`](base/05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles) | pantallas, reportes y mensajes a terceros |

### La forma correcta ya estaba escrita en otra regla del mismo cuerpo

[`14·EST3`](base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `01·C3` **el mismo criterio de alcance** que `Q7`, y estaba en CUMPLE: la nombra entre paréntesis como el **motivo** y todo lo demás es suyo. `Q7` reformulaba el criterio entero antes de enlazarlo.

**Faltaba leerlas juntas.** El análisis del 2026-08-07 ya las había nombrado en la misma línea.

### Tres capas del mismo criterio, y solo una aportaba

[`00·N6`](base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada) (blindada) → `05·E5` → `12·PR4`, cada una reformulando a la anterior. La única parte que no dice ninguna otra regla es **la mitad de pantallas y reportes de `PR4`** — `E5` habla de logs. Es lo que la salvó de derogarse.

**Y su ejemplo se quedaba ilustrando lo que la regla dejó de decir:** era de logs. Un ejemplo así es peor que ninguno, porque manda a buscar la exigencia donde ya no está. Se cambió con ella. `PR4` además **declara ahora `depende de 05·E5`**, en una de las tres formas de [`20·M7`](base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md): la relación existía y no estaba dicha.

### Lo que **no** hace

**La categoría queda a medias, y se dice.** Siguen repitiendo `12·PR3` —que no exige nada propio—, `01·C16` —cuyo arreglo pasa por normalizar el bloque `Encadenamiento` en cuatro reglas a la vez— y [`04·S7`](base/04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas), cuyos dos sellos prescriben **derogarla** en favor de [`10·DEP3`](base/10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día).

**Las tres necesitan una decisión, no una redacción.** Derogar obliga a adoptarlo ([`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)) en todos los proyectos.

Reglas en NO CUMPLE: **72 → 70**. Fase: [`D-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/D-EP-001-HU-009-enlazar-en-vez-de-repetir/).

---

## 23.7.3 — 2026-08-18

**PARCHE** — cuatro reglas nombraban un stack, un dominio o una herramienta. Se dicen en concepto; **ninguna cambia lo que exige**.

### Quien heredaba el estándar leía reglas escritas para el stack de otro

[`20·M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md) manda que la base no nombre lenguaje, framework, motor, herramienta ni dominio real. Cuatro reglas lo hacían:

| Regla | Decía |
|---|---|
| [`01·C10`](base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) | `SQLite`, `MariaDB`, `React`, `Django` y «este ERP» |
| [`01·C15`](base/01-conducta.md#c15--al-replicar-un-patrón-replicar-la-paridad-completa) | «el módulo Aportes», de un proyecto real |
| [`01·C16`](base/01-conducta.md#c16--re-lee-justo-antes-de-editar--nunca-sobre-contexto-viejo) | Las órdenes de lectura y edición del agente, y dos del control de versiones |
| [`04·S10`](base/04-seguridad.md#s10--no-mates-procesos-globales--solo-pid-exacto-y-estrictamente-necesario) | `node` y `php` |

**No rompe nada, y por eso duraba:** un proyecto lee la regla, la entiende a medias y la aplica peor.

### `C10` no pasaba la pregunta que ella misma manda hacerse

Es la regla que enseña a decidir si algo es transversal o local, y **su criterio para decidirlo nombraba dos frameworks**: *«¿esta regla tendría sentido en un proyecto React + Django de otra empresa?»*. Ahora pregunta por otra empresa, otro lenguaje y otro negocio.

### La cuarta la encontró el programa, no una lectura

`S10` no estaba en la lista, y su sello explica por qué: **sí había argumentado la fila 5** —para defender `killall`, `pkill` y `taskkill`— y **al hacerlo la dio por revisada**. Los dos intérpretes estaban tres líneas más arriba.

**Un argumento sobre una fila no es una revisión de la fila.** Quien lee el sello ve que alguien la miró; no ve qué parte miró.

Y el detector callaba la mitad: `node` no estaba en su lista, así que de los dos nombres solo reportaba `php`. Ahora conoce `node`, `deno`, `bun`, `dotnet` y `softdeletes` — **solo lo que se le escapó de verdad**, porque una lista inflada por precaución empieza a reportar de más y una comprobación que reporta de más se apaga.

### Lo que se conserva, y por qué se escribió en una prueba

**`killall`, `pkill` y `taskkill` se quedan.** No son producto ni framework: son cómo se llama la misma acción en cada sistema, y quitarlos deja a `S10` sin decir qué prohíbe.

**Tienen su caso de prueba, y es el que más pesa de los nueve.** Un criterio que solo vive en un sello se pierde; uno que vive en una prueba se defiende solo — sin él, la próxima pasada los borra creyendo que mejora.

**Y [`04·S11`](base/04-seguridad.md#s11--escritura-contra-el-almacén-productivo-requiere-autorización-por-operación) sigue nombrando `SoftDeletes`**, también a propósito: ahí el nombre del método **es el argumento** —suena a borrar y escribe—, así que reescribirlo es parte de partir la regla. La prueba contra `base/` no exige cero: exige exactamente esa lista.

### El costo, dicho

`C10` pasó de 1724 a 1780 caracteres. **Escribir en concepto es más largo que nombrar la herramienta**, y es por eso que el nombre propio sobrevive: se lee más fácil y convence más. El ejemplo con código real de `03·D8` duró cuatro meses.

Fase: [`C-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/C-EP-001-HU-009-las-tres-reglas-con-nombre-propio/).

---

## 23.7.2 — 2026-08-18

**PARCHE** — dieciséis sellos de checklist decían dos cosas contrarias. Se corrige la descripción del veredicto; **ninguna regla cambia de texto**.

### La tabla decía una cosa y su propio párrafo, otra

Cada bloque de checklist tiene dos mitades: una tabla de veinte casillas y un texto que explica qué falla. **En cinco reglas no coincidían** — el texto reprobaba una fila que la tabla mostraba en ✅.

**Pesa porque la tabla es lo que se lee.** Nadie recorre veinte filas de prosa: se mira el renglón de emoticones y se sigue. Cuando las dos mitades se contradicen, gana la que se ve, que era la falsa.

**El defecto no era de juicio, era de transcripción.** En cuatro de los cinco se corrió **una casilla del bloque `C`** — siete seguidas, sin encabezado por columna, y contar de memoria hasta la séptima falla. Es exactamente lo que un programa hace sin equivocarse y una persona no.

**Y en los tres del capítulo `01` la fila que se perdió fue siempre la 5:** la que dice que la base no nombra tecnología. Escrita en el texto las tres veces, y las tres veces sin llegar a la tabla.

### Diez resúmenes que no cuadraban con su tabla, y un sello apilado

La línea de totales de diez sellos decía una cuenta y su tabla tenía otra — **nueve por el mismo lado**, una N/A de más y un ✅ de menos. Se recalcularon desde la tabla, que es lo que alguien puede verificar casilla por casilla.

Y [`20·M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md) llevaba **dos bloques de checklist superpuestos** desde el 2026-08-07, el de la `v2.1.0` encima del de la `v2.2.0`: quien leía de arriba abajo se quedaba con el viejo, que además tenía mal la cuenta. Un sello se reemplaza, no se apila. Es la regla que dice que ninguna regla nace fuera del procedimiento.

### Tres comprobaciones para que no vuelva

`validar.py metareglas` reporta ahora el sello cuyo texto reprueba una fila que su tabla da por buena, el resumen que no cuadra con su tabla, y la regla con dos sellos.

**Se escribieron antes de corregir nada, a propósito.** Al revés se habrían estrenado sobre un cuerpo ya limpio: cero hallazgos y ninguna forma de saber si sirven. Así, los cinco los encontró la comprobación — y el falso positivo también.

**Lo difícil no era encontrar: era no inventar.** La primera corrida reportó seis, y el sexto estaba bien: un sello en CUMPLE que cuenta qué reprobaba **antes** de corregirlo. Un CUMPLE ya no se compara contra su prosa; lo que sí se le exige es que su tabla no traiga ni un ❌. La mitad de los quince casos son de silencio, porque una comprobación que reporta de más se apaga a la semana.

### Lo que esto **no** hace

**No arregla ninguna regla.** Las 72 en NO CUMPLE siguen siendo 72, y [`01·C10`](base/01-conducta.md#c10--cada-mensaje-del-usuario-se-evalúa-como-posible-mejora-del-setup) sigue nombrando tecnologías concretas. Lo que cambió es que ahora su tabla lo dice. Eso es el [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

Fase: [`B-EP-001-HU-009`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/B-EP-001-HU-009-el-sello-no-se-contradice/).

---

## 23.7.1 — 2026-08-18

**PARCHE** — el aviso de vuelta de la 23.7.0 estaba escrito y probado, y **el comando no lo llamaba**.

### Lo que la 23.7.0 afirmaba y no era

La entrada de abajo dice *«el aviso lo escribe `cerrar.py` al cerrar»*. La función existía, tenía sus doce casos y todos pasaban — pero `main()` nunca la invocaba. **Cerrar un pendiente no avisaba a nadie**, que es exactamente el defecto que [`02·F24`](base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md) vino a cerrar.

**Lo destapó correr el comando de verdad**, no una prueba. Las pruebas llamaban a `avisar()` directamente, así que verificaban la pieza sin verificar que estuviera conectada.

### Y al conectarlo salieron dos más

- **El estándar se mandaba un aviso a sí mismo.** Está en su propio registro, y la comparación de rutas era por texto: el registro escribe `c:\` y el comando `C:\`. Ahora se compara con `normcase`.
- **El archivo se llamaba `algo.md.md`.** El destino ya traía su extensión.

Los tres tienen su caso ahora, y los dos nuevos comprueban **lo que se vio fallar**, no lo que debería pasar.

### Lo que dejó el primer envío real

Llegó a **un** proyecto de nueve, aunque la ficha decía «a todos»: los otros ocho no tienen carpeta `pendientes/` y a un proyecto que no lleva backlog **no se le inventa**. Queda anotado en el [61](pendientes/hecho/el-aviso-de-vuelta-llega-a-uno-de-nueve.md), porque lo que falta no es el aviso — es que ocho proyectos no tienen dónde escribir un pendiente.

---

## 23.7.0 — 2026-08-18

**MENOR** — el defecto del estándar se reporta, y al corregirlo el estándar avisa de vuelta. Aditivo: un proyecto al día no tiene que hacer nada.

### La regla que faltaba: `02·F24`

Nace [`02·F24`](base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md). Un proyecto que encuentra un defecto del estándar tenía tres caminos y **ninguno escrito**: parcharlo por su cuenta —y pisar a los demás—, anotarlo solo en su repositorio —donde el estándar nunca lo ve— o no hacer nada. Los tres pasaron en `shopnest-mesa` el mismo fin de semana, y ninguno incumplió nada, porque la regla no existía.

**Va al capítulo `02` y no a la épica de instalación:** lo que gobierna es un paso del flujo —qué hace el agente cuando lo que hay que arreglar no es suyo—; la instalación es por dónde viaja el aviso, no de qué trata la regla.

**Y cierra el choque con [`02·F20`](base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md):** `F20` manda parar y proponer, y no decía a dónde va lo propuesto cuando es del estándar. Ahora `F20` para y `F24` dice a dónde.

### El paso que nadie hacía era el sexto

Los siete pasos estaban dictados desde el 2026-08-16. Los cinco primeros se venían haciendo por criterio de cada sesión; **el aviso de vuelta no lo hacía nadie**, y sin él el séptimo —el pendiente del proyecto queda abierto hasta confirmar— deja pendientes abiertos para siempre: nadie vuelve a mirar el repositorio ajeno.

Ahora lo escribe [`validadores/cerrar.py`](validadores/cerrar.py) al cerrar, porque **el aviso es parte de cerrar**: un programa aparte abre la puerta a cerrar sin avisar, que es justo el defecto.

**Escribe un pendiente y nada más — nunca toca código**, y hay una prueba que compara la raíz del proyecto antes y después. Escribir en el repositorio de otro es bastante delicado como para que el alcance sea de una línea. Es idempotente, va solo a proyectos del registro, y al que no lleva backlog no se le inventa la carpeta.

### Dos plantillas, cada una nombrando a la otra

[pendiente-reportado](plantillas/pendiente-reportado.md) —el del estándar— y [pendiente-de-seguimiento](plantillas/pendiente-de-seguimiento.md) —el del proyecto, que **no se cierra al reportar**. Se nombran entre sí a propósito: uno sin el otro es exactamente la mitad que falló los dos días de agosto que originaron esto.

### Y se comprueba por programa

`validar.py pendientes` reporta el pendiente que dice venir de un proyecto sin nombrarlo — casilla vacía o con el molde `«…»` todavía puesto. **Los 34 del backlog pasan sin tocar ninguno**, que es la señal de que la regla describe lo que ya se hacía bien en vez de inventar una exigencia.

Fase: [`A-EP-007-HU-008`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/) · pendiente [36](pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md).

---

## 23.6.0 — 2026-08-18

**MENOR** — el enganche que recuerda escribir la señal, y su molde recortado. Aditivo.

### El recordatorio llega en el turno, no al cerrar

Nace [`validadores/hook_senales.py`](validadores/hook_senales.py), conectado a `UserPromptSubmit`. Al cerrar la sesión no sirve: **un chat no tiene final** y nadie sabe cuál fue el último mensaje hasta mucho después.

**Lo difícil no era avisar: era que no se volviera ruido**, que es lo que pasa con un aviso en cada turno. Tres condiciones lo evitan, y las tres tienen prueba: una vez por sesión, solo si el proyecto lleva señales, y **nunca escribe una señal** — reconocer qué merece serlo es criterio del agente.

La marca de «ya avisé» vive dentro del propio archivo, en un comentario invisible al leerlo. Un temporal se borraría al reiniciar y el aviso volvería.

### El molde de la señal pasa de siete campos a cuatro

**Qué pasó · por qué importa · qué se decidió · dónde queda.** Siete campos se llenan las dos primeras veces, y a la tercera la señal no se escribe — que es peor que escribirla incompleta.

Nada se pierde: la fecha y el autor los guarda el control de versiones.

### La plantilla dice qué es señal y qué es pendiente

Lo que se aprendió va a las señales; lo que falta hacer, a `pendientes/`. **Los dos salen del mismo momento y por eso se confunden**, y una misma conversación suele dejar las dos.

## 23.5.0 — 2026-08-18

**MENOR** — una regla nueva de conducta. Aditiva: ningún proyecto al día tiene que hacer nada.

### `01·C23` · Busca en el repositorio antes de preguntar

Antes de pedirle una decisión al usuario se busca si ya la dejó escrita, **en este orden**: la historia y su §9 · la épica · el resumen de sesión · el histórico · la memoria. De lo más específico a lo más general, parando en cuanto se encuentra.

Si está, se sigue **citando dónde** —o se muestra, si contradice lo pedido—. Si no, se pregunta **diciendo dónde se buscó**.

- **De dónde sale:** el 2026-08-14 el agente preguntó en qué orden trabajar dos historias y ofreció tres opciones. La respuesta estaba en la §9 de una de ellas. **La pregunta tenía premisa falsa:** cualquiera de las tres respuestas habría contradicho algo ya decidido.
- **No reduce las preguntas, cambia cuáles.** Preguntar lo que de verdad no está decidido es lo que evita adivinar.
- **Extiende [`01·C7`](base/01-conducta.md#c7--ante-dos-lecturas-pregunta)**, que manda preguntar ante dos lecturas y **da por hecho que el dato no está**.
- **Validable a medias, y así queda registrada:** que el agente haya buscado no lo puede ver ningún programa; que la respuesta traiga su cita, sí — y esa mitad queda pendiente.

**El orden no salió de una preferencia:** salió de dónde el estándar ya manda escribir cada cosa. Una decisión sobre una historia vive en la historia antes que en el histórico.

**Dos cosas las destapó el plan de pruebas, no la lectura.** La primera redacción no cubría el `CA-03` —mostrar la contradicción— y no cabía en el molde: 368 caracteres para 320. Se corrigió la regla, no el criterio, y el porqué del orden se fue a la historia.

## 23.4.0 — 2026-08-18

**MENOR** — cuatro comprobaciones nuevas, una herramienta que mueve sin romper, y un procedimiento que se va a su capítulo. Aditivo: ningún proyecto al día tiene que hacer nada.

### Ningún validador termina en silencio

**Treinta y tres de los cuarenta y cinco programas de `validadores/` salían con código 0 sin imprimir nada.** Un módulo que calla no es que falte: **afirma** — sale igual que cuando ha mirado todo y está en orden. Una fase se lo creyó y escribió «cero enlaces rotos» sobre veinte.

Ahora cada uno muere diciendo por dónde se corre, con su subcomando exacto, y sale con **código 2**: ni 0 ni 1, para que «no comprobé nada» no se confunda ni con «todo bien» ni con «hay fallas».

- **`validar.py metareglas`**, que faltaba. Es el único programa que comprueba once de las veinte filas del [checklist del estándar](base/20-meta-reglas/checklist.md) —entre ellas la 5, que `M3` necesita, y la 15, que impide que una regla normal mande sobre una `[BLINDADA]`— y no tenía por dónde correrse desde el 2026-08-14.
- La prueba que lo protege **lee los módulos del disco, no una lista**, así que el programa número 46 entra solo. Uno de sus casos comprueba que la lista no esté vacía: un barrido sobre cero archivos pasaría diciendo lo mismo que uno sobre cuarenta.

### Un sello de checklist vencido se reporta

Cada bloque de checklist cierra con «vale mientras el texto de arriba no cambie», y **nada lo comprobaba**. Una regla podía editarse y seguir mostrando un CUMPLE aplicado contra otro texto, otra versión y otro día. Es peor que no tener sello: el que no lo tiene al menos no engaña.

- Se compara **la fecha del sello contra la del último cambio**, y la fecha sale del control de versiones y no del disco: la del sistema de archivos cambia con un `clone`, un `checkout` o un antivirus, y daría vencidos falsos en cada máquina nueva. Sin dato **no se inventa un vencimiento**.
- Sale como **aviso**. Que un sello caducó no es que la regla esté mal escrita: es que hay que volver a mirarla.
- **Son 36 de 73.** Casi la mitad de las reglas selladas. Ese número no se sabía.

### Los enlaces y las citas dejan de reportar lo que no es

Cinco falsos positivos en `base/`, resueltos **sin tocar una línea de `base/`** — torcer el texto para callar al validador era la salida mala.

- Un enlace escrito entre comillas invertidas es una **muestra**, no un enlace: `comun.enlaces()` ya no mira ahí, igual que cualquier lector de Markdown.
- Un identificador en una **columna de ejemplos** —«Lo que sale mal»— muestra, no cita.
- La **segunda mención** del mismo archivo no pide enlace si la primera lo lleva.
- El **ancla al mismo archivo** es la forma correcta de citar a una vecina.
- Un enlace con `%20` se decodifica antes de buscarlo en disco.

**Y el reparador obedece al validador.** Medido antes de arreglarlo, `citas.py --aplicar` habría **escrito** esos cinco errores en `base/`. Si el validador no lo reporta, el reparador no lo toca.

### La carpeta del día nace con su línea en el índice

El enganche del resumen creaba la carpeta y el archivo, y no anotaba ninguno de los dos índices. Un resumen que no está en el índice es un resumen que nadie va a abrir — el defecto que el resumen existe para arreglar.

Se cerró por los dos caminos, porque hacen falta los dos: el enganche **escribe** la línea, y un validador **rompe** si falta. El enganche solo cubre lo que nazca de aquí en adelante.

**El enganche sigue sin escribir hallazgos:** poner el nombre de una carpeta en una lista no interpreta nada.

### Mover un documento ya no rompe sus citas

Nace [`validadores/cerrar.py`](validadores/cerrar.py). **No busca texto:** resuelve cada enlace contra el disco y compara rutas absolutas, así que da igual cuántos `../` lleve delante.

- Cerrar un pendiente a mano dejaba **58 enlaces rotos en 39 archivos**. Se midió al mover el 53.
- Recalcula **las dos direcciones**: lo que cita al archivo y lo que el archivo cita. Mover un documento lo baja un nivel y sus propios `../` quedan cortos.
- `mover()` sirve para cualquier `.md`, no solo para un pendiente.

### El registro de versión ya no dice que falta escribirse

El apartado «Qué quedó pendiente» se calculaba **antes** de escribir el archivo, así que el registro recién nacido se listaba a sí mismo como faltante. Ahora se calcula después: la foto se toma con el trabajo terminado.

Cuesta escribir el archivo dos veces. Es el precio de que diga la verdad.

### `base/13-documentacion/retrodocumentacion.md`

**Un procedimiento no es un molde:** no se copia ni se llena, se lee y se sigue. Estaba en `plantillas/` y pasa a vivir junto a la regla que lo exige, donde ya estaba `render-local-de-md.md`. Sus citas se arrastraron con él, y sus enlaces pasaron de `«RUTA-ESTANDAR»` a rutas relativas: `plantillas/` se copia dentro de los proyectos y `base/` no.

Nace [`plantillas/README.md`](plantillas/README.md), que dice que ahí viven **dos** cosas —modelos que llena una persona y fuentes con las que el instalador genera— y trae la pregunta que las separa. Con eso, un archivo sin marcas `«…»` deja de necesitar una lista de excepciones escrita a mano.

### Reglas puestas al día

- **`02·F13`** tiene su checklist aplicado otra vez. Decía «pendiente de aplicar» desde el 2026-08-08, una forma que el validador no reconocía: figuraba como aviso cuando era una regla publicada sin sello válido. **Reprueba la fila 10** —631 caracteres para un molde de 320— y así queda escrito.
- **`14·EST3`** reprobaba la misma fila por **tres caracteres**. Se recortó el porqué y quedó en CUMPLE. No cambia qué exige.
- **`14·EST1` y `14·EST3`** quedan selladas en CUMPLE; **`14·EST2` en NO CUMPLE**, y su bloque dice por qué: son tres reglas metidas en una, y por eso ni el título puede ser imperativo ni el cuerpo cabe.
- **El capítulo `15` entero**: `IM1`, `IM4` e `IM5` en CUMPLE; `IM2` e `IM3` en NO CUMPLE. `IM2` pasa a llamarse *Guarda los tres estados y la trazabilidad de quien anula* — el título anterior nombraba un tema sin decir ninguna norma. No cambia qué exige.
- **El capítulo `11` entero**: `CFG1`, `CFG2` y `CFG4` en CUMPLE; `CFG3` en NO CUMPLE — son tres exigencias en una. A `CFG4` se le agregó el ejemplo INCORRECTO/CORRECTO que le faltaba: la bandera que se enciende al liberar y nadie quita.
- **El capítulo `12` entero**: `PR1`, `PR2` y `PR5` en CUMPLE; `PR3` y `PR4` en NO CUMPLE. `PR5` pasa a llamarse *Define cuánto se conservan y qué pasa después* y `PR2` gana su ejemplo. **`PR3` es la grave: no exige nada propio** — sus cuatro frases remiten al capítulo `04`, así que quien la cumple no hace nada distinto de cumplir aquel. Es un índice con forma de regla.
- **El capítulo `10` entero**: `DEP1`, `DEP2`, `DEP4` y `DEP5` en CUMPLE; `DEP3` en NO CUMPLE por repetir `04·S7`. **El arreglo está en el otro capítulo:** `DEP3` es el dueño correcto —una vulnerabilidad de una dependencia es asunto de dependencias— y lo que toca es derogar `S7`. `DEP3` y `DEP5` ganan el ejemplo que les faltaba.
- **El capítulo `05` entero**: `E1`, `E3` y `E5` en CUMPLE; `E2` y `E4` en NO CUMPLE. `E2` son dos exigencias y **la mitad que sobra ya se cita desde fuera** —`15·IM3` y el `13` apuntan acá para la transacción—, así que al partirla hay que llevar esas citas. `E4` no cabe: su escala de cuatro niveles es una tabla de referencia dentro de una regla.
- **El capítulo `06` entero, y es el primero que queda sin una sola regla reprobada:** `R1` a `R6`, las seis en CUMPLE. Sirve de referencia de qué aspecto tiene un capítulo al día.
- **El capítulo `07` entero**: `Q1` a `Q6` en CUMPLE; `Q7` en NO CUMPLE por reformular `01·C3` en vez de enlazarla. `Q6` gana el ejemplo que le faltaba.
- **El capítulo `08` entero**: `T2`, `T3`, `T5` y `T6` en CUMPLE; `T1`, `T4` y `T7` en NO CUMPLE. **`T7` es la regla más larga del cuerpo: 1645 caracteres para un molde de 320**, y ella misma declara que cubre «dos frentes». **`T1` es la más delicada:** su excepción deja al agente autorizándose a sí mismo a no probar.
- **El capítulo `17` entero**: `I2`, `I4`, `I5` e `I6` en CUMPLE; `I1` e `I3` en NO CUMPLE. **`I6` se llamaba «Adaptable»** —una sola palabra, que ni ordena ni enuncia nada— y pasa a *Funciona en los tamaños de pantalla que el proyecto soporta*. `I5` e `I6` ganan el ejemplo que les faltaba.
- **El capítulo `03` entero, y es el peor del cuerpo:** siete de sus ocho reglas reprueban. Solo `D2` cabe en el molde. **`D7` mide 3839 caracteres —doce veces el molde y la regla más larga del estándar—** y es un manual de ocho pasos con encabezado de regla. `D8` traía en su ejemplo el código de un stack y una entidad reales, contra `M3`: reescrito en pseudocódigo agnóstico.
- **El capítulo `04` entero, y es el que más reprueba:** diez de sus once reglas. Solo `S8` pasa. `S4` pasa a llamarse *Guarda los secretos fuera del código y rota el que se expuso*. **`04·S9` resultó ser el modelo de excepción del estándar** —la única cuya excepción declara condición, límite y autorizador—, y eso es justo lo que les falta a `08·T1`, `03·D4` y `03·D5`.
- **El capítulo `09` entero**: `G1` a `G5` en CUMPLE; `G6` a `G9` en NO CUMPLE. `G3` pasa a llamarse *Deja fuera del control de versiones los secretos y lo generado* y `G4` gana su ejemplo. **El corte que el análisis proponía para `G8` reservaba el número `G9`, y ese número ya está ocupado** por una regla que nació después: la mitad que salga se lleva `G10`.
- **El núcleo blindado, las seis:** `N2`, `N3` y `N5` en CUMPLE; `N1`, `N4` y `N6` en NO CUMPLE. **`N1` es lo más serio de la pasada: una regla `[BLINDADA]` con una excepción escrita**, cuando la cabecera del capítulo promete que nada las desactiva. El arreglo es de forma —eso no es excepción sino el alcance de la autorización— y no se toca acá: el núcleo cambia con decisión del usuario.
- **Los capítulos `18` y `19` enteros**, los dos `opt-in` de DevOps: catorce reglas, **y ninguna tiene un solo ejemplo INCORRECTO/CORRECTO**. Nacieron juntos y se escribieron de corrido. Se anota como un trabajo y no como catorce: el capítulo es la unidad, y hoy ningún proyecto los tiene encendidos.
- **El capítulo `01` y `20·M15`, los últimos que faltaban. Las 200 reglas del cuerpo tienen ya su bloque de checklist**, y **`01·C14` traía la peor cita del estándar**: atribuía a `01·C1` un texto que `C1` no dice. Es el único hallazgo de la pasada falso de contenido y no de forma. Corregida.
- **Las reglas sin sello bajan de 121 a 0**; las publicadas en NO CUMPLE suben de 7 a 72. Ese número sube porque ahora todas dicen la verdad: **el sello ya no es el problema, lo es lo que el sello dice.**

### `citas.py` no pedía enlace dos veces… salvo en el mismo renglón

La regla que nació con el pendiente 55 —la segunda mención no pide enlace si la primera lo lleva— miraba solo las **líneas anteriores**. Dos menciones en el mismo renglón se le escapaban, y el reparador quería enlazar la segunda.

Ahora mira el tramo de línea que queda a la izquierda, incluidos los enlaces que ya venían escritos. Se descubrió sellando `07·Q4`. Ese segundo número **sube porque ahora dicen la verdad**: antes no tenían bloque. El que mide el avance es el primero.

### La fila 10 medía mal, y castigaba a las reglas que citan bien

`M5` da cuatro líneas —320 caracteres— y `M15` exige que **toda** cita lleve su enlace. El conteo cobraba el marcado completo: cada enlace costaba unos cincuenta caracteres que nadie lee.

**Dos reglas del estándar tirando en direcciones contrarias, y perdía la que se cumplía.**

- De las **108** reglas que se pasaban del límite, **27 se pasaban solo por eso**. `ID3` contaba 561 y son 265.
- Ahora se mide el cuerpo **leído**: `[texto](destino)` cuenta como `texto`. Las que se pasan bajan de 108 a **78**, y ninguna de las 30 rescatadas hubo que tocarla.
- **No relaja la fila:** la regla que de verdad no cabe sigue sin caber, y hay una prueba que lo fija.
- Conviene volver a mirar cualquier lista de «reglas largas» hecha antes de esta fecha.

## 23.3.0 — 2026-08-17

**MENOR** — dos comprobaciones nuevas que cuentan lo que antes se contaba a mano. Aditivo: ningún proyecto al día tiene que hacer nada.

### La numeración de pendientes se comprueba sola

Nace [`validadores/pendientes.py`](validadores/pendientes.py) con su subcomando `pendientes`, de la fase [`A-EP-004-HU-018`](documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/A-EP-004-HU-018-el-numero-de-pendiente-libre/). Dice el próximo número libre, avisa del repetido y cruza la carpeta con su índice.

- **Al construirlo apareció que la carpeta no es la fuente de la numeración.** Al cerrarse, un pendiente se mueve a `hecho/` y **pierde su número**: `02-vigencia…md` pasa a `vigencia-y-poda-de-memoria.md`. Mirando los archivos, el 02 parece libre — y no lo está. **Quince de los cincuenta y cinco números tomados existen solo en el índice**, en su fila tachada.
- Sin ese hallazgo, el validador habría entregado el 02 al siguiente pendiente y roto en silencio toda cita al 02 anterior. Un validador equivocado es peor que ninguno, porque se le cree.
- El número que entrega es **el siguiente al mayor, no el primer hueco**: los huecos son historia, y reutilizarlos haría que «el 02» apuntara a dos cosas según cuándo se leyera.

### La corrida de fases dice cuántas HU hay y cuántas están completas

`validar.py fases` cierra con una línea nueva: `HU: 68 en total · 25 completas · 43 incompletas (F12.2)`. Sale de la fase [`A-EP-004-HU-017`](documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/A-EP-004-HU-017-la-corrida-cuenta-las-hu-sin-fase/).

- **Una HU cuenta completa cuando todas sus fases tienen los cinco documentos**, no cuando alguna los tiene. Con dos fases y una a medias la historia no está terminada, y contarla completa escondería justo el trabajo que falta.
- **La línea va después de los hallazgos y aparece aunque no haya ninguno:** es el resumen de cuánto falta, no un incumplimiento más.
- **Cruza con el [pendiente 48](pendientes/48-inventario-hu.md)**, que lleva la misma cuenta a mano. Hay una prueba que compara los tres números: si se separan, una de las dos está mal y la suite lo dice.
- Los tres bordes quedan definidos y escritos en [`validadores/docs/fases.md`](validadores/docs/fases.md): árbol sin `epicas/` calla, épica sin HU no aporta, y carpeta `HU-` sin su `.md` **cuenta como incompleta** — existe como trabajo aunque le falte el papel.

## 23.2.1 — 2026-08-17

**PARCHE** — el enganche del resumen prepara su salida, como los otros cinco. No cambia qué se exige.

`hook_resumen.py` era **el único** de los seis enganches que no llamaba a `preparar_salida()`. Su texto lleva acentos y comillas angulares, así que salía en la página de códigos de la consola: quien lo leyera recibía mojibake, y con la salida en una tubería no se podía ni decodificar — dos pruebas del camino real llevaban tiempo en rojo por eso.

- **Es el pendiente [45](pendientes/hecho/instalar-prepara-su-propia-salida.md) otra vez, en otro archivo.** Allá `instalar()` se moría al imprimir una flecha porque solo `main()` preparaba la consola. Mismo descuido, misma clase de síntoma.
- **Nace la prueba que impide que se repita:** `TodoEnganchePreparaSuSalida` recorre los seis y falla si alguno no lo hace, para que la lista no quede coja cuando nazca el séptimo.
- Salió al ejecutar las fases del pendiente [48](pendientes/48-inventario-hu.md).

## 23.2.0 — 2026-08-16

**MENOR** — plantilla nueva. No cambia qué se exige: `02·F12.2` ya pedía la fase, y esto es el molde del tablero que muestra cuáles la tienen.

Nace [`plantillas/inventario-hu.md`](plantillas/inventario-hu.md), el inventario de historias de usuario: **una fila por HU y una casilla por documento** de la fase (`plan_trabajo`, `plan_pruebas`, `resultado_pruebas`, `estado-fase`, `funcionalidad_implementada`).

- **Sale de un caso real.** En este repositorio, **52 de las 66 HU** no tienen su fase completa: 49 sin ninguna carpeta de fase y 3 a medias. El inventario quedó en el pendiente [48](pendientes/48-inventario-hu.md).
- **Lleva todas las HU, también las completas.** Un tablero que solo anota lo que falta no deja decir cuántas hay ni de dónde salió el número.
- **Los dos contadores se corrigen juntos.** Al cerrar una fila, `Completas` sube uno e `Incompletas` baja uno en la misma edición; si se pierde la cuenta, se recuenta mirando la tabla.
- **Separa construcción de retrodocumentación**, que es casi todo lo que falta acá: el código existe y lo que no existe es el documento que diga con qué plan se hizo y qué salió — el mismo hallazgo del pendiente [38](pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md).

## 23.1.1 — 2026-08-16

**PARCHE** — ninguna regla del estándar queda fuera del registro de lo validable. No cambia qué se exige ni el texto de ninguna regla.

El validador de meta-reglas reportaba **33 reglas sin clasificar**, incluidos los capítulos `18` y `19` completos. Bajaron a cero en la fase [`A-EP-001-HU-009-clasificar-las-que-faltan`](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/).

- **Quince ya estaban clasificadas**, y el problema era cómo: el registro decía `C1–C17` y el programa busca cada identificador literal. **Un documento que alimenta a un programa se escribe como el programa lee.**
- **Los capítulos `18` y `19` no aparecían ni una vez**, ni para decir que no se validan. Ser opt-in no exime: `20·M9` no exceptúa a las reglas opcionales.
- **`20·M15` y `02·F12` ya estaban construidas** y no figuraban entre los validadores hechos.
- La lista de validables **creció** de ~12 a ~22: clasificar de más como «no validable» era el camino cómodo.

**El [pendiente 19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) no cierra:** siguen las siete publicadas en «no cumple» —que necesitan una decisión de quien define el estándar— y las 121 sin bloque de checklist.

## 23.1.0 — 2026-08-16

**MENOR** — una fase ya no puede tener dos veredictos distintos sin que se note. Aditivo: no cambia ningún molde.

El veredicto de una fase se escribe **dos veces a mano** —en el §6 del `resultado_pruebas` y en el `estado-fase`— y nada comprobaba que dijeran lo mismo. Ya habían dejado de decirlo: en `A-EP-003-HU-010` el resultado decía «No cumple» y el estado-fase seguía diciendo «aprobada». El `estado-fase` es el que se mira para pasar la puerta de verificación. Se construyó en la fase [`A-EP-004-HU-014-comparar-los-dos-veredictos`](documentacion/epicas/EP-004-comprobacion-automatica/HU-014-un-solo-veredicto-por-fase/A-EP-004-HU-014-comparar-los-dos-veredictos/).

- **`veredicto()` en [`validadores/fases.py`](validadores/fases.py)** compara tres cosas: el concepto, las exigencias en «No» del §5 con la fase dada por cumplida, y el conteo de criterios. Comparar solo el concepto dejaría medio archivo verificado.
- **Dos límites a propósito:** si falta uno de los dos documentos calla —una fase a medio escribir no es una contradicción—, y «Cumple, con una salvedad» no contradice a «Cumple».
- **Cuatro casos de prueba nuevos.** El repositorio pasa de 32 a 36.

**La decisión que faltaba, tomada y escrita:** compara un programa, y el `estado-fase` sigue escribiendo su veredicto. La otra salida —que lo enlace en vez de copiarlo— obligaría a reescribir todas las fases cerradas; si algún día se hace, esta comprobación se retira.

## 23.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar — la revisión de la instalación deja de decir «completo» con la cadena vacía.

`02·F0` exige `planteamiento → épica → HU → especificación → plan → código`, y la revisión no miraba ninguno de los tres primeros: un proyecto podía tener código commiteado, `prompts/` sin un solo archivo y ninguna épica, con el arranque diciendo **«13 de 13, instalación completa»**. Pasó en `shopnest-mesa`, y lo notó el usuario preguntando. Se construyó en la fase [`A-EP-007-HU-007-la-revision-ve-la-cadena`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/A-EP-007-HU-007-la-revision-ve-la-cadena/).

- **La lista de componentes pasa de 13 a 14**, con el punto `cadena` en [`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md): al menos un planteamiento en `prompts/`, y una épica si ya hay código en `proyectos/`.
- **Es el único punto que el instalador no instala**, y su columna lo dice. El planteamiento lo escribe el agente con lo que el usuario quiere; dejar la plantilla cruda sería peor, porque parecería un planteamiento y la revisión lo daría por cumplido.
- **La épica solo se exige si ya hay código.** A un proyecto recién instalado no se le pide: el ruido se deja de leer.
- **Tres casos de prueba nuevos.** El repositorio pasa de 29 a 32.

**Qué tiene que hacer un proyecto al día:** correr el instalador una vez —la huella del stack cambió— y escribir su planteamiento si no lo tiene. Hasta entonces dirá «13 de 14», que es el punto.

## 22.1.0 — 2026-08-16

**MENOR** — un programa comprueba que cada regla de negocio diga de dónde baja. Aditivo: lo que obliga ya lo declaró la 22.0.0.

La 22.0.0 fijó el molde; esta escribe el programa que lo mira. Se construyó en la fase [`A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen`](documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/A-EP-004-HU-004-la-regla-de-negocio-declara-su-origen/).

- **`reglas_sin_origen()` en [`validadores/plantillas.py`](validadores/plantillas.py)** marca como **falla** cada regla del §4 sin identificador de procedencia. Es falla y no aviso: una regla sin fuente ya llegó hasta un criterio de aceptación en un proyecto real, y lo que avisa se ignora.
- **Un `spec.md` ahora se reconoce.** Antes no se comparaba contra ninguna plantilla —el programa no sabía cuál le tocaba—, así que el documento más importante de un módulo era invisible para el validador de forma. Sin esto, la comprobación nueva no se habría disparado nunca.
- **Tres casos de prueba nuevos**, con las dos reglas reales del caso que lo destapó. El repositorio pasa de 26 a 29 pruebas.

**Lo primero que encontró fue deuda propia:** las dos especificaciones de este repositorio traen **31 reglas de negocio sin origen**. No se apagó la comprobación para que el número diera cero; quedaron en el [pendiente 47](pendientes/hecho/el-origen-de-las-reglas-de-negocio.md).

## 22.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar — toda regla de negocio dice de dónde baja.

El §4 del modelo de especificación pedía `«Regla — por qué existe.»`: **el porqué, nunca el de dónde**. Una regla de negocio no se inventa en la especificación de un módulo —baja de un requisito, de una historia o de una decisión—, pero como nadie lo preguntaba, una regla con buena justificación y ninguna procedencia entraba sin resistencia. En `shopnest-mesa` una así bajó sola a una decisión, una fila de trazabilidad, dos escenarios de prueba y un criterio de aceptación; tardó un día en verse, y solo porque alguien preguntó de dónde salía. Se construyó en la fase [`A-EP-003-HU-004-el-origen-de-la-regla-de-negocio`](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-004-modelo-de-la-especificacion/A-EP-003-HU-004-el-origen-de-la-regla-de-negocio/).

- **El molde pasa a ser** `«Regla — de dónde baja (el identificador del requisito, la historia o la decisión) — por qué existe.»`, en [`plantillas/plantilla-especificacion-modulo.md`](plantillas/plantilla-especificacion-modulo.md).
- **Se pide un identificador, no una frase.** «Lo pidió el cliente» no se puede seguir hasta ninguna parte.
- **La regla sin procedencia no se escribe ahí:** se sube a la historia que corresponda y baja desde allá.

**Qué tiene que hacer un proyecto al día:** escribir la procedencia en cada regla de negocio que agregue de acá en adelante. **No** hay que reescribir las especificaciones ya escritas: quedan selladas con su versión, les falta un dato y no quedan inválidas.

## 21.3.1 — 2026-08-16

**PARCHE** — el programa que comprueba la `F22` queda retrodocumentado y bajo prueba. No cambia qué se exige ni una línea de producción.

El 2026-08-16 se escribió [`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) y, en la misma sesión, el programa que la comprueba — sin épica, sin historia y sin fase. El repositorio que escribe la regla, incumpliéndola mientras la escribe. Se retrodocumentó en la fase [`A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22`](documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22/).

- **Los tres criterios de la HU-015 quedaron con evidencia de una corrida real**, en [`validadores/tests/test_version_derogaciones.py`](validadores/tests/test_version_derogaciones.py): el proyecto atrasado con fases falla y la falla nombra la regla, lo ya adoptado no se vuelve a cobrar, sin fases no se cobra, y los límites callan en vez de romper. El repositorio pasa de 22 a 26 pruebas.
- **Los casos corren contra las derogaciones reales del estándar.** Si cambia la marca del encabezado que [`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) exige, la prueba lo dice en vez de pasar contra un dato inventado.
- **Lo que le faltaba al trabajo sin cadena no era documentación, era prueba.** `validadores/docs/version.md` ya explicaba las tres funciones con ejemplos; lo que nadie había escrito era con qué se comprobaban.

## 21.3.0 — 2026-08-16

**MENOR** — renombrar una sesión deja coherente el resumen que arrastra. Aditivo: ningún proyecto tiene que hacer nada.

`historico.py --renombrar` movía el resumen de la sesión a su nombre nuevo, pero adentro el enlace de vuelta a la transcripción se quedaba apuntando al nombre viejo. Es el propio estándar el que pide nombrar la sesión, y el comando que ofrecía para hacerlo dejaba el repositorio con un enlace roto. Lo reportó `shopnest-mesa` y le pasó tres veces a esta casa el mismo día. Se construyó en la fase [`B-EP-005-HU-008-renombrar-deja-el-resumen-coherente`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/B-EP-005-HU-008-renombrar-deja-el-resumen-coherente/).

- **`_reenlazar()` corrige el enlace de adentro del resumen**, texto y destino: un enlace que abre pero se anuncia con el nombre viejo también miente ([`13·DOC14`](base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md)). Se reemplaza el par exacto, así que un resumen que nombre otras sesiones las conserva intactas.
- **Nace la primera suite de pruebas de `historico.py`** — [`validadores/tests/test_historico_renombrar.py`](validadores/tests/test_historico_renombrar.py), tres casos: el normal, el que nombra otra sesión y el de una sesión sin resumen. El repositorio pasa de 19 a 22 pruebas.
- **La HU-008 gana su `CA-04`.** Su `RN-06` pedía el arrastre desde el principio y ningún criterio lo medía, así que no había de dónde derivar el plan ([`02·F18`](base/02-flujo-de-trabajo/reglas/F18-deriva-el-plan-de-los-ca-aprobados-no-de-la-proactividad.md)).
- **`validadores/docs/historico.md`** documenta `renombrar()`, `_mover_resumen()` y `_reenlazar()`, que no estaban.

## 21.2.1 — 2026-08-16

**PARCHE** — el instalador se moría al imprimir si nadie le había preparado la consola. No cambia qué se exige.

`validadores/instalar.py` escribe su avance con tildes y con una flecha `→`, y la consola de Windows tal como arranca no admite esos caracteres: al llegarle uno, el programa **se muere ahí mismo**, no instalando sino escribiendo en pantalla. Para eso existe `preparar_salida()`, pero solo la llamaba `main()` — o sea únicamente al correrlo desde la línea de comandos. Un programa que llamara a `instalar()` como biblioteca lo mataba. Se construyó en la fase [`B-EP-007-HU-001-prepara-su-propia-salida`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/).

- **`instalar()` prepara su propia salida al entrar.** Delegarlo en quien lo llame era pedirle al de afuera que conociera las tripas del de adentro.
- **Su prueba comprueba que se pone roja sin el arreglo**, que no es un lujo: el primer caso instalaba en carpeta vacía y **pasaba en verde con el defecto puesto**, porque esa corrida nunca imprime una flecha. Ahora instala, sube la versión para que los sellos queden viejos, y comprueba que la corrida medida sí imprimió una `→`.
- **Se quitó el rodeo** que la [21.2.0](#2120--2026-08-16) había puesto en su propia prueba para esquivar esto.

**Qué hacer para quedar al día:** nada. El programa vive en el estándar y los proyectos lo llaman por su dirección.

## 21.2.0 — 2026-08-16

**MENOR** — el instalador repara lo que ya estaba instalado, y registra la versión aunque no cambie ninguna plantilla. No cambia qué se exige.

**Lo que la [21.1.0](#2110--2026-08-16) arregló no llegaba a los proyectos ya instalados, y el registro de versión se quedaba atrás para siempre.** Dos defectos que reportó `shopnest-mesa` y que resultaron ser el mismo: el instalador decide si hay trabajo mirando una huella, y cuando la huella no cambia se queda quieto aunque el proyecto sí esté mal. Se cerraron juntos en la fase [`A-EP-007-HU-006-poner-al-dia-lo-ya-instalado`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/).

- **Toda copia que ya existe pasa por `_reparar_marcadores`.** Rellena en el sitio los huecos que quedaron crudos de una instalación anterior y no reescribe nada más. Sin bandera: reinstalar repara. Antes, «al día» se medía contra la plantilla central, así que una copia podía estar al día y mal escrita a la vez.
- **Lo que llena el proyecto no se toca.** `_rellenar` solo conoce los huecos que el instalador sabe calcular; `«motor»` o `«manual / pipeline»` salen intactos, y un caso de prueba cuenta los huecos antes y después para comprobarlo.
- **Subir de versión es por sí solo motivo de registro.** Antes el instalador decía «nada que registrar» y la revisión decía «falta el registro»: el proyecto se quedaba en 12 de 13 para siempre, con el aviso de instalación incompleta sonando en cada mensaje y sin más salida que editar a mano un archivo que dice que no se edita a mano. A la carpeta del propio estándar no se le escribe registro: lleva este `CHANGELOG`.
- **Se corrigió el texto de ayuda de la fila `versiones`** en [`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md), que mandaba hacer lo que el instalador ya había hecho.
- **Su prueba:** [`validadores/tests/test_instalar_reparar.py`](validadores/tests/test_instalar_reparar.py), seis casos. Los cinco automáticos corren contra una copia desechable del estándar, para poder editarle una plantilla y subirle la versión sin tocar el de verdad ([`00·N4`](base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

**Qué hacer para quedar al día:** correr el instalador una vez. Repara la copia y escribe el registro que falte, sin banderas y sin editar nada a mano. Es lo que la [21.1.0](#2110--2026-08-16) decía que no se podía.

## 21.1.1 — 2026-08-16

**PARCHE** — el revisor de enlaces daba un veredicto distinto según desde dónde se lo corriera. No cambia qué se exige.

**Un enlace bueno salía roto dentro de un proyecto.** [`validadores/enlaces.py`](validadores/enlaces.py) resolvía `«RUTA-ESTANDAR»` contra la carpeta que estaba revisando, dando por hecho que esa carpeta era el estándar. No lo es: los enganches corren el programa desde el estándar y le pasan el proyecto como `--raiz`, así que iba a buscar `«proyecto»/base/…`, una carpeta que ningún proyecto tiene — las reglas no se copian, se enganchan por su dirección completa. Dentro de un proyecto el marcador **no se resolvía bien nunca**, ni cuando estaba bien puesto.

Es la otra mitad de lo que dejó la [20.0.1](#2001--2026-08-16), y se construyó en la fase [`A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar`](documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar/).

- **El marcador se resuelve contra la carpeta donde vive el estándar.** Corriendo sobre el propio estándar las dos coinciden, así que acá no cambia nada: se comprobó comparando la salida antes y después, y son idénticas.
- **Se queda aunque la [21.1.0](#2110--2026-08-16) haga que dejen de llegar marcadores.** Aquella quita la causa; esta es la red para el que se escape mañana.
- **Su prueba:** [`validadores/tests/test_enlaces_marcador.py`](validadores/tests/test_enlaces_marcador.py). Comprueba que la misma cita da el mismo veredicto desde dos carpetas distintas, y que lo que no resuelve se sigue reportando — un arreglo que callara sería peor que el defecto.

**Qué hacer para quedar al día:** nada. El programa vive en el estándar y los proyectos lo llaman por su dirección, así que ya corren esta versión.

## 21.1.0 — 2026-08-16

**MENOR** — arregla la instalación y suma la prueba que faltaba. No cambia qué se exige.

**Tres de los cuatro sitios donde el instalador copia no llenaban los huecos.** Solo el del `CLAUDE.md` pasaba el texto por `_rellenar()`; el del stack, el de la memoria y el de los cuatro archivos de `.agente/` escribían la plantilla cruda. Así, `«RUTA-ESTANDAR»` llegaba intacto al proyecto y la cita a la regla no abría. Lo reportó `shopnest-mesa`, mirando el enlace a [`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) de su `.agente/stack-instalacion.md`.

Es la deuda que dejó cerrar la [20.0.1](#2001--2026-08-16) sin fase ni plan de pruebas — el caso que motivó [`02·F23`](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md). Esta vez sí hubo fase: [`A-EP-007-HU-001-rellenar-los-marcadores-al-copiar`](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/).

- **Los tres puntos de copia de [`validadores/instalar.py`](validadores/instalar.py) rellenan.** Se verificó que el sello no se ve afectado: la huella sale del stack central, no del texto copiado.
- **Nace la primera prueba del repositorio**, [`validadores/tests/test_instalar_marcadores.py`](validadores/tests/test_instalar_marcadores.py). Se corre con `python -m unittest discover -s validadores/tests` y usa la biblioteca estándar: sin internet y sin instalar nada.
- **Qué comprueba, y qué no.** Solo los marcadores que `_rellenos()` sabe llenar. Los otros huecos —a qué se dedica el negocio, quién usa el sistema— llegan vacíos **a propósito**: los contesta el proyecto, y borrarlos sería inventar la respuesta.
- **Se comprobó que la prueba no es vacía:** con el defecto reintroducido se pone roja y nombra cada marcador.

**Qué hacer para quedar al día:** los proyectos **nuevos** nacen bien desde ya. Los que ya estaban instalados **no se arreglan reinstalando**, y son dos motivos distintos:

- Los cuatro archivos de `.agente/` no se pisan una vez creados, porque los llena el proyecto.
- El `stack-instalacion.md` sí se pisaría, pero la huella se calcula del stack central y no del archivo copiado: como la plantilla no cambió, el instalador dice «ya estaba al día» y no reescribe. Lo comprobó `shopnest-mesa` el mismo día, y quedó como [pendiente 42](pendientes/hecho/el-arreglo-del-40-no-llegaba-a-lo-ya-instalado.md).

Mientras el 42 no cierre, un proyecto viejo se repara a mano: reemplazar `«RUTA-ESTANDAR»` por la ruta del estándar, o borrar el archivo y reinstalar si todavía nadie lo había llenado.

## 21.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (cambia por dónde entra al trabajo lo que dice el backlog).

**Un pendiente se estaba ejecutando como si fuera un plan.** El backlog dice qué falta y por qué, y eso se leía como permiso para editar directo: se cambiaba el código, se subía la versión y se marcaba hecho. Sin fase no hay plan de pruebas, y sin plan de pruebas nadie escribe qué había que comprobar. Se vio el mismo día en la [20.0.1](#2001--2026-08-16): los enlaces de las plantillas se arreglaron sin fase, y la única prueba que importaba —instalar en un proyecto y hacer clic— no la corrió nadie. El defecto salió del proyecto que lo sufrió, no del estándar que lo produjo.

- **[`02·F23`](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)**: el pendiente se baja a historia de usuario de su épica y se construye como fase de esa historia. El archivo del backlog no es el plan.
- **Extiende a [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)**, y hereda su excepción: el pendiente que solo pide decidir algo o leer no es desarrollo y no abre fase.
- **Dos procedimientos decían lo contrario y quedan corregidos.** Los nueve pasos de [`20 · base.md`](base/20-meta-reglas/base.md) y el §2 del [`CLAUDE.md`](CLAUDE.md) del estándar describían cambiar una regla como *buscar → enrutar → escribir → versionar*. Eso sigue siendo cómo queda **escrita** la regla; no reemplaza la cadena.
- **Validable, falta el validador**, y así queda en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): un programa puede comprobar que el pendiente cerrado nombre su HU y su fase, pero antes hay que fijar dónde se escribe esa referencia.

**Qué hacer para quedar al día:** el pendiente que ya esté en curso se termina como venía; el siguiente que se abra entra por su HU. Lo cerrado no se reabre — salvo lo que quedó sin probar, que se retrodocumenta con su fase.

## 20.0.1 — 2026-08-16

**PARCHE** — arregla enlaces que nacían rotos. No cambia qué se exige.

**Cada proyecto nacía con las citas a las reglas rotas.** Las plantillas citan sus reglas con enlace, como pide [`20·M15`](base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md), y el destino era relativo: `../base/…`. Dentro de este repositorio abre. Pero la plantilla no se queda acá: el instalador la copia dentro de un proyecto, y allá `../base/` es la carpeta que está **encima** del proyecto — nunca el estándar. Lo reportó `shopnest-mesa`, donde `hook_md.py` quedaba siempre en rojo por catorce enlaces muertos; un aviso que siempre suena se deja de leer, y por eso se perdieron fallas reales durante media sesión.

- **Los 91 enlaces de las 22 plantillas pasan a `«RUTA-ESTANDAR»/base/…`.** El marcador ya existía y lo resuelve [`instalar.py · _rellenos()`](validadores/instalar.py) contra la carpeta donde corre el estándar. No está escrito a mano en ningún lado: si el estándar se muda, basta reinstalar desde la carpeta nueva.
- **[`validadores/enlaces.py`](validadores/enlaces.py) aprende el marcador.** Sin esto el arreglo rompía la comprobación acá: 87 enlaces daban por rotos porque el marcador solo se llena al instalar. Ahora, sin llenar, se resuelve contra la raíz del repositorio.
- **El límite:** la ruta que entra al archivo es la de la máquina donde se instaló, y los documentos generados sí se versionan. En otra máquina ese enlace no abre. No empeora nada —hoy no abre en ninguna—, pero tampoco lo resuelve del todo.

**Qué hacer para quedar al día:** volver a correr la instalación, y los enlaces quedan apuntando al estándar de esta máquina.

## 20.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (cambia cómo se entrega todo lo que el agente escribe).

**Explicar más largo no es explicar mejor.** El usuario lo cortó otra vez con dos palabras —*"menos es más"*— después de un reporte de cinco bloques y tres listas. [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) ya pedía que el texto se entienda sin saber del tema, pero eso no alcanza: un texto puede entenderse perfecto y no leerse por largo, y lo que no se lee no comunicó nada.

- **[`00·ID9`](base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)**: se entrega en la menor extensión con la que se entienda — la conclusión primero, y nada que no cambie lo que el lector va a decidir o a hacer.
- **Qué se recorta y qué no.** Sobra el repaso de lo ya dicho, la justificación que nadie pidió y el recuento paso a paso. El dato exacto nunca. Lo que no cabe corto va al archivo del repositorio que le corresponde, y en el mensaje queda su enlace.
- **Extiende a `ID7`, no la repite.** Aquella se ocupa de que se entienda; esta, de que se lea.
- **No es validable**, y así queda registrado en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): contar renglones es fácil, pero decidir cuál sobra exige entender qué cambia la decisión del que lee.

**Qué hacer para quedar al día:** nada en los archivos del proyecto; cambia cómo se escribe de acá en adelante.

## 19.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (todo proyecto con una derogación sin adoptar tiene que ponerse al día antes de su próxima fase).

**Derogar una regla no llegaba a los proyectos.** El estándar es central, así que al derogar una regla todo proyecto deja de leerla ese mismo día — pero ninguno se pone al día solo: cada uno declara su versión en su `CLAUDE.md` y ahí se queda. [`validadores/version.py`](validadores/version.py) reportaba ese desfase como **aviso**, sin límite escrito de hasta cuándo se podía sostener. Un proyecto podía quedarse tres versiones atrás para siempre y ningún reporte lo llamaba incumplimiento.

- **[`02·F22`](base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)**: ninguna fase se abre ni se cierra mientras el proyecto declare una versión anterior a la que derogó una regla que ese proyecto cumplía.
- **Adoptar no es cambiar el número.** Lo único que se abre es la fase que adopta la derogación, una por cada HU que implementaba la regla derogada ([`02·F12`](base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)); ahí se aplica la regla que la reemplazó, y al cerrarla se sube la versión declarada. Sin eso, subir el número deja el trabajo viejo tal como estaba y la regla nueva sin aplicar.
- **El amarre es la fase, no la sesión.** Abrir y cerrar una fase ya son momentos donde alguien revisa y firma, así que la comprobación se cuelga de una parada que ya existe en vez de inventar otra. Fuera de esos dos momentos el desfase se reporta pero no detiene nada: un proyecto que solo hace el trabajo que [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) exceptúa queda marcado, no bloqueado.
- **Dos textos decían lo contrario y se corrigieron:** la nota de retroactividad de [`base/20-meta-reglas/base.md`](base/20-meta-reglas/base.md) y [`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md), que daban el desfase de versión como informativo siempre.
- **Ya la comprueba un programa.** [`version.py`](validadores/version.py) suma `derogaciones()`, `sin_adoptar()` y `validar_fase()`, y [`flujo.py`](validadores/flujo.py) —el que recorre las fases— la cobra donde hay fases. Las reglas jubiladas se leen de la marca `[DEROGADA en X.Y.Z → ver ID]` del título de cada regla, que es dato exacto; el `CHANGELOG.md` es prosa y nombrar ahí la palabra "derogación" no jubila nada. Queda un filtro fino sin hacer, anotado en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): si la regla derogada era una `*opt-in*` que el proyecto nunca encendió, hoy igual se le cuenta.

**Qué hacer para quedar al día:** mirar si entre la versión declarada y la vigente hay alguna derogación; si la hay, abrir una fase por cada HU que implementaba la regla derogada, aplicar ahí la regla que la reemplazó, y al cerrarla subir la versión declarada en el `CLAUDE.md` del proyecto.

## 18.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (cambia el nombre de una plantilla y de una ruta del proyecto).

**"Brief" se dice planteamiento.** La palabra estaba en inglés y nombraba el largo del documento, no su contenido: traducida literal queda "breve", que no dice nada de lo que hay que entender. El usuario lo destapó con un caso: alguien lee *"el brief responde qué se necesita y qué no se negocia"*, no sabe qué es, va al glosario y lo que encuentra no lo saca del apuro.

- **`plantillas/brief.md` pasa a [`plantillas/planteamiento.md`](plantillas/planteamiento.md)**, y el `brief.md` de la raíz a [`planteamiento.md`](planteamiento.md).
- **La ruta del proyecto pasa de `prompts/<slug>-brief.md` a `prompts/<slug>-planteamiento.md`.**
- **La palabra cambia en la zona normativa**: `base/`, `plantillas/`, `skills/`, `anatomia/` y el validador de plantillas. 30 ocurrencias.
- **Los enlaces que apuntaban al archivo viejo se corrigieron en todo el repositorio**, incluidos los de fases ya cerradas: un enlace roto no le sirve a nadie. El texto de esos registros no se tocó.

**Qué hacer para quedar al día:** renombrar `prompts/<slug>-brief.md` a `prompts/<slug>-planteamiento.md`.

**Lo que queda pendiente:** la palabra sigue escrita en `documentacion/`, `pendientes/`, `analisis/` e `historico-chat/`, que son registros de otras sesiones y de fases cerradas.

## 17.0.2 — 2026-08-16

**PARCHE** (redacción; no cambia qué se exige).

**Un glosario es un mini diccionario, y varias entradas no lo eran.** Lo destapó el usuario con un caso: alguien lee *"el brief responde qué se necesita y qué no se negocia"*, no sabe qué es un brief, va al glosario y encuentra *"el primer papel"*. No se entiende, y entonces el glosario no sirvió para lo que existe.

- **La prueba que ahora pasan las 72 entradas:** reemplazar la palabra por su definición y que la frase siga teniendo sentido. *"El **documento donde se escribe qué se necesita, antes de que exista una solución** responde qué se necesita y qué no se negocia."*
- **Cada definición empieza diciendo qué clase de cosa es** —el documento, la lista, la acción, el conjunto, el apunte— y sigue con qué hace. Antes 48 de 72 arrancaban en el aire: *"el primer papel"*, *"qué se va a hacer"*, *"lo que se escribe"*.
- **Ninguna pasa de 115 caracteres.**
- **Se quitó el anuncio del idioma, no la explicación.** *"En inglés quiere decir breve"* empieza informando algo que ya se ve: que la palabra está en inglés. Se recortó ese arranque en seis entradas y quedó solo lo que explica el nombre. Donde el idioma no es obvio se conserva: *postmortem* en latín, *meta* como "sobre", *retro* como "hacia atrás", y el inglés *hook* detrás de enganche.

La definición de **brief** es literal del usuario y no se toca.

## 17.0.1 — 2026-08-16

**PARCHE** (redacción; no cambia qué se exige).

**La columna "Qué quiere decir el nombre" estaba escrita en español de ninguna parte.** [`00·ID8`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) lo nombra en su sección 5: el español neutro, del que nadie reconoce de dónde es, delata que lo armó una máquina. Las 27 celdas llenas de [`base/glosario.md`](base/glosario.md) se reescribieron como se habla acá.

- *"Lo que se halla trabajando"* pasa a *"lo que uno se encuentra trabajando, sin andarlo buscando"*.
- *"Como la señal de una carretera"* pasa a *"como una señal de tránsito"*.
- *"Línea de montaje"* pasa a *"línea de ensamble"*; *"antes de salir"*, a *"antes de arrancar"*.
- *"Blindada contra cambios"*, que repetía la palabra, pasa a *"como un carro blindado: por más que le den, no cede"*.
- Se quitaron las comillas de las traducciones: *"En inglés, «pila»"* pasa a *"en inglés quiere decir pila"*.

## 17.0.0 — 2026-08-16

**MAYOR** ⚠ obliga a migrar (todo proyecto al día tiene que escribir su glosario).

**Las palabras del negocio no estaban definidas en ninguna parte.** El estándar ya tiene su glosario desde la 15.3.0, pero eso define las palabras del estándar. Las del negocio de cada proyecto —cómo se llama acá un cliente, qué cuenta como pedido, qué es un cierre— seguían en la cabeza de quien las usaba, y dos documentos del mismo proyecto podían llamarle distinto a la misma cosa sin que nadie lo notara.

- **[`13·DOC23`](base/13-documentacion/reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md)**: todo proyecto mantiene el glosario de sus términos, cada uno en una línea entendible por quien no conoce el dominio, actualizado en el mismo cambio que introduce el término.
- **La sección Glosario de [`plantillas/dominio.md`](plantillas/dominio.md)** deja de ser un espacio en blanco y dice qué entra, qué no, y cuándo se actualiza. Existía desde antes; lo que faltaba era la regla que obligara a llenarla.
- **Qué entra y qué no.** La palabra que el negocio ya trae va acá. El concepto de la base que en este proyecto se llama de otro modo va en `mapeo-nombres.md`, que sigue siendo otra cosa.
- **Validable a medias**, y así queda registrado: un programa puede ver si el glosario existe y si tiene entradas; si la definición se entiende, no.

**Qué hacer para quedar al día:** llenar la sección Glosario de `dominio.md` con las palabras del negocio que ya usan las especificaciones del proyecto.

## 16.0.0 — 2026-08-15

**MAYOR** ⚠ obliga a migrar (un plan de pruebas en curso con pasos de dos acciones hay que partirlo).

**Un paso de dos acciones pierde la mitad de lo que salió.** El plan de una fase decía *«tomar la lista de origen **y** contar cuántos términos tiene»* en una sola fila, con un solo renglón de resultado esperado. Al ejecutar quedó anotado el conteo y se perdió de dónde había salido la lista, que era lo que había que comprobar. El caso quedó en "aprobado" con la mitad sin registro, y eso no se vio hasta bajar el resultado a la forma nueva de [`plantillas/planes/resultados.md`](plantillas/planes/resultados.md).

- **[`plantillas/planes/pruebas.md`](plantillas/planes/pruebas.md)** §6: **un paso, una acción**. Cada fila lleva un solo verbo y un solo resultado esperado, con su ejemplo INCORRECTO/CORRECTO.
- **Se aplicó al plan que lo destapó**, [la fase A de EP-003 · HU-010](documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/plan_pruebas.md), versión 1.1: seis pasos partidos o reescritos en CP-001, CP-002, CP-004, CP-005, CP-007 y CP-008. Ningún caso cambia lo que comprueba.
- **El resultado de esa fase pasa de «aprobada con una prueba pendiente» a «No cumple».** No es un cambio de criterio: la plantilla no admite estado intermedio y `RNF-01` no tiene caso ejecutado. Con los pasos partidos se ve además que 15 de los 33 no dejaron registro de qué salió.
- **La regla «se arranca desde cero» destapó dos pasos dados por supuestos** en el mismo plan (versión 1.2): CP-004 no decía cómo se eligen las tres entradas de muestra, y CP-006 no decía que hay que conseguir a alguien que no haya escrito el glosario — que era justo lo que tenía el caso bloqueado, sin que apareciera en ninguna fila.
- **La sección 2 de [`plantillas/planes/resultados.md`](plantillas/planes/resultados.md) pedía lo mismo dos veces** —un bloque por pareja `CA`–`CP` arriba y un «Detalle de `CP-00N`» abajo—, y quien leyera no sabía cuál mandaba. Queda un solo bloque, con sus tres partes y **cuatro reglas que dicen qué es "detallado"**: un paso por cada fila del plan, se arranca desde cero, ningún paso queda vacío, y está detallado cuando alguien que no estuvo puede repetir la prueba sin preguntar nada.

## 15.4.3 — 2026-08-15

**PARCHE** (se documenta y se prueba algo que ya corría; nadie tiene que hacer nada nuevo).

**El reparto de las reglas al abrir la sesión no estaba escrito en ninguna parte, y nadie lo probaba.** [`validadores/cargador.py`](validadores/cargador.py) manda completos los capítulos que empiezan por `00-` y `01-` y del resto manda el índice, desde la versión 5.0.0. Esa decisión solo vivía en un comentario del programa: una línea cambiada dejaba al agente sin identidad y nada avisaba.

- **[`documentacion/automatismos/spec.md`](documentacion/automatismos/spec.md)** gana la sección 4.1 con siete reglas de negocio: qué llega completo, qué llega en índice, por qué se decide por la ruta y no por el nombre del archivo, qué pasa cuando el arranque está detenido y por qué no se puede cargar todo.
- **Diez pruebas nuevas** en la clase `RepartoDeLasReglas`, y se comprobó que cazan el defecto: con el reparto roto a propósito, el capítulo de conducta deja de llegar y la prueba lo detecta.
- **Medido y escrito:** 73 KB de 369 KB, y 0,21 s el enganche que los entrega.
- **El [pendiente 25](pendientes/hecho/las-reglas-de-como-se-escribe-si-llegaban-puestas.md) se cierra por falso.** Decía que `ID8` se incumplió porque llegaba como línea de índice; llegaba completa. La causa se había deducido en vez de verificarse, y esa es la parte que no se puede repetir.

## 15.4.2 — 2026-08-15

**PARCHE** (deja escrita la pregunta que la sección ya venía respondiendo; no exige nada nuevo).

**La sección de identificación no decía qué se responde ahí.** Arrancaba directo en la tabla, así que se llenaba como un trámite. Ahora abre con su pregunta: **¿qué se está probando?**

- **[`plantillas/planes/resultados.md`](plantillas/planes/resultados.md)**: una línea al abrir la sección 0.
- **«Corrida» pasa a «ejecución»** en esa plantilla, y la sección 1 dice qué es: correr las pruebas de principio a fin. «Corrida» era jerga y no estaba en el [glosario](base/glosario.md) como término propio.
- **Las secciones 1 y 2 también abren con su pregunta**, y la 2 pide explicar qué problema resuelve cada pareja `CA`–`CP`, con su ejemplo: el problema, las condiciones, los pasos con lo que salió, y cómo se verificó que la pareja cumple.

## 15.4.1 — 2026-08-15

**PARCHE** (le da forma a lo que pidió la 15.4.0; no exige nada nuevo).

**El detalle de un caso quedó en tres partes, no en cinco.** Al aplicarlo a los diecisiete casos de una fase se vio que dos sobraban: los pasos esperados y los que se siguieron son los mismos pasos, así que van en una sola tabla de tres columnas —qué hacer, qué tiene que pasar y qué salió—, y el desvío se lee en la fila. El veredicto tampoco se repite en el detalle: ya vive en la tabla de casos ejecutados.

- **[`plantillas/planes/resultados.md`](plantillas/planes/resultados.md)**: las tres partes, con el ejemplo en esa forma.

## 15.4.0 — 2026-08-14

**MENOR** (el instalador deja una carpeta más; nadie tiene que hacer nada nuevo).

**El enganche que sostenía el resumen de la sesión no creaba el resumen.** La fase que lo construyó cerró el mismo día con sus tres criterios en "cumple", y el programa no hacía lo que esos criterios piden: los dos resúmenes que había en el repositorio los había escrito el agente a mano. Se reabrió la fase [`A-EP-005-HU-008`](documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md) en vez de abrir una nueva: lo que fallaba era ese trabajo, y su documentación decía que estaba hecho.

- **El archivo nace en el primer mensaje de la sesión, no al abrir.** Al abrir, la transcripción todavía no existe, y de su nombre sale el del resumen. Los dos modos del enganche lo aseguran: la sesión que se retoma lo tiene desde el arranque y la nueva en el primer turno.
- **`instalar.py` deja puesta `historico-chat/resumenes/` con su índice.** Sin ella el enganche quedaba mudo en todo proyecto que hereda el estándar, y crearla era un paso a mano que nadie había documentado.
- **El encabezado del resumen ya no enlaza `plantillas/sesion.md`.** Esa carpeta es del estándar y no viaja al proyecto: ahí el enlace nacía roto. Enlaza el índice del histórico, que el instalador sí deja en todos.
- **La corrida 2 de las pruebas dispara el enganche como orden del sistema**, con el JSON que le manda Claude Code, sobre un proyecto que arma el instalador. Ninguna precondición se monta a mano: eso fue lo que dejó pasar el defecto. La fase no se declara cumplida hasta que el archivo aparezca solo en una sesión real.
- **[`plantillas/planes/resultados.md`](plantillas/planes/resultados.md)**: el detalle de un caso pasa a tener cinco partes fijas — el problema que resuelve, la precondición, qué hacer para que cumpla, con qué reprueba y los pasos que se siguieron de verdad. Con el detalle a medias un caso puede pasar habiendo probado otra cosa, y eso fue lo que pasó. Queda escrito que si lo ejecutado no son los pasos de "para que cumpla", el caso no cumple, aunque haya salido bien.

## 15.4.0 — 2026-08-15  ·  ⚠ **número repetido**

> **Este número está usado dos veces**, y la de arriba es del día anterior. Lo dejaron dos sesiones abiertas a la vez sobre el mismo repositorio, que es lo que describe el [pendiente 22](pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).
>
> **No se renumera a propósito.** Un proyecto pudo haber adoptado «15.4.0», y cambiarle el número ahora le movería el piso sin que se entere. Queda marcado, que es lo honesto: quien adoptó esa versión tiene **las dos cosas**, la de arriba y esta.
>
> Desde la v23.11.0 esto no puede volver a pasar sin que se diga: `validar.py versionado` lo reporta.

**MENOR** (una sección más en una plantilla; ningún brief ya escrito deja de valer).

**El brief no decía cómo se llama el proyecto.** La plantilla tenía el nombre solo en el título, y ese título nombra el módulo o la épica. Un proyecto entero no tenía dónde decir cómo se llama, y el nombre es lo primero que heredan todos los documentos que salen de ahí.

- **Sección 0, Identificación**, en [`plantillas/planteamiento.md`](plantillas/planteamiento.md): nombre del proyecto, qué cubre el encargo y fecha.
- El [`planteamiento.md`](planteamiento.md) de este repositorio la estrena: el proyecto se llama **Cimiento**.

## 15.3.0 — 2026-08-14

**MENOR** (nace un documento de consulta; nadie queda obligado a nada nuevo).

**Las reglas usaban palabras que no estaban definidas en ningún lado.** Para saber qué es una especificación había que encontrar la regla que la exige; para saber qué es una señal, otra; para saber qué es una fase, un capítulo entero. El caso que lo destapó: el usuario preguntó qué significaba "spec", y la respuesta tomó tres intentos y terminó cambiando una regla.

- **[`base/glosario.md`](base/glosario.md)**: 72 términos en cuatro grupos (la cadena de trabajo, las reglas, lo que comprueba y lo que se guarda). Cada uno en una línea, con quién lo escribe, dónde vive y qué regla lo manda. Es un anexo, no una regla: no exige nada y por eso no lleva checklist.
- **Una columna dice qué quiere decir el nombre**, no solo qué es la cosa: por qué a una fase le decimos estación, de dónde sale bitácora, qué significa brief. Sin eso, un término se puede leer y seguir sin entender por qué se llama así.
- **Cada entrada enlaza a su regla y no copia su texto.** Dos copias de la misma norma se desincronizan, y manda la que nadie relee.
- **Se alcanza desde las tres puertas de entrada**: [`README.md`](README.md), [`base/README.md`](base/README.md) y [`anatomia/mapa-del-sitio.md`](anatomia/mapa-del-sitio.md).
- **Queda el inventario de lo que sigue en otro idioma**: 10 términos que se quedan con su motivo escrito y 12 que faltan traducir, con el archivo donde vive cada uno. Renombrarlos es trabajo aparte, porque rompe las citas.

Cierra la parte del glosario del [pendiente 21](pendientes/hecho/los-nombres-de-rol-en-espanol.md), que nace del hallazgo H-8 del 2026-08-14. La parte de los roles queda abierta.

## 15.2.0 — 2026-08-14

**MENOR** (una columna más en una plantilla; no invalida los resultados ya escritos).

**Un caso de prueba aprobado no decía con qué se probó.** El plan dice qué **tipo** de dato usar; el resultado decía solo "aprobado". Con eso nadie puede repetir la prueba, y un caso que no se puede repetir no es una prueba: es un recuerdo.

- **Columna nueva `Con qué se probó`** en [`plantillas/planes/resultados.md`](plantillas/planes/resultados.md), con el ejemplo real: el archivo, el valor o el comando que se corrió.
- Su ejemplo lo deja claro: no vale *"un usuario sin permiso"*, vale *"`qa.consulta` sobre `/facturas/42/anular`"*.

## 15.1.0 — 2026-08-14

**MENOR** (dos enganches nuevos; nadie queda obligado a nada que no estuviera ya exigido).

**El resumen de la sesión dependía de que alguien se acordara.** Desde la 14.0.0 [`13·DOC22`](base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) lo exige, el modelo existe y el índice lo enlaza. Faltaba el programa. Es la misma lección de la transcripción, que solo empezó a escribirse siempre cuando la escribió un programa.

- **[`validadores/resumen.py`](validadores/resumen.py) y [`validadores/hook_resumen.py`](validadores/hook_resumen.py)**: el archivo se crea al abrir la sesión, con el modelo puesto y sin hallazgos.
- **Avisa qué falta**, una vez por cada cosa y máximo dos: que no haya ningún hallazgo, y que nadie haya dicho si la sesión se puede cerrar. La marca del aviso vive dentro del propio resumen.
- **Muestra lo que sigue abierto del propósito** que la sesión declara, y nada de otros temas. Una sesión abierta para un tema no tiene por qué ver los hallazgos de otro: eso es ruido, y el ruido se deja de leer.
- **El resumen se mueve con la transcripción** al ponerle el tema a la sesión. Los dos se llaman igual, así que renombrar solo uno dejaba el índice apuntando a un archivo que no está.
- **Lo que el enganche no hace:** escribir hallazgos ni interpretarlos. Reconocer uno es criterio, y el criterio no lo tiene un programa. Lo que sí puede es que el hueco se vea.

**Qué tiene que hacer un proyecto al día.** Correr el instalador para recibir los dos enganches. Un proyecto sin carpeta de resúmenes no se ve afectado.

## 15.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (una regla nueva que exige algo a todo proyecto al día).

**Un pendiente se estaba usando como permiso.** El repositorio tenía anotado que 354 enlaces no cumplen [`13·DOC14`](base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), y los documentos escritos ese mismo día sumaban 122 incumplimientos nuevos de la misma familia. La deuda dejaba de ser deuda y pasaba a ser costumbre.

- **[`02·F21`](base/02-flujo-de-trabajo/reglas/F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md)**: desde que un incumplimiento queda registrado en un pendiente, un hallazgo o una señal, lo que se escriba de ahí en adelante nace cumpliendo. El pendiente guarda lo viejo y se limpia aparte; no autoriza a producir más.
- El usuario lo dijo así: *"yo antes escribía sin ortografía, pero a partir de que aprendí ya escribo con ortografía, no importa el contexto"*.

**Qué tiene que hacer un proyecto al día.** Nada hacia atrás: sus pendientes siguen como están. Lo que cambia es de aquí en adelante, y el costo de cumplirla es cero cuando el incumplimiento ya se conoce.

## 14.0.1 — 2026-08-14

**PARCHE** (enlaces; no cambia qué se exige).

**Las plantillas citaban reglas por su ID y sin enlace**, contra [`20·M15`](base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md), que exige que toda cita lleve el enlace al sitio donde vive la regla. Peor: muchas citaban sin el prefijo del capítulo —`F4`, `DOC5`, `C19`—, y así ni siquiera se sabía dónde buscar.

- **122 citas enlazadas en 23 plantillas**, cada una con su capítulo y su ruta.
- **El modelo del resumen de sesión lo deja escrito**: toda regla que se nombre va enlazada, en cualquier campo del hallazgo.

## 14.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (una regla nueva que exige algo a todo proyecto al día).

**Lo que una sesión dejaba se perdía dentro de su propia transcripción.** La transcripción prueba lo que se dijo, y por eso es larga: nadie la relee. Una sesión produjo cinco aprendizajes y nueve pendientes que hubo que ir a rescatar leyendo el chat. El molde para escribir lo que quedó existía desde la 12.2.0, pero nada lo exigía y nada lo enlazaba, así que dependía de que alguien se acordara.

- **[`13·DOC22`](base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)**: cada sesión deja su resumen en un documento aparte, escrito **en el momento en que aparece cada hallazgo**, no al cerrar. Un chat no tiene final, y lo que se deja para el final no se escribe.
- **El resumen se encuentra desde donde se busca.** El índice del histórico enlaza, en la misma línea de cada sesión, su transcripción y su resumen. [`validadores/historico.py`](validadores/historico.py) escribe ese enlace al ponerle nombre a la sesión, y solo si el resumen ya existe: un enlace roto en el índice es peor que no tenerlo.
- **Un hallazgo se nombra `AAAA-MM-DD · tema · H-N`.** Cada resumen numera los suyos desde `H-1`, así que el número solo no identifica nada. La numeración corrida entre sesiones se descartó: obligaría a un contador único, y dos sesiones abiertas a la vez lo rompen, que es justo lo que ya pasó con la versión.
- **El hallazgo que se hereda no se copia.** La sesión que retoma uno abierto lo nombra en su «viene de» y trabaja sobre el original. Dos copias del mismo hallazgo terminan diciendo cosas distintas, y manda la que nadie está mirando.
- **Cuál de los dos documentos abrir** queda escrito en [`historico-chat/resumenes/README.md`](historico-chat/resumenes/README.md): se arranca siempre por el resumen, y la transcripción se abre cuando el resumen no alcanza.
- **Toda regla que el resumen nombre va enlazada.** [`20·M15`](base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) ya lo exigía y el modelo no lo decía, así que los resúmenes citaban por ID y quien los leía tenía que salir a buscar.

**Qué tiene que hacer un proyecto al día.** Correr el instalador para recibir el modelo, y crear la carpeta de resúmenes la primera vez que la use. Lo ya escrito no se rehace y una sesión vieja sin resumen no se reabre: la norma aplica al trabajo en curso y al que viene.

## 13.1.0 — 2026-08-14

**MENOR** (dos precisiones en tres plantillas; no invalida nada escrito).

**Un veredicto de pruebas que decía "cumple con observaciones" no dice nada.** Si el carro vuelve del taller sin frenos, no está arreglado: "cumple con observaciones" era la forma amable de decir que no cumple, y quien lo lee después no sabe si podía cerrar la fase o no.

- **Los requisitos no funcionales de una HU van numerados `RNF-0N`** en [`plantillas/HU.md`](plantillas/HU.md), igual que los criterios de aceptación. Sin número no se pueden citar desde el plan ni desde las pruebas, y terminaban verificándose de vista.
- **Y cuentan como exigencia propia.** En [`plantillas/planes/pruebas.md`](plantillas/planes/pruebas.md) y [`plantillas/planes/resultados.md`](plantillas/planes/resultados.md) cada `RNF-0N` lleva su fila en la matriz y en el veredicto, y la cobertura suma criterios y requisitos por separado. En la fase donde salió esto, tres requisitos venían contados como uno solo: la cobertura decía 4 de 4 cuando era 6 de 6.
- **El veredicto pasa a ser binario** en [`plantillas/planes/resultados.md`](plantillas/planes/resultados.md) y en [`plantillas/estado-fase.md`](plantillas/estado-fase.md): cumple o no cumple. Lo que falte hace que sea no cumple. Los defectos ya tienen su tabla, con severidad y con quién los aceptó.
- **Cada `CP-00N` se escribe como enlace a su caso, y cada `CA-0N` o `RNF-0N` como enlace a su exigencia en la HU**, en el plan de trabajo, el plan de pruebas, el resultado y el documento de cierre. Un identificador suelto obliga a buscarlo a mano, y así es como se termina juzgando un caso sin haber leído lo que exigía. Salió de una fase real: el caso decía "los que se declaró" sin decir dónde, y quien ejecutaba acababa decidiendo la lista.

## 13.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (tres reglas nuevas que exigen algo a todo proyecto al día).

**Los huecos de un modelo se marcaban de tres formas distintas, y ninguna estaba escrita.** Al contarlo archivo por archivo: 25 de 30 plantillas usaban `«…»`, once convivían con `[texto]` y dos con `<texto>`. La convención se cumplía porque alguien se acordaba, no porque estuviera en ninguna regla. Un documento entregado a medias dejaba sus huecos confundidos con el texto, y nadie los veía al aprobarlo.

- **[`13·DOC19`](base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md)**: los espacios por llenar se marcan `«…»`, la misma marca en todos los modelos. Deja escrito además qué **no** es un hueco: la sintaxis de un comando que se copia y se pega la llena quien lo corre.
- **[`13·DOC20`](base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md)**: un documento que conserva una sola marca no está terminado, y no se presenta como tal.
- **[`13·DOC21`](base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md)**: la sección que no aplica se escribe `N/A`. Dejarla marcada la vuelve un hueco; borrarla hace creer que el modelo nunca la pidió.
- **179 huecos convertidos** en 13 plantillas, sin tocar enlaces, casillas ni bloques de guía. Tres archivos de `plantillas/` quedaron sin marca a propósito: `historico-chat.md`, `memoria.md` y `retrodocumentacion.md` no son modelos que alguien llene, y así queda escrito.
- **Por qué esa marca y no otra**, con las cuatro descartadas y el motivo de cada una: [`notas/marca-del-espacio-por-llenar.md`](notas/marca-del-espacio-por-llenar.md).

**Qué tiene que hacer un proyecto al día.** Correr el instalador para recibir las plantillas nuevas. Los documentos que ya llenó no se tocan: un documento terminado no es un modelo.

## 12.4.0 — 2026-08-14

**MENOR** (precisa un campo que ya existía; no invalida los resúmenes ya escritos).

**Un problema partido en dos historias no dejaba ver cuál va primero.** Las épicas están cortadas por tipo de entregable: el documento modelo cae en una y el programa que lo llena, en otra. Un hallazgo que dispara las dos queda repartido, y entrando por cualquiera de las dos épicas el orden no se ve. Pasó con el resumen de sesión: su modelo es de EP-003 y su enganche de EP-005, y hubo que deducir a mano que el enganche va después porque escribe el archivo con el modelo adentro.

- **El campo `Dispara` de [`plantillas/sesion.md`](plantillas/sesion.md) numera las historias** en el orden en que se resuelven, y cada una dice por qué va ahí.
- **También nombra lo que las bloquea aunque el hallazgo no lo haya disparado.** Una historia vieja en backlog puede estar deteniendo a una nueva, y eso solo se ve desde acá.
- **Por qué en el hallazgo y no en la épica:** el hallazgo es el único sitio donde el problema está entero. Recortar las épicas por problema costaría rehacer las 54 historias ya colgadas.

## 12.3.0 — 2026-08-14

**MENOR** (aditivo: un campo nuevo en una plantilla; no invalida los resúmenes ya escritos).

**Una sesión que va a resolver un hallazgo no decía cuál.** El resumen de sesión guardaba de dónde nace cada hallazgo y dónde se cierra, pero no de dónde nace **la sesión**. Cuando alguien abre una sesión con un hallazgo en la mano ("trabajemos en H-4"), ese origen no quedaba escrito en ninguna parte: se perdía en la transcripción, que es justo lo que el resumen viene a evitar.

- **Campo nuevo `Viene de`** en [`plantillas/sesion.md`](plantillas/sesion.md), al principio del resumen: la fecha, el tema y el número del hallazgo que se fue a resolver, o `—` si es trabajo nuevo.
- **Es el enlace hacia adelante.** El de vuelta ya existía: el `cerrado en` del hallazgo apunta a la sesión que lo cerró. Con los dos, un hallazgo que se arrastra tres sesiones se sigue en cualquier dirección; con uno solo, no.
- Si la sesión atiende más de un hallazgo, se nombran todos.

## 12.2.0 — 2026-08-14

**MENOR** (aditivo: una plantilla nueva; no cambia nada de lo escrito).

**Lo que una sesión deja se quedaba en la transcripción.** Una sesión entera produjo cinco aprendizajes y nueve pendientes, y ninguno tenía dónde escribirse: había que releer la conversación para encontrarlos. La transcripción guarda **lo que se dijo**; faltaba el molde de **lo que quedó**.

- **Nueva plantilla [`plantillas/sesion.md`](plantillas/sesion.md)**: cuatro campos por hallazgo — qué pasó, por qué importa, qué se decidió y dónde queda.
- **No es un resumen de cierre.** Se llena en el momento en que aparece el hallazgo. Es la misma lección de la transcripción de sesiones: lo que se deja para el final no se escribe nunca, porque un chat no tiene final.
- **Cada hallazgo termina en uno de cuatro sitios**, y la plantilla lo dice: señal, pendiente, regla o memoria del usuario. Lo que no cabe en ninguno era conversación, y ya está en la transcripción.
- **Falta el enganche** que lo recuerde en el momento. Mientras dependa de que el agente se acuerde, se va a olvidar, y eso queda anotado como pendiente.

## 12.1.0 — 2026-08-14

**MENOR** (precisa el alcance de una regla que ya existía; no invalida nada escrito).

**"Responde corto" se cumplía en los reportes y no en las explicaciones.** [`01·C5`](base/01-conducta.md#c5--responde-corto) pedía respuestas cortas, y el agente las daba al reportar trabajo. Al explicar un concepto hacía lo contrario: párrafos, tablas y opciones para responder una pregunta de una línea. El usuario lo cortó tres veces en la misma sesión, la última con *"explicar algo no es extenderse en prosa y que no se entienda nada, explicar es poder decir algo en pocas palabras pero que se entienda"*.

- **`C5` dice ahora que la explicación también va corta**, y que si no cabe en dos o tres frases el asunto todavía no se entendió: se piensa más, no se escribe más.
- **Queda fijado qué significa "menos es más"** dicho por el usuario: lo anterior fue largo y no se entendió, y se responde otra vez más corto. Antes era una señal que el agente podía leer como un comentario de estilo.
- **El ejemplo es el de la sesión**: tres párrafos y una tabla para explicar qué es una especificación, contra una sola frase.
- La regla trae su bloque de checklist, que antes no tenía.

## 12.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (desde ahora, un comando rechazado no cancela lo que el usuario pidió: el agente corrige el comando y vuelve a intentar).

**Un rechazo se leía como "olvídelo todo".** El usuario aprobó un renombrado, rechazó el comando con que el agente iba a hacerlo, y el agente dio el encargo por cancelado y respondió con una explicación. Hubo que pedirlo tres veces. [`01·C1`](base/01-conducta.md#c1--avisa-antes-de-tocar) y [`01·C17`](base/01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación) dicen qué cuenta como **aprobación**; ninguna decía qué significa un **no** al comando, y el agente lo resolvió a su criterio, que es lo que las reglas existen para impedir.

- **Nace [`01·C22`](base/01-conducta.md#c22--ante-un-comando-rechazado-corrige-el-comando--la-orden-sigue-en-pie)**: lo que el usuario rechaza es **cómo** el agente iba a hacerlo, no lo que pidió. El agente corrige la llamada y reintenta, o pregunta en una línea qué cambiarle; la orden solo la retira el usuario, diciéndolo. Extiende `C17`.
- **Nace en `base/` y no en la memoria del agente.** Es conducta de cualquier agente, no preferencia de un usuario: `base/` es la línea de comportamiento y la memoria se construye encima ([`01·C19`](base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto), [`20·M13`](base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)). Escribirla en la memoria era conducta sin versionar.
- **Sin validador.** Lo que se exige pasa después del rechazo y no queda en ningún archivo ([`20·M9`](base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)). Queda anotada como no validable.
- **Retroactividad.** No reabre nada. Aplica a los rechazos que lleguen desde ahora.

## 11.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (desde ahora, el agente no arranca con un pedido al que le falte un dato: pregunta por ese dato y espera).

**El pedido incompleto se completaba adivinando.** [`01·C7`](base/01-conducta.md#c7--ante-dos-lecturas-pregunta) y [`01·C17`](base/01-conducta.md#c17--confirma-tu-entendimiento-antes-de-ejecutar--solo-palabra-afirmativa-del-usuario-cuenta-como-aprobación) cubrían el pedido que admite **dos lecturas**, pero no el que no trae el dato: *"arregle eso"* no tiene dos lecturas, no tiene ninguna. El agente deducía a qué apuntaba "eso" por el contexto, acertaba a veces, y el trabajo quedaba a medias o en el archivo equivocado.

- **Nace [`01·C21`](base/01-conducta.md#c21--pide-el-dato-que-falte-antes-de-arrancar)**: un pedido de trabajo declara **sobre qué**, **qué quiere**, **qué debe quedar hecho** y **qué no se toca**; el que solo pide información declara los dos primeros. Si falta alguno, el agente pregunta por ese y no toca nada mientras espera. Extiende `C7`.
- **[`plantillas/CLAUDE.md.plantilla`](plantillas/CLAUDE.md.plantilla) gana el punto 6**, con los cuatro campos y un ejemplo de cada uno. Llega solo a cada proyecto por [`01·C18`](base/01-conducta.md#c18--auto-sincronización-del-claudemd-con-la-plantilla-central), que es aditivo: nadie copia nada a mano.
- **Sin validador.** Lo que se exige pasa en el chat y ningún script lo lee ([`20·M9`](base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md)). Queda anotada como no validable.
- **Retroactividad.** No reabre nada. Aplica a los mensajes que lleguen desde ahora.

## 10.0.0 — 2026-08-14

**MAYOR** ⚠ obliga a migrar (desde ahora, el documento que use una palabra de otro idioma la traduce o la explica la primera vez).

**El estándar escribía en inglés y exigía escribir en español.** [`01·C8`](base/01-conducta.md#c8--habla-el-idioma-del-proyecto) manda que todo lo que ve el usuario vaya en el idioma del proyecto, y el propio estándar usaba "spec" en 53 archivos. Quien lee "falta la spec" no sabe qué documento le piden ni dónde ponerlo, que es justo lo que [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) vino a evitar.

- **Nace [`01·C20`](base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica)**: el término de otro idioma se traduce, y el que no tenga traducción usada se explica la primera vez que aparece. Extiende `C8`, que fijaba el idioma pero no decía qué hacer con las palabras que no lo tienen.
- **"spec" pasa a "especificación"** en el texto de `base/`, `plantillas/`, `validadores/` y `documentacion/`: 162 cambios. **Los nombres de archivo y las rutas no se tocan** — `spec.md`, `plantilla-especificacion-modulo.md` y el archivo de `F2` siguen igual, así que ningún proyecto tiene que renombrar nada. Fue decisión del usuario, para que el cambio no obligara a mover archivos.
- **Los identificadores no cambian.** `F2` sigue siendo `F2`; lo que cambió es su título, que ahora dice *"Sin especificación acordada no hay código"*.
- **Se anula el checklist de las reglas cuyo texto se tocó** ([`20·M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md)): `F2`, `F7`, `DOC3`, `DOC6`, `DOC11`, `DOC12`, `DOC13` y las cuatro `F4.x` derogadas. Cambió una palabra y no lo que exigen, pero las filas 8 a 11 se juzgan sobre el texto. Se vuelven a aplicar en la fase que las toque.
- **Retroactividad.** Un documento ya escrito y aceptado no se reabre para traducirle las palabras. Aplica a lo que se escriba desde ahora.

## 9.2.0 — 2026-08-14

**MENOR** (aditivo: una columna nueva en la tabla de deuda del cierre).

**La deuda se anotaba sin decir de dónde salía.** Se registraba qué quedó pendiente y a dónde se traslada, pero no por qué apareció. Y no todas las deudas dicen lo mismo: una que sale de no haber visto lo que se iba a romper señala que la línea base de [`02·F17`](base/02-flujo-de-trabajo/base.md) se hizo floja; una que se decidió por tiempo, o que la produjo el propio plan al diferir algo, no señala nada malo. Sin separarlas, no se puede saber si el análisis previo se está haciendo bien.

- **[`plantillas/funcionalidad-implementada.md`](plantillas/funcionalidad-implementada.md) §6 gana la columna `Origen`**, con cuatro valores: *no previsto*, *atajo decidido*, *cambio del entorno* y *diferido por el plan*. Cada uno con qué pasó y qué significa.
- **Para qué sirve.** Un análisis bueno no elimina la deuda: convierte la **descubierta** en **declarada**. Si fase tras fase se repite *"no previsto"*, el problema no es la deuda: es que la línea base se está haciendo por encima. Antes eso no se veía en ningún lado.
- **Retroactividad.** Las fases cerradas no se reabren para clasificar su deuda.

## 9.1.0 — 2026-08-14

**MENOR** (aditivo: una subsección nueva en el cierre y una en el estado de fase; el plan de trabajo pierde una columna y una sección que ya vivían mejor en otro lado).

**Nada verificaba que el plan de trabajo se hubiera cumplido.** El `resultado_pruebas` que trajo [`9.0.0`](#900--2026-08-13) comprueba que **el resultado sirve**. Pero que **se haya hecho lo que se dijo que se iba a hacer** no lo revisaba nadie: el avance se marcaba con una casilla dentro del propio plan, que es autorreporte y encima pisa el documento aprobado, y el `funcionalidad_implementada` trazaba solo contra la spec. Una fase podía pasar todas las pruebas y haber dejado tres tareas sin tocar, o haber tocado archivos que el plan no declaraba, sin que quedara rastro.

- **[`plantillas/funcionalidad-implementada.md`](plantillas/funcionalidad-implementada.md) §2 pasa a tener dos trazabilidades**, porque responden preguntas distintas: **§2.1 spec → implementación** (qué había que lograr) y **§2.2 plan de trabajo → ejecución** (qué se iba a hacer para lograrlo). La §2.2 va tarea por tarea, con su identificador copiado del plan, y suma dos cosas que antes no se preguntaban: las **tareas que no se hicieron** y los **archivos tocados que el plan no declaraba** ([`02·F8`](base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). "Ninguno" es la respuesta esperada; que quede escrito cuando no lo es permite ver si el plan se amplía sobre la marcha y por qué.
- **[`plantillas/planes/trabajo.md`](plantillas/planes/trabajo.md) pierde la columna `Estado` de §3 y el §13 de cierre.** Marcar avance ahí pisaba el plan aprobado y dejaba sin contra qué comparar, el mismo defecto que `9.0.0` corrigió en el plan de pruebas. El cierre ya vivía completo en el `funcionalidad_implementada`, duplicado.
- **[`plantillas/estado-fase.md`](plantillas/estado-fase.md) gana §1.2 · Avance de las tareas del plan**, que es donde va el seguimiento **en vivo** mientras la fase corre. Queda la cadena completa: el plan dice qué se va a hacer, el estado dice por dónde va, el cierre dice qué se hizo.
- **Retroactividad.** Las fases cerradas no se reabren. Los planes ya aprobados conservan su columna de estado; el cambio aplica a los que se escriban desde acá.

## 9.0.0 — 2026-08-13

**MAYOR** ⚠ obliga a migrar (toda fase que se abra desde ahora produce un quinto documento; el plan de pruebas deja de ser donde se anotan los resultados).

**El plan de pruebas se aprobaba antes y se sobreescribía después.** La plantilla traía la tabla de ejecución dentro de cada caso y el resumen de la corrida en §12: el mismo archivo que el usuario aprueba **antes** de probar terminaba pisado con lo que pasó **después**. Tres consecuencias: se pierde la línea base aprobada, así que no hay contra qué comparar lo que se acordó probar; no queda un veredicto formal de si la fase cumple; y el documento de cierre tenía que redactar de memoria la sección "qué se probó". Además la plantilla decía apoyarse en ISO/IEC/IEEE 29119-3, que separa el plan del registro de ejecución, y la nuestra los juntaba.

- **Nueva plantilla [`plantillas/planes/resultados.md`](plantillas/planes/resultados.md)**, el `resultado_pruebas.md` de la fase. Registra qué se ejecutó, con qué resultado, qué defectos salieron, y sobre todo el **veredicto por criterio de aceptación** y el **veredicto de la fase**. Se crea **junto con los dos planes**, no cuando se corre la primera prueba: el formato puesto desde el principio se ve, se revisa y no se olvida. Lo que no se ha corrido se escribe **"no ejecutado"**, nunca en blanco ni como aprobado, y el veredicto arranca en *"todavía no se ejecutó"*, que no es lo mismo que "no cumple". Los ciclos de reprueba se apilan sin pisar el anterior, porque saber que algo falló y después pasó vale más que ver solo el resultado final.
- **[`02·F12.13`](base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) suma el quinto documento al árbol de la fase.** El cambio a `F12` lo **decidió el usuario el 2026-08-13**; esa regla está congelada como texto suyo y el agente no la ajusta por cuenta propia.
- **El resultado se arma desde el plan, no desde lo que se hizo.** La lista de casos, su criterio y su prioridad **se copian** del `plan_pruebas`; un caso que esté en uno y no en el otro es defecto de trazabilidad y se arregla antes de dar veredicto. Y §5.1 pone frente a frente **cada meta que el plan fijó** (cobertura, casos críticos ejecutados, métricas propias, criterios de salida) contra lo que dio de verdad: sin eso, el plan podía exigir el 100% de los críticos y el resultado no decirlo nunca.
- **[`plantillas/planes/pruebas.md`](plantillas/planes/pruebas.md) deja de recibir resultados.** Se le quitan la tabla de ejecución por caso y el resumen de corrida; en su lugar apunta al documento nuevo. El plan define **qué se va a medir**; el resultado dice **cuánto dio**.
- **[`plantillas/estado-fase.md`](plantillas/estado-fase.md) gana §1.1 · Veredicto de las pruebas**, que se **copia** del resultado y no se escribe de memoria. Es de donde sale el estado de la estación de verificación, y con un criterio en "No" la fase no cierra.
- **[`plantillas/funcionalidad-implementada.md`](plantillas/funcionalidad-implementada.md) §3 pasa a resumir del resultado**, no a redactarlo: si dice algo que el resultado no respalda, manda el resultado.
- **[`plantillas/HU.md`](plantillas/HU.md)** suma la columna de resultado a la tabla de fases y la fila correspondiente a la tabla de qué documento responde qué.
- **[`base/02`](base/02-flujo-de-trabajo/base.md)**: `F4` aclara que lo que se aprueba son los dos planes y que el plan aprobado no se modifica para anotarle resultados; la etapa 7 de `F15` cierra ahora con el `resultado_pruebas` escrito, no con un conteo verde reportado de palabra.
- **[`validadores/fases.py`](validadores/fases.py)** incluye `resultado_pruebas.md` entre los documentos que espera de una fase. Sigue siendo **aviso**, no falla: una fase recién abierta todavía no lo tiene, y eso no es incumplimiento.
- **Retroactividad.** Las fases ya cerradas no se reabren para producirlo. Aplica a las que se abran desde esta versión.

## 8.2.0 — 2026-08-13

**MENOR** (aditivo: una sección nueva en la plantilla de HU; no invalida ninguna HU ya escrita).

**La cadena de trazabilidad se cortaba en la HU.** El brief lista sus épicas, la épica lista sus HU y cada HU nombra su épica ([`13·DOC16`](base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md)). De ahí para abajo el hilo se perdía: la HU no nombraba las fases que la implementan ni sus planes, así que desde el requisito no había cómo llegar a la ejecución. Se llegaba al revés —la fase sí declara qué CA cubre— y un enlace de una sola vía no se mantiene: cuando la fase se mueve o se divide, nadie actualiza el otro lado porque el otro lado no existe.

- **[`plantillas/HU.md`](plantillas/HU.md) gana la sección `8 · Fases que la implementan`**: una fila por fase con los CA que cubre, sus dos planes y su estado. Las secciones siguientes corren de número.
- **Se completa a medida**, igual que la lista de épicas del brief y la de HU de la épica. Una HU recién escrita la tiene vacía, y eso es correcto: las fases se definen después.
- **Además, una tabla de qué documento responde qué** (el requisito, el plan, las pruebas, el estado, el cierre), para no ir a buscar al documento equivocado. Es el mismo problema que resolvió [`8.1.0`](#810--2026-08-13) en los dos planes, visto desde arriba.
- **Retroactividad.** Una HU ya escrita y aceptada no se reabre por esto; la sección se agrega cuando se le definan fases.

## 8.1.0 — 2026-08-13

**MENOR** (aditivo: dos secciones nuevas en dos plantillas; no invalida ningún plan ya escrito).

**Un documento terminado no decía qué era.** El propósito de cada plantilla vivía dentro de la caja de instrucciones, y esa caja la plantilla manda borrar al llenarla. Resultado: el `plan_trabajo` y el `plan_pruebas` de una fase quedaban sin una sola línea que explicara para qué existe cada uno. Quien los abre meses después tiene que deducirlo del contenido, y quien tiene que aprobarlos no sabe qué está aprobando.

- **[`plantillas/planes/trabajo.md`](plantillas/planes/trabajo.md) y [`plantillas/planes/pruebas.md`](plantillas/planes/pruebas.md)** ganan una línea fija bajo el título: **para qué sirve** el documento, y dónde vive lo que no le toca a él. Va fuera de la caja de instrucciones y **sobrevive al llenado**.
- **Una línea, no dos.** La primera versión traía además un apartado *"qué no es"*. Se descartó: si el "para qué sirve" está bien escrito, ya excluye lo demás, y la negación repetía en forma de contraposición lo que la [lista de marcadores](base/00-identidad-y-rol/marcadores-de-ia.md) señala como adorno. Lo que sí valía era decir **dónde vive lo otro**, y eso se dice en positivo, dentro de la misma línea.
- **La caja de instrucciones lo dice explícito**: se borra ella, no la línea de arriba.
- **Retroactividad.** Un plan ya escrito y aprobado no se reabre por esto. Las dos líneas se agregan al escribir el siguiente.
- Como las plantillas cambiaron de huella, su copia local en cada proyecto queda marcada vieja hasta la próxima corrida del instalador; el texto local no se pisa.

## 8.0.1 — 2026-08-13

**PARCHE** (no cambia qué se exige: la narrativa ya tenía que estar; ahora se ve).

- **[`plantillas/HU.md`](plantillas/HU.md) §2 · Narrativa.** Las tres líneas (`Como`, `Quiero`, `Para`) pasan a lista. Sin el guion, Markdown junta los tres renglones en un solo párrafo corrido y la narrativa, que es lo primero que alguien lee de una HU, queda ilegible. Se agrega la nota que dice por qué van como lista, para que nadie las vuelva a dejar sueltas.
- Como la plantilla cambió de huella, la copia local del catálogo de cada proyecto queda marcada vieja hasta la próxima corrida del instalador; el texto local no se pisa.

## 8.0.0 — 2026-08-12

**MAYOR** ⚠ obliga a migrar (todo catálogo de proyecto con reglas `P` ya escritas tiene que agregarles su respaldo; la que no lo tenga se queda sin respaldo hasta que se cree la regla de base que le falta).

**Las reglas de un proyecto dejan de nacer sueltas.** Hasta ahora la capa 3 podía escribir cualquier regla `P` sin más justificación que "lo acordó el equipo": la plantilla del catálogo lo admitía de frente, con un campo que aceptaba *"regla nueva, no cubierta por la base"*. Un catálogo así crece hasta volverse un estándar paralelo, con la diferencia de que ese no pasa por checklist, no se versiona y nadie lo audita.

- **Nueva [`20·M16 · Toda regla de proyecto nombra la regla de base que concreta`](base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)** (extiende [`M1`](base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md)). Cada `P` declara, con su enlace, la regla de `base/` cuyo criterio concreta o endurece. Si ningún criterio la cubre, la regla de base se escribe primero, agnóstica y por el procedimiento completo ([`M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md)); hasta entonces la `P` no se publica.
- **El respaldo es del criterio, no del detalle**, y por eso la regla no choca con [`M3`](base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md). La base dice **qué hay que decidir** (`06·R4`: lo caro y estable se cachea, con invalidación clara); la `P` dice **con qué valor se decide aquí** (el catálogo, 10 minutos). Sin esa separación la regla se trancaba: una `P` de stack no puede subir a `base/`, y sin respaldo tampoco podría existir. El desarrollo, con la tabla de las dos mitades, queda en [`base.md`](base/20-meta-reglas/base.md).
- **Qué pasa con lo que no encaja.** Si al quitarle el detalle del proyecto no queda nada que le sirva a otro, no era una regla: era una decisión de configuración, y va donde va la configuración.
- **[`plantillas/reglas-proyecto.md`](plantillas/reglas-proyecto.md) cambia de forma.** El campo *Relación con la base* pasa a llamarse **Respaldo**, es obligatorio y lleva enlace; desaparece la salida *"regla nueva, no cubierta por la base"*. Se suma la sección *Ninguna `P` se sostiene sola*. Como la plantilla cambió de huella, el catálogo de cada proyecto queda marcado viejo hasta la próxima corrida del instalador; el texto local no se pisa.
- **[`20·M16` queda registrada como validable](validadores/reglas-validables.md)**, y no en seco: el catálogo vive en el proyecto. El script comprueba que cada `P` trae su respaldo y que el ID citado existe en `base/`; que el criterio citado sea de verdad el que la `P` concreta lo decide quien lee.
- **[`13·DOC10`](base/13-documentacion/reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md) no se toca.** Esa regla exige registrar y numerar la regla propia, que es otra exigencia; el respaldo es de dónde sale, y son dos cosas que se cumplen por separado ([`M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)).

## 7.0.0 — 2026-08-10

**MAYOR** ⚠ obliga a migrar (todo documento que se entregue desde ahora se relee contra la lista de marcadores; un proyecto al día tiene que empezar a hacerlo).

**Lo que el agente entrega deja de leerse como escrito por una máquina.** Hasta ahora el estándar solo pedía que el texto se entendiera ([`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)), y un documento puede entenderse perfecto y venir lleno de muletillas, rayas largas y secciones todas del mismo tamaño. Eso lo nota cualquiera que lo lea, y en un entregable pesa.

- **Nueva [`00·ID8 · Escribe sin las marcas que delatan generación automática`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md)** (extiende `ID7`). Alcanza a documentación, manuales, informes y a cualquier texto que una persona vaya a leer como trabajo terminado. Ningún documento se entrega sin releerlo contra la lista.
- **Nuevo anexo del capítulo [`marcadores-de-ia.md`](base/00-identidad-y-rol/marcadores-de-ia.md)**, la lista cerrada: 62 marcas en ocho secciones, cada una con qué se escribe en su lugar. Van ordenadas de la más fácil de ver a la más difícil de disimular: palabras y muletillas, puntuación y tipografía, marcas invisibles, estructura, el español que no es de acá, contenido y tono, metadatos del archivo, y el contraste con lo escrito antes. Va como anexo y no dentro de la regla porque el cuerpo de una regla son cuatro líneas ([`20·M5`](base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md)), y vive en `base/` porque es lo único que heredan los proyectos.
- **Dos secciones que no venían en la guía de origen.** *Marcas invisibles* (espacio duro, caracteres de ancho cero, guion suave, `…` como carácter único): no se ven leyendo, sobreviven a cualquier reescritura y son las únicas que un script cuenta sin equivocarse. Y *El español que no es de acá*: el léxico de España, el `vosotros`, el pretérito compuesto donde va el simple y el español neutro sin acento de ninguna parte, que en Colombia salta a la primera lectura.
- **Qué no cuenta como marca.** La notación que el propio estándar define (la cita `NN·ID`, los `[BLINDADA]` y `*opt-in*`, los bloques `INCORRECTO / CORRECTO`, los ✅ ❌ de la tabla del checklist), la flecha dentro de una notación, la sección fija que pide una plantilla, los bloques de código y la salida de herramientas. Y el límite: la lista quita adorno, nunca precisión. Si quitar una marca vuelve el texto confuso, manda `ID7`.
- **Lo que la lista no cubre, dicho en la lista.** La norma del español —ortografía, gramática, sintaxis, variedad del país— no está en el estándar: [`01·C8`](base/01-conducta.md#c8--habla-el-idioma-del-proyecto) fija el idioma y nada más. Escribir bien y no sonar a máquina son dos exigencias distintas, y la primera todavía no tiene regla.
- **[`00·ID8` queda registrada como validable parcial**](validadores/reglas-validables.md): un script puede contar las marcas de palabra y tipografía; que el documento suene o no a máquina lo decide quien lo lee.
- **Lo que esto deja pendiente.** El texto que ya está escrito —`base/`, `plantillas/`, los README del repositorio— usa la raya larga como inciso por todas partes. La norma nueva no reabre lo cerrado, así que rige para lo que se escriba desde ahora; limpiar lo anterior es un trabajo aparte que todavía no se hizo.

## 6.1.0 — 2026-08-09

**MENOR** (aditivo: nada de lo que ya se cumplía deja de cumplirse).

**Cada sesión pide su nombre mientras todavía hay con quién acordarlo.** El enganche crea el archivo como `AAAA-MM-DD-sesion.md` porque al abrir el chat nadie sabe de qué va a tratar, y ponerle el tema después quedaba en que el agente se acordara — que es justo lo que el estándar no da por hecho. En el histórico de este repositorio se veía el resultado: ocho sesiones quedaron llamándose "sesión del AAAA-MM-DD", y esa línea del índice es lo único que la siguiente sesión ve de ellas.

- **[`validadores/historico.py`](validadores/historico.py) — `aviso_de_nombre`.** Cuando el archivo todavía tiene el nombre genérico y la sesión ya tuvo una respuesta, devuelve el recordatorio de proponerle al usuario nombre y resumen. [`hook_historico.py`](validadores/hook_historico.py) lo escribe en su salida del `UserPromptSubmit`, que Claude Code le entrega al agente en ese mismo turno. **Se pide una sola vez**: queda la marca `<!-- nombre: preguntado -->` en el archivo. No se pide en el primer mensaje —ahí el tema todavía no existe— y **nada se renombra solo**: el nombre lo aprueba el usuario.
- **`--renombrar`, el comando que hace el cambio completo.** `python validadores/historico.py --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"` mueve el archivo, corrige su título y arregla la línea del índice — las tres cosas. Renombrar a mano dejaba el índice apuntando a un archivo que ya no está. La fecha sale del nombre viejo y no del reloj: una sesión que se nombra al otro día sigue siendo la del día que ocurrió. Las tildes se conservan en el título y en el índice, y se quitan del nombre del archivo, que viaja en enlaces y rutas.
- **El mismo nombre en la sesión de Claude Code.** El recordatorio trae también la línea `/rename <tema>` para que el usuario la pegue: pone ese nombre en la pestaña, en la barra del prompt y en `/resume`. La pega él porque `/rename` es un comando del usuario — el agente no lo puede ejecutar y ningún enganche fija el título de la sesión. Lo que se automatiza es que los dos nombres salgan de la misma propuesta, en el mismo momento.
- **[`plantillas/historico-chat.md`](plantillas/historico-chat.md)** documenta las tres cosas en *Qué hace el agente aquí*. Como la plantilla cambió de huella, el `historico-chat/README.md` de cada proyecto queda marcado viejo hasta la próxima corrida del instalador; el texto local no se pisa.

## 6.0.0 — 2026-08-08

**MAYOR** ⚠ obliga a migrar (`00·ID2` queda derogada: lo que se escriba desde ahora sigue `00·ID7`, y quien cite `ID2` tiene que citar `ID7`).

**Todo lo que el agente escribe se entiende sin saber del tema.** Hasta ahora la norma decía lo contrario: [`00·ID2`](base/00-identidad-y-rol/reglas/ID2-escribe-en-registro-tecnico-sin-adornos.md) pedía escribir *"para quien lee código: preciso, técnico"*, y el "que hasta un niño lo entienda" quedaba reservado a la pantalla del producto ([`17·I4`](base/17-interfaz.md#i4--texto-para-el-usuario-no-jerga)). El resultado se veía en la práctica: documentación correcta que solo entiende quien ya sabe. Ahora el estándar es uno solo, y las reglas mismas entran en él.

- **Nueva [`00·ID7 · Escribe para que lo entienda quien no sabe del tema`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)** (deroga `ID2`). Alcanza a todo lo que el agente produce —respuestas, documentación, manuales, mensajes y las reglas del propio estándar—: palabras de todos los días, ideas directas, párrafos cortos, y el término técnico que no se pueda evitar explicado en sencillo la primera vez. Cada cosa se explica diciendo **qué hace**, **para qué sirve** y **qué resultado deja**. El ejemplo se agrega solo si aclara. Antes de dar un texto por terminado se relee comprobando que se entiende sin conocimiento previo.
- **La claridad no se compra con imprecisión.** Se cambia la palabra difícil por la fácil, nunca el dato exacto por uno vago: la documentación técnica también sigue la regla, sin perder lo que la hace exacta.
- **[`00·ID2`](base/00-identidad-y-rol/reglas/ID2-escribe-en-registro-tecnico-sin-adornos.md) queda `[DEROGADA]`**, con su texto intacto y la nota de qué la reemplaza ([`20·M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)). Lo único suyo que sobrevive —sin relleno ni fórmulas de cortesía— lo conserva `ID7`.
- **[`17·I4`](base/17-interfaz.md#i4--texto-para-el-usuario-no-jerga) deja de ser "lo contrario"** de cómo escribe el agente: pasa a ser el mismo estándar llevado a la pantalla del producto, donde además no asoman siglas ni códigos internos.
- **La higiene de [`20 · Meta-reglas`](base/20-meta-reglas/base.md) se alinea:** el lenguaje de una regla ya no es "técnico", es imperativo, corto y en palabras de todos los días.

## 5.0.0 — 2026-08-08

**MAYOR** ⚠ obliga a migrar (`02·F13` cambia de exigencia: el agente ya no se detiene a esperar que el usuario cree la estructura, la crea él).

**El `CLAUDE.md` pasa a ser el setup del agente, y la instalación se hace sola.** Instalar un proyecto pedía siete pasos a mano —copiar la plantilla, reemplazar cada `«…»`, crear `proyectos/`, editar el `.gitignore`, poner los 4 archivos de `.agente/`, anotar el proyecto en el registro central y fijar la versión adoptada— y hasta que alguien los hiciera, el proyecto trabajaba **sin reglas**. Ahora los pone el instalador: una línea deja el entorno completo, operativo y comprobado.

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

- **[`plantillas/CLAUDE.md.plantilla`](plantillas/CLAUDE.md.plantilla) — sin el recuadro de pasos manuales.** Se abría con *"BORRAR ESTE RECUADRO"* y cuatro instrucciones para el usuario; ese recuadro **era** el proceso de instalación, y era lo que fallaba. En su lugar, la sección **Instalación** con la única línea que hay que correr, qué deja puesto y qué no decide. Los marcadores (`«RUTA-ESTANDAR»`, `«NOMBRE-PROYECTO»`, `«SLUG-PROYECTO»`, `«VERSION-ESTANDAR»`) los llena el instalador; los opt-in `15`–`19` traen su valor por defecto (`no`) en vez de un `«sí / no»` que dejaba el archivo reprobando hasta que alguien lo editara. Nueva sección **2.5** (el código del usuario) y arranque de sesión reordenado: instalar es el paso 1.
- **[`validadores/instalar.py`](validadores/instalar.py) instala el proyecto entero**, no solo los enganches: estructura base (`proyectos/`, `documentacion/`, `prompts/`), `CLAUDE.md` generado desde la plantilla con las rutas de la máquina, `.gitignore`, los 4 archivos de `.agente/`, la fila en el registro central — y al terminar corre el checklist y reporta lo que quedó. Sobre un proyecto ya instalado no duplica ni pisa nada; sobre uno con el `CLAUDE.md` viejo, llena los marcadores que queden (incluidos los de plantillas anteriores) y agrega solo las secciones que la plantilla sumó.
- **[`02·F13`](base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) deja de ser un muro.** Pasa de *"Detente si el proyecto no tiene su estructura base"* a *"Deja la estructura base puesta antes de trabajar"*: crear una carpeta que la norma exige no es una decisión del usuario, es la norma. Lo que sigue siendo suyo —y la regla lo dice más fuerte que antes— es **qué va dentro de `proyectos/`**: el agente crea la carpeta vacía y **nunca** mueve, reorganiza ni acomoda código que ya exista. Se retiran el mensaje de orientación y el bloqueo del arranque. El resultado del checklist de la regla queda **anulado**: se vuelve a aplicar en el próximo repaso del capítulo.
- **[`01·C18`](base/01-conducta.md) se aplica sola.** Pedía *"avisa al usuario y ofrece aplicarlos"* y *"jamás en silencio"*: una pregunta cuya única respuesta útil es "sí", que mientras no se contestaba dejaba el `CLAUDE.md` viejo. Ahora el instalador aplica lo aditivo y **dice qué agregó** — en su salida y en el registro de `documentacion/versiones/`. Sigue sin pisar, reordenar ni borrar lo escrito.
- **[`plantillas/stack-instalacion.md`](plantillas/stack-instalacion.md)** cambia la columna *"Cómo se instala"* por *"Qué hace el instalador"*: los 13 componentes se instalan con la misma línea. Ninguna fila le pide nada al usuario.
- Un `«…»` dentro de una frase deja de contar como marcador sin llenar: es cómo se nombra a un marcador, no un hueco.
- **El propio estándar queda fuera** de la configuración de proyecto: no es un proyecto que use el agente, es donde viven las reglas. Recibe los enganches, el histórico y la memoria; no `proyectos/`, ni `.agente/`, ni un `.gitignore` que borraría su `CLAUDE.md` del repositorio.

## 4.0.0 — 2026-08-08

**MAYOR** ⚠ obliga a migrar (dos reglas del capítulo `02` quedan derogadas: quien cite `02·F6` o `02·F7` tiene que citar `13·DOC1` y `13·DOC3`).

**`13 · Documentación` se somete al checklist.** Era el único capítulo grande que nunca había pasado por [`M14`](base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md): 16 reglas, 30 KB, cero bloques de checklist. La auditoría de [`analisis/base-2026-08-07-cumplimiento-meta-reglas.md`](analisis/base-2026-08-07-cumplimiento-meta-reglas.md) §5.14 lo había medido — **1 cumplía, 5 al borde y 10 no**. Ahora son **18 reglas, las 18 CUMPLE**, cada una con su resultado escrito y su motivo.

- `base/13-documentacion.md` → `base/13-documentacion/base.md` + `reglas/`, el mismo molde que `00-identidad-y-rol/`, `02-flujo-de-trabajo/` y `20-meta-reglas/`. El índice del capítulo dice qué exige cada regla en una línea; el cuerpo de cada una pasó de párrafos a una a cuatro líneas.
- **Dos reglas nuevas, ninguna exigencia nueva.** [`DOC17`](base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md) (un `README.md` por nivel del árbol) vivía dentro de `DOC15`, y `DOC16` ya la citaba como si fuera regla propia. [`DOC18`](base/13-documentacion/reglas/DOC18-actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad.md) (actualizar el mapa al cerrar) era la segunda mitad de `DOC9`, que pedía dos cosas cumplibles por separado — lo anunciaba su propio título. Quien las citaba dentro de la regla vieja ahora las cita por su ID.
- **`DOC14` deja de nombrar herramientas.** Era la regla más larga del capítulo (58 líneas): nombraba visor de repositorio, editor, código de error y "route", y traía **rutas reales de un cliente** en los ejemplos — `M3` de frente. Los ejemplos son ficticios y el montaje del render local salió a [`base/13-documentacion/render-local-de-md.md`](base/13-documentacion/render-local-de-md.md), anexo del capítulo: es infraestructura del proyecto, no regla de redacción de enlaces.
- **`DOC5` describe el backend en concepto**, no con un motor, una herramienta y una carpeta concretos. Cuál se usa lo declara la capa 3, que es donde `M3` lo manda.
- **`DOC10` deja de depender hacia arriba.** Citaba `P28` —una regla del catálogo de **un proyecto**— desde capa 2, que [`M7`](base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) prohíbe, y cerraba con una enumeración congelada de IDs citables que ya estaba vieja; lo que garantiza que toda regla se pueda citar es `M4`.
- **`DOC3` y `DOC11` dejan de repetirse.** `DOC11` se declaraba *"extiende DOC3"* y a continuación copiaba entera su tabla. El principio queda en `DOC3`, la tabla solo en `DOC11`.
- **`DOC12` completa su excepción** —tenía condición, le faltaban límite y autorizador ([`M8`](base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md))— y **`DOC4` gana el ejemplo** que no tenía.
- Los procedimientos y formatos que ocupaban el cuerpo de `DOC6`, `DOC8`, `DOC12` y `DOC13` viven donde corresponde: `plantillas/`. Nueva: [`plantillas/retrodocumentacion.md`](base/13-documentacion/retrodocumentacion.md), los seis pasos de `DOC6`.

**Se consolidan los dos duplicados.** [`02·F6`](base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md) y [`02·F7`](base/02-flujo-de-trabajo/reglas/F7-no-cierres-una-fase-con-trazabilidad-incompleta.md) exigían lo mismo que `DOC1` y `DOC3` —el ejemplo de `F7` era idéntico palabra por palabra— y las cuatro reprobaban por eso. Quedan **derogadas** ([`M11`](base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)): marca en el encabezado, texto original conservado debajo, ID no reutilizado. Con eso, `DOC1` y `DOC3` pasan a CUMPLE y el capítulo `13` queda **18 de 18**.

**Qué hay que hacer en un proyecto:** cambiar `02·F6` por `13·DOC1` y `02·F7` por `13·DOC3` donde se los cite —specs, planes, fases abiertas—. Las fases ya cerradas no se reabren: quedan selladas con la versión bajo la que cerraron.

Las citas del resto del estándar se reenlazaron solas a los archivos de destino (`validadores/citas.py`).

## 3.1.1 — 2026-08-07

**PARCHE** ⚠ **corrige una pérdida de datos.** Quien tenga 3.0.0 o 3.1.0 instalado debe actualizar antes de abrir otra sesión.

**La migración borraba memoria real.** `recuerdos.migrar()` borraba el archivo del almacén de la herramienta cuando era idéntico a uno del repositorio, con el argumento de que no se perdía nada. El argumento se cae cuando el almacén es un *junction* a `historico-chat/memory/`: origen y destino son **el mismo archivo**, compararlo consigo mismo da idéntico siempre, y el borrado se llevaba el único ejemplar. Pasó en un proyecto real, dos veces — una desde el instalador y otra desde el enganche, que corre solo en cada arranque y en cada edición.

- **Ya no se borra nada, nunca.** Todo lo que hay en el almacén se mueve; si el nombre está ocupado, entra como `<nombre>-local.md` y decide el usuario. Un enganche que corre solo no puede tener permiso de destruir: se equivoca una vez y se lleva la memoria entera sin que nadie lo pida.
- **El almacén enlazado pasa a ser una forma válida de cumplir `01·C19`.** Si es un *junction* o un enlace simbólico a la carpeta del repositorio, la herramienta ya escribe dentro del repositorio: no hay nada que mover, el checklist da por cumplido y el instalador **no toca la carpeta**. Se compara por identidad en disco (`os.path.samefile`), no por el texto de la ruta — dos rutas distintas pueden ser el mismo sitio.
- Cinturón además de eso: mover un archivo sobre sí mismo se detecta y se salta.

Lo escrito antes no se recupera solo: si la carpeta quedó vacía, se restaura del último commit (`git checkout -- historico-chat/memory/`).

Detrás: 2 pruebas nuevas —el duplicado idéntico que ya no se borra y el almacén enlazado que no se toca— y una verificación contra un *junction* de Windows de verdad, no simulado (206 en total).

## 3.1.0 — 2026-08-07

**MENOR** (aditivo: la sesión nueva arranca sabiendo qué pasó en las anteriores; ningún proyecto tiene que hacer nada más que reinstalar).

**Un chat nuevo empieza en blanco: lo que no se le inyecta, no existe para él.** El histórico se venía escribiendo desde `2.0.0`, pero nadie lo leía — la sesión siguiente no sabía siquiera que existía. Y la memoria acababa de mudarse al repositorio (`3.0.0`), donde la herramienta ya no la carga sola. Las dos cosas se resuelven igual: al abrir la sesión se inyecta el **índice**, no el contenido.

- `validadores/hook_sesion.py` — además de las reglas base, carga el índice de la memoria (`historico-chat/memory/memory.md`) y el del histórico (las últimas 40 sesiones, con el tema de cada una), con la orden de abrir con `Read` la que haga falta. Las transcripciones enteras no van: son la conversación completa y llenarían la ventana con lo que casi nunca se necesita.
- **Las dos se cargan también en el propio estándar.** Ahí no hay instalación que revisar —el enganche salía sin hacer nada—, pero la memoria y el histórico sí son los del usuario.
- `validadores/historico.py` — `sesiones()` y `contexto()` leen el índice del `README.md`; la línea de la sesión se comprueba **en cada mensaje** y no solo al crear el archivo: si al crearlo no había índice, esa sesión quedaba invisible para siempre.
- `validadores/enlaces.py` — `historico-chat/` entra en las carpetas con índice obligatorio. Una sesión sin su línea pasa a ser **falla**, no descuido; una línea que apunta a un archivo renombrado, aviso.
- `plantillas/historico-chat.md` — nueva sección: el índice es lo que lee la próxima sesión, y renombrar el archivo sin corregir la línea lo rompe.

Detrás: 6 pruebas nuevas (205 en total).

## 3.0.0 — 2026-08-07

**MAYOR** ⚠ obliga a migrar (la memoria del agente pasa al repositorio; un proyecto al día tiene que reinstalar para mover la suya).

**La memoria del agente deja de vivir en la herramienta.** Claude Code guardaba lo que el agente debe recordar entre sesiones en `~/.claude/projects/<ruta-del-proyecto>/memory/`, fuera del proyecto. Ahí no se ve en `git`, no se puede revisar en un cambio, no se versiona y no viaja a otra máquina: al clonar el proyecto en otro equipo, la memoria se queda atrás y nadie se entera. Ahora va en `historico-chat/memory/` del proyecto, y el almacén local queda **vacío** — sin copia ni puntero, porque dos versiones del mismo recuerdo terminan diciendo cosas distintas y la que manda es la que nadie puede leer.

- `base/01-conducta.md` · **`C19`** (nueva) — la memoria se escribe en `historico-chat/memory/`, un archivo por recuerdo; el almacén de la herramienta queda vacío. Vive en `01` y no en `13` por lo mismo que `C18`: el capítulo se carga literal en cada sesión, así que rige aunque el proyecto todavía no tenga la carpeta.
- `plantillas/memoria.md` (nueva) — el índice que se instala como `historico-chat/memory/memory.md`: la norma, la forma de cada recuerdo (qué se pide · por qué · cómo se aplica) y la tabla. Es documento heredado con sello; **no se pisa**, lo llena el proyecto.
- `plantillas/CLAUDE.md.plantilla` · **§2.4** (nueva) — la cuarta carpeta del proyecto, con su regla de versionado. El paso 6 la nombra entre lo que deja instalado.
- `plantillas/stack-instalacion.md` — componente **`recuerdos`**: la carpeta con su índice **y** el almacén local vacío. Las dos mitades son la misma exigencia: tener la carpeta y dejar los recuerdos afuera es no tener memoria.

Detrás, para que no dependa de que el agente se acuerde:

- `validadores/recuerdos.py` (nuevo) — resuelve dónde guarda la herramienta la memoria de cada proyecto (reemplaza por `-` todo lo que no sea letra o dígito de la ruta) y la **mueve**. Un archivo idéntico al que ya está en el repositorio se borra; uno con el nombre ocupado entra como `<nombre>-local.md` y se avisa — nada se pisa. La comparación de nombres ignora mayúsculas: en Windows `MEMORY.md` y `memory.md` son el mismo archivo.
- `validadores/hook_recuerdos.py` (nuevo) — enganche en `SessionStart` (recoge lo que quedó de sesiones anteriores) y en `PostToolUse`·`Write|Edit` (recoge el recuerdo en el momento en que se escribió; si no, pasaría toda la sesión en la carpeta equivocada y el agente lo daría por guardado). Es el único enganche que **sí** corre en el propio estándar: ahí vive la memoria del usuario.
- `validadores/instalar.py` — `instalar_recuerdos()`: crea la carpeta con el índice sellado y vacía el almacén local en la misma corrida.
- `validadores/checklist.py` · `versiones.py` — el componente `recuerdos` reprueba si falta la carpeta, si el índice quedó viejo o si algo sigue en el almacén local.

**Qué hay que hacer en un proyecto ya instalado:** correr `python validadores/instalar.py "<proyecto>" --aplicar`. Crea la carpeta y mueve lo que hubiera. Lo que entre como `-local` lo decide el usuario.

## 2.5.0 — 2026-08-07

**MENOR** (las diecinueve reglas del flujo pasan por el molde y por el checklist; ninguna cambia qué exige).

**El capítulo 02 se somete al estándar, como ya hizo el 20.** `M14` dice que ninguna regla nace fuera del procedimiento y que su cierre es el checklist. Se aplicó a `F0`–`F13`. **Resultado: 9 cumplen, 10 no** — y las diez reprueban por cosas que solo el usuario puede decidir.

**La regla se separó de su explicación.** Cada archivo de `reglas/` conserva **solo la exigencia**: encabezado, cuerpo de una a cuatro líneas, dependencia declarada, excepción con sus tres partes y ejemplo. Todo lo que desarrollaba, ilustraba o justificaba —la tabla de once etapas, la construcción de la línea base, la casuística de migración, el protocolo de `F8`, el mensaje de orientación de `F13`— pasó a `base.md`, a una sección `### F<n>` por regla. `F4.3`, que era la regla más larga del catálogo con 78 líneas, quedó en cinco.

- **`F0` toma el texto corregido que `estructura-regla.md` ya publicaba** desde la v2.2.0 sin que nadie lo aplicara. Convivían dos versiones de la misma regla y ninguna decía cuál mandaba.
- **Los títulos que contaban ahora mandan** (`M5`): `F0 · Recorre la cadena completa, sin saltar eslabones` · `F3 · Ejecuta seguido el plan aprobado` · `F5 · Corre solo las suites que la fase toca` · `F7 · No cierres una fase con trazabilidad incompleta` · `F9 · No subdividas ni renegocies un plan ya aprobado` · `F13 · Detente si el proyecto no tiene su estructura base`, entre otros. **Ningún ID cambió** (`M4`); los archivos se renombraron detrás del título.
- **`F13` pierde la marca inventada** `[GATE DE ARRANQUE · PRECONDICIÓN]`, que el propio `estructura-regla.md` usaba como anti-ejemplo literal. Que corra primero lo dice el capítulo, no una etiqueta.
- **Ocho excepciones que decían cuándo no aplican pero no hasta dónde ni quién autoriza** quedaron completas (`M8`): `F0`, `F2`, `F4`, `F4.2`, `F4.4`, `F9`, `F10`, `F11`.
- **Se rompió el ciclo de dependencias `F4.4 ↔ F4.5`** y la duplicación `F3`/`F9`, que ahora es `extiende 02·F3` (`M7`). El texto que `F5`, `F6` y `F7` copiaban de `08·T5`, `13·DOC1` y `13·DOC3` —ejemplo incluido, palabra por palabra— se reemplazó por el enlace (`M5`).

**Las diez que reprueban, y por qué.** No son defectos de redacción: son decisiones de catálogo, y el catálogo lo decide el usuario.

| Reglas | Fila | Qué falta decidir |
|---|---|---|
| `F4.1`–`F4.5` | 6 | el sub-ID decimal no lo contempla `M4`: legalizarlo o promoverlas a `F14`… |
| `F4`, `F4.3`, `F4.5` | 8 · 9 | llevan dos exigencias que se cumplen por separado; partirlas crea IDs nuevos |
| `F5`, `F6`, `F7` | 2 · 4 | el dueño del tema es `08` y `13`; derogarlas a favor de `T5`, `DOC1` y `DOC3` es `M11` |
| `F12` | 8 · 9 · 10 | su texto está **congelado por decisión del usuario** y el agente no lo reescribe |

Cada una lo dice en su propio archivo, con la marca *"regla vigente y reprobada"* que ya usa `M4`: siguen rigiendo (`M10` — un cambio de norma no reabre lo cerrado), pero no son conformes hasta que se resuelva.

## 2.4.0 — 2026-08-07

**MENOR** (el capítulo 02 pasa a carpeta; ninguna regla cambia qué exige ni qué ID tiene).

**`02 · Flujo de trabajo` se muda a su carpeta.** Era el archivo más grande del estándar —46 KB, catorce reglas y cinco subpartes en un solo `.md`— y ya tenía dos reglas viviendo aparte (`F12/`, `F13/`), así que el capítulo se leía en dos sitios a la vez. Ahora sigue el mismo molde que `00-identidad-y-rol/` y `20-meta-reglas/`: `base.md` es el índice y cada regla tiene su archivo en `reglas/`.

- `base/02-flujo-de-trabajo.md` → `base/02-flujo-de-trabajo/base.md`. Queda como índice: la tabla de las catorce reglas con qué exige cada una, y la secuencia del flujo. De 494 líneas a 36.
- `base/02-flujo-de-trabajo/reglas/` — **una regla, un archivo `<ID>-<título>.md`**, igual que `ID1`–`ID6` y `M1`–`M15`: `F0`–`F13`, más las cinco partes `F4.1`–`F4.5`, con el texto sin reescribir. Sin subcarpetas: `F12/` y `F13/` colgaban del capítulo y eran las únicas reglas fuera del sitio de las reglas.
- `base/02-flujo-de-trabajo/estructura-base.md` — el anexo de `F13` (el árbol obligatorio) pasa a la raíz del capítulo, donde `20-meta-reglas/` ya tiene los suyos (`checklist.md`, `estructura-regla.md`).
- **Las citas se reenlazaron al archivo de destino**, no a un ancla del índice: `02·F5` ahora abre la regla `F5`, no un encabezado dentro de un archivo de 46 KB. Aplica `M15`.

**Efecto en el arranque:** el cargador inyecta el índice de los capítulos temáticos, no su texto. Antes el índice de `02` era una línea de 46 KB; ahora son quince líneas que dicen de qué trata cada regla, y el agente lee **solo la que va a tocar**. El gate `F13` se sigue cargando literal — cambió su ruta (`validadores/cargador.py`).

Lo que **no** cambió: ningún ID, ningún texto de regla, ninguna exigencia. `F12` conserva intacto el texto literal del usuario.

## 2.3.0 — 2026-08-07

**MENOR** (aditivo: una regla nueva y un validador; ningún proyecto que herede el estándar tiene que hacer nada).

**Toda cita a otra regla lleva su enlace.** Citar por ID —`M5`, `09·G6`— obliga a quien lee a salir a buscar: abrir el capítulo, encontrar el encabezado. Con 206 citas repartidas en 43 archivos eso es fricción suficiente para que nadie compruebe nada, y una cita que nadie sigue es una dependencia que nadie verifica.

- `base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md` — la regla. Extiende `M4`, que fija el ID y la forma `NN·ID`.
- **Las 206 citas de `base/` quedan enlazadas**, al archivo y al ancla del encabezado. Las que viven en su propio archivo enlazan al archivo, sin ancla: un ancla de más se rompe al renombrar el título.
- **De paso se normalizaron tres formatos que convivían** — `` `04·S4` ``, `` `00` · N3 `` y `` `00`·N3 `` — a la única forma que `M4` admite. No es un cambio de norma: es aplicar la que ya estaba escrita.

Lo cercado no se tocó: ahí las citas son el molde que alguien va a copiar, no citas a nadie.

Detrás: `validadores/citas.py` (nuevo) — indexa dónde vive cada regla leyendo `base/`, enlaza y valida. Entra en `validar.py estandar`, así que una cita suelta o un enlace a una regla inexistente se reportan solos. 11 pruebas nuevas (191 en total).

## 2.2.0 — 2026-08-07

**MENOR** (las catorce meta-reglas pasan a archivo propio y se les aplica el checklist; ninguna cambia qué exige).

**El capítulo 20 se somete a sí mismo.** `M14` dice que ninguna regla nace fuera del procedimiento y que su cierre es el checklist en `CUMPLE`. Se aplicó a `M1`–`M14`. **Resultado: 10 cumplen, 4 no** — y las cuatro reprueban la misma fila, la 17, que exige decisión del usuario.

**La regla se separó de su explicación.** Cada archivo de `reglas/` conserva **solo la exigencia**: encabezado, cuerpo de una a cuatro líneas, ejemplo y checklist. Lo que desarrollaba, ilustraba o justificaba la regla —tablas, listas de apoyo, el porqué— vuelve a `base.md`, a una sección `### M<n>` por regla, enlazada desde el cuerpo. Con eso las filas 9 (una sola exigencia) y 10 (de una a cuatro líneas) pasan a verde en `M2`, `M5`, `M7` y `M12`, que antes las reprobaban.

**Efecto que conviene tener presente:** varias piezas movidas **mandan**, no solo explican — los tipos MAYOR/MENOR/PARCHE de `M10`, las dos prohibiciones de `M7` (sin ciclos, nunca hacia arriba), las tres aclaraciones de `M8`, el orden de búsqueda de `M12`, la tabla de destinos de `M13`. Siguen siendo texto del capítulo y el agente las lee igual, pero **ya no son texto de una regla citable por ID**. Si alguna debe poder citarse, se promueve a regla propia (`M15`…) — es decisión del usuario.

- `base/20-meta-reglas/reglas/` — las catorce, una por archivo, con el texto sin reescribir. `base.md` queda como capítulo e índice (de 204 líneas a 60).
- Se añadió el ejemplo INCORRECTO/CORRECTO que faltaba en nueve (`M2`, `M4`, `M5`, `M7`, `M9`, `M10`, `M11`, `M12`, `M13`) y el enlace de `M5` a su propio anexo `estructura-regla.md`, que no tenía — rompía la fuente única que `M2` exige.
- `validadores/reglas-validables.md` — las catorce clasificadas (`M9`). Siete se validan **en seco** sobre el propio estándar (`M3`, `M4`, `M5`, `M7`, `M9`, `M10`, `M14`): son las más rentables del catálogo y hoy no existe ninguna.
- `validadores/cargador.py` — el índice listaba las reglas nuevas como "(sin título)": un archivo de una sola regla no lleva `H1`, su encabezado es el `##` de la regla. Ahora lo usa como respaldo.
- `base/00-identidad-y-rol/reglas/` — corregida la aritmética de los seis sellos: eran `17 ✅ · 3 N/A`, no `16 ✅ · 4 N/A`.

**Las cuatro que no cumplen** quedan marcadas en su propio archivo, vigentes y reprobadas (`M10`: un cambio de norma no reabre lo cerrado). Las cuatro reprueban **solo la fila 17** — no choca con ninguna regla vigente:

| Regla | Con qué choca |
|---|---|
| `M2` | no contempla que el preámbulo comparta el número `00` con el núcleo |
| `M4` | no contempla los sub-ID decimales que el catálogo ya usa (`F4.1`–`F4.5`, `F12.1`–`F12.13`) |
| `M7` | el catálogo usa una cuarta forma de dependencia —el bloque `Encadenamiento`— 22 veces |
| `M8` | dice que las `[BLINDADA]` no admiten excepción, y `00·N1` es blindada y tiene una escrita |

Ninguna se puede cerrar sin decidir qué gana: o la meta-regla absorbe la práctica, o la práctica se corrige. Es del usuario.

## 2.1.0 — 2026-08-07

**MENOR** (aditivo: una regla nueva; ningún proyecto que herede el estándar tiene que hacer nada).

**`20·M14` · Ninguna regla nace fuera del procedimiento.** El capítulo tenía trece meta-reglas que gobernaban **cada pieza** de la creación de una regla —dónde va, qué ID lleva, qué forma tiene, cómo se versiona— pero ninguna gobernaba **el acto completo**. El procedimiento de nueve pasos existía como *sección*, sin identificador: no se podía citar desde un commit ni desde una spec, ni exigir por ID. `M14` cierra ese hueco.

Su cierre es el checklist en `CUMPLE`: sin eso la regla no se publica, se corrige o se retira.

- `base/20-meta-reglas/base.md` — la regla, con su checklist aplicado al pie. Se aplicó a sí misma: sería incoherente que la regla que exige el checklist naciera sin él.
- `validadores/reglas-validables.md` — `M14` clasificada (`M9`) como validable parcial: que la regla haya recorrido el procedimiento no lo decide un script, pero su cierre sí — la fila 19 ya la comprueba `version.py`, y la presencia del bloque de checklist es mecánica.

Queda anotado que las otras trece `M` siguen sin evaluar, igual que el resto del catálogo.

## 2.0.0 — 2026-08-07

**MAYOR** · `⚠ obliga a migrar`. Un proyecto al día tiene que correr el instalador **una vez**.

Nada de lo que un proyecto hereda del estándar puede quedarse viejo. Antes se intentaba detectar comparando títulos de sección y fechas de archivo, y las dos cosas fallan: un paso nuevo **dentro** de una sección que ya existía no cambia ningún título, y la fecha miente en cuanto alguien clona el repositorio o edita el archivo por cualquier motivo.

- **El sello.** `CLAUDE.md`, `historico-chat/README.md` y `.agente/stack-instalacion.md` llevan al final `<!-- huella: … · estandar X.Y.Z -->` con la huella de **la plantilla contra la que se sincronizaron** —no la del archivo local, que cada proyecto llena con lo suyo—. Cualquier cambio de la plantilla rompe la coincidencia, venga por dentro o por fuera del documento.
- **Quedar viejo reprueba.** Era AVISO y el componente pasaba igual: un proyecto con el `CLAUDE.md` viejo figuraba como instalación completa.
- **El registro.** Cada actualización deja un `.md` en `documentacion/versiones/`: desde cuándo el proyecto usa esa versión, qué componentes se actualizaron con su huella antes y después, qué aplicó el instalador y qué quedó pendiente. Va en `documentacion/` y no en `.agente/` porque `.agente/` está en el `.gitignore`, y saber bajo qué versión cerró cada fase tiene que poder mirarse desde cualquier copia del repositorio. Componente nuevo del stack: `versiones`.
- **El número de versión deja de reprobar.** Al proyecto no le interesan todos los cambios del estándar, solo los que tiene que aplicar: que declare `1.8.0` con el central en `2.0.0` no obliga a nada por sí solo, y dejarlo en rojo por eso es ruido que enseña a ignorar la alerta. El desfase se informa al margen; `version` ahora solo exige que la versión adoptada esté **declarada**, porque sin ella no hay con qué sellar una fase cerrada.

**Cómo se migra** — la línea de siempre, la del paso 6:

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

Deja los sellos puestos y escribe el primer registro. Hasta que se corra, `claude-md`, `historico` y `stack-instalacion` salen en rojo: no porque el proyecto esté mal, sino porque todavía no declara contra qué versión se sincronizó.

Detrás: `validadores/versiones.py` (nuevo — sellos, comparación y registro), `checklist.py`, `instalar.py`, `validar.py versiones` para verlo a mano, y 19 pruebas nuevas (180 en total).

## 1.6.0 — 2026-08-07

**MENOR.** Ningún proyecto que herede el estándar tiene que hacer nada: la exigencia nueva recae sobre quien escribe reglas **del estándar**.

**El checklist respondido queda dentro del capítulo, en dos piezas.** En 1.5.0 la sección decía lo contrario —que no se persistía copia por regla, para no inflar `base/`—. Se cambia por una razón que pesa más: **que una auditoría posterior no vuelva a analizar lo ya verificado**. La regla cuyo sello dice `CUMPLE` contra la versión vigente se salta; el trabajo se concentra en las que no lo traen o lo traen anulado. Sin esto, cada auditoría reevalúa el catálogo entero desde cero.

Dos piezas, y cada una donde sirve:

1. **El instrumento — `base/20-meta-reglas/checklist.md`, archivo nuevo.** El checklist **es estándar**, así que vive con las meta-reglas, al lado de su `base.md` y como fuente única (`M2`): las 20 filas con su meta-regla y su criterio de aprobado, cómo se decide el resultado, el molde de cómo se aplica, la regla de caducidad, y qué filas puede decidir un script (once) y cuáles piden leer la regla (nueve).
2. **La evaluación — dentro de cada regla.** Al final de su archivo, como `###`: el veredicto, contra qué versión y en qué fecha, el resultado por bloque, las `N/A` justificadas, y **el enlace al instrumento** — para que quien abra una regla suelta sepa de dónde sale esa evaluación. No repite las 20 filas (`M5`).

- `base/20-meta-reglas/base.md` — la sección del checklist queda en resumen + enlace, como ya hacen `F12` y `F13` con sus fuentes únicas.
- `base/00-identidad-y-rol/reglas/` — las seis reglas quedan evaluadas: 16 ✅ · 0 ❌ · 4 N/A · **CUMPLE**.
- `base/00-identidad-y-rol/base.md` — el capítulo lo dice y enlaza el instrumento.

**Backlog que esto abre:** las otras 164 reglas de `base/` quedan **sin sellar**. No es incumplimiento retroactivo —`M10` dice que un cambio de norma no reabre lo cerrado— pero sí es la cola de trabajo: hasta que una regla se selle, sigue entrando en cada auditoría. Se salda por capítulos, no de una vez.

## 1.5.1 — 2026-08-07

**PARCHE** (redacción y una justificación que había quedado falsa; no cambia qué se exige).

Se aplicó el checklist recién agregado a las seis reglas de `00 · Identidad y rol`. **En la primera pasada ninguna cumplía.** El resultado quedó dentro de cada regla, en [`base/00-identidad-y-rol/reglas/`](base/00-identidad-y-rol/reglas/).

- `base/20-meta-reglas/base.md` — la tabla de `M1` describía el preámbulo como *"No: describe, no exige"*. Desde que el capítulo tiene reglas (`ID1`–`ID6`, v1.4.0) esa frase era falsa, y las seis reglas chocaban con `M1` — la fila 17 del checklist. La columna es **¿Se ajusta?**: la respuesta sigue siendo **No** y la precedencia no cambia; lo que se corrigió es la justificación, que ahora dice *"un proyecto no redefine quién es el agente ni el molde de las reglas"*.
- `base/00-identidad-y-rol/reglas/` — `ID1` y `ID6` repetían texto de `01·C14` y de `20·M1` además de enlazarlo (fila 11, `M5` sin texto prestado): ahora difieren en vez de reformular. `ID1`–`ID4` pasaron de tercera persona descriptiva a presente imperativo, que es lo que pide `M5`. `ID5` gana el enlace a `00·N2`, de donde sale que la autorización sea de un solo uso.

Sigue disponible, y es decisión pendiente del usuario, la otra vía para el choque: que el capítulo deje de ser preámbulo y pase a **capa 2**. Eso sí movería la precedencia, y por eso no se tomó por cuenta propia.

## 1.5.0 — 2026-08-07

**MENOR** (aditivo: agrega una comprobación, no cambia ninguna exigencia existente).

- `base/20-meta-reglas/base.md` — sección nueva **«Checklist de la regla — qué cumple y qué no»**, entre el procedimiento de alta y la higiene del conjunto. Veinte filas agrupadas en cinco bloques (dónde va · cómo se identifica · cómo está escrita · cómo se relaciona · qué obliga fuera de su texto), cada una con su meta-regla y su criterio de aprobado, y un resultado al final que dice **CUMPLE** o **NO CUMPLE**.

El criterio de resultado es binario a propósito: una sola fila en ❌ y la regla no se publica. No hay "cumple parcial" — una regla a medias es la que después nadie sabe si rige. Solo cuatro filas admiten `N/A` (ejemplo, dependencias, ciclos y excepción), y siempre con motivo escrito.

Por qué ahí y no en `estructura-regla.md`: el checklist verifica `M1`–`M13` completas, y el anexo solo desarrolla `M5`. Además no cabía dentro de `M5`, que exige cuerpo de una a cuatro líneas.

La sección deja anotado cuáles de las veinte filas puede decidir un script solo (once) y cuáles piden leer la regla (nueve). Esa división es la especificación del validador de meta-reglas que falta.

## 1.4.0 — 2026-08-07

**MENOR** (aditivo: reglas nuevas en un capítulo que no las tenía; nada de lo que ya se cumplía deja de valer).

El capítulo del preámbulo se ajusta al capítulo 20: deja de ser prosa y pasa a tener reglas con identificador.

- `base/00-identidad-y-rol/reglas/` — seis reglas nuevas, **una por archivo**, nombradas `<PREFIJO><n>-<título>`: `ID1` criterio de desarrollador senior · `ID2` registro técnico sin adornos · `ID3` qué cuenta como entregado · `ID4` el ciclo completo de entender a documentar · `ID5` el borde del rol (seis cosas fuera por definición) · `ID6` los roles por etapa no cambian la precedencia.
- `base/00-identidad-y-rol/base.md` — pasa a ser el capítulo con el índice enlazado a las seis. El texto que antes era prosa suelta queda repartido en las reglas; lo que ya decía otro capítulo se enlaza en vez de repetirse (`20·M5`).
- `base/20-meta-reglas/estructura-regla.md` — el prefijo **`ID`** se registra en la tabla de letras ocupadas, como exige `M4` antes de estrenar un prefijo.
- `validadores/reglas-validables.md` — `ID1`–`ID6` clasificadas (criterio humano, `M9`). `ID3` se anota como caso parcial: sus cuatro condiciones ya se validan por separado; lo que no se valida es la conjunción.

Con esto queda cerrada la primera mitad del hallazgo **H-22** del informe de `analisis/`: el capítulo que `02·F0` citaba como fuente de reglas ya tiene reglas citables. Sigue abierto que el número `00` esté compartido con el núcleo.

## 1.3.1 — 2026-08-07

**PARCHE** (no cambia qué se exige; solo dónde vive el texto).

- `base/00-identidad-y-rol.md` pasa a `base/00-identidad-y-rol/base.md`. El capítulo del preámbulo queda con carpeta propia, como `20-meta-reglas/`, para poder crecer con anexos sin inflar el archivo que se carga en cada turno. El texto no cambió.

Detrás: `validadores/cargador.py` decidía qué se carga **literal en todos los turnos** por el nombre del archivo (`00-`, `01-`). Con el capítulo en carpeta, el nombre pasa a ser `base.md` y la identidad del agente habría caído al índice — es decir, el agente arrancaría sin saber quién es. Ahora la comprobación mira el **primer tramo de la ruta**, así que un capítulo del núcleo carga igual viva en archivo suelto o en carpeta.

## 1.3.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). El histórico de sesiones deja de depender de que el agente se acuerde de escribirlo:

- Plantilla nueva: `historico-chat.md` — el `README.md` de la carpeta `historico-chat/` de cada proyecto.
- `CLAUDE.md.plantilla`: punto **2.3** (la carpeta, quién la escribe, se versiona, y cómo excluirla si el chat maneja datos sensibles) y punto **6** ampliado: el instalador es el camino por el que **toda** herramienta nueva del estándar llega al proyecto, sin pasos manuales. Si algo exige configurar a mano, es defecto del estándar.

Detrás: `validadores/hook_historico.py` (enganches `UserPromptSubmit` y `Stop`) e `instalar.py`, que los deja puestos y crea la carpeta. Un proyecto al día no tiene que hacer nada: los recibe la próxima vez que corra el paso 6.

Y el **stack de instalación**: la lista de todo lo que un proyecto debe tener para que el agente esté completo.

- Plantilla nueva: `stack-instalacion.md` — los 11 componentes, qué es cada uno y cómo se instala. Se copia a `./.agente/` de cada proyecto, sellada con la huella del original: si el estándar agrega un componente, la copia deja de coincidir y eso se reporta como actualización pendiente.
- `CLAUDE.md.plantilla`: punto **2.1** (los dos archivos que el estándar escribe en `.agente/` y no se editan a mano) y paso **8** — mientras exista `.agente/INSTALACION-INCOMPLETA.md`, el agente no está completo y debe decir qué falta en cada respuesta. No bloquea: el único gate sigue siendo `F13`.

Detrás: `validadores/checklist.py` (la comprobación de cada componente; la lista se lee de la plantilla, no se duplica en código), `hook_checklist.py` en `UserPromptSubmit`, y `validar.py checklist --raiz` para verlo a mano.

## 1.2.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Un capítulo de **preámbulo**:

- `00 · Meta-reglas` — la regla de reglas: jerarquía de cuatro niveles, organización por dominio con fuente única, orden determinista de desempate ante conflicto, formato canónico de una regla, ID estable, dependencias declaradas (`extiende` / `depende de` / `deroga`), excepciones escritas dentro de la regla, criterio de validable, versionamiento obligatorio, derogación en vez de borrado, y procedimiento para agregar una regla sin duplicar ni contradecir.

No cambia ninguna regla existente: **formaliza** las convenciones que la base ya usaba de hecho y cubre lo que no estaba escrito (desempate, dependencias, derogación, anti-duplicación).

## 1.1.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Dos capítulos **opt-in** de dominio DevOps:

- `18 · Despliegue e infraestructura` — despliegue como artefacto versionado, IaC, build-una-vez, config por entorno fuera del artefacto, release reversible, checklist de despliegue, health/readiness, y correr contra producción gateado por el usuario. Extiende `09·G6`.
- `19 · Observabilidad y operación` — logs estructurados, señales doradas + trazas, SLO/alertas como código sobre síntomas, runbooks, postmortem sin culpa. Extiende `05`.

Plantillas nuevas: `checklist-despliegue.md`, `postmortem.md`. Toggles en `CLAUDE.md.plantilla §5.1`.

## 1.0.0 — 2026-08-06

Primera versión sellada del estándar. Línea base: núcleo blindado (`00`), conducta y flujo (`01`–`02`), buenas prácticas (`03`–`17`), plantillas de capa 3, memoria por señales con vigencia y ciclo de deuda, y la capa de validadores automáticos + hooks.

A partir de aquí, cada cambio de `base/` o `plantillas/` suma una entrada con su tipo.
