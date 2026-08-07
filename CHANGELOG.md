# Cambios del estándar

Historial de versiones de `base/` y `plantillas/`. La versión vive en [`VERSION`](VERSION); el esquema y la regla de retroactividad están en el [README](README.md#versión-del-estándar).

**`MAYOR.MENOR.PARCHE`:**
- **MAYOR** — una norma nueva o cambiada que **obliga** (un proyecto al día tiene que hacer algo para cumplir). Marca `⚠ obliga a migrar`.
- **MENOR** — algo **aditivo** que no invalida nada: regla opcional nueva, plantilla, validador, sección.
- **PARCHE** — redacción, ejemplos, correcciones que no cambian qué se exige.

> Retroactividad: un cambio de norma **no reabre** fases ya cerradas — quedan selladas con la versión bajo la que cerraron. La versión nueva aplica al trabajo en curso y al que viene. El aviso de desfase (al abrir sesión/fase) informa, no migra solo.

---

## 1.4.0 — 2026-08-07

**MENOR** (aditivo: reglas nuevas en un capítulo que no las tenía; nada de lo que ya se cumplía deja de valer).

El capítulo del preámbulo se ajusta al capítulo 20: deja de ser prosa y pasa a tener reglas con identificador.

- `base/00-identidad-y-rol/reglas/` — seis reglas nuevas, **una por archivo**, nombradas `<PREFIJO><n>-<título>`: `ID1` criterio de desarrollador senior · `ID2` registro técnico sin adornos · `ID3` qué cuenta como entregado · `ID4` el ciclo completo de entender a documentar · `ID5` el borde del rol (seis cosas fuera por definición) · `ID6` los roles por etapa no cambian la precedencia.
- `base/00-identidad-y-rol/base.md` — pasa a ser el capítulo con el índice enlazado a las seis. El texto que antes era prosa suelta queda repartido en las reglas; lo que ya decía otro capítulo se enlaza en vez de repetirse (`20·M5`).
- `base/20-meta-reglas/estructura-regla.md` — el prefijo **`ID`** se registra en la tabla de letras ocupadas, como exige `M4` antes de estrenar un prefijo.
- `validadores/reglas-validables.md` — `ID1`–`ID6` clasificadas (criterio humano, `M9`). `ID3` se anota como caso parcial: sus cuatro condiciones ya se validan por separado; lo que no se valida es la conjunción.

Con esto queda cerrada la primera mitad del hallazgo **H-22** del informe de `analisis/`: el capítulo que `02·F0` citaba como fuente de reglas ya tiene reglas citables. Sigue abierto que el número `00` esté compartido con el núcleo.

## 1.3.1 — 2026-08-07

**PARCHE** (no cambia qué se exige; solo dónde vive el texto).

- `base/00-identidad-y-rol.md` pasa a `base/00-identidad-y-rol/base.md`. El capítulo del preámbulo queda con carpeta propia, como `20-meta-reglas/`, para poder crecer con anexos sin inflar el archivo que se carga en cada turno. El texto no cambió.

Detrás: `validadores/cargador.py` decidía qué se carga **literal en todos los turnos** por el nombre del archivo (`00-`, `01-`). Con el capítulo en carpeta, el nombre pasa a ser `base.md` y la identidad del agente habría caído al índice — es decir, el agente arrancaría sin saber quién es. Ahora la comprobación mira el **primer tramo de la ruta**, así que un capítulo del núcleo carga igual viva en archivo suelto o en carpeta.

## 1.3.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). El histórico de sesiones deja de depender de que el agente se acuerde de escribirlo:

- Plantilla nueva: `historico-chat.md` — el `README.md` de la carpeta `historico-chat/` de cada proyecto.
- `CLAUDE.md.plantilla`: punto **2.3** (la carpeta, quién la escribe, se versiona, y cómo excluirla si el chat maneja datos sensibles) y punto **6** ampliado: el instalador es el camino por el que **toda** herramienta nueva del estándar llega al proyecto, sin pasos manuales. Si algo exige configurar a mano, es defecto del estándar.

Detrás: `validadores/hook_historico.py` (enganches `UserPromptSubmit` y `Stop`) e `instalar.py`, que los deja puestos y crea la carpeta. Un proyecto al día no tiene que hacer nada: los recibe la próxima vez que corra el paso 6.

Y el **stack de instalación**: la lista de todo lo que un proyecto debe tener para que el agente esté completo.

- Plantilla nueva: `stack-instalacion.md` — los 11 componentes, qué es cada uno y cómo se instala. Se copia a `./.agente/` de cada proyecto, sellada con la huella del original: si el estándar agrega un componente, la copia deja de coincidir y eso se reporta como actualización pendiente.
- `CLAUDE.md.plantilla`: punto **2.1** (los dos archivos que el estándar escribe en `.agente/` y no se editan a mano) y paso **8** — mientras exista `.agente/INSTALACION-INCOMPLETA.md`, el agente no está completo y debe decir qué falta en cada respuesta. No bloquea: el único gate sigue siendo `F13`.

Detrás: `validadores/checklist.py` (la comprobación de cada componente; la lista se lee de la plantilla, no se duplica en código), `hook_checklist.py` en `UserPromptSubmit`, y `validar.py checklist --raiz` para verlo a mano.

## 1.2.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Un capítulo de **preámbulo**:

- `00 · Meta-reglas` — la regla de reglas: jerarquía de cuatro niveles, organización por dominio con fuente única, orden determinista de desempate ante conflicto, formato canónico de una regla, ID estable, dependencias declaradas (`extiende` / `depende de` / `deroga`), excepciones escritas dentro de la regla, criterio de validable, versionamiento obligatorio, derogación en vez de borrado, y procedimiento para agregar una regla sin duplicar ni contradecir.

No cambia ninguna regla existente: **formaliza** las convenciones que la base ya usaba de hecho y cubre lo que no estaba escrito (desempate, dependencias, derogación, anti-duplicación).

## 1.1.0 — 2026-08-06

**MENOR** (aditivo, no obliga a migrar). Dos capítulos **opt-in** de dominio DevOps:

- `18 · Despliegue e infraestructura` — despliegue como artefacto versionado, IaC, build-una-vez, config por entorno fuera del artefacto, release reversible, checklist de despliegue, health/readiness, y correr contra producción gateado por el usuario. Extiende `09·G6`.
- `19 · Observabilidad y operación` — logs estructurados, señales doradas + trazas, SLO/alertas como código sobre síntomas, runbooks, postmortem sin culpa. Extiende `05`.

Plantillas nuevas: `checklist-despliegue.md`, `postmortem.md`. Toggles en `CLAUDE.md.plantilla §5.1`.

## 1.0.0 — 2026-08-06

Primera versión sellada del estándar. Línea base: núcleo blindado (`00`), conducta y flujo (`01`–`02`), buenas prácticas (`03`–`17`), plantillas de capa 3, memoria por señales con vigencia y ciclo de deuda, y la capa de validadores automáticos + hooks.

A partir de aquí, cada cambio de `base/` o `plantillas/` suma una entrada con su tipo.
