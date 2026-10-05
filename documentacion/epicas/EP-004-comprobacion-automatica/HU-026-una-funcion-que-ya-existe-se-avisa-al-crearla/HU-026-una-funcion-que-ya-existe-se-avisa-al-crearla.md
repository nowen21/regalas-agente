# HU-026 · Una función que ya existe se avisa al crearla

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1 del pendiente 116](../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), puntos 2 y 3, que salen de sus acuerdos 2, 3 y 4, y resuelven el [pendiente 117](../../../../historico-chat/resumenes/2026-10-04/pendientes/117-nada-avisa-cuando-se-crea-una-funcion-que-ya-existe/pendiente.md). Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-026 |
| **Épica / Feature** | [EP-004 Comprobación automática](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/validadores/` |
| **Tipo** | Técnica |
| **Prioridad** | Segunda del análisis 1 del pendiente 116 (acuerdo 2: «primero el validador de `07·Q4`») |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada el 2026-10-04, con sus cinco criterios probados |

---

## 2. Narrativa

- **Como** el usuario, que mantiene Cimiento y los proyectos que lo heredan
- **Quiero** que al crear una función se avise si ya existe otra que hace lo mismo
- **Para** que no nazcan copias nuevas mientras se juntan las de hoy

---

## 3. Contexto y descripción

[`07·Q4`](../../../../base/07-calidad-de-codigo.md#q4--no-repitas-dry-pero-no-abstraigas-de-más) pide no repetir lógica, y ningún validador lo comprueba. El inventario del 2026-10-04 encontró `_leer` en 13 archivos, `raiz_pedida` en 10, `dicho` en 9, `_entrada` en 8 y `_git` en 6 (pendiente 117).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Al encontrar una copia, avisa y no frena | Análisis 1 del pendiente 116, acuerdo 4 |
| RN-02 | Compara lo que hace la función, no solo su nombre | Acuerdo 4 |
| RN-03 | Sirve a cualquier proyecto y reutiliza el recorrido de código y la separación de funciones, sin copiarlos | Acuerdo 3 |
| RN-04 | La separación de funciones vive una sola vez, y la usan este validador y el de `07·Q3` | Punto 2 |

### 3.2 Supuestos

- Que los lenguajes que lee `07·Q3` (funciones con llaves y `def` de Python) cubren el código de los proyectos de hoy.

### 3.3 Fuera de alcance

- Juntar las copias que ya existen: es otra épica (acuerdo 2).
- Detectar repetición dentro de una misma función.

---

## 4. Criterios de aceptación

### CA-01 · La separación de funciones vive una sola vez

**Sale de:** análisis 1, punto 2 (del pendiente 116).

```gherkin
Dado el validador de funciones largas y el de funciones repetidas
Cuando separan las funciones de un archivo
Entonces los dos usan la misma pieza de core/validadores/codigo.py
Y el de funciones largas sigue dando lo mismo que antes
```

**Cómo validarlo:**
1. Abrir `proyectos/cimiento/core/validadores/codigo.py` y `calidad.py`.
2. Correr `python manage.py test core.validadores` desde `proyectos/cimiento/`.

**Aprobado cuando:** la separación está solo en `codigo.py` y las pruebas de `07·Q3` pasan sin cambios.

### CA-02 · Avisa la función que hace lo mismo que otra, aunque se llame distinto

**Sale de:** análisis 1, punto 3 (del pendiente 116).

```gherkin
Dado un proyecto con una función que ya existe en otro archivo, con otro nombre y otras variables
Cuando se corre validar.py repetidas
Entonces sale un aviso que nombra las dos funciones con su archivo y su línea
Y el código de salida no cambia por ese aviso
```

**Cómo validarlo:**
1. En un proyecto de prueba, dos archivos con la misma función escrita con nombres distintos.
2. Correr `python validadores/validar.py repetidas --raiz <proyecto>`.

**Aprobado cuando:** sale un AVISO con las dos funciones y el código de salida es 0.

### CA-03 · No avisa lo que solo se parece por el nombre o es demasiado corto

**Sale de:** análisis 1, punto 3 (del pendiente 116).

```gherkin
Dado dos funciones con el mismo nombre que hacen cosas distintas, y funciones de una o dos líneas iguales
Cuando se corre validar.py repetidas
Entonces no sale ningún aviso
```

**Cómo validarlo:**
1. En un proyecto de prueba, los dos casos.
2. Correr `python validadores/validar.py repetidas --raiz <proyecto>`.

**Aprobado cuando:** no sale ningún aviso.

### CA-04 · Al guardar, avisa la función nueva que repite una que ya estaba

**Sale de:** análisis 1, punto 3 (del pendiente 116).

```gherkin
Dado un proyecto con una función versionada
Cuando se prepara un commit que agrega otra que hace lo mismo
Entonces validar.py repetidas --preparados avisa la nueva y nombra la que ya estaba
Y no avisa las copias que ya estaban antes de ese commit
```

**Cómo validarlo:**
1. En un proyecto de prueba con git, versionar una función y preparar otra igual.
2. Correr `python validadores/validar.py repetidas --raiz <proyecto> --preparados`.

**Aprobado cuando:** sale un aviso por la nueva y ninguno por las viejas.

### CA-05 · Corre en un proyecto que no es Cimiento

**Sale de:** análisis 1, punto 3 (del pendiente 116).

```gherkin
Dado un proyecto que hereda el estándar y no es Cimiento
Cuando se corre validar.py repetidas desde su carpeta
Entonces revisa su código y no el del estándar
```

**Cómo validarlo:**
1. Correr `python "C:/Ing. Jose/ia/agente/validadores/validar.py" repetidas` parado en `c:/wamp64/www/proyectos/personales/agro-system`.

**Aprobado cuando:** los avisos nombran archivos de agro-system y ninguno del estándar.

### Criterios de aceptación transversales

- [x] Rendimiento: responde dentro del umbral acordado con un **volumen realista** (`06`).
- [x] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Revisa el código de Cimiento en menos de 30 segundos |

---

## 6. Diseño y referencias

- Documento funcional: [análisis 1 del pendiente 116](../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), acuerdos 2 a 4 y puntos 2 y 3.

---

## 7. Tareas técnicas derivadas

- [ ] Mover la separación de funciones de `calidad.py` a `codigo.py`.
- [ ] El validador `repetidas` de `07·Q4`, con su modo `--preparados`.
- [ ] Sumarlo a `validar.py`.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida` | CA-01 a CA-05 | (vacío) | [plan_trabajo.md](A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida/plan_trabajo.md) | [plan_pruebas.md](A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida/plan_pruebas.md) | [resultado_pruebas.md](A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que el aviso salga por casualidad y se aprenda a ignorarlo | Umbral alto y tamaño mínimo, medidos sobre Cimiento antes de fijarlos |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 116 |
