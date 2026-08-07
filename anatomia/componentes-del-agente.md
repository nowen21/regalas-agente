# Componentes del agente

Qué hay dentro de este repositorio, qué hace cada pieza y cuál de ellas **necesita una IA** para funcionar.

> Referido al estándar **v1.3.0** · 2026-08-07.

---

## 1 · La idea en una frase

El agente son **dos mitades**:

| Mitad | Qué es | Quién la ejecuta |
|---|---|---|
| **Determinista** | Programas en Python que comprueban, registran, recuerdan y miden. | La máquina. Siempre da el mismo resultado. |
| **De criterio** | Texto: reglas, plantillas y skills. Dice *qué* se debe hacer y *cómo* pensarlo. | Una IA (o una persona) que lo lea y lo aplique. |

La primera mitad **funciona sola, sin IA**. La segunda no: es papel hasta que alguien lo aplica.

Por eso el estándar puede exigir cosas y además comprobarlas. La regla vive en el texto; la comprobación, en el código.

---

## 2 · Inventario general

| Carpeta | Contiene | ¿Corre sin IA? |
|---|---|---|
| [`base/`](../base/) | 21 capítulos de reglas (00–20). Es la norma que heredan los proyectos. | No — es texto |
| [`plantillas/`](../plantillas/) | 23 plantillas de documentos (épica, HU, fase, ADR, brief, postmortem…). | No — es texto |
| [`skills/`](../skills/) | 11 procedimientos para la IA (analizar proyecto, diseñar arquitectura, generar spec…). | No — es texto |
| [`validadores/`](../validadores/) | 23 comprobaciones + 5 enganches automáticos + el instalador. | **Sí** |
| [`memoria/`](../memoria/) | Memoria por señales (SQLite + FTS5) y búsqueda semántica local. | **Sí** |
| [`metricas/`](../metricas/) | Lector de métricas del proceso. | **Sí** |
| [`interfaz/`](../interfaz/) | Visor web local (Django) del estándar y de la memoria. | **Sí** |
| [`notas/`](../notas/) | 12 notas de diseño: **por qué** se decidió algo así. | No — es texto |
| [`pendientes/`](../pendientes/) | 4 mejoras acordadas y todavía no hechas. | No — es texto |
| [`historico-chat/`](../historico-chat/) | Transcripción literal de cada sesión de trabajo. | Lo **escribe** un enganche |

---

## 3 · Lo que funciona sin IA

Todo esto es Python 3.11+ con **solo biblioteca estándar** — salvo el visor (necesita Django) y la búsqueda semántica (opcional). No hay servicios en la nube ni llamadas a ninguna API.

### 3.1 · Validadores — el linter del proceso

El principio que decide qué entra aquí:

> Si dos personas pueden discutir si se cumplió → se queda en el `.md`.
> Si un script puede decir sí/no sin opinar → validador.

Se corren así:

```sh
python validadores/validar.py <comprobación> [ruta]
```

Las 23 comprobaciones disponibles:

| Grupo | Comprobaciones | Qué revisa |
|---|---|---|
| **Documentación** | `estandar` · `plantilla` · `fases` · `trazabilidad` · `flujo` | Enlaces rotos, índices desactualizados, marcadores sin llenar, jerarquía épica→HU→fase, enlace bidireccional, las 13 preguntas del plan |
| **Git** | `commit` · `rama` · `versionado` · `ci` | Formato del mensaje, trabajo en rama dedicada y al día, secretos o artefactos versionados por error, pipeline de CI con pruebas y linter |
| **Seguridad** | `secretos` · `seguridad` | Claves y tokens incrustados en el código; concatenación SQL/shell, asignación masiva, flags de cookie |
| **Datos** | `esquema` · `migraciones` | FK con política de borrado, `NOT NULL` sin default, longitud de identificador; cada migración con su reversión |
| **Código** | `errores` · `rendimiento` · `calidad` · `aislamiento` · `dependencias` | Capturas de error vacías, `SELECT *`, consultas dentro de un bucle (N+1), funciones demasiado largas, pruebas contra BD efímera, lockfile presente |
| **Herramientas del stack** | `linter` · `suite` · `audit` | Detectan el ecosistema por el manifiesto (`composer.json`, `package.json`, `pyproject.toml`…) y **corren la herramienta real**: pint/phpstan, eslint, ruff, phpunit, pytest, `npm audit`… |
| **Instalación** | `version` · `checklist` | Desfase entre la versión del estándar y la que declara el proyecto; qué componentes del agente le faltan |

Dos severidades, y la diferencia no es cosmética:

- **`FALLA`** — incumplimiento claro. Sale con código 1 y rompe el pipeline.
- **`AVISO`** — algo que un humano debe mirar. Sale con código 0.

Las plantillas dicen *"elimine las secciones que no apliquen"*, así que una sección ausente es `AVISO`, no `FALLA`. Un validador que grita por todo se termina ignorando.

**Los validadores reportan, no arreglan.** Y no duplican la norma: el validador de plantillas abre la plantilla real y compara, así que si la plantilla cambia, el validador cambia con ella sin tocar código.

### 3.2 · Enganches automáticos — lo que corre solo

Cinco enganches, cada uno en un momento distinto. Ninguno se solapa con otro.

