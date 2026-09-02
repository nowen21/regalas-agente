# HU-002 — Ver en qué estación va cada fase

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-019 El ciclo se opera desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-012` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Ciclo de vida |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien tiene doscientas fases y no puede abrirlas una por una
- **Quiero** ver en qué estación va cada una y qué le falta
- **Para** que el estado no dependa de que alguien lo recuerde

---

## 3. Contexto y descripción

**Una fase se mira abriendo su documento; doscientas no se miran de ninguna forma.** Está en la ficha de `F-012`: *«sirve para ver todas las fases a la vez»*.

**El estado lo fija lo escrito, no la opinión** (`RN-5` de la ficha). Y un `estado-fase.md` lo dice dos veces: en una frase y en una tabla. **Manda la tabla**, y cuando no coinciden se dice, porque no coincidir es justamente la señal de que alguien avanzó sin marcar.

**Hay que leer lo que hay, no lo que debería haber.** Medido acá: de las **209 fases**, **107 no usan la tabla de trece estaciones** —83 traen once y 24 traen menos— y **76 cierran con `✅` en vez de `☑`**. Ninguna se reescribe.

### 3.1 Reglas de negocio

- `RN-1` La estación actual es la primera que no está cumplida.
- `RN-2` **Manda la tabla sobre la frase**, y si no coinciden se dice.
- `RN-3` Las dos marcas de cumplida valen: `☑` y `✅`.
- `RN-4` **«Sin marcar» no es «pendiente»**, y se dicen distinto.
- `RN-5` Solo se compara la frase con la tabla cuando la tabla es de trece.
- `RN-6` Una fase detenida dice desde cuándo; la que no lo dice, lo dice.

### 3.2 Supuestos

- Que la fase tiene su `estado-fase.md`.

### 3.3 Fuera de alcance

- **Marcar las estaciones.** Las marca quien hace el trabajo.
- Reescribir las fases viejas.

---

## 4. Criterios de aceptación

### CA-01 — Se ve la estación actual de cualquier fase

```gherkin
Dada una fase con su tabla de estaciones
Cuando se pregunta en cuál va
Entonces sale la primera que no está cumplida
```

**Cómo validarlo:** con tablas de trece, de once y con las dos marcas.
- **Aprobado cuando:** sale la que corresponde en los tres casos.

### CA-02 — Se ve qué falta para pasar a la siguiente

```gherkin
Dada una fase detenida en una estación
Cuando se lee la respuesta
Entonces dice cuál es la puerta pendiente, por su nombre
```

**Cómo validarlo:** mirando la puerta que sale.
- **Aprobado cuando:** sale el nombre de la puerta, no solo el número.

### CA-03 — Una fase detenida dice desde cuándo

```gherkin
Dada una fase sin cerrar
Cuando se pregunta hace cuánto no se toca
Entonces salen los días
Y si el documento no lo dice, se dice que no se sabe
```

**Cómo validarlo:** con una fase con fecha y otra sin ella.
- **Aprobado cuando:** las dos se distinguen. **No saber tiene su propio nombre.**

### Criterios transversales

- Una tabla que no es de trece estaciones **no se compara** con la frase.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | Las 209 fases se leen de una corrida |
| Honestidad | Ninguna fase cerrada se reescribe para que encaje |

---

## 6. Diseño y referencias

- Funcionalidad `F-012` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Ciclo de vida](../../../ciclo-de-vida/spec.md).
- Señales [`S-107`](../../../senales.md) y [`S-110`](../../../senales.md).

---

## 7. Tareas técnicas derivadas

1. Leer la tabla de estaciones.
2. Aceptar las dos marcas de cumplida.
3. Separar «sin marcar» de «pendiente».
4. Comparar la frase solo cuando el modelo coincide.
5. Decir desde cuándo, y cuándo no se sabe.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [T-EP-019-HU-002-la-tabla-manda-sobre-la-frase](T-EP-019-HU-002-la-tabla-manda-sobre-la-frase/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que abre las fases |
| **Riesgo 1** | Acusar de contradicción a una fase de otro modelo. Solo se compara cuando la tabla es de trece |
| **Riesgo 2** | Confundir «no se marcó» con «está pendiente». Son dos respuestas distintas |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Medidos los modelos de tabla que conviven.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado contra las 209 fases reales.
- ☑ Ninguna fase cerrada reescrita.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Lee lo que la `HU-001` abre |
| Negociable | Sí | Qué se muestra de cada fase se puede ajustar |
| Valiosa | Sí | Doscientas fases no se miran de otra forma |
| Estimable | Sí | Es leer una tabla |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre contra el repositorio y se mira |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
