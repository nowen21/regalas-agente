# HU-011 — Dónde termina el estándar y dónde empieza el adaptador

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-011 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos — enganches e instalador |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien mantiene el estándar
- **Quiero** saber qué piezas sirven con cualquier agente y cuáles están amarradas a la herramienta de hoy
- **Para** que el día que la herramienta cambie se sepa exactamente qué hay que rehacer, y no se caiga todo lo demás

---

## 3. Contexto y descripción

Las reglas de [base/](../../../../base/) son texto y sirven en cualquier parte. **Lo que las hace cumplir, no.**

- Cinco validadores son enganches de Claude Code: [validadores/hook_md.py](../../../../validadores/hook_md.py), [validadores/hook_checklist.py](../../../../validadores/hook_checklist.py), [validadores/hook_sesion.py](../../../../validadores/hook_sesion.py), [validadores/hook_recuerdos.py](../../../../validadores/hook_recuerdos.py) y [validadores/hook_historico.py](../../../../validadores/hook_historico.py).
- [validadores/instalar.py](../../../../validadores/instalar.py) escribe esos enganches en `.claude/settings.json`.
- [validadores/cargador.py](../../../../validadores/cargador.py) arma el texto que se le entrega al agente en el formato que espera esa herramienta, y el archivo de entrada se llama `CLAUDE.md`.
- La carpeta [skills/](../../../../skills/) es un formato de esa herramienta.
- El histórico de sesiones y la memoria del agente se llenan porque un enganche de esa herramienta los dispara.

Si mañana el usuario trabaja con otro agente, lo que sobrevive son las reglas escritas. Se pierde todo lo que las hace cumplir solas — que es justo lo que este repositorio lleva meses construyendo. **Y el estándar no se daría cuenta:** hoy no hay ningún archivo que diga cuáles piezas están amarradas y cuáles no.

Hay una ironía que vale nombrar. El estándar le exige esto mismo a los proyectos que lo heredan: [base/10-dependencias.md](../../../../base/10-dependencias.md) manda cuidar de qué se depende, y [base/11-configuracion-entornos.md](../../../../base/11-configuracion-entornos.md) manda separar lo de cada máquina de lo que va en el repositorio. El estándar no se lo aplica a sí mismo.

**El mapa vale por sí solo.** Es de leer una vez y se puede hacer hoy; abstraer el adaptador es otra cosa, y se hace cuando exista el segundo caso — antes, se abstraería contra una sola herramienta, que es adivinar.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Existe un mapa que clasifica cada pieza del repositorio en una de tres columnas: sirve con cualquier agente, es adaptador de la herramienta, o es de la máquina |
| RN-02 | Toda pieza del repositorio aparece en el mapa; ninguna queda sin columna |
| RN-03 | Una pieza nueva que sea adaptador se anota en el mapa al nacer, no después |
| RN-04 | El mapa dice, por cada pieza amarrada, qué se pierde si la herramienta desaparece |

### 3.2 Supuestos

- Hoy hay una sola herramienta. El mapa se escribe sabiendo eso, y no pretende ser el diseño de la portabilidad.

### 3.3 Fuera de alcance

- Abstraer el adaptador o construir un segundo. Se hace cuando exista el segundo caso real.
- Cambiar el nombre del archivo de entrada o el formato de `skills/`. El mapa los nombra; no los mueve.

---

## 4. Criterios de aceptación

### CA-01 — Toda pieza tiene su columna

```gherkin
Dado que el repositorio tiene sus carpetas y sus programas
Cuando se recorre el mapa
Entonces cada pieza aparece en una de las tres columnas
Y ninguna aparece en dos
```

**Cómo validarlo:**

1. Listar las carpetas de primer nivel del repositorio y los programas de [validadores/](../../../../validadores/).
2. Buscar cada uno en el mapa.
3. Contar los que no aparecen, y los que aparecen dos veces. Resultado esperado: cero y cero.
- **Aprobado cuando:** los dos conteos dan cero.

