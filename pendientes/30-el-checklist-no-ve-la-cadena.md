# Pendiente · El checklist no ve la cadena: un proyecto llega a código con `prompts/` vacía y el arranque en verde

**Estado:** abierto · anotado 2026-08-15, desde el proyecto `shopnest-mesa`.

`02·F0` exige `brief → épica → HU → especificación → plan → código` y dice que ningún eslabón se salta. El checklist de instalación no mira ninguno de los tres primeros: recorre `stack-instalacion.md`, y ahí el brief **no es un componente**. `instalar.py` crea `prompts/` (`CARPETAS_BASE`) y la deja vacía.

Resultado: un proyecto puede tener código commiteado, `prompts/` sin un solo archivo, ninguna épica, ninguna HU, y el arranque diciendo «13 de 13, instalación completa». Eso fue exactamente lo que pasó en `shopnest-mesa`: la fase 1 —un esqueleto Django funcionando contra MySQL— se construyó y se commiteó sin que existiera el brief, y nada lo señaló. Lo notó el usuario preguntando, no el estándar.

## Qué se propone

Que el checklist reporte como **pendiente** que la cadena esté vacía. Como mínimo:

- `prompts/` sin ningún `<slug>-planteamiento.md`.
- Código de proyecto en `proyectos/` con `documentacion/epicas/` vacía.

No es un componente que falte instalar, así que probablemente no va como los trece actuales: es una comprobación de proceso sobre un proyecto que ya está completo. Si el checklist solo admite componentes, el sitio puede ser el validador de flujo del pendiente [01](01-validadores-de-codigo-de-proyecto.md), que es el que ya cubre las puertas de flujo.

## Lo que NO se propone

**Que el instalador deje el brief.** No puede: el brief lo escribe el agente con lo que el usuario quiere (`base/glosario.md`), y el instalador no pregunta. Copiar `plantillas/planteamiento.md` con los marcadores sin llenar sería peor que no dejar nada — parecería un brief y no lo es, y el checklist lo daría por cumplido.

Lo que falta no es dejarlo puesto: es **decir que falta**.

## Por qué importa más de lo que parece

El checklist es lo que el agente lee en cada mensaje para saber si el entorno está completo. Mientras diga «completo» con la cadena vacía, está afirmando algo que `F0` contradice, y el proyecto se entera cuando ya hay código escrito — que es cuando la trazabilidad hacia atrás cuesta.

## Relación con otros pendientes

- **[01 · Validadores de código de proyecto](01-validadores-de-codigo-de-proyecto.md)** — ahí viven las puertas de flujo. Si esto se resuelve como validador y no como componente, es parte del 01.
- **[20 · `F2` no dice cuándo no aplica](20-f2-no-dice-cuando-no-aplica.md)** — mismo tipo de hueco, un eslabón más abajo: una regla de cadena que la práctica salta con buenos motivos y el estándar no contempla. Conviene mirarlos juntos: puede que `F0` también necesite decir qué pasa con lo que ya se construyó antes de que existiera la cadena.
