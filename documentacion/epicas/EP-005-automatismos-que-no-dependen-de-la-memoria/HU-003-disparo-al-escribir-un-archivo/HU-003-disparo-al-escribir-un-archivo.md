# HU-003 — Disparar las comprobaciones al escribir un archivo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En implementación — CA-01 y CA-02 cumplidos; el CA-03, no |

---

## 2. Narrativa

- **Como** quien escribe documentación mientras trabaja
- **Quiero** que la comprobación corra apenas se guarda el archivo
- **Para** arreglar en el momento lo que rompí, y no descubrirlo días después

---

## 3. Contexto y descripción

Una comprobación que hay que acordarse de correr no protege nada. La que corre sola, en el momento en que ocurre el cambio, sí: el error se ve cuando todavía se tiene el contexto en la cabeza y arreglarlo cuesta un minuto.

El momento correcto es al escribir el archivo, no al final del día. Un enlace roto que se detecta enseguida se arregla enseguida; el mismo enlace descubierto una semana después obliga a reconstruir qué se estaba haciendo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Al escribir un archivo de documentación, la comprobación corre sola |
| RN-02 | El resultado vuelve a quien escribió, en el momento |
| RN-03 | Solo corre lo que es rápido: lo lento se corre a demanda |
| RN-04 | Lo que no le toca se ignora en silencio, sin ruido |
| RN-05 | La comprobación no modifica el archivo |
| RN-06 | Cada hallazgo es **duro** o **blando**: el duro detiene el trabajo hasta que se arregle, el blando avisa y el trabajo sigue |
| RN-07 | Cuál es duro lo dice la regla que se incumplió, no el programa ni el momento: así no cambia según quién lo corra |

### 3.2 Supuestos

- Las comprobaciones rápidas terminan en menos de lo que tarda quien escribe en seguir trabajando.

### 3.3 Fuera de alcance

- Escribir las comprobaciones. Eso es EP-004.
- Corregir lo encontrado.

---

## 4. Criterios de aceptación

### CA-01 — Al escribir un archivo corre la comprobación

```gherkin
Dado que se escribe un archivo de documentación
Cuando termina de escribirse
Entonces la comprobación corre sola
Y su resultado vuelve a quien escribió
```

**Cómo validarlo:**

1. Escribir en un archivo de documentación un enlace a algo que no existe.
2. Guardar. Resultado esperado: aparece el hallazgo enseguida, con el archivo y la línea.
3. Arreglar el enlace y guardar. Resultado esperado: ya no aparece.
- **Aprobado cuando:** el error se ve en el momento en que se comete.

### CA-02 — Lo que no le toca se ignora en silencio

```gherkin
Dado que se escribe un archivo que no es de documentación
Cuando termina de escribirse
Entonces no pasa nada ni se muestra ningún mensaje
```

**Cómo validarlo:**

1. Escribir un archivo de otro tipo en el proyecto de prueba.
2. Guardar. Resultado esperado: no aparece ningún mensaje.
- **Aprobado cuando:** el automatismo no genera ruido.

### CA-03 — El hallazgo grave detiene; el resto avisa

```gherkin
Dado que la comprobación encontró algo al escribir el archivo
Cuando ese hallazgo es de los que la regla marca como duros
Entonces el trabajo se detiene y se dice qué hay que arreglar
Y cuando no lo es, se avisa y el trabajo sigue
```

**Cómo validarlo:**

1. Escribir un archivo con un hallazgo de los blandos, como una errata de forma. Resultado esperado: sale el aviso y se puede seguir.
2. Escribir uno con un hallazgo duro, de los que la regla marca así. Resultado esperado: no se puede seguir hasta arreglarlo, y se dice cuál es.
3. Arreglarlo y volver a guardar. Resultado esperado: sigue.
- **Aprobado cuando:** lo grave no se puede ignorar por descuido, y lo leve no estorba.

### Criterios de aceptación transversales

- [ ] **Rendimiento** — el disparo no se nota en el ritmo de trabajo.
- [ ] **Errores** — si la comprobación falla, se avisa y el trabajo continúa.
- [ ] **Reversibilidad** — detener nunca deja el archivo a medias: lo escrito queda como estaba.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | Corre en el tiempo que toma seguir escribiendo |
| **Silencio** | Solo habla cuando tiene algo que decir |
| **Inocuidad** | No modifica el archivo escrito |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), criterio CAE-03.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Enganchar la comprobación al momento de escribir un archivo.
- [ ] Decidir qué comprobaciones son lo bastante rápidas.
- [ ] Devolver el resultado a quien escribió.
- [ ] Ignorar en silencio lo que no aplica.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir](A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md#6-veredicto-de-la-fase) — el CA-01 y el CA-02 sí; el CA-03 no. Pendiente el commit |

**La fase retro-documenta.** El enganche corre con cada escritura y comprueba los enlaces. Lo que tiene que responder es el CA-03: hoy devuelve el detalle y no distingue entre detener y avisar, como sí hace la línea de comandos.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | EP-004, porque dispara comprobaciones ya escritas | Alto |
| Riesgo | Que el disparo demore y estorbe | Solo corren las rápidas; el resto se corre a demanda |
| Riesgo | Que hable cuando no tiene nada que decir | Se ignora en silencio lo que no aplica |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La comprobación corre al escribir
- [ ] El resultado vuelve en el momento
- [ ] Lo que no aplica no genera mensajes
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita comprobaciones que disparar |
| **N**egociable | Sí | Cuáles se disparan se puede discutir |
| **V**aliosa | Sí | Convierte una comprobación optativa en una que siempre corre |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Un enganche |
| **T**esteable | Sí | Se prueba rompiendo algo y guardando |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Nacen `RN-06`, `RN-07` y `CA-03`: la historia decía que la comprobación corre y que el resultado vuelve, pero no qué pasa cuando el hallazgo es grave. Con eso, un hallazgo crítico y una errata valían igual, y los dos se podían ignorar. Sale del hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen` |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. El disparo corre en el momento y calla con lo que no le toca, y se comprueba que callar no es no haber corrido. CA-03 en «No»: nada detiene, todo avisa |
