# Funcionalidad implementada — Fase B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive.

## 0. Qué quedó, en una frase

**El `README` heredado del histórico ya recibe lo que el estándar suma**, sin pisar una línea de lo que el proyecto escribió, y diciendo qué agregó.

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| El README heredado se completa | código | `validadores/instalar.py` | ✅ | `instalar_historico` usa el mecanismo aditivo y lo reporta |
| Nada de lo escrito se pisa | prueba | el test nuevo | ✅ | `CP-02` |
| Sin novedad no se toca nada | prueba | el mismo | ✅ | `CP-03` |
| Queda escrito qué manda entre el histórico y lo acordado | doc | `plantillas/historico-chat.md` | ✅ | sección nueva, que además viaja por el mecanismo recién construido |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.3.0 |

## 2. Lo que cambia para un proyecto que hereda

**Nada que hacer, y algo que se recibe:** la próxima vez que un proyecto corra el instalador, su `historico-chat/README.md` gana las secciones que el estándar haya sumado desde que se instaló, empezando por la que dice qué manda cuando el histórico y lo acordado se contradicen.

## 3. Lo que queda abierto

**Los demás documentos heredados siguen sin completarse.** El índice de la memoria y los archivos de `.agente/` se copian una vez y no reciben secciones nuevas. Se dejó fuera porque no hay evidencia de que se haya perdido nada por ahí; si aparece, es otra fase de esta historia.
