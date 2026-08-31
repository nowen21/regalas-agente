# Resultado de Pruebas — Fase `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca` |
| **HU** | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../HU-001-buscar-en-lo-conversado.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre este repositorio conectado a la plataforma |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 7 |
| Ejecutados | 7 |
| Pasaron | 7 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **33** (22 del módulo, 11 del lector de turnos) |

**Sobre el histórico de verdad, que es lo que importa:**

| | Cuánto |
|---|---|
| Archivos en `historico-chat/` | 329 |
| Sesiones indexadas | **67** |
| Mensajes indexados | **3 720** |
| Cuánto tardó | **35,7 s** |
| Archivos del histórico que cambiaron | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Lo conversado se encuentra, y se ve en qué mensaje

Sobre el histórico real:

```
$ python manage.py buscar_en_lo_conversado "menos es más" --limite 3
2026-08-17 · historico-chat/2026-08-17-sesion-4.md · usuario: menos es más
2026-08-17 · historico-chat/2026-08-17-sesion-4.md · usuario: que significa menos es más para usted?
2026-08-17 · historico-chat/2026-08-17-sesion-4.md · usuario: «Menos es más» significa que una explicación…
3 mensaje(s).
```

Cada resultado dice la fecha, la sesión, quién habló y qué dijo. Los dos lados de la conversación se indexan: buscar algo que dijo el agente también lo encuentra.

**Resultado: pasa.**

### CP-002 — El índice se borra entero y vuelve completo

Se indexa, se borra todo, se rehace: la misma cuenta de sesiones y de mensajes. Indexar dos veces no duplica, y una sesión que creció desde la última pasada queda completa, no partida.

**Resultado: pasa.**

### CP-003 — Lo que sale mal se dice

| Entrada | Qué pasó |
|---|---|
| Un archivo que no es UTF-8 | Se reporta nombrándolo; el resto se indexa igual |
| Un archivo sin marcas de turno | Una sesión con cero mensajes |
| Un proyecto sin `historico-chat/` | Cuenta en cero, sin reventar |
| Un proyecto con la ruta perdida | Se dice, con la ruta que se buscó |
| `README.md` dentro del histórico | No se indexa |

**Resultado: pasa.**

### CP-004 — Indexar no toca el histórico

**El criterio de «que NO pase» de esta historia, medido sobre los 329 archivos reales:**

```
== Cimiento, el estandar ==
  archivos en el historico: 329
  indexado: 67 sesion(es), 3720 mensaje(s), en 35.7 s
  CA-04 · archivos del historico que cambiaron: 0
```

Se comparó **nombre, tamaño y huella del contenido** de cada archivo, antes y después. No se miró la fecha de modificación: un programa puede reescribir el mismo texto y dejarla igual, y entonces la fecha diría que no pasó nada.

**Resultado: pasa.**

### CP-005 — Ninguna credencial queda en lo indexado

Se le pasó a los 3 720 mensajes el detector de secretos del estándar:

```
  mensajes indexados: 3720
  con forma de credencial: 2
```

**Los dos se miraron uno por uno, y ninguno es una credencial.** Los dos son la misma línea de una sesión donde el agente estaba explicando cómo se tapan las claves, y en las dos el valor es literalmente `«enmascarado»`:

```
password: "«enmascarado»" y API_KEY=«enmascarado»  →  las dos tapadas
```

El detector reconoce **la forma** `password: "…"`, y ahí la forma está pero el valor es la máscara. Es decir: la clave se tapó antes de escribirse, que es donde tiene que taparse, y este módulo indexó lo que había sin destaparla.

**Resultado: pasa**, y queda escrito qué eran los dos, para que la próxima corrida no tenga que volver a averiguarlo.

### CP-006 — Los dos silencios se distinguen

```
$ python manage.py buscar_en_lo_conversado "xilofono cuantico"
Ninguna conversación dice «xilofono cuantico».
```

