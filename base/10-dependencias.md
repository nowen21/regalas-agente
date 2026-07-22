# 10 · Dependencias de terceros

> **Capa 2 · agnóstica al stack.** Cuándo y cómo incorporar librerías externas. Cada dependencia es código ajeno que se hereda: sus bugs, sus vulnerabilidades, su mantenimiento y su licencia pasan a ser tuyos. La capa 3 declara el gestor de paquetes y las herramientas de auditoría concretas.

---

## DEP1 · Agregar una dependencia es una decisión, no un reflejo

Antes de sumar una librería, evaluar:

- ¿La necesito de verdad o resuelvo esto con lo que ya tengo (el framework, la librería estándar, unas pocas líneas)?
- ¿Está **mantenida** (releases recientes, issues atendidos), es **usada** y tiene **buena reputación**?
- ¿Su **licencia** es compatible con el proyecto?
- ¿Cuánto **peso** agrega y cuántas dependencias transitivas arrastra?

Agregar una dependencia es una decisión funcional: el agente la **propone**, no la incorpora por su cuenta (`01-conducta.md` C4).

```
INCORRECTO: sumar una librería pesada para formatear una fecha en un solo lugar
CORRECTO:   resolverlo con la utilidad estándar; reservar dependencias para lo que aporta valor real
```

---

## DEP2 · Versiones fijadas y reproducibles

- Fijar versiones mediante el **archivo de bloqueo** (lockfile) del ecosistema, y **versionarlo**: garantiza que todos (y producción) instalen exactamente lo mismo.
- No depender de "la última" versión flotante que puede cambiar sin aviso entre instalaciones.
- Actualizar dependencias de forma **deliberada** (revisando cambios), no arrastrado por una instalación descuidada.

```
INCORRECTO: no versionar el lockfile → cada máquina instala versiones distintas
CORRECTO:   versionar el lockfile → instalación idéntica y reproducible en todos lados
```

---

## DEP3 · Auditar vulnerabilidades y mantener al día

- Revisar periódicamente las **vulnerabilidades conocidas** con la herramienta de auditoría del ecosistema (ver `04-seguridad.md` S7).
- No introducir ni dejar una dependencia con vulnerabilidades sin resolver que afecten al proyecto.
- Mantener las dependencias razonablemente actualizadas: quedarse muy atrás vuelve costoso e inseguro actualizar después.

---

## DEP4 · No versionar lo instalado

Las dependencias instaladas (carpetas de paquetes, binarios descargados) **no van al control de versiones** (`09-git.md` G3): se reconstruyen desde el manifiesto y el lockfile. Se versiona la **declaración** (qué se necesita), no el **resultado** (los archivos descargados).

```
INCORRECTO: commitear la carpeta de dependencias instaladas
CORRECTO:   versionar el manifiesto + el lockfile; ignorar la carpeta instalada
```

---

## DEP5 · Aislar el acoplamiento a una librería que puede cambiar

Cuando una dependencia es central y podría reemplazarse en el futuro (un cliente de pago, un proveedor de correo, un motor de búsqueda), conviene **encapsular su uso** detrás de una interfaz propia del proyecto, en vez de esparcir llamadas directas por todo el código. Así, cambiar de proveedor toca un punto, no cien.

> No sobre-aplicar: para una utilidad estable y ubicua no hace falta envolver todo. Es para las dependencias sustituibles y de riesgo.

---

## Relación con el resto del estándar

- **`04-seguridad.md` S7** — las dependencias son superficie de ataque; auditar vulnerabilidades.
- **`09-git.md` G3** — no versionar lo instalado; sí el manifiesto y el lockfile.
- **`01-conducta.md` C4** — incorporar una dependencia es una decisión que se consulta.
- **`11-configuracion-entornos.md`** — la instalación reproducible es parte de la paridad entre entornos.
