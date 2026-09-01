# HU-002 — Fijar el estado desde la evidencia

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-015 Lo exigido se comprueba solo](../epica.md) |
| **Funcionalidad** | `F-021` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Comprobaciones |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus cuatro criterios probados |
---

## 2. Narrativa

- **Como** quien decide qué está listo y qué falta
- **Quiero** que el estado de una funcionalidad lo fije la prueba corrida
- **Para** que «verificado» quiera decir que alguien lo comprobó, no que alguien lo escribió

---

## 3. Contexto y descripción

El inventario tiene **35 funcionalidades y todas dicen «Sin verificar»**. No están mal escritas: es que nada convierte una prueba corrida en un estado. Y el día que alguien empiece a escribirlo a mano, va a decir lo que esa persona cree.

**La cadena ya existe escrita, y no hay que inventarla:**

```
inventario -> especificacion del modulo (§13) -> fase -> veredicto
```

**Y hay una distinción que esta historia hereda de la anterior.** «Sin verificar» no es «no cumple»: una es que nadie comprobó, la otra es que se comprobó y salió mal. Lo primero no se puede cerrar; lo segundo hay que arreglarlo.

### 3.1 Reglas de negocio

- `RN-1` **El estado se deriva, no se escribe.** Sale de la fase que construyó la funcionalidad.
- `RN-2` **Sin prueba queda «sin verificar», y no se cierra.**
- `RN-3` **Con prueba fallida queda «no cumple»**, y se dice cuál fase.
- `RN-4` El estado dice **de dónde sale**. Un estado sin origen es una opinión.

### 3.2 Supuestos

- Que la especificación de cada módulo nombra la fase que construye cada funcionalidad. Si no la nombra, la funcionalidad queda sin verificar, que es la respuesta correcta.

### 3.3 Fuera de alcance

- Escribir el estado en el inventario. **La cuenta se deriva al pedirla**, y una copia escrita envejece.
- Impedir la publicación, que es la `HU-003`.

---

## 4. Criterios de aceptación

### CA-01 — Con prueba y evidencia queda verificado

```gherkin
Dado una funcionalidad cuya fase declaró un veredicto de cumple
Cuando se pide su estado
Entonces queda verificada
Y se dice de qué fase sale
```

**Cómo validarlo:** sobre este repositorio.
- **Aprobado cuando:** las que están construidas salen verificadas, y ninguna más.

### CA-02 — Sin prueba queda sin verificar, y no se puede cerrar

```gherkin
Dado una funcionalidad que ninguna fase construyó
Cuando se pide su estado
Entonces queda sin verificar
Y no se puede cerrar
```

**Cómo validarlo:** con una funcionalidad sin fase, y con una cuya fase no declara veredicto.
- **Aprobado cuando:** las dos quedan sin verificar. **Es lo que impide que el estado lo ponga quien escribe.**

### CA-03 — Con prueba fallida queda «no cumple», con lo que falló

```gherkin
Dado una funcionalidad cuya fase declaró que no cumple
Cuando se pide su estado
Entonces queda en «no cumple»
Y se dice cuál fase fue
```

**Cómo validarlo:** con una fase que declare «No cumple».
- **Aprobado cuando:** sale «no cumple», con el nombre de la fase, y no se puede cerrar.

### CA-04 — Las dos formas de escribir un veredicto se leen las dos

```gherkin
Dado que las fases de la versión 1 escriben el veredicto de otra manera
Cuando se lee su estado
Entonces se entiende igual
```

**Cómo validarlo:** con las fases de la versión 1 de este repositorio.
- **Aprobado cuando:** se leen. **Una fase cerrada no se reescribe para que un programa la entienda.**

### Criterios transversales

- Derivar el estado **no modifica** ningún documento.
- Una funcionalidad con varias fases queda verificada solo si **todas** declararon.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Trazabilidad | Cada estado dice de dónde sale |
| Recuperación | Nada que reconstruir: se deriva al pedirlo |

---

## 6. Diseño y referencias

- Funcionalidad `F-021` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-21` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- La cadena que se sigue: la §13 de cada especificación de módulo.

---

## 7. Tareas técnicas derivadas

1. Leer las funcionalidades del inventario.
2. Seguir la §13 de cada especificación hasta la fase.
3. Leer el veredicto de la fase, en sus dos formas.
4. Derivar el estado y decir de dónde sale.
5. Impedir cerrar lo que está sin verificar.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio](E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio/estado-fase.md) | Los cuatro CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-020`, que abrió el módulo |
| **Riesgo 1** | Que la cadena esté rota en alguna especificación. Entonces la funcionalidad queda sin verificar, que es la respuesta correcta |
| **Riesgo 2** | Que el molde del veredicto haya cambiado y no se lea el viejo. **Pasó, y por eso existe el `CA-04`** |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ `F-020` cerrada.

## 11. Definition of Done

- ☑ Los cuatro criterios con veredicto y evidencia.
- ☑ Las 35 funcionalidades de este repositorio, con su estado derivado.
- ☑ Comprobado que derivar no modifica nada.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita el módulo que abrió `F-020` |
| Negociable | Sí | Qué se muestra de cada estado se puede ajustar |
| Valiosa | Sí | Hoy las 35 dicen lo mismo y ninguna lo dice por haberse comprobado |
| Estimable | Sí | Es seguir una cadena que ya está escrita |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre sobre este repositorio y se cuenta |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
