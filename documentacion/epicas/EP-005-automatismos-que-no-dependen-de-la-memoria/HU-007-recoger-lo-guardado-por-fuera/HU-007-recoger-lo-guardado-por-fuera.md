# HU-007 — Recoger al abrir sesión lo que quedó guardado por fuera del repositorio

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — los dos CA y los dos transversales verificados el 2026-08-17 |
---

## 2. Narrativa

- **Como** quien trabaja en varias máquinas
- **Quiero** que lo que la herramienta guardó en su propia carpeta se mueva al repositorio
- **Para** que no quede conocimiento en un rincón que nadie revisa y que no viaja

---

## 3. Contexto y descripción

La herramienta con la que se conversa guarda algunas cosas en una carpeta suya, fuera del proyecto. Lo que queda ahí no se ve en el historial, no se puede revisar y se pierde al cambiar de máquina.

Pedirle a la IA que no lo haga no funciona: dónde guarda su memoria lo decide la herramienta, no el que escribe las reglas. Lo que sí funciona es recogerlo: al abrir la sesión, y también en el momento en que se escribe.

Se mueve, no se copia. Dos versiones del mismo recuerdo terminan diciendo cosas distintas, y la que manda es la que nadie puede leer.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo que quedó en la carpeta de la herramienta se mueve al repositorio |
| RN-02 | Se mueve, no se copia: no quedan dos versiones |
| RN-03 | Un archivo idéntico al que ya está se descarta |
| RN-04 | Un archivo con el nombre ocupado entra con otro nombre y se avisa: nada se pisa |
| RN-05 | Corre al abrir la sesión y también al escribir, para que no pase la sesión entera en el lugar equivocado |

### 3.2 Supuestos

- La carpeta de la herramienta es conocida y se puede leer desde la máquina donde se trabaja.

### 3.3 Fuera de alcance

- Decidir qué merece guardarse. Eso es EP-006.
- Cambiar dónde guarda la herramienta sus cosas.

---

## 4. Criterios de aceptación

### CA-01 — Lo guardado por fuera se recoge al abrir sesión

```gherkin
Dado que quedó un archivo en la carpeta de la herramienta
Cuando se abre una sesión
Entonces ese archivo queda en el repositorio
Y la carpeta de la herramienta queda vacía
```

**Cómo validarlo:**

1. Dejar a mano un archivo en la carpeta de la herramienta.
2. Abrir una sesión. Resultado esperado: el archivo aparece en el repositorio.
3. Mirar la carpeta de la herramienta. Resultado esperado: quedó vacía.
- **Aprobado cuando:** no queda nada guardado por fuera.

### CA-02 — Nada se pisa

```gherkin
Dado que llega un archivo con un nombre que ya existe en el repositorio
Cuando se recoge
Entonces entra con otro nombre y se avisa
```

**Cómo validarlo:**

1. Dejar en la carpeta de la herramienta un archivo con el nombre de uno que ya está en el repositorio, con contenido distinto.
2. Abrir sesión. Resultado esperado: entra con otro nombre y aparece el aviso.
3. Repetir con contenido idéntico. Resultado esperado: se descarta, sin duplicar.
- **Aprobado cuando:** cuál versión manda lo decide la persona, no el automatismo.

### Criterios de aceptación transversales

- [ ] **Límites** — nombres que solo difieren en mayúsculas se tratan como el mismo archivo.
- [ ] **Errores** — si la carpeta de la herramienta no se puede leer, se avisa y la sesión sigue.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Seguridad de datos** | Nada se pisa ni se pierde al mover |
| **Oportunidad** | Corre al abrir y al escribir, no solo al final |
| **Compatibilidad** | Funciona donde los nombres de archivo no distinguen mayúsculas |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Ubicar la carpeta de la herramienta.
- [ ] Mover lo que haya al repositorio, sin pisar.
- [ ] Descartar los duplicados idénticos y avisar de los conflictos.
- [ ] Correr al abrir la sesión y al escribir.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera](A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-005-HU-007-retrodocumentar-el-recogido-de-lo-guardado-por-fuera/resultado_pruebas.md#6-veredicto-de-la-fase) — los dos CA y los dos transversales verificados. Pendiente el commit |

**La fase retro-documenta.** El enganche recoge del almacén local lo que debe vivir en el repositorio. La mitad delicada es el CA-02: recoger sin pisar, que es lo que separa recoger de destruir, y hoy nadie lo comprueba.

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
| Dependencia | EP-006, porque el destino de lo recogido lo define esa épica | Alto |
| Riesgo | Que al mover se pise algo escrito antes | Nada se pisa: entra con otro nombre y se avisa |
| Riesgo | Que la herramienta cambie dónde guarda | La ubicación se declara en un solo lugar |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Lo guardado por fuera se recoge al abrir sesión y al escribir
- [ ] Nada se pisa ni se duplica
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita saber a dónde va lo recogido |
| **N**egociable | Sí | Cuándo corre se puede discutir |
| **V**aliosa | Sí | Evita que quede conocimiento en un rincón que no viaja |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Mover archivos con cuidado |
| **T**esteable | Sí | Se prueba dejando archivos a mano en la carpeta de la herramienta |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Los dos CA verificados: se recoge, el almacén queda sin texto ni puntero, y nunca se borra. Queda escrito en la especificación por qué nunca borra, con la historia de la memoria que se perdió |
