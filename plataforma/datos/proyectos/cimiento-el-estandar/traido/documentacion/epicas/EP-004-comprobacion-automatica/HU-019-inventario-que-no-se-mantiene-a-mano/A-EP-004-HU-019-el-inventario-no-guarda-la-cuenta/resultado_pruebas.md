# Resultado de Pruebas — Fase `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado, y si cada criterio de aceptación quedó cumplido**. Lo que se iba a probar está en el [plan_pruebas.md](plan_pruebas.md); lo que quedó construido, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-019-el-inventario-no-guarda-la-cuenta` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-26 |
| **Ejecutado por** | El agente, en la sesión del 2026-08-26 |
| **Ciclo** | 2. El ciclo 1 dejó un hueco que se corrigió y se volvió a correr entero |

---

## 2. Veredicto

**Cumple.**

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 6 de 6 | 6 de 6 |
| Criterios en verde | 3 de 3 | 3 de 3 |
| Sabotajes cazados | Todos | 6 de 6, **en el ciclo 2** |
| Fallas en la suite completa | 0 | 0, sobre **373 pruebas** |

---

## 3. Resultado por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 | El pendiente remite al comando y el comando responde | ✅ |
| CP-002 | Reponer un total a mano se reporta | ✅ |
| CP-003 | La comprobación reporta y **no corrige** | ✅ |
| CP-004 | La narrativa fechada y la condición de cierre sobreviven | ✅ |
| CP-005 | Un número dentro de la narrativa **no** se marca | ✅ |
| CP-006 | Nada más se movió | ✅ |

### CP-001 — El pendiente remite al comando

Los tres rótulos —`Total de HU`, `Completas`, `Incompletas`— **no aparecen** como campo con número. La expresión que los busca devolvió lista vacía sobre el archivo real. El encabezado trae `python validadores/validar.py fases`, copiable, y al correrlo terminó con:

```
HU: 113 en total · 70 completas · 43 incompletas (F12.2)
```

### CP-002 — Reponer un total a mano se reporta

Sobre un árbol de mentira en carpeta temporal:

| Paso | Resultado |
|---|---|
| Sin la fila | 0 avisos |
| Con `| **Total de HU** | 99 |` | 1 aviso |
| El texto del aviso | «guarda la cuenta a mano en el campo **Total de HU**, y el árbol ya la sabe: la da `validar.py fases`. Dos copias del mismo dato se separan» |
| Quitando la fila | 0 avisos |

Con los tres campos puestos, tres avisos: uno por campo, no uno global.

### CP-003 — Reporta y no corrige

Se comparó el archivo **en bytes**, antes y después de correr la comprobación: **idéntico**. Y la carpeta quedó con los mismos archivos, sin ninguno nuevo.

**Se comparó en bytes y no como texto a propósito.** Comparar como texto habría dejado pasar un cambio de fin de línea, que es exactamente el defecto que se coló en la fase E de la plataforma y que allá solo se cazó por comparar bytes.

### CP-004 — La narrativa sobrevive

| Qué | Antes | Después |
|---|---|---|
| Párrafos de narrativa fechada | 11 | 11 |
| El bloque completo, letra por letra | — | **Idéntico** |
| Sección «Cómo se sabe que cerró» | Sí | Sí |
| Sección «Casi todo es retrodocumentación» | Sí | Sí |
| Líneas del archivo | 148 | 83 |

El «antes» no se tomó de memoria: se sacó del historial con `git show HEAD:pendientes/48-inventario-hu.md`.

### CP-005 — Las cifras de la narrativa no disparan

Con un párrafo que dice «68 a 74 total. Seis historias nuevas al enrutar el backlog: 6 que ya existían» y **ningún campo de cuenta**: 0 avisos.

### CP-006 — Nada más se movió

| Qué | Antes | Después |
|---|---|---|
| Avisos de `validar.py fases` | 54 | 54 |
| Fallas | 0 | 0 |
| Total de historias | 112 | 113 |
| Completas | 69 | 70 |
| Incompletas | 43 | 43 |

**El total sube uno porque la historia que arregla el conteo entra en el conteo**, con su fase completa. No es un desfase nuevo.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Los sabotajes

Seis, uno por cada cosa que la fase promete. Restaurados **con copia, nunca con el control de versiones**.