### CA-02 — Cada pieza amarrada dice qué se pierde

```gherkin
Dado que una pieza está clasificada como adaptador de la herramienta
Cuando se lee su fila
Entonces dice qué deja de funcionar si la herramienta desaparece
```

**Cómo validarlo:**

1. Abrir el mapa y filtrar la columna de adaptador.
2. Recorrer sus filas. Resultado esperado: cada una trae, escrito, qué se pierde.
3. Buscar una fila de adaptador sin ese texto. Resultado esperado: no existe.
- **Aprobado cuando:** ninguna fila de adaptador está sin su consecuencia escrita.

### CA-03 — El mapa se queda viejo y se nota

```gherkin
Dado que se agrega un programa nuevo al repositorio
Cuando ese programa no aparece en el mapa
Entonces la comprobación lo reporta
```

**Cómo validarlo:**

1. Agregar un archivo de prueba en [validadores/](../../../../validadores/).
2. Correr la comprobación del mapa. Resultado esperado: reporta que esa pieza no está clasificada.
3. Clasificarla y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** la pieza sin clasificar se reporta. Sin esto el mapa envejece en silencio, que es lo que le pasa a todo mapa escrito a mano.

### Criterios de aceptación transversales

- [ ] **Límites** — una pieza que es mitad y mitad, y una carpeta vacía, tienen comportamiento definido.
- [ ] **No regresión** — el mapa no cambia el comportamiento de ninguna pieza; solo las describe.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | Cada fila del mapa cita la ruta real de la pieza, comprobable contra el disco |
| RNF-02 | **Determinismo** | El mismo repositorio da el mismo mapa |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es una tabla.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md).
- **Dónde vive el mapa:** `anatomia/`, que es donde el repositorio guarda su mapa del sitio.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el mapa en `anatomia/`, con sus tres columnas.
- [ ] Clasificar cada carpeta de primer nivel y cada programa de `validadores/`.
- [ ] Escribir, por cada pieza amarrada, qué se pierde si la herramienta desaparece.
- [ ] Comprobación que reporta la pieza sin clasificar.
- [ ] Agregar la fila de `anatomia/` a la tabla del §3 del [CLAUDE.md](../../../../CLAUDE.md) — es un hueco anotado en el punto 8 del [pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md](../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| — | — | — | — | — | Sin empezar |

**De dónde sale esta historia:** el [pendientes/15-el-estandar-depende-de-una-sola-herramienta.md](../../../../pendientes/15-el-estandar-depende-de-una-sola-herramienta.md). Su punto 1 —el mapa— es esta historia; sus puntos 2 y 3 esperan al segundo caso.

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
| Dependencia | Ninguna. El mapa se escribe leyendo lo que ya existe | — |
| Riesgo | Que el mapa se escriba una vez y envejezca sin que nadie lo note | El CA-03 lo convierte en algo que se rompe cuando queda viejo |
| Riesgo | Que clasificar se convierta en rediseñar | El alcance es describir, y está escrito en §3.3 |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] El mapa escrito en `anatomia/`, con sus tres columnas
- [ ] Los tres criterios de aceptación verificados
- [ ] La fila de `anatomia/` en el `CLAUDE.md` §3
- [ ] Versionada (`20·M10`)
- [ ] El pendiente 15 cerrado en su punto 1, nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Se hace leyendo lo que ya está |
| **N**egociable | Sí | Las tres columnas se pueden discutir |
| **V**aliosa | Sí | Hoy no hay forma de saber qué se pierde si cambia la herramienta |
| **E**stimable | Sí | El alcance lo fija el árbol del repositorio |
| **S**mall (pequeña) | Sí | Es de una tarde, como dice el propio pendiente |
| **T**esteable | Sí | Se cuentan las piezas sin columna |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, para que el pendiente 15 deje de estar suelto |
