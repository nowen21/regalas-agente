# Los porqués que se recortaron de los capítulos 18 y 19

**Qué es esto.** `20·M5` da cuatro líneas por regla y manda el porqué a `notas/`. El 2026-08-22 (pendiente 19) cinco reglas de los capítulos `18` y `19` se recortaron al molde; lo que sobraba no era exigencia sino explicación, y queda acá para que no se pierda.

| Regla | Lo que se recortó |
|---|---|
| `18·DP8` | «La identidad del agente es desarrollador senior, no SRE.» Operar el sistema vivo, vigilar tableros y responder incidentes en caliente es del humano; la regla solo conserva que lo prepara y espera la autorización. |
| `19·OB1` | «Sin estructura, un log a escala no se puede buscar ni agregar.» Es el motivo de exigir datos en vez de texto libre. |
| `19·OB3` | «Una alerta que se ignora siempre es peor que ninguna.» Es el motivo de alertar por síntoma y no por ruido: el ruido enseña a silenciar. |
| `19·OB5` | El tipo de señal sugerido (`error-resuelto` o `aprendizaje`) y el molde del postmortem; la regla conserva que se escribe y que se registra. |
| `19·OB6` | «La identidad es desarrollador senior, no SRE de guardia.» El mismo porqué de `DP8`, dicho desde la operación. |

Lo que no se recortó en ninguna: la exigencia, el ejemplo y las dependencias declaradas.
