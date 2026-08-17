# HU-005 — No pisar lo que escribió la persona

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien ya escribió cosas en su proyecto
- **Quiero** que instalar o actualizar nunca borre lo que escribí
- **Para** poder correr el instalador sin revisar antes qué voy a perder

---

## 3. Contexto y descripción

Un instalador que pisa archivos se corre una vez y no se vuelve a correr nunca. Y entonces el proyecto se queda viejo para siempre, que es justo lo que la épica quiere evitar.

La distinción que resuelve esto es entre lo generado y lo escrito. Lo generado lo produce el estándar y se puede reescribir sin pérdida. Lo escrito lo llenó una persona con datos de su proyecto, y eso no se toca: a lo sumo se le agrega lo que falte al final.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo escrito por una persona no se pisa nunca |
| RN-02 | Lo generado por el estándar se puede reescribir entero |
| RN-03 | Cada componente declara a cuál de los dos grupos pertenece |
| RN-04 | A un documento que la persona llenó se le pueden agregar las secciones nuevas, al final, sin tocar lo que ya decía |
| RN-05 | Ante la duda, no se pisa |

### 3.2 Supuestos

- Se puede distinguir un documento generado de uno llenado, porque cada componente lo declara.

### 3.3 Fuera de alcance

- Resolver conflictos de contenido entre lo escrito y lo nuevo. Eso lo decide la persona.

---

## 4. Criterios de aceptación

### CA-01 — Un documento llenado por la persona no se pierde

```gherkin
Dado que la persona llenó un documento que vino del estándar
Cuando se instala otra vez
Entonces lo que escribió sigue ahí
```

**Cómo validarlo:**

1. Llenar con datos propios un documento heredado del estándar.
2. Correr la instalación otra vez. Resultado esperado: el texto propio sigue igual.
3. Comparar palabra por palabra. Resultado esperado: no se perdió nada.
- **Aprobado cuando:** instalar es seguro sobre un proyecto con trabajo.

### CA-02 — Las secciones nuevas se agregan sin tocar lo viejo

```gherkin
Dado que el estándar agregó una sección a un documento heredado
Cuando se instala sobre un proyecto que ya lo tenía llenado
Entonces la sección nueva aparece al final
Y lo que ya estaba escrito queda igual
```

**Cómo validarlo:**

1. Agregar una sección al documento modelo en el estándar.
2. Instalar sobre el proyecto que ya lo tenía llenado. Resultado esperado: la sección nueva se agregó al final.
3. Revisar lo anterior. Resultado esperado: intacto.
- **Aprobado cuando:** actualizar no obliga a elegir entre lo nuevo y lo escrito.

### Criterios de aceptación transversales

- [ ] **Límites** — un archivo que la persona modificó y que el estándar considera generado tiene comportamiento definido y se avisa.
- [ ] **Errores** — si no se puede decidir si pisar, no se pisa y se dice.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Seguridad de datos** | Ninguna pérdida de texto escrito por una persona |
| **Prudencia** | Ante la duda, no se pisa |
| **Transparencia** | Se dice qué se reescribió y qué se respetó |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), criterio CAE-03.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Declarar, por componente, si es generado o llenado.
- [ ] Reescribir solo lo generado.
- [ ] Agregar al final las secciones nuevas de lo llenado.
- [ ] Reportar qué se reescribió y qué se respetó.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito](A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito/README.md) | CA-01 y CA-02 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase retro-documenta la exigencia central de la épica:** que actualizar no borre lo que la persona escribió. Falta la prueba, con el archivo que más duele: el `CLAUDE.md` del proyecto, que mezcla lo heredado con lo propio.

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
| Dependencia | HU-001, porque es la regla que gobierna cómo instala | Alto |
| Riesgo | Que un componente esté mal clasificado y se pise algo | Ante la duda no se pisa, y se reporta qué se tocó |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Nada escrito por una persona se pierde
- [ ] Las secciones nuevas se agregan sin tocar lo anterior
- [ ] Se reporta qué se reescribió
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Es una regla del instalador de HU-001 |
| **N**egociable | Sí | Cómo se agregan las secciones nuevas se puede discutir |
| **V**aliosa | Sí | Es lo que hace que el instalador se vuelva a correr |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Una distinción y su aplicación |
| **T**esteable | Sí | Se prueba instalando sobre documentos llenados |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
