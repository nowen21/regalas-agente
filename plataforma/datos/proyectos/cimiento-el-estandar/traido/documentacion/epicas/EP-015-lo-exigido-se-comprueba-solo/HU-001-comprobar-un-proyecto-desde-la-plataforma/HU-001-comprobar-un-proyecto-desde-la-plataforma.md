# HU-001 — Comprobar un proyecto desde la plataforma

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-015 Lo exigido se comprueba solo](../epica.md) |
| **Funcionalidad** | `F-020` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Comprobaciones |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus cinco criterios probados |
---

## 2. Narrativa

- **Como** quien administra varios proyectos desde un solo lugar
- **Quiero** preguntar si uno cumple lo que las reglas exigen, sin entrar a él
- **Para** saber dónde está el problema antes de que alguien lo descubra publicando

---

## 3. Contexto y descripción

El estándar tiene **32 comprobaciones** y funcionan. **La plataforma no usa ninguna:** para saber si un proyecto cumple hay que abrir su carpeta y correrlas ahí.

Esta historia no escribe comprobaciones: **le pide al estándar que corra las suyas** y lee lo que responde. Es la misma forma de los otros dos puentes de la plataforma, y por la misma razón: dos versiones de lo mismo se separan, y la vieja da por bueno lo que la nueva rechaza.

**Y hay una distinción que decide el diseño.** Un proyecto sin el estándar instalado **no está en verde: está sin comprobar.** Devolver «cumple» ahí sería mentir, y devolver «no cumple» haría que nadie mire los rojos de verdad.

### 3.1 Reglas de negocio

- `RN-1` **Se comprueba, no se corrige.**
- `RN-2` Lo que no cumple sale **con su archivo y su línea**.
- `RN-3` **«Sin comprobar» y «no cumple» son cosas distintas**, y se responden distinto.
- `RN-4` Las comprobaciones **no se duplican**: se corren las del estándar, por su punto de entrada.
- `RN-5` **Cero comprobaciones corridas es rojo.** Es lo mismo que no haber mirado.
- `RN-6` El veredicto **no se guarda**: se calcula al pedirlo.

### 3.2 Supuestos

- Que el proyecto conectado tiene el estándar instalado. Si no, se dice.

### 3.3 Fuera de alcance

- Corregir lo que encuentra.
- Escribir comprobaciones nuevas.
- Fijar el estado de una funcionalidad, que es la `HU-002`.
- La pantalla.

---

## 4. Criterios de aceptación

### CA-01 — Un proyecto que cumple pasa

```gherkin
Dado un proyecto conectado con el estándar instalado y sin incumplimientos
Cuando se pide comprobarlo
Entonces el veredicto dice que cumple
Y dice cuántas comprobaciones corrieron
```

**Cómo validarlo:** con un proyecto de prueba que pase.
- **Aprobado cuando:** dice que cumple **y** cuántas corrieron. Lo segundo importa: sin el número no se sabe si miró algo.

### CA-02 — Uno que no cumple es rechazado, con archivo y línea

```gherkin
Dado un proyecto con algo que incumple
Cuando se pide comprobarlo
Entonces el veredicto dice que no cumple
Y cada falla trae el archivo y la línea donde está
```

**Cómo validarlo:** sobre este repositorio, provocando un enlace roto.
- **Aprobado cuando:** sale la ruta con su línea. Un veredicto sin ubicación no se puede atender.

### CA-03 — Apuntada a algo que no le corresponde, lo dice

```gherkin
Dado un proyecto sin el estándar instalado
Cuando se pide comprobarlo
Entonces se dice que no hay contra qué comprobarlo
Y no se da veredicto
```

**Cómo validarlo:** con una carpeta vacía registrada como proyecto.
- **Aprobado cuando:** ni «cumple» ni «no cumple». **Es el caso de «que NO pase» de esta historia.**

### CA-04 — Comprobar no modifica nada

```gherkin
Dado un proyecto cualquiera
Cuando se comprueba
Entonces ningún archivo cambia
```

**Cómo validarlo:** retrato de la carpeta antes y después.
- **Aprobado cuando:** nada cambió, ni el contenido ni la fecha.

### CA-05 — Cero comprobaciones corridas es rojo

```gherkin
Dado que la corrida no comprobó nada
Cuando se lee el veredicto
Entonces no dice que cumple
```

**Cómo validarlo:** con un resumen de cero comprobaciones.
- **Aprobado cuando:** no cumple. Una corrida que no corrió nada y termina en verde es un silencio que se lee como éxito.

### Criterios transversales

- La salida **se tapa antes de mostrarse**: trae fragmentos de los archivos del proyecto, y uno puede traer una clave.
- Una carpeta que ya no está se dice, en vez de reventar.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | Comprobar este repositorio no debe tardar tanto que nadie lo pida. **El número queda escrito** |
| Seguridad | La salida pasa por el tapador antes de mostrarse |
| Recuperación | Nada que reconstruir: el veredicto se calcula al pedirlo |

---

## 6. Diseño y referencias

- Funcionalidad `F-020` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-20` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- El punto de entrada del estándar: `validadores/validar.py`.
- El puente que tapa: [plataforma/nucleo/seguridad/claves.py](../../../../plataforma/nucleo/seguridad/claves.py).

---

## 7. Tareas técnicas derivadas

1. Comprobar que el proyecto exista y tenga el estándar.
2. Correr el punto de entrada del estándar en un proceso aparte.
3. Leer su resumen y sus fallas, con archivo y línea.
4. Tapar la salida antes de devolverla.
5. Distinguir «sin comprobar» de «no cumple».

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige](D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige/estado-fase.md) | Los cinco CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-008`, que sabe dónde vive cada proyecto |
| **Riesgo 1** | Que tarde tanto que nadie lo pida. Se mide, y el número queda escrito |
| **Riesgo 2** | Que un proyecto sin el estándar dé un veredicto falso. Lo cubre el `CA-03` |
| **Riesgo 3** | Que la salida traiga una credencial de un archivo del proyecto. Se tapa antes de mostrarla |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La vuelta de la columna de dependencias, resuelta.
- ☑ El módulo Comprobaciones, con [especificación](../../../comprobaciones/spec.md) aprobada el 2026-09-01.

## 11. Definition of Done

- ☑ Los cinco criterios con veredicto y evidencia.
- ☑ Este repositorio comprobado desde la plataforma, con el tiempo medido.
- ☑ Comprobado que no modifica nada.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita que haya un proyecto registrado |
| Negociable | Sí | Qué se muestra de cada falla se puede ajustar |
| Valiosa | Sí | Hoy hay que entrar a la carpeta para saberlo |
| Estimable | Sí | Las comprobaciones ya existen: falta pedirlas y leer |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre sobre este repositorio y se mira |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-09-01 | Nace de `F-020`, con la épica `EP-015` aprobada ese día |
