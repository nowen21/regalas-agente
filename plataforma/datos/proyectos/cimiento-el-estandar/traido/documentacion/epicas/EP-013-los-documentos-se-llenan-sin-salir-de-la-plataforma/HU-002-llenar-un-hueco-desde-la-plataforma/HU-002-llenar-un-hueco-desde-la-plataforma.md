# HU-002 — Llenar un hueco desde la plataforma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-013 Los documentos se llenan sin salir de la plataforma](../epica.md) |
| **Funcionalidad** | `F-014` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Ciclo de vida |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus cinco criterios probados |
---

## 2. Narrativa

- **Como** quien está completando un documento del ciclo
- **Quiero** escribir lo que va en cada hueco sin salir de la plataforma
- **Para** que documentar sea parte del trabajo y no una tarea aparte

---

## 3. Contexto y descripción

La [HU-001](../HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md) muestra los huecos. Esta los llena: se escribe lo que va, y **queda en el archivo de texto**, no en una copia dentro de la base.

**Lo que decide si esto sirve o no es una sola cosa: que guardar no toque nada más.** La ficha de `F-014` trae su propia advertencia, *«si escribir ahí es más incómodo que en un editor, nadie lo va a usar»*, y la forma más rápida de volverlo incómodo es que la plataforma reescriba el documento a su manera. Un guardado que reformatea obliga a revisar el archivo entero cada vez, y entonces el editor gana.

**Se llena por huecos y no con un cuadro de texto libre.** Decidido con el usuario el 2026-09-01: redactar libre compite con el editor del usuario y pierde; pedir el hueco con su contexto es lo que un editor no puede hacer, porque no sabe qué molde sigue el archivo.

### 3.1 Reglas de negocio

- `RN-1` **Lo escrito va al archivo original del proyecto**, no a la copia de `datos/`. Decidido el 2026-09-01. La copia se rehace al importar, así que lo escrito ahí se perdería; y el proyecto quedaría igual.
- `RN-1.1` **Después de escribir se vuelve a traer ese documento**, para que la copia no se separe del original.
- `RN-2` **Se toca solo el hueco.** Ni una línea más del documento cambia.
- `RN-3` Escribir queda **registrado en la auditoría**: quién, cuándo, qué documento y qué hueco.
- `RN-4` Si el archivo cambió por fuera desde que se leyó, **se avisa y no se escribe encima**.
- `RN-5` Lo guardado queda **legible sin la plataforma**, con el mismo formato que tenía.

### 3.2 Supuestos

- Que el proyecto está bajo control de versiones, así que un guardado equivocado se revierte. No reemplaza a `RN-4`: avisar antes vale más que poder deshacer después.

### 3.3 Fuera de alcance

- Redactar libre, y editar lo que ya está escrito fuera de un hueco.
- Crear documentos nuevos, que necesita `F-011`, de la versión 5.
- Aprobar el documento o cerrar su fase, que son `F-015` y `F-013`.

---

## 4. Criterios de aceptación

### CA-01 — Se llena un hueco y queda en el archivo

```gherkin
Dado un documento con un hueco sin llenar
Cuando se escribe lo que va en él y se guarda
Entonces el archivo del proyecto queda con ese texto en el lugar del hueco
Y se lee igual abriéndolo por fuera de la plataforma
```

**Cómo validarlo:** sobre una copia de un documento real de este repositorio.
- **Aprobado cuando:** el texto está en el archivo, y el archivo se abre sin la plataforma.

### CA-02 — Lo que no es el hueco no cambia

```gherkin
Dado un documento cualquiera
Cuando se llena uno de sus huecos
Entonces el resto del archivo queda idéntico, carácter por carácter
```

**Cómo validarlo:** comparar el archivo entero antes y después, con el hueco descontado. Sobre un documento largo y con tablas, que es donde un guardado descuidado reformatea.
- **Aprobado cuando:** la única diferencia es el hueco. **Es el criterio que decide esta historia.**

### CA-03 — La cuenta de huecos baja

```gherkin
Dado un documento con N huecos
Cuando se llena uno
Entonces quedan N menos uno
```

**Cómo validarlo:** con la cuenta de la `HU-001`, antes y después.
- **Aprobado cuando:** baja en uno, no en más ni en menos.

