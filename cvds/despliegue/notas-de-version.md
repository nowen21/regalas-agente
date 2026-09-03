# Notas de versión   ·   `[CAPA 3]`

**Para qué sirve este documento.** Le cuenta a quien usa Cimiento qué trae cada versión: qué puede hacer ahora que antes no, qué cambió de lugar, y qué tiene que hacer para actualizarse. No es el [registro técnico de cambios](../../CHANGELOG.md) —ese es del cuerpo de reglas—: es la traducción para quien usa la plataforma.

> **Una advertencia antes de leer.** Las cinco versiones se cerraron entre el 2026-08-31 y el 2026-09-02, y **ninguna se entregó a nadie por separado**: la plataforma corre en la máquina de quien la escribió. Las fechas dicen cuándo quedó construida cada una, no cuándo alguien la recibió. Lo que sí es cierto es el orden: cada versión se construyó sobre la anterior.

---

## 5 · Operar el ciclo · 2026-09-02

**Ahora la plataforma abre fases, dice en cuál estación va cada una, avisa lo que se salió de lo acordado, y todo eso se puede mirar sin abrir una consola.**

**Nuevo:**

- **Abrir una fase con sus cinco documentos**, sin escribir el nombre a mano (`F-011`). El nombre lo arma la plataforma con la letra, la épica, la historia y de qué trata.
- **Ver en qué estación va cada fase** y qué puerta le falta (`F-012`). Sirve para mirar doscientas a la vez, que es lo que no se podía.
- **No dejar pasar sin la puerta cumplida** (`F-013`), diciendo cuál falta. Son tres puertas comprobables y no trece: una puerta que estorba se termina saltando.
- **Elegir qué reglas opcionales rigen en cada proyecto** (`F-004`). De las 257 reglas del estándar, **49 son opcionales**; las demás rigen siempre y no se pueden apagar.
- **Los avisos de lo que se desvía** (`F-029`) y **el reporte de cómo va cada proyecto** (`F-030`).
- **Cuánto tiempo se gasta revisando** (`F-032`), sacado de las horas que ya quedan escritas: nadie cronometra nada.
- **Cinco pantallas**: el tablero, las fases, las funcionalidades, las aprobaciones y la memoria.

**Cambió:**

- El lector de fases aprendió que **hay dos marcas de «cumplida»** y **tres modelos de tabla** conviviendo. Ninguna fase vieja se reescribió.

**Corregido:**

- El expediente reportaba documentos faltantes que existían, y contaba huecos que eran citas de la marca. Los dos salían de contar sobre una copia vieja o con reglas propias.

**Para actualizarse:** nada. La plataforma corre desde su propia carpeta y no guarda nada que haya que migrar, salvo una tabla nueva de la versión 4.

---

## 4 · Dejar constancia · 2026-09-01

**Ahora una aprobación dice sobre qué texto se dio, y caduca cuando ese texto cambia.**

**Nuevo:**

- **Aprobar un documento guardando la huella de su texto** (`F-015`). Antes las aprobaciones se escribían a mano y ninguna decía sobre qué.
- **Ver qué está aprobado y qué no** (`F-016`), con palabras y no con color: aprobado, caducada, sin aprobación.
- **Caducar la aprobación cuando el texto cambia** (`F-017`), diciendo cuánto cambió. **La aprobación anterior no se borra.**
- **Buscar en la auditoría** por proyecto, fecha y tipo de acción (`F-019`).
- **Guardar lo aprendido y devolverlo después** (`F-023`), y **consultarlo y corregirlo** (`F-024`). Corregir conserva lo que decía antes; dar de baja marca y no borra.

**Corregido:**

- El rango de fechas de la auditoría cortaba el último día en la medianoche, y devolvía resultados que parecían completos.

**Para actualizarse:** hay **una migración**, la de la tabla de aprobaciones. Se aplica sola al arrancar.

---

## 3 · Gobernar al agente · 2026-09-01

**Ahora las reglas se escriben, numeran, derogan y publican desde la plataforma, y lo exigido se comprueba solo.**

**Nuevo:**

- **Escribir, cambiar y derogar reglas** (`F-005`), con el identificador asignado **sin reutilizar ninguno** (`F-006`).
- **El sello del checklist de cada regla** (`F-007`), **publicar una versión del cuerpo** (`F-008`), **entregárselo al agente al abrir sesión** (`F-009`) y **avisar al proyecto que quedó atrás** (`F-010`).
- **Comprobar solo lo que las reglas exigen** (`F-020`) y **declarar sin verificar lo que no tiene prueba** (`F-021`).
- **Comprobar que lo nuevo no rompió lo anterior** antes de publicar (`F-022`).
- **Correr las pruebas del propio estándar** (`F-031`): 650 pruebas que existían y no corría nadie.

**Corregido:**

- El aviso de «qué cambió desde entonces» llevaba **54 versiones saliendo vacío**.

**Para actualizarse:** nada.

---

## 2 · Entregar · 2026-08-31

**Ahora el expediente de un proyecto se arma y se entrega el mismo día.**

**Nuevo:**

- **Llenar los documentos del ciclo desde la plataforma** (`F-014`), hueco por hueco, escribiendo en el archivo original del proyecto.
- **Armar el expediente** (`F-025`) y **generar el entregable de ofimática** (`F-026`).
- **Guardar las conversaciones donde se pueda buscar** (`F-033`) y **ver qué correcciones se repiten** (`F-034`). Una corrección que se repite no es un descuido: es una regla que falta.

**Para actualizarse:** nada.

---

## 1 · Ver lo que hay · 2026-08-31

**La primera versión: conectar proyectos, traer lo que ya tienen escrito, y ver cómo van sin entrar a ellos.**

**Nuevo:**

- **Conectar un proyecto** (`F-001`) y **avisar cuando su ruta se pierde** (`F-002`).
- **Ver el estado de un proyecto sin entrar a él** (`F-003`) y **administrarlo** (`F-035`): desconectar, reconectar, renombrar y corregir.
- **Traer un proyecto con lo que ya tenga escrito** (`F-027`) y **reportar qué de lo traído no sigue ningún molde** (`F-028`).
- **Registrar cada acción que se hace** (`F-018`), con la constancia antes que el efecto.

**Para actualizarse:** es la primera. Se instala y se conecta el primer proyecto.

---

## Lo que ninguna versión trae todavía

- **Seis módulos no tienen pantalla:** Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén. Se operan por consola.
- **Nada se cambia desde la pantalla.** Aprobar, corregir un recuerdo o abrir una fase son cambios de estado y van por consola, con su confirmación.
- **No hay límite de intentos al entrar**, ni recuperación de contraseña por correo. El control de acceso sí está: cuentas, dos grupos y permisos, desde el 2026-09-02.
