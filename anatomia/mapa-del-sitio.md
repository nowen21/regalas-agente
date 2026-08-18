# Mapa del sitio del agente

Dónde está cada cosa y para qué sirve. Si busca un archivo y no sabe por dónde empezar, empiece aquí.

> Estándar **v1.4.0** · actualizado el **2026-08-07**.
> Para entender *cómo funciona* el agente: [componentes-del-agente.md](componentes-del-agente.md).

---

## 1 · Cómo leer este mapa

El repositorio se divide en **cuatro zonas**. Toda carpeta pertenece a una:

| Zona | Qué guarda | Carpetas |
|---|---|---|
| 🟦 **Norma** | Lo que se exige y con qué molde se escribe. Es lo que heredan los proyectos. | `base/` · `plantillas/` · `skills/` |
| 🟩 **Herramientas** | Programas que comprueban, recuerdan, miden y muestran. Corren sin IA. | `validadores/` · `memoria/` · `metricas/` · `interfaz/` |
| 🟨 **Bitácora** | Qué pasó y por qué. No es norma: es memoria escrita. | `historico-chat/` · `notas/` · `pendientes/` · `prompts/` · `anatomia/` |
| ⬜ **Apoyo** | Configuración, empaquetado y material que no es del estándar. | `.claude/` · `.claude-plugin/` · `.githooks/` · `diplomado-ia/` |

La distinción importa: **solo la zona Norma viaja a los proyectos** que heredan el estándar. Lo demás se queda aquí.

---

## 2 · El árbol completo

