# Análisis 4: las HU de una épica repiten el contexto del pendiente

> **Aprobado** por el usuario el 2026-10-01, en el turno 53. El hallazgo y el pendiente no pasaron a otra versión, porque el análisis no los cambió. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 3](analisis-3.md), aprobado el 2026-10-01. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Recomendaciones

> Se agregó en el piloto, por el [análisis 9](analisis-9.md): este análisis no consultó recomendaciones, porque el archivo no existía. De sus lecciones salen: R-13 y R-14.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| Ninguna | El archivo de [recomendaciones del análisis](../../../../../plantillas/recomendaciones-del-analisis.md) nació después |

---

## Hallazgo

### H-3. Las HU de una épica repiten el contexto del pendiente

| Campo | Valor |
|---|---|
| Qué pasó | Las siete HU de [EP-023](../../epica.md) tienen el mismo «Contexto y descripción»: el problema del pendiente copiado tal cual, como pide la [plantilla de la HU](../../../../../plantillas/ciclo-vida-proyectos/04-HU.md). Ese problema ya está en la épica, en su sección 3.1, así que el mismo texto queda en ocho sitios. |
| Por qué importa | Si el texto cambia, hay que corregirlo en todos: es el riesgo de un registro en dos sitios (S-064). Y el contexto no dice qué parte del problema de la épica resuelve cada HU. Pedir «el problema del pendiente tal cual» sirve cuando un pendiente da una sola HU; cuando hay épica, ese texto le corresponde a la épica. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La pasa el enganche desde la [transcripción del día](../../../../../historico-chat/2026-10-01-sesion.md), a partir del turno 46, donde se dijo «Analicemos: el pendiente 103».

### 46 · Usuario, 2026-10-01 22:29:42
> Analicemos: el pendiente 103

**Agente**, 2026-10-01 22:30:45
<!-- agente: 62453c10-6798-40cc-8205-48e648d15f7e -->

El análisis 4 quedó prendido.

- Parte del H-2, que ahora enlaza a este análisis desde el [resumen de hoy](../../../../../historico-chat/resumenes/2026-10-01/sesion.md).
- El archivo es [analisis-4.md](analisis-4.md), en la carpeta del pendiente, y ya le entró el turno 46.

**Lo primero, según la conclusión 7 del análisis 2: ¿el H-2 es parte del plan en curso?**

| Opción | Qué pasa |
|---|---|
| **A. Sí es parte** | El pendiente pasa a la V4 y EP-023 suma lo que se decida sobre las plantillas. Se resuelve antes de aprobar las HU 2 a 7 |
| B. No es parte | Se crea su propio pendiente, y EP-023 sigue sin tocarse |

**Recomiendo A.** El H-2 apareció escribiendo EP-023 y hoy la frena. El contexto repetido en las siete HU es un caso del mismo hallazgo: la plantilla de la HU no dice qué va en ese campo cuando un pendiente da una épica, y eso choca con «cada documento sale del anterior», que es el centro del pendiente. Mientras no se decida, las HU 2 a 7 no se pueden aprobar sin arrastrar ese campo.

¿A o B?

### 47 · Usuario, 2026-10-01 22:35:16
> el hallazgo es este:
> "
> 
> Sí. El problema general del pendiente ya está en la épica, en su sección 3.1. Al copiarlo en las siete HU, el mismo texto queda en ocho sitios, y si cambia hay que corregirlo en todos. Es el riesgo que la señal S-064 dice de un registro en dos sitios.
>
> El contexto de cada HU debería decir lo suyo: qué parte del problema de la épica resuelve esa HU, con el enlace a la épica para lo general.
>
> Que la plantilla pida «el problema del pendiente tal cual» sirve cuando un pendiente da una sola HU, sin épica de por medio. Cuando hay épica, ese texto le corresponde a la épica.
>
> " y no se ha registrado

**Agente**, 2026-10-01 22:35:22
<!-- agente: cac4c9c9-6087-49e7-a2ec-3e5f0fc39d21 -->

