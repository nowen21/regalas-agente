# 11 · Configuración y entornos

> **Capa 2 · agnóstica al stack.** Cómo se maneja lo que cambia entre entornos (local, pruebas, producción) y lo que se configura sin tocar código. La capa 3 declara los entornos concretos y el mecanismo de configuración.

---

## CFG1 · La configuración vive fuera del código

Todo lo que cambia entre entornos (credenciales, URLs de servicios, claves de API, banderas de entorno) se lee de la **configuración de entorno**, no se "quema" en el código.

- El mismo artefacto de código corre en todos los entornos; lo que cambia es la configuración que recibe.
- Los **secretos** en configuración de entorno, nunca en el código (blindado en `00` · N6; ver `04-seguridad.md` S4).

> Esto se refiere a la configuración **de infraestructura/entorno**. Los valores **del negocio** que un administrador podría cambiar (umbrales, listas, textos) van a **catálogo en la BD**, no a variables de entorno (`03-datos.md` D4).

```
INCORRECTO: la URL del servicio de pago escrita en el código con un if por entorno
CORRECTO:   leer la URL de la configuración de entorno; cada entorno trae la suya
```

---

## CFG2 · El archivo de entorno real no se versiona; sí una plantilla

- El archivo con los valores reales (y sus variantes con secretos) está **ignorado** por el control de versiones (`09-git.md` G3).
- Se versiona una **plantilla de ejemplo** que lista todas las variables necesarias **sin valores reales**, para que cualquiera sepa qué configurar al montar el proyecto.
- Documentar qué significa cada variable y cuáles son obligatorias.

```
INCORRECTO: versionar el archivo de entorno con las claves reales
CORRECTO:   versionar una plantilla vacía; el archivo real queda solo en cada entorno
```

---

## CFG3 · Paridad entre entornos

Los entornos deben parecerse lo más posible para que "funciona en mi máquina" signifique "funciona". Reducir las diferencias entre desarrollo, pruebas y producción (mismas versiones de dependencias, misma configuración estructural).

- Cuando el entorno de pruebas **no** puede reproducir una peculiaridad de producción, se compensa con **verificaciones manuales documentadas** (ver `08-pruebas.md` T4), no ignorando la diferencia.
- Los cambios de esquema y de configuración que producción necesita se **documentan** como parte del entregable (`13-documentacion.md`), no se aplican de memoria.

---

## CFG4 · Cambios de comportamiento detrás de banderas

Cuando se introduce funcionalidad que conviene poder activar/desactivar sin desplegar código (una feature en progreso, un cambio arriesgado, algo específico de un cliente), se controla con una **bandera de configuración** (feature flag).

- Permite desactivar rápido si algo sale mal, sin revertir código.
- Limpiar las banderas obsoletas una vez que la funcionalidad se estabiliza: una bandera eterna es deuda.

---

## Relación con el resto del estándar

- **Núcleo `00` · N6** — los secretos nunca se exponen ni se versionan.
- **`04-seguridad.md` S4** — gestión de secretos en configuración de entorno.
- **`09-git.md` G3** — el archivo de entorno real no se versiona; sí la plantilla.
- **`03-datos.md` D4** — los valores del negocio van a catálogo, no a variables de entorno.
- **`08-pruebas.md` T4 / `13-documentacion.md`** — diferencias de entorno → verificación manual documentada.
