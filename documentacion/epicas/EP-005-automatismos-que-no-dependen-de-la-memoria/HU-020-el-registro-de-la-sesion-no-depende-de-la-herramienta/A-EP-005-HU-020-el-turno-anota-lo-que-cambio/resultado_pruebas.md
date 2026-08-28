# Resultado de Pruebas — Fase `A-EP-005-HU-020-el-turno-anota-lo-que-cambio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el [estado-fase.md](estado-fase.md) para pasar la puerta de verificación, y la fuente de la sección «qué se probó» del [funcionalidad_implementada.md](funcionalidad_implementada.md). El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-020-el-turno-anota-lo-que-cambio` |
| **HU** | [HU-020](../HU-020-el-registro-de-la-sesion-no-depende-de-la-herramienta.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-28 |
| **Ejecutado por** | El agente, sobre este repositorio |
| **Ambiente y versión** | Windows 11 · Python 3.11 · git de verdad · Cimiento `35.8.0` |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**Se ejecutaron ocho, no siete.** El plan §5 lista `CP-000` a `CP-007`; la tabla de prioridades solo numeraba los siete que quedan al descontar el previo. `CP-000` se corrió igual, porque es el que autorizaba a tocar el registro.

---

## 2. Ejecución caso por caso

### CP-000 — Las pruebas del registro admiten más contenido

**El problema que resuelve:** si alguna prueba fija **exactamente** qué contiene el registro, agregarle entradas la rompe, y eso se descubre a mitad de camino en vez de antes de empezar.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar las pruebas que miran el registro: `grep -n "tocado\|leer_sesion\|registros(" validadores/pruebas.py` | Se listan | 11 apariciones, todas en la clase `ElCommitNoSeLlevaLoAjeno` |
| 2 | Leer cada una y ver si fija exactamente el contenido | **Ninguna debería** | Todas usan `assertIn` sobre un archivo concreto o cuentan hallazgos; **ninguna compara el conjunto completo** |
| 3 | Si alguna lo hace, parar y decidir | — | No hizo falta |

**Cómo se verificó que la pareja cumple:** decide el paso 2, y lo que lo hace concluyente es que se leyeron **las 11**, no una muestra. El paso 1 deja el comando escrito para que otro llegue al mismo listado.

---

### CP-001 — Lo escrito con un guion queda registrado

**El problema que resuelve:** el registro se llenaba solo desde las herramientas de escritura, y casi todos los archivos de este repositorio los escriben guiones que se corren en la terminal. Por ese hueco entraron 712 líneas ajenas a un commit sin que nadie lo viera.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear un repositorio de git de verdad, con `user.name` y `user.email` **locales** | Queda inicializado | Quedó, en una carpeta temporal que la prueba borra |
| 2 | Correr `anotar_el_turno(raiz, "s1")` para arrancar el reloj | Se crea `historico-chat/.tocado/s1.txt` | Se creó |
| 3 | Escribir `del-guion.md` **con `io.open`, no con las herramientas de escritura**, con fecha posterior al reloj | El archivo queda escrito | Quedó |
| 4 | Correr `anotar_el_turno(raiz, "s1")` otra vez | — | Devolvió `['del-guion.md']` |
| 5 | Leer el registro de la sesión | **El archivo está** | Está |
| 6 | Repetir con un archivo nuevo, **sin seguimiento de git todavía** | También está | Está: `git status` lo entrega como `??` y se anota igual |

**Cómo se verificó que la pareja cumple:** decide el paso 5, y el 6 es el que importa de verdad — **los dos moldes que causaron el daño eran archivos nuevos**, y un programa que solo mirara lo ya versionado los habría dejado pasar. El paso 3 escribe sin las herramientas a propósito: probarlo con ellas habría probado lo que ya funcionaba.

Pruebas: `test_lo_escrito_sin_las_herramientas_queda_anotado`, `test_un_archivo_nuevo_sin_seguimiento_tambien_se_anota`.

---

### CP-002 — No se reclama lo que no se tocó en el turno   ·   **crítico**

**El problema que resuelve:** si el registro reclama lo que ya estaba sucio, la primera conversación del día se atribuye el proyecto entero, y la comprobación pasa de callar siempre a hablar siempre. **El ruido apaga también lo que servía**, así que sería peor que no hacer nada.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Repositorio nuevo; arrancar el reloj con una primera vuelta | Se crea el registro | Se creó |
| 2 | Escribir `viejo.md` con fecha **una hora anterior** al reloj | Queda sucio para git | Quedó, `git status` lo da como `??` |
| 3 | Correr `anotar_el_turno` | `viejo.md` **no entra** al registro | No entró |
| 4 | En otro repositorio, dejar **cinco** archivos sucios y correr la **primera** vuelta | **No se reclama nada** | Devolvió `[]`, y el registro quedó vacío |
| 5 | Comprobar que aun así quedó el reloj puesto | El archivo del registro existe | Existe, vacío |
| 6 | Con el reloj puesto, escribir uno **antes** y uno **después** de su hora, y correr | Entra solo el de después | Entró `despues.md`; `antes.md` no |
| 7 | Contar cuántos entrarían sobre el árbol real | Un puñado, no decenas | Se midió en `CP-006`, sobre doce commits |

**Cómo se verificó que la pareja cumple:** decide el paso 4, no el 3. El 3 comprueba el filtro por fecha, que es lo fácil; **el 4 comprueba el caso que se cuela**, que es la primera vuelta, cuando no hay fecha anterior contra la cual comparar y un programa ingenuo se lo lleva todo. El paso 5 existe porque la salida obvia al 4 —no hacer nada la primera vez— dejaría el registro sin arrancar nunca.

Pruebas: `test_no_reclama_un_archivo_de_antes_del_turno`, `test_la_primera_vuelta_no_reclama_el_arbol_entero`, `test_la_primera_vuelta_deja_el_reloj_puesto`, `test_solo_entra_lo_modificado_despues_del_reloj`.

---

### CP-003 — Dos sesiones que tocan lo mismo producen colisión

**El problema que resuelve:** es el caso que causó el daño. Si no se ve acá, la fase no sirvió para lo que se abrió.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Anotar el mismo archivo en dos registros de sesión distintos, `s1` y `s2` | Los dos lo tienen | Los dos |
| 2 | `git add compartido.md` | Entra al commit | Entró |
| 3 | Correr `validar_preparados` | **Avisa**, y nombra el archivo | Un hallazgo: «este commit mezcla archivos de 2 sesiones... empieza por `compartido.md`» |
| 4 | **Reproducir el caso real:** una sesión escribe `manual-a.md` y `manual-b.md` en su turno; otra sesión toca `manual-a.md` en el suyo; `git add -A` | Avisa | Avisó, un hallazgo |

**Cómo se verificó que la pareja cumple:** decide el paso 4. El 3 monta la colisión a mano —los registros escritos directamente—, así que prueba la comprobación, no el arreglo. **El 4 la monta por el camino nuevo**: los dos registros salen de `anotar_el_turno`, sin que la prueba escriba en ellos. Es la única forma de saber que el registro nuevo alimenta la comprobación vieja.

Pruebas: `test_dos_sesiones_con_el_mismo_archivo_avisan`, `test_el_caso_real_una_sesion_escribe_y_otra_commitea`.

---

### CP-004 — No se duplica lo que ya estaba

**El problema que resuelve:** el registro tenía una fuente y ahora tiene dos. Si se suman en vez de fundirse, cada archivo escrito con las herramientas queda dos veces y los conteos del aviso mienten.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Arrancar el reloj y escribir `doble.md` dentro de la ventana | — | Escrito |
| 2 | Anotarlo con `anotar`, como hace el enganche de escritura | Entra al registro | Entró |
| 3 | Correr `anotar_el_turno`, que lo ve cambiado | — | Corrió |
| 4 | Leer el archivo del registro **crudo** y contar las apariciones | **Una sola vez** | Una |
| 5 | Comprobar que no se perdió nada de lo anterior | Todo sigue | Sigue: las pruebas de `ElCommitNoSeLlevaLoAjeno` en verde |

**Cómo se verificó que la pareja cumple:** decide el paso 4, y se lee el archivo **crudo** —no `leer_sesion`, que devuelve un conjunto y borraría el duplicado antes de que se pudiera contar. Es el error que más se repite en esta casa: preguntarle a la función que ya arregla lo que se quería medir.

Prueba: `test_no_duplica_lo_que_la_herramienta_ya_anoto`.

---

### CP-005 — Un fallo del enganche no rompe el turno

**El problema que resuelve:** cuando esto corre, la respuesta ya se dio. Lo único que puede lograr un fallo es alarmar sin motivo, y un automatismo que rompe la conversación se desinstala el mismo día.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `cambios_del_turno` sobre una carpeta **que no es repositorio de git** | Devuelve vacío, sin afirmar nada | `[]` |
| 2 | Correr el enganche con entrada **vacía** | Termina en 0 y calla | 0, sin salida |
| 3 | Correr el enganche con entrada **que no es JSON** | Termina en 0 y calla | 0, sin salida |
| 4 | Correr el enganche con `[]` —JSON válido que no es un objeto | Termina en 0 y calla | 0, sin salida |
| 5 | Correr el enganche con una carpeta **inexistente** como `cwd` | Termina en 0, calla, **y no la crea** | 0, sin salida, y la carpeta no existe |
| 6 | Correr `anotar_el_turno` sin identificador de sesión | No hace nada, ni crea carpeta | `[]`, y no se creó `.tocado` |

**Cómo se verificó que la pareja cumple:** el paso 5 es el que se ganó su fila. La primera versión usaba `/no/existe`, que en Windows apunta a la raíz del disco y falla por permisos: **habría pasado sin probar nada**. Con una carpeta temporal inexistente sí se puede crear, y ahí se vio que el programa la creaba — escribir fuera de todo proyecto, contra `04·S9`. Se corrigió con una guardia, y el paso 5 la vigila.

Pruebas: `test_sin_git_no_revienta_y_no_anota`, `test_sin_sesion_no_hace_nada`, `test_el_enganche_calla_y_sale_bien_con_entrada_rota`.

---

### CP-006 — Cuánto hablaría la comprobación con el registro nuevo   ·   **el que podía tumbar la fase**

**El problema que resuelve:** un arreglo que cambia un silencio inútil por un ruido inútil **es peor que no hacerlo**.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `python historico-chat/scripts/2026-08-28/t06-cuanto-hablaria.py` | Recorre los últimos doce commits | Recorrió 12 |
| 2 | Contar en cuántos coincidirían **dos** sesiones sobre el mismo archivo | **Menos de seis** | **0 de 12** |
| 3 | Comparar con el diseño descartado | Mejor, y dicho con el número | El descartado avisaba en **7 de 12**, con hasta 31 archivos de una vez |

**Cómo se verificó que la pareja cumple:** decide el paso 2, y **el número hay que leerlo con su límite**, que el guion imprime: hoy hay **una sola sesión viva**, así que el cero no prueba que las colisiones se vean — prueba que **no avisa por falta de registro**, que era exactamente el defecto del diseño descartado. Que las colisiones sí se vean lo prueba `CP-003` paso 4. Esa división es deliberada: ninguna de las dos alcanza sola.

---

### CP-007 — El enganche está colgado

**El problema que resuelve:** en `EP-002·HU-004` un aviso quedó construido, probado, en verde — y nadie lo llamaba.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar `hook_turno.py` en `instalar.HOOKS_CLAUDE` | Está, como enganche de `Stop` | Está |
| 2 | Que una prueba lo busque **en la lista del instalador**, no en el disco | Está | `test_el_enganche_esta_registrado_en_el_instalador` |
| 3 | Cambiarle el nombre en el instalador y correr las pruebas | Fallan | Fallaron: 1 falla |

**Cómo se verificó que la pareja cumple:** decide el paso 3, no el 1. Mirar la lista solo prueba que el nombre está escrito; **el sabotaje prueba que alguien lo está mirando.** Un archivo existente y una prueba que no lo comprueba dan el mismo verde.

---

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-000 | Previo | — | 2026-08-28 | `grep -n "tocado\|leer_sesion\|registros("` sobre `pruebas.py`: 11 apariciones, ninguna fija el conjunto completo | Aprobado | EV-01 | — |
| CP-001 | CA-01 | Alta | 2026-08-28 | `anotar_el_turno` devolvió `['del-guion.md']` tras escribirlo con `io.open`; el archivo sin seguimiento también entró | Aprobado | EV-02 | — |
| CP-002 | CA-02 | **Crítica** | 2026-08-28 | `viejo.md` (una hora antes) no entró; con cinco sucios, la primera vuelta devolvió `[]` y dejó el reloj puesto | Aprobado | EV-02 | — |
| CP-003 | CA-03 | Alta | 2026-08-28 | dos turnos reales sobre `manual-a.md`; `validar_preparados` devolvió 1 hallazgo nombrándolo | Aprobado | EV-02 | — |
| CP-004 | CA-04 | Media | 2026-08-28 | `doble.md` anotado por las dos vías: el archivo crudo del registro lo trae **una** vez | Aprobado | EV-02 | — |
| CP-005 | CA-05 | Media | 2026-08-28 | cuatro entradas rotas al enganche: 0 y sin salida en las cuatro; la carpeta inexistente **no** se creó | Aprobado | EV-02 | DEF-01 |
| CP-006 | Transversal | **Crítica** | 2026-08-28 | `t06-cuanto-hablaria.py` sobre 12 commits: **avisaría en 0**, contra 7 del diseño descartado | Aprobado | EV-03 | — |
| CP-007 | CA-01 · conexión | Media | 2026-08-28 | `hook_turno.py` en `HOOKS_CLAUDE`; renombrarlo en el instalador tumba las pruebas | Aprobado | EV-04 | — |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada en el ciclo 1. Los defectos de §4 salieron **antes** del ciclo, del guion de sabotaje.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el enganche anota lo escrito por un guion **en este repositorio de verdad**, no solo en uno temporal | `T-08`: dos turnos seguidos, con un archivo escrito desde la terminal entre medias | Turno 1 arrancó el reloj sin reclamar nada; turno 2 anotó `del-guion.md` y **no** el archivo viejo que estaba sucio |
| 2 | Que ninguna prueba escribe en el registro real del repositorio | Correr la clase entera y mirar `historico-chat/.tocado/` antes y después | Sin cambios: todas usan carpetas temporales |
| 3 | Que los sabotajes se cazan | `python historico-chat/scripts/2026-08-28/sabotajes-hu020.py` | **7 de 7 cazados**, tras corregir los dos que se colaron |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | El enganche **creaba** la carpeta del registro en una raíz que no existe: escribía fuera de todo proyecto | Sabotaje «escribe en una raíz que no existe» | **Alta** (`04·S9`) | Corregido y verificado | Guardia `if not os.path.isdir(raiz)` en `anotar_el_turno`, vigilada por `CP-005` paso 5 |
| DEF-02 | Un `os.utime` que no hacía nada: el archivo se acababa de crear y ya traía la hora | Sabotaje «no arranca el reloj», que **se coló** | Baja | Corregido | Se quitaron las tres líneas; el sabotaje se apuntó al renglón que sí decide |
| DEF-03 | Una aserción quedó pegada en la prueba de **otro** enganche, donde su variable ni existía | Revisión al depurar DEF-01 | Media | Corregido | Se movió a su prueba |

**Defectos abiertos que se aceptan y por qué:** ninguno. Los tres quedaron corregidos y verificados dentro del ciclo 1.

**DEF-03 se habría escapado.** Corrí la clase sola, y el error vivía en otra: **una clase en verde no dice nada sobre las de al lado**. Lo destapó el sabotaje que «se coló» sin razón aparente.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 — lo escrito fuera de las herramientas queda registrado | CP-001, CP-007 | Anota lo escrito por un guion, versionado o nuevo, y el enganche está colgado | Sí |
| CA-02 — no se reclama lo que no se tocó en el turno | CP-002, CP-006 | Ni lo viejo ni el árbol entero en la primera vuelta; 0 de 12 commits harían ruido | Sí |
| CA-03 — dos sesiones que tocan lo mismo producen colisión | CP-003 | El caso real, montado por el camino nuevo, produce el aviso | Sí |
| CA-04 — lo que ya se registraba se sigue registrando | CP-004, CP-000 | Una sola vez en el registro; las pruebas anteriores siguen en verde | Sí |
| CA-05 — un fallo del enganche no rompe el turno | CP-005 | Seis entradas malas, seis salidas en 0 y calladas | Sí |
| RNF-01 — rendimiento | CP-006 | Se apoya en `git status`, sin recorrer el árbol; la clase entera corre en ~5 s con repositorios reales | Sí |
| RNF-02 — no estorbar | CP-005 | No escribe salida en ninguna entrada, ni cuando falla | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100% | 5 CA y 2 RNF, todos con caso ejecutado | Sí |
| Casos críticos ejecutados | Plan §3.2 | 100% | `CP-002` y `CP-006`, los dos | Sí |
| Casos ejecutados | Plan §12 | 7 de 7 | 8 de 8 | Sí |
| **Archivos de antes del turno que se reclaman** | Plan §12 | **0** | **0** | Sí |
| **Commits en que avisaría, de los últimos doce** | Plan §12 | menos de 6, con el número | **0**, y dicho con su límite | Sí |
| Turnos rotos por el enganche | Plan §12 | 0 de 4 | 0 de 4 | Sí |
| Entradas duplicadas en el registro | Plan §12 | 0 | 0 | Sí |
| Sabotajes cazados | Plan §12 | Todos | 7 de 7 | Sí |
| Fallas en la suite completa | Plan §12 | 0, con conteo distinto de cero | **515 pruebas, 0 fallas** (4 esperadas, declaradas de antes) | Sí |
| Criterios de salida | Plan §4.2 | Todos | Los cinco | Sí |
| Criterios de suspensión | Plan §4.3 | Ninguno alcanzado | Ninguno: 0 archivos viejos reclamados, 0 commits con ruido, 0 turnos rotos | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**

**Justificación:** los cinco criterios y los dos requisitos no funcionales quedaron cubiertos por casos ejecutados (§5), las metas del plan se alcanzaron (§5.1) y ninguno de los tres criterios de suspensión se acercó. **El que decidía si la fase tenía sentido era `CP-006`**, escrito para poder tumbarla: avisaría en **0 de 12** commits, contra los **7 de 12** del diseño que se descartó. Los tres defectos salieron del sabotaje y de la revisión que provocó, no del ciclo, y los tres quedaron corregidos y verificados.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Búsqueda de las pruebas del registro | `grep -n "tocado\|leer_sesion\|registros(" validadores/pruebas.py` |
| EV-02 | Las 15 pruebas de la fase | `validadores/pruebas.py`, clase `ElTurnoAnotaLoQueCambio` |
| EV-03 | Medición del ruido sobre doce commits | [t06-cuanto-hablaria.py](../../../../../historico-chat/scripts/2026-08-28/t06-cuanto-hablaria.py) |
| EV-05 | Salida de la suite completa | [salida-suite.txt](../../../../../historico-chat/scripts/2026-08-28/salida-suite.txt) |
| EV-04 | Los siete sabotajes y su salida | [sabotajes-hu020.py](../../../../../historico-chat/scripts/2026-08-28/sabotajes-hu020.py) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-28 | 8 | 0 | Primera ejecución |
