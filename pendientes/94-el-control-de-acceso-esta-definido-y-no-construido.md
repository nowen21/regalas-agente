# Pendiente · El control de acceso está definido y no construido

> **Este pendiente es del producto, no del cuerpo de reglas.** Entra por acá porque es el camino que la etapa de análisis dejó escrito en su sección 11: un cambio a lo ya acordado se pide como pendiente, el agente dice a qué le pega, y el usuario aprueba.

**Estado:** abierto, anotado el 2026-09-02.

| | |
|---|---|
| **Historia de usuario** | Por crear. Sale de este pendiente cuando se apruebe |
| **De dónde sale** | El usuario lo vio leyendo el manual de uso, el 2026-09-02: *«el que yo lo use no significa que no pueda tener seguridad»* |
| **Proyecto de origen** | Cimiento, como producto |

## El problema

**El análisis ya definió los permisos.** Su sección 6 tiene una tabla de cuatro actores con qué hace cada uno y qué no puede hacer, incluido que **quien recibe un proyecto no entra a la plataforma**.

**El diseño los aplazó, y dijo hasta cuándo.** Su sección 8 dice *«un solo usuario en esta versión, sin credenciales propias: quien tenga la máquina, entra»*, y a continuación:

> El día que la plataforma corra en un servidor, esta sección se rehace entera. Con un solo usuario en su máquina, no tener credenciales es razonable; **con dos, es una falla.**

**Y no hay nada construido.** Medido el 2026-09-02: `django.contrib.auth` no está instalada, no hay ninguna vista con `login_required`, no hay ni un permiso en el código, y ninguna de las siete pantallas pregunta quién entra.

## Por qué importa

**No bloquea hoy y por eso es fácil de posponer.** Con una persona en una máquina, el aplazamiento se sostiene.

Lo que lo vuelve urgente es otro requisito ya acordado: **`RNF-09` pide que la plataforma pueda correr en un servidor sin rehacer la aplicación.** El día que eso pase —y es un requisito, no una idea— el sistema queda abierto a cualquiera que alcance el puerto, con permiso para aprobar documentos, derogar reglas y publicar versiones.

**Y hay un segundo daño, más callado.** El campo `--quien "Nombre"` de `aprobar` se escribe y no se comprueba. Una aprobación registrada así **dice quién la dio, y no lo prueba**. Mientras haya una persona da igual; con dos, la firma deja de valer justo cuando empieza a hacer falta.

## Qué NO es el problema

Conviene separarlo, porque es donde el agente se equivocó al documentarlo:

- **Los datos sí están cuidados.** No se guardan credenciales (`RNF-05`, con un módulo que las tapa) ni datos de personas (`RNF-06`), y toda acción queda registrada sin poder editarse (`RNF-12`).
- Lo que falta es **el control de acceso**: quién entra y qué puede hacer.

## Qué falta

1. **Decidir el alcance.** No es lo mismo una clave para abrir la plataforma que los cuatro perfiles del análisis con sus permisos. El diseño ya nombra la segunda como la candidata `C-2` del inventario.
2. **Rehacer la sección 8 del diseño**, que ella misma dice que se rehace entera.
3. **Construirlo**, con su historia y su fase.
4. **Que `quién` deje de ser un campo de texto** en las aprobaciones, y pase a salir de quien entró.

## El límite

**Esto no se ejecuta desde este archivo.** Baja a historia de usuario y se construye como fase, con su plan y sus pruebas (`02·F23`).

## A qué le pega

| Qué | Cómo |
|---|---|
| `cvds/diseno/README.md` §8 | Se rehace entera |
| `cvds/analisis-requisitos/README.md` §6 | Ya está escrito; pasa de definido a exigible |
| Las catorce `spec.md` | Su sección 8 dice hoy «un solo usuario, sin credenciales propias» |
| El módulo Aprobaciones | `quién` deja de ser un campo que se escribe |
| `manuales/manual-de-usuario.md` §9 | Se reescribe cuando exista |
