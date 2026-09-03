# 2026-09-01 · El orden de las versiones  ·  `[CAPA 3]`

Lo que dejó esta sesión. La conversación literal vive en la transcripción; acá va lo que hay que poder encontrar sin releerla.

---

## De dónde viene esta sesión

**Viene de:** nada, es trabajo nuevo. Se abrió para construir `F-014`, la última funcionalidad obligatoria de la versión 2, y no llegó a construirse: el plan que la ordena resultó estar mal leído.

---

## Hallazgos de esta sesión

### H-1 · La columna «Depende de» se estaba leyendo como orden de construcción

- **Qué pasó:** al abrir `F-014` —versión 2— apareció que su ficha dice **Depende de F-011**, que está en la versión 5. Se propuso intercambiarlas de versión y se hizo. **Al contar después, los pares fuera de orden pasaron de dos a tres:** `F-014` arrastra a `F-015` y a `F-025`. El movimiento se deshizo entero y el reparto quedó como estaba.
- **Por qué importa:** el recorrido completo de las 35 fichas mostró que la columna no dice lo que se le estaba pidiendo. **`F-027`, de la versión 1, y `F-025`, de la versión 2, están cerradas, construidas y funcionando sin su dependencia**, porque la importación trae los documentos y las fases ya escritos. Quien lea esa columna como orden de trabajo reordena un plan que no estaba mal, y de paso cree bloqueado lo que no lo está: `F-014` se puede construir hoy.
- **Qué lo soluciona:** el inventario ahora explica qué dice la columna y qué no, con las dos funcionalidades cerradas como prueba; y el plan de implementación dice por qué ninguna versión se movió, con una tabla de cambios a la línea base. No dispara historia: es un defecto de dos documentos, no una capacidad que falte.
- **Qué se decidió:** **`F-014` se queda en la versión 2 y se construye sobre lo importado.** El desorden aparente se arregla en la columna, que es donde estaba el error.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-103` · [cvds/analisis-requisitos/inventario-funcionalidades.md](../../../cvds/analisis-requisitos/inventario-funcionalidades.md) · [cvds/implementacion/README.md](../../../cvds/implementacion/README.md) §2
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-2 · Una convención de marcado que usa los signos de la prosa no se puede contar

- **Qué pasó:** el módulo iba a contar dos clases de espacio por llenar: `«…»` y el que trae nombre, como `«RESPONSABLE»`. **Se midió antes de construir** sobre las 130 historias de usuario reales: 341 marcas, 75 también en el molde, y **cero** todavía en la línea del molde. Ninguna era un hueco.
- **Por qué importa:** acá se cita con esas mismas comillas todo el tiempo, así que una marca con nombre no se distingue de una cita. Contarlas habría dado por incompleto **todo documento bien escrito**, que es el mismo error que una vez dio 559 documentos incompletos donde había 31. Y no se habría visto en las pruebas: con documentos inventados el conteo se ve perfecto.
- **Qué lo soluciona:** ya construido. El módulo cuenta solo el anónimo y lista el de nombre aparte, porque cuando `F-011` cree documentos desde el molde sí van a ser ciertos.
- **Qué se decidió:** **dos listas**, decidido por el usuario el 2026-09-01. La cuenta manda sobre los ciertos.
- **Estado:** resuelto acá
- **Responde a:** EP-013 · HU-001 · CA-03
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-104` · [documentacion/ciclo-de-vida/spec.md](../../../documentacion/ciclo-de-vida/spec.md) §5.1 · `plataforma/nucleo/ciclo_de_vida/huecos.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-3 · 24 documentos con espacios por llenar que el expediente nunca mostró

- **Qué pasó:** al comparar la cuenta nueva con la del módulo Expediente salieron **54 contra 31**. Los 24 de diferencia **son todos índices**, y un índice no entra al expediente. El uno que va al revés es una marca dentro de un bloque cercado, donde se escribe para mostrarla.
- **Por qué importa:** el expediente se usa para decidir si un proyecto está listo para entregar, y venía diciendo 31 cuando eran 54. No estaba mal: estaba respondiendo otra pregunta. Pero quien lea 31 y crea que es todo lo que falta, se equivoca.
- **Qué lo soluciona:** llenar esos 24 es trabajo de la `HU-002`, que ya está escrita y aprobada. No hace falta pieza nueva.
- **Qué se decidió:** las dos cuentas se quedan, cada una con su alcance dicho. La del expediente cuenta lo que se entrega; la del ciclo, todo lo traído.
- **Estado:** resuelto acá
- **Responde a:** EP-013 · HU-001 · CA-02
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la §3 del [resultado de pruebas](../../../documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/A-EP-013-HU-001-los-huecos-de-un-documento-se-ven/resultado_pruebas.md)
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-4 · Un documento que habla de una convención parece incumplirla

- **Qué pasó:** el módulo contaba **77 espacios por llenar en 54 documentos**. Al correr la orden sobre un documento real resultó que **51 de los 77 no eran huecos**: era la marca escrita dentro de código en la misma línea. El caso extremo fue la especificación de la marca, cuyos siete «huecos» eran las siete veces que la nombra. La cuenta de verdad es **26, en 25 documentos**.
- **Por qué importa:** un estándar escribe sobre sus propias convenciones todo el tiempo. La pieza ya excluía los bloques cercados por esa razón, y faltaba el código en la misma línea: **la regla estaba aplicada a medias**. Cincuenta pruebas verdes no lo veían, porque a nadie se le ocurre inventar un ejemplo que hable de la marca.
- **Qué lo soluciona:** ya arreglado, con dos pruebas nuevas. El mismo intento destapó que la orden se caía al mostrar un renglón con emoji, y eso también quedó cerrado.
- **Qué se decidió:** **arreglar los dos en la misma fase**, decidido por el usuario el 2026-09-01, ampliando el plan para tocar `huecos.py`. Cerrar en verde un criterio que ya se sabe malo no es cerrar.
- **Estado:** resuelto acá
- **Responde a:** EP-013 · HU-002 · CA-02
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-105` · `plataforma/nucleo/ciclo_de_vida/huecos.py` · la §5.1 de [documentacion/ciclo-de-vida/spec.md](../../../documentacion/ciclo-de-vida/spec.md)
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-5 · La protección que iba a corromper lo que protege