Falta la palabra que dice qué se espera (`01·C28`). Con «Registre» anoto ese hallazgo como H-3 y lo pongo como el que origina el análisis 4, en lugar del H-2.

### 48 · Usuario, 2026-10-01 22:35:32
> Registre

**Agente**, 2026-10-01 22:36:14
<!-- agente: 4d1bdad0-0c08-438c-a791-8921e48b426f -->

Quedó registrado como H-3, «Las HU de una épica repiten el contexto del pendiente», en el [resumen de hoy](../../../../../historico-chat/resumenes/2026-10-01/sesion.md). Lleva solo «Qué pasó» y «Por qué importa», con el texto del usuario.

- **El análisis 4** ahora parte del H-3. Cambiaron su título y la copia del hallazgo.
- **El H-2** volvió a tener su pendiente «por definir».

Lo primero que decide el análisis 4 (conclusión 7 del análisis 2) es si el H-3 es parte del plan en curso:

| Opción | Qué pasa |
|---|---|
| **A. Sí es parte** | El pendiente pasa a la V4 y EP-023 suma cómo se escribe el contexto de una HU que sale de una épica. Se resuelve antes de aprobar las HU 2 a 7 |
| B. No es parte | Se crea su propio pendiente, y EP-023 sigue sin tocarse |

**Recomiendo A.** El H-3 apareció escribiendo EP-023 y toca la sección 3 de sus siete HU, incluida la HU-001, que ya está aprobada. Repetir el texto de la épica en cada HU va contra «cada documento sale del anterior», que es el centro del pendiente.

¿A o B?

### 49 · Usuario, 2026-10-01 22:41:46
> 
> A. Deben ser las 7

**Agente**, 2026-10-01 22:41:52
<!-- agente: efec0366-5dc8-492d-8a37-30bb724205b4 -->

Falta la palabra que dice qué se espera (`01·C28`). Para seguir el análisis 4 con la opción A en las siete HU, escribir «Analicemos» o «Continúe».

### 50 · Usuario, 2026-10-01 22:42:49
> Continúe

**Agente**, 2026-10-01 22:43:06
<!-- agente: 5fd98380-ae39-4d87-a005-24b62d8222ec -->

Queda la opción A: el H-3 es parte del plan en curso y toca las siete HU.

**Lo siguiente es qué va en «Contexto y descripción» de una HU que sale de una épica.**

Propongo esto: el contexto dice qué parte del problema de la épica resuelve esa HU y enlaza a la sección 3.1 de la épica para lo general. Para que yo no invente esa relación, la debe fijar la propuesta final del análisis, junto a cada HU.

Así se reparte el problema del pendiente entre las siete HU. Es propuesta mía:

| HU | Parte del problema que resuelve |
|---|---|
| HU-001 | No hay un documento que fije el alcance antes de la HU, y lo que pasa la conversación al análisis hay que configurarlo a mano |
| HU-002 | Nada obliga a que cada documento salga del anterior |
| HU-003 | El hallazgo y el pendiente cargan campos que son del análisis, así que no salen de su documento anterior |
| HU-004 | Nada detiene al agente cuando aparece un hallazgo al ejecutar el plan |
| HU-005 | El agente agrega lo que no se pidió, porque `01·C14` se lo permite |
| HU-006 | No resuelve una frase del problema: ataca su «por qué importa», para que los hallazgos que se podían evitar no se repitan |
| HU-007 | Nada detiene al agente cuando trabaja fuera del plan aprobado, y la plantilla del plan no permite comprobarlo con un programa |

**Y la plantilla de la HU** tendría que distinguir los dos casos:
- si la HU sale directo de un pendiente, el contexto es el problema del pendiente;
- si sale de una épica, es la parte del problema de la épica que le toca, con el enlace.

¿Así quedan el reparto y el cambio de la plantilla?

