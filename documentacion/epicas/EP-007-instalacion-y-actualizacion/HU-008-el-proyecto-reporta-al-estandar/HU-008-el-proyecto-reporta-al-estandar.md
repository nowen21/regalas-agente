# HU-008 — El proyecto reporta lo que es del estándar, y el estándar le avisa de vuelta

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Canal proyecto ↔ estándar |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | `shopnest-mesa`, que lo reportó |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Done |

---

## 2. Narrativa

- **Como** quien trabaja en un proyecto que heredó el estándar y encuentra un defecto del estándar
- **Quiero** un procedimiento escrito para reportarlo sin tocarlo, y que me avisen cuando esté corregido
- **Para** que el arreglo llegue a todos los proyectos y no se quede parchado solo en el mío

---

## 3. Contexto y descripción

El estándar dice qué no se toca, pero no dice **qué hacer con lo que no se toca**.

Un proyecto que encuentra un defecto del estándar hoy tiene tres caminos y ninguno escrito: arreglarlo por su cuenta —y pisar a los demás proyectos—, anotarlo solo en su repositorio —donde el estándar nunca lo va a ver— o no hacer nada. Los tres pasaron en `shopnest-mesa` el mismo día:

- El 2026-08-15 se parchearon los enlaces en las copias locales y se dejó anotado *«su pendiente va en el repositorio del estándar y ese no es este»*. El estándar no se enteró durante un día entero.
- El 2026-08-16 el agente creó el pendiente acá y **cerró el del proyecto**, dándolo por traspasado. El seguimiento se perdió en el mismo acto de traspasarlo.

Nada de eso incumplió ninguna regla, porque la regla no existe.

**El procedimiento ya está dictado.** El usuario lo escribió completo el 2026-08-16, en siete pasos:

| # | Paso |
|---|---|
| 1 | No modificar el estándar. El defecto se deja intacto para que lo corrija quien lo escribe |
| 2 | Crear un pendiente en `pendientes/` del estándar, con qué se encontró y qué debe corregirse |
| 3 | Nombrar explícitamente el proyecto de origen en ese pendiente |
| 4 | Crear también un pendiente en el proyecto, diciendo que hay una corrección pendiente en el estándar |
| 5 | El proyecto sigue trabajando solo lo suyo |
| 6 | El estándar avisa al proyecto cuando la corrección esté hecha |
| 7 | El pendiente del proyecto queda abierto hasta confirmar la corrección |

**La mitad que falta es el paso 6.** Los pasos 1 a 5 se han venido haciendo por criterio de cada sesión; el aviso de vuelta no lo hace nadie, y sin él el paso 7 deja pendientes abiertos para siempre en los proyectos. El estándar sí puede hacerlo: sabe qué proyectos lo usan y dónde vive cada uno, porque están listados en [plantillas/proyectos.md](../../../../plantillas/proyectos.md).

**Es la contraparte de la instalación.** La épica ya cubre cómo el estándar baja al proyecto; esto es cómo el proyecto sube al estándar. Sin este canal la herencia va en un solo sentido, y el estándar solo aprende de lo que le pasa a él mismo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un proyecto no modifica el estándar: lo reporta |
| RN-02 | Todo reporte deja dos pendientes, uno en cada lado, y cada uno nombra al otro |
| RN-03 | El pendiente del estándar nombra el proyecto de origen; sin eso no hay trazabilidad |
| RN-04 | El pendiente del proyecto queda abierto hasta que llegue el aviso de que se corrigió |
| RN-05 | Al cerrar el pendiente, el estándar le avisa al proyecto de origen |
| RN-06 | Si el arreglo rige para todos los proyectos, el aviso va a todos, no solo al de origen |

### 3.2 Supuestos

- Los proyectos que heredan el estándar viven en la misma máquina y están listados, así que el aviso se puede escribir en su repositorio.

### 3.3 Fuera de alcance

