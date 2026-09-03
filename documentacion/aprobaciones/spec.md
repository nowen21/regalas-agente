# Especificación del módulo Aprobaciones  ·  `[CAPA 3]`

- **Slug del módulo:** `aprobaciones`
- **Estado:** aprobada, el 2026-09-01 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 4, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Guardar quién aprobó un documento, cuándo, y **sobre qué texto exacto**; y saber si lo aprobado sigue siendo lo que hay.

- **Dentro de alcance:** registrar la aprobación (`F-015`), mostrar el estado de cada documento (`F-016`), y caducarla cuando el texto cambia (`F-017`).
- **Fuera de alcance:** decidir si algo merece aprobarse, y aprobar por cuenta propia. La plataforma registra; quien aprueba es una persona.

## 2. Contexto — qué hay hoy

**Las aprobaciones se escriben a mano dentro de los documentos.** Medido el 2026-09-01: **21 documentos** de este repositorio traen una línea del estilo de `| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ |`.

**Y esa línea no dice sobre qué texto se aprobó.** El documento pudo cambiar tres veces desde entonces, y la marca sigue ahí igual. La ficha de `F-015` lo dice sin rodeos: *«es la pieza que hoy no existe, y de la que se sostiene todo el gobierno»*.

**`F-017` salió de un caso real**, y está escrito en su ficha: se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que el documento vive en el proyecto y se puede leer.
- **Dependencias:** Proyectos, que dice dónde vive cada uno; Auditoría, que registra que se aprobó.
- **Preguntas abiertas:** qué hacer con las 21 marcas escritas a mano. **No se migran solas:** cada una diría que se aprobó un texto que hoy no se puede reconstruir.

## 4. Reglas de negocio

1. **Una aprobación guarda la huella del texto aprobado.** Sin ella no dice nada.
2. **No se aprueba un documento que no existe.** Sería firmar en blanco.
3. **Si el texto cambia, la aprobación caduca**, y se dice cuánto cambió.
4. **La aprobación anterior no se borra.** Es la historia de qué se autorizó.
5. **Los tres estados se dicen con palabras**, no con color.
6. **Un documento sin aprobación aparece así, no vacío.**
7. **Aprobar queda registrado en la auditoría.**

## 5. Modelo de datos

**Es el segundo módulo de la plataforma con una entidad propia**, y el porqué importa:

| Qué | Dónde vive | Por qué ahí |
|---|---|---|
| La aprobación | **En la base** | **Aprobar es un hecho que ocurrió.** No se puede derivar del texto: si no queda escrito, no ocurrió para nadie más |
| El documento aprobado | En el proyecto | La fuente es el texto, como siempre |
| Que se aprobó, y cuándo | Auditoría | `DA-08` |

Los demás módulos calculan al pedir porque su respuesta **está** en el texto. Esta no: el texto no sabe quién lo aprobó.

- **Valores configurables:** ninguno.
- **Migración:** una tabla nueva, sin datos previos.

### 5.1 Los tres estados, y por qué no son dos

| Estado | Qué quiere decir | Qué hacer |
|---|---|---|
| **Aprobado** | Alguien lo aprobó, y el texto sigue siendo ese | Nada |
| **Caducada** | Alguien lo aprobó, **y el texto cambió después** | Mirar qué cambió, y volver a aprobar si procede |
| **Sin aprobación** | Nadie lo ha mirado | Aprobarlo, o no |

**Confundir «caducada» con «sin aprobación» pierde información.** La primera dice que hubo un juicio y que algo lo invalidó; la segunda, que nunca lo hubo. Y confundir cualquiera de las dos con «rechazado» sería peor todavía: la plataforma no rechaza nada.

**Se dicen con palabras.** Lo pide el `CA-1` de `F-016`, y el motivo está en su ficha: quien no distingue colores tiene que poder saberlo igual.

## 6. Comportamiento y flujos

**Aprobar.** Se recibe el proyecto, el documento y quién aprueba. Se lee el texto, se guarda su huella y su tamaño, y queda registrado. **Si el documento no existe, no se aprueba.**

**Consultar el estado.** Se compara la huella de lo que hay con la de la última aprobación. Si coincide, aprobado; si no, caducada; si no hay aprobación, se dice.

