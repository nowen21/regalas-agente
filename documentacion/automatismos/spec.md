# Especificación del módulo Automatismos

- **Slug del módulo:** `automatismos`
- **Estado:** en implementación

> El módulo son los programas que corren solos al trabajar: los enganches de la sesión. Esta especificación crece con cada fase. Lo que cubre hoy:
>
> | Incremento | Fase | Estado |
> |---|---|---|
> | El enganche que sostiene el resumen de sesión | [`A-EP-005-HU-008-enganche-del-resumen`](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/README.md) | Cerrada el 2026-08-14 |
>
> Los siete enganches que ya existen (transcripción, memoria, enlaces, instalación) se construyeron antes de que hubiera especificación de módulo. Retro-documentarlos es trabajo aparte, y lo pide [`13·DOC6`](../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-spec-antes-de-tocarlo.md).

---

## 1. Propósito y alcance

Lo que depende de que alguien se acuerde, no pasa. El módulo existe para que las cosas que el estándar exige en cada sesión las haga un programa, no la memoria de quien esté trabajando.

- **Dentro de alcance:** el enganche del resumen de sesión, con sus tres comportamientos: crear el archivo al abrir, avisar qué le falta al resumen cuando la sesión ya produjo algo, y mostrar lo que sigue abierto del propósito que la sesión declara.
- **Fuera de alcance:**
  - **Escribir los hallazgos.** Reconocer un hallazgo y redactarlo es criterio, y el criterio no lo tiene un programa. El enganche crea, avisa y arrastra.
  - **Decidir qué es un hallazgo.** Eso lo decide quien trabaja.
  - **El modelo del resumen**, que es de EP-003 · HU-009 y ya está cerrado.
  - **Los otros enganches** que ya existen. Esta fase no los toca.

## 2. Contexto — qué hay hoy

Verificado el 2026-08-14.

**Siete enganches ya corriendo**, conectados en `.claude/settings.json` por [`validadores/instalar.py`](../../validadores/instalar.py), que es quien los instala en cada proyecto:

| Evento | Programa | Qué hace |
|---|---|---|
| `SessionStart` | `hook_sesion.py` | Carga las reglas, la memoria y el índice del histórico |
| `SessionStart` | `hook_recuerdos.py` | Recoge la memoria que quedó en el almacén de la herramienta |
| `UserPromptSubmit` | `hook_historico.py` | Anota el mensaje del usuario en la transcripción |
| `Stop` | `hook_historico.py` | Anota la respuesta del agente |
| `UserPromptSubmit` | `hook_checklist.py` | Revisa que el agente esté bien instalado |
| `PostToolUse` | `hook_md.py` | Revisa los enlaces al escribir un archivo |
| `PostToolUse` | `hook_recuerdos.py` | Recoge la memoria al escribir un archivo |

**La lección ya está probada.** La transcripción de la sesión solo empezó a escribirse siempre cuando la escribió un programa. Antes era una obligación escrita, y se incumplía.

**El resumen está en ese punto.** Desde la 14.0.0 [`13·DOC22`](../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) lo exige, el modelo existe y el índice lo enlaza. Lo que no existe es el programa: hoy el resumen se escribe porque el agente se acuerda, que es exactamente la forma en que se pierde.

**Un detalle que condiciona el diseño.** La transcripción nace como `AAAA-MM-DD-sesion.md` y se renombra cuando el tema está claro. El resumen se llama igual, sin la fecha, así que **los dos nombres tienen que moverse juntos**: si solo se renombra uno, el enlace del índice apunta a un archivo que no existe.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:**
  - "La sesión ya produjo algo" se puede detectar sin criterio: hubo un commit, o cambió un archivo de `base/` o de `plantillas/`.
  - Lo que un enganche imprime le llega al agente en ese turno. Es como funciona hoy el recordatorio de ponerle nombre a la sesión.
- **Dependencias / prerequisitos:**
  - EP-003 · HU-009, el modelo del resumen. **Cerrada** el 2026-08-14.
  - EP-005 · HU-001, la transcripción de la sesión. Ya corriendo: comparte el momento y el nombre del archivo.
