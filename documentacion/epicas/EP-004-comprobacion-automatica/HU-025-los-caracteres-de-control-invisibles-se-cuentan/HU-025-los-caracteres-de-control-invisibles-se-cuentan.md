# HU-025 — Los caracteres de control invisibles se cuentan y se quitan

> Historia de usuario del estándar. Nace del [pendiente 92](../../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md), aprobado por el usuario el 2026-08-30.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-025 |
| **Épica / Feature** | [EP-004 — Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | 2 puntos |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

**Como** quien lee un documento del proyecto
**quiero** que ningún carácter de control se cuele dentro de un archivo de texto
**para** que una tabla no se rompa sin que nadie lo vea.

---

## 3. Contexto y descripción

Al ir a agregar una fila a la tabla de fases de una historia, la fila que ya estaba empezaba con un carácter de control en vez de con la barra de la tabla. Esa fila **no se renderiza como fila**: en cualquier visor desaparece del cuadro y queda como un párrafo suelto debajo.

Buscándolo aparece en **26 archivos**, trece de ellos en `documentacion/`.

El programa que cuenta las marcas invisibles ya conoce siete caracteres —el espacio duro, el de ancho cero, el guion suave y cuatro más— y los limpia. Ninguno de control está en esa lista.

### 3.1 Reglas de negocio

- Un carácter que no se ve leyendo y que rompe el documento es exactamente lo que un programa debe cazar: una persona no puede.
- Lo que la lista del anexo diga y lo que el programa cuente tienen que ser lo mismo.
- Limpiar los archivos que ya lo traen va en su propio commit, sin mezclarse con otro trabajo.

### 3.2 Supuestos

- Los caracteres de control dentro de un bloque de código pueden ser legítimos y no se tocan.
- El salto de línea y el tabulador no son el problema.

### 3.3 Fuera de alcance

- **Averiguar de dónde salieron.** Nadie sabe qué los metió, y saberlo no es condición para limpiarlos.
- Los caracteres invisibles que ya se cuentan, que siguen igual.

---

## 4. Criterios de aceptación

### CA-01 — El carácter de control se reporta, con su archivo y su línea

```gherkin
Dado un archivo de texto con un carácter de control dentro
Cuando se corre el validador de marcas
Entonces lo reporta nombrando el archivo, la línea y qué carácter es
```

**Cómo validarlo:**
1. Crear una carpeta temporal con un archivo que traiga un carácter de control en medio de una línea.
2. Correr el validador de marcas sobre esa carpeta → resultado esperado: un hallazgo que nombra el archivo, la línea y el carácter.
3. Comprobar que el nombre del carácter se entiende sin conocer la tabla de códigos.
- **Aprobado cuando:** el hallazgo dice dónde está y qué es, sin que haya que buscarlo a mano.

### CA-02 — El árbol queda en cero

```gherkin
Dado que 26 archivos del repositorio traen un carácter de control
Cuando se limpian
Entonces la búsqueda no devuelve ninguno
Y el texto que se ve no cambió
```

**Cómo validarlo:**
1. Antes de limpiar, contar cuántos archivos lo traen y anotar el número.
2. Limpiar, y volver a contar → resultado esperado: cero.
3. Comparar un archivo antes y después → resultado esperado: la única diferencia es el carácter que no se veía.
- **Aprobado cuando:** la cuenta queda en cero y ninguna palabra del texto cambió.

### CA-03 — Lo legítimo no se toca

```gherkin
Dado un archivo con un tabulador dentro de un bloque de código
Cuando se corre el validador
Entonces no lo reporta
```

**Cómo validarlo:**
1. Crear un archivo con un bloque de código que use tabulador para alinear.
2. Correr el validador → resultado esperado: ningún hallazgo por ese tabulador.
- **Aprobado cuando:** el caso legítimo pasa sin reclamo.

### Criterios de aceptación transversales

- [x] **Límites** — el archivo vacío y el que no se puede decodificar tienen comportamiento definido.
- [x] **No regresión** — los siete caracteres que ya se contaban se siguen contando igual.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | La comprobación nueva no agrega ninguna pasada: va en la misma lectura del archivo |
| RNF-02 | **Trazabilidad** | La lista del anexo y la del programa dicen lo mismo, y eso se prueba |

---

## 6. Diseño y referencias

- **Documento funcional:** el [pendiente 92](../../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md).
- **Programa afectado:** `validadores/marcas.py`.
- **La norma que se amplía:** la lista de marcas invisibles del anexo de generación automática.

---

## 7. Tareas técnicas derivadas

- [ ] Programa: contar los caracteres de control, y decidir si se barre el rango entero o solo los que aparecieron
- [ ] Programa: que la limpieza los quite
- [ ] Norma: agregar la fila al anexo, para que la lista y el programa digan lo mismo
- [ ] Limpieza: los 26 archivos, en su propio commit
- [ ] Pruebas: un caso por criterio, incluido el legítimo que no se toca

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados.

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| Sin abrir todavía | — | — | — | — | — | Sin empezar |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la limpieza cambie texto visible | El CA-02 compara el antes y el después: la única diferencia permitida es el carácter invisible |
| Riesgo | Que se limpien archivos de otras sesiones en curso | Se comprueba el registro de sesiones antes de tocar, como se hizo con los enlaces el 2026-08-30 |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible: no aplica, no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código implementado y en rama principal
- [ ] Pruebas unitarias e integración pasando
- [ ] Code review aprobado
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica actualizada
- [ ] Desplegada: no aplica, no hay ambiente
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No depende de ninguna otra historia |
| **N**egociable | ☑ | Si se barre el rango entero o solo lo que apareció, se discute |
| **V**aliosa | ☑ | Hoy una historia muestra una fase menos de las que tiene |
| **E**stimable | ☑ | Un programa y una limpieza contada |
| **S**mall (pequeña) | ☑ | Una fase, y la limpieza en su commit |
| **T**esteable | ☑ | La cuenta antes y después es el criterio |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-30 | El agente | Se crea la historia a partir del pendiente 92, aprobado por el usuario |