### CA-04 — Si el archivo cambió por fuera, se avisa

```gherkin
Dado un documento que se abrió para llenar
Y que alguien cambió por fuera mientras tanto
Cuando se intenta guardar
Entonces se avisa y no se escribe encima
```

**Cómo validarlo:** leer, modificar el archivo por fuera, y guardar.
- **Aprobado cuando:** avisa y el cambio de afuera sigue ahí. Es el caso de «que NO pase» de esta historia.

### CA-05 — Queda registrado

```gherkin
Dado que se llenó un hueco
Cuando se consulta la auditoría
Entonces aparece quién escribió, cuándo, en qué documento y en qué hueco
```

**Cómo validarlo:** llenar uno y leer el registro.
- **Aprobado cuando:** el registro alcanza para saber qué pasó sin abrir el archivo.

### Criterios transversales

- Guardar sin escribir nada no cambia el archivo ni deja registro de un cambio que no hubo.
- Un documento sin huecos no se puede llenar, y lo dice.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | El archivo nunca queda a medio escribir, ni siquiera si el guardado se interrumpe |
| Trazabilidad | Todo cambio queda en la auditoría (`DA-12`) |
| Portabilidad | Lo guardado se lee sin la plataforma (`CA-3` de la ficha) |
| Comodidad | Llenar un hueco no debe costar más pasos que abrir el editor y escribirlo |

---

## 6. Diseño y referencias

- Funcionalidad `F-014` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md), criterios `CA-1` y `CA-3`.
- Requisito `RF-14` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Decisión que la gobierna: [`DA-12`](../../../../cvds/diseno/decisiones-de-arquitectura.md), que exige que todo cambio quede registrado.
- Quién guarda con constancia, y de dónde se parte: el módulo Auditoría, con su [especificación](../../../auditoria/spec.md).

---

## 7. Tareas técnicas derivadas

1. Escribir en el lugar del hueco sin tocar el resto del texto.
2. Guardar de forma que el archivo nunca quede a medias.
3. Detectar que el archivo cambió por fuera antes de escribir.
4. Registrar el cambio en la auditoría.
5. Recalcular la cuenta de huecos.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas](B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas/estado-fase.md) | Los cinco CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`: sin saber dónde está el hueco no hay dónde escribir |
| **Riesgo 1** | Que guardar reformatee el documento. Es el riesgo que hunde la historia, y por eso el `CA-02` compara el archivo entero |
| **Riesgo 2** | Que dos sesiones escriban a la vez sobre el mismo documento. Lo cubre el `CA-04` |
| **Riesgo 4** | **Es la primera vez que la plataforma escribe fuera de `datos/`.** Hasta hoy solo leía los proyectos. Un guardado equivocado toca el repositorio del usuario, y por eso el `CA-02` compara el archivo entero y el `CA-04` no escribe encima de un cambio ajeno |
| **Riesgo 3** | Que llenar por huecos resulte incómodo y nadie lo use. Se mide llenando un documento real de punta a punta, no un ejemplo de tres huecos |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ El camino decidido: se llena por huecos, no con un cuadro libre.
- ☑ Dónde se escribe, decidido el 2026-09-01: en el archivo original del proyecto.
- ☑ El módulo Ciclo de vida, con [especificación aprobada](../../../ciclo-de-vida/spec.md) el 2026-09-01.
- ☑ La `HU-001`, cerrada el 2026-09-01 con **Cumple**.

## 11. Definition of Done

- ☑ Los cinco criterios con veredicto y evidencia.
- ☑ Un documento real de este repositorio llenado, y le quedó **cero** por llenar.
- ☑ Comprobado carácter por carácter: **cero cambios fuera del hueco**.
- ☑ El registro de auditoría, leído.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la `HU-001` |
| Negociable | Sí | Cómo se pide cada hueco se puede ajustar |
| Valiosa | Sí | Es lo que la funcionalidad promete: documentar sin salir |
| Estimable | Sí | Es escribir en un lugar del texto y guardar bien |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se compara el archivo entero antes y después |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-09-01 | Nace de `F-014`, con la épica `EP-013` aprobada ese día |
