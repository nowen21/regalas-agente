# HU-014 — El consumo de la sesión se ve mientras se puede actuar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-014 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos — enganches |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien paga lo que la sesión consume
- **Quiero** enterarme de cuánto lleva gastado mientras la sesión sigue
- **Para** decidir si cierro, compacto o sigo, antes de que el total sea una sorpresa

---

## 3. Contexto y descripción

El aviso de consumo existe desde la 27.0.0: [adaptadores/claude-code/hook_presupuesto.py](../../../../adaptadores/claude-code/hook_presupuesto.py) lee la transcripción de la herramienta, y [validadores/presupuesto.py](../../../../validadores/presupuesto.py) suma y compara contra un umbral. Corre cuando la respuesta termina. Ese es el problema: el total llega cuando ya se pagó.

**Nació sin historia.** Se construyó por orden directa, sin cadena, y quedó escrito así en el resumen del 2026-08-19. Esta historia le da dueño a lo que ya existe (`CA-01`) y agrega lo que falta (`CA-02`, `CA-03`).

**La medida que fija el tramo.** El 2026-08-20 se midieron las ocho sesiones más recientes de este repositorio con el propio enganche:

| Sesión | Turnos | Entrada | Salida | Total sin caché |
|---|---:|---:|---:|---:|
| 1 | 46 | 143.802 | 354 | 144.156 |
| 2 | 65 | 492.632 | 97.819 | 590.451 |
| 3 | 78 | 974.781 | 38.339 | 1.013.120 |
| 4 | 48 | 1.167.905 | 33.898 | 1.201.803 |
| 5 | 248 | 1.629.107 | 485.945 | 2.115.052 |
| 6 | 226 | 2.128.278 | 224.527 | 2.352.805 |
| 7 | 769 | 2.873.594 | 942.716 | 3.816.310 |
| 8 | 3.407 | 9.549.928 | 3.143.722 | 12.693.650 |

Un tramo de **un millón** avisa entre cero y doce veces por sesión, según su tamaño, y ninguna sesión corta lo cruza. Un tramo más chico avisaría en todas y se dejaría de leer.

Sale del [pendientes/hecho/el-consumo-se-ve-a-tiempo.md](../../../../pendientes/hecho/el-consumo-se-ve-a-tiempo.md).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El enganche mide, no detiene: sale siempre con código 0 |
| RN-02 | Al terminar cada respuesta se reporta el total de la sesión: turnos, fichas de entrada, de salida y leídas de caché |
| RN-03 | En cada mensaje del usuario se mira si el último turno cruzó un tramo; si lo cruzó, se avisa una vez, diciendo cuánto va y qué tramo se pasó |
| RN-04 | El tramo por defecto es 1.000.000 de fichas de entrada más salida, sin contar la caché; se cambia con un argumento |
| RN-05 | No hay estado compartido: el cruce se decide comparando el total con y sin el último turno |
| RN-06 | La suma y el cruce son agnósticos y viven en `validadores/`; leer el formato de la transcripción vive en el adaptador |
| RN-07 | Sin transcripción, o con una ilegible, calla |

### 3.2 Supuestos

- La transcripción de la herramienta llega al enganche del mensaje del usuario igual que al de cierre. En las pruebas se le pasa por la entrada estándar.

### 3.3 Fuera de alcance

- Cortar la sesión al pasar un tope. El corte lo pone la herramienta.
- Convertir fichas a dinero: el precio cambia por modelo y por fecha, y el enganche no lo conoce.

---

## 4. Criterios de aceptación

### CA-01 — Al terminar se reporta el consumo de la sesión

```gherkin
Dado que una sesión tiene transcripción con turnos del agente
Cuando termina una respuesta
Entonces se imprime el total: turnos, entrada, salida y caché
```

**Cómo validarlo:**

1. Correr el enganche sin modo (o con `--modo cierre`) pasándole una transcripción de prueba con dos turnos.
2. Resultado esperado: una línea con "Consumo de la sesión", 2 turnos y las tres cifras.
- **Aprobado cuando:** la línea sale con los cuatro números correctos. Es lo que ya hace la 27.0.0; el caso lo fija.

### CA-02 — Al cruzar un tramo se avisa una vez

```gherkin
Dado que la sesión llevaba 950.000 fichas sin caché
Cuando el último turno la lleva a 1.050.000
Entonces el mensaje siguiente trae un aviso que dice que se cruzó el primer millón y cuánto va
```

**Cómo validarlo:**