```
agente/
│
├── README.md ......................... qué es el estándar y qué problema resuelve
├── CLAUDE.md ......................... cómo se trabaja DENTRO de este repo
├── CHANGELOG.md ...................... qué cambió en cada versión
├── VERSION ........................... versión del estándar (hoy 1.4.0)
├── LICENSE
├── Manual-Estandar-Agente.docx ....... manual en Word
├── _base_modulo.md ................... plantilla canónica de spec de módulo (no se versiona)
│
├── 🟦 base/ .......................... LA NORMA · 21 capítulos (00–20) + el glosario
│   ├── glosario.md ................... anexo: cada término del estándar en una línea
│   ├── 00-nucleo-blindado.md ......... reglas que nunca se pueden relajar
│   ├── 00-identidad-y-rol/
│   │   ├── base.md ................... quién es el agente y qué puede decidir
│   │   └── reglas/ ................... ID1–ID6, una regla por archivo
│   ├── 01-conducta.md ................ cómo se comporta en la sesión
│   ├── 02-flujo-de-trabajo/
│   │   ├── base.md ................... índice del flujo (F0…F13)
│   │   ├── estructura-base.md ........ anexo de F13: el árbol obligatorio del proyecto
│   │   └── reglas/ ................... F0–F20, una por archivo (F4.1–F4.5 derogadas)
│   ├── 03-datos.md ................... modelo de datos y migraciones
│   ├── 04-seguridad.md ............... secretos, inyección, sesiones
│   ├── 05-errores-y-logging.md
│   ├── 06-rendimiento.md
│   ├── 07-calidad-de-codigo.md
│   ├── 08-pruebas.md
│   ├── 09-git.md ..................... commits, ramas, qué no se versiona, CI
│   ├── 10-dependencias.md
│   ├── 11-configuracion-entornos.md
│   ├── 12-privacidad-datos.md
│   ├── 13-documentacion/ ............. qué se documenta y con qué índices vivos
│   │   ├── base.md · reglas/DOC1–DOC18 · render-local-de-md.md
│   ├── 14-estructura-codigo.md
│   ├── 15-registros-inmutables.md
│   ├── 16-cumplimiento-y-calidad.md
│   ├── 17-interfaz.md
│   ├── 18-despliegue-e-infraestructura.md
│   ├── 19-observabilidad-y-operacion.md
│   └── 20-meta-reglas/ ............... PREÁMBULO · cómo son las reglas mismas
│       ├── base.md ................... M1…M13: dónde vive cada regla, cuál gana, cómo se agrega
│       └── estructura-regla.md ....... el molde exacto de una regla (M5)
│
├── 🟦 plantillas/ .................... 24 MOLDES DE DOCUMENTO
│   ├── CLAUDE.md.plantilla ........... el CLAUDE.md que recibe cada proyecto
│   ├── planteamiento.md · epica.md · HU.md · fase.md · estado-fase.md
│   ├── planes/
│   │   ├── trabajo.md ................ plan de trabajo (las 13 preguntas)
│   │   └── pruebas.md
│   ├── plantilla-especificacion-modulo.md · catalogo-modulos.md · mapa-dependencias.md
│   ├── ADR.md ........................ decisión de arquitectura
│   ├── stack.md · dominio.md · mapeo-nombres.md · marco-normativo.md
│   ├── reglas-proyecto.md ............ reglas propias del proyecto
│   ├── stack-instalacion.md .......... qué componentes debe tener instalados un proyecto
│   ├── senales.md .................... formato de las señales de memoria
│   ├── inventario-hu.md ............. qué HU están completas y qué documento le falta a cada una
│   ├── historico-chat.md · cierre-analisis.md · funcionalidad-implementada.md
│   ├── checklist-despliegue.md · postmortem.md
│   └── proyectos.md .................. registro local de proyectos (no se versiona)
│
├── 🟦 skills/ ........................ 11 PROCEDIMIENTOS PARA LA IA (un SKILL.md cada uno)
│   ├── sdd-orchestrator/ ............. coordina las demás; es la entrada del flujo
│   ├── analizar-proyecto/ ............ leer un proyecto existente y entenderlo
│   ├── proponer-alcance/ ............. qué entra y qué no
│   ├── disenar-arquitectura/
│   ├── generar-spec-modulo/
│   ├── planificar-tareas/
│   ├── implementar/
│   ├── generar-casos-prueba/
│   ├── revisar-critico/
│   ├── cerrar-fase/
│   └── usar-memoria/ ................. cuándo consultar y cuándo grabar una señal
│
├── 🟩 validadores/ ................... LAS COMPROBACIONES + LOS ENGANCHES
│   ├── README.md ..................... el principio y la tabla completa
│   ├── validar.py .................... ENTRADA ÚNICA: python validar.py <comprobación>
│   ├── comun.py ...................... severidades FALLA/AVISO, utilidades
│   ├── codigo.py ..................... recorre el código versionado del proyecto
│   │
│   ├── ── documentación ──
│   ├── enlaces.py .................... enlaces rotos e índices desactualizados
│   ├── plantillas.py ................. un documento contra su plantilla
│   ├── fases.py ...................... jerarquía épica → HU → fase
│   ├── trazabilidad.py ............... enlace bidireccional, ORIGEN, tabla de cierre
│   ├── flujo.py ...................... el plan trae las 13 preguntas y sin incertidumbre
│   │
│   ├── ── git ──
│   ├── commits.py .................... formato del mensaje
│   ├── rama.py ....................... rama dedicada y al día
│   ├── versionado.py ................. secretos y artefactos versionados por error
│   ├── ci.py ......................... existe pipeline con pruebas y linter
│   │
│   ├── ── seguridad y datos ──
│   ├── secretos.py ................... claves incrustadas en el código
│   ├── seguridad.py .................. concatenación SQL/shell, asignación masiva
│   ├── esquema.py .................... FK con política de borrado, NOT NULL sin default
│   ├── migraciones.py ................ cada migración declara su reversión
│   │
│   ├── ── código ──
│   ├── errores.py .................... capturas vacías, secretos en logs
│   ├── rendimiento.py ................ SELECT *, consultas en bucle (N+1)
│   ├── calidad.py .................... funciones demasiado largas
│   ├── aislamiento.py ................ pruebas contra BD efímera
│   ├── dependencias.py ............... lockfile presente y versionado
│   ├── herramientas.py ............... corre linter / suite / audit del stack real
│   │
│   ├── ── instalación y estado ──
│   ├── instalar.py ................... deja el agente instalado y operativo en otro proyecto
│   ├── checklist.py .................. qué componentes le faltan al proyecto
│   ├── version.py .................... desfase de versión estándar vs proyecto
│   ├── sesion.py ..................... revisión de arranque de sesión
│   ├── cargador.py ................... carga las reglas base al contexto del agente
│   ├── historico.py .................. ESCRIBE la transcripción de la sesión
│   ├── recuerdos.py .................. MUEVE la memoria del agente al repositorio
│   │
│   ├── ── enganches (los llama Claude Code) ──
│   ├── hook_md.py .................... tras editar un .md → revisa enlaces
│   ├── hook_sesion.py ................ al abrir sesión → revisa y carga reglas, memoria e histórico
│   ├── hook_historico.py ............. cada mensaje y cada respuesta → al histórico
│   ├── hook_checklist.py ............. cada mensaje → revisa la instalación
│   ├── hook_recuerdos.py ............. al abrir sesión y al escribir → recoge la memoria
│   │
│   ├── pruebas.py .................... suite de los validadores
│   └── reglas-validables.md .......... qué regla se puede comprobar y cuál no
│
├── 🟩 memoria/ ....................... LO QUE NO SE DEBE VOLVER A OLVIDAR
│   ├── memoria.py .................... CLI: add · search · pendientes · cerrar · revisar…
│   ├── semantica.py .................. búsqueda por significado, local y opcional
│   ├── esquema.sql ................... tablas + índice FTS5
│   ├── requirements-semantica.txt .... dependencias opcionales
│   ├── pruebas.py
│   └── senales.db .................... la base real (NO se versiona)
│
├── 🟩 metricas/ ...................... ¿EL ESTÁNDAR ESTÁ SIRVIENDO?
│   ├── metricas.py ................... lee senales.db y agrega
│   ├── pruebas.py
│   └── README.md ..................... qué reporta y qué falta instrumentar
│
├── 🟩 interfaz/ ...................... VISOR WEB LOCAL (Django, funciona sin internet)
│   ├── manage.py ..................... python interfaz/manage.py runserver
│   ├── requirements.txt
│   ├── config/ ....................... settings, urls, wsgi
│   ├── visor/
│   │   ├── core.py ................... lee los .md del estándar y consulta la memoria
│   │   ├── views.py
│   │   ├── templates/visor/ .......... home · panel · doc · memoria · detalle de señal
│   │   ├── templatetags/
│   │   └── static/vendor/ ............ Bootstrap 5, AdminLTE 4, Chart.js (incluidos)
│   ├── README.md
│   └── _visor.sqlite3 ................ base interna de Django (NO se versiona)
│
├── 🟨 anatomia/ ...................... CÓMO ESTÁ HECHO EL AGENTE
│   ├── componentes-del-agente.md ..... qué hace cada pieza y cuál necesita IA
│   └── mapa-del-sitio.md ............. este archivo
│
├── 🟨 notas/ ......................... POR QUÉ se decidió algo así (12 notas)
│   ├── README.md ..................... índice
│   ├── cobertura-del-agente.md ....... qué cumple hoy y qué no
│   ├── memoria-por-senales.md · memoria-buscable-fts5.md
│   ├── roles-especializados.md · orquestador-y-triangulacion.md
│   ├── compactacion-mata-decisiones.md · aislamiento-checkpoints-memoria.md
│   ├── agente-24-7-y-tareas.md · subagentes-y-entorno.md
│   ├── velocidad-consistencia-calidad.md · que-es-triangulacion-de-pruebas.md
│
├── 🟨 prompts/ ....................... LO QUE PIDIÓ EL USUARIO, CON SUS PALABRAS
│   ├── README.md ..................... índice: qué pidió cada uno y en qué quedó
│   └── regla-reglas-proyecto.md ...... el pedido del que salió `20·M16`
│
├── 🟨 pendientes/ .................... BACKLOG DEL ESTÁNDAR
│   ├── README.md ..................... el número es el orden, no la prioridad
│   ├── 01-validadores-de-codigo-de-proyecto.md
│   ├── 08-patrones-rpa.md
│   └── hecho/ ........................ 7 pendientes ya cerrados, uno por tema
│
├── 🟨 historico-chat/ ................ TRANSCRIPCIÓN LITERAL DE CADA SESIÓN
│   ├── README.md ..................... formato y plantilla + índice de sesiones
│   ├── AAAA-MM-DD-tema.md ............ una por sesión; las escribe hook_historico.py
│   ├── memory/ ....................... LA MEMORIA DEL AGENTE (01·C19)
│   │   ├── memory.md ................. índice de los recuerdos
│   │   └── <recuerdo>.md ............. uno por recuerdo: qué se pide · por qué · cómo se aplica
│   └── reglas-2026-08-06/
│
├── ⬜ prompts/ ....................... (vacía)
│
├── ⬜ diplomado-ia/ .................. apuntes de clase — NO es parte del estándar
│
├── ⬜ .claude/settings.json .......... configuración de los 7 enganches (NO se versiona)
├── ⬜ .claude-plugin/plugin.json ..... empaqueta el repo como plugin de Claude Code
├── ⬜ .githooks/
│   ├── commit-msg .................... bloquea el commit con mensaje mal formado
│   └── pre-commit .................... bloquea secretos y artefactos
└── ⬜ .gitignore
```

