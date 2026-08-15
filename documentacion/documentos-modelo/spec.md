# Especificación del módulo Documentos modelo

- **Slug del módulo:** `documentos-modelo`
- **Estado:** en implementación

> Primera entrega de este módulo: la marca del espacio por llenar. El módulo es más grande (los diez modelos de EP-003), y esta especificación crece con cada fase. Lo que hoy cubre es lo que construye la fase [`A-EP-003-HU-001-marca-de-espacio-por-llenar`](../epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/README.md).

---

## 1. Propósito y alcance

Un modelo es un esqueleto con huecos. Este módulo define **cómo se marca un hueco** para que se vea al leer y para que un programa lo pueda contar, y **qué significa** que un documento entregado todavía traiga marcas.

- **Dentro de alcance:** la marca, qué es un hueco y qué no lo es, qué se escribe cuando una sección no aplica, y la aplicación de todo eso a las 30 plantillas que ya existen.
- **Fuera de alcance:**
  - El programa que cuenta las marcas. Es de EP-004, y se apoya en lo que esta especificación define.
  - El contenido de cada modelo. Acá se toca la marca, no lo que el modelo pide.
  - Los documentos ya llenados en `documentacion/`, `historico-chat/` y `pendientes/`: son documentos terminados, no modelos.
  - Los otros nueve modelos de EP-003. Son incrementos posteriores de este mismo módulo y se suman a esta especificación cuando abran su fase.

## 2. Contexto — qué hay hoy

Módulo nuevo en cuanto a norma escrita, pero **no** en cuanto a práctica: la convención ya se usa sin que ninguna regla la exija.

Verificado el 2026-08-14, contando archivo por archivo en `plantillas/`:

| Situación | Cuántos | Cuáles |
|---|---|---|
| Usan `«…»` | 25 de 30 | `ADR.md`, `brief.md`, `HU.md`, `fase.md`, `senales.md`, `sesion.md`, `planes/trabajo.md`, `CLAUDE.md.plantilla` y 17 más |
| Usan otra marca | 2 | [`plantillas/epica.md`](../../plantillas/epica.md) con `[Resultado observable…]` y `<slug>`; [`plantillas/marco-normativo.md`](../../plantillas/marco-normativo.md) con `` `<nombre>` `` |
| Por decidir | 3 | [`memoria.md`](../../plantillas/memoria.md), [`historico-chat.md`](../../plantillas/historico-chat.md) y [`retrodocumentacion.md`](../../plantillas/retrodocumentacion.md) |

Lo más cercano a una norma escrita es la frase que repiten las cajas de instrucciones de las plantillas: *"Reemplaza los `«…»` y borra esta caja"*. Dice qué hacer con la marca, no cuál es la marca ni por qué. Nunca se escribió como regla, así que hoy se cumple porque alguien se acuerda.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:**
  - Los modelos se llenan a mano o con ayuda de la IA, no con un formulario. Si mañana hubiera formulario, la marca seguiría sirviendo, pero el argumento de "que se vea al leer" pesaría menos.
  - `«` y `»` no chocan con la sintaxis de markdown ni con la de los comandos que aparecen dentro de las plantillas.
- **Dependencias / prerequisitos:** ninguna. Es la primera historia de EP-003 y su §9 lo declara.
- **Preguntas abiertas:** ninguna viva. Las tres que había se respondieron el 2026-08-14 y quedaron en §12.

## 4. Reglas de negocio

1. **Hay una sola marca para el espacio por llenar, y es `«…»`.** Si cada modelo usa la suya, ni se ve al leer ni se puede contar.
2. **La marca se nota sin buscarla.** Un hueco que hay que ir a cazar se aprueba con el hueco adentro.
3. **Un programa la encuentra sin confundirla con el texto normal.** De eso depende que EP-004 pueda comprobarla.
4. **Un hueco es lo que llena quien usa el modelo.** La sintaxis de un comando que se copia y se pega no es un hueco: la llena quien corre el comando, y marcarla daría falsos positivos.
5. **Un documento entregado con marcas sin reemplazar no está terminado.** La condición de terminado es objetiva y se puede señalar dónde falla.
6. **Una sección que no aplica se escribe `N/A`**, no se deja con la marca ni se borra. Borrarla haría creer que el modelo no la pedía.
7. **La caja de instrucciones del modelo se borra al llenarlo; lo que explica para qué sirve el documento se queda.**

## 5. Modelo de datos

No aplica porque el entregable es texto normativo y plantillas: no hay entidades, tablas ni catálogos.

## 6. Comportamiento y flujos

**Caso principal, alguien llena un modelo:**

1. Copia la plantilla al sitio que le indica su caja de instrucciones.
2. Reemplaza cada `«…»` por lo que corresponda, o escribe `N/A` si esa sección no le aplica.
3. Borra la caja de instrucciones.
4. Entrega. Si quedó una marca, el documento no está terminado, y quien lo recibe puede señalar cuál.

