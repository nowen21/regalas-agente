# HU-024 — El validador dice sobre qué corrió y qué no comprueba

> Historia de usuario del estándar. Nace del [pendiente 91](../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md), aprobado por el usuario el 2026-08-30.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-024 |
| **Épica / Feature** | [EP-004 — Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | 2 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

**Como** quien corre un validador antes de entregar un documento
**quiero** que su salida diga sobre qué carpetas corrió y qué partes de la norma no cuenta
**para** no leer un cero como si fuera un aprobado.

---

## 3. Contexto y descripción

`validar.py marcas` recorre `base/` y `plantillas/`. Sobre `documentacion/` devuelve cero **porque no mira**, no porque esté limpio, y la salida no distingue una cosa de la otra.

El programa tampoco cuenta todo lo que la norma pide: cubre las marcas mecánicas y deja para la lectura las que hay que juzgar. Su «0 en 0 archivos» tampoco lo dice.

**Ya cobró.** El 2026-08-30 el agente corrió el comando sobre veinticinco documentos nuevos, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de esos archivos. El enganche del commit, que sí lee lo que entra al índice, encontró trece avisos en esos mismos archivos. La afirmación falsa quedó publicada.

### 3.1 Reglas de negocio

- Un validador que no dice sobre qué corrió no entrega un veredicto: entrega un número que el lector completa con lo que quiere creer.
- Decir qué **no** se comprobó no es una disculpa: es parte del resultado.
- Ampliar el alcance del recorrido es una decisión aparte, y no la reemplaza esta historia.

### 3.2 Supuestos

- La salida la lee una persona, no otro programa: se escribe en palabras, no en códigos.
- El alcance actual del recorrido se conserva mientras no se decida otra cosa.

### 3.3 Fuera de alcance

- **Ampliar el recorrido a `documentacion/`.** Es más trabajo y produciría ruido de entrada, porque esa carpeta arrastra deuda vieja.
- Construir la comprobación de las marcas que hoy se leen a mano.

---

## 4. Criterios de aceptación

### CA-01 — La salida nombra sobre qué corrió

```gherkin
Dado que el validador de marcas termina su corrida
Cuando imprime su resultado
Entonces la salida nombra las carpetas que recorrió
Y quien la lee puede saber si su archivo estaba entre ellas
```

**Cómo validarlo:**
1. Desde la raíz del repositorio, correr `python validadores/validar.py marcas`.
2. Leer la salida completa → resultado esperado: aparece una línea que nombra las carpetas recorridas.
3. Comprobar que un archivo de `documentacion/` no está cubierto por esa lista, y que la salida lo deja claro.
- **Aprobado cuando:** la salida nombra las carpetas y no hay que abrir el código para saber cuáles son.

### CA-02 — La salida nombra qué partes de la norma no cuenta

```gherkin
Dado que el validador cubre unas marcas y deja otras para la lectura
Cuando termina su corrida
Entonces la salida dice qué partes no contó
Y dice que esas se leen
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py marcas` sobre un árbol sin ninguna marca mecánica.
2. Leer la salida → resultado esperado: además del cero, aparece qué quedó sin contar.
3. Comprobar que lo nombrado coincide con lo que el programa de verdad no mira.
- **Aprobado cuando:** un cero no se puede leer como «cumple la norma entera».

### CA-03 — Un recorrido sin archivos lo dice, y no dice «limpio»

```gherkin
Dado que se corre el validador sobre una carpeta sin ningún archivo que mirar
Cuando termina
Entonces dice que no encontró nada que revisar
Y no dice que esté limpio
```

**Cómo validarlo:**
1. Crear una carpeta temporal vacía.
2. Correr el validador con esa carpeta como raíz → resultado esperado: un mensaje de que no había nada que mirar.
3. Comprobar que el texto no afirma limpieza.
- **Aprobado cuando:** los dos ceros, el de «no encontré nada» y el de «no hay marcas», se distinguen leyendo.

### Criterios de aceptación transversales

- [x] **Errores** — un archivo que no se puede leer no tumba la corrida, y se dice cuál fue.
- [x] **No regresión** — la suite del validador queda verde, y ningún conteo cambia.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | La salida nueva no agrega ninguna pasada sobre el árbol: se arma con lo que la corrida ya sabe |
| RNF-02 | **Trazabilidad** | Lo que la salida diga que no cuenta tiene que coincidir con lo que el programa no mira, y eso se prueba |

---

## 6. Diseño y referencias

- **Documento funcional:** el [pendiente 91](../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md).
- **Programa afectado:** `validadores/marcas.py` y su entrada en `validadores/validar.py`.
- **La norma que se comprueba:** el anexo de marcas de generación automática.

---

## 7. Tareas técnicas derivadas

- [ ] Programa: que la corrida sepa qué carpetas recorrió y las imprima
- [ ] Programa: que imprima qué partes de la norma no cuenta
- [ ] Programa: distinguir «no había nada que mirar» de «no hay marcas»
- [ ] Pruebas: un caso por cada uno de los tres criterios
- [ ] Documentación: cerrar el pendiente 91

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados.

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| Sin abrir todavía | — | — | — | — | — | Sin empezar |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la salida se vuelva tan larga que nadie la lea | Se dice en una línea, al final, y solo lo que cambia la lectura del número |
| Riesgo | Que lo declarado y lo que el programa mira se separen con el tiempo | El CA-02 lo prueba: lo declarado sale de lo que el programa recorre, no de un texto escrito aparte |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible: no aplica, no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código implementado y en rama principal
- [ ] Pruebas unitarias e integración pasando
- [ ] Code review aprobado
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica actualizada
- [ ] Desplegada: no aplica, no hay ambiente
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No depende de ninguna otra historia abierta |
| **N**egociable | ☑ | Qué se nombra y con qué palabras es discutible |
| **V**aliosa | ☑ | Evita el defecto que ya publicó una afirmación falsa |
| **E**stimable | ☑ | Tres criterios, un solo programa |
| **S**mall (pequeña) | ☑ | Una fase |
| **T**esteable | ☑ | Los tres criterios se comprueban corriendo el comando |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-30 | El agente | Se crea la historia a partir del pendiente 91, aprobado por el usuario |
