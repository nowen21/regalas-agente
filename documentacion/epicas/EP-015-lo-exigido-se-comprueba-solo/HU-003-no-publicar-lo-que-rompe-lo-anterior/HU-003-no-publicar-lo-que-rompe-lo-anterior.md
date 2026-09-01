# HU-003 — No publicar lo que rompe lo anterior

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica** | [EP-015 Lo exigido se comprueba solo](../epica.md) |
| **Funcionalidad** | `F-022` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Comprobaciones |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus cuatro criterios probados |
---

## 2. Narrativa

- **Como** quien publica una versión que otros proyectos van a adoptar
- **Quiero** que antes de publicar se vuelva a correr todo lo que ya funcionaba
- **Para** no mandarle a nadie una versión que le rompe lo que le servía

---

## 3. Contexto y descripción

**Publicar es la única acción de la plataforma que no se puede deshacer del lado de quien recibe.** Un proyecto que adopta una versión rota se lleva el problema, y retirarla no le devuelve el día que perdió.

**Qué es «lo que ya funcionaba».** No una lista escrita a mano de lo que alguien se acuerda: **las comprobaciones del estándar y la suite del proyecto**, enteras. Lo que estaba en verde y tiene que seguir estándolo.

Esta historia **cierra la vuelta** de la columna de dependencias: `F-008`, publicar una versión, esperaba esta puerta.

### 3.1 Reglas de negocio

- `RN-1` **Una versión que rompe algo no se publica.**
- `RN-2` **Lo que obliga a rehacer se declara.** Publicar sabiendo qué queda mal es una decisión; publicar sin saberlo es un accidente.
- `RN-3` **Lo que está sin verificar se declara y no detiene.** Que no tenga prueba no quiere decir que esta versión lo rompió.
- `RN-4` **No haber podido revisar no es haber pasado.** Sin revisar no se publica.
- `RN-5` **Una sola orden.** Si pasar la puerta cuesta trabajo manual, se va a saltar.

### 3.2 Supuestos

- Que el proyecto tiene su suite. Si no se pudo correr, no se publica.

### 3.3 Fuera de alcance

- Publicar. Esta historia es la puerta, no el acto.
- Decidir qué entra en la versión.

---

## 4. Criterios de aceptación

### CA-01 — Una versión que rompe algo no se publica

```gherkin
Dado un proyecto con una comprobación en rojo o una prueba en rojo
Cuando se pide la puerta de publicación
Entonces no pasa
```

**Cómo validarlo:** con cada uno de los dos rojos por separado.
- **Aprobado cuando:** ninguno de los dos pasa. **Es el criterio que decide.**

### CA-02 — Una que obliga a rehacer algo lo declara

```gherkin
Dado un proyecto con una funcionalidad en «no cumple»
Cuando se pide la puerta
Entonces se dice cuál es
Y no pasa
```

**Cómo validarlo:** con una funcionalidad en «no cumple».
- **Aprobado cuando:** sale nombrada, y detiene.

### CA-03 — Una que no rompe nada pasa sin trabajo manual

```gherkin
Dado un proyecto con todo en verde
Cuando se pide la puerta
Entonces pasa, con una sola orden
Y dice cuánto tardó
```

**Cómo validarlo:** sobre este repositorio.
- **Aprobado cuando:** pasa, y el tiempo queda escrito.

### CA-04 — Sin revisar no se publica

```gherkin
Dado que las comprobaciones o las pruebas no se pudieron correr
Cuando se pide la puerta
Entonces no pasa
```

**Cómo validarlo:** con un proyecto que no existe, y con las baterías que no corrieron.
- **Aprobado cuando:** no pasa. **Un «no se pudo» tratado como «pasó» es publicar a ciegas.**

### Criterios transversales

- Lo que está **sin verificar** se declara y no detiene.
- Cero comprobaciones corridas tampoco pasa: viene del veredicto.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Confianza | **Un rojo falso es peor que no tener puerta**: enseña a ignorarla |
| Rendimiento | El tiempo queda escrito. Si la puerta tarda demasiado, se va a saltar |
| Claridad | Se dice qué detuvo la publicación, no solo que se detuvo |

---

## 6. Diseño y referencias

- Funcionalidad `F-022` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-22` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- El veredicto de `F-020` y el estado de `F-021`, que esta puerta junta.

---

## 7. Tareas técnicas derivadas

1. Correr las comprobaciones del proyecto.
2. Correr su suite.
3. Derivar qué funcionalidades obligan a rehacer.
4. Decidir si pasa, y decir por qué no si no pasa.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba](F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba/estado-fase.md) | Los cuatro CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-020` y `F-021`, que aportan el veredicto y el estado |
| **Riesgo 1** | **Que dé un rojo falso.** Pasó al construirla, y por eso está declarado en el cierre |
| **Riesgo 2** | Que tarde tanto que se salte. El tiempo queda escrito |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ `F-020` y `F-021` cerradas.

## 11. Definition of Done

- ☑ Los cuatro criterios con veredicto y evidencia.
- ☑ La puerta corrida sobre este repositorio, con el tiempo medido.
- ☑ Comprobado que un «no se pudo» no pasa.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Junta lo que aportan `F-020` y `F-021` |
| Negociable | Sí | Qué detiene y qué solo se declara se puede ajustar |
| Valiosa | Sí | Es lo que impide mandarle a otro una versión rota |
| Estimable | Sí | Es correr dos cosas que ya existen y juntar el resultado |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre sobre este repositorio |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
