# Inventario de funcionalidades: lo que se quiere desarrollar   ·   `[CAPA 3]`

> Plantilla. Acompaña a la **propuesta** de todo desarrollo: la lista completa de funcionalidades de lo
> que se va a construir, con estado por ítem, para que el alcance lo confirme el usuario y no lo asuma
> el agente. **Sin este inventario aprobado no se derivan épicas**
> ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).
> Se copia a la carpeta de la propuesta del proyecto, se reemplazan los `«…»` y se borra esta caja.
> En un proyecto chico el inventario es una tabla de diez filas: la puerta es la aprobación, no el tamaño.

**Estado: «BORRADOR / EN REVISIÓN DEL USUARIO / APROBADO»** («AAAA-MM-DD»). Este inventario es **el punto de partida de las épicas**: ninguna épica se deriva hasta que el usuario lo apruebe. Lo que diga «por confirmar» es una pregunta, no una decisión.

**Por qué existe:** la propuesta viene acompañada del inventario que tenga, de manera clara, **todas** las funcionalidades de lo que se va a desarrollar. El alcance no lo asume el agente: lo confirma el usuario acá.

**Destino del documento:** este inventario **se convierte en la documentación final del producto**. No es un artefacto de planeación que se bota al arrancar: cada ítem, cuando se construya, gana aquí su descripción de uso, y el documento madura junto con el sistema hasta ser el manual. Por eso cada fila se escribe para que la entienda quien va a **usar** el producto, no solo quien lo construye.

## 0. Lo que el usuario ya definió («AAAA-MM-DD»)

> Las decisiones de alcance que el usuario ya tomó, con sus palabras. Es el techo y el piso del inventario: nada de acá se vuelve a preguntar, y nada que no esté acá se da por decidido.

1. «Decisión de alcance, en palabras del usuario.»
2. «…»

## 1. «Nombre del grupo de funcionalidades»

> Un numeral por grupo con sentido propio (lo ya construido, el producto base, cada módulo grande). Los cuatro estados posibles de un ítem, y ninguno más: **Existe** (construido y en uso), **Parcial** (construido a medias, y se dice qué falta), **Por construir** (acordado, sin construir), **Por confirmar** (es una pregunta al usuario, enlazada en la sección de preguntas).

| # | Funcionalidad | Estado |
|---|---|---|
| 1.1 | «Qué hace, dicho para quien va a usarla» | «Existe / Parcial: qué falta / Por construir / Por confirmar (P-«n»)» |
| 1.2 | «…» | «…» |

**Cuenta:** «cuántas existen, cuántas parciales, cuántas por construir, de cuántas». La cuenta hace visible el tamaño real de lo que se está aprobando.

## 2. Proyección: por confirmar con el usuario

> Nada de esta sección está decidido; cada fila es una pregunta de la sección siguiente. Es la que evita que el proyecto se cierre a lo inmediato: lo que se quiere a futuro queda escrito como candidato, no como supuesto.

| # | Funcionalidad candidata | Estado |
|---|---|---|
| 2.1 | «…» | **Por confirmar** (P-«n») |

## 3. Preguntas abiertas: las contesta el usuario

> Una por decisión pendiente, numeradas `P-1`, `P-2` y las que sigan. Cada una con las opciones sobre la mesa y, si el agente tiene recomendación, dicha como propuesta. Una pregunta sin contestar no bloquea el resto del inventario: bloquea solo los ítems que la citan.

- **P-1 · «¿La pregunta, completa?»** «Las opciones, con su costo. Propuesta del agente: «cuál y por qué».»

## 4. Qué pasa cuando el usuario apruebe

1. El planteamiento de la propuesta se revisa para que diga esto y no lo que se haya asumido antes.
2. Los ítems aprobados bajan a requisitos, cada uno con su identificador.
3. Las épicas se derivan **de este inventario**, cada una citando los ítems que cubre ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).
4. El documento no se archiva: sigue madurando con cada ítem construido, camino a ser el manual.

---

*«Quién lo escribió y cuándo, y sobre qué instrucción del usuario. Nada de las secciones de proyección y preguntas se da por decidido hasta que el usuario lo marque.»*