---

## 3 · Quién usa a quién

El mapa de arriba dice *dónde está*. Este dice *qué depende de qué*:

| Componente | Lee / usa | Por qué importa |
|---|---|---|
| `validadores/plantillas.py` | `plantillas/*.md` | La norma no se duplica en el código: si cambia la plantilla, cambia la comprobación. |
| `validadores/checklist.py` | `plantillas/stack-instalacion.md` | La lista de componentes vive en la plantilla, no en el código. Una prueba exige que coincidan. |
| `validadores/cargador.py` | `base/*.md` | Mete las reglas al contexto del agente al abrir la sesión, sin depender de que se acuerde. |
| `validadores/sesion.py` | `plantillas/CLAUDE.md.plantilla` | Avisa si el `CLAUDE.md` del proyecto quedó desfasado. |
| `validadores/instalar.py` | `plantillas/CLAUDE.md.plantilla` · `plantillas/stack-instalacion.md` · `.githooks/` · `historico-chat/` · `historico-chat/memory/` · `plantillas/proyectos.md` | Es lo que deja el agente instalado y operativo en otro proyecto, sin pasos manuales. |
| `validadores/recuerdos.py` | `~/.claude/projects/<proyecto>/memory/` | Vacía el almacén de la herramienta hacia el repositorio: la memoria que no se versiona no se puede revisar (`01·C19`). |
| `metricas/metricas.py` | `memoria/senales.db` | Solo agrega lo que ya se registró; no instrumenta nada nuevo. |
| `interfaz/visor/core.py` | `base/` · `skills/` · `plantillas/` · `notas/` · `senales.db` | Lee los archivos y la base **reales**, no una copia. |
| `.githooks/commit-msg` | `validadores/validar.py commit` | El hook es una cáscara; la regla está en el validador. |
| Todos los `hook_*.py` | `validadores/*.py` | Los enganches no tienen lógica propia: llaman al validador que corresponde. |

