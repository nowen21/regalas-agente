# HU-022 · andamio.py impone un orden de trabajo incorrecto

> Nace del [pendiente 97](../../../../pendientes/97-andamio-impone-un-orden-de-trabajo-incorrecto.md), aprobado por el usuario el 2026-09-27.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-022 |
| **Épica / Feature** | [EP-005 · Automatismos que no dependen de que alguien se acuerde](../epica.md) |
| **Módulo / Componente** | `validadores/andamio.py` y la regla `02·F23` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | 3 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Pendiente |

## 2. Narrativa

- **Como** quien anota lo que le falta al estándar
- **Quiero** registrar un pendiente sin tener que inventarle antes su historia de usuario
- **Para** que la HU nazca del pendiente aprobado y no fije el alcance antes de tiempo

## 3. Contexto y descripción

`andamio.py` impone un orden de trabajo distinto del que fijó el usuario el 2026-09-27: hallazgo, pendiente, HU y fase. En [andamio.py:286-287](../../../../validadores/andamio.py#L286-L287), `crear_pendiente` exige que la HU exista antes de registrar el pendiente, así que obliga a crear la HU antes de que el pendiente se apruebe.

Ese orden tampoco está escrito en ninguna regla: [`02·F0`](../../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) arranca en el planteamiento y [`02·F23`](../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) cubre de pendiente a fase, pero ninguna nombra el tramo de hallazgo a pendiente.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El orden es hallazgo, pendiente, HU y fase: un pendiente se anota antes de que exista su HU |
| RN-02 | Toda HU es hija de una épica: no hay HU suelta |
| RN-03 | Mientras el pendiente no esté aprobado, su historia se declara «Por asignar» |
| RN-04 | La herramienta hace cumplir el mismo orden que la regla, no otro |
| RN-05 | El orden queda escrito en una regla del estándar |

### 3.2 Supuestos

- Precisar `02·F23` alcanza para escribir el orden sin agregarle una segunda exigencia (`20·M5`). Si no alcanza, el orden va en una regla nueva del capítulo 02.

### 3.3 Fuera de alcance

- Cuándo se construye un pendiente: sigue necesitando su HU y su fase (`02·F23`).
- Asignar la historia de los pendientes que hoy dicen «Por asignar».

## 4. Criterios de aceptación

### CA-01 · Un pendiente se anota sin historia

```gherkin
Dado que el pendiente todavía no tiene HU
Cuando se corre andamio.py pendiente sin --hu
Entonces crea el pendiente con su historia en «Por asignar»
Y le agrega su fila al índice de pendientes
Y no le agrega fila al mapa de historias
```

**Cómo validarlo:**
1. Correr `python validadores/andamio.py pendiente prueba-sin-historia` → resultado esperado: dice qué crearía, sin error.
2. Correr el mismo comando con `--aplicar` sobre una copia del repositorio → resultado esperado: existe `pendientes/NN-prueba-sin-historia.md` con «Por asignar» en la fila «Historia de usuario».
3. Abrir `pendientes/README.md` de esa copia → resultado esperado: la fila del pendiente está en la tabla, y el mapa «Ningún pendiente vive suelto» no tiene fila nueva.

Se aprueba cuando los tres pasos dan lo esperado.

### CA-02 · Con historia, sigue como hoy

```gherkin
Dado que la HU ya existe
Cuando se corre andamio.py pendiente con --hu apuntando a ella
Entonces crea el pendiente enlazado a su HU
Y le agrega su fila al mapa de historias
```

**Cómo validarlo:**
1. Correr `python -m unittest validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` → resultado esperado: OK.

Se aprueba cuando la prueba que ya existe sigue en verde.

### CA-03 · Una historia que no existe sigue siendo un error

```gherkin
Dado que se pasa --hu con una HU que no existe
Cuando se corre andamio.py pendiente
Entonces falla con «no existe la historia»
Y no crea ningún archivo
```

**Cómo validarlo:**
1. Correr `python validadores/andamio.py pendiente prueba --hu EP-001-cuerpo-de-reglas-heredable/HU-999-no-existe` → resultado esperado: termina con error y el mensaje «no existe la historia».
2. Revisar `git status` → resultado esperado: ningún archivo nuevo.

Se aprueba cuando los dos pasos dan lo esperado: un `--hu` mal escrito no se confunde con «sin historia».

### CA-04 · El orden queda escrito en la regla

```gherkin
Dado que la regla 02·F23 cubre de pendiente a fase
Cuando se precisa
Entonces nombra el orden hallazgo, pendiente, HU y fase
Y dice que la HU nace de la épica que le corresponde
Y su checklist queda en CUMPLE
```

**Cómo validarlo:**
1. Leer el cuerpo de `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` → resultado esperado: nombra los cuatro eslabones en ese orden y la épica de la HU.
2. Correr `python validadores/validar.py metareglas` → resultado esperado: 0 fallas, con el checklist de `F23` vuelto a aplicar.

Se aprueba cuando los dos pasos dan lo esperado (RN-01, RN-02 y RN-05).

### CA-05 · El índice dice cuándo vale «Por asignar»

```gherkin
Dado que el índice pide que cada pendiente declare su historia
Cuando se lee la sección «Ningún pendiente vive suelto»
Entonces dice que «Por asignar» vale mientras el pendiente no esté aprobado
```

**Cómo validarlo:**
1. Leer la sección «Ningún pendiente vive suelto» de `pendientes/README.md` → resultado esperado: la frase sobre «Por asignar» está.

Se aprueba cuando la frase está (RN-03).

### CA-06 · Un pendiente «Por asignar» no reprueba la validación

```gherkin
Dado un pendiente abierto con su historia en «Por asignar»
Cuando se corre validar.py pendientes
Entonces no lo reporta como falla
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py pendientes` → resultado esperado: 0 fallas, sin ninguna sobre un pendiente «Por asignar».

Se aprueba cuando la validación no da falla por esa causa.

### Criterios de aceptación transversales

- [ ] No regresión: las tres pruebas de `validadores/tests/test_el_andamio_*.py`, `validar.py metareglas`, `estandar` y `pendientes` quedan sin fallas.

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El cambio se registra en `CHANGELOG.md` y sube `VERSION` como MENOR |
| RNF-02 | **Compatibilidad** | Quien ya usa `--hu` no tiene que cambiar nada |

## 6. Diseño y referencias

- Documento funcional: el [pendiente 97](../../../../pendientes/97-andamio-impone-un-orden-de-trabajo-incorrecto.md)
- Código afectado: [`validadores/andamio.py`](../../../../validadores/andamio.py), función `crear_pendiente` y su argumento `--hu`
- Regla afectada: [`02·F23`](../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)

## 7. Tareas técnicas derivadas

- [ ] Hacer opcional `--hu` en `andamio.py pendiente` y escribir «Por asignar» cuando falte
- [ ] Agregar la prueba del modo sin historia
- [ ] Precisar `02·F23` y volver a aplicar su checklist
- [ ] Agregar la frase sobre «Por asignar» a `pendientes/README.md`
- [ ] Versionar y registrar el cambio
- [ ] Cerrar el pendiente 97

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto`](A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto/) | CA-01 a CA-06 | | [plan_trabajo](A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto/plan_trabajo.md) | por escribir | | En curso |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que un `--hu` mal escrito se lea como «sin historia» y el pendiente quede suelto sin que nadie lo note | El CA-03 comprueba que sigue fallando |
| Riesgo | Que precisar `F23` le agregue una segunda exigencia y el checklist repruebe la fila 9 | El supuesto 3.2 dice qué hacer: el orden pasa a una regla nueva |

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código y regla en rama principal
- [ ] Pruebas del andamio en verde
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Aceptada por el usuario

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No espera a otra historia |
| **N**egociable | ☑ | La redacción de `F23` se ajusta en la fase |
| **V**aliosa | ☑ | Hoy anotar un pendiente obliga a inventarle su historia |
| **E**stimable | ☑ | Un argumento del andamio, su prueba, una regla y una frase del índice |
| **S**mall (pequeña) | ☑ | Una fase |
| **T**esteable | ☑ | Cuatro criterios se comprueban con comandos y dos leyendo |

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-27 | El agente | Creación de la HU, a partir del pendiente 97 |
