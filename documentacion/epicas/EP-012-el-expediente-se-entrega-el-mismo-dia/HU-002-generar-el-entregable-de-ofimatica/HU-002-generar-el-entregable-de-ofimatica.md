# HU-002 — Generar el entregable de ofimática

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-012 El expediente se entrega el mismo día](../epica.md) |
| **Funcionalidad** | `F-026` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Expediente |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Aprobada el 2026-08-31 |
---

## 2. Narrativa

- **Como** quien entrega la documentación a un cliente
- **Quiero** que el expediente se convierta solo en el archivo que el cliente espera
- **Para** no mantener dos versiones del mismo texto

---

## 3. Contexto y descripción

El cliente espera un archivo de ofimática. La fuente es texto, versionado línea por línea, y **así se queda**: [`DA-09`](../../../../cvds/diseno/decisiones-de-arquitectura.md) decide que el archivo se produce desde el texto cuantas veces haga falta, y nunca al contrario.

**Lo que se pierde está declarado, y no es poco:** quien recibe el entregable no puede devolver correcciones escritas encima. Tiene que pedirlas. Se aceptó a cambio de no mantener un segundo original para siempre.

**Lo difícil ya está advertido en la ficha:** las listas dentro de una celda tienen que salir como listas, no con la etiqueta a la vista. Es donde este tipo de generadores se cae, y este repositorio está lleno de tablas con viñetas adentro.

### 3.1 Reglas de negocio

- `RN-1` La fuente es el texto. **La salida no se edita** (`RN-7` del inventario).
- `RN-2` Generar dos veces sobre lo mismo da el mismo archivo.
- `RN-3` Un expediente con espacios sin llenar **avisa antes de generar**, y no lo impide: la decisión es del usuario.
- `RN-4` Nada del entregable se escribe a mano.

### 3.2 Supuestos

- Que el expediente que llega ya viene armado y con su lista de lo que falta, de la [HU-001](../HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md).

### 3.3 Fuera de alcance

- Recibir cambios hechos encima del entregable. Es lo que `DA-09` declara como pérdida.
- Elegir la plantilla visual del cliente: se entrega con la estructura del expediente.

---

## 4. Criterios de aceptación

### CA-01 — Un expediente completo se genera con todas sus secciones

```gherkin
Dado un expediente armado
Cuando se pide el entregable
Entonces el archivo trae todas sus secciones, en el mismo orden
```

**Cómo validarlo:** generar el de este repositorio y contar las secciones contra el expediente.
- **Aprobado cuando:** no falta ninguna, y el orden es el mismo.

### CA-02 — Las listas y las tablas salen como listas y tablas

```gherkin
Dado un documento con una lista dentro de una celda de tabla
Cuando se genera el entregable
Entonces la lista se ve como lista
Y no aparece ninguna etiqueta del texto de origen
```

**Cómo validarlo:** con un documento real del repositorio que tenga tablas con viñetas adentro.
- **Aprobado cuando:** no queda ninguna marca del formato de origen a la vista. **Es el criterio que decide esta historia.**

### CA-03 — Generar dos veces da el mismo resultado

```gherkin
Dado el mismo expediente
Cuando se genera dos veces
Entonces los dos archivos son iguales
```

**Cómo validarlo:** generar dos veces y comparar la huella del contenido.
- **Aprobado cuando:** son idénticos. Si difieren por la fecha de generación, esa fecha se saca de la comparación **y se dice**.

### CA-04 — Con espacios sin llenar, avisa antes de generar

```gherkin
Dado un expediente con documentos incompletos
Cuando se pide el entregable
Entonces se avisa cuáles están incompletos antes de generar
Y se genera igual si el usuario lo pide
```

**Cómo validarlo:** con un expediente que traiga marcas de espacio por llenar.
- **Aprobado cuando:** avisa y **no impide**: la decisión de entregar es del usuario.

### Criterios transversales

- Generar **no modifica** ningún documento del expediente.
- El archivo se genera sin salir a la red.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Disponibilidad | Funciona sin red (`RNF-03`) |
| Recuperación | El entregable se rehace desde el texto: perderlo no pierde nada |
| Fidelidad | Lo que se lee en el texto es lo que se ve en el archivo |

---

## 6. Diseño y referencias

- Funcionalidad `F-026` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-26` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Decisión que la gobierna: [`DA-09`](../../../../cvds/diseno/decisiones-de-arquitectura.md).

---

## 7. Tareas técnicas derivadas

1. Convertir un documento del expediente al formato de salida.
2. Resolver las listas dentro de celdas, que es lo difícil.
3. Juntar los documentos en un solo archivo, con su índice.
4. Avisar de lo incompleto antes de generar.
5. Comprobar que dos corridas dan lo mismo.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| Por abrir | Esta historia | Sin abrir |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`: sin expediente armado no hay qué generar |
| **Riesgo 1** | Que el formato se rompa en listas y tablas. **Es el riesgo de peso**, y se prueba temprano con un documento real |
| **Riesgo 2** | Que generar necesite instalar algo que salga a la red. Si no se puede sin eso, se dice y se decide; no se instala por decisión del agente |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La decisión que la gobierna está aprobada (`DA-09`).
- ☑ El módulo Expediente tiene especificación aprobada: [documentacion/expediente/spec.md](../../../expediente/spec.md), el 2026-08-31.
- ☑ Está decidido con qué se genera, el 2026-08-31: **formato abierto con la librería estándar**, sin instalar nada.

## 11. Definition of Done

- ☐ Los cuatro criterios con veredicto y evidencia.
- ☐ El `CA-02` probado con un documento real con tablas y viñetas.
- ☐ Comprobado que dos corridas dan el mismo archivo.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la `HU-001` |
| Negociable | Sí | El formato de salida y su estructura se pueden ajustar |
| Valiosa | Sí | Es lo que el cliente recibe |
| Estimable | A medias | Lo que cuesta resolver las listas dentro de celdas no se sabe hasta probarlo |
| Pequeña | Sí | Cabe en una fase, si la generación no obliga a instalar nada |
| Verificable | Sí | Se genera el de este repositorio y se abre |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-31 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-08-31 | Nace de `F-026`, con la épica `EP-012` aprobada ese día |