| Cuándo | Qué hace | Efecto si incumple |
|---|---|---|
| **Antes de aceptar un commit** (`git commit-msg`) | Revisa el mensaje contra la norma de git. | El commit **no se crea** |
| **Al abrir la sesión** (`SessionStart`) | Revisa el estado del estándar. | Informa |
| **Al enviar cada mensaje** (`UserPromptSubmit`) | Anota el mensaje del usuario en el histórico, con la hora del reloj de la máquina. | Escribe |
| **Al terminar cada respuesta** (`Stop`) | Anota la respuesta en el histórico, leyéndola del transcript. | Escribe |
| **Al editar un `.md`** (`PostToolUse`) | Comprueba enlaces e índices y devuelve el detalle en el momento. | Informa |
| **Al enviar cada mensaje** (`UserPromptSubmit`) | Revisa qué le falta al proyecto del stack del agente. | Escribe `INSTALACION-INCOMPLETA.md`; no bloquea |

Dos detalles que explican el diseño:

- **El hook de git va en `.githooks/`, no en `.git/hooks/`**, porque esa segunda carpeta no se versiona. Así el enganche viaja con el repositorio; cada clon nuevo solo corre `git config core.hooksPath .githooks` una vez.
- **El histórico lo escribe el enganche, no el agente.** La regla dice que toda sesión queda registrada, y mientras eso dependa de que alguien se acuerde, no se cumple siempre. Un `CLAUDE.md` informa; un enganche ejecuta.

### 3.3 · Memoria — lo que el proyecto no debe volver a olvidar

Base SQLite con búsqueda de texto completo (FTS5). Guarda **señales**: decisiones, errores resueltos, patrones, gotchas, supuestos, restricciones, deuda técnica, preguntas abiertas.

```sh
python memoria/memoria.py add --tipo decision --titulo "..." --why "..."
python memoria/memoria.py search "facturacion iva" --scope proyecto:tienda
python memoria/memoria.py pendientes            # deuda y preguntas sin cerrar
python memoria/memoria.py cerrar S-014 --ref "F3 / commit abc1234"
python memoria/memoria.py revisar --viejas      # las que llevan más sin verificar
python memoria/memoria.py supersede S-003 --by S-012
python memoria/memoria.py archivar S-003        # sale de search, se conserva
```

Cada señal tiene **ciclo de vida**: se crea, se revisa, se supera, se cierra o se archiva. Una señal sin revisar en más de 6 meses se marca *sin verificar* — no se borra, se señala.

**Búsqueda semántica (opcional).** FTS5 encuentra palabras; el módulo semántico encuentra significado, y la búsqueda combina los dos. Es opt-in: si las dependencias no están instaladas, la memoria sigue funcionando solo con FTS5. Los vectores se calculan **en la máquina** y se guardan en la misma base — el contenido nunca sale del equipo.

```sh
pip install -r memoria/requirements-semantica.txt
python memoria/memoria.py indexar
```

### 3.4 · Métricas — si el estándar está sirviendo

```sh
python metricas/metricas.py [--scope proyecto:x] [--meses 6]
```

Lee lo que **ya se registra** en la memoria y lo agrega. No es telemetría: no instrumenta nada nuevo.

Reporta hoy: deuda diferida abierta vs cerrada, señales activas sin verificar hace más de N meses, y el conteo por estado y por tipo.

> **Para decidir qué reglas cambiar, no para calificar el trabajo.**

Una métrica visible se convierte en objetivo y deja de medir: "cero fases reabiertas" se consigue **no reabriendo** ninguna, no haciéndolas bien.

### 3.5 · Visor — el estándar y la memoria en el navegador

```sh
python interfaz/manage.py runserver
```

Luego abrir **http://127.0.0.1:8000**.

Django + Bootstrap 5 + AdminLTE 4, con todo el vendor incluido: **funciona sin internet**. Muestra las reglas, las skills, las plantillas y las notas renderizadas, y una tabla de la memoria con filtro dinámico y detalle por señal. Modo oscuro incluido.

### 3.6 · Instalador — cómo llega el agente a otro proyecto

```sh
python validadores/instalar.py --raiz "<ruta del proyecto>"
```

Copia los cinco enganches, la carpeta `historico-chat/` y la lista de componentes al proyecto destino. La regla de diseño:

> Una herramienta nueva del estándar se agrega a la lista y **llega sola** a todos los proyectos. Si exige configurarla a mano, está mal hecha.

---

## 4 · Lo que **no** funciona sin IA

| Recurso | Por qué necesita criterio |
|---|---|
| Las reglas de [`base/`](../base/) | Son texto normativo. Alguien tiene que leerlas y aplicarlas al caso concreto. |
| Las 11 [`skills/`](../skills/) | Son procedimientos de razonamiento: analizar un proyecto, proponer alcance, diseñar arquitectura, generar una spec, planificar tareas, implementar, generar casos de prueba, revisar críticamente, cerrar fase, usar la memoria. |
| Las [`plantillas/`](../plantillas/) | El validador comprueba que estén **llenas**; no comprueba que estén **bien** llenas. |
| Las puertas del flujo | "¿La spec está completa?", "¿el plan es viable?", "¿esta decisión fue buena?" — no hay script que responda eso sin opinar. |
| Redactar, decidir, revisar | El trabajo mismo. |

---

## 5 · Resumen

**Sin IA** el repositorio es un **linter de proceso + una memoria de proyecto + un visor**, que se instalan solos en cualquier proyecto y no dependen de ningún servicio externo.

**Lo que no hay sin IA** es quien redacte, decida o revise.

Las dos mitades se necesitan: el texto sin el código se incumple en silencio; el código sin el texto comprueba reglas que nadie puede consultar. De ahí la regla de oro de los validadores — **nada se comprueba que no esté escrito en la norma**: primero se escribe en `base/`, después se comprueba.
