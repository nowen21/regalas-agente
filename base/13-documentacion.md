# 13 · Documentación  ·  `[CAPA 2]`

El chat se pierde y el contexto se comprime; los archivos quedan. Documentar es parte del entregable. La capa 3 declara ubicación, nombres y estructura.

---

## DOC1 · Persiste el trabajo de cada unidad completada

Al cerrar, guarda en documentación versionada: **qué se planeó** (el plan aprobado), **qué se probó** (escenarios + verificaciones manuales que el entorno automático no cubre — `08` · T4), **qué quedó** (cómo usarlo, puntos de entrada, enlaces al código). El chat no sustituye los archivos.

```
INCORRECTO: implementar, mostrar todo en el chat y cerrar
CORRECTO:   implementar + persistir plan, pruebas y resultado
```

## DOC2 · Documenta las decisiones no obvias y su porqué

**Documenta:** reglas de negocio, decisiones de diseño que no se ven en el código (por qué X y no Y), convenciones del módulo, dónde se aplica cada regla (enlace a archivo y línea).
**No documentes:** cómo funciona el código línea por línea, ni lo obvio de leer el archivo.

```
INCORRECTO: comentar el porqué en el código y confiar en que lo relean
CORRECTO:   registrar la decisión y su motivo en la doc, enlazando al código
```

## DOC3 · Verifica la trazabilidad spec → implementación antes de cerrar

Revisa ítem por ítem que cada afirmación técnica de la spec (`02` · F2) esté en el código, el esquema, las pruebas y los docs. No cierres con faltantes sin justificar.

Formato: una tabla persistida en el documento de resultado, una fila por afirmación:

| Ítem de la spec | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la spec) | (esquema/modelo/servicio/vista/prueba/permiso/ruta/doc) | (archivo real) | ✅ / ❌ / N/A / parcial | (enlace o prueba) |

Faltante, parcial y N/A llevan justificación. Si al revisar una unidad cerrada aparece un faltante, se corrige **en su lugar** y se actualiza la tabla.

```
INCORRECTO: "pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + tabla de trazabilidad sin faltantes → cierro"
```

## DOC4 · Documenta lo que producción necesita

Los pasos de despliegue (cambios de esquema, datos base, permisos, comandos post-deploy) se documentan **auto-suficientes y ejecutables**. Quien despliega lo hace leyendo el entregable, sin volver a mirar el código.

---

Ver: `02` F1/F2/F6/F7, `08` (plan de pruebas y verificaciones manuales), `07` Q5 (documentar, no solo comentar), `11` CFG3.