**Ver qué cambió.** Se dice cuántos caracteres hay de más y de menos respecto de lo aprobado. **No es un diff completo:** es lo que alcanza para decidir si vale la pena mirar. El diff de verdad lo da el control de versiones, que ya lo hace bien.

## 7. Interfaz

**Las aprobaciones** (`P-06`, en `/proyecto/<id>/aprobaciones/`): el estado de cada documento con alguna aprobación, dicho con palabras y no con color, y cuánto cambió desde lo aprobado.

**La pantalla dice lo que no muestra:** solo salen los documentos que tienen alguna aprobación registrada, y no son todos los del proyecto. Callarlo haría creer que esos son todos.

Aprobar sigue por orden de consola: es un cambio de estado, y va con su confirmación.

## 8. Permisos y autorización

**Desde `EP-022` hay cuentas, dos grupos y permisos.** Quién puede qué está en la [especificación de Acceso](../acceso/spec.md) §8. Acá vale la regla general: **el agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas.**

**Y `quien` dejó de ser un texto libre:** tiene que ser una cuenta con permiso para aprobar. Una aprobación que dice quién la dio y no lo prueba es el mismo problema que este módulo vino a resolver en los documentos.

## 9. Marco normativo

**Una aprobación es lo más parecido a una firma que este sistema guarda.** No sale del proyecto y no se comparte, pero sí es lo que alguien podría invocar meses después. Por eso nada se borra, y por eso la huella va siempre.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Aprobar | Con documento · sin documento · sin proyecto |
| La huella | Que sea la del texto aprobado |
| Caducar | Editando · borrando el documento |
| La historia | Que la anterior se conserve |
| Los tres estados | Cada uno con su frase |

## 11. Criterios de aceptación

- `CA-1` Queda registrado quién aprobó, cuándo y sobre qué texto.
- `CA-2` La aprobación se puede consultar meses después.
- `CA-3` No se puede aprobar un documento que no existe.
- `CA-4` Se distingue lo aprobado de lo que está en borrador, **con palabras**.
- `CA-5` Un documento sin aprobación aparece así, no vacío.
- `CA-6` Editar un documento aprobado le quita la aprobación.
- `CA-7` Se ve qué cambió respecto de lo aprobado.
- `CA-8` La aprobación anterior no se borra: queda como historia.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **La aprobación se guarda en la base** | Escribirla en el documento | Es lo que se hace hoy, y no dice sobre qué texto se aprobó |
| **Se guarda la huella del texto** | Solo quién y cuándo | Sin la huella, «aprobado» no responde la única pregunta que importa |
| **Tres estados, no dos** | Aprobado / no aprobado | «Caducada» dice que hubo un juicio; «sin aprobación», que nunca lo hubo |
| **Se dice con palabras** | Con color | Quien no distingue colores tiene que poder saberlo |
| **Nada se borra** | Reemplazar la aprobación anterior | Es la historia de qué se autorizó y cuándo |
| **Lo que cambió se mide en caracteres** | Un diff completo | El diff lo da el control de versiones; acá alcanza con saber si vale la pena mirar |
| **Las 21 marcas a mano no se migran** | Convertirlas en aprobaciones | Cada una diría que se aprobó un texto que hoy no se puede reconstruir |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-015 | RF-15 | [HU-001 Registrar una aprobación con su firma](../epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-001-registrar-una-aprobacion-con-su-firma/HU-001-registrar-una-aprobacion-con-su-firma.md) | [M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto](../epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-001-registrar-una-aprobacion-con-su-firma/M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto/estado-fase.md), cerrada el 2026-09-01 |
| F-016 | RF-16 | [HU-002 Ver qué está aprobado y qué no](../epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-002-ver-que-esta-aprobado-y-que-no/HU-002-ver-que-esta-aprobado-y-que-no.md) | [N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras](../epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-002-ver-que-esta-aprobado-y-que-no/N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras/estado-fase.md), cerrada el 2026-09-01 |
| F-017 | RF-17 | [HU-003 Caducar la aprobación cuando el texto cambia](../epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md) | [O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia](../epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia/O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia/estado-fase.md), cerrada el 2026-09-01 |

## 14. Cruces con otros módulos

- **Proyectos:** dice dónde vive cada documento.
- **Auditoría:** registra que se aprobó, quién y cuándo.
- **Ciclo de vida:** un documento que se llena desde la plataforma caduca su aprobación, y eso es correcto.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| — | — | — | — |
