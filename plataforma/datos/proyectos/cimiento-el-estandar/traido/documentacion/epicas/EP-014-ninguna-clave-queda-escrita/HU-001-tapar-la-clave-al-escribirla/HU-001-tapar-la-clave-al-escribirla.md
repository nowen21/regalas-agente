# HU-001 — Tapar la clave al escribirla

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-014 Ninguna clave queda escrita](../epica.md) |
| **Funcionalidad** | `F-031` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Seguridad |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus cinco criterios probados |
---

## 2. Narrativa

- **Como** quien escribe documentos desde la plataforma
- **Quiero** que una clave que se me escape quede tapada antes de llegar al archivo
- **Para** que no quede en el historial de versiones, de donde ya no sale

---

## 3. Contexto y descripción

La pieza que tapa claves existe: es un puente hacia el enmascarador del estándar, que conoce ocho formas de secreto. **La usa un solo camino de los seis que escriben.**

Y hay un límite que la medición fijó antes de construir. Sobre los 1 002 documentos guardados, tapar todo cambiaría **7 documentos y 21 fragmentos**, y los 21 son claves inventadas en los documentos de las fases que construyeron el tapador. **Tapar lo importado corrompería justo eso, sin vuelta atrás.**

De ahí la regla de esta historia: **se tapa lo que se teclea, no lo que se copia.**

### 3.1 Reglas de negocio

- `RN-1` **Se tapa lo que una persona acaba de escribir**, no el texto que ya existía en un archivo.
- `RN-2` **El nombre de la variable queda intacto.** Taparlo haría el documento ilegible sin proteger nada.
- `RN-3` **Lo importado no se altera.** Lo que parezca traer credenciales se dice con su número.
- `RN-4` **Si el enmascarador no está, se revienta en vez de escribir sin tapar** (`00·N6`).
- `RN-5` **El reconocimiento no se duplica.** Vive en el estándar; la plataforma lo usa por un puente.

### 3.2 Supuestos

- Que el enmascarador del estándar reconoce lo que hay que reconocer. Sus formas y sus pruebas viven allá.

### 3.3 Fuera de alcance

- Tapar lo importado.
- Reconocer formas nuevas de credencial.
- Quitar del historial de versiones una clave ya escrita: eso no lo puede hacer la plataforma.

---

## 4. Criterios de aceptación

### CA-01 — Una clave tecleada al llenar un hueco queda tapada

```gherkin
Dado un documento con un espacio por llenar
Cuando se llena con un texto que trae una clave
Entonces el archivo queda con la clave tapada
Y el nombre de la variable sigue legible
```

**Cómo validarlo:** llenar un hueco con `password: "inventada123"`.
- **Aprobado cuando:** en el archivo está el nombre y no está la clave.

### CA-02 — Se dice que se tapó

```gherkin
Dado que al llenar se tapó una clave
Cuando termina la operación
Entonces se dice cuántas se taparon
```

**Cómo validarlo:** llenar con dos claves y leer la respuesta.
- **Aprobado cuando:** el número sale. Tapar en silencio deja al usuario creyendo que escribió otra cosa.

### CA-03 — Lo importado no se altera

```gherkin
Dado un proyecto cuyos documentos traen claves de ejemplo
Cuando se importa
Entonces ningún documento cambia
```

**Cómo validarlo:** sobre los 7 documentos reales que el tapador tocaría.
- **Aprobado cuando:** los 7 entran idénticos. **Es el caso de «que NO pase» de esta historia.**

### CA-04 — Lo que no se tapa se dice

```gherkin
Dado un proyecto con documentos que parecen traer credenciales
Cuando se pregunta por ellos
Entonces se dice cuántos son y cuáles
```

**Cómo validarlo:** sobre este repositorio, donde son 7.
- **Aprobado cuando:** salen con su nombre. Callarlos sería perder en silencio.

### CA-05 — Sin enmascarador no se escribe

```gherkin
Dado que el enmascarador del estándar no está disponible
Cuando se intenta escribir por un camino que tapa
Entonces no se escribe nada, y se dice por qué
```

**Cómo validarlo:** apuntando la ruta de validadores a una carpeta que no existe.
- **Aprobado cuando:** revienta. Escribir sin tapar es el daño que esto viene a evitar.

### Criterios transversales

- El texto sin claves pasa **idéntico**: tapar no puede cambiar lo que no era una clave.
- Cada camino que escribe queda declarado, tape o no.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Seguridad | `00·N6`, blindada: una credencial no se escribe, no se registra y no se guarda |
| Integridad | Lo importado entra idéntico |
| Claridad | Lo tapado se cuenta; lo no tapado se nombra |

---

## 6. Diseño y referencias

- Funcionalidad `F-031` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-31` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Quién reconoce la credencial: `validadores/enmascarar.py`, del estándar.
- El puente: [plataforma/nucleo/seguridad/claves.py](../../../../plataforma/nucleo/seguridad/claves.py).

---

## 7. Tareas técnicas derivadas

1. Tapar en el camino que llena un hueco.
2. Decir cuántas se taparon.
3. Contar, sin alterar, cuántos documentos importados parecen traer credenciales.
4. Declarar camino por camino quién tapa y quién no.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia](C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia/estado-fase.md) | Los cinco CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-013`, que abrió el camino que teclea |
| **Riesgo 1** | Tapar de más y corromper un documento sin vuelta atrás. Medido antes: por eso lo importado no se tapa |
| **Riesgo 2** | Que un camino nuevo nazca sin tapar. Cada uno queda declarado en la especificación |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Medido qué pasaría si taparan todos los caminos: 7 documentos alterados.
- ☑ El módulo Seguridad, con [especificación](../../../seguridad/spec.md) aprobada el 2026-09-01.

## 11. Definition of Done

- ☑ Los cinco criterios con veredicto y evidencia.
- ☑ Comprobado que los 7 documentos reales entran idénticos.
- ☑ El aviso medido sobre los 1 002 documentos.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita el camino que abrió `EP-013` |
| Negociable | Sí | Qué caminos tapan se puede ajustar |
| Valiosa | Sí | Es el único daño irreversible de la versión |
| Estimable | Sí | El reconocimiento ya existe; falta enchufarlo |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se llena con una clave y se mira el archivo |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-09-01 | Nace de `F-031`, con la épica `EP-014` aprobada ese día |
