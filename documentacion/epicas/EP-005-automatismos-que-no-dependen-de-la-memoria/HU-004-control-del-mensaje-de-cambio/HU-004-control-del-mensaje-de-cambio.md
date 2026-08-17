# HU-004 — Controlar el mensaje con que se guarda un cambio

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien lee el historial del proyecto meses después
- **Quiero** que cada cambio guardado explique qué se hizo y por qué
- **Para** entender una decisión vieja sin tener que reconstruirla del código

---

## 3. Contexto y descripción

El historial es la única memoria que no se borra. Si cada cambio se guarda con un mensaje vacío, esa memoria no dice nada: quedan cien líneas de "arreglos" y "cambios varios" que no explican ninguna decisión.

Revisar los mensajes a mano no funciona: se revisa al principio y después se deja. La comprobación tiene que correr en el momento de guardar, y rechazar el mensaje que no cumple.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El mensaje se comprueba antes de aceptar el cambio |
| RN-02 | El asunto dice qué se hizo, con contenido: no vale una palabra genérica |
| RN-03 | El cuerpo dice por qué, cuando el porqué no es obvio |
| RN-04 | Va en el idioma del proyecto |
| RN-05 | No lleva rastros de la herramienta que ayudó a escribirlo |
| RN-06 | Si el mensaje no cumple, el cambio no se guarda |

### 3.2 Supuestos

- Quien guarda el cambio acaba de hacerlo, así que es el mejor momento para pedirle que lo explique.

### 3.3 Fuera de alcance

- Juzgar si lo que dice el mensaje es cierto. Eso es criterio.
- Decidir qué entra en cada cambio guardado.

---

## 4. Criterios de aceptación

### CA-01 — Un mensaje sin contenido no pasa

```gherkin
Dado que se intenta guardar un cambio
Cuando el asunto no dice qué se hizo
Entonces el cambio no se guarda
Y se dice qué le falta al mensaje
```

**Cómo validarlo:**

1. Intentar guardar un cambio con un asunto genérico de una palabra.
2. Observar. Resultado esperado: el cambio no se guarda y aparece el motivo.
3. Escribir un asunto que diga qué se hizo. Resultado esperado: ahora sí se guarda.
- **Aprobado cuando:** el historial no admite mensajes vacíos.

### CA-02 — El rastro de la herramienta se detecta

```gherkin
Dado que el mensaje trae una firma de la herramienta que ayudó a escribirlo
Cuando se intenta guardar
Entonces el cambio no se guarda
```

**Cómo validarlo:**

1. Escribir un mensaje correcto y agregarle al final una línea de atribución de herramienta.
2. Intentar guardar. Resultado esperado: no se guarda, y el mensaje señala esa línea.
3. Quitarla. Resultado esperado: se guarda.
- **Aprobado cuando:** la firma automática no llega al historial.

### Criterios de aceptación transversales

- [ ] **Límites** — un mensaje muy largo, uno con una sola línea y uno con comentarios del sistema tienen comportamiento definido.
- [ ] **Errores** — el motivo del rechazo dice cómo arreglarlo.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Oportunidad** | Corre antes de aceptar el cambio, no después |
| **Claridad** | El rechazo dice qué falta y cómo se arregla |
| **Universalidad** | Aplica a todo cambio, venga de una persona o de la IA |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Enganchar la comprobación al momento de guardar.
- [ ] Comprobar asunto, cuerpo, idioma y rastros de herramienta.
- [ ] Escribir el mensaje de rechazo con la forma correcta como ejemplo.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio](A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio/README.md) | CA-01 y CA-02 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**Mitad retro-documentación, mitad construcción.** `commits.py` ya revisa el mensaje y **nadie lo llama al guardar**: los seis enganches instalados se disparan en otros momentos. Comparte el disparo con HU-005.

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
| Dependencia | EP-004, porque la comprobación del mensaje ya existe ahí | Alto |
| Riesgo | Que el control se desactive por estorbar | El rechazo explica cómo arreglar, así que arreglar cuesta menos que saltárselo |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El mensaje se comprueba antes de aceptar el cambio
- [ ] El mensaje vacío y el rastro de herramienta se rechazan
- [ ] El rechazo dice cómo arreglarlo
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la comprobación del mensaje |
| **N**egociable | Sí | Qué se exige del mensaje se puede discutir |
| **V**aliosa | Sí | El historial es la memoria que no se borra |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un enganche |
| **T**esteable | Sí | Se prueba con mensajes malos a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
