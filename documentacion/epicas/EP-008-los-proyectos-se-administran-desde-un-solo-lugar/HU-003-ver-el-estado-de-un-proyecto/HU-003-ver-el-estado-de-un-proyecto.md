# HU-003 — Ver el estado de un proyecto sin entrar a él

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../epica.md) |
| **Funcionalidad** | `F-003` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Proyectos |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Ready |

---

## 2. Narrativa

- **Como** quien responde por varios proyectos
- **Quiero** ver en qué va cualquiera sin abrir su carpeta
- **Para** decidir dónde poner el tiempo sin gastar media hora averiguándolo

---

## 3. Contexto y descripción

Es el motivo por el que la plataforma existe. El estado se calcula leyendo lo que la plataforma guardó de ese proyecto: qué etapas tienen documento, qué fases están abiertas y qué falta aprobar.

**El estado no se guarda a mano.** Se calcula, y si se guarda es como índice que se rehace.

### 3.1 Reglas de negocio

- `RN-1` Lo que no tiene prueba corrida se muestra como sin verificar.
- `RN-2` Un proyecto sin nada escrito lo dice; no muestra una pantalla vacía.
- `RN-3` Lo aprobado se distingue de lo que está en borrador, con palabras y no solo con color.

### 3.2 Supuestos

- Que el estado se puede calcular sin abrir la carpeta del proyecto.

### 3.3 Fuera de alcance

- Reportar y comparar proyectos entre sí, que es `F-030` de la versión 5.

---

## 4. Criterios de aceptación

### CA-01 — El estado se ve sin abrir la carpeta

```gherkin
Dado un proyecto conectado con documentación traída
Cuando el usuario lo abre en la plataforma
Entonces ve qué etapas tienen documento, qué fases están abiertas y qué falta aprobar
Y no hace falta abrir su carpeta para saberlo
```

### CA-02 — Un proyecto sin trabajo abierto lo dice

```gherkin
Dado un proyecto conectado y sin documentación
Cuando el usuario lo abre
Entonces se muestra «sin empezar», con qué haría falta para arrancar
Y no se muestra una pantalla vacía
```

### CA-03 — Lo aprobado se distingue de lo que no

```gherkin
Dado un proyecto con documentos aprobados y en borrador
Cuando el usuario ve su estado
Entonces cada documento dice si está aprobado y desde cuándo
Y lo dice con palabras, no solo con color
```

### Criterios transversales

- Listar cincuenta proyectos con su estado responde en menos de un segundo (`RNF-02`).
- Un proyecto con la ruta perdida muestra su estado igual, con el aviso.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | `RNF-02`: menos de un segundo con cincuenta proyectos |
| Usabilidad | `RNF-07`: se entiende sin conocer el proyecto, y sin siglas sin explicar |

---

## 6. Diseño y referencias

- Especificación: [documentacion/proyectos/spec.md](../../../proyectos/spec.md), sección 6.
- Pantallas `P-01` y `P-02` del [diseño de interfaz](../../../../cvds/diseno/diseno-de-interfaz.md).
- Sección 5 del [modelo de datos](../../../../cvds/diseno/modelo-de-datos.md): el estado se calcula.

---

## 7. Tareas técnicas derivadas

1. Calcular el estado de un proyecto a partir de sus documentos y fases.
2. Guardarlo como índice, con cómo se rehace.
3. Mostrarlo, distinguiendo aprobado de borrador y señalando lo sin verificar.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| G · Se ve el estado de un proyecto | Esta historia | Sin abrir |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `HU-001`, y de que EP-010 haya traído algo: mostrar sin contenido sería mostrar vacío |
| **Riesgo** | Que calcular el estado sea lento con muchos documentos. Se guarda como índice |

---

## 10. Definition of Ready

- ☑ La especificación del módulo está aprobada.
- ☑ Está definido qué se muestra como estado.
- ☑ Los tres criterios son comprobables.

## 11. Definition of Done

- ☐ Los tres criterios con veredicto y evidencia.
- ☐ Medido el tiempo de respuesta con cincuenta proyectos.
- ☐ Comprobado con un proyecto vacío y con uno con la ruta perdida.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita proyectos conectados y algo traído |
| Negociable | Sí | Qué se muestra en el estado se puede ajustar |
| Valiosa | Sí | Es el motivo de la plataforma |
| Estimable | Sí | Es calcular y mostrar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se prueba mirando la pantalla y midiendo el tiempo |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-003`, al aprobarse el inventario de Cimiento |