**Camino de error, la marca se confunde con otra cosa:** dentro de las plantillas hay comandos con su propia sintaxis, como `--tema "<tema>"`. Ese `<tema>` **no** se marca: lo llena quien corre el comando. La regla lo deja escrito para que ni la persona ni el programa lo cuenten como hueco.

## 7. Interfaz / UI

No aplica: no hay interfaz. Los documentos se abren en un editor de texto.

## 8. Permisos y autorización

No aplica porque no hay servicio ni autenticación.

| Permiso | Quién lo tiene | Qué habilita |
|---|---|---|
| Ninguno | — | — |

## 9. Marco normativo

No aplica: el módulo no toca datos personales ni ninguna norma externa.

## 10. Plan de pruebas

El detalle vive en el [plan_pruebas.md](../epicas/EP-003-documentos-modelo-y-procedimientos/HU-001-marca-de-espacio-por-llenar/A-EP-003-HU-001-marca-de-espacio-por-llenar/plan_pruebas.md) de la fase. En resumen:

- **Caso feliz:** los huecos de tres plantillas se señalan de una sola lectura, y el recuento a ojo coincide con el del `grep`.
- **Casos límite:** un archivo sin huecos (que debe quedar en cero con su motivo escrito) y una sección marcada `N/A`.
- **Errores:** un documento entregado con dos marcas sin reemplazar; una marca descartada que sobrevive en alguna plantilla.
- **Triangulación:** el recuento se hace de dos formas independientes, a ojo y con `grep`, y tienen que dar lo mismo.
- **Verificación manual (`08·T4`):** que la marca no estorbe la lectura. Eso no lo mide ningún programa.

## 11. Criterios de aceptación (Definition of Done)

- [x] La marca está escrita como regla, con el porqué en `notas/`.
- [x] Está escrito qué es un hueco y qué no lo es.
- [x] Las 30 plantillas usan la misma marca, y las que no tienen huecos dicen por qué.
- [x] Un documento con marcas sin reemplazar no se da por terminado, y se puede señalar cuáles.
- [x] Una sección que no aplica se escribe `N/A`.
- [x] Pruebas verdes, incluida la triangulación del recuento.
- [x] Trazabilidad especificación → implementación sin faltantes (`13·DOC3`).
- [x] Entrada en `CHANGELOG.md` y subida de `VERSION` (`20·M10`).

## 12. Decisiones tomadas

- **`2026-08-14` — la marca es `«…»`.** Ya se usa en 25 de 30 plantillas: elegir otra costaría cambiar 25 archivos en vez de 5. Las alternativas chocan con sintaxis que el propio documento usa: `[]` con los enlaces de markdown y las casillas, `<>` con las etiquetas y con los comandos, `{{}}` con los motores de plantillas.
- **`2026-08-14` — la sintaxis de un comando no es un hueco.** La llena quien corre el comando, no quien usa el modelo. Contarla daría falsos positivos, y el riesgo de la épica es perder la confianza por eso.
- **`2026-08-14` — una sección que no aplica se escribe `N/A`.** Decisión del usuario. Deja rastro de que la sección se leyó y no aplicaba, que es distinto de haberla saltado.
- **`2026-08-14` — este módulo sí lleva especificación aparte.** Decisión del usuario. Cierra la duda que arrastraban las dos fases anteriores, que se habían abierto declarando que no la necesitaban: `02·F2` se cumple, no lleva excepción.
- **`2026-08-14` — la regla va en el capítulo 13.** `20·M13` manda enrutar a lo que ya existe, y la marca es cómo se escribe la documentación.

## 13. Trazabilidad (se completa al implementar)

| Ítem de la especificación | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · una sola marca, `«…»` | regla | `base/13-documentacion/reglas/DOC19-…` | ✅ | CP-002 |
| RN-04 · la sintaxis de comando no es hueco | regla | Dentro de `DOC19` | ✅ | CP-003 |
| RN-05 · con marcas no está terminado | regla | `base/13-documentacion/reglas/DOC20-…` | ✅ | CP-004 |
| RN-06 · lo que no aplica se escribe `N/A` | regla | `base/13-documentacion/reglas/DOC21-…` | ✅ | CP-004 |
| El porqué de la marca | documentación | `notas/marca-del-espacio-por-llenar.md` | ✅ | La nota |
| Aplicación de la marca | plantilla | 13 archivos de `plantillas/` | ✅ | 179 huecos convertidos |

## 14. Cruces con otros módulos

**Qué consume este módulo de otros:**

| Módulo | Qué consume | Por qué |
|---|---|---|
| Ninguno | — | Es la primera historia de su épica y no depende de nada |

**Historial cruzado — quién consume de este módulo:**

| Fecha | Módulo que consume | Qué cambió acá por eso |
|---|---|---|
| 2026-08-14 | `programas-de-comprobacion` (EP-004) | Nada todavía. Queda anotado que el programa que cuente las marcas se apoya en la RN-04: sin ella, reportaría la sintaxis de los comandos |
