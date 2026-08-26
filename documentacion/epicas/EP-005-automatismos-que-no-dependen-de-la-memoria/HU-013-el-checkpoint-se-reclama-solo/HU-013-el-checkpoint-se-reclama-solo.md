# HU-013 — El checkpoint de la fase se reclama solo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-013 |
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

- **Como** quien retoma una fase en una sesión nueva
- **Quiero** que el estado de la fase se reclame en el momento en que una puerta pasa sin él
- **Para** leer en qué estación va sin releer la conversación, y sin creerle a un estado viejo

---

## 3. Contexto y descripción

El `estado-fase.md` es el checkpoint de la fase: la plantilla [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) lo define como lo que "se escribe en cada puerta para sobrevivir a la compactación". Hoy lo escribe el agente cuando se acuerda. [validadores/fases.py](../../../../validadores/fases.py) lo compara con el resultado de pruebas después, cuando alguien corre `validar.py fases`.

Es la situación que esta épica ya resolvió dos veces, con la transcripción y con el resumen: lo que depende de que alguien se acuerde, no pasa. Lo que un programa no puede hacer es decir en qué estación va la fase, porque eso es criterio. Lo que sí puede es que el hueco se vea en el momento.

Sale del [pendientes/hecho/el-checkpoint-se-reclama-solo.md](../../../../pendientes/hecho/el-checkpoint-se-reclama-solo.md).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Los documentos que marcan una puerta son tres: `plan_trabajo.md`, `resultado_pruebas.md` y `funcionalidad_implementada.md`. Escribir cualquier otro archivo no dispara nada |
| RN-02 | Al escribir uno de esos tres dentro de una fase, el enganche mira el `estado-fase.md` de esa fase: si falta, o si su última escritura es anterior a la del documento, avisa |
| RN-03 | El aviso nombra la fase y el documento que avanzó sin checkpoint. Un aviso genérico obliga a buscar |
| RN-04 | El enganche no escribe ni modifica el `estado-fase.md`: decir en qué estación va es criterio |
| RN-05 | No detiene el trabajo: sale siempre con código 0 |
| RN-06 | La lógica es agnóstica y vive en `validadores/`; lo que lee el formato de la herramienta vive en el adaptador |
| RN-07 | Llega a cada proyecto por el instalador, como los demás enganches |

### 3.2 Supuestos

- La fecha de última escritura del archivo (la que guarda el sistema de archivos) alcanza para saber cuál de los dos se escribió después. No hace falta leer el contenido.
- Una fase se reconoce por el nombre de su carpeta, con el patrón que ya usa `fases.py` (`02·F12.6`).

### 3.3 Fuera de alcance

- Comprobar que el estado escrito sea cierto: eso es de `fases.py` (veredicto) y de quien lee.
- Avisar cuando se escribe el `plan_pruebas.md` o el `README.md` de la fase: no marcan puerta.

---

## 4. Criterios de aceptación

### CA-01 — Una puerta pasa sin checkpoint y se avisa

```gherkin
Dado que una fase tiene su carpeta con el nombre del estándar y no tiene estado-fase.md
Cuando se escribe su resultado_pruebas.md
Entonces aparece un aviso que nombra la fase y dice que el checkpoint falta
```

**Cómo validarlo:**

1. Crear una carpeta de fase de prueba (por ejemplo `A-EP-001-HU-001-prueba/`) con un `resultado_pruebas.md` y sin `estado-fase.md`.
2. Correr el enganche con la ruta de ese `resultado_pruebas.md` como archivo escrito. Resultado esperado: imprime un aviso con el nombre de la fase y la palabra "falta".
3. Mirar el código de salida. Resultado esperado: 0.
- **Aprobado cuando:** el aviso sale, nombra la fase, y la sesión no se detiene.

### CA-02 — El checkpoint existe pero quedó atrás

```gherkin
Dado que una fase tiene estado-fase.md
Cuando se escribe su funcionalidad_implementada.md después del estado-fase.md
Entonces el aviso nombra la fase y el documento que avanzó sin checkpoint
Y si después se escribe el estado-fase.md y se vuelve a escribir el documento, no hay aviso
```

**Cómo validarlo:**

1. En la fase de prueba, escribir `estado-fase.md` y después `funcionalidad_implementada.md`.
2. Correr el enganche con la ruta del segundo. Resultado esperado: aviso con el nombre de la fase y `funcionalidad_implementada.md`.
3. Volver a escribir `estado-fase.md` (queda más reciente) y correr el enganche con la misma ruta. Resultado esperado: silencio.
- **Aprobado cuando:** avisa mientras el checkpoint está atrás y calla cuando se puso al día.

