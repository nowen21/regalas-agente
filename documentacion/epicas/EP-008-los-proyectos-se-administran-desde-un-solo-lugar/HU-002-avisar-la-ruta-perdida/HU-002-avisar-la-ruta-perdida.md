# HU-002 — Avisar cuando la ruta de un proyecto se pierde

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../epica.md) |
| **Funcionalidad** | `F-002` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Proyectos |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-08-25, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien tiene varios proyectos y a veces mueve carpetas
- **Quiero** que la plataforma me diga cuando la ruta de un proyecto ya no existe
- **Para** no descubrirlo el día que necesito trabajar en él

---

## 3. Contexto y descripción

La plataforma guarda dónde vive el código de cada proyecto. Esa ruta se rompe sola: alguien mueve la carpeta, cambia de máquina, o la borra. Sin aviso, la plataforma seguiría mostrando como vivo algo que no está.

**Perder la ruta no pierde nada.** La documentación vive en la plataforma, no allá.

### 3.1 Reglas de negocio

- `RN-1` La documentación de un proyecto con ruta perdida se sigue mostrando.
- `RN-2` El aviso dice qué ruta se buscó, no solo que falló.

### 3.2 Supuestos

- Comprobar la existencia de la ruta al listar es suficiente, y no hace falta vigilarla todo el tiempo.

### 3.3 Fuera de alcance

- Corregir la ruta sola, buscando la carpeta en otro lado.

---

## 4. Criterios de aceptación

### CA-01 — La ruta que dejó de existir se avisa

```gherkin
Dado un proyecto registrado cuya carpeta se borró o se movió
Cuando el usuario abre la lista de proyectos
Entonces ese proyecto aparece marcado
Y el aviso dice qué ruta se buscó
```

### CA-02 — Su documentación se sigue viendo

```gherkin
Dado un proyecto con la ruta perdida
Cuando el usuario entra a él
Entonces ve su documentación completa
Y ve el aviso de que su código no está donde estaba
```

### CA-03 — Volver a apuntar la ruta quita el aviso

```gherkin
Dado un proyecto con la ruta perdida
Cuando el usuario corrige la ruta a una carpeta que existe
Entonces el aviso desaparece
Y el cambio queda registrado en la auditoría
```

### Criterios transversales

- La comprobación de rutas no hace que listar cincuenta proyectos pase de un segundo (`RNF-02`).

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | Comprobar las rutas cabe dentro del segundo que exige `RNF-02` |
| Disponibilidad | Funciona sin red |

---

## 6. Diseño y referencias

- Especificación: [documentacion/proyectos/spec.md](../../../proyectos/spec.md), sección 6.
- Pantalla `P-01` del [diseño de interfaz](../../../../cvds/diseno/diseno-de-interfaz.md).

---

## 7. Tareas técnicas derivadas

1. Comprobar la existencia de cada ruta al listar.
2. Marcar el proyecto y componer el aviso con la ruta buscada.
3. Permitir corregir la ruta, y registrar el cambio.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [C · La ruta perdida se avisa](C-EP-008-HU-002-la-ruta-perdida-se-avisa/README.md) | Esta historia | Cerrada el 2026-08-25, commit `ff2248e`. Los tres criterios con veredicto |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `HU-001`: primero hay que poder conectar |
| **Riesgo** | Que comprobar muchas rutas haga lenta la lista. Se mide contra `RNF-02` |

---

## 10. Definition of Ready

- ☑ La especificación del módulo está aprobada.
- ☑ `HU-001` está definida.
- ☑ Los tres criterios son comprobables.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Medido: listar cincuenta proyectos tarda **0.010 s**, contra un límite de un segundo.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita que exista el registro de `HU-001` |
| Negociable | Sí | Cuándo se comprueba la ruta se puede ajustar |
| Valiosa | Sí | Evita descubrir el problema en el peor momento |
| Estimable | Sí | Es una comprobación y un aviso |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se prueba moviendo una carpeta |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-002`, al aprobarse el inventario de Cimiento |
| 2026-08-25 | Se abre la fase C. Al planearla se vio que `CA-01` y `CA-02` ya estaban casi construidos, de rebote, por la fase B |
| 2026-08-25 | Cierra la fase C. El aviso ya nombra la ruta, y se puede corregir |
