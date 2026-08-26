# Funcionalidad implementada — Fase A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia (módulo Memoria)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** El criterio de cuál va dónde quedó escrito y resuelve el caso de borde; los 18 recuerdos traen sus tres partes. Pero **una misma cosa está guardada en los dos sitios y las dos versiones ya divergen**, y eso es justo lo que el CA-01 existía para impedir.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |
| **Módulo** | Memoria — [`historico-chat/memory/`](../../../../../historico-chat/memory/memory.md) y `memoria/senales.db` |
| **Especificación del módulo** | No la hay aparte: la especificación son los CA de [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-005: [CA-01](../HU-005-separar-aprendizaje-de-preferencia.md#ca-01--las-dos-cosas-se-guardan-por-separado), [CA-02](../HU-005-separar-aprendizaje-de-preferencia.md#ca-02--la-preferencia-dice-por-qué-se-pidió) y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 |
| **Commit** | Pendiente de autorización del usuario |

---

## 1. Qué se implementó — resumen

**Lo único que se escribió de nuevo es el criterio que faltaba**, en la cabecera del índice de la memoria. Los dos sitios llevaban meses funcionando y la separación se hacía **por costumbre**: nadie había escrito qué va dónde ni qué hacer con lo que parece de los dos.

Al escribirlo y aplicarlo a cinco casos reales apareció lo que la costumbre no había visto.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Dos sitios distintos, cada uno con su índice | datos | `historico-chat/memory/memory.md` y `memoria/senales.db` | ✅ Ya existía | CP-001 |
| **El criterio de cuál va dónde** | documentación | [`memory.md`](../../../../../historico-chat/memory/memory.md), sección «Cuál va dónde» | ✅ **Escrito acá** | CP-001, CP-002 |
| **Qué hacer con la preferencia que vale para todos** | documentación | La misma sección | ✅ **Escrito acá** | CP-002 |
| **La regla de un solo sitio** — nada se copia, se enlaza | documentación | La misma sección | ✅ **Escrito acá** | `D-01` |
| El recuerdo trae qué se pide, por qué y cómo se aplica | datos | Los 18 archivos de la carpeta | ✅ Ya existía | CP-003 |
| Que se detecte el que no las trae | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ElRecuerdoTraeSusTresPartes` | ✅ Escrito acá | CP-004 |

### 2.2 Criterios de aceptación

| CA | Cómo quedó cubierto | Estado |
|---|---|---|
| CA-01 | Dos sitios con criterio escrito, **y una cosa guardada en los dos, divergida** | ❌ |
| CA-02 | 18 de 18 con sus tres partes; el detector caza al incompleto sin juzgar la redacción | ✅ |
| Transversal · Límites | Lo que parece de los dos tipos tiene criterio, con su caso de borde | ✅ |
| Transversal · No regresión | 0 recuerdos y 0 señales movidos | ✅ |

---

## 3. El criterio que se escribió

La pregunta que separa los tres sitios es **qué haría que eso cambiara**:

| Cambiaría porque… | Es | Va en |
|---|---|---|
| el **usuario** cambia de opinión | Preferencia | Un recuerdo |
| el **código** cambia | Aprendizaje | Una señal |
| cambia lo exigible a **cualquier** proyecto | Regla | `base/` |

Y trae las dos cosas que la costumbre no cubría:

- **El caso de borde.** Cuando una preferencia pasa a ser exigible a cualquiera, **sube a `base/` y el recuerdo no se borra**: se queda con el registro de que el usuario lo pidió y cuántas veces lo repitió. Eso no cabe en una regla. Ya estaba hecho así en [Respuestas cortas](../../../../../historico-chat/memory/respuestas-cortas.md), que es hoy `00·ID9`; ahora está escrito.
- **La regla de un solo sitio.** Nada se guarda dos veces; el segundo enlaza al primero.

---

## 4. Lo que la fase encontró

| Hallazgo | Qué es |
|---|---|
| **La terminología del proyecto está en los dos sitios** — señal `S-002` y recuerdo [Terminología](../../../../../historico-chat/memory/terminologia-agente-vs-estandar.md) | Y **ya dicen cosas distintas**: el recuerdo dice «Cimiento» desde el 2026-08-14, la señal sigue en «el agente = Claude Code» |
| «Fixtures sin secretos literales» es aprendizaje guardado como preferencia | Y además le serviría a cualquier proyecto: se propone subirlo a `base/` |
| De cinco cosas reales clasificadas, **tres** no coinciden con dónde están | Una grave, dos de bajo daño |

**Nada se movió.** Mover un recuerdo cambia lo que rige la sesión, y decidir cuál de las dos versiones manda es del usuario. La fase lo deja anotado en el propio criterio, con el caso citado, para que quien lo lea lo vea.

**Lo que este hallazgo enseña.** El índice de la memoria advertía desde siempre que dos copias del mismo recuerdo terminan diciendo cosas distintas — lo decía del almacén de la herramienta. Está pasando **entre los dos sitios del repositorio**, que es donde nadie lo estaba vigilando.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El criterio se escribe en el índice de la memoria, no en `base/`: qué es preferencia del usuario es de esta casa (`20·M13`) | §2.6 del [plan_trabajo.md](plan_trabajo.md) |
| Lo que esté en el sitio equivocado **se anota, no se mueve** | `D-01` y `D-02` del [resultado](resultado_pruebas.md) |
| La prueba mira que las tres partes **estén**, no si el porqué convence: lo primero es sí o no, lo segundo es criterio | CP-004 del resultado |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Decidir cuál versión de la terminología manda | **Decisión del usuario** |
| Decidir si «fixtures sin secretos literales» sube a `base/` | **Decisión del usuario** (`20·M13`) |
| Que un programa detecte lo guardado en los dos sitios | **Sin destino todavía.** Hoy se encontró leyendo |

**La advertencia que deja esta fase:** el criterio se venía aplicando bien por costumbre, y la costumbre no detecta duplicados. Lo que estaba mal no era ninguna clasificación: era que nadie miraba **si algo estaba dos veces**.