### 51 · Usuario, 2026-10-01 22:46:22
> Hágalo

**Agente**, 2026-10-01 22:47:19
<!-- agente: 705508d7-f99a-4ab6-be40-93a5b41a86aa -->

Quedó escrito en el [análisis 4](analisis-4.md):

- **5 conclusiones**: el H-3 es parte del plan; el contexto de una HU que sale de una épica es la parte del problema que le toca, con el enlace; esa parte la fija la propuesta final; el reparto de las siete HU; y el cambio a la plantilla de la HU.
- **3 puntos de lo que se tiene que hacer**:
  1. la plantilla de la HU distingue los dos casos y va a la HU-002;
  2. la plantilla del análisis pide la parte del problema junto a cada HU y va a la HU-001;
  3. reescribir el contexto de las siete HU.
- **El pendiente sigue en la V3**: «nada obliga a que cada documento salga del anterior» ya cubre este caso.

El punto 2 lo saqué de la conclusión 3: si la propuesta final debe fijar esa parte, la plantilla del análisis tiene que pedirla. Conviene revisarlo.

Todavía no toqué las HU ni las plantillas:
- **Las HU** se escriben al aprobarse el análisis (conclusión 53 del análisis 1).
- **Las plantillas** se cambian dentro de su HU, con su plan y sus pruebas, como manda el `CLAUDE.md` del repo.

Para cerrar hace falta «Apruebo el análisis». Después reescribo el contexto de las siete HU y sumo los dos puntos nuevos a la épica, que pasa de 39 a 41 puntos.

### 52 · Usuario, 2026-10-01 22:55:15
> Pregunta: osea que ya quedó?

**Agente**, 2026-10-01 22:55:21
<!-- agente: 4c14f2fe-e535-4de3-8b2b-ab3bd316b5f0 -->

El análisis 4 está completo y no le queda ninguna pregunta abierta. Falta que el usuario lo apruebe con «Apruebo el análisis».

Después de la aprobación quedan dos cosas por hacer:

1. Reescribir el contexto de las siete HU con el reparto acordado.
2. Sumar a la épica los dos puntos nuevos: uno va a la HU-002 y otro a la HU-001.

### 53 · Usuario, 2026-10-01 22:55:58
> Apruebo el análisis

**Agente**, 2026-10-01 22:57:15
<!-- agente: 0383bba5-e2f8-42f7-a40a-043bed5074ab -->

Lo marqué como aprobado. Ahora aplico lo que se tiene que hacer: el contexto de las siete HU y los dos criterios nuevos.

El análisis 4 quedó aprobado en el turno 53, y ya apliqué lo que se tiene que hacer.

- **Contexto de las siete HU:** cada una dice qué parte del problema de la épica resuelve, con el enlace a la sección 3.1 de la épica. La HU-006 dice que ataca el «por qué importa».
- **HU-001:** suma el CA-16, para que la plantilla del análisis pida la parte del problema junto a cada HU.
- **HU-002:** suma el CA-03, para que la plantilla de la HU distinga si su contexto sale de un pendiente o de una épica.
- **Épica:** pasa de 39 a 41 puntos, enlaza el análisis 4 y lo anota en su bitácora.

No hay enlaces rotos y el validador da cero marcas.

La HU-001 estaba aprobada y cambió: tiene un contexto nuevo y el CA-16. La dejé con su aprobación y anoté el cambio en su bitácora. ¿Se mantiene aprobada o la revisa de nuevo?

> acá termina la conversación

---

## Lo acordado

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis, que después se quitaron para no repetirlas; cada punto conserva el número de su conclusión. No decide nada nuevo.