- **Qué pasó:** al abrir la versión 3 apareció que `F-031` estaba **construida a medias y sin declarar**: el puente que tapa credenciales existía y **lo usaba un solo camino de los seis que escriben**. Lo obvio era encenderlo en los seis. Se midió primero: cambiaría **7 documentos y 21 fragmentos** de los 1 002 guardados, y **ninguno de los 21 era una clave**.
- **Por qué importa:** los 21 son ejemplos escritos en los documentos de las fases **que construyeron el tapador**. Encenderlo en los seis habría corrompido la documentación del propio tapador, en silencio, y tapar **no se deshace**. Es la tercera vez en el día que un documento que habla de algo parece contenerlo; las dos anteriores se podían recontar, esta no.
- **Qué lo soluciona:** ya construido. **Se tapa lo que se teclea, no lo que se copia**, y lo que no se tapa se cuenta y se nombra. Los seis caminos quedan declarados en la especificación del módulo, que no tenía.
- **Qué se decidió:** el usuario pidió arrancar la versión 3 por `F-031` y después autorizó ejecutar la épica entera sin aprobar paso por paso.
- **Estado:** resuelto acá
- **Responde a:** EP-014 · HU-001 · CA-03
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-106` · [documentacion/seguridad/spec.md](../../../documentacion/seguridad/spec.md) §5.1 · `plataforma/nucleo/seguridad/revision.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-6 · La columna de dependencias tiene una vuelta, y el veredicto le faltaba una respuesta

- **Qué pasó:** al abrir las comprobaciones salió que la columna «Depende de» **tiene un ciclo**: `F-008` espera a `F-022`, que espera a `F-020`, que espera a `F-008`. Leída como orden de construcción, ninguna de las tres arranca. Y al diseñar el veredicto apareció que un proyecto sin el estándar instalado no cabe ni en «cumple» ni en «no cumple».
- **Por qué importa:** las dos son la misma clase de error. Una cadena de **necesidades** puede tener vueltas sin que nada esté mal, porque lo necesario puede existir ya; una de **construcción**, no. Y un estado que admite «no se sabe» necesita su propio nombre: devolver «cumple» a lo que no se miró es mentir, y devolver «no cumple» llena los rojos de proyectos que solo estaban sin instalar, hasta que nadie los mira.
- **Qué lo soluciona:** ya resuelto. La vuelta queda explicada en el inventario, y el veredicto tiene **tres respuestas**: cumple, no cumple, y no se pudo comprobar.
- **Qué se decidió:** arrancar la versión 3 por las comprobaciones, que es lo que desbloquea la vuelta, y después seguir con las reglas.
- **Estado:** resuelto acá
- **Responde a:** EP-015 · HU-001 · CA-03
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-107` · [cvds/analisis-requisitos/inventario-funcionalidades.md](../../../cvds/analisis-requisitos/inventario-funcionalidades.md) · `plataforma/nucleo/comprobaciones/core.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-7 · La puerta de publicación dio un rojo falso en su primera corrida

