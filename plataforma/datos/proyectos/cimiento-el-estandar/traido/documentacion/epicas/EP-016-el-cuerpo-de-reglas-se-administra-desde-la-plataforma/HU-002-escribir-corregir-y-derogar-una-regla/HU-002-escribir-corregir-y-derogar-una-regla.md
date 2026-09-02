# HU-002 — Escribir, corregir y derogar una regla

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-016 El cuerpo de reglas se administra desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-005` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Reglas |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien mantiene el cuerpo de reglas
- **Quiero** escribir una regla y quitarle vigencia desde la plataforma
- **Para** no editar archivos a mano y no repetir lo que otra regla ya decía

---

## 3. Contexto y descripción

**Lo difícil no es escribir la regla.** Lo dice la propia ficha de `F-005`: *«escribir la regla es lo fácil; lo que cuesta es que no repita ni contradiga a otra»*. Con **248 reglas vigentes**, nadie las tiene todas en la cabeza.

**Y hay un límite que hay que decir en voz alta.** La plataforma puede poner al lado las reglas que **hablan de lo mismo**; no puede decir si se contradicen, porque eso depende de lo que significan. Llamarlo detector de contradicciones sería peor que no tenerlo: **quien confía en un detector deja de mirar**.

**Derogar no borra.** La regla se queda escrita, marcada, con su texto debajo y su número ocupado. Lo exige `M11`, y el porqué es el mismo del número: una cita escrita hace un año tiene que seguir apuntando a lo que apuntaba.

### 3.1 Reglas de negocio

- `RN-1` **La fuente es el texto.** La regla se escribe en un archivo, no en la base.
- `RN-2` **Nada se borra: se deroga**, conservando el texto.
- `RN-3` **Antes de guardar se muestran las que se parecen**, con lo que eso no puede decir.
- `RN-4` **Una regla blindada no se deroga desde acá.** Sostienen a las demás.
- `RN-5` **La regla nace con sus huecos puestos**, para que se vea que está incompleta.
- `RN-6` Escribir y derogar quedan registrados.

### 3.2 Supuestos

- Que el capítulo destino existe con su carpeta de reglas.

### 3.3 Fuera de alcance

- **Decidir si la regla es buena.** La plataforma acompaña; el criterio es de una persona.
- **Detectar contradicciones.**
- Aplicar el checklist, que es `F-007`.

---

## 4. Criterios de aceptación

### CA-01 — Una regla nueva queda guardada con su identificador

```gherkin
Dado un capítulo y un título
Cuando se pide escribir la regla
Entonces queda un archivo con el formato canónico
Y con el identificador que le tocaba
```

**Cómo validarlo:** escribiendo una en un cuerpo de reglas de prueba.
- **Aprobado cuando:** el archivo trae el encabezado, el cuerpo y el ejemplo.

### CA-02 — Derogar deja la regla legible y marcada

```gherkin
Dado una regla vigente
Cuando se deroga
Entonces su encabezado queda con la marca de derogación
Y su texto original sigue ahí
Y su identificador sigue ocupado
```

**Cómo validarlo:** derogando una y volviendo a leer el archivo.
- **Aprobado cuando:** está marcada, se lee entera, y su número no se libera. **Es el criterio que decide.**

### CA-03 — Una regla que habla de lo mismo se muestra antes de guardar

```gherkin
Dado un título parecido al de una regla vigente
Cuando se pide escribirla
Entonces salen las que hablan de lo mismo, con las palabras en común
Y no se escribe nada todavía
```

**Cómo validarlo:** con el título de una regla que ya existe.
- **Aprobado cuando:** la encuentra, **y el aviso dice que esto no detecta contradicciones**.

### Criterios transversales

- Una regla que no existe, una ya derogada y **una blindada** se responden diciendo por qué no.
- La regla nueva nace con sus huecos puestos.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Derogar conserva el texto entero |
| Claridad | El aviso de las parecidas dice **cada vez** lo que no puede decir |
| Portabilidad | Todo queda como texto, legible sin la plataforma |

---

## 6. Diseño y referencias

- Funcionalidad `F-005` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-05` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Las reglas que lo mandan: [`20·M11`](../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) y [`20·M5`](../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md).

---

## 7. Tareas técnicas derivadas

1. El molde canónico de una regla, con sus huecos.
2. Escribirla, pidiendo el identificador antes.
3. Derogar: marcar el encabezado y conservar el texto.
4. Las reglas que hablan de lo mismo.
5. El aviso de lo que eso no puede decir.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [H-EP-016-HU-002-derogar-marca-y-no-borra](H-EP-016-HU-002-derogar-marca-y-no-borra/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`: sin identificador no se puede escribir |
| **Riesgo 1** | Que alguien crea que la plataforma detecta contradicciones. El aviso lo dice cada vez |
| **Riesgo 2** | Que derogar pierda el texto. El `CA-02` lo comprueba leyendo el archivo entero |
| **Riesgo 3** | Que se derogue una blindada por una orden de consola. Está impedido |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La `HU-001`, cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que derogar conserva el texto.
- ☑ Comprobado sobre este repositorio que las parecidas encuentran el duplicado real.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la numeración de la `HU-001` |
| Negociable | Sí | Cuántas parecidas se muestran se puede ajustar |
| Valiosa | Sí | Es lo que evita repetir una regla que ya existe |
| Estimable | Sí | Es escribir texto con un molde fijo |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se escribe una, se deroga otra, y se lee el archivo |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
