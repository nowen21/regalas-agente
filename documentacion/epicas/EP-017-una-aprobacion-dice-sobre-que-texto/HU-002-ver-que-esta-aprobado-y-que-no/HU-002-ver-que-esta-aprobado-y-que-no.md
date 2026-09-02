# HU-002 — Ver qué está aprobado y qué no

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-017 Una aprobación dice sobre qué texto](../epica.md) |
| **Funcionalidad** | `F-016` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Aprobaciones |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien va a construir sobre un documento
- **Quiero** saber si está aprobado, si su aprobación caducó, o si nadie lo ha mirado
- **Para** no construir sobre algo que todavía puede cambiar

---

## 3. Contexto y descripción

**Son tres estados, no dos**, y confundirlos pierde información:

| Estado | Qué quiere decir |
|---|---|
| **Aprobado** | Alguien lo aprobó, y el texto sigue siendo ese |
| **Caducada** | Alguien lo aprobó, **y el texto cambió después** |
| **Sin aprobación** | Nadie lo ha mirado |

«Caducada» dice que hubo un juicio y que algo lo invalidó; «sin aprobación», que nunca lo hubo.

**Y se dice con palabras.** Lo pide la ficha: *«dicho con palabras, no solo con color: quien no distingue colores tiene que poder saberlo»*.

### 3.1 Reglas de negocio

- `RN-1` **Los tres estados se dicen con palabras.**
- `RN-2` **Un documento sin aprobación aparece así, no vacío.**
- `RN-3` Se ve **desde cuándo** está aprobado y por quién.
- `RN-4` La frase de «caducada» dice **por qué** caducó.

### 3.2 Supuestos

- Que la aprobación se registró con su huella.

### 3.3 Fuera de alcance

- La pantalla. Se muestra por orden de consola.
- Juzgar si un documento debería estar aprobado.

---

## 4. Criterios de aceptación

### CA-01 — Se distingue lo aprobado de lo que está en borrador

```gherkin
Dado varios documentos en estados distintos
Cuando se pide su estado de aprobación
Entonces cada uno sale con el suyo, dicho con palabras
```

**Cómo validarlo:** con uno aprobado y uno sin aprobar.
- **Aprobado cuando:** los dos salen, y con palabras distintas.

### CA-02 — Se ve desde cuándo

```gherkin
Dado un documento aprobado
Cuando se pide su estado
Entonces se dice quién lo aprobó y cuándo
```

**Cómo validarlo:** aprobando y consultando.
- **Aprobado cuando:** salen los dos datos.

### CA-03 — Un documento sin aprobación aparece así, no vacío

```gherkin
Dado un documento que nadie aprobó
Cuando se pide su estado
Entonces dice que nadie lo ha aprobado todavía
```

**Cómo validarlo:** con un documento nuevo.
- **Aprobado cuando:** lo dice. **Un vacío se leería como un error de la consulta.**

### Criterios transversales

- Los tres estados tienen su frase, y la de caducada dice por qué.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Accesibilidad | **Con palabras, no con color** |
| Claridad | Tres estados distintos, dichos distinto |

---

## 6. Diseño y referencias

- Funcionalidad `F-016` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-16` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- La §5.1 de la [especificación del módulo](../../../aprobaciones/spec.md).

---

## 7. Tareas técnicas derivadas

1. Los tres estados, con su frase.
2. Comparar la huella de lo que hay con la de la aprobación.
3. Decir desde cuándo y por quién.
4. Que lo sin aprobación aparezca.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras](N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que registra la aprobación |
| **Riesgo 1** | Que el estado se comunique solo con color. Los tres tienen su frase |
| **Riesgo 2** | Que lo sin aprobación salga vacío y se lea como un fallo. Aparece con su frase |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La `HU-001` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que los tres estados tienen su frase.
- ☑ Comprobado que lo sin aprobación aparece.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la aprobación de la `HU-001` |
| Negociable | Sí | Cómo se muestra se puede ajustar |
| Valiosa | Sí | Es lo que evita construir sobre algo que puede cambiar |
| Estimable | Sí | Es comparar una huella y elegir una frase |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se mira el estado de dos documentos distintos |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
