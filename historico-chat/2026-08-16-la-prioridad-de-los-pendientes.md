<!-- sesion: f6fdedcf-068a-4573-8f8d-b23dfbc3117a -->
<!-- nombre: preguntado -->

# 2026-08-16 — La prioridad de los pendientes

## Conversación

### 1 · Usuario — 2026-08-16 12:09:16
> analice la carpeta pendientes dele un orden de prioridad cada uno

**Agente** — 2026-08-16 12:13:16
<!-- agente: 18eb2bfb-2a81-4039-8094-d5f37d7696bb -->

Leí los 28 abiertos (+ el README y los puntos internos del 09 y el 33). El criterio con que ordeno: **qué está causando daño hoy** > **qué afirma algo falso** > **qué es barato y evita rehacer trabajo** > **qué falta decidir** > **limpieza** > **cobertura nueva**.

Dos cosas antes de la tabla:

- El [README](pendientes/README.md) dice *«el número es el orden, no la prioridad»* — o sea que hoy no hay prioridad escrita en ninguna parte, y trabajar por número deja de últimos justo a los tres que más duelen.
- El [33](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) no es un pendiente, son ocho, con costos que van de una línea de código a revisar proyecto por proyecto. Lo desarmo: su punto 6 es lo primero de todo el backlog, y su punto 8 es lo último.

---

## P0 · Se está perdiendo algo, o se sigue produciendo el daño

| # | Pendiente | Por qué acá | Costo |
|---|---|---|---|
| **1** | [33 · punto 6](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) — a qué proyectos les borró la memoria el enganche | Es lo único del backlog donde **hay información que no está en ninguna otra parte**. En agro-system se recuperó del último commit; de los demás no se sabe. Cada día que pasa hay más commits encima. | Horas |
| **2** | [34](pendientes/34-las-plantillas-enlazan-una-carpeta-base-que-el-proyecto-no-tiene.md) — las plantillas enlazan una `base/` que el proyecto no tiene | **Cada proyecto nuevo nace roto**, y el efecto real no son los 14 enlaces: es que `hook_md.py` queda siempre en rojo y se deja de leer. En shopnest-mesa ya se perdieron fallas reales por eso. El marcador `«RUTA-ESTANDAR»` ya existe: es buscar y reemplazar. | Bajo |
| **3** | [29 · punto 2](pendientes/29-la-transcripcion-se-escribio-dos-veces.md) — que el `CLAUDE.md` deje de pedir lo que el enganche ya hace | **La causa sigue viva.** Mientras la §1 mande escribir la transcripción a mano, cualquier sesión vuelve a duplicarla. Ya pasó 6 veces (1 + 4 encontradas + 1 borrada en caliente). Son dos párrafos. | Muy bajo |
| **4** | [36](pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md) — la regla de reportar al estándar | Es el de fondo del 34 y el 35: llegaron acá por criterio de una sesión, no por norma. Sin el paso 6 (el aviso de vuelta), cada pendiente reportado deja uno abierto para siempre en el proyecto. El usuario ya dictó el procedimiento completo. | Medio |

## P1 · El estándar afirma algo que no es cierto

| # | Pendiente | Por qué acá | Costo |
|---|---|---|---|
| **5** | [30](pendientes/30-el-checklist-no-ve-la-cadena.md) — el checklist no ve la cadena | El arranque dice «13 de 13, instalación completa» sobre un proyecto con código commiteado, `prompts/` vacía y ninguna épica. Es el mensaje que el agente lee en **cada mensaje**. | Medio |
| **6** | [27](pendientes/27-la-fase-a-de-hu-010-cerro-sin-cumplir.md) — la fase A de HU-010 cerró sin cumplir | Hay una fase cerrada cuyo veredicto real es «No cumple». Bloquea al 28. Ojo: CP-006 necesita **una persona que no escribió el glosario**, y eso no lo agenda el agente. | Medio-alto |
| **7** | [28](pendientes/28-el-veredicto-de-la-fase-vive-en-dos-sitios.md) — el veredicto en dos sitios | La puerta de verificación lee el `estado-fase`, que es la copia que nadie actualiza. Va justo después del 27, que es el caso que lo destapó. | Medio |
| **8** | [19](pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) + [33 · punto 7](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) — el capítulo 20 no se cumple a sí mismo | 7 reglas publicadas en «no cumple» cuando `M14` lo prohíbe, 33 sin clasificar, 129 sin checklist. El punto 7 del 33 es el mismo agujero por el otro lado: el sello caduca con el texto y nada lo comprueba. **Partirlo:** clasificar las 33 es una tarde; las 129 es trabajo largo, por capítulo. | Alto (divisible) |