- **Preguntas abiertas:** cuál es la señal de que el tema ya cerró. Viene arrastrada del hallazgo H-4 y sigue sin decidir. No bloquea: lo que el enganche mira es si la sección de cierre está llena, no si el tema cerró de verdad.

## 4. Reglas de negocio

1. **El archivo del resumen se crea solo al abrir la sesión**, con el modelo puesto y sin hallazgos.
2. **El resumen se renombra con la transcripción.** Los dos nombres se mueven en la misma operación, o el índice queda apuntando a un archivo que no existe.
3. **Cuando la sesión ya produjo algo y al resumen le falta algo, se avisa una vez por cada cosa que falte.** Son dos como máximo: que no haya ningún hallazgo escrito, y que no se haya dicho si la sesión se puede cerrar. Un aviso repetido se vuelve ruido y se deja de leer.
4. **El aviso dice qué falta**, con la lista. Un aviso genérico obliga a preguntar, y preguntar es justo lo que se quiere evitar.
5. **Para cerrar una sesión cuentan los hallazgos de su propósito.** Cada sesión se abre para resolver algo; lo que aparece y es de otro tema nace acá y se cierra en otra sesión, y basta con que quede anotado.
6. **Se muestra lo que sigue abierto del propósito de la sesión, y nada más.** El propósito lo declara el usuario al abrir; el programa no lo adivina. Mostrar todos los hallazgos abiertos del repositorio es ruido: una sesión abierta para una cosa no tiene por qué ver las de otro tema.
7. **El enganche no escribe hallazgos ni los interpreta.** Crea, avisa y arrastra.
8. **El enganche no detiene el trabajo.** Si no puede escribir, avisa y la sesión sigue.
9. **El enganche no modifica un hallazgo ya escrito.**

## 5. Modelo de datos

No aplica porque el entregable son programas de línea de comandos sobre archivos de texto: no hay entidades, tablas ni catálogos.

## 6. Comportamiento y flujos

**Al abrir la sesión.** El enganche mira si existe el resumen del día para esa sesión. Si no está, lo crea con el modelo y sin hallazgos.

**Al declararse el propósito.** Cuando la sesión dice qué hallazgo viene a resolver —en su «viene de»—, el enganche va a buscarlo, y muestra ese hallazgo y lo que siga abierto de él. Nada de otros temas: una sesión abierta para una cosa no tiene por qué ver las demás.

**Durante la sesión.** Cada vez que el usuario manda un mensaje, el enganche pregunta si la sesión ya produjo algo. Si sí, mira qué le falta al resumen y avisa lo que encuentre, una vez cada cosa:

| Qué falta | Qué imprime |
|---|---|
| Ningún hallazgo escrito | Que el resumen está vacío, y dónde está el archivo |
| Hay hallazgos, pero no dice si la sesión se puede cerrar | Cuáles son los hallazgos del propósito que siguen sin resolver |

Cada aviso deja su marca en el propio resumen, así que no se repite. Dos avisos como máximo en toda la sesión.

**Al ponerle nombre a la sesión.** El renombrado mueve los dos archivos, la transcripción y el resumen, y corrige la línea del índice con el enlace nuevo.

**Camino de error.** Si el enganche no puede escribir —carpeta sin permisos, disco lleno—, imprime el motivo y sale con código 0. La sesión sigue. Un enganche que detiene el trabajo es peor que el problema que resuelve.

## 7. Interfaz / UI

No aplica: se ve como un mensaje en la sesión, no como pantalla.

## 8. Permisos y autorización

No aplica porque no hay servicio ni autenticación.

| Permiso | Quién lo tiene | Qué habilita |
|---|---|---|
| Ninguno | — | — |

## 9. Marco normativo

No aplica: el módulo no toca datos personales ni ninguna norma externa.

## 10. Plan de pruebas

El detalle vive en el [plan_pruebas.md](../epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/A-EP-005-HU-008-enganche-del-resumen/plan_pruebas.md) de la fase. En resumen:

