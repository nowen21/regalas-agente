# HU-036 — El pedido dice qué se espera del agente

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-036 |
| **Épica / Feature** | [EP-001 Cuerpo de reglas heredable](../epica.md) |
| **Módulo / Componente** | Capítulo `01 · Conducta del agente` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Ready |

---

## 2. Narrativa

- **Como** quien le escribe al agente
- **Quiero** que no adivine qué hacer con lo que escribo
- **Para** que no cambie el proyecto cuando yo solo estaba preguntando

---

## 3. Contexto y descripción

El agente decide por su cuenta qué clase de pedido recibió. Si el usuario pregunta «¿por qué el título dice eso?», el agente asume que hay que cambiar el título y lo cambia. Si el usuario nombra algo, asume que hay que corregirlo.

`00·N1` exige aprobación para cambiar el estado del proyecto, y aun así el problema persiste: el agente entiende la pregunta **como si fuera** la aprobación. Lo que falta no es una segunda aprobación, es que el pedido diga qué se espera antes de que el agente interprete.

**El caso que la originó, el 2026-08-24:** el usuario preguntó si le ponía otro encabezado a una tabla; en la misma respuesta el agente ya lo había cambiado. Al reclamo —*«¿en dónde le dije que cambiara?»*— hubo que devolver el cambio.

### 3.1 Reglas de negocio

- `RN-1` El pedido sin palabra clave no autoriza nada, por obvio que parezca.
- `RN-2` La palabra clave dice el máximo que el agente puede hacer, no el mínimo.
- `RN-3` Preguntar y actuar en la misma respuesta es actuar sin permiso.

### 3.2 Supuestos

- El usuario acepta escribir la palabra al empezar cada pedido.
- La lista de palabras cabe en un anexo y se consulta sin memorizarla.

### 3.3 Fuera de alcance

- Que el agente adivine la palabra a partir del texto: eso es lo que se quiere quitar.
- Palabras distintas por proyecto: la lista es del estándar y viaja igual a todos.

---

## 4. Criterios de aceptación

### CA-01 — Sin palabra clave no se actúa

```gherkin
Dado un pedido que no trae ninguna de las palabras de la lista
Cuando el agente lo recibe
Entonces no toca nada
Y responde diciendo que falta la palabra, con la lista
```

**Cómo validarlo:** escribirle al agente un mensaje suelto, sin palabra clave, que se pueda leer como orden. Resultado esperado: ningún archivo cambiado, y una respuesta que pide la palabra.

- **Aprobado cuando:** el árbol de trabajo queda sin cambios y la respuesta trae la lista.

### CA-02 — Con palabra clave se hace eso, y solo eso

```gherkin
Dado un pedido que empieza con una palabra de la lista
Cuando el agente lo ejecuta
Entonces hace lo que esa palabra autoriza
Y no hace nada de lo que autorizan las otras
```

**Cómo validarlo:** pedir `revise` sobre un documento con un error evidente. Resultado esperado: lo reporta y no lo corrige.

- **Aprobado cuando:** el documento queda igual y el error aparece reportado.

### CA-03 — La palabra que no está en la lista se trata como ausente

```gherkin
Dado un pedido que empieza con una palabra parecida pero que no está en la lista
Cuando el agente lo recibe
Entonces no la interpreta
Y pide la palabra, con la lista
```

**Cómo validarlo:** escribir `arregle esto`, que no está en la lista. Resultado esperado: pide la palabra en vez de asumir que es `corrija`.

- **Aprobado cuando:** no se ejecuta nada y se pide la palabra.

### Criterios de aceptación transversales

- La regla cumple el molde de regla y el checklist del estándar, sin ❌.
- El anexo con la lista de palabras vive junto al capítulo, y la regla lo enlaza.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Claridad | La lista se entiende sin explicación previa: cada palabra dice qué autoriza en una línea |
| Costo de uso | Escribir la palabra no puede volver lento el trabajo: va al empezar el mensaje y nada más |
| Herencia | Rige igual en cualquier proyecto que adopte el estándar |

---

## 6. Diseño y referencias

- La regla nueva vive en [base/01-conducta.md](../../../../base/01-conducta.md), como `C28`.
- La lista de palabras va a un anexo del capítulo, porque no cabe en el cuerpo de una regla.
- Se apoya en [`00·N1`](../../../../base/00-nucleo-blindado.md) y la endurece: `N1` pide aprobación para cambiar el estado; esta pide que el pedido diga qué se espera, aunque no cambie nada.

---

## 7. Tareas técnicas derivadas

1. Escribir `01·C28` con su ejemplo incorrecto y correcto.
2. Escribir el anexo con las palabras y lo que autoriza cada una.
3. Aplicarle el checklist del estándar y sellar el resultado.
4. Subir versión **MAYOR** y escribir su entrada en el registro.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [A-EP-001-HU-036-la-palabra-clave-que-dice-que-hacer](A-EP-001-HU-036-la-palabra-clave-que-dice-que-hacer/README.md) | La regla, el anexo y el sello del checklist | En curso |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | Nada: la regla se escribe sola |
| **Riesgo 1** | Que la lista crezca hasta no recordarse. Se mitiga con un anexo corto y agrupado por lo que autoriza |
| **Riesgo 2** | Que el usuario olvide la palabra y el trabajo se trabe. Se mitiga porque el agente responde con la lista, no con un rechazo seco |
| **Riesgo 3** | Que el agente cumpla la forma y siga adivinando el fondo. Solo lo detecta el uso diario |

---

## 10. Definition of Ready (DoR)

- ☑ La lista de palabras está acordada con el usuario.
- ☑ Se sabe dónde va la regla y dónde el anexo.
- ☑ Los tres criterios de aceptación son comprobables.

---

## 11. Definition of Done (DoD)

- ☐ La regla escrita, con su checklist en **CUMPLE**.
- ☐ El anexo escrito y enlazado desde la regla.
- ☐ Versión **MAYOR** publicada, con su entrada en el registro.
- ☐ Los tres criterios comprobados y con veredicto.

---

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | No necesita otra historia para escribirse |
| Negociable | Sí | La lista de palabras se puede recortar o ampliar |
| Valiosa | Sí | Evita el daño de que el agente actúe sobre una pregunta |
| Estimable | Sí | Es una regla y un anexo |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Los tres criterios se comprueban escribiéndole al agente |

---

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-24 | Nace del reclamo del usuario: el agente cambió un encabezado que solo se había ofrecido cambiar. Se acuerda la lista de dieciocho palabras |
