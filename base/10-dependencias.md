# 10 · Dependencias de terceros

Cada dependencia es código ajeno que heredas: sus bugs, vulnerabilidades, mantenimiento y licencia. La capa 3 declara el gestor de paquetes y las herramientas de auditoría.

---

## DEP1 · Agregar una dependencia es una decisión

Antes de sumar una librería: ¿la necesito o lo resuelvo con lo que ya tengo? ¿Está **mantenida** y es confiable? ¿Su **licencia** es compatible? ¿Cuánto **peso** y cuántas transitivas arrastra? Es una decisión funcional: el agente la **propone**, no la mete por su cuenta (`01` · C4).

```
INCORRECTO: sumar una librería pesada para formatear una fecha en un solo lugar
CORRECTO:   resolverlo con la utilidad estándar
```

## DEP2 · Versiones fijadas y reproducibles

Fija versiones con el **lockfile** del ecosistema y **versiónalo**: todos (y producción) instalan lo mismo. No dependas de "la última" flotante. Actualiza **deliberado**, revisando cambios.

```
INCORRECTO: no versionar el lockfile → cada máquina instala versiones distintas
CORRECTO:   versionarlo → instalación idéntica en todos lados
```

## DEP3 · Audita vulnerabilidades y mantén al día

Revisa **vulnerabilidades conocidas** con la herramienta del ecosistema (`04` · S7). No dejes una dependencia con vulnerabilidades sin resolver. Quedarse muy atrás vuelve caro e inseguro actualizar después.

## DEP4 · No versiones lo instalado

Las dependencias instaladas (carpetas de paquetes, binarios) no van al control de versiones (`09` · G3): se reconstruyen del manifiesto + lockfile. Versiona la **declaración**, no el **resultado**.

```
INCORRECTO: commitear la carpeta de dependencias instaladas
CORRECTO:   versionar manifiesto + lockfile; ignorar la carpeta instalada
```

## DEP5 · Aísla la dependencia que puede cambiar

Una dependencia central y sustituible (cliente de pago, proveedor de correo) se **encapsula** detrás de una interfaz propia, en vez de esparcir llamadas directas. Cambiar de proveedor toca un punto, no cien. No lo sobre-apliques a utilidades estables y ubicuas.

---

Ver: `04` S7 (vulnerabilidades), `09` G3 (no versionar lo instalado), `01` C4 (se consulta), `11` (instalación reproducible).