Con el índice vacío responde otra cosa: que no hay conversaciones indexadas todavía, y por dónde indexarlas.

**Resultado: pasa.**

### CP-007 — Volumen real

**35,7 segundos** para 67 sesiones y 3 720 mensajes. Es el riesgo `B-01` del plan, cerrado con un número: indexar lo acumulado no pesa, y se hace una vez.

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las dos formas de credencial encontradas | Ninguna es una clave: las dos traen la máscara |
| La búsqueda de una palabra que sí se dijo, en el histórico real | Sale, con su sesión y su turno |
| Los dos silencios, leídos como los lee una persona | Dicen cosas distintas |

**Ninguna prueba escribió dentro de `historico-chat/`.** El histórico se leyó, y el `CP-004` comprueba que quedó intacto.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | **Dos pruebas de la plataforma estaban en rojo por la subida de versión de hoy**, y no por esta fase. Su proyecto de mentiras declaraba `34.1.0` a mano, y al pasar el estándar a `37.1.0` empezaron a recibir el aviso de desfase que daban por ausente | Alta | Arreglado acá: leen la versión publicada en vez de escribirla |

**Lo que ese defecto destapa es más grande que él.** La batería de la plataforma **no la corre nada** del estándar: `validar.py internas` mira solo `validadores/tests/`. Por eso una subida de versión la puso en rojo esta mañana y nadie se enteró hasta esta tarde. Queda como señal.

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-001-buscar-en-lo-conversado.md#ca-01--lo-conversado-se-encuentra-por-una-palabra-suya) | CP-001 | **Cumple** |
| [CA-02](../HU-001-buscar-en-lo-conversado.md#ca-02--el-índice-se-puede-borrar-y-rehacer) | CP-002 | **Cumple** |
| [CA-03](../HU-001-buscar-en-lo-conversado.md#ca-03--ninguna-credencial-queda-en-lo-indexado) | CP-005 | **Cumple** |
| [CA-04](../HU-001-buscar-en-lo-conversado.md#ca-04--indexar-no-toca-el-histórico) | CP-004 | **Cumple** |
| Transversal — sin coincidencias se dice | CP-006 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| `historico.turnos`, en el estándar | Hecha, con 11 pruebas |
| El módulo `medicion` con sus dos entidades | Hecho, con 22 pruebas |
| Indexar, buscar y rehacer | Hechos, y corridos sobre el histórico real |
| Las dos órdenes de consola | Hechas |
| El histórico intacto | Comprobado sobre 329 archivos |
| Cuánto tarda | 35,7 s, escrito |
| La §13 de la especificación | Nombra esta fase |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Los cuatro criterios y el transversal quedaron cumplidos con evidencia, y los dos que más importaban se comprobaron **sobre el histórico de verdad**, no sobre uno inventado: ningún archivo cambió, y ninguna credencial quedó indexada.

**Lo que la fase no entrega, y está declarado:** pantalla —la especificación lo permite— y el conteo de lo repetido, que es la `HU-002`. Y sigue en pie el supuesto que puede fallar en silencio: una conversación que no pase por el enganche no se indexa y nadie se entera.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | La corrida sobre el histórico real | [historico-chat/scripts/2026-08-31/medir-lo-indexado.py](../../../../../historico-chat/scripts/2026-08-31/medir-lo-indexado.py) |
| EV-02 | Las 11 pruebas del lector de turnos | `validadores/tests/test_la_transcripcion_se_parte_en_turnos.py` |
| EV-03 | Las 22 pruebas del módulo | `plataforma/nucleo/medicion/tests.py` |
| EV-04 | Las dos órdenes corridas | §2, `CP-001` y `CP-006` |
| EV-05 | El detector de secretos sobre lo indexado | §2, `CP-005` |
| EV-06 | El retrato de la carpeta antes y después | §2, `CP-004` |
| EV-07 | La §13 de la especificación | [documentacion/medicion/spec.md](../../../../medicion/spec.md) |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
