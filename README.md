# Estándar de Agente para Desarrollo de Software

> Reglas y buenas prácticas que guían a un agente de IA al programar.

Este repositorio es un **estándar reutilizable de buenas prácticas de desarrollo** para agentes de código (Claude Code u otro asistente de programación). Define cómo debe comportarse el agente, cómo debe trabajar, y qué buenas prácticas de ingeniería aplicar siempre. El objetivo es que **cualquier sesión de desarrollo con un agente sea predecible, segura y consistente**, sin que cada conversación reinterprete el proyecto a su manera.

Está empaquetado como **plugin de Claude Code**: se hereda como base común en cualquier proyecto y cada proyecto lo **extiende** con lo suyo, sin tocar el estándar.

## El problema que resuelve

Cuando un agente de IA desarrolla software sin reglas claras, cada sesión:

- Reinventa el diseño y contradice decisiones previas.
- Olvida el contexto del proyecto y toma decisiones funcionales por su cuenta.
- Aplica —o ignora— buenas prácticas de forma inconsistente.
- Puede ejecutar acciones peligrosas (tocar datos reales, publicar cambios, exponer secretos).

Este estándar convierte todo eso en un **contrato explícito y versionado** que el agente lee antes de actuar.

## Las tres capas

El estándar está organizado para que lo universal se **herede** y lo específico de cada proyecto se **agregue encima**, sin mezclarse:

| Capa | Qué contiene | Dónde vive | ¿Se sobrescribe? |
|---|---|---|---|
| **1 · Núcleo blindado** | Seguridad crítica: proteger datos reales, control de versiones bajo demanda, no exponer secretos | `base/00` | **Nunca.** Gana a cualquier regla o instrucción. |
| **2 · Convenciones base** | Buenas prácticas agnósticas al stack (conducta, flujo, datos, seguridad, cumplimiento, UI…) | `base/01`–`base/17` | Solo la capa de proyecto puede ajustarlas. |
| **3 · Capa de proyecto** | Stack, dominio, sector, marco normativo y nombres propios | `plantillas/` (para copiar) → en el repo de cada proyecto | Es la capa que ajusta. |

**Precedencia:** la capa 3 ajusta la capa 2, pero **nunca** la capa 1. Cada archivo de la base lleva su etiqueta de capa (`[CAPA 1]` / `[CAPA 2]`), y cada regla del núcleo la marca `[BLINDADA]`.

## Cómo lo usa un proyecto

1. Instalar/activar este plugin.
2. Crear el `CLAUDE.md` del proyecto que **importe la base** y declare los ajustes de capa 3 (stack, dominio, sector).
3. Copiar y llenar las plantillas de capa 3 (`plantillas/`), p. ej. `marco-normativo.md`.
4. A partir de ahí, el agente arranca cada sesión entendiendo el estándar + lo específico del proyecto.

## La base por capas

**Antes de leer, el [glosario](base/glosario.md):** cada término del estándar explicado en una línea, con qué regla lo manda y dónde vive.

### Preámbulo

- [`00-identidad-y-rol/base.md`](base/00-identidad-y-rol/base.md) — quién es el agente, su rol, misión y principios (el marco del que derivan las reglas)

### Capa 1 · Núcleo blindado — no se sobrescribe

- [`00-nucleo-blindado.md`](base/00-nucleo-blindado.md) — seguridad crítica innegociable

### Capa 2 · Convenciones base — agnósticas, ajustables por el proyecto

