# HU-008 — El enganche que sostiene el resumen de la sesión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En implementación |

---

## 2. Narrativa

- **Como** quien retoma el trabajo días después
- **Quiero** que el resumen de la sesión exista aunque nadie se acuerde de escribirlo
- **Para** no depender de la memoria del agente para saber qué quedó

---

## 3. Contexto y descripción

El modelo del resumen y su carpeta ya existen. Llenarlos depende de que el agente se acuerde, y esa es exactamente la forma en que se pierde: un chat no tiene final, así que lo que se deja para el cierre no se escribe.

Es lo mismo que pasaba con la transcripción, que solo empezó a escribirse siempre cuando la escribió un programa.

Lo que un programa no puede hacer es reconocer el hallazgo ni redactarlo: eso es criterio. Lo que sí puede es que el hueco se vea.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El archivo del resumen se crea solo al abrir la sesión, con el modelo puesto |
| RN-02 | Cuando la sesión ya produjo algo y falta llenar el resumen, se avisa: una vez por hueco y máximo dos veces en la sesión |
| RN-03 | Se muestra lo que sigue abierto **del propósito de la sesión**, y nada de otros temas |
| RN-04 | El aviso dice **qué falta**, con la lista; no avisa en genérico |
| RN-05 | Para cerrar una sesión cuentan los hallazgos de su propósito; los que nacieron acá y son de otro tema basta con que queden anotados |
| RN-06 | El enganche no escribe hallazgos: solo crea, avisa y arrastra |
| RN-07 | No detiene el trabajo |

### 3.2 Supuestos

- "La sesión ya produjo algo" se puede detectar: hubo un commit, o cambió el cuerpo de reglas.

### 3.3 Fuera de alcance

- El modelo del resumen, que es de EP-003.
- Decidir qué es un hallazgo.

---

## 4. Criterios de aceptación

### CA-01 — El archivo nace solo

```gherkin
Dado que se abre una sesión
Cuando se mira la carpeta de resúmenes del día
Entonces existe el archivo de esa sesión, con el modelo puesto y sin hallazgos
```

**Cómo validarlo:**

1. Abrir una sesión en un proyecto de prueba.
2. Mirar la carpeta del día. Resultado esperado: está el archivo, con los campos del modelo.
3. Abrir una segunda sesión el mismo día. Resultado esperado: aparece su propio archivo, sin pisar el anterior.
- **Aprobado cuando:** el hueco se ve, en vez de no existir.

### CA-02 — Avisa cuando la sesión ya produjo algo y el resumen sigue vacío

```gherkin
Dado que la sesión hizo un commit o cambió una regla
Cuando al resumen le falta algo por llenar
Entonces se avisa una vez por cada cosa que falte, y se dice cuál es
```

**Cómo validarlo:**

1. En la sesión de prueba, hacer un cambio y guardarlo sin escribir el resumen.
2. Seguir trabajando. Resultado esperado: aparece el aviso, y dice que no hay ningún hallazgo escrito.
3. Escribir un hallazgo y seguir. Resultado esperado: no repite ese aviso; si la sección de cierre sigue vacía, avisa eso, una vez.
4. Llenar la sección de cierre y seguir. Resultado esperado: no vuelve a avisar.
- **Aprobado cuando:** avisa qué falta, una vez por cada cosa, y calla cuando no falta nada.

### CA-03 — Del propósito se muestra lo que sigue abierto, y nada más

```gherkin
Dado que la sesión declara su propósito, el hallazgo que viene a resolver
Cuando se abre o se le pone el nombre
Entonces se muestra ese hallazgo y lo que sigue abierto de él
Y no se muestra ningún hallazgo de otro tema
```

**Cómo validarlo:**

1. Dejar hallazgos abiertos en dos temas distintos, en sesiones de días distintos.
2. Abrir una sesión que declara como propósito uno de los dos. Resultado esperado: se muestra ese, con su pregunta viva; el otro no aparece.
3. Cerrarlo y abrir otra sesión con el mismo propósito. Resultado esperado: ya no aparece.
- **Aprobado cuando:** se retoma sin ir a buscar, y sin que sobre nada.

> **El propósito lo pone el usuario, no lo adivina el programa.** Una sesión abierta para resolver un hallazgo no tiene por qué ver los de otro tema: eso es ruido, y el ruido se deja de leer. Esta sesión sirve de ejemplo: se abrió con un solo propósito, resolver el H-4 de otra sesión.

### Criterios de aceptación transversales

- [x] **Inocuidad** — el enganche no modifica los hallazgos ya escritos.
- [x] **Límites** — un proyecto sin carpeta de resúmenes no se ve afectado.
- [x] **Errores** — si no puede escribir, avisa y la sesión sigue.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Oportunidad** | Avisa durante la sesión, no al cerrarla |
| RNF-02 | **Silencio** | Una vez por cada cosa que falta, máximo dos en la sesión |
| RNF-03 | **Rendimiento** | No demora el arranque |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** el pendiente 17 y el hallazgo H-4 del 2026-08-14.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [x] Crear el archivo del resumen al abrir la sesión.
- [x] Detectar que la sesión ya produjo algo.
- [x] Avisar una vez por hueco, con la marca que evita repetirlo.
- [x] Mostrar lo que sigue abierto del propósito de la sesión.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-008-enganche-del-resumen](A-EP-005-HU-008-enganche-del-resumen/README.md) | CA-01, CA-02 y CA-03 | Estación 11: las siete exigencias en verde, esperando el commit |

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
| Dependencia | EP-003 · HU-009, porque crea el archivo con ese modelo | Alto |
| Dependencia | HU-001 de esta épica, porque comparte el momento de la sesión | Medio |
| Riesgo | Que el aviso se vuelva ruido | Una vez por cada cosa que falta, y solo cuando de verdad falta |
| Riesgo | Que el archivo vacío se quede vacío igual | Se arrastra a la sesión siguiente, así que no desaparece |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [x] El archivo se crea solo
- [x] Avisa qué falta, una vez por cada cosa
- [x] Del propósito de la sesión se muestra lo que sigue abierto, y nada de otros temas
- [x] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita el modelo de EP-003 |
| **N**egociable | Sí | La señal que dispara el aviso se puede discutir |
| **V**aliosa | Sí | Es lo que hace que el resumen exista siempre |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Tres comportamientos |
| **T**esteable | Sí | Se prueba abriendo sesiones de prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-4 del 2026-08-14 |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Se abre la fase A con la especificación del módulo y sus dos planes. Los requisitos no funcionales quedan numerados |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Fase ejecutada: nacen `resumen.py` y `hook_resumen.py`, y el renombrado mueve los dos archivos. Con esto cierra la cadena de H-4 |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | El aviso pasa a decir **qué** falta y a salir una vez por hueco. `CA-03` se acota al propósito de la sesión: mostrar todo lo abierto es ruido, y el propósito lo pone el usuario |
