# 13 · Documentación

> **Capa 2 · agnóstica al stack.** Cómo persistir el trabajo y las decisiones para que sobrevivan a la sesión. El chat se pierde y el contexto se comprime; los archivos quedan. Documentar no es opcional: es parte del entregable. La capa 3 declara la ubicación, el formato de nombres y la estructura de carpetas concretos.

---

## DOC1 · Persistir el trabajo de cada unidad completada

Al cerrar una unidad de trabajo (una fase, una funcionalidad, un cambio con plan), se persiste en documentación versionada, como mínimo:

- **Qué se planeó** — el plan de trabajo tal como se aprobó (archivos, cambios, alcance, decisiones).
- **Qué se probó** — el plan de pruebas (escenarios, casos, y las verificaciones manuales que el entorno automático no cubre — `08-pruebas.md` T4).
- **Qué quedó implementado** — el resultado: cómo usarlo, puntos de entrada, y enlaces al código relevante.

La presentación en el chat **no sustituye** estos archivos.

```
INCORRECTO: implementar, mostrar todo en el chat y cerrar
CORRECTO:   implementar + persistir plan, pruebas y resultado en documentación versionada
```

---

## DOC2 · Documentar las decisiones no obvias y su porqué

Toda regla de negocio, decisión de arquitectura o patrón no evidente se documenta, con **el porqué**.

**Qué documentar:**

- Reglas de negocio implementadas (validaciones, restricciones, flujos).
- Decisiones de diseño que no se ven en el código (por qué X en vez de Y).
- Convenciones específicas del módulo.
- Puntos del código donde se aplica una regla (con enlaces al archivo y línea).

**Qué NO documentar:**

- Cómo funciona el código línea por línea (eso lo dice el código).
- Lo obvio y derivable de leer el archivo.

```
INCORRECTO: comentar el porqué en el código y confiar en que alguien lo relea
CORRECTO:   registrar la decisión y su motivo en la documentación, enlazando al código
```

---

## DOC3 · Verificar la trazabilidad spec → implementación antes de cerrar

Antes de declarar terminada una unidad de trabajo, verificar **ítem por ítem** que cada afirmación técnica de la spec (`02-flujo-de-trabajo.md` F2) esté realmente reflejada en el código, el esquema, las pruebas y los docs. No se cierra con ítems faltantes sin justificar.

**Formato sugerido** — una tabla persistida en el documento de resultado, con una fila por afirmación técnica de la spec:

| Ítem de la spec | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la spec) | (esquema / modelo / servicio / vista / prueba / permiso / ruta / doc) | (archivo real) | ✅ / ❌ / N/A / parcial | (enlace al código o prueba) |

- Los estados **faltante**, **parcial** y **no aplica** llevan justificación explícita.
- Si al revisar una unidad ya cerrada aparece un faltante, se corrige **en su lugar** (no se abre una unidad nueva) y se actualiza la tabla.

**Por qué:** sin este chequeo, una regla explícita de la spec ("el selector se filtra por X") se pierde en el ruido de un plan largo y reaparece meses después como bug. La spec es el contrato; la tabla es la prueba de que se cumplió.

```
INCORRECTO: "todas las pruebas verdes → cierro"
CORRECTO:   "pruebas verdes + tabla de trazabilidad sin faltantes → cierro"
```

---

## DOC4 · Documentar lo que producción necesita

Cuando un cambio requiere pasos para desplegarse (cambios de esquema, datos base, permisos nuevos, comandos post-despliegue), esos pasos se documentan de forma **auto-suficiente y ejecutable**, no se reconstruyen de memoria en cada despliegue. Quien despliega debe poder hacerlo leyendo el entregable, sin volver a mirar el código.

---

## Relación con el resto del estándar

- **`02-flujo-de-trabajo.md` F1/F2/F6/F7** — cargar contexto documentado, spec como línea base, persistir, trazabilidad.
- **`08-pruebas.md`** — el plan de pruebas y las verificaciones manuales se documentan aquí.
- **`07-calidad-de-codigo.md` Q5** — las decisiones no obvias se documentan, no solo se comentan.
- **`11-configuracion-entornos.md` CFG3** — los cambios que producción necesita se documentan.