- **Qué pasó:** la puerta que decide si se puede publicar corría las pruebas del proyecto con un subcomando que **no acepta el argumento que se le pasaba**. Salió con código 2, la puerta lo leyó como rojo, y dijo **«no se publica» con las 1 082 pruebas en verde**. Su pariente apareció en la fase anterior: el lector del estado seguía solo la convención de ahora, y **siete funcionalidades cerradas y en verde salían «sin verificar»**.
- **Por qué importa:** un código de salida distinto de cero puede querer decir «las pruebas fallaron» o «no entendí lo que me pediste», y tratarlos igual convierte un error propio en un veredicto ajeno. **Un rojo falso enseña a ignorar la puerta:** la primera vez uno investiga, la tercera la salta, y el día que el rojo sea de verdad ya nadie lo mira.
- **Qué lo soluciona:** ya arreglado. La puerta corre la suite del proyecto, y el «no se pudo» tiene su propia respuesta. El lector del estado lee las dos formas de veredicto, sin reescribir ninguna fase cerrada.
- **Qué se decidió:** el usuario mandó hacer todo lo que faltaba de la versión 3 sin aprobar paso por paso.
- **Estado:** resuelto acá
- **Responde a:** EP-015 · HU-003 · CA-04
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-108` · `plataforma/nucleo/comprobaciones/puerta.py` y `estado.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-8 · Lo que más cuidado costó de una funcionalidad fue una frase

- **Qué pasó:** al escribir una regla nueva, la plataforma muestra las que hablan de lo mismo. Sobre las 248 vigentes, con un título casi idéntico al de una regla real, **encontró esa misma regla**: habría evitado un duplicado. Pero lo que decidió el diseño no fue el código: fue la frase que lo acompaña.
- **Por qué importa:** contar palabras encuentra reglas que **hablan de lo mismo**, no las que **se contradicen**. Llamarlo detector de contradicciones sería peor que no tenerlo: **quien confía en un detector deja de mirar**. Por eso el aviso dice lo que no puede decir **encuentre o no encuentre**, y hay una prueba que lo comprueba.
- **Qué lo soluciona:** ya construido, con su aviso y su prueba. Y en la misma tanda quedó impedido lo único irreversible de la épica: **ningún identificador se reutiliza**, ni el de una derogada.
- **Qué se decidió:** el usuario mandó arrancar Reglas, que es el módulo más grande de la versión 3, sabiendo que iba a ser largo.
- **Estado:** resuelto acá
- **Responde a:** EP-016 · HU-002 · CA-03
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-109` · [documentacion/reglas/spec.md](../../../documentacion/reglas/spec.md) §5.2 · `plataforma/nucleo/reglas/parecidas.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —


### H-9 · Un aviso llevaba 54 versiones saliendo vacío, y por eso nadie lo notó

- **Qué pasó:** el aviso de desfase de un proyecto trae dos partes, y la segunda —**qué cambió desde entonces**— llevaba 54 versiones saliendo vacía. El lector del registro reconocía **143 de 197** entradas, y la más reciente que entendía era la **34.2.0**. En la misma tanda apareció su pariente: comparando fechas, **185 de 248** reglas tenían el sello anulado, y el estándar dice que ninguna.
- **Por qué importa:** **un aviso vacío se ve exactamente igual que un aviso que no tenía nada que decir.** No hay error, no hay rojo, no hay nada: solo falta lo único que servía para decidir. Y su pariente es el opuesto: un aviso que sale de más enseña a ignorarlo. Los dos vuelven inútil una señal sin que nadie lo note.
- **Qué lo soluciona:** ya arreglado. El lector acepta los dos órdenes del registro, versionado como **PARCHE 37.2.1**; y la comparación barata se llama `parece_vencido`, con una prueba que comprueba que no exista una que se llame como si decidiera.
- **Qué se decidió:** el usuario mandó hacer todo lo que hacía falta de la versión 3. **Ninguna de las 197 entradas del registro se reescribió**, ni ninguna fase cerrada: el que se adapta es el que lee.
- **Estado:** resuelto acá
- **Responde a:** EP-016 · HU-006 · CA-01
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-110` · `validadores/version.py` · `plataforma/nucleo/reglas/desfase.py` y `sello.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-10 · Veintiuna aprobaciones escritas a mano, y ninguna dice sobre qué texto se dio