- [`01-conducta.md`](base/01-conducta.md) — cómo se comporta el agente
- [`02-flujo-de-trabajo/`](base/02-flujo-de-trabajo/base.md) — especificación → plan → pruebas → docs
- [`03-datos.md`](base/03-datos.md) — diseño de BD, migraciones, catálogos, cero-hardcode
- [`04-seguridad.md`](base/04-seguridad.md) — authz, secretos, validación, inyección, archivos sensibles
- [`05-errores-y-logging.md`](base/05-errores-y-logging.md) — manejo de excepciones y logging
- [`06-rendimiento.md`](base/06-rendimiento.md) — eficiencia, N+1, caché, paginación
- [`07-calidad-de-codigo.md`](base/07-calidad-de-codigo.md) — legibilidad, DRY, complejidad, lint
- [`08-pruebas.md`](base/08-pruebas.md) — estrategia de pruebas
- [`09-git.md`](base/09-git.md) — control de versiones
- [`10-dependencias.md`](base/10-dependencias.md) — librerías de terceros
- [`11-configuracion-entornos.md`](base/11-configuracion-entornos.md) — configuración y entornos
- [`12-privacidad-datos.md`](base/12-privacidad-datos.md) — datos personales y retención
- [`13-documentacion/`](base/13-documentacion/base.md) — persistir trabajo y decisiones
- [`14-estructura-codigo.md`](base/14-estructura-codigo.md) — organización y nomenclatura
- [`15-registros-inmutables.md`](base/15-registros-inmutables.md) — patrón append-only *(opt-in)*
- [`16-cumplimiento-y-calidad.md`](base/16-cumplimiento-y-calidad.md) — leyes, frameworks (COBIT, ISO, OWASP…), cumplimiento por construcción *(opt-in)*
- [`17-interfaz.md`](base/17-interfaz.md) — UI/UX: estados de vista, validación, accesibilidad, texto para el usuario *(opt-in)*
- [`18-despliegue-e-infraestructura.md`](base/18-despliegue-e-infraestructura.md) — CI/CD e IaC como código, release reversible, checklist de despliegue *(opt-in)*
- [`19-observabilidad-y-operacion.md`](base/19-observabilidad-y-operacion.md) — logs estructurados, métricas/SLO, runbooks, postmortem *(opt-in)*

### Capa 3 · Proyecto — vive en cada repo (plantillas para copiar)

- [`plantillas/CLAUDE.md.plantilla`](plantillas/CLAUDE.md.plantilla) — el `CLAUDE.md` del proyecto: precedencia, ajustes y punteros a los anexos
- [`plantillas/stack.md`](plantillas/stack.md) — lenguajes, frameworks, comandos, entorno de pruebas
- [`plantillas/dominio.md`](plantillas/dominio.md) — qué hace el sistema, entidades y reglas de negocio
- [`plantillas/mapeo-nombres.md`](plantillas/mapeo-nombres.md) — cómo se llaman aquí los conceptos abstractos de la base
- [`plantillas/marco-normativo.md`](plantillas/marco-normativo.md) — sector, jurisdicción, leyes y frameworks del cliente
- [`plantillas/plantilla-especificacion-modulo.md`](plantillas/plantilla-especificacion-modulo.md) — esqueleto para redactar la especificación de un módulo (se copia por módulo a `documentacion/`)
- [`plantillas/senales.md`](plantillas/senales.md) — log de señales (memoria: decisiones, errores resueltos, patrones, aprendizajes)
- [`plantillas/checklist-despliegue.md`](plantillas/checklist-despliegue.md) — checklist de un despliegue (opt-in `18`)
- [`plantillas/postmortem.md`](plantillas/postmortem.md) — postmortem de incidente, sin culpa (opt-in `19`)

## Skills

Herramientas activables que aplican el estándar:

