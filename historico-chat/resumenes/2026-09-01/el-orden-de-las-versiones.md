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

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ no quedó ninguno abierto |
| Toda historia disparada está escrita en su épica | ☑ ninguna quedó sin escribir |
| Lo que se hizo está aprobado y guardado | ☐ falta el commit de las cuatro últimas de Reglas |

**Falta guardar, y con eso se cierra.** Lo que la sesión vino a hacer quedó hecho: `EP-013` nació y **cerró el mismo día** con sus dos historias, el módulo Ciclo de vida tiene especificación, y con él `F-014` queda completa. **Con `F-014` cierra la versión 2.**

**Y la versión 3 arrancó**, por `F-031`, que era lo único con daño irreversible y estaba construido a medias sin que nadie lo hubiera declarado.

**Y `EP-015` cerró entera:** con `F-022` la vuelta de la columna queda cerrada, porque publicar una versión ya tiene su puerta.

**Y las reglas cerraron enteras:** `EP-016` nació con sus seis funcionalidades y las seis quedaron construidas el mismo día. **Con ellas cierra la versión 3.**

**Lo que sigue no es de esta sesión:** las versiones 4 y 5, que son las aprobaciones, la memoria y operar el ciclo. Y una pregunta que quedó viva sin ser un hallazgo: si llenar por huecos resulta cómodo. Hoy el documento con más huecos tiene dos, y eso no lo responde.