- Corregir el defecto reportado. Cada uno se construye por su cuenta, en la HU que le corresponda.
- Avisarle a un proyecto que no esté en la lista, o que viva en otra máquina.

---

## 4. Criterios de aceptación

### CA-01 — El reporte deja los dos pendientes

```gherkin
Dado que un proyecto encuentra un defecto del estándar
Cuando lo reporta siguiendo el procedimiento
Entonces queda un pendiente en el estándar y otro en el proyecto
Y cada uno nombra al otro
```

**Cómo validarlo:**

1. En una carpeta de proyecto de prueba, simular un defecto del estándar.
2. Seguir el procedimiento escrito en la regla.
3. Abrir los dos pendientes. Resultado esperado: el del estándar nombra el proyecto de origen y el pendiente de seguimiento; el del proyecto nombra el pendiente del estándar.
- **Aprobado cuando:** los dos existen y el enlace resuelve en los dos sentidos.

### CA-02 — Un pendiente sin proyecto de origen se reporta

```gherkin
Dado que un pendiente del estándar nació de un proyecto
Cuando no nombra cuál
Entonces la comprobación lo reporta
Y la corrida termina con error
```

**Cómo validarlo:**

1. Escribir un pendiente de prueba que diga que salió de un proyecto, sin nombrarlo.
2. Correr la comprobación de cruces. Resultado esperado: lo reporta.
3. Nombrar el proyecto y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el que no nombra se reporta y el que nombra no.

### CA-03 — Al cerrar, el aviso llega solo

```gherkin
Dado que un pendiente reportado por un proyecto se marca como hecho
Cuando se cierra
Entonces se escribe el aviso en el repositorio del proyecto de origen
Y el aviso dice qué versión trae la corrección
```

**Cómo validarlo:**

1. Cerrar un pendiente de prueba que declare su proyecto de origen.
2. Abrir el repositorio de ese proyecto y buscar el aviso. Resultado esperado: está, y dice qué versión lo corrige.
3. Abrir el repositorio de otro proyecto de la lista. Resultado esperado: no tiene aviso, porque no era el de origen.
- **Aprobado cuando:** el aviso llega al de origen y no al resto.

### CA-04 — El arreglo que rige para todos avisa a todos

```gherkin
Dado que el pendiente declara que su corrección rige para todos los proyectos
Cuando se cierra
Entonces el aviso se escribe en todos los proyectos de la lista
```

**Cómo validarlo:**

1. Cerrar un pendiente de prueba marcado como «avisar a todos».
2. Recorrer los proyectos de [plantillas/proyectos.md](../../../../plantillas/proyectos.md) y buscar el aviso en cada uno. Resultado esperado: está en todos.
- **Aprobado cuando:** ninguno de la lista se quedó sin aviso.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto de la lista que ya no existe en disco, y un pendiente sin proyecto de origen que sí nació acá, tienen comportamiento definido.
- [ ] **Errores** — si no se puede escribir en el repositorio del proyecto, se dice cuál falló y el cierre no se da por completo en silencio.
- [ ] **No regresión** — los pendientes que ya declaran su proyecto de origen siguen validando igual.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El aviso dice qué pendiente se cerró, con qué versión y en qué fase |
| RNF-02 | **Idempotencia** | Cerrar dos veces el mismo pendiente no duplica el aviso |
| RNF-03 | **Claridad** | El aviso lo entiende quien no siguió el trabajo del estándar |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md).
- **Moldes ya escritos con la forma correcta:** [pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md](../../../../pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md) y [pendientes/hecho/renombrar-deja-el-resumen-coherente.md](../../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md).
- **Lista de proyectos:** [plantillas/proyectos.md](../../../../plantillas/proyectos.md).
- **Programa donde encaja la comprobación:** [validadores/cruces.py](../../../../validadores/cruces.py).

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la regla en `base/`, con su checklist. El capítulo lo decide el estándar: `01 · Conducta` o `02 · Flujo de trabajo`.
- [ ] Resolver el choque con `02·F20` —parar y proponer— cuando el defecto es del estándar y no del proyecto. Está anotado en el punto 8 del [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- [ ] Plantilla del pendiente del lado del estándar: proyecto de origen, pendiente de seguimiento, a quién avisar al cerrar.
- [ ] Plantilla del pendiente del lado del proyecto: dónde está el defecto, qué se reportó allá, qué se espera, cuándo cierra.
- [ ] La pieza que escribe el aviso de vuelta al cerrar.
- [ ] Comprobación de trazabilidad en `cruces.py`.
- [ ] Versionar el cambio (`20·M10`).

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| [`A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta`](A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/) | CA-01 a CA-04 | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/plan_trabajo.md](A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/plan_trabajo.md) | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/plan_pruebas.md](A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/plan_pruebas.md) | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/resultado_pruebas.md](A-EP-007-HU-008-la-regla-y-el-aviso-de-vuelta/resultado_pruebas.md) · **Cumple** | Cerrada |

