# Resultado de Pruebas — Fase `A-EP-003-HU-012-una-sola-palabra-por-estado`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado, y si cada criterio de aceptación quedó cumplido**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md); lo que quedó construido, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-012-una-sola-palabra-por-estado` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-26 |
| **Ciclo** | 2. El ciclo 1 dejó siete pruebas de otra clase en rojo |

---

## 2. Veredicto

**Cumple.**

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 7 de 7 | 7 de 7 |
| Criterios en verde | 4 de 4 | 4 de 4 |
| Historias dentro del vocabulario | 115 de 115 | **115 de 115** |
| **Historias que cambiaron de sentido** | **0** | **0** |
| Diferencia en la cuenta de completas | **0** | **0** |
| Sabotajes cazados | Todos | 7 de 7 |
| Fallas en la suite completa | 0 | 0, sobre **396 pruebas** |

---

## 3. Resultado por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 | El vocabulario vive en un solo sitio | ✅ |
| CP-002 | Las 115 usan el vocabulario, y el cambio es de sinónimo | ✅ |
| CP-003 | Ninguna historia cambió de sentido | ✅ |
| CP-004 | El estado inventado se avisa | ✅ |
| CP-005 | Reporta, no corrige, y sale por `validar` | ✅ |
| CP-006 | Los bordes | ✅, **con una decisión distinta a la del plan** |
| CP-007 | La versión subió y lo dice | ✅ |

### CP-001 — Un solo sitio define

El glosario gana su sección 5 con los nueve estados y los tres conjuntos. Los cuatro moldes citan esa sección en vez de listar; se comprobó que ninguno conserve su lista vieja. **La lista de la épica, que estaba escrita dos veces sin coincidir, ahora está una sola vez.**

Y «terminado» es `Terminada` en los tres conjuntos, que es el corazón de la historia.

### CP-002 — Las 115 usan el vocabulario

| Qué | Resultado |
|---|---|
| Historias comparadas contra la foto previa | 115 |
| Fuera del vocabulario | **0** |
| Cambios fuera del mapa declarado en el plan | **0** |
| Sin cambio, porque ya estaban bien | 4 |
| Cambiadas | 111 |

**El texto que seguía a la palabra se conservó entero.** `Cumplida — los tres CA verificados el 2026-08-17` quedó `Terminada — los tres CA verificados el 2026-08-17`.

### CP-003 — Ninguna cambió de sentido

Los dos caminos, independientes:

| Qué | Antes | Después |
|---|---|---|
| Línea del inventario | 115 · 72 · 43 | **115 · 72 · 43** |
| Historias clasificadas como cerradas | 36 | **36** |
| Historias que cambiaron de abierto a cerrado, o al revés | — | **0** |

**Los dos caminos miran cosas distintas**, y por eso hacen falta los dos: la cuenta del árbol mira documentos presentes; la clasificación mira el campo `Estado`, que es lo que esta fase toca.

### CP-004 y CP-005 — La comprobación

| Situación | Resultado |
|---|---|
| Estado del vocabulario | 0 avisos |
| `Casi lista` | 1 aviso, que lo nombra y dice cuáles valen |
| `Cancelada` (existe, pero es de una épica) | 1 aviso |
| El archivo, comparado en **bytes** después de correr | **Idéntico** |
| El aviso, buscado a través de `validar` | **Sale** |
| Quitar `Terminada` del glosario | **Cambia qué acepta** el validador |

**El último es el que más importa.** Si el vocabulario estuviera escrito en el código, quitarlo del glosario no cambiaría nada — y volverían las dos copias, que es el problema entero de esta fase.

### CP-006 — Los bordes, con una decisión distinta a la del plan

| Borde | Plan | Real |
|---|---|---|
| Estado con texto detrás | válido | ✅ válido |
| Estado en negrita | válido | ✅ válido |
| Estado en minúscula | por decidir | **se reporta**, y se declara: aceptar `terminada` abriría la puerta a que vuelvan las variantes |
| Campo vacío | se reporta | ✅ se reporta, distinto de «falta» |
| **Sin campo `Estado`** | se reporta | **NO se reporta.** Ver §4.3 |

### CP-007 — La versión

`VERSION` pasó de `34.2.0` a **`35.0.0`**, y es **MAYOR ⚠ obliga a migrar**: quien ya tenga documentos escritos cambia la palabra de su campo `Estado`. La entrada trae la tabla de qué pasa a qué. `validar.py versionado` pasa.