## P2 · Barato, y evita volver a hacer el mismo trabajo

| # | Pendiente | Por qué acá | Costo |
|---|---|---|---|
| **9** | [32](pendientes/32-la-carpeta-del-dia-nace-sin-su-linea-en-el-indice.md) — la carpeta del día sin su línea en el índice | Perdió su ventana (los 33 resúmenes ya se anotaron a mano), pero el próximo día vuelve a nacer fuera del índice. | Bajo |
| **10** | [35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) — renombrar rompe el enlace del resumen | Nombre fijo, archivo conocido, el nombre nuevo ya está calculado. Es el más barato de los que vienen de un proyecto. | Muy bajo |
| **11** | [33 · punto 5](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) — la prueba que protege el `GATE` del arranque | Una prueba. Protege la puerta que detiene el arranque, que ya desapareció en silencio una vez y las 191 pruebas no lo vieron. | Muy bajo |
| **12** | [33 · punto 1](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) — `unquote` en `enlaces.py` | Una línea. Falsos positivos en el validador que más se corre. | Muy bajo |
| **13** | [33 · punto 4](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) — renombrar rompe los enlaces de fuera | Ya dejó 41 enlaces rotos arreglados a mano. `citas.py` ya tiene el modo reparar: es reusarlo. Hermano del 35. | Bajo |
| **14** | [23](pendientes/23-plantillas-mezcla-modelos-con-procedimientos.md) — mover `retrodocumentacion.md` al capítulo 13 | Ya está decidido qué se hace y con los otros tres archivos ya se resolvió que se quedan. Solo falta ejecutarlo. | Muy bajo |
| **15** | [29 · punto 1](pendientes/29-la-transcripcion-se-escribio-dos-veces.md) — limpiar la transcripción del 2026-08-15 | Mecánico: se distinguen por la marca `<!-- agente: … -->`. Va después del punto 2, o se vuelve a ensuciar. | Bajo |

## P3 · Falta una decisión escrita (nadie puede construir hasta que se decida)

| # | Pendiente | Por qué acá |
|---|---|---|
| **16** | [13](pendientes/13-inventario-y-riesgo-de-las-acciones-del-agente.md) — inventario y riesgo de las acciones | Es una lista y una tabla, y **desbloquea dos**: el ítem 15 del 09 y toda la clasificación de riesgo del 12. Lo más rentable del P3. |
| **17** | [24](pendientes/24-buscar-en-el-repositorio-antes-de-preguntar.md) — buscar antes de preguntar | La HU ya está redactada en el propio pendiente. Es conducta del agente en cada sesión: rinde todos los días. |
| **18** | [20](pendientes/20-f2-no-dice-cuando-no-aplica.md) — `F2` no dice cuándo no aplica | **Va junto con el 5 (el 30):** las dos son reglas de cadena que la práctica salta con buenos motivos. Dos fases ya se abrieron sin especificación; a la tercera es costumbre. |
| **19** | [22](pendientes/22-dos-sesiones-versionando-a-la-vez.md) — dos sesiones versionando a la vez | Ya produjo dos numeraciones vivas en un día. No lo resuelve un validador: hace falta el acuerdo, y son tres opciones sobre la mesa. |
| **20** | [16](pendientes/16-primero-que-el-proceso-sirva-despues-se-automatiza.md) — primero que el proceso sirva | **Se resuelve escribiéndolo**, no construyendo nada. Y es puerta del 09: sin este criterio, promover ítems del 09 es apostar. |
| **21** | [17](pendientes/17-las-senales-no-tienen-donde-escribirse.md) — las señales no tienen dónde escribirse | El archivo ya existe; falta el enganche y bajar la plantilla de 7 campos a 4. Mismo patrón que ya funcionó con el histórico. |
| **22** | [14](pendientes/14-las-reglas-no-tienen-fecha-de-revision.md) — las reglas no tienen fecha de revisión | Real, pero con 188 reglas de 10 días de antigüedad todavía no hay nada vencido. Gana valor con el tiempo, no ahora. |