### CA-03 — Lo que no es puerta calla, y el enganche no toca el checkpoint

```gherkin
Dado que el enganche corre al escribir cualquier archivo
Cuando el archivo es el propio estado-fase.md, el plan_pruebas.md, el README.md de la fase, o un archivo fuera de una fase
Entonces no imprime nada
Y el estado-fase.md no cambia por correr el enganche
```

**Cómo validarlo:**

1. Correr el enganche con la ruta de `estado-fase.md`, de `plan_pruebas.md`, de `README.md` de la fase y de un `.md` fuera de `documentacion/epicas/`. Resultado esperado: sin salida, código 0, en los cuatro.
2. Guardar la huella del `estado-fase.md` antes y después de correr el enganche con un `resultado_pruebas.md` atrasado. Resultado esperado: la misma huella.
- **Aprobado cuando:** los cuatro callan y el checkpoint queda intacto.

### Criterios de aceptación transversales

- [x] **Límites** — el archivo que ya no existe cuando el enganche llega no lo revienta; la entrada sin JSON válido tampoco.
- [x] **Errores** — si algo falla al leer, imprime el motivo y sale con 0.
- [x] **No regresión** — las suites que ya corrían siguen en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | No demora la escritura: mira dos fechas del sistema de archivos, no lee el contenido |
| RNF-02 | **Claridad** | El aviso dice qué falta y dónde, con la ruta relativa al proyecto |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** N/A.
- **Documento funcional:** la especificación del módulo, [documentacion/automatismos/spec.md](../../../automatismos/spec.md).
- **Contrato de API:** N/A.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Módulo agnóstico que reconoce la fase y compara las fechas.
- [ ] Enganche del adaptador que lee la ruta escrita y llama al módulo.
- [ ] Alta en la lista de enganches del instalador.
- [ ] Casos de prueba.
- [ ] Registro en la especificación del módulo, el mapa del sitio y el mapa del amarre.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| [A-EP-005-HU-013-el-enganche-del-checkpoint](A-EP-005-HU-013-el-enganche-del-checkpoint/README.md) | CA-01, CA-02 y CA-03 | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/A-EP-005-HU-013-el-enganche-del-checkpoint/plan_trabajo.md](A-EP-005-HU-013-el-enganche-del-checkpoint/plan_trabajo.md) | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/A-EP-005-HU-013-el-enganche-del-checkpoint/plan_pruebas.md](A-EP-005-HU-013-el-enganche-del-checkpoint/plan_pruebas.md) | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/A-EP-005-HU-013-el-enganche-del-checkpoint/resultado_pruebas.md](A-EP-005-HU-013-el-enganche-del-checkpoint/resultado_pruebas.md) | Cerrada el 2026-08-20: Cumple, 8 de 8 casos |

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
| Dependencia | HU-003 de esta épica: es el mismo momento de disparo, al escribir un archivo | Medio |
| Dependencia | `validadores/fases.py`, que ya sabe reconocer el nombre de una fase | Bajo |
| Riesgo | Que el aviso salte en cada escritura y se vuelva ruido | Solo tres documentos disparan, y solo mientras el checkpoint esté atrás |
| Riesgo | Que el reloj del sistema de archivos no distinga dos escrituras muy seguidas | El caso de prueba separa las escrituras; en uso real el checkpoint se escribe minutos después |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas

## 11. Definition of Done (DoD)

- [x] Los tres criterios de aceptación verificados
- [x] El enganche instalado en los proyectos del registro
- [x] Especificación del módulo, mapa del sitio y mapa del amarre al día
- [x] Versionada (`20·M10`): 27.1.0
- [x] El pendiente 64 cerrado nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No espera a nadie |
| **N**egociable | Sí | Cuáles documentos cuentan como puerta se puede discutir |
| **V**aliosa | Sí | Es lo que hace que el checkpoint exista cuando hace falta |
| **E**stimable | Sí | Un módulo, un enganche, sus casos |
| **S**mall (pequeña) | Sí | Tres comportamientos |
| **T**esteable | Sí | Se prueba con fases de mentira en carpetas temporales |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el pendiente 64, que sale del H-1 de la sesión del día |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Fase A ejecutada y cerrada: nacen `validadores/checkpoint.py` y `hook_checkpoint.py`, instalados en los 9 proyectos. 27.1.0 |
