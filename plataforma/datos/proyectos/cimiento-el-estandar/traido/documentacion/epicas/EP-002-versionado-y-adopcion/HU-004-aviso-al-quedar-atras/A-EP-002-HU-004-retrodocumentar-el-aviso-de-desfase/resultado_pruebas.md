# Resultado de Pruebas — Fase A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |
| **Proyecto de prueba** | **shopnest-mesa**, que declara `27.2.0` con el estándar en `32.0.1` |

---

## 1. Ejecución caso por caso

### CA-01 · El proyecto atrasado recibe el aviso al abrir sesión

El aviso **existe** y dice lo que tiene que decir:

```
$ python validadores/validar.py version --raiz <shopnest-mesa>
[AVISO] CLAUDE.md — el proyecto declara v27.2.0, el estándar va en v32.0.1:
        subir es decisión del usuario; las fases cerradas quedan selladas
```

**Pero nadie lo entrega al abrir sesión.** El enganche de apertura es `hook_sesion.py`, y lo que hace es llamar a `sesion.revisar()` y a `cargador.contexto()`. Corrido `sesion.revisar()` sobre shopnest-mesa, devuelve **un solo hallazgo**, y no es este:

```
[AVISO] CLAUDE.md — la plantilla central cambió después de este CLAUDE.md — C18
```

Ni `sesion.py` ni `cargador.py` nombran la versión. El aviso solo aparece si alguien escribe el comando a mano, y **el criterio dice «al abrir sesión»**.

**Resultado del criterio: No cumple.**

### CA-02 · El proyecto al día no recibe nada

Se copió el `CLAUDE.md` a una carpeta temporal declarando la versión vigente:

```
$ python validadores/validar.py version --raiz C:/tmp/prueba-aldia
== Versión del estándar · C:/tmp/prueba-aldia ==
OK: sin incumplimientos.
```

Silencio, que es lo pedido.

**Resultado del criterio: Cumple.**

### CA-03 · El aviso no migra ni detiene

Tres comprobaciones:

| Qué | Resultado |
|---|---|
| Severidad del hallazgo | `AVISO`, no `FALLA` |
| Código de salida | **0** |
| Archivos del proyecto modificados | ninguno |

No migra y no detiene.

**Resultado del criterio: Cumple.**

---

## 2. Verificaciones manuales

**Lo que el plan daba por cierto y no lo es.** Su línea base, del 2026-08-17, dice: *«el enganche de apertura, que entrega el aviso en pantalla sin que nadie lo pida (RN-01)»*. Comprobado el 2026-08-22 leyendo `hook_sesion.py`, `sesion.py` y `cargador.py`: **ninguno de los tres mira la versión**.

Es la cuarta fase seguida de esta jornada cuyo plan afirma algo que hoy no se sostiene.

**Lo que el plan sí anticipaba bien:** el mensaje nombra las dos versiones y no dice qué cambió entre ellas. La decisión 24 del [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md) ya fijó qué debería decir —la versión, su tipo y su título, al nivel de entrada del registro— y eso sigue sin implementarse.

---

## 3. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Crítica** | El aviso de desfase no llega al abrir sesión. Existe como subcomando y hay que pedirlo a mano, que es justo lo que la HU quería evitar | **Abierto**, necesita pendiente |
| D-02 | Alta | El aviso no dice **qué cambió** entre las dos versiones, y la decisión 24 ya fijó qué debería decir | **Abierto**, mismo pendiente |
| D-03 | Baja | El plan afirmaba que el enganche de apertura ya lo entregaba | **Cerrado** al comprobarlo |

---

## 4. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, llega al abrir sesión | Lectura de los tres módulos del arranque, y corrida de `sesion.revisar()` | **No cumple** |
| CA-02, el que está al día no recibe nada | Copia temporal declarando la vigente | Cumple |
| CA-03, no migra ni detiene | Severidad, código de salida y archivos sin tocar | Cumple |

## 4.1 Lo que el plan exigía

El plan quería dejar constancia de tres estados. Los tres se comprobaron, y el primero salió al revés de lo que todos suponían: **la funcionalidad central de esta historia no está conectada**.

Vale la pena decir por qué nadie lo había notado. El aviso se ve todos los días... **en este repositorio**, donde el agente corre las comprobaciones a mano. En un proyecto instalado, que es donde tiene que llegar, no aparece nunca.

---

## 5. Veredicto de la fase

**Concepto:** No cumple.

**Justificación:** el CA-01 quedó en rojo, y es el criterio principal de la historia: el aviso al quedar atrás no llega al abrir sesión. Los otros dos cumplen.

**Qué falta para que cumpla:** que el enganche de apertura entregue el aviso junto con lo demás que ya entrega, y que el mensaje diga qué cambió entre las dos versiones.

---

## 6. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El aviso, cuando se pide a mano | `validar.py version --raiz <proyecto>` |
| EV-02 | Lo que sí entrega el arranque | `sesion.revisar()` sobre shopnest-mesa: un hallazgo, y no es este |
| EV-03 | El silencio del que está al día | Copia temporal con la versión vigente |
| EV-04 | Que no detiene | Código de salida 0 y ningún archivo tocado |

---

## 7. Ciclos anteriores

Ninguno: la fase estaba aprobada desde el 2026-08-17 y nunca se había ejecutado.
