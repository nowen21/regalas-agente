# HU-007 — Revisar qué le falta al proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien no sabe si su proyecto quedó bien instalado
- **Quiero** una revisión que diga qué le falta
- **Para** enterarme antes de necesitarlo, y no cuando algo no funciona

---

## 3. Contexto y descripción

Una instalación puede quedar a medias por muchos motivos: se interrumpió, se instaló una versión vieja, alguien borró una carpeta. Sin una forma de revisar, eso se descubre el día que algo no anda.

La revisión responde una sola pregunta: qué de lo que debería tener no está. Y lo dice componente por componente, para poder arreglar sin adivinar.

Además tiene un uso que vale más que revisar a mano: mientras falte algo, se avisa en cada sesión. Cuando ya no falta nada, el aviso desaparece; su ausencia es la señal de que está completo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se puede revisar qué le falta al proyecto, componente por componente |
| RN-02 | La lista de lo que debe tener vive fuera del programa, en un documento |
| RN-03 | Mientras falte algo, se avisa en cada sesión |
| RN-04 | Cuando no falta nada, el aviso desaparece: su ausencia es la señal |
| RN-05 | La revisión no instala nada; solo dice qué falta |
| RN-06 | El aviso no detiene el trabajo |

### 3.2 Supuestos

- Un aviso permanente se deja de leer, así que el aviso tiene que poder apagarse solo.

### 3.3 Fuera de alcance

- Instalar lo que falta. Eso lo hace el instalador.
- Revisar varios proyectos a la vez.

---

## 4. Criterios de aceptación

### CA-01 — La revisión dice qué falta, componente por componente

```gherkin
Dado que a un proyecto le falta un componente
Cuando se revisa
Entonces se nombra ese componente y qué le falta
```

**Cómo validarlo:**

1. Quitar un componente de un proyecto instalado.
2. Revisar. Resultado esperado: lo nombra, con qué falta y cómo se arregla.
3. Instalarlo de nuevo y revisar. Resultado esperado: no lo nombra.
- **Aprobado cuando:** se puede arreglar sin abrir el programa.

### CA-02 — El aviso se apaga solo cuando ya no falta nada

```gherkin
Dado que el proyecto tenía algo incompleto y se arregló
Cuando se abre una sesión
Entonces no aparece ningún aviso de instalación
```

**Cómo validarlo:**

1. Con algo faltante, abrir sesión. Resultado esperado: aparece el aviso.
2. Completar la instalación y abrir sesión otra vez. Resultado esperado: el aviso ya no aparece.
3. Buscar el archivo de aviso. Resultado esperado: se borró.
- **Aprobado cuando:** el silencio significa que está completo.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto sin instalar responde con la lista completa, no con un error.
- [ ] **Inocuidad** — revisar no modifica nada.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Mantenimiento** | La lista de lo que debe tener vive en un documento, no en el código |
| **Rendimiento** | Corre en cada sesión sin que se note |
| **Claridad** | Dice cómo arreglar cada faltante |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), criterio CAE-05.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la lista de lo que un proyecto debe tener, fuera del programa.
- [ ] Revisar cada componente y decir qué falta.
- [ ] Escribir el aviso mientras falte algo y borrarlo cuando no falte.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-007-HU-007-la-revision-ve-la-cadena](A-EP-007-HU-007-la-revision-ve-la-cadena/README.md) | CA-01 y CA-02 | Cerrada 2026-08-16 (v23.0.0) |

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
| Dependencia | HU-001, porque revisa lo que el instalador deja puesto | Alto |
| Dependencia | EP-005, porque el aviso aparece al abrir la sesión | Medio |
| Riesgo | Que el aviso se vuelva permanente y se ignore | Se borra solo cuando ya no falta nada |
| Riesgo | Que la lista se separe de lo que el instalador hace | La lista vive en un documento y el instalador la usa |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La revisión dice qué falta y cómo se arregla
- [ ] El aviso aparece mientras falte y se borra cuando no
- [ ] Revisar no modifica nada
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Revisa lo que instala HU-001 |
| **N**egociable | Sí | Qué entra en la lista se puede discutir |
| **V**aliosa | Sí | Evita descubrir la instalación a medias cuando ya estorba |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Una revisión y un aviso |
| **T**esteable | Sí | Se prueba quitando componentes |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Fase `A` (v23.0.0): la revisión pasa a 14 puntos y mira si el proyecto arrancó la cadena de `02·F0`. Es el único punto que el instalador no instala, y por eso su fila lo dice |