1. Es parte del plan en curso: El H-3 apareció escribiendo EP-023 y toca sus siete HU, incluida la HU-001 ya aprobada. Se resuelve antes de aprobar las demás (Turnos 49 y 50).
2. Qué va en el contexto de una HU que sale de una épica: La parte del problema de la épica que esa HU resuelve, con el enlace a la épica para lo general. El problema completo vive solo en la épica (Turnos 50 y 51).
3. Quién fija esa parte: La propuesta final del análisis, junto a cada HU, para que el agente no la invente (Turnos 50 y 51).
4. El reparto en EP-023: HU-001: no hay un documento que fije el alcance antes de la HU, y lo que pasa la conversación al análisis hay que configurarlo a mano. HU-002: nada obliga a que cada documento salga del anterior. HU-003: el hallazgo y el pendiente cargan campos que son del análisis. HU-004: nada detiene al agente cuando aparece un hallazgo al ejecutar el plan. HU-005: el agente agrega lo que no se pidió, porque `01·C14` se lo permite. HU-006: ataca el «por qué importa» del problema, para que los hallazgos evitables no se repitan. HU-007: nada detiene al agente cuando trabaja fuera del plan aprobado, y la plantilla del plan no permite comprobarlo con un programa (Turnos 50 y 51).
5. La plantilla de la HU: Distingue dos casos: si la HU sale directo de un pendiente, el contexto es el problema del pendiente; si sale de una épica, es la parte del problema de la épica que le toca, con el enlace (Turnos 50 y 51).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `13·DOC15` (la HU se escribe desde la plantilla central) y `13·DOC16` (la épica enlaza sus HU y cada HU nombra su épica). Choca la plantilla de la HU, que pide en «Contexto y descripción» el problema del pendiente tal cual; se resuelve en el punto 1 de lo que se tiene que hacer.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| EP-023 | El problema del pendiente está en la sección 3.1 de la [épica](../../epica.md) y copiado en la sección 3 de sus siete HU |
| Plantilla de la HU | [`04-HU.md`](../../../../../plantillas/ciclo-vida-proyectos/04-HU.md) no distingue la HU que sale de un pendiente de la que sale de una épica |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| S-064 | Un registro en dos sitios deja el segundo atrás. Lo recoge la conclusión 2 |
| Conclusión 6 del análisis 1 | Cada documento conserva lo del anterior y le agrega precisión, sin repetirlo. Lo recoge la conclusión 2 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Reciben la plantilla de la HU cambiada. Es un cambio de plantilla que no obliga a rehacer las HU ya escritas: MENOR según `20·M10` |
| Normas y leyes | Ninguna aplica |
| Herramientas | La conversación entró con el guion intermedio, prendido escribiendo a mano el archivo de estado |

### Dónde más puede pasar

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| HU que sale directo de un pendiente | Cualquier proyecto | El contexto repite o no dice el problema | Conclusión 5 |
| HU que sale de una épica | Cualquier épica | Cada HU repite el problema completo | Conclusiones 2 y 3 |

---

## Propuesta final: hallazgo y pendiente

> El H-3 no cambia. El pendiente sigue en la V3: su problema ya dice «nada obliga a que cada documento salga del anterior», y este hallazgo es un caso de eso. EP-023 suma un punto, que va a la HU-002.

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | El agente copió el mismo contexto en siete HU porque la plantilla lo pedía, sin ver que ese texto ya estaba en la épica | Falló | Por escribir |
| 2 | El agente abrió el análisis con el hallazgo equivocado (H-2) y el usuario tuvo que señalar cuál era | Falló | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que la plantilla de la HU distinga los dos casos de «Contexto y descripción»: el problema del pendiente, o la parte del problema de la épica con su enlace | 5 | EP-023, HU-002 |
| 2 | Que la plantilla del análisis pida, junto a cada HU de la propuesta final, la parte del problema que resuelve | 3 | EP-023, HU-001 |
| 3 | Reescribir el contexto de las siete HU de EP-023 con el reparto de la conclusión 4 | 2, 4 | EP-023, al aprobar este análisis |

## Lo que aporta al análisis principal

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

**Resultado:** Aclara.

**Lo que suma al análisis principal:** El contexto de cada HU que sale de una épica es la parte del problema que le toca.