- **Qué pasó:** este repositorio tiene **21 documentos con una marca de aprobación escrita a mano**, del estilo `| Usuario | Ing. José | ☑ |`. Ninguna dice sobre qué texto se aprobó. Y el daño no es teórico: la ficha de `F-017` cuenta que **se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor**. Nada avisó.
- **Por qué importa:** una marca parece completa cuando dice **quién** y **cuándo**. Le falta el tercer dato, que es el único que la vuelve verificable: **qué**. Sin la huella del texto, la marca dice «aprobado» para siempre, aunque debajo el documento se haya reescrito entero.
- **Qué lo soluciona:** ya hecho. `EP-017` entera, con sus tres historias: la aprobación guarda la huella, editar la caduca, y la anterior no se borra. Un documento que **desaparece** también caduca — ese es el caso que se olvida, porque nadie edita lo que borró.
- **Qué se decidió:** **las 21 marcas a mano no se migran.** Cada una diría que se aprobó un texto que hoy no se puede reconstruir, y sería inventar aprobaciones. Se quedan como están, declaradas.
- **Estado:** resuelto acá
- **Responde a:** EP-017 · HU-001 a HU-003
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-111` · `plataforma/nucleo/aprobaciones/` · `documentacion/aprobaciones/spec.md`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-11 · Dos módulos del mismo día, uno con tabla y otro sin ella, y la diferencia no es de estilo

- **Qué pasó:** Aprobaciones y Memoria se construyeron el mismo día. El primero **guarda en la base**; el segundo **no tiene ninguna entidad** y trabaja sobre los archivos que ya existen en `historico-chat/memory/`.
- **Por qué importa:** `DA-01` manda que el texto sea la verdad, y la pregunta útil para decidir no es «¿esto es importante?» sino **«¿el texto sabe la respuesta?»**. Un recuerdo dado de baja se reconoce por su marca y uno corregido por lo que quedó escrito debajo: **el texto sabe**. Quién aprobó un documento no está en ninguna parte del documento: **el texto no sabe**. Guardar de más no es neutral — una copia en la base y un archivo que cambia por fuera son dos verdades, y gana la que nadie está mirando.
- **Qué lo soluciona:** ya hecho, y quedó escrito en las dos especificaciones para que la próxima vez no se decida por costumbre.
- **Qué se decidió:** en un módulo cuyo único trabajo es no perder nada, la primera prueba que se escribe es la de que **guardar no pisa**. Es el fallo irreparable, y es el que no salta solo.
- **Estado:** resuelto acá
- **Responde a:** EP-018 · HU-001 y HU-002
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-112` · `plataforma/nucleo/memoria/core.py` · `documentacion/memoria/spec.md`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-12 · El rango de fechas de la auditoría cortaba el último día en la medianoche

- **Qué pasó:** la búsqueda de la auditoría filtra por rango. La fecha se guarda como texto con la hora pegada, así que comparar contra el `hasta` tal cual **deja por fuera todo lo registrado ese día después de la medianoche**: el último día entero.
- **Por qué importa:** un rango que pierde el día más reciente **es peor que uno que falla**, porque devuelve resultados y parecen completos. Y el último día es justo el que uno está buscando. El borde no se ve leyendo el código —leyendo parece correcto—; se ve probando con un registro de las once de la noche.
- **Qué lo soluciona:** ya arreglado, con prueba propia. En la misma función quedaron dos hermanos suyos: el resultado que se recorta **avisa que se recortó**, y los tipos de acción disponibles salen **de lo registrado**, no de una lista fija que envejecería sin avisar.
- **Qué se decidió:** el criterio pedía «menos de un segundo con un año de registros». **Se midió con lo que hay y el número que salió es el que quedó escrito**, con la advertencia de volver a medirlo cuando la auditoría real llegue a ese volumen. Un tiempo supuesto y uno medido se escriben igual; solo uno sirve.
- **Estado:** resuelto acá
- **Responde a:** EP-009 · HU-002 · CA-01 y CA-03
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-113` · `plataforma/nucleo/auditoria/busqueda.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-13 · Conviven tres modelos de tabla de estaciones, y el lector suponía uno solo

- **Qué pasó:** al leer las **209 fases** para decir en cuál estación va cada una, salió que **107 no usan la tabla de trece estaciones** —83 traen once y 24 traen menos o ninguna—, y que **76 cierran con `✅` en vez de `☑`**. Reconociendo una sola marca daban 18 fases terminadas; reconociendo las dos, 76. Y comparando la frase contra tablas de otro modelo se acusaba de contradicción a fases que hablaban de otra cosa.
- **Por qué importa:** es la cuarta vez en este proyecto que el mismo patrón aparece — **suponer que todo sigue la convención de hoy**. Y trajo una distinción nueva: **«sin marcar» no es «pendiente»**. Las fases más viejas escriben qué pasó con la estación en vez de marcarla, y decir que está pendiente inventa un estado que el documento nunca declaró.
- **Qué lo soluciona:** ya hecho. **Ninguna fase cerrada se reescribió**: el lector reconoce las dos marcas, le da nombre propio a «sin marcar», y solo compara la frase con la tabla cuando las dos hablan del mismo modelo.
- **Qué se decidió:** quedan **33 fases** cuya frase y cuya tabla no coinciden de verdad. **No se arreglan**: arreglarlas es reescribir fases cerradas, y eso no se hace.
- **Estado:** resuelto acá
- **Responde a:** EP-019 · HU-002 · CA-01
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-114` · `plataforma/nucleo/ciclo_de_vida/estaciones.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-14 · La lista que decide qué se puede apagar incluía la cadena entera del flujo de trabajo

