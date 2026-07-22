# 11 · Configuración y entornos

Lo que cambia entre entornos (local, pruebas, producción) y lo que se configura sin tocar código. La capa 3 declara los entornos y el mecanismo concretos.

---

## CFG1 · La configuración vive fuera del código

Lo que cambia entre entornos (credenciales, URLs, claves, flags de entorno) se lee de la **configuración de entorno**. El mismo código corre en todos lados; cambia la config que recibe. Secretos, nunca en el código (`00` · N6, `04` · S4).

> Esto es config de **infraestructura**. Los valores **del negocio** que un admin cambiaría (umbrales, listas, textos) van a **catálogo en la BD** (`03` · D4).

```
INCORRECTO: la URL del servicio de pago en el código con un if por entorno
CORRECTO:   leerla de la configuración; cada entorno trae la suya
```

## CFG2 · El entorno real no se versiona; sí una plantilla

El archivo con valores reales está **ignorado** (`09` · G3). Se versiona una **plantilla de ejemplo** con todas las variables **sin valores**, y se documenta qué es cada una y cuáles son obligatorias.

```
INCORRECTO: versionar el archivo de entorno con las claves reales
CORRECTO:   versionar la plantilla vacía; el real queda en cada entorno
```

## CFG3 · Paridad entre entornos

Los entornos se parecen lo más posible (mismas versiones, misma config estructural) para que "funciona en mi máquina" signifique algo. Lo que pruebas no puede reproducir se cubre con **verificaciones manuales documentadas** (`08` · T4). Los cambios que producción necesita se **documentan** (`13`), no se aplican de memoria.

## CFG4 · Cambios de comportamiento tras banderas

Funcionalidad que conviene activar/desactivar sin desplegar (en progreso, arriesgada, de un cliente) va tras una **bandera** (feature flag): permite apagar rápido sin revertir código. Limpia las banderas obsoletas — una eterna es deuda.

---

Ver: `00` N6 (secretos), `04` S4, `09` G3 (plantilla versionada), `03` D4 (negocio → catálogo), `08` T4 / `13` (diferencias documentadas).