**Se eligió MAYOR y no MENOR**, aunque la comprobación solo avise. El precedente del propio registro es claro: *«un proyecto que ya tenga su inventario de funcionalidades escrito lo reescribe con la estructura nueva»* también fue MAYOR. Llamarlo MENOR porque «solo avisa» sería esconderse en un tecnicismo: **un aviso permanente es trabajo pendiente, no información.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Siete, restaurados **con copia**.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | El vocabulario se escribe en el código | Cazado | Cazado |
| 2 | La comprobación se descuelga de `validar` | Cazado | Cazado |
| 3 | Se compara la frase entera, no la palabra | Cazado (3) | Cazado (3) |
| 4 | El aviso no dice cuáles valen | Cazado (2) | Cazado (2) |
| 5 | La comprobación **corrige** el archivo | Cazado | Cazado |
| 6 | El glosario rompe la palabra compartida | Cazado | Cazado |
| 7 | Un molde vuelve a listar por su cuenta | Cazado | Cazado |

**Ninguno pasó en verde**, que es la primera vez en la sesión.

### 4.2 El defecto que encontró la suite completa

**En el ciclo 1, siete pruebas de la clase `Fases` quedaron en rojo** — ninguna de esta fase.

La causa: la comprobación reportaba también las historias **sin campo de estado**, como el plan pedía. Los árboles de mentira de esas siete no traen ese campo, porque no están probando eso.

**El rojo no era de las siete: era del alcance.** Y en un proyecto habría hecho lo mismo con cualquier historia mínima — un aviso permanente sobre documentos que están bien para lo que son.

Se sacó de esta comprobación, con su porqué escrito al lado. **No es taparlo:** que el campo falte sigue siendo un problema, y pasa a quien comprueba que un documento traiga sus campos. Queda `S-050` y una deuda en el cierre §6.

**Lo encontró correr la suite entera**, no las clases tocadas. Correr solo lo propio la habría dejado pasar.

### 4.3 Un rastro que resultó no serlo

El guion contó **110 historias modificadas** después de los sabotajes y lo reportó como posible daño. **No lo era:** eran las 111 normalizadas por `T-05`, sin commitear todavía. Se comprobó mirando el `diff` de una: decía `Backlog` → `Pendiente`, que es el trabajo de la fase, no del sabotaje.

Vale anotarlo porque la comprobación de rastros, tal como está escrita, **no distingue el trabajo pendiente del daño**. Con el árbol limpio funciona; con trabajo sin guardar, hay que mirar el `diff`.

### 4.4 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

### 4.5 Una prueba toca el glosario real, y lo devuelve

`test_cambiar_el_glosario_cambia_que_acepta` **tiene** que tocar el archivo real: es la única forma de comprobar que el vocabulario sale de ahí. Guarda una copia en bytes, la restaura en el `cleanup`, y se verificó con `git diff` que el glosario quedó con sus 34 líneas nuevas y **ninguna borrada**.

---

## 5. Trazabilidad criterio a evidencia

| CA / RNF | Evidencia | Estado |
|---|---|---|
| CA-01 — el glosario define, una vez | CP-001 | ✅ |
| CA-02 — las 115 usan el vocabulario | CP-002 | ✅ |
| CA-02 — ninguna cambió de sentido | CP-003, por dos caminos | ✅ |
| CA-03 — el estado inventado se avisa | CP-004 | ✅ |
| CA-03 — y no corrige, y sale por `validar` | CP-005 | ✅ |
| CA-04 — la versión sube y lo dice | CP-007 | ✅ |
| RNF-01 — se sabe qué poner leyendo un solo molde | CP-001 paso 4 | ✅ |
| RNF-02 — cada cambio se puede comparar | CP-002, contra la foto | ✅ |

---

## 6. Veredicto final

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 4 de 4 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno |
| **Suite** | `python validadores/pruebas.py`: **396 pruebas, OK** |

### Defectos encontrados y corregidos

| ID | Qué era | Cómo se cazó | Estado |
|---|---|---|---|
| DEF-01 | El guion de normalización quitaba el punto de `En implementación. CA-01…` y dejaba `En curso CA-01…` | El **ensayo en seco**, antes de aplicar | Corregido |
| DEF-02 | El mismo guion dejaba `Terminada** Los tres…`: el `**` que cierra la negrita queda **en medio**, y `rstrip` no lo alcanza | El ensayo en seco, simulando los tres casos difíciles | Corregido |
| DEF-03 | La comprobación reportaba fuera de su tema y dejaba siete pruebas ajenas en rojo | La **suite completa** | Corregido. `S-050` |

**Los dos primeros los cazó el ensayo en seco, no una prueba.** Aplicar directo habría dañado 43 documentos de forma difícil de ver: el texto se lee casi bien.

---

## 7. Lo que este resultado NO dice

- **No dice que todos los documentos del proyecto usen el vocabulario.** Dice que las **historias** sí. Las épicas y los planes tienen su conjunto definido y su molde citando, pero **no hay comprobación para ellos todavía**.
- **No dice que un documento sin campo de estado esté bien.** Dice que esta comprobación no es quien lo reporta.
- **No cubre los proyectos que heredan el estándar.** Sus documentos se avisarán cuando corran `validar.py fases`, y migrar es decisión suya, como dice el `CHANGELOG`.
