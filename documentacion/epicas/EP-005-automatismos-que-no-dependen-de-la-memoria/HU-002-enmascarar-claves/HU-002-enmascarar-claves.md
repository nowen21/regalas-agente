# HU-002 — Enmascarar una clave antes de que quede escrita

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien a veces pega una clave en el chat sin pensarlo
- **Quiero** que se enmascare antes de que quede escrita en el repositorio
- **Para** que un descuido de un segundo no quede guardado para siempre

---

## 3. Contexto y descripción

Todo lo que se conversa queda escrito, y eso, que es lo que hace útil la transcripción, es también su riesgo: una clave pegada en el chat quedaría guardada en el historial, donde ya no se borra.

Atajarla después no sirve. Tiene que ser antes de escribir, en el mismo momento.

Y no puede romper el texto: quien lea la transcripción tiene que entender que ahí había una clave, sin poder leerla.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo que tiene forma de clave se enmascara antes de quedar escrito |
| RN-02 | Se enmascara, no se borra: queda la marca de que ahí había algo |
| RN-03 | Vale para lo que escribe la persona y para lo que responde la IA |
| RN-04 | Lo dudoso se enmascara: perder legibilidad se arregla, filtrar una clave no |
| RN-05 | La comprobación corre siempre, no cuando alguien se acuerda |

### 3.2 Supuestos

- Las claves reales tienen formas reconocibles. Lo que no la tenga, no se va a distinguir de un texto cualquiera.

### 3.3 Fuera de alcance

- Sacar una clave que ya quedó en el historial. Eso es una operación de rescate.
- Revisar el código del proyecto en busca de claves. Eso es EP-004.

---

## 4. Criterios de aceptación

### CA-01 — Una clave pegada en el chat no queda escrita en claro

```gherkin
Dado que alguien pega una clave en el chat
Cuando el intercambio se escribe en la transcripción
Entonces la clave aparece enmascarada
```

**Cómo validarlo:**

1. Pegar en el chat un texto con forma de clave.
2. Abrir la transcripción de esa sesión. Resultado esperado: en su lugar hay una marca, no la clave.
3. Buscar la clave literal en todo el repositorio. Resultado esperado: no aparece.
- **Aprobado cuando:** la clave no está escrita en ninguna parte.

### CA-02 — El texto sigue siendo legible

```gherkin
Dado que un mensaje llevaba una clave enmascarada
Cuando alguien lee ese mensaje después
Entonces entiende que ahí iba una clave y qué se estaba haciendo
```

**Cómo validarlo:**

1. Leer la transcripción del caso anterior.
2. Revisar si se entiende el intercambio. Resultado esperado: se entiende, y se ve dónde estaba la clave.
- **Aprobado cuando:** enmascarar no vuelve la transcripción inútil.

### Criterios de aceptación transversales

- [ ] **Privacidad** — el valor enmascarado no queda en ningún archivo intermedio.
- [ ] **Límites** — un texto largo que parece clave y no lo es tiene comportamiento definido: se enmascara igual.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Seguridad** | Se enmascara antes de escribir, no después |
| **Rendimiento** | No demora la escritura del intercambio |
| **Prudencia** | Ante la duda, se enmascara |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), criterio CAE-04.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Reconocer las formas de clave más comunes.
- [ ] Enmascarar antes de escribir, en los dos lados del diálogo.
- [ ] Escribir pruebas donde los ejemplos se arman al vuelo, para no dejar una clave real en las pruebas.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla](A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla/README.md) | CA-01 y CA-02 | **Cerrada 2026-08-18** · Cumple |

**La fase construye, y es la mitad que le falta a una regla blindada.** `00·N6` prohíbe que una clave quede escrita, y ningún programa enmascara: `secretos.py` detecta las que ya están en el código, y la transcripción copia tal cual lo que se pega en el chat.

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
| Dependencia | HU-001, porque enmascara lo que esa historia escribe | Alto |
| Riesgo | Que enmascare de más y la transcripción quede ilegible | Queda la marca de qué se enmascaró y por qué |
| Riesgo | Que las pruebas dejen una clave real guardada | Los ejemplos se arman al vuelo |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Una clave pegada en el chat no queda escrita en claro
- [ ] El texto enmascarado sigue siendo legible
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Va pegada a la transcripción de HU-001 |
| **N**egociable | Sí | Qué formas se reconocen se puede ampliar |
| **V**aliosa | Sí | Evita la filtración que no se puede deshacer |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Una comprobación antes de escribir |
| **T**esteable | Sí | Se prueba pegando una clave de prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
