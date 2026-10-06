# HU-024 · El aviso del freno dice cómo salir sin tocar archivos


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-024 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/enganches/freno.py`, `adaptadores/claude-code/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja con el agente
- **Quiero** que el freno, al detener algo, diga la salida prevista
- **Para** no terminar tocando archivos ni código a mano

---

## 3. Contexto y descripción

El freno bloqueaba con razón, pero no decía cómo salir, y el usuario terminó editando archivos a mano. Además, al leer el análisis prendido, el freno miraba el archivo de estado único y no el de su sesión, así que dejaba pasar lo que mandaba otro análisis y detenía lo que mandaba el propio; y resolvía las rutas de un comando de Bash sin tener en cuenta su `cd` ([análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 1, puntos 9 y 11; H-8 del [resumen del 2026-10-04, sesión 3](../../../../historico-chat/resumenes/2026-10-04/sesion-3.md)).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Cuando el freno detiene, su aviso dice las dos salidas: la herramienta que deshace lo creado (`andamio quitar`, `cerrar.py reabrir`, `reabrir_fase`, `instalar.py --desinstalar`), o pedirle al usuario la suspensión de la regla en Cimiento, con la dirección de la pantalla del proyecto | Acuerdo 1, punto 9 |
| RN-02 | Si la regla es del núcleo, el aviso dice que no se suspende y que se resuelve en la conversación | Acuerdo 5 |
| RN-03 | El freno lee el análisis prendido de su propia sesión, y deja escribir toda ruta que ese análisis manda hacer «de una y sin fase», también un archivo nuevo | Punto 11 |
| RN-04 | En un comando de Bash, cada parte resuelve sus rutas desde la carpeta en que la dejó el `cd` anterior | Punto 11 |

### 3.2 Supuestos

- La HU-013 dejó las suspensiones en Cimiento.

### 3.3 Fuera de alcance

- Suspender desde el aviso mismo: lo decide el usuario en Cimiento.

---

## 4. Criterios de aceptación

### CA-01 · El aviso dice la salida

**Sale de:** análisis 3 del pendiente 119, punto 9.

```gherkin
Dado una acción que el freno detiene por 02·F8
Cuando el agente recibe el aviso
Entonces el aviso nombra las herramientas que deshacen y la suspensión en Cimiento, con su dirección
Y si la regla es del núcleo, dice que no se suspende
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_freno_salida` desde `proyectos/cimiento/` → pasan los casos del aviso.

**Aprobado cuando:** el aviso trae las dos salidas, o la del núcleo.

### CA-02 · El análisis de la propia sesión

**Sale de:** análisis 3 del pendiente 119, punto 11.

```gherkin
Dado dos sesiones con análisis prendidos distintos
Cuando el freno revisa una escritura de una de ellas
Entonces mira las filas «de una y sin fase» del análisis de esa sesión
Y deja crear un archivo nuevo que ese análisis nombra
Y no deja escribir el que solo nombra el análisis de la otra sesión
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_freno_salida` → pasan los casos del análisis.

**Aprobado cuando:** cada sesión ve su análisis.

### CA-03 · El `cd` de un comando

**Sale de:** análisis 3 del pendiente 119, punto 11.

```gherkin
Dado un comando «cd carpeta && rm archivo»
Cuando el freno lo revisa
Entonces resuelve archivo dentro de carpeta, no en la carpeta de la sesión
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_freno_salida` → pasan los casos del `cd`.

**Aprobado cuando:** la ruta resuelta es la de después del `cd`.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Buscar la transcripción de la sesión lee solo el comienzo de cada archivo |

---

## 6. Diseño y referencias

Documento funcional: [análisis 3 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdo 1.

---

## 7. Tareas técnicas derivadas

- [x] El aviso con la salida.
- [x] El análisis de la propia sesión.
- [x] El `cd` de un comando.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-024-la-salida-del-freno` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-024-la-salida-del-freno/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-024-la-salida-del-freno/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-024-la-salida-del-freno/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-013 (suspensiones), HU-020 (quitar) | Alto |
| Riesgo | Que el freno deje pasar de más | Las pruebas del freno completas siguen en verde |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 3 del pendiente 119 |
