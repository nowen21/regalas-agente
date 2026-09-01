# HU-006 — Avisar al proyecto que quedó atrás

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica** | [EP-016 El cuerpo de reglas se administra desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-010` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Reglas |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien decide cuándo sube un proyecto de versión
- **Quiero** que el aviso me diga qué cambió desde la versión que declaro
- **Para** saber si subo hoy o la semana que viene, en vez de solo saber que voy atrás

---

## 3. Contexto y descripción

**Decir «estás atrasado» no ayuda a decidir.** Lo que decide es si alguna de las versiones que pasaron **obliga a migrar**, cuántas van, y de qué se trataban.

**Y esto estaba construido a medias sin que nadie lo declarara.** El aviso existía y se daba al conectar un proyecto; lo que no salía era qué cambió. Se midió el 2026-09-01 y apareció por qué: **el lector del registro reconocía 143 de 197 entradas**, y la más reciente que entendía era la **34.2.0**. Una convención cambió y el lector se quedó atrás.

**Un número inventado tampoco es estar al día.** Una versión mayor que la real apagaría el aviso en vez de dispararlo. Se comprueba contra el registro, que es donde está lo que existió.

### 3.1 Reglas de negocio

- `RN-1` **El aviso dice qué cambió**, no solo que hay desfase.
- `RN-2` **Lo primero es si alguna obliga a migrar.** Es lo único que cambia qué hacer.
- `RN-3` **Un número que no existe se dice como lo que es**, no como ir adelantado.
- `RN-4` **No declarar nada no es declarar algo falso.**

### 3.2 Supuestos

- Que el registro de cambios del estándar está completo.

### 3.3 Fuera de alcance

- **Subir la versión de un proyecto.** Es decisión del usuario.

---

## 4. Criterios de aceptación

### CA-01 — Con versión anterior, avisa y dice qué cambió

```gherkin
Dado un proyecto que declara una versión anterior
Cuando se revisa su desfase
Entonces se dice cuántas versiones pasaron y cuáles obligan a migrar
```

**Cómo validarlo:** con un proyecto en una versión vieja de este estándar.
- **Aprobado cuando:** sale el resumen. **Es el criterio que decide.**

### CA-02 — Con la misma, no molesta

```gherkin
Dado un proyecto al día
Cuando se revisa
Entonces no hay aviso
```

**Cómo validarlo:** con la versión vigente.
- **Aprobado cuando:** dice que está al día y no da lista de cambios.

### CA-03 — Con un número que no existe, lo dice

```gherkin
Dado un proyecto que declara una versión que nunca se publicó
Cuando se revisa
Entonces se dice que ese número no existió
Y no se concluye que va adelantado
```

**Cómo validarlo:** con un número mayor que el real.
- **Aprobado cuando:** lo dice. Es el caso de «que NO pase».

### Criterios transversales

- No declarar nada se responde distinto de declarar algo falso.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Utilidad | El aviso tiene que servir para decidir, no solo para informar |
| Honestidad | Tres respuestas distintas, dichas distinto |

---

## 6. Diseño y referencias

- Funcionalidad `F-010` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-10` del [análisis](../../../../cvds/analisis-requisitos/README.md).

---

## 7. Tareas técnicas derivadas

1. Comprobar que la versión declarada existió.
2. Comparar con la del estándar.
3. Traer las versiones del tramo.
4. Decir cuáles obligan a migrar.
5. Juntarlo en un aviso.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [L-EP-016-HU-006-el-aviso-dice-que-cambio](L-EP-016-HU-006-el-aviso-dice-que-cambio/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | El lector de versiones del estándar |
| **Riesgo 1** | **Que el lector no entienda el registro y el aviso salga vacío.** Pasó, y llevaba 54 versiones así |
| **Riesgo 2** | Que un número inventado apague el aviso. Se comprueba contra el registro |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Medido: el lector reconocía 143 de 197 entradas.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ El lector del registro, corregido y versionado en la 37.2.1.
- ☑ Comprobado que un número inventado no pasa por estar al día.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita el lector de versiones del estándar |
| Negociable | Sí | Cuántas versiones se listan se puede ajustar |
| Valiosa | Sí | Un aviso que no dice qué cambió se ignora |
| Estimable | Sí | Es juntar lo que el estándar ya sabe responder |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se prueba con las tres respuestas |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
