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

## DOC5 · Registrar señales (memoria) — *opt-in*

Guardar las **señales** de alto valor que **no se pueden recuperar del código**. Una señal = **what / why / where / learned** + un **tipo** (`decisión`, `error-resuelto`, `patrón`, `aprendizaje`, `alternativa-descartada`, `supuesto`, `restricción`, `pregunta-abierta`, `gotcha`, `deuda-técnica`) + un **scope** (a quién sirve: proyecto o toda la organización).

**Dónde se guardan (backend — lo elige la capa 3, uno solo):**
- **Archivo** `documentacion/senales.md` (versionado, simple) — plantilla `plantillas/senales.md`. Para pocas señales.
- **Base central buscable** `memoria/` (SQLite+FTS5, con `scope`, buscable y compartida entre proyectos) — se opera con la skill `usar-memoria`; es data local, no se versiona. Para muchas señales.

Guardan la **misma** señal; se elige por volumen (ver [`notas/memoria-por-senales.md`](../notas/memoria-por-senales.md)). **Opt-in**: se activa cuando la capa 3 declara el backend (el `CLAUDE.md` del proyecto).

- **No borrar** una señal revertida: marcarla `reemplazada` y enlazar la nueva (rastro, como `## Decisiones` clásico).
- **Verificar antes de confiar:** una señal vieja puede estar obsoleta (`01`·C2).
- Es la defensa contra "la compactación mata decisiones": la señal vive en la memoria, no en el chat.

```
INCORRECTO: la decisión "elegimos X y no Y porque Z" queda solo en el chat → se pierde al compactar
CORRECTO:   se registra como señal (decisión) en la memoria con what/why/where/learned
```

---

Ver: `02` F1/F2/F6/F7, `08` (plan de pruebas y verificaciones manuales), `07` Q5 (documentar, no solo comentar), `11` CFG3.