| # | Qué se rompió | Ciclo 1 | Ciclo 2 |
|---|---|---|---|
| 1 | La comprobación no busca nada | Cazado (3 pruebas) | Cazado (4) |
| 2 | Marca cualquier cifra, no el campo | Cazado (3) | Cazado (4) |
| 3 | **Corrige** el archivo en vez de reportar | Cazado (1) | Cazado (1) |
| 4 | Se descuelga de la corrida | **En verde** | Cazado (1) |
| 5 | El pendiente vuelve a guardar la cuenta | Cazado (1) | Cazado (1) |
| 6 | El pendiente deja de nombrar el comando | **En verde** | Cazado (1) |

### 4.2 Los dos que pasaron en verde, y por qué no eran lo mismo

**Es la lección de `S-033`: un sabotaje en verde tiene dos diagnósticos opuestos, y solo se distinguen corriendo el escenario y mirando el estado final.** Se hizo, y dieron distinto:

**El 6 no saboteó.** El pendiente nombra el comando **tres veces** y el guion reemplazaba una sola, así que el archivo seguía diciéndolo. La prueba tenía razón en pasar. Se corrigió el guion para que quite las tres, y entonces la prueba falló, que es lo correcto.

**El 4 sí saboteó, y la prueba era floja.** Descolgar `cuenta_escrita_a_mano` de `validar` dejaba las seis pruebas en verde, porque **todas la llamaban directo**. La comprobación existía y nadie la llamaba: por el comando que la gente corre, no salía nada.

Se agregó `test_el_aviso_sale_en_la_corrida_de_fases`, que la busca **a través de `validar`**. Con ella, el sabotaje 4 falla.

**Esto es un defecto que las pruebas del plan no habrían encontrado.** Los seis casos comprobaban el comportamiento de la función; ninguno comprobaba que estuviera conectada.

### 4.3 El guion de sabotaje decía correr la suite completa y corría cero

Su última corrida usaba `unittest discover`, que sobre esa carpeta encontró **cero pruebas** y reportó `OK`. Dos ciclos antes se habría leído como «suite completa en verde».

Se cambió por lanzar `pruebas.py` como programa, y se le agregó un corte: si la corrida final no dice `OK`, o dice `Ran 0`, el guion sale con error en vez de callarse.

### 4.4 Rastros

Ninguno. Los seis sabotajes editan un archivo que se restaura con copia, y las pruebas escriben solo en carpeta temporal. **El pendiente real no se editó para probar** (`08·T4`).

### 4.5 Ninguna prueba usa credenciales

Ni reales ni inventadas. No hay autenticación en esto (`00·N6`).

---

## 5. Trazabilidad criterio a evidencia

| CA / RNF | Evidencia | Estado |
|---|---|---|
| CA-01 — responde sin guardar la respuesta | CP-001 | ✅ |
| CA-02 — reponer se reporta | CP-002, CP-005 | ✅ |
| CA-02 — y no se corrige | CP-003 | ✅ |
| CA-03 — la narrativa sobrevive | CP-004 | ✅ |
| RNF-01 — dice de dónde sale la cuenta | CP-001 paso 4 | ✅ |
| RNF-02 — no agrega un recorrido nuevo | T-10: la función hace un `isfile` y una lectura, sin recorrer | ✅ |

---

## 6. Veredicto final

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple**, en el ciclo 2 |
| **CA cumplidos** | 3 de 3 |
| **CA en "No"** | Ninguno |
| **Defectos abiertos aceptados** | Ninguno. `DEF-01` corregido y verificado |
| **Suite** | `python validadores/pruebas.py`: **373 pruebas, OK** |

### Defectos encontrados y corregidos

| ID | Qué era | Cómo se cazó | Estado |
|---|---|---|---|
| DEF-01 | La comprobación podía descolgarse de `validar` sin que ninguna prueba lo dijera | Sabotaje 4 | Corregido: `test_el_aviso_sale_en_la_corrida_de_fases` |
| DEF-02 | El guion de sabotaje reportaba `OK` sin correr ninguna prueba | Leyendo su salida: decía `Ran 0 tests` | Corregido: lanza el programa, y se cae si corre cero |

---

## 7. Lo que este resultado NO dice

- **No dice que el inventario esté al día.** Dice que ya no puede quedar viejo, que es otra cosa. Las 43 historias incompletas siguen incompletas.
- **No cubre la plantilla [`inventario-hu.md`](../../../../../plantillas/inventario-hu.md)**, que sigue describiendo la tabla que acá se quitó. Un proyecto que herede el estándar arma su inventario a mano con el mismo defecto. Está fuera del alcance declarado en §2.1 del plan, y se reporta en el cierre.
