# HU-004 — Administrar un proyecto conectado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../epica.md) |
| **Funcionalidad** | `F-035` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Proyectos |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Cerrada el 2026-08-25, con sus cinco criterios probados |

---

## 2. Narrativa

- **Como** quien conecta proyectos a la plataforma
- **Quiero** poder desconectar uno, renombrarlo o corregir la versión que declara
- **Para** que equivocarme al conectarlo no sea permanente

---

## 3. Contexto y descripción

Hoy conectar no tiene reversa. Un proyecto registrado con el nombre o la ruta equivocados queda así para siempre, y el único arreglo es editar a mano el texto que la plataforma administra, que es justo lo que la plataforma vino a evitar.

**Ninguno de los tres cambios borra nada.** Desconectar saca el proyecto de la lista y deja su documentación donde está; renombrar cambia el nombre sin mover la carpeta.

**Esto ya estaba decidido sin estar pedido.** La especificación del módulo dice desde el 2026-08-25 cómo se comporta desconectar, en su §7 y en su §12, y ninguna funcionalidad lo pedía. Lo que faltaba no era decidir: era pedirlo.

### 3.1 Reglas de negocio

- `RN-1` Desconectar no borra la documentación del proyecto.
- `RN-2` Renombrar no mueve la carpeta donde vive su documentación.
- `RN-3` Los tres cambios piden confirmación antes de hacerse.
- `RN-4` Los tres quedan registrados en la auditoría.
- `RN-5` La versión corregida se comprueba contra las publicadas, igual que al conectar.

### 3.2 Supuestos

- Que desconectar y volver a conectar el mismo proyecto es una salida aceptable para corregir su ruta. Corregir la ruta perdida sin desconectar es `HU-002`.

### 3.3 Fuera de alcance

- Borrar la documentación de un proyecto. Desconectar no borra, y esa decisión ya está tomada.
- Corregir la ruta perdida, que es [HU-002](../HU-002-avisar-la-ruta-perdida/HU-002-avisar-la-ruta-perdida.md).
- Configurar qué reglas rigen en cada proyecto, que es `F-004` de la versión 5.

---

## 4. Criterios de aceptación

### CA-01 — Desconectar saca el proyecto y deja su documentación

```gherkin
Dado un proyecto conectado, con documentación guardada
Cuando el usuario lo desconecta y confirma
Entonces deja de aparecer en la lista
Y su documentación sigue estando en la plataforma
```

**Cómo validarlo:** desconectar y después buscar su carpeta de documentación, que tiene que seguir ahí con lo que tenía.

### CA-02 — Renombrar no mueve la carpeta

```gherkin
Dado un proyecto conectado
Cuando el usuario le cambia el nombre y confirma
Entonces la lista muestra el nombre nuevo
Y su carpeta de documentación sigue donde estaba
```

**Cómo validarlo:** anotar dónde está la carpeta antes, renombrar, y comprobar que es la misma.

### CA-03 — La versión corregida se vuelve a comprobar

```gherkin
Dado un proyecto que declara una versión de reglas
Cuando el usuario pide corregirla
Entonces se vuelve a leer del proyecto y se comprueba contra las publicadas
Y si no existe, no se guarda
```

### CA-04 — Los tres piden confirmación y quedan registrados

```gherkin
Dado cualquiera de los tres cambios
Cuando el usuario lo pide
Entonces se le pregunta antes de hacerlo
Y al confirmarlo, la acción queda en la auditoría con quién y cuándo
```

### CA-05 — Que NO pase: que desconectar toque el proyecto

```gherkin
Dado un proyecto conectado
Cuando se desconecta
Entonces ningún archivo de su carpeta de código cambia, se mueve ni se borra
```

**Cómo validarlo:** comparar la carpeta del proyecto antes y después, archivo por archivo. Es el mismo caso que protege `HU-001` al conectar.

### Criterios transversales

- Desconectar un proyecto que no existe lo dice, en vez de fallar en silencio.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Trazabilidad | `RNF-12`: los tres cambios dicen quién, cuándo y sobre qué |
| Recuperación | Lo que queda escrito es texto, y el índice se reconstruye (`RNF-04`) |
| Disponibilidad | Funciona sin red (`RNF-03`) |

---

## 6. Diseño y referencias

- Especificación: [documentacion/proyectos/spec.md](../../../proyectos/spec.md), §1, §6, §7 y §12.
- Funcionalidad `F-035` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-35` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Pantalla `P-02` Un proyecto, del [diseño de interfaz](../../../../cvds/diseno/diseno-de-interfaz.md).
- De dónde sale: [pendientes/86](../../../../pendientes/86-conectar-un-proyecto-no-tiene-reversa.md).

---

## 7. Tareas técnicas derivadas

1. Desconectar, dejando la documentación.
2. Renombrar, sin mover la carpeta.
3. Corregir la versión declarada, comprobándola.
4. La confirmación de los tres, y su registro en la auditoría.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [H · Un proyecto conectado se administra](H-EP-008-HU-004-un-proyecto-conectado-se-administra/README.md) | Esta historia | Cerrada el 2026-08-25. Los cinco criterios con veredicto |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `HU-001`, fase B: hay que poder conectar antes de poder desconectar |
| **Riesgo 1** | Que desconectar deje la documentación huérfana y nadie sepa de quién era. Se mitiga dejando en su carpeta la constancia de cuándo se desconectó |
| **Riesgo 2** | Que renombrar y el identificador guardado se desincronicen. El código de la fase B ya los guarda aparte a propósito |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su cambio anotado.
- ☑ La especificación del módulo ya define cómo se comporta desconectar.
- ☑ Los cinco criterios son comprobables.

## 11. Definition of Done

- ☑ Los cinco criterios con veredicto y evidencia.
- ☑ Comprobado que desconectar no borra la documentación: se compara su contenido, no que la carpeta exista.
- ☑ Comprobado que la carpeta del proyecto no cambió, archivo por archivo.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la fase B |
| Negociable | Sí | Qué se puede corregir se puede ajustar |
| Valiosa | Sí | Sin esto, equivocarse al conectar es permanente |
| Estimable | Sí | Son tres cambios sobre algo que ya existe |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se conecta mal a propósito y se comprueba que se puede deshacer |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-035`, que entró al inventario ese día. La destapó el usuario al ver la primera pantalla: «pero eso no tiene administración?» |
| 2026-08-25 | Aprobada, junto con los dos planes de su fase H |
| 2026-08-25 | Cierra la fase H. Conectar ya tiene reversa |