**La cadena que sostiene todo:** una regla se escribe en `base/` → si es comprobable sin criterio, se le hace un validador → el validador se cuelga de un enganche → el enganche llega a cada proyecto por `instalar.py`. Si un paso falta, la regla se cumple solo cuando alguien se acuerda.

---

## 4 · Lo que existe en disco pero no en el repositorio

Estos archivos aparecen al trabajar y están en [`.gitignore`](../.gitignore) a propósito:

| Archivo | Por qué no se versiona |
|---|---|
| `memoria/senales.db` | Es la memoria del usuario, no del estándar. |
| `interfaz/_visor.sqlite3` | Base interna de Django. |
| `plantillas/proyectos.md` | Registro de qué proyectos usan el agente en **esta** máquina. |
| `.claude/` | Configuración local de la herramienta. |
| `_base_modulo.md` | Material de trabajo local. |
| `__pycache__/` · `*.pyc` | Compilados. |

---

## 5 · Cómo se mantiene este mapa al día

**Regla: este archivo se actualiza en el mismo cambio que agrega, elimina o modifica un componente.** No después, no en otro commit — el mapa que va un paso atrás miente, y un mapa que miente es peor que no tener mapa.

Qué obliga a tocarlo:

| Si el cambio… | Actualice |
|---|---|
| Agrega o borra una carpeta | Zona (§1), árbol (§2) |
| Agrega o borra un archivo de `base/`, `plantillas/`, `skills/`, `validadores/` | Árbol (§2) y el conteo del encabezado de esa carpeta |
| Agrega un enganche o un componente al instalador | Árbol (§2) y dependencias (§3) |
| Cambia qué lee un programa | Dependencias (§3) |
| Agrega una entrada al `.gitignore` | §4 |
| Sube la versión del estándar | El encabezado del documento |

Para comprobar que el árbol coincide con la realidad:

```sh
find . -not -path "./.git/*" -not -path "*/__pycache__/*" \
       -not -path "./interfaz/visor/static/vendor/*" | sort
```

Y para que no queden enlaces rotos después de editar:

```sh
python validadores/validar.py estandar
```