- **Qué pasó:** para saber qué reglas puede apagar un proyecto se buscaba `*opt-in*` en cada archivo de `base/`. Daba **52 reglas opcionales**; las reales son **49**. Entre las tres que sobraban estaba **`02·F0`**, que es la cadena completa: planteamiento → épica → historia → especificación → plan → código. Las otras dos eran `R7` y `R8`, que ni siquiera son reglas: son los **ejemplos** con que el capítulo 20 explica cómo se escribe una.
- **Por qué importa:** un archivo de capítulo nombra varias reglas, y buscar la marca en el texto entero la contagia a todas. Lo grave no es la cuenta: **esa lista es justamente la que decide qué se puede apagar**. Con `F0` dentro, la plataforma habría dejado apagar la cadena entera del flujo de trabajo — el estándar convertido en sugerencia por una expresión regular ancha.
- **Qué lo soluciona:** ya arreglado, con cuatro pruebas propias. La marca vale donde está escrita: en la línea de la regla, o en la cabecera del capítulo cuando rige a todas las suyas.
- **Qué se decidió:** **ante la duda, una regla es obligatoria.** Una regla que no aparezca en la lista no se puede apagar, y una desconocida tampoco.
- **Estado:** resuelto acá
- **Responde a:** EP-008 · HU-005 · CA-02
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-115` · `plataforma/nucleo/proyectos/configuracion.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-15 · La medición inicial no se tomó, y ninguna reconstrucción la reemplaza

- **Qué pasó:** `F-032` pide medir cuánto tiempo se gasta revisando y compararlo contra un antes. **Ese antes no existe**, y la propia ficha lo advertía. Medido sobre el histórico real hay **1615 revisiones, 144 horas y una mediana de 99 segundos**, todo dentro de **un solo mes**.
- **Por qué importa:** con un mes no hay contra qué comparar. El módulo **se niega a comparar** en vez de inventar un porcentaje, y la línea base sale **siempre marcada como reconstruida**: presentarla como un antes de verdad haría que cualquier mejora futura pareciera mayor de lo que es.
- **Qué lo soluciona:** nada la reconstruye. Lo que sí se hizo fue que medir **no le cueste nada al usuario**: el tiempo sale de las horas que el enganche ya escribe, y de 3720 mensajes los **55 sin hora** se dicen aparte en vez de rellenarse.
- **Qué se decidió:** **la parte más difícil de esta funcionalidad fue una frase, no un cálculo.** Y queda la lección para el próximo proyecto: en uno que va a querer demostrar que mejoró, la primera medida se toma antes de la primera línea de código.
- **Estado:** resuelto acá, con una restricción declarada
- **Responde a:** EP-011 · HU-003 · CA-01
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-117` · `plataforma/nucleo/medicion/revision.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-16 · Cinco carpetas vacías que ni git ni una búsqueda de texto podían ver

