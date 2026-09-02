# Resultado de Pruebas — Fase `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-004-HU-008-ningun-programa-nuevo-se-cuela-en-silencio` |
| **HU** | [documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md](../HU-008-corrida-completa.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre el repositorio del estándar |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 5 |
| Ejecutados | 5 |
| Pasaron | 5 |
| Fallaron | 0 |

| | Antes | Después |
|---|---|---|
| Programas que salen con 0 sin decir nada | 2 | **0** |
| Fallas de la batería por estas causas | 4 | **0** |
| Recuento del amarre | 27 de 85 | **27 de 85** |

---

## 2. Ejecución caso por caso

### CP-001 — Cada programa dice quién lo corre, y sale con 2

```
$ python validadores/estacion_commit.py
estacion_commit.py no se corre solo: lo corre el enganche `post-commit` de git,
después de cada commit, y correrlo así **no hace nada**.        (código 2)

$ python validadores/rutas_fuera.py
rutas_fuera.py no se corre solo: lo corre el enganche del adaptador, cada vez
que se escribe un archivo, y correrlo así **no hace nada**.     (código 2)
```

Los otros cuarenta módulos siguen diciendo `validar.py`, con el mismo texto de siempre: el parámetro es opcional y el camino viejo no se tocó.

**Resultado: pasa.**

### CP-002 — La prueba sigue cazando al que calla

**Este es el caso que decide la fase**, porque lo que se cambió es la comprobación que reportaba el defecto.

Se escribió en `validadores/` un módulo de mentiras que no imprime nada y sale con 0, se corrió la prueba y se borró el módulo:

```
lo caza: True
la corrida falla: True
el módulo de mentiras se borró: True
```

**Resultado: pasa.** La comprobación se amplió en **qué corredores acepta**, no en cuánto silencio deja pasar.

### CP-003 — El resumen es lo último que se lee

```
$ python validadores/validar.py todo
...
32 comprobación(es) corridas · 0 con fallas
Sin fallas. Los avisos de cada comprobación salen arriba.
```

El conteo por regla sigue saliendo entero, ahora arriba del resumen. **Se movió, no se recortó:** ese conteo es lo que dice qué regla cambiar.

**Resultado: pasa.**

### CP-004 — El contador del amarre no cambia

```
$ python validadores/validar.py amarre
Piezas de `validadores/`: 85 · amarradas a la herramienta: 27 · libres: 58
```

**Encontró un defecto de verdad.** El primer intento nombraba el archivo del enganche —`hook_rutas.py`, `hook_estacion.py`— dentro del mensaje, y el recuento subió de 27 a 29: el contador busca esa palabra dentro del texto y no distingue **nombrar** de **ser**. Se reescribió nombrando al corredor sin su archivo.

**Resultado: pasa.**

### CP-005 — No regresión

`validar.py internas` sobre las 713 pruebas. **Las cuatro fallas de estas causas quedaron en verde**, y no apareció ninguna nueva.

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Los dos mensajes, leídos como los lee una persona | Dicen quién corre el programa, y no mandan a ningún comando que no exista |
| El camino viejo del guardián | Intacto: mismo texto y misma línea de ayuda |
| La corrida completa, de principio a fin | El conteo arriba, el veredicto al final |

Ninguna prueba tocó datos reales. El módulo de mentiras del `CP-002` se borró en el mismo bloque que lo escribió.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | Nombrar el archivo del enganche en el mensaje hizo que dos programas agnósticos **se contaran como amarrados a la herramienta** | Media | Arreglado acá, nombrando al corredor sin su archivo |
| D-02 | La prueba exigía la palabra `validar.py`, y dos programas no cuelgan del validador | Media | Arreglado acá: se exige nombrar al corredor, no un nombre concreto |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-03](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) | CP-001, CP-002, CP-003 | **Cumple** |
| [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | CP-004, CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| El guardián acepta nombrar al corredor | Hecho, con parámetro opcional |
| Los dos programas lo usan | Hecho, cada uno con su corredor real |
| La prueba acepta un corredor que no sea `validar.py` | Hecha, y comprobada con sabotaje |
| El conteo antes del resumen | Hecho |
| La batería sin fallas de estas causas | Comprobado |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Los dos criterios vuelven a estar cumplidos, y el arreglo no consistió en callar la comprobación: se comprobó con un módulo de mentiras que el silencio se sigue cazando. Lo que cambió es qué cuenta como «decir por dónde se corre», porque dos programas no cuelgan del validador y exigirles que lo nombraran era mandarlos a mentir.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las seis pruebas del silencio | `validadores/tests/test_ninguno_termina_en_silencio.py` |
| EV-02 | Las siete pruebas de la corrida completa | `validadores/tests/test_la_corrida_completa_en_una_linea.py` |
| EV-03 | La batería interna | `historico-chat/.estado/internas.txt` |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
