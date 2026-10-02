# Análisis 7: la plantilla de la HU no tiene dónde poner «Sale de»

> **Aprobado** por el usuario el 2026-10-02, en el turno 132. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 6](analisis-6.md), aprobado el 2026-10-02. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Hallazgo

### H-7. La plantilla de la HU no tiene dónde poner «Sale de»

| Campo | Valor |
|---|---|
| Qué pasó | Al escribir la fase `A` de la [HU-002](../HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md) de EP-023, el 2026-10-02, se encontró que los criterios de `plantillas/ciclo-vida-proyectos/04-HU.md` no tienen el campo «Sale de». La regla nueva del CA-01 lo exige en cada criterio, y `13·DOC15` manda crear la HU desde esa plantilla. Las de análisis, pendiente y plan sí tienen su campo. |
| Por qué importa | Una HU hecha con la plantilla, como manda `DOC15`, no cumpliría la regla nueva, y el validador la detendría: dos reglas chocarían (análisis 1, conclusión 12). Cambiar la plantilla no está en los criterios de la HU-002. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La pasa el enganche desde la [transcripción del día](../../../../historico-chat/2026-10-01-sesion.md), a partir del turno 129, donde se dijo «Analicemos: el pendiente 103».

### 129 · Usuario, 2026-10-02 08:15:11
> Analicemos: el pendiente 103

**Agente**, 2026-10-02 08:15:45
<!-- agente: e8fbc03e-61ef-4cef-99cf-3509edf6e383 -->

Ya está el encabezado del análisis 7. Hay que decidir qué se hace con la plantilla de la HU.

**El choque:** `F27` va a exigir «Sale de» en cada criterio de la HU, y la plantilla `04-HU.md` no tiene ese campo. Ningún validador revisa los campos de los criterios contra la plantilla, así que agregarlo no rompe las HU viejas.

**Mi recomendación:**
1. Agregar a cada criterio de `04-HU.md` la línea `**Sale de:** «el punto de "Lo que se tiene que hacer" del análisis, con su número»`, encima del bloque del escenario, como ya está en las HU de EP-023.
2. Que entre a la HU-002 como parte del CA-03, que ya trata de la plantilla de la HU. Así no nace un criterio nuevo.

¿Se hace así?

### 130 · Usuario, 2026-10-02 08:17:11
> Pregunta osea recomienda los 2?

**Agente**, 2026-10-02 08:17:17
<!-- agente: d643e8e0-3bf3-4128-b7fa-fc358468cf61 -->

Sí, son las dos partes de la misma recomendación:

1. **Qué se cambia:** se agrega «Sale de» a cada criterio de la plantilla de la HU.
2. **Dónde queda pedido:** dentro del CA-03 de la HU-002, porque ese criterio ya trata de la plantilla de la HU.

¿Se hace así?

### 131 · Usuario, 2026-10-02 08:17:40
> Hágalo

**Agente**, 2026-10-02 08:18:28
<!-- agente: 0db45c23-92d5-4acf-8a7f-3e95b9977b23 -->

Ya escribí lo que faltaba del [análisis 7](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-7.md):

- **Conclusiones:**
  1. El H-7 frena la fase A.
  2. Cada criterio de la plantilla de la HU lleva «Sale de».
  3. Ese cambio entra al CA-03 de la HU-002.
- **Lo que se tiene que hacer:**
  1. El CA-03 pasa a su versión siguiente.
  2. El plan de la fase A pasa a su versión 2.

La plantilla todavía no cambia: se cambia al ejecutar la fase, cuando el usuario apruebe el plan.

`validar.py estandar` no muestra incumplimientos, y lo escrito no tiene marcas de `00·ID8`.

Para cerrarlo: «Apruebo el análisis».

### 132 · Usuario, 2026-10-02 08:19:12
> Apruebo el análisis

**Agente**, 2026-10-02 08:19:20
<!-- agente: dae31b62-d25c-43f7-b2e9-55e81f552389 -->

El análisis 7 quedó aprobado, con la marca en el turno 132. Se apaga al terminar esta respuesta y en el próximo mensaje confirmo que quedó apagado.

Faltan sus dos puntos: pasar el CA-03 de la HU-002 a su versión siguiente y pasar el plan de la fase A a su versión 2. Con eso, la HU-002 y los planes quedan para aprobar.

Para hacerlo: «Escriba».

> acá termina la conversación

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `13·DOC15` (la HU se crea desde la plantilla central), `02·F18` y la regla nueva `02·F27` de la HU-002 (cada punto lleva «Sale de»). Chocan `DOC15` y `F27`: la plantilla no tiene el campo que `F27` exige. Se resuelve en el punto 1 de lo que se tiene que hacer.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `plantillas/ciclo-vida-proyectos/04-HU.md` | Sus tres criterios de ejemplo tienen el escenario, «Cómo validarlo» y «Aprobado cuando»; no tienen «Sale de» |
| Las HU de EP-023 | Sus 42 criterios ya llevan «**Sale de:**» encima del escenario |
| Validadores | Ninguno compara los campos de los criterios contra la plantilla; agregar el campo no rompe las HU anteriores |
| Fase `A` de la HU-002 | Planes escritos el 2026-10-02, sin aprobar; ningún archivo tocado |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Conclusión 45 del análisis 1 | Lo que el análisis no previó y queda fuera de los criterios es un hallazgo. Lo recoge la conclusión 1 |
| Lección 1 del análisis 6 | Se repite: el análisis 1 decidió exigir «Sale de» sin revisar las plantillas que lo tienen que llevar |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno nuevo: la fase ya sube a 42.0.0, MAYOR, por `F27`. El campo en la plantilla va en la misma versión |
| Normas y leyes | Ninguna aplica |
| Herramientas | La conversación entró sola, y el análisis 6 se apagó con la corrección del H-6 |

---

## Conclusiones

| # | Tema | Conclusión | Sale de |
|---|---|---|---|
| 1 | Es parte del plan en curso | El H-7 frena la fase `A` de la HU-002 antes de aprobarse, y se resuelve antes de seguirla | Turno 129 |
| 2 | La plantilla de la HU | Cada criterio de `04-HU.md` lleva la línea «Sale de», con el punto de «Lo que se tiene que hacer» del análisis, encima del escenario | Turnos 130 y 131 |
| 3 | Dónde queda pedido | Entra al CA-03 de la HU-002, que ya trata de la plantilla de la HU; no nace un criterio nuevo | Turnos 130 y 131 |

Siguen abiertas: ninguna.

## Propuesta final: hallazgo y pendiente

> El H-7 no cambia. El pendiente sigue en la V3. EP-023 no suma HU: el cambio cabe en la HU-002.

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | Al exigir un campo nuevo, el análisis no revisó las plantillas que lo tienen que llevar | Falló | Por escribir |
| 2 | Medir, antes de escribir el plan, qué documentos ya cumplen y cuáles no destapó el hallazgo antes de aprobar | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de la conclusión | Pasó a |
|---|---|---|---|
| 1 | Pasar el CA-03 de la HU-002 a la versión siguiente: además del contexto, cada criterio de la plantilla de la HU lleva «Sale de» | 2, 3 | EP-023, [HU-002](../HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md) |
| 2 | Pasar el plan de la fase `A` de la HU-002 a su versión siguiente con ese campo, y volver a aprobarlo | 1, 3 | EP-023, HU-002, fase `A` |
