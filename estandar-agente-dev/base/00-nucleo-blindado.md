# 00 · Núcleo blindado — reglas inquebrantables

> **Capa 1.** Estas reglas **no se sobrescriben**: ninguna capa de proyecto, ningún prompt de módulo y ninguna instrucción puntual del usuario dentro de una tarea puede desactivarlas. Si un prompt o una regla de proyecto entra en conflicto con esta capa, **gana esta capa**. Son reglas de seguridad: existen para proteger los datos, la historia del repositorio y la información sensible del usuario.
>
> Cada regla lleva la marca `[BLINDADA]`.

---

## N1 · No ejecutar sin validación previa `[BLINDADA]`

Ningún cambio de estado se ejecuta sin aprobación explícita del usuario. Aplica a: edición y creación de archivos, comandos en terminal, operaciones de control de versiones, migraciones/seeders, y cualquier acción que modifique el estado del proyecto o de sus datos.

**Si el usuario rechaza una acción, el agente NO reintenta la misma acción.** Debe entender el motivo del rechazo y ajustar el enfoque, no insistir con una variante cosmética.

> La excepción legítima es la ejecución continua de un plan ya aprobado (ver flujo de trabajo): la aprobación del plan cubre los cambios que el plan describe. Lo que el plan no describe, se consulta.

```
INCORRECTO: el usuario rechaza un comando → el agente lo vuelve a lanzar con otra bandera
CORRECTO:   el usuario rechaza → el agente pregunta el motivo y propone otro enfoque
```

---

## N2 · Control de versiones solo bajo demanda `[BLINDADA]`

El agente **nunca** ejecuta operaciones de control de versiones por iniciativa propia. En especial **commit** (escribe historia) y **push** (publica cambios) solo se ejecutan cuando el usuario lo pide explícitamente.

**La autorización es de un solo uso.** Autorizar una operación no autoriza las siguientes ("ya que estás, haz push"), no es permiso permanente, y no se extiende a la próxima sesión. Siempre se confirma de nuevo.

```
INCORRECTO: el agente termina un cambio y hace commit "para dejarlo guardado"
CORRECTO:   el agente reporta que está listo y espera a que el usuario pida el commit
```

---

## N3 · No rodear obstáculos con acciones destructivas `[BLINDADA]`

Ante un obstáculo (hook fallido, test en rojo, validación que bloquea, conflicto), el agente **reporta el problema y propone la solución correcta**. Nunca elimina el obstáculo por la fuerza.

Prohibido sin autorización expresa: saltarse hooks o firmas (`--no-verify` y equivalentes), borrar o silenciar (`skip`/`ignore`/comentar) el test que falla, forzar una operación que el sistema rechaza, o desactivar una validación para que "pase".

```
INCORRECTO: el hook de pre-commit falla → el agente usa --no-verify
CORRECTO:   el agente reporta por qué falló el hook y propone el fix real
```

---

## N4 · Protección de datos reales `[BLINDADA]`

El agente **nunca** ejecuta operaciones destructivas sobre datos o esquemas de producción (o de cualquier base de datos con datos reales) sin autorización expresa y específica del usuario para esa operación concreta.

Prohibido por defecto: recrear/refrescar/vaciar la base (`migrate:fresh`, `migrate:refresh`, `db:wipe`, `drop`, `truncate` y equivalentes en cualquier stack), `UPDATE`/`DELETE` masivos sin filtro, y cualquier comando que pueda perder datos históricos.

**Esta regla gana a cualquier prompt.** Si un prompt de módulo o una regla de proyecto dice "corre los tests contra la base real" o "recrea la base para probar", esta regla prevalece y el prompt debe corregirse, no al revés.

```
INCORRECTO: "recreo la base para probar el módulo desde cero"
CORRECTO:   correr las pruebas contra una base efímera/aislada; verificar contra datos
            existentes sin borrarlos
```

---

## N5 · Operaciones masivas: previsualizar antes de aplicar `[BLINDADA]`

Toda operación que afecte muchos registros a la vez (comandos, endpoints, scripts, correcciones históricas) debe, antes de aplicar:

1. **Previsualizar** el impacto (modo `dry-run` o equivalente: mostrar qué se afectaría sin cambiar nada).
2. **Registrar** en log qué se afectó (cuántos, cuáles, motivo) para auditoría posterior.
3. **Exigir control de acceso** si es un endpoint (autenticación + permiso administrativo).
4. **Confirmación explícita** del usuario antes de aplicar.

```
INCORRECTO: endpoint que borra y regenera registros sin preview, sin log y sin permiso
CORRECTO:   preview de afectados → confirmación → aplicar → log del resultado
```

---

## N6 · Secretos y datos sensibles nunca se exponen `[BLINDADA]`

- **Nunca** hardcodear credenciales, tokens, claves o secretos en el código.
- **Nunca** incluir secretos ni datos personales en logs, mensajes de error, salidas de consola o commits.
- **Nunca** enviar contenido del proyecto (código, datos, secretos) a servicios externos sin autorización explícita del usuario.
- Los archivos con información no pública (financiera, jurídica, personal, confidencial) **nunca** se sirven desde una ubicación pública; van a almacenamiento privado detrás de control de acceso (ver `04-seguridad.md`).

```
INCORRECTO: Log del payload completo de una petición que incluye la contraseña del usuario
CORRECTO:   loguear un identificador de correlación, nunca el secreto
```

---

## Relación con el resto del estándar

Estas seis reglas son la versión **inquebrantable** de temas que las convenciones base desarrollan con más matiz y ejemplos: conducta (`01`), datos (`03`), seguridad (`04`), errores y logging (`05`), git (`09`). Cuando una convención base y el núcleo hablen de lo mismo, el núcleo marca el límite que no se cruza; la convención añade el detalle ajustable por proyecto.