- [`analizar-proyecto`](skills/analizar-proyecto/SKILL.md) — diagnostica un proyecto existente: inventario (qué hay), brechas (qué falta), plan priorizado (qué sigue), estrategia de pruebas y tecnologías necesarias. (rol Explorer)
- [`cerrar-fase`](skills/cerrar-fase/SKILL.md) — valida antes de cerrar: pruebas + triangulación + calidad + trazabilidad especificación→implementación. (rol Verifier)
- [`generar-spec-modulo`](skills/generar-spec-modulo/SKILL.md) — redacta la especificación de un módulo antes de programarlo, guiando la plantilla. (rol Spec Writer)
- [`revisar-critico`](skills/revisar-critico/SKILL.md) — revisión adversarial: busca bugs, seguridad y casos que la especificación no anticipó. (rol Reviewer/Crítico)
- [`proponer-alcance`](skills/proponer-alcance/SKILL.md) — traduce una solicitud en un alcance concreto (dentro/fuera) para aprobar. (rol Proposer)
- [`disenar-arquitectura`](skills/disenar-arquitectura/SKILL.md) — define el diseño técnico desde la especificación: datos, estructura, decisiones. (rol Designer)
- [`planificar-tareas`](skills/planificar-tareas/SKILL.md) — divide el trabajo en tareas con grafo de dependencias y plan de pruebas, para aprobación. (rol Task Planner)
- [`implementar`](skills/implementar/SKILL.md) — ejecuta un plan aprobado: código + pruebas, de corrido. (rol Implementer)
- [`sdd-orchestrator`](skills/sdd-orchestrator/SKILL.md) — dirige la línea de montaje: llama a cada rol, controla las puertas, usa el grafo y persiste el estado. (rol Orchestrator)
- [`generar-casos-prueba`](skills/generar-casos-prueba/SKILL.md) — deriva la matriz de casos (corner cases) y triangula el resultado esperado. (apoya Task Planner / Verifier)
- [`usar-memoria`](skills/usar-memoria/SKILL.md) — consulta y registra señales en la memoria central buscable (SQLite+FTS5, con `scope`). Helper en [`memoria/`](memoria/).

## Visor (interfaz local)

[`interfaz/`](interfaz/) — app local (Django + Bootstrap 5 + AdminLTE 4) para **leer todo lo que hace el agente** (reglas, roles, plantillas, notas) y **ver la memoria** (panel + tabla de señales con filtro dinámico, colores por tipo, orden, detalle, registro y export CSV). Funciona sin internet.

**Cómo se corre** (desde la raíz del proyecto):

```
python interfaz/manage.py runserver
```

Luego abrir **http://127.0.0.1:8000** · parar con **Ctrl + C**.

- Si el puerto 8000 está ocupado: `python interfaz/manage.py runserver 8010`
- Requisitos: Python 3.11+ y Django 5 (`pip install -r interfaz/requirements.txt`).

## Versión del estándar

El estándar se versiona. La versión actual vive en [`VERSION`](VERSION); qué cambió en cada una, en [`CHANGELOG.md`](CHANGELOG.md).

**`MAYOR.MENOR.PARCHE`:** MAYOR = una norma que **obliga** (hay que hacer algo para cumplir); MENOR = algo **aditivo** que no invalida nada (regla opcional, plantilla, validador); PARCHE = redacción o ejemplos.

**Cada proyecto fija la versión que sigue.** Su `CLAUDE.md` (capa 3) declara, en el punto 1, la versión adoptada y la fecha (`Versión del estándar adoptada: X.Y.Z · sellada YYYY-MM-DD`). Al abrir sesión, si el proyecto quedó por detrás de `VERSION`, el estándar lo **avisa** (`validadores/validar.py version --raiz .`) — no migra solo.

**Retroactividad:** un cambio de norma **no reabre** fases ya cerradas; quedan selladas con su versión. Lo nuevo aplica al trabajo en curso y al que viene. Así afinar una redacción no obliga a re-tocar trabajo terminado.

## Estado

**Base completa (00–17)** y etiquetada por capa. **Capa 3 lista:** `CLAUDE.md`, `stack`, `dominio`, `mapeo-nombres`, `marco-normativo` y `plantilla-spec-modulo`. **10 skills** (los 8 roles de la línea de montaje + el `sdd-orchestrator` + `generar-casos-prueba`, más `usar-memoria`). **Memoria por señales** operativa (SQLite+FTS5), con **vigencia y poda**, **ciclo de deuda**, **búsqueda semántica opcional** (híbrida, local) y **métricas del proceso**. **Visor local** (Django + AdminLTE) para leer el estándar y la memoria. Pendiente: mejoras opcionales (ejecución paralela en vivo, assets del visor offline) y patrones opt-in de DevOps/RPA.
