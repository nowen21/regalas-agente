# HU-001 — Escribir la sesión a medida que pasa, con hora del reloj

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien retoma un trabajo días después
- **Quiero** que cada sesión quede escrita mientras ocurre, con la hora real
- **Para** poder leer qué se decidió y por qué, aunque el chat ya no exista

---

## 3. Contexto y descripción

El chat se borra. Lo que se decidió ahí se pierde con él, y la sesión siguiente empieza sin saber qué se acordó ni por qué.

Dejarlo para el final no funciona: un chat casi nunca tiene final claro. Se cierra la ventana y ya. Por eso la transcripción se escribe a medida que pasa, después de cada intercambio.

La hora importa tanto como el texto: sirve para saber cuánto tomó cada cosa y en qué orden pasó. Se lee del reloj de la máquina en el momento, nunca se estima después.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada sesión queda escrita en el repositorio, sin que nadie lo pida |
| RN-02 | Se escribe después de cada intercambio, no al cerrar |
| RN-03 | Va la transcripción, no un resumen: cada mensaje tal como se escribió |
| RN-04 | Cada intercambio lleva la hora leída del reloj de la máquina |
| RN-05 | Una hora que no se registró se escribe como no registrada; no se estima |
| RN-06 | La salida cruda de las herramientas no entra: eso no es diálogo |
| RN-07 | Cada sesión queda en el índice de la carpeta, para que la siguiente la encuentre |

### 3.2 Supuestos

- El repositorio del proyecto está disponible durante la sesión.

### 3.3 Fuera de alcance

- Resumir o interpretar lo que pasó. Se transcribe.
- Guardar lo aprendido como conocimiento buscable. Eso es EP-006.

---

## 4. Criterios de aceptación

### CA-01 — La sesión se escribe sola, desde el primer intercambio

```gherkin
Dado que se abre una sesión de trabajo
Cuando pasa el primer intercambio
Entonces ya existe el archivo de la sesión con ese intercambio escrito
```

**Cómo validarlo:**

1. Abrir una sesión nueva en un proyecto de prueba y escribir un mensaje cualquiera.
2. Buscar en el repositorio la carpeta de sesiones. Resultado esperado: hay un archivo nuevo con el mensaje y la respuesta.
3. Cerrar la ventana sin avisar y volver a mirar. Resultado esperado: lo escrito sigue ahí.
- **Aprobado cuando:** cerrar de golpe no pierde nada.

### CA-02 — Cada intercambio lleva su hora real

```gherkin
Dado que se escribe un intercambio en la transcripción
Cuando se mira su marca de tiempo
Entonces es la hora del reloj de la máquina en ese momento
```

**Cómo validarlo:**

1. Anotar la hora de la máquina y enviar un mensaje.
2. Abrir la transcripción. Resultado esperado: la marca coincide con la hora anotada.
3. Provocar que una hora no se pueda leer. Resultado esperado: queda escrito que no se registró, no una hora inventada.
- **Aprobado cuando:** ninguna hora es una estimación.

### CA-03 — La sesión aparece en el índice

```gherkin
Dado que se creó el archivo de una sesión
Cuando se abre el índice de la carpeta
Entonces la sesión está listada
```

**Cómo validarlo:**

1. Tener una sesión escrita en el proyecto de prueba.
2. Abrir el índice de la carpeta de sesiones. Resultado esperado: aparece con su fecha y su tema.
3. Renombrar el archivo con el tema real. Resultado esperado: el índice queda apuntando al nombre nuevo.
- **Aprobado cuando:** ninguna sesión queda fuera del índice.

### Criterios de aceptación transversales

- [ ] **Privacidad** — lo que se enmascara no queda escrito en claro en la transcripción.
- [ ] **Límites** — un proyecto sin carpeta de sesiones no se ve afectado.
- [ ] **Errores** — si no se puede escribir el archivo, se avisa y no se pierde el trabajo.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Persistencia** | Lo escrito sobrevive al cierre abrupto de la ventana |
| **Fidelidad** | La transcripción no condensa ni parafrasea |
| **Rendimiento** | Escribir no demora la conversación |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), criterios CAE-01 y CAE-02.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el mensaje del usuario apenas se envía.
- [ ] Escribir la respuesta apenas termina.
- [ ] Leer la hora del reloj en cada uno de los dos momentos.
- [ ] Mantener el índice de la carpeta al día.
- [ ] Definir el nombre del archivo y cómo se le pone el tema real.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

Todavía no se descompuso en fases.

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
| Dependencia | HU-002, porque una clave pegada en el chat no puede quedar escrita en claro | Alto |
| Riesgo | Que la transcripción crezca tanto que nadie la lea | Se carga solo el índice; la sesión se abre cuando hace falta |
| Riesgo | Que se escriba un resumen en vez de la transcripción | La regla lo dice, y el archivo se revisa contra el diálogo |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La sesión se escribe sola desde el primer intercambio
- [ ] Cada intercambio lleva la hora del reloj
- [ ] La sesión queda en el índice
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita el enmascarado de HU-002 para no escribir claves |
| **N**egociable | Sí | El formato de la transcripción se puede discutir |
| **V**aliosa | Sí | Es lo que evita perder lo decidido |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Escribir dos veces por intercambio |
| **T**esteable | Sí | Se prueba cerrando la ventana de golpe |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