## P4 · Limpieza de texto ya escrito (grande, mecánica, no bloquea nada)

| # | Pendiente | Nota |
|---|---|---|
| **23** | [18](pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md) — 354 enlaces `DOC14` | `F21` ya cortó el crecimiento: la cuenta no sube. Unos 200 reales. Decidir primero si el validador entra a la corrida diaria. |
| **24** | [21](pendientes/21-el-glosario-y-los-terminos-en-ingles.md) — los 12 términos que siguen en inglés | El glosario (su mitad cara) ya está hecho y dejó el inventario. Va de una vez, con HU y plan, porque renombrar archivos rompe enlaces. |
| **25** | [26](pendientes/26-corrida-y-ejecucion-en-el-estandar.md) — «corrida» vs «ejecución» | El propio pendiente dice «no urge». Conviene hacerlo **con el 24**: es el mismo tipo de cambio de vocabulario en los mismos archivos. |
| **26** | [11](pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md) — marcadores de IA en `base/` y `plantillas/` | **Bloqueado de hecho:** sin el validador mecánico de `ID8`, el recuento sobre 200 archivos es inabordable. No moverlo hasta que exista el script. |

## P5 · Construcción grande — cuando haya quien lo pida

| # | Pendiente | Nota |
|---|---|---|
| **27** | [01](pendientes/01-validadores-de-codigo-de-proyecto.md) — validadores de código de proyecto | Los 9 que faltan necesitan que el proyecto declare su convención en `.agente/`, y eso no existe. **La precondición es el ítem 04 del 09** (manifiesto de convenciones): sin él, cinco de los nueve no tienen contra qué comparar. |
| **28** | [09](pendientes/09-autonomia-sin-ia.md) — autonomía sin IA | No es un ítem, son 16. Sus tres de prioridad alta y costo bajo —**01 guardián de versión, 02 secretos en el histórico, 03 sello de puerta**— valen más que la mitad del P3 y podrían subir si se promueven. Pasan primero por el filtro del 16. |
| **29** | [15](pendientes/15-el-estandar-depende-de-una-sola-herramienta.md) — dependencia de Claude Code | Su punto 1 (el mapa en `anatomia/`) es una tarde y deja el resto decidible; los puntos 2 y 3 son abstracción prematura. **Subir solo el punto 1.** |

## P6 · Cobertura opt-in sin demanda hoy

| # | Pendiente | Nota |
|---|---|---|
| **30** | [12](pendientes/12-patron-ia.md) — patrón IA | Bien escrito y casi listo para redactarse. Se adelanta el día que haya un proyecto de IA. Reusa la tabla del 13. |
| **31** | [08](pendientes/08-patrones-rpa.md) — patrón RPA | Igual, sin proyecto que lo pida. |
| **32** | [10](pendientes/10-ideas.md) — ideas | Libreta. Su idea 1 (que lo del posgrado entre al estándar) ya está produciendo: de ahí salieron el 12 al 16. |
| — | [33 · punto 8](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) — doce huecos chicos | Casi todos son «decidir algo». **Excepción:** el que dice que las fases de EP-001 son plan o retrodocumentación **bloquea 24 documentos** y merece subir al P3. |

---

**Lo que haría esta semana:** los cuatro del P0 (el 3 y el 2 son de una mañana entre los dos), y el bloque 9–14 del P2, que son siete arreglos pequeños que quitan ruido del validador y dejan de repetir trabajo a mano.