- **Qué pasó:** el aviso de «historia sin fase», recién construido, encontró en su primera corrida **cinco carpetas vacías** de un `EP-018` con otro nombre, sobrantes de un plan anterior de la misma jornada. Se habían buscado antes sin éxito: `git status` no las mostraba, `grep` sobre todo el repositorio no daba nada, y una lectura byte a byte de todos los archivos tampoco.
- **Por qué importa:** **no aparecían en ningún archivo porque no había ningún archivo.** El control de versiones no versiona carpetas vacías y una búsqueda de texto necesita texto; lo único que las ve es algo que **recorre el disco**. Estuvieron ahí varias horas, y el validador venía proponiendo las rutas de sus documentos faltantes sin que se entendiera de dónde salían.
- **Qué lo soluciona:** se quitaron con `rmdir`, una por una. `rmdir` se niega si adentro hay algo, y esa negativa es la comprobación de que estaban vacías.
- **Qué se decidió:** cuando algo aparece en un aviso y **no aparece en ningún archivo**, la respuesta no es que el aviso mienta: es que existe algo sin contenido. Y una comprobación nueva se estrena mirando lo que ya está.
- **Estado:** resuelto acá
- **Responde a:** EP-020 · HU-001 · CA-02
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-116` · `plataforma/nucleo/avisos/core.py`
- **Nace en:** 2026-09-01 · el orden de las versiones
- **Cerrado en:** 2026-09-01 · el orden de las versiones
- **Con qué se retoma:** —

### H-17 · La columna se escribía a mano mientras el programa ya sabía la respuesta

- **Qué pasó:** el inventario declaraba **35 funcionalidades sin verificar**. Preguntado el módulo Comprobaciones, la respuesta era **31 verificadas**; arreglado un defecto de lectura, **35**. La columna llevaba semanas diciendo lo contrario de lo que la plataforma sabía.
- **Por qué importa:** el defecto de lectura es lo que vale contar. La fila de trazabilidad se buscaba exigiendo la columna del requisito y el identificador sin comillas, y **dos de las once especificaciones no la traían así** — las dos las había escrito el agente ese mismo día. Sus cuatro funcionalidades salían como «ninguna fase la construye todavía». **El módulo daba un defecto del lector con la forma de un hecho del proyecto.**
- **Qué lo soluciona:** ya hecho. El lector acepta las dos formas y ahora tiene una respuesta para «no supe leer esta fila», separada de «esto no existe». Las dos tablas de hoy se emparejaron con las nueve demás, y la columna del inventario dejó de escribirse a mano.
- **Qué se decidió:** **verificada quiere decir que la fase que la construyó cerró con veredicto Cumple**, no que alguien de afuera la haya auditado. Queda escrito debajo de la tabla, para que la columna no prometa más de lo que mide.
- **Estado:** resuelto acá
- **Responde a:** EP-015 · HU-002
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-118` · `plataforma/nucleo/comprobaciones/estado.py`
- **Nace en:** 2026-09-02 · el orden de las versiones
- **Cerrado en:** 2026-09-02 · el orden de las versiones
- **Con qué se retoma:** —

### H-18 · La mitad del backlog pedía trabajo que ya estaba hecho

- **Qué pasó:** cinco pendientes abiertos. Tres estaban marcados **hechos** dentro de su propio texto desde el 2026-08-30. Los otros dos —el `85` y el `86`, este último **P0**— pedían exactamente lo que `F-033`, `F-034` y `F-035` habían construido el 2026-08-31. Se comprobó corriendo las órdenes: el `85` pedía contar qué correcciones se repiten, y la plataforma responde que «estoy preguntando» se repitió en **8 sesiones**; el `86` pedía desconectar, reconectar, renombrar y corregir, y las cinco operaciones existen.
- **Por qué importa:** **el backlog envejece hacia arriba.** Un pendiente se escribe cuando se ve el problema y nadie lo vuelve a mirar hasta que alguien planea; mientras tanto el problema se resuelve por otro camino y el archivo sigue pidiendo. Una lista en la que uno de cada dos ya está hecho se lee entera o no se lee.
- **Qué lo soluciona:** los dos quedaron cerrados, diciendo qué los cerró y cuándo.
- **Qué se decidió:** **antes de planear trabajo nuevo, el backlog se revisa contra lo que ya existe**, no contra lo que se recuerda.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-120` · `pendientes/85-…` y `pendientes/86-…`
- **Nace en:** 2026-09-02 · el orden de las versiones
- **Cerrado en:** 2026-09-02 · el orden de las versiones
- **Con qué se retoma:** —

### H-19 · Lo que costó de cinco pantallas nuevas no fue mostrar: fue el caso vacío

- **Qué pasó:** de trece módulos, solo dos tenían pantalla. Se construyeron cinco —tablero, fases, funcionalidades, aprobaciones y memoria—, y el trabajo de verdad no estuvo en mostrar los datos sino en **los cinco casos vacíos**, que son cinco frases distintas: no tener fases no es lo mismo que no tener aprobaciones, ni que no tener memoria escrita.
- **Por qué importa:** **un proyecto recién conectado ve las cinco pantallas vacías**, y esa es la primera impresión que se lleva. Una pantalla en blanco no dice «no hay nada»: dice «esto está roto», y quien la lee así desconfía también de las que sí traen datos.
- **Qué lo soluciona:** ya hecho, con quince pruebas. Y el mismo cuidado va del otro lado: cada pantalla dice **qué deja por fuera** —las aprobaciones, que no son todos los documentos; el tablero, que «vencida» es un número puesto acá; las fases, cuáles usan otra tabla—, y esas advertencias van impresas con los datos, no en la especificación.
- **Qué se decidió:** **son pantallas de solo mirar.** Aprobar, corregir un recuerdo o abrir una fase son cambios de estado y quieren su confirmación (`00·N1`); hacerlos desde la pantalla ahora sería media confirmación. Y seis módulos siguen sin pantalla, declarados.
- **Estado:** resuelto acá
- **Responde a:** EP-021 · HU-001
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-119` · `plataforma/templates/`
- **Nace en:** 2026-09-02 · el orden de las versiones
- **Cerrado en:** 2026-09-02 · el orden de las versiones
- **Con qué se retoma:** —