- **Caso feliz:** se abre una sesión y el archivo aparece, con el modelo y sin hallazgos.
- **Casos límite:** dos sesiones el mismo día, una sesión que no produce nada, un resumen que ya tiene hallazgos.
- **Errores:** carpeta sin permiso de escritura; el aviso no se repite; el enganche no toca lo ya escrito.
- **Triangulación:** que la sesión "produjo algo" se comprueba por dos caminos independientes, el commit y el cambio en `base/`.
- **Verificación manual ([`08·T4`](../../base\08-pruebas.md#t4--protege-los-datos-reales-al-probar)):** que el aviso se lea como ayuda y no como ruido. Eso no lo mide ningún programa.

## 11. Criterios de aceptación (Definition of Done)

- [x] El archivo del resumen se crea solo al abrir la sesión.
- [x] Se renombra junto con la transcripción, y el índice queda al día.
- [x] Avisa qué falta, una vez por cada cosa, cuando la sesión produjo algo.
- [x] Lo que sigue abierto del propósito se muestra al abrir la sesión.
- [x] No escribe hallazgos, no modifica los escritos y no detiene la sesión.
- [x] Pruebas verdes, incluida la triangulación de "produjo algo".
- [ ] Trazabilidad especificación → implementación sin faltantes ([`13·DOC3`](../../base/13-documentacion/reglas/DOC3-verifica-la-trazabilidad-spec-implementacion-antes-de-cerrar.md)).
- [ ] Entrada en `CHANGELOG.md` y subida de `VERSION` ([`20·M10`](../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 12. Decisiones tomadas

- **`2026-08-14` — el enganche crea, avisa y arrastra; no escribe hallazgos.** Reconocer un hallazgo es criterio. Lo que un programa sí puede hacer es que el hueco se vea.
- **`2026-08-14` — el resumen se crea al abrir la sesión, no al cerrarla.** Un chat no tiene final: lo que se deja para el cierre no se escribe. Es la misma lección de la transcripción.
- **`2026-08-14` — el aviso sale una vez por cada cosa que falta, no una por sesión.** Se descartó el aviso único porque dejaba pasar el caso real: escribir un hallazgo y no decir nunca si la sesión se puede cerrar. Son dos como máximo.
- **`2026-08-14` — el aviso dice qué falta, con la lista.** Un aviso genérico obliga a preguntar qué falta, y preguntar es lo que se quiere evitar.
- **`2026-08-14` — para cerrar cuentan los hallazgos del propósito de la sesión.** Cada sesión se abre para resolver algo. Lo que aparece y no es de ese propósito se cierra en otra, y acá basta con dejarlo anotado.
- **`2026-08-14` — se muestra solo lo abierto del propósito de la sesión.** Se descartó mostrar todo lo abierto del repositorio: una sesión que trabaja un tema no tiene por qué ver los hallazgos de otro, y ese ruido es lo que hace que los avisos se dejen de leer. Sin límite de días: el hallazgo del propósito se busca donde esté.
- **`2026-08-14` — el enganche nunca detiene el trabajo.** Sale con código 0 pase lo que pase, igual que los siete que ya existen.

## 13. Trazabilidad (se completa al implementar)

| Ítem de la especificación | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · el archivo se crea al abrir | programa | `validadores/resumen.py` | ✅ | CP-001 |
| RN-02 · se renombra con la transcripción | programa | `validadores/historico.py` | ✅ | CP-003 |
| RN-03 · avisa qué falta, una vez por hueco | programa | `validadores/hook_resumen.py` | ✅ | CP-004 y CP-007 |
| RN-04 a RN-06 · qué falta, qué cuenta para cerrar, y lo abierto del propósito | programa | `validadores/resumen.py` | ✅ | CP-006 |
| RN-07 a RN-09 · límites del enganche | programa | `validadores/hook_resumen.py` | ✅ | CP-009 |
| Instalación en cada proyecto | programa | `validadores/instalar.py` | ✅ | Los dos enganches en `.claude/settings.json` |

## 14. Cruces con otros módulos

**Qué consume este módulo de otros:**

| Módulo | Qué consume | Por qué |
|---|---|---|
| `documentos-modelo` | El modelo `plantillas/sesion.md` | Es lo que copia al crear el archivo |
| `instalador` | `validadores/instalar.py` | Es quien conecta el enganche en cada proyecto |

**Historial cruzado — quién consume de este módulo:**

| Fecha | Módulo que consume | Qué cambió acá por eso |
|---|---|---|
| Ninguno | — | — |
