# 14 · Estructura del código y nomenclatura

> **Capa 2 · agnóstica al stack.** Dónde vive cada archivo y cómo se nombra, para que cualquiera encuentre las cosas donde espera. Los nombres concretos (namespaces, prefijos, convenciones del lenguaje) los declara la capa 3; aquí van los principios que la capa 3 instancia.

---

## EST1 · Organizar el código nuevo por módulo, en ubicación predecible

Cada elemento nuevo (modelo, componente, servicio, prueba, vista) vive en una ubicación **predecible** derivada de su módulo y su tipo. Todo el código de un módulo se encuentra en un lugar, no disperso.

Beneficios: se localiza cualquier archivo por convención; borrar un módulo es borrar una carpeta, no cazar archivos sueltos; un desarrollador nuevo abre la carpeta del módulo y ve el dominio de un vistazo.

> La capa 3 define el esquema exacto (cómo se traduce "módulo" y "tipo" a rutas y namespaces del stack).

```
INCORRECTO: archivos de un mismo módulo dispersos por carpetas globales según su tipo
CORRECTO:   todo el módulo agrupado en una ubicación predecible por convención
```

---

## EST2 · Nomenclatura consistente en todo el proyecto

Una sola convención para cada tipo de elemento (tablas, columnas, clases, archivos, permisos), aplicada de forma uniforme. La consistencia es lo que hace que un nombre sea **adivinable** sin buscarlo.

- Definir y respetar el estilo de cada tipo (p. ej. cómo se nombran tablas, clases, booleanos, marcas de tiempo, claves foráneas).
- Nombres **cortos, directos y con significado por contexto**: el nombre no repite lo que la ubicación ya dice.
- Cuidar los **límites de longitud** del motor/lenguaje (p. ej. nombres de índices y restricciones que se autogeneran y pueden exceder el máximo): nombrarlos explícitamente cuando haga falta.

```
INCORRECTO: un booleano llamado "es_socio_principal_del_grupo_familiar"
CORRECTO:   "es_principal" — el contexto de la tabla ya aclara de qué

INCORRECTO: dejar que se autogenere el nombre de un índice en una tabla de nombre largo
            → excede el límite del motor y falla
CORRECTO:   pasar un nombre corto y explícito al índice
```

---

## EST3 · Respetar el código legacy — la convención aplica a lo nuevo

Las convenciones de estructura y nombres aplican a lo **nuevo**. El código existente que no las sigue **no se renombra ni se mueve** solo "para ordenar": eso rompe referencias, infla el diff y sale del alcance (`01-conducta.md` C3).

- Lo nuevo se crea siguiendo la convención; lo viejo se deja donde está y puede seguir usándose.
- Migrar código legacy a la convención es una tarea **propia y acordada**, no un efecto colateral de otra tarea.

```
INCORRECTO: mover y renombrar archivos legacy "de paso" mientras se hace otra cosa
CORRECTO:   crear lo nuevo con la convención; dejar lo legacy intacto salvo tarea explícita
```

---

## Relación con el resto del estándar

- **`01-conducta.md` C3** — no salir del alcance con reorganizaciones no pedidas.
- **`07-calidad-de-codigo.md` Q1/Q2** — el código nuevo imita al vecino; nombres que revelan intención.
- **`03-datos.md` D1** — la nomenclatura de tablas y columnas se apoya en el diseño de datos.
- **`13-documentacion.md`** — migrar legacy a la convención es una tarea documentada, no un efecto colateral.