### H-20 · Los 22 documentos faltantes existían, y escribirlos habría documentado trabajo sin terminar

- **Qué pasó:** el expediente decía que faltaban **22 documentos** y que había **70 huecos** en 38. Los 22 existían: la copia traída del proyecto tenía **546 documentos menos** que el disco. De los 70 huecos quedaron **2**; los otros 68 eran citas de la marca dentro de bloques de código, o marcas del propio molde, porque `expediente` contaba con `texto.count()` a secas mientras `ciclo_de_vida` ya sabía descontarlas.
- **Por qué importa:** **lo grave no era el número, sino lo que habría pasado al hacerle caso.** De esas 22 «faltas», catorce eran fases en la estación 6 de 11 —abiertas— y **cinco tenían veredicto «No cumple»**. Escribirles un `funcionalidad_implementada.md` habría documentado como terminado un trabajo que no terminó, obedeciendo a un reporte de la propia plataforma.
- **Qué lo soluciona:** ya hecho. Se trajo el proyecto de nuevo —de 1002 a 1548 documentos—, el expediente le pregunta los huecos a Ciclo de vida en vez de contarlos por su cuenta, y el validador aprendió que el molde 16 tiene dos nombres (**PARCHE 37.2.2**). Los dos huecos reales se llenaron con la propia plataforma.
- **Qué se decidió:** **antes de actuar sobre un reporte, comprobar de cuándo son los datos que lo produjeron.** Y la segunda pregunta —«si el reporte tuviera razón, ¿qué escribiría?»— es la que salvó el caso.
- **Estado:** resuelto acá
- **Responde a:** EP-012 · HU-001
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señal `S-121` · `plataforma/nucleo/expediente/core.py` · `validadores/expediente.py`
- **Nace en:** 2026-09-02 · el orden de las versiones
- **Cerrado en:** 2026-09-02 · el orden de las versiones
- **Con qué se retoma:** —

### H-21 · El acta de entrega la firman las dos partes, y son la misma persona

- **Qué pasó:** faltaban seis documentos del ciclo, los de entregar y operar. Se escribieron los cinco que faltaban de verdad —manual técnico, notas de versión, acta de entrega, bitácora de operación y plan de mantenimiento—, y al escribir el acta apareció lo que no se puede disimular: **quien entrega y quien recibe son la misma persona.**
- **Por qué importa:** un acta firmada de ida y vuelta por el mismo no prueba que el producto sirva; prueba que está terminado y que se sabe qué es. Lo mismo con la bitácora de operación, que no tiene un solo incidente: **un renglón vacío no es un sistema estable, es un sistema que nadie ha usado.** Escribir esos dos documentos como si hubiera un tercero recibiendo habría sido el peor documento del expediente.
- **Qué lo soluciona:** los cinco existen y cada uno declara su propio límite. El acta deja **la firma de recibido en blanco**: marcarla desde acá sería que el agente firme por el usuario.
- **Qué se decidió:** **un documento sin materia existe igual y dice por qué no la tiene.** Uno ausente y uno vacío no se distinguen desde afuera; uno que declara su límite sí.
- **Estado:** resuelto acá
- **Responde a:** el ciclo de vida del proyecto
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** `cvds/despliegue/` y `cvds/mantenimiento/`
- **Nace en:** 2026-09-02 · el orden de las versiones
- **Cerrado en:** 2026-09-02 · el orden de las versiones
- **Con qué se retoma:** —


### H-22 · El aplazamiento que se levantó, y el hueco que la propia funcionalidad había dejado abierto

