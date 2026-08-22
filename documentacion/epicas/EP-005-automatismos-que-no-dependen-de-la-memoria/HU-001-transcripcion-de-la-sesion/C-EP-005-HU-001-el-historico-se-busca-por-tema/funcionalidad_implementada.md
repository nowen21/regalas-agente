# Funcionalidad implementada — Fase C-EP-005-HU-001-el-historico-se-busca-por-tema

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive.

## 0. Qué quedó, en una frase

**El histórico se puede buscar por tema:** los 345 hallazgos de los 59 resúmenes, en un archivo, cada uno enlazado a donde vive.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Los temas de todas las sesiones en un solo sitio | doc | `historico-chat/resumenes/indice-tematico.md` | ✅ | 345 hallazgos, 59 resúmenes |
| Cada tema enlaza a su resumen | prueba | `temas.py` | ✅ | `CP-02` |
| Se regenera en una línea | doc | `validar.py temas --aplicar` | ✅ | subcomando con su ayuda |
| Avisa cuando queda atrás, sin detener | prueba | `temas.py` | ✅ | `CP-06` |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.4.0 |

## 2. Lo que cambia para un proyecto que hereda

**Nada obligatorio.** El índice es de este repositorio; un proyecto que herede puede generar el suyo con el mismo subcomando, porque lee la estructura de resúmenes que el estándar ya instala.

## 3. Lo que queda abierto

**El disparo sigue siendo a mano.** Nadie lo regenera solo al cerrar la sesión; el aviso dice cuándo quedó atrás, que es el paso previo a automatizarlo según `20·M19`.

**Y seis resúmenes no tienen ningún hallazgo escrito.** El índice lo dice en su recuento; si es que esas sesiones no dejaron nada o que nadie lo escribió, es una pregunta para quien las revise.
