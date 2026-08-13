# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo.

---

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
- Los procedimientos y formatos que ocupaban el cuerpo de `DOC6`, `DOC8`, `DOC12` y `DOC13` viven donde corresponde: `plantillas/`. Nueva: [`plantillas/retrodocumentacion.md`](plantillas/retrodocumentacion.md), los seis pasos de `DOC6`.

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