- **Qué pasó:** al leer el manual de uso, el usuario respondió a la frase «no hay usuarios ni permisos, confía en quien lo abre»: **«el que yo lo use no significa que no pueda tener seguridad»**. La revisión mostró que el agente había contado un **aplazamiento** como si fuera una **postura**, y que el aplazamiento tenía condición escrita: *«con dos usuarios, es una falla»*. El usuario decidió levantarlo antes de esa fecha y mandó construirlo con `django.contrib.auth`.
- **Por qué importa:** al construirlo apareció algo peor que la falta de login. **`aprobar --quien "cualquier cosa"` aceptaba cualquier texto**: la funcionalidad que existía justamente para que una aprobación dijera **sobre qué texto** se dio, seguía dejando que dijera **quién** sin probarlo. Una funcionalidad puede tapar un hueco y dejarlo abierto en su propia puerta de entrada.
- **Qué lo soluciona:** ya hecho. `EP-022`, con dos historias: ninguna pantalla responde sin haber entrado, y dos grupos con sus permisos. **El guardián va como middleware y no como decorador por vista**, para que una pantalla nueva nazca protegida; y la prueba recorre **las rutas del propio enrutador**, no una lista escrita a mano.
- **Qué se decidió:** **dos grupos y no cuatro.** De los cuatro actores del análisis, dos no entran: un proyecto administrado es una carpeta, y quien recibe un proyecto tiene escrito que no puede entrar. Y **catorce pruebas que se pusieron en rojo fueron la comprobación, no el daño**: aprobaban con nombres inventados.
- **Estado:** resuelto acá
- **Responde a:** EP-022 · HU-001 y HU-002
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** señales `S-124` y `S-125` · `plataforma/nucleo/acceso/` · `cvds/diseno/README.md` §8 · pendiente 94, cerrado
- **Nace en:** 2026-09-02 · el orden de las versiones
- **Cerrado en:** 2026-09-02 · el orden de las versiones
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ no quedó ninguno abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguna quedó sin escribir |
| Lo que se hizo está aprobado y guardado | ☐ subidas las versiones 4, 5 y las pantallas; falta el commit del expediente |

**Falta guardar, y con eso se cierra.** Lo que la sesión vino a hacer quedó hecho: `EP-013` nació y **cerró el mismo día** con sus dos historias, el módulo Ciclo de vida tiene especificación, y con él `F-014` queda completa. **Con `F-014` cierra la versión 2.**

**Y la versión 3 arrancó**, por `F-031`, que era lo único con daño irreversible y estaba construido a medias sin que nadie lo hubiera declarado.

**Y `EP-015` cerró entera:** con `F-022` la vuelta de la columna queda cerrada, porque publicar una versión ya tiene su puerta.

**Y las reglas cerraron enteras:** `EP-016` nació con sus seis funcionalidades y las seis quedaron construidas el mismo día. **Con ellas cierra la versión 3.**

**Y la versión 4 cerró entera:** `EP-017` con las aprobaciones que dicen sobre qué texto, `EP-018` con la memoria que se ve y se corrige, y `EP-009` completa por fin — registrar y consultar, las dos mitades. **Seis funcionalidades, tres épicas, tres hallazgos.**

**Y la versión 5 cerró entera:** `EP-019` con el ciclo operable —abrir una fase, ver en cuál estación va, y no dejar pasar la puerta que falta—, `EP-020` con los avisos y el reporte, `EP-008` con la configuración por proyecto y `EP-011` con la medición del tiempo de revisión. **Siete funcionalidades, cuatro hallazgos, y las cinco versiones del plan cerradas el mismo día en que se decidió el orden.**

**Y después de subir la 5, el usuario preguntó «qué sigue» y mandó hacer los tres frentes de una.** Los tres salieron más chicos de lo que parecían, y por la misma razón: **lo que se escribe a mano al lado de lo que un programa deriva termina diciendo otra cosa.** Las 35 funcionalidades «sin verificar» eran 0 —la columna estaba vieja, y el lector tenía un defecto—; los cinco pendientes abiertos eran dos, y a los dos los había cerrado la plataforma sin que nadie lo anotara; y de once módulos sin pantalla, cinco ya la tienen.

**Y al preguntar si ya se había terminado, la respuesta fue que no: el software estaba construido y el proyecto no estaba entregado.** Faltaban 22 documentos, 70 huecos y seis documentos del ciclo. **Los 22 existían** —la copia traída tenía 546 documentos menos que el disco—, **68 de los 70 huecos eran citas de la marca**, y de los seis documentos uno ya estaba escrito con otro nombre. Quedaron cinco por escribir, y se escribieron. **El expediente: 1290 documentos, cero faltantes, cero a medio llenar.**

**Lo que queda, declarado:** seis módulos siguen sin pantalla —Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén—, nada se cambia desde la pantalla y así se quiso, y hay 33 fases cuya frase y cuya tabla no coinciden porque arreglarlas sería reescribir fases cerradas. Y una que no tiene arreglo: la medición inicial, que son las aprobaciones, la memoria y operar el ciclo. Y una pregunta que quedó viva sin ser un hallazgo: si llenar por huecos resulta cómodo. Hoy el documento con más huecos tiene dos, y eso no lo responde.
