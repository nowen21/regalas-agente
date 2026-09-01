# Especificación del módulo Comprobaciones  ·  `[CAPA 3]`

- **Slug del módulo:** `comprobaciones`
- **Estado:** aprobada, el 2026-09-01 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 3, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Decir si un proyecto cumple lo que las reglas exigen, **sin corregir nada**.

- **Dentro de alcance:** correr las comprobaciones del estándar contra un proyecto conectado y dar el veredicto con archivo y línea (`F-020`); fijar el estado de una funcionalidad desde la evidencia (`F-021`); y volver a correr lo que ya funcionaba antes de publicar (`F-022`).
- **Fuera de alcance:** corregir lo que encuentra, escribir comprobaciones nuevas, y la pantalla.

## 2. Contexto — qué hay hoy

El estándar tiene **32 comprobaciones** y **733 pruebas**, y funcionan. **La plataforma no usa ninguna:** para saber si un proyecto cumple hay que abrir su carpeta y correrlas ahí.

Es la misma forma que ya tienen otros dos puentes de la plataforma: el que tapa credenciales y el que parte una conversación en turnos. Ninguno duplica lo que el estándar sabe hacer.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que el proyecto conectado tiene el estándar instalado. Si no lo tiene, **se dice en vez de dar veredicto**.
- **Dependencias:** Proyectos, que sabe dónde vive cada uno; el estándar, que aporta las comprobaciones.
- **La vuelta de la columna:** `F-008` espera a `F-022`, que espera a `F-020`, que espera a `F-008`. No bloquea: lo que hay que comprobar ya existe escrito en `base/`, y no hace falta que la plataforma lo publique.

## 4. Reglas de negocio

1. **Se comprueba, no se corrige.** Las comprobaciones leen y dicen.
2. **Lo que no cumple se dice con su archivo y su línea.** Un veredicto sin ubicación no se puede atender.
3. **Apuntada a algo que no le corresponde, se dice.** Un proyecto sin el estándar instalado no está en verde: está sin comprobar, y son cosas distintas.
4. **Las comprobaciones no se duplican.** Viven en el estándar y se corren por su punto de entrada.
5. **Cero comprobaciones corridas no es verde.** Es lo mismo que no haber mirado.
6. **El veredicto no se guarda como verdad.** Se calcula al pedirlo: el proyecto cambia, y un veredicto guardado envejece sin avisar (`DA-01`).

## 5. Modelo de datos

- **Entidades:** ninguna. El veredicto se calcula al pedirlo.
- **Valores configurables:** dónde vive `validadores/`, que ya lo declara la configuración.
- **Migración:** no aplica.

### 5.1 Por qué se corren en un proceso aparte

**Se le pide al estándar por su punto de entrada**, que es como se corre de verdad: arma su contexto, descubre sus comprobaciones y las corre. Cargar sus archivos desde la plataforma daría un número que nadie más obtiene, y el día que el estándar cambie por dentro, la plataforma se rompe sin que nadie lo note.

Es la misma decisión que ya tomó el corredor del estándar para correr la batería de la plataforma. **Las dos direcciones usan el mismo criterio.**

## 6. Comportamiento y flujos

**Comprobar un proyecto.** Se recibe cuál. Se mira que exista su carpeta y que tenga el estándar instalado; si no, **se dice y no se da veredicto**. Si lo tiene, se corre el conjunto completo y se devuelve:

- **Cuántas comprobaciones corrieron**, y cuántas fallaron.
- **Cada falla con su archivo y su línea**, tal como el estándar las reporta.
- **Cuánto tardó**, porque una comprobación que tarda demasiado deja de pedirse.

Si corrieron **cero**, es rojo: cero no es verde.

## 7. Interfaz

Sin pantalla en esta versión. Se pide por orden de consola, como el resto de los módulos de esta etapa.

## 8. Permisos y autorización

Un solo usuario, sin credenciales propias.

## 9. Marco normativo

**No saca nada del sistema.** Lee la carpeta de un proyecto y devuelve un veredicto. Lo que sí aplica es que **la salida puede traer fragmentos de los archivos del proyecto**: si alguno trae una credencial, el mensaje la llevaría. Se tapa antes de mostrarla, con el mismo puente del módulo Seguridad.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Un proyecto que cumple | Pasa, y dice cuántas corrieron |
| Uno que no cumple | Se rechaza, **con archivo y línea** |
| Uno sin el estándar instalado | Lo dice, sin dar veredicto |
| Una carpeta que ya no está | Lo dice |
| Cero comprobaciones corridas | **Es rojo** |
| Que NO pase | Que comprobar modifique algún archivo |
| Sobre lo real | Este repositorio, con el tiempo medido |

## 11. Criterios de aceptación

- `CA-1` Un proyecto que cumple pasa.
- `CA-2` Uno que no cumple es rechazado, con archivo y línea.
- `CA-3` Apuntada a algo que no le corresponde, lo dice en vez de dar veredicto.
- `CA-4` Comprobar no modifica nada.
- `CA-5` Cero comprobaciones corridas es rojo.

Los cinco son de `F-020`. Los de `F-021` y `F-022` se agregan cuando lleguen sus historias.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **Se corren por su punto de entrada, en un proceso aparte** | Importar los módulos del estándar | Es como se corren de verdad; importarlos da un número que nadie más obtiene |
| **El veredicto se calcula al pedirlo** | Guardarlo | El proyecto cambia, y un veredicto guardado envejece sin avisar |
| **Sin el estándar instalado se dice, no se falla** | Devolver rojo | «Sin comprobar» y «no cumple» son cosas distintas, y confundirlas hace que nadie mire el rojo |
| **Cero comprobaciones es rojo** | Tratarlo como verde | Una corrida que no corrió nada y termina en verde es un silencio que se lee como éxito |
| **La salida se tapa antes de mostrarse** | Mostrarla tal cual | Puede traer fragmentos de archivos del proyecto, y uno de esos puede traer una clave |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-020 | RF-20 | [HU-001 Comprobar un proyecto desde la plataforma](../epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/HU-001-comprobar-un-proyecto-desde-la-plataforma.md) | [D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige](../epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige/estado-fase.md), cerrada el 2026-09-01 |
| F-021 | RF-21 | Por escribir | — |
| F-022 | RF-22 | Por escribir | — |

## 14. Cruces con otros módulos

- **Proyectos:** dice dónde vive cada proyecto y si su ruta sigue ahí.
- **Seguridad:** tapa la salida antes de mostrarla.
- **El estándar:** aporta las comprobaciones. Este módulo **no sabe** qué exige ninguna regla.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| — | — | — | — |