Dos cosas que quedaron anotadas en [el resumen de la sesión](historico-chat/resumenes/2026-08-16/sesion-2.md) y que necesitan tu decisión:

1. **¿Escribo esta prioridad en el `README.md` de `pendientes/`?** Como columna aparte del número, que sigue siendo el orden de construcción.
2. **¿Promuevo el punto 6 del 33 a pendiente numerado propio?** El README ya dice del 09 y del 10 que «no son un ítem, son un tema»; el 33 es el mismo caso y no lo dice, y ahí es donde se está escondiendo lo más urgente.

### 2 · Usuario — 2026-08-16 12:14:57
> osea no le cambia el nombre al archivo sino que los deja en el readme?

**Agente** — 2026-08-16 12:15:22
<!-- agente: 8a5cdfaf-bbb4-43d6-9c51-51b6fbc3665d -->

Exacto. Nada se renombra ni se renumera — y no es preferencia mía, lo prohíbe el propio README:

> **El número es el orden, no la prioridad.** [...] Al cerrar uno, el número no se reutiliza ni se renumeran los demás: los huecos son historia.

Hay dos razones más para no tocar el nombre del archivo:

- **El número se cita desde fuera.** El 30 nombra al 01 y al 20; el 33 nombra al 19 y al 31; el 36 nombra al 34 y al 35. Renumerar rompe todos esos enlaces — que es exactamente el defecto de los pendientes [35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) y [33 · punto 4](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Son dos cosas distintas y las dos sirven.** El número dice en qué orden se puede construir (qué se apoya en qué); la prioridad dice qué duele hoy. Si el número absorbe la prioridad, se pierde la dependencia.

Lo que propongo entonces es una **columna nueva** en las tablas que ya existen, más un bloque al principio con el orden de ataque:

```
| # | P | Pendiente | Qué resuelve |
|---|---|---|---|
| 01 | P5 | Validadores de código de proyecto | … |
| 30 | P1 | El checklist no ve la cadena | … |
| 34 | P0 | Las plantillas enlazan una base/ … | … |
```

Así el archivo se sigue llamando igual, el enlace sigue abriendo, y para saber qué sigue se lee la columna en vez del número.

Queda una decisión que sí es tuya: **la prioridad envejece.** Escrita en el README, dentro de dos semanas va a estar diciendo P0 sobre algo ya hecho. Dos salidas:

| Salida | Qué implica |
|---|---|
| **Columna en el README** (lo que propuse) | Se ve al lado de cada pendiente, pero hay que acordarse de mantenerla — y eso es justo lo que el [pendiente 09](pendientes/09-autonomia-sin-ia.md) llama «una regla que se cumple cuando alguien se acuerda, no se cumple» |
| **Un bloque «qué sigue» con 6 u 8 ítems**, al principio del README | No hay 28 valores que mantener, solo una lista corta que se reescribe cuando se vacía. Los otros 20 no llevan marca |

Me inclino por la segunda: mantener 28 prioridades a mano es trabajo que nadie va a hacer dos veces.

¿Cuál escribo?

---

Y aparte, del enganche: esta sesión la guardo como `2026-08-16-la-prioridad-de-los-pendientes.md` — se analizaron los 28 pendientes abiertos y se les dio un orden de prioridad, ¿va?

### 3 · Usuario — 2026-08-16 12:42:18
> 00·ID9

**Agente** — 2026-08-16 12:42:36
<!-- agente: e2540979-4104-453d-a0cf-12347720d200 -->

Sí: el nombre no se toca, la prioridad va en el README.

Renumerar está prohibido por el propio README, y el número se cita desde otros pendientes (el 30 nombra al 01 y al 20; el 36, al 34 y al 35).

Falta que elijas:

| | |
|---|---|
| **Columna `P` en las tablas** | 28 valores que envejecen y hay que mantener |
| **Bloque «qué sigue» de 6–8 ítems** al principio (recomiendo) | Una lista corta que se reescribe cuando se vacía |

Y el nombre de la sesión: `2026-08-16-la-prioridad-de-los-pendientes.md`, ¿va?

### 4 · Usuario — 2026-08-16 12:44:32
> qué debo elegir
>
> si me parece bien el nombre: 2026-08-16-la-prioridad-de-los-pendientes.md

**Agente** — 2026-08-16 12:45:27
<!-- agente: 18635b52-361e-457b-99e1-6c4a779da134 -->

Sesión renombrada e índice al día.

**Elige el bloque «qué sigue».** La columna te obliga a mantener 28 valores a mano; la lista corta se reescribe cuando se vacía. Y el propio [pendiente 09](pendientes/09-autonomia-sin-ia.md) ya lo dice: una regla que se cumple cuando alguien se acuerda, no se cumple.

Al renombrar se reprodujo el [pendiente 35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md): el enlace dentro del resumen quedó apuntando al nombre viejo. Lo corregí a mano y lo anoté como H-3 — deja de ser un defecto de `shopnest-mesa` y pasa a ocurrirle al estándar cada vez que nombra una sesión.

¿Escribo ya el bloque en [pendientes/README.md](pendientes/README.md)?

### 5 · Usuario — 2026-08-16 12:45:57
> no entendí qué es lo que tengo que elegir

**Agente** — 2026-08-16 12:46:12
<!-- agente: ed15fbe6-12ea-4c50-bdea-5f2ba951fc84 -->

Perdón, lo dije enredado. Es solo **dónde escribir el orden que te di**, para que no se pierda en el chat. Dos formas:

**A · Marcar los 28**, con una columna en las tablas que ya están:

```
| # | P | Pendiente |
|---|---|---|
| 01 | P5 | Validadores de código de proyecto |
| 30 | P1 | El checklist no ve la cadena |
| 34 | P0 | Las plantillas enlazan una base/ … |
```

**B · Marcar solo los próximos**, con un párrafo arriba del README y nada en las tablas:

```
## Lo próximo

1. 33 · punto 6 — a qué proyectos les borró la memoria el enganche
2. 34 — las plantillas enlazan una base/ que el proyecto no tiene
3. 29 · punto 2 — que el CLAUDE.md deje de pedir lo que el enganche ya hace
4. 36 — la regla de reportar al estándar
5. 30 — el checklist no ve la cadena
6. 27 — la fase A de HU-010 cerró sin cumplir

Cuando esta lista se vacíe, se escriben los seis siguientes.
```

La diferencia: con **A** quedan 28 marcas que hay que corregir cada vez que algo cambia. Con **B** hay seis renglones y se reescriben de una sentada.

**Elige B.** ¿Lo escribo?

### 6 · Usuario — 2026-08-16 12:47:15
> no entiendo, en dónde los va a marcar?

**Agente** — 2026-08-16 12:47:26
<!-- agente: c8bde9bc-eca1-46c6-b3b9-fc7a47fb9227 -->

En un solo archivo: [pendientes/README.md](pendientes/README.md). No se toca ningún otro.

Hoy ese archivo empieza así:

```
# Pendientes del estándar

Backlog de mejoras del estándar del agente que aún no se implementan…

El número es el orden, no la prioridad…

### 7 · Usuario — 2026-08-16 12:48:07
> entonces A para que todo quede actualizado

**Agente** — 2026-08-16 12:55:40
<!-- agente: 683fefe8-beee-4978-9257-88bb76c631bf -->

Va A. Escribo la columna en los 28.

Listo. La columna `P` quedó en [pendientes/README.md](pendientes/README.md), en las nueve tablas, con una sección arriba que explica los siete niveles. Validador de enlaces en cero.

Tres cosas que aparecieron al hacerlo:

- **Otra sesión agregó los pendientes 37 y 38** mientras escribía. Los incorporé: el 37 (dónde vive la fuente de las reglas) en **P3**, el 38 (el validador de `F22` sin su fase) en **P1** — es el mismo hueco del 30 pero visto desde adentro, el propio estándar llegando a código sin cadena.
- Eso mismo es el [pendiente 22](pendientes/22-dos-sesiones-versionando-a-la-vez.md) ocurriendo fuera de `VERSION`. El 22 está escrito solo para la versión y el registro; el problema es de cualquier archivo único que dos sesiones editen.
- El [35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) subió a **P1**: se reprodujo acá al nombrar esta sesión.

Todo quedó en [el resumen](historico-chat/resumenes/2026-08-16/la-prioridad-de-los-pendientes.md), con cuatro hallazgos.

Falta tu visto bueno para commitear.

### 8 · Usuario — 2026-08-16 12:58:17
> ya se puede cerrar la sesión?

**Agente** — 2026-08-16 12:58:36
<!-- agente: fd4462e3-5cf9-4d77-a760-ac8485274dbc -->

Todavía no. Faltan tres:

| Para cerrar | Estado |
|---|---|
| H-1 · la prioridad — decidida y escrita | ✅ |
| H-3 · el enlace del resumen — corregido, y el defecto ya vive en el [35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) | ✅ |
| **H-2** · promover el punto 6 del [33](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) a pendiente propio | ☐ anotado en el README, pero sin archivo |
| **H-4** · ampliar el [22](pendientes/22-dos-sesiones-versionando-a-la-vez.md) a cualquier archivo compartido | ☐ solo está en el resumen |
| **Aprobado y guardado** | ☐ sin commit |

Los dos primeros son cortos: el H-2 es crear `pendientes/39-...md` con el punto 6 (la memoria borrada a los proyectos, que es el P0 de todo el backlog) y quitarlo del 33; el H-4 es un párrafo dentro del 22.

¿Los hago y te dejo listo el commit para que lo apruebes?

### 9 · Usuario — 2026-08-16 13:00:08
> si

**Agente** — 2026-08-16 13:04:16
<!-- agente: 6f6b39cd-c975-4cdb-b87a-015afcd28006 -->

Ahora el README y el 22.

Ahora el 22:

Cierro el resumen y preparo el commit.

Todo hecho y con enlaces en cero. Esto es lo que iría al commit:

| Archivo | Qué cambia |
|---|---|
| [pendientes/README.md](pendientes/README.md) | La columna `P` en las nueve tablas + la sección que explica los siete niveles |
| [pendientes/39-…](pendientes/39-a-que-proyectos-les-borro-la-memoria-el-enganche.md) | **Nuevo.** El punto 6 del 33, promovido. Único P0 |
| [pendientes/33-…](pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) | El punto 6 se va y queda el puntero al 39 |
| [pendientes/22-…](pendientes/22-dos-sesiones-versionando-a-la-vez.md) | Sección nueva: no es solo `VERSION`, es cualquier archivo compartido |
| [resumenes/2026-08-07/memoria-del-agente-en-el-repo.md](historico-chat/resumenes/2026-08-07/memoria-del-agente-en-el-repo.md) | Su H-3 ahora apunta al 39 y no al 33 |
| [resumenes/2026-08-16/la-prioridad-de-los-pendientes.md](historico-chat/resumenes/2026-08-16/la-prioridad-de-los-pendientes.md) | **Nuevo.** Los cuatro hallazgos, con la tabla de cierre |
| Transcripción + los dos índices | El renombrado de la sesión |

Una cosa antes: los pendientes **35 y 36 nunca se commitearon** — los dejó otra sesión de esta mañana. El README que voy a subir los enlaza, así que si los dejo por fuera el commit queda apuntando a archivos que no están en el repo.

¿Los incluyo, o prefieres que esa sesión suba lo suyo y yo dejo el commit sin ellos?

### 10 · Usuario — 2026-08-16 13:04:37
> suba todo

## Abiertos                          ← acá arrancan las tablas de los 28

### Garantía y sostenimiento del estándar (01–06, en orden)
| # | Pendiente | Qué resuelve | Por qué va aquí |
…
```

- **Opción A** = agregarle una columna a esas tablas, o sea tocar los 28 renglones.
- **Opción B** = meter seis renglones nuevos justo **antes** de `## Abiertos`, y dejar las tablas como están.

En los dos casos es el mismo archivo. Lo que cambia es cuánto de él se toca.