**De dónde sale esta historia:** el [pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md](../../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md), reportado por `shopnest-mesa`.

**Deuda que esta historia cobra.** Tres cierres anteriores quedaron con el aviso sin mandar: el [pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md](../../../../pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md), el [pendientes/hecho/renombrar-deja-el-resumen-coherente.md](../../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md) y el [pendientes/hecho/poner-al-dia-lo-ya-instalado.md](../../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md) — este último sí avisó. Son la prueba de que el paso 6 hecho a mano se olvida.

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
| Dependencia | [HU-006](../HU-006-poner-al-dia/HU-006-poner-al-dia.md), porque el aviso viaja por el mismo canal que pone al día lo instalado | Medio |
| Riesgo | Que la pieza escriba en el repositorio de un proyecto sin que nadie lo haya autorizado | Escribe un archivo de pendiente, nunca toca código; y el proyecto tiene que estar en la lista |
| Riesgo | Que el procedimiento quede escrito y nadie lo siga, como los siete casos de `ID9` | Por eso el CA-02 y el CA-03 son comprobaciones, no recordatorios |
| Riesgo | Que el choque con `02·F20` deje al agente sin saber si parar o reportar | Se resuelve dentro de esta historia, no después |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas
- [x] Decidido en qué capítulo va la regla — el `02`, por la fila 4 del checklist

## 11. Definition of Done (DoD)

- [x] La regla escrita en `base/` con su checklist — [`02·F24`](../../../../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md), en CUMPLE
- [x] Las dos plantillas del pendiente, una por lado, cada una nombrando a la otra
- [x] Los cuatro criterios de aceptación verificados
- [x] El aviso de vuelta funcionando, comprobado sobre proyectos de mentira — **no sobre uno real**: escribe en repositorios ajenos y eso se prueba en carpetas desechables (`00·N4`)
- [x] Versionada (`20·M10`) — 23.7.0
- [x] El pendiente 36 cerrado nombrando la fase
- [x] Avisado al cerrar el 36 — llegó a `shopnest-mesa`, el único de los nueve con carpeta `pendientes/`. Que los otros ocho no tengan dónde recibirlo es el [61](../../../../pendientes/hecho/el-aviso-de-vuelta-llega-a-uno-de-nueve.md)

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | El procedimiento ya está dictado; falta escribirlo y construir el aviso |
| **N**egociable | Parcial | Los siete pasos los dictó el usuario; lo negociable es dónde vive la regla |
| **V**aliosa | Sí | Sin esto, cada reporte deja un pendiente abierto para siempre en el proyecto |
| **E**stimable | Sí | Una regla, dos plantillas, una pieza y una comprobación |
| **S**mall (pequeña) | Parcial | Son cuatro entregables; se parten en fases |
| **T**esteable | Sí | Se prueba cerrando un pendiente de prueba y mirando si el aviso llegó |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, para que el pendiente 36 deje de estar suelto |
