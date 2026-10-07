# HU-010 · La base se copia sola en una carpeta hermana de `agente`

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-010 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/historia/` y el enganche de inicio de sesión |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra Cimiento
- **Quiero** que la base se copie sola cada día y se guarden las últimas siete copias
- **Para** no perder la historia si la base se daña

---

## 3. Contexto y descripción

Si toda la historia vive en la base, perderla es perder todo. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 23, 24 y 25, punto 16 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La copia va en la carpeta `cimiento-copias`, hermana de la carpeta del estándar: `C:\Ing. Jose\ia\cimiento-copias` en esta máquina (acuerdos 23 y 24) |
| RN-02 | Se hace una vez al día, sola, sin que nadie tenga que acordarse (acuerdo 24) |
| RN-03 | Se guardan las últimas 7; las más viejas se quitan (acuerdo 25) |
| RN-04 | Va sin claves: las sesiones del navegador no se copian (`00·N6`) |
| RN-05 | Se puede comprobar que una copia se restaura, en una base aparte |

### 3.2 Supuestos

- El usuario de la base puede crear una base aparte para la prueba de restauración.

### 3.3 Fuera de alcance

- Copias fuera de esta máquina.

---

## 4. Criterios de aceptación

### CA-01 · La copia del día se hace sola

**Sale de:** análisis 1 del pendiente 132, punto 16 de «Lo que se tiene que hacer»

```gherkin
Dado que hoy todavía no hay copia
Cuando abre una sesión de Claude Code
Entonces se escribe en segundo plano cimiento-AAAA-MM-DD.sql en la carpeta de copias
Y si ya hay copia de hoy no se hace otra
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: los casos de la copia pasan.

### CA-02 · Se guardan las últimas 7

**Sale de:** análisis 1 del pendiente 132, acuerdo 25

```gherkin
Dado que hay 8 copias en la carpeta
Cuando se hace la copia de hoy
Entonces quedan las 7 más nuevas
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: el caso pasa.

### CA-03 · La copia va sin claves y se restaura

**Sale de:** `00·N6` y el punto 16 de «Lo que se tiene que hacer»

```gherkin
Dada una copia
Cuando se corre manage.py probar_copia sobre ella
Entonces se carga en una base aparte, se cuentan sus tablas y se borra la base aparte
Y la copia no trae filas de las sesiones del navegador
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Abrir una sesión no espera a la copia: corre en segundo plano |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Copiar, guardar 7 y probar la restauración, sin Django.
- [ ] El inicio de sesión lanza la copia del día.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-010-la-copia-diaria` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-010-la-copia-diaria/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-010-la-copia-diaria/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-010-la-copia-diaria/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la copia falle sin que nadie lo note | El inicio de sesión avisa si la última copia falló |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | La historia no se pierde |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