1. Armar una transcripción de prueba cuyos turnos sumen 950.000 y agregarle uno de 100.000.
2. Correr el enganche con `--modo aviso`. Resultado esperado: un aviso que nombra el tramo 1 y el total.
3. Agregar un turno de 10.000 (queda en 1.060.000) y volver a correr. Resultado esperado: silencio.
4. Agregar turnos hasta pasar los 2.000.000 y correr. Resultado esperado: aviso del tramo 2.
- **Aprobado cuando:** avisa en el mensaje que sigue al cruce, una vez por tramo, y calla entre cruces.

### CA-03 — Sin transcripción calla, y nunca detiene

```gherkin
Dado que el enganche corre en cada mensaje
Cuando no recibe ruta de transcripción, o la ruta no existe, o el archivo trae líneas ilegibles
Entonces no imprime aviso por eso y sale con código 0
```

**Cómo validarlo:**

1. Correr `--modo aviso` sin `transcript_path`. Resultado esperado: sin salida, código 0.
2. Correr con una ruta inexistente. Resultado esperado: igual.
3. Correr con un archivo que mezcla líneas válidas e ilegibles. Resultado esperado: suma las válidas; código 0.
- **Aprobado cuando:** los tres casos salen con 0 y sin aviso falso.

### Criterios de aceptación transversales

- [x] **Límites** — un total exactamente igual al tramo cuenta como cruzado; un umbral de 0 apaga el aviso.
- [x] **No regresión** — el reporte de cierre de la 27.0.0 no cambia su texto ni su momento.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Silencio** | Un aviso por tramo y ninguno entre tramos |
| RNF-02 | **Rendimiento** | Leer la transcripción en cada mensaje no se nota: es un archivo local, leído una vez por turno |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** N/A.
- **Documento funcional:** la especificación del módulo, [documentacion/automatismos/spec.md](../../../automatismos/spec.md), y `notas/estructura.md` §3.2, de donde salió la brecha.
- **Contrato de API:** N/A.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] El cruce de tramo en `validadores/presupuesto.py`.
- [ ] El modo `aviso` en el enganche del adaptador, sin cambiar el comando del modo de cierre ya instalado.
- [ ] Alta del evento de mensaje en la lista de enganches del instalador.
- [ ] Casos de prueba, incluido el que fija el comportamiento de cierre ya construido.
- [ ] Registro en la especificación del módulo y en el mapa del sitio.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| [A-EP-005-HU-014-el-aviso-por-tramo](A-EP-005-HU-014-el-aviso-por-tramo/README.md) | CA-01, CA-02 y CA-03 | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/A-EP-005-HU-014-el-aviso-por-tramo/plan_trabajo.md](A-EP-005-HU-014-el-aviso-por-tramo/plan_trabajo.md) | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/A-EP-005-HU-014-el-aviso-por-tramo/plan_pruebas.md](A-EP-005-HU-014-el-aviso-por-tramo/plan_pruebas.md) | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/A-EP-005-HU-014-el-aviso-por-tramo/resultado_pruebas.md](A-EP-005-HU-014-el-aviso-por-tramo/resultado_pruebas.md) | Cerrada el 2026-08-20: Cumple, 8 de 8 casos |

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
| Dependencia | La transcripción de la herramienta, que es lo que se suma. Es del adaptador, no del estándar | Medio |
| Riesgo | Que el tramo quede mal calibrado y avise de más o de menos | Salió de ocho sesiones reales; se cambia con un argumento sin tocar código |
| Riesgo | Que dos enganches del mismo mensaje corran a la vez y el orden no esté garantizado | Este no escribe nada: el orden le da igual |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas

## 11. Definition of Done (DoD)

- [x] Los tres criterios de aceptación verificados
- [x] El enganche del mensaje instalado en los proyectos del registro
- [x] Especificación del módulo y mapa del sitio al día
- [x] Versionada (`20·M10`): 27.1.0
- [x] El pendiente 65 cerrado nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Se apoya en lo que la 27.0.0 ya dejó |
| **N**egociable | Sí | El tamaño del tramo |
| **V**aliosa | Sí | Es la diferencia entre un número y un aviso útil |
| **E**stimable | Sí | Dos funciones, un modo, sus casos |
| **S**mall (pequeña) | Sí | Tres comportamientos |
| **T**esteable | Sí | Transcripciones de prueba con sumas conocidas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el pendiente 65, que sale del H-1 de la sesión del día. Le da dueño al enganche de la 27.0.0 |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Fase A ejecutada y cerrada: el tramo en `presupuesto.py`, el modo `aviso` en el enganche, instalado en los 9 proyectos. 27.1.0 |
