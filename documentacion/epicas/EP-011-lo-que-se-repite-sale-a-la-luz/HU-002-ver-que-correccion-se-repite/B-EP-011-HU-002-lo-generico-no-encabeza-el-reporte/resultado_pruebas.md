# Resultado de Pruebas — Fase `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte` |
| **HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre lo indexado de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |
| Pruebas del módulo | **47** (9 nuevas) |

**El reporte, antes y después:**

| Antes | Después |
|---|---|
| `22 debe quedar` | `11 estoy preguntando · 8 sesiones` |
| `21 meta reglas` | `15 plan trabajo · 7 sesiones` |
| `19 puede cerrar` | `7 historico chat · 7 sesiones` |
| `19 historico chat` | `9 espanol colombiano · 5 sesiones` |
| `17 debe tener` | `8 suba git · 5 sesiones` |

**«Español colombiano» pasó del puesto 21 al cuarto.** Y las tres filas genéricas de las cinco primeras se fueron.

---

## 2. Ejecución caso por caso

### CP-001 — Lo dicho en muchas sesiones no es tema

Sobre diez sesiones con «debe quedar» en todas: no aparece en el reporte, y `vocabulario_de_la_casa` incluye «debe».

Sobre el corpus real, de 67 sesiones, el vocabulario calculado son **40 palabras**: «debe», «archivo», «carpeta», «cada», «cerrar», «crear» y «dice». Ninguna se escribió a mano.

**Resultado: pasa.**

### CP-002 — Lo que sí es tema queda

El caso que decide, porque un filtro que limpia de más deja un reporte limpio y vacío.

- En las pruebas: el tema aparece en dos de diez sesiones, entra al reporte, y su palabra **no** está en el vocabulario.
- **Sobre lo real:** «espanol colombiano» sigue ahí, con nueve repeticiones en cinco sesiones.

**Resultado: pasa.**

### CP-003 — Las rutas pegadas no cuentan

| Entrada | Salió |
|---|---|
| «mire c:/Ing. Jose/ia/agente y arregle» | «mire y arregle» |
| «revise historico-chat/2026-01-02.md y me dice» | «revise» y «me dice» |

**Esto sacó dos filas de las diez primeras:** «ing jose» (12 sesiones) y «users user» (6), que salían del nombre de una carpeta pegada en un mensaje.

**Resultado: pasa.**

### CP-004 — Con pocas sesiones no se filtra

Con dos sesiones, el vocabulario sale vacío y el reporte no queda mudo.

**Por qué importa:** con el umbral aplicado a un corpus chico, cualquier palabra dicha dos veces pasa y el filtro se lleva todo. Un reporte vacío se lee como «no hubo nada», que es mentira.

**Resultado: pasa.**

### CP-005 — Repetir en un solo día no cuenta, y primero lo de más días

| Entrada | Salió |
|---|---|
| Lo mismo tres veces el mismo día | no entra |
| Lo mismo en dos días distintos | entra |
| Cuatro días contra diez veces en dos días | primero el de cuatro días |

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las primeras filas del reporte | **De ahí sí sale algo.** «estoy preguntando» aparece en ocho sesiones distintas: es el usuario aclarando que pregunta, no que ordena |
| «Español colombiano» | Sigue, en el cuarto puesto |
| El vocabulario calculado | Las 40 palabras son de la casa, no temas |

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | **La mejora que se propuso y se aprobó no funcionaba.** Ordenar por sesiones distintas dejaba «debe quedar» de primero igual, con 14 sesiones | Alta | Se midió **antes** de construirla y se dijo. El mecanismo que sí sirve salió de medir tres formas y comparar |
| D-02 | El primer filtro se llevaba todo en las pruebas: sobre diez sesiones, una palabra en tres ya pasa el umbral | Media | Arreglado con el resguardo de corpus chico, y la mentira de la prueba ajustada a la franja donde vive un tema |
| D-03 | Las pruebas de la fase A daban por bueno repetir en un solo día | Media | Se repartieron en días distintos. **El criterio cambió y las pruebas cambiaron con él**, no al revés |

---

## 5. Veredicto

| Qué | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-002-ver-que-correccion-se-repite.md#ca-01--el-reporte-sale-por-período) | CP-001 a CP-005 | **Cumple** |
| Riesgo 2 de la §9 — que no diga lo obvio | §3 | **Cumple**, y queda a juicio del usuario |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Medir las tres formas antes de elegir | Hecho, y dos se descartaron con su número |
| El vocabulario calculado, no escrito | Hecho: 40 palabras salidas del corpus |
| Las rutas pegadas fuera | Hecho: dos filas menos |
| El resguardo de corpus chico | Hecho |
| El reporte sobre lo real, escrito | Hecho, antes y después |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

El reporte pasó de encabezarse con la forma de redactar del usuario a encabezarse con lo que de verdad tuvo que repetir. La comprobación que importaba —que el filtro no se llevara lo bueno— se hizo con el único caso conocido de regla que faltaba, y sigue ahí.

**Lo que esta fase no puede decir**, y es el riesgo 2 de la historia: si de esas filas nace una regla. Lo juzga el usuario. **Lo que sí se puede decir es que ahora hay de dónde**: «estoy preguntando», ocho sesiones distintas.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 47 pruebas del módulo | `plataforma/nucleo/medicion/tests_repeticion.py` |
| EV-02 | El reporte antes y después | §1 y §2 |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
