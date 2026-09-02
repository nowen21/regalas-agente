# Resultado de Pruebas — Fase `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre` |
| **HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md](../HU-021-las-pruebas-que-existen-se-corren.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **9** |

| | Antes | Después |
|---|---|---|
| Baterías del repositorio que nada corre | 1 de 2 | **0 de 2** |
| Pruebas que la orden ejecuta | 724 | **911** |

---

## 2. Ejecución caso por caso

### CP-001 — Corre la batería que hay, y la cuenta

```
pruebas de la plataforma: 187
```

Ningún hallazgo de falla: las 187 están en verde. Se le pide **por su punto de entrada**, que es como se corre de verdad.

**Resultado: pasa.**

### CP-002 — No tener plataforma se dice, y no es falla

```
sin plataforma: 0 | AVISO | no hay plataforma en este repositorio: no se
corrió su batería. No es lo mismo que estar en verde
```

Es un **aviso**, no una falla. Cada proyecto que hereda el estándar está en este caso: si fuera falla, tendría un rojo permanente desde el día que instala, y un rojo que siempre está se apaga.

**Resultado: pasa.**

### CP-003 — Cero pruebas es rojo

Una plataforma de mentiras con un punto de entrada que no corre nada:

```
FALLA — la batería de la plataforma corrió **0 pruebas** — cero no es verde:
quiere decir que no se comprobó nada (08·T5)
```

Es la misma regla que ya regía para la otra batería, escrita en el mismo lenguaje.

**Resultado: pasa.**

### CP-004 — Una prueba de la plataforma en rojo se caza

**El caso que decide la fase.** Se escribió dentro de la plataforma una prueba que falla a propósito, se corrió, y se borró:

```
con una rota: 188 pruebas | 1 hallazgo(s)
   FALLA | la batería de la plataforma falló: 188 prueba(s) · 1 falla(s) ·
   0 error(es) — se corre con `python manage.py test` desde `plataforma/`
```

Dice cuántas corrieron, cuántas fallaron, y **por dónde ir a verlo**. Sin este caso, todo lo demás pasaría igual con un corredor que no mira nada.

**Resultado: pasa**, y el archivo de sabotaje se borró en el mismo bloque que lo escribió.

### CP-005 — El subconjunto no arrastra la otra batería

Sobre un repositorio chico con una sola prueba: pidiendo esa prueba, el resumen **no** nombra la plataforma; sin pedir nada, sí.

**Resultado: pasa.** Es lo que mantiene barata la orden del día a día, que es la que `02·F5` obliga a usar en cada fase.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| El resumen de la corrida completa | Dice las dos cifras, separadas |
| El costo en tiempo | Medio minuto más sobre diez: la batería de la plataforma corre dos veces, una como producto y otra dentro de su prueba de integración. Está declarado en el plan como costo aceptado |
| El archivo de sabotaje | Borrado; la carpeta quedó como estaba |

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | La primera versión de una prueba llamaba a la corrida completa **desde dentro de la corrida completa**: las 724 corriendo dentro de la 725, y la orden no terminaba | Alta | Arreglado acá: se arma un repositorio chico con una sola prueba. Queda dicho en el propio archivo, porque volver a caer en eso es fácil |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-021-las-pruebas-que-existen-se-corren.md#ca-01--la-carpeta-se-corre-con-una-orden-y-es-la-documentada) | CP-001, CP-004 | **Cumple** |
| [CA-02](../HU-021-las-pruebas-que-existen-se-corren.md#ca-02--cero-pruebas-no-pasa-por-verde) | CP-002, CP-003 | **Cumple** |
| [CA-03](../HU-021-las-pruebas-que-existen-se-corren.md#ca-03--se-puede-pedir-un-subconjunto) | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Correr la otra batería por su punto de entrada | Hecho |
| Su cifra aparte en el resumen | Hecho |
| Cero pruebas es rojo, no tenerla es aviso | Hecho |
| El subconjunto no la arrastra | Hecho |
| Sabotaje | Hecho, y cazado |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Este repositorio ya no tiene ninguna batería que nada ejecute. Los tres criterios quedaron cumplidos, y el que decide —que una prueba en rojo de la plataforma se cace— se comprobó rompiendo una a propósito, no leyendo el código.

**Lo que la fase no resuelve, y queda dicho:** lo que se lee es la línea que el corredor de la plataforma imprime al terminar. Si mañana cambia de marco, esa línea cambia y hay que volver acá.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las nueve pruebas de la fase | `validadores/tests/test_la_bateria_de_la_plataforma_se_corre.py` |
| EV-02 | El sabotaje | §2, `CP-004` |
| EV-03 | La corrida completa con las dos cifras | `historico-chat/.estado/internas.txt` |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
