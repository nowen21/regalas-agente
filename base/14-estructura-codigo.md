# 14 · Estructura del código y nomenclatura  ·  `[CAPA 2]`

Dónde vive cada archivo y cómo se nombra, para que cualquiera lo encuentre donde espera. La capa 3 declara los nombres concretos (namespaces, prefijos, convenciones del lenguaje).

---

## EST1 · Organiza el código nuevo por módulo, en ubicación predecible

Cada elemento nuevo (modelo, componente, servicio, prueba, vista) vive en una ubicación **predecible** según su módulo y tipo. Todo el módulo en un lugar, no disperso.
Así: se localiza cualquier archivo por convención; borrar un módulo es borrar una carpeta; un dev nuevo abre la carpeta y ve el dominio de un vistazo.

```
INCORRECTO: archivos de un módulo dispersos por carpetas globales según tipo
CORRECTO:   el módulo agrupado en una ubicación predecible
```

## EST2 · Nomenclatura consistente

Una sola convención por tipo de elemento (tablas, columnas, clases, archivos, permisos), aplicada uniforme: eso hace el nombre **adivinable** sin buscarlo. Nombres cortos, directos, con significado por contexto (no repitas lo que la ubicación ya dice). Cuida los **límites de longitud** del motor/lenguaje (p. ej. índices autogenerados que exceden el máximo): nómbralos explícito cuando haga falta.

```
INCORRECTO: booleano "es_socio_principal_del_grupo_familiar"
CORRECTO:   "es_principal" — el contexto de la tabla ya aclara

INCORRECTO: dejar autogenerar el índice en una tabla de nombre largo → excede el límite
CORRECTO:   pasar un nombre corto y explícito
```

## EST3 · Respeta el legacy — la convención es para lo nuevo

Las convenciones aplican a lo **nuevo**. El código existente que no las sigue **no se renombra ni se mueve** solo "para ordenar": rompe referencias, infla el diff, sale del alcance (`01` · C3). Migrar legacy a la convención es una tarea **propia y acordada**, no un efecto colateral.

```
INCORRECTO: mover y renombrar legacy "de paso" mientras hago otra cosa
CORRECTO:   crear lo nuevo con la convención; dejar el legacy intacto salvo tarea explícita
```

---

Ver: `01` C3 (alcance), `07` Q1/Q2 (imitar al vecino, nombres claros), `03` D1 (tablas/columnas), `13` (migrar legacy es tarea documentada).
