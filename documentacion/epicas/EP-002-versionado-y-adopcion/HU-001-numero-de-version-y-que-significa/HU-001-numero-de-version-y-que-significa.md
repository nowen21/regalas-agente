# HU-001 — Fijar el número de versión y qué significa cada parte

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-002 Versionado de las reglas y adopción por proyecto](../epica.md) |
| **Módulo / Componente** | Versionado del estándar |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En implementación — CA-02, CA-03 y transversales cumplidos; el CA-01, no |

---

## 2. Narrativa

- **Como** quien mantiene las reglas
- **Quiero** un número de versión con reglas escritas de cuándo sube cada parte
- **Para** que se distinga un cambio que obliga a hacer algo nuevo de uno que solo aclara la redacción

---

## 3. Contexto y descripción

Las reglas van a cambiar. Sin número, un cambio de una coma y uno que obliga a rehacer trabajo se ven igual, y entonces todo cambio genera la misma duda: ¿esto me toca?

Un número por sí solo tampoco alcanza. Lo que sirve es que cada parte del número signifique algo acordado, para que al ver que subió se sepa de inmediato si hay que hacer algo o no.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El número tiene tres partes: mayor, menor y de corrección |
| RN-02 | Sube la mayor cuando un proyecto al día queda obligado a hacer algo nuevo |
| RN-03 | Sube la menor cuando se agrega algo que no obliga a nadie |
| RN-04 | Sube la de corrección cuando cambia la redacción y no lo que se exige |
| RN-05 | El número vive en un solo archivo, y ese archivo es la verdad |
| RN-06 | Ninguna parte del número se salta ni se reinicia |

### 3.2 Supuestos

- Quien cambia una regla sabe decir si su cambio obliga a alguien. Si duda, sube la parte mayor: equivocarse por exceso avisa de más, equivocarse por defecto no avisa.

### 3.3 Fuera de alcance

- El registro de qué cambió. Eso es HU-002.
- Que un proyecto declare qué versión sigue. Eso es HU-003.

---

## 4. Criterios de aceptación

### CA-01 — El número existe y se lee en un solo lugar

```gherkin
Dado que el estándar tiene reglas escritas
Cuando alguien pregunta en qué versión va
Entonces la respuesta está en un solo archivo
Y el número tiene sus tres partes
```

**Cómo validarlo:**

1. Abrir la raíz del estándar y buscar el archivo que declara la versión.
2. Leer su contenido. Resultado esperado: un número de tres partes y nada más.
3. Buscar si algún otro archivo declara la versión. Resultado esperado: ninguno la declara como propia; los demás la citan.
- **Aprobado cuando:** hay una sola fuente del número.

### CA-02 — Un cambio que obliga sube la parte mayor

```gherkin
Dado que se cambia una regla y un proyecto al día queda obligado a hacer algo nuevo
Cuando se versiona el cambio
Entonces sube la parte mayor
Y las otras dos vuelven a cero
```

**Cómo validarlo:**

1. Tomar un cambio de regla que obligue, por ejemplo exigir un documento que antes no se pedía.
2. Aplicar el criterio escrito. Resultado esperado: dice que es de la parte mayor.
3. Ver el número resultante. Resultado esperado: la mayor subió uno y las otras quedaron en cero.
- **Aprobado cuando:** el criterio se aplica sin discusión y el número queda como dice.

### CA-03 — Una corrección de redacción no sube la parte mayor

```gherkin
Dado que se afina la redacción de una regla sin cambiar qué exige
Cuando se versiona el cambio
Entonces sube solo la parte de corrección
```

**Cómo validarlo:**

1. Tomar un cambio que solo mejore cómo está escrita una regla.
2. Aplicar el criterio. Resultado esperado: dice que es corrección.
3. Ver el número. Resultado esperado: subió la última parte y las otras dos quedaron igual.
- **Aprobado cuando:** un cambio de redacción no alarma a nadie.

### Criterios de aceptación transversales

- [ ] **Límites** — está definido qué se hace cuando un cambio parece de dos tipos a la vez: manda el más alto.
- [ ] **No regresión** — el número nunca baja.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | El criterio de cuándo sube cada parte se entiende sin saber de versionado |
| **Estabilidad** | El criterio no cambia con cada versión |
| **Trazabilidad** | El número se puede citar desde cualquier documento |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es un archivo de texto.
- **Documento funcional:** [documentacion/epicas/EP-002-versionado-y-adopcion/epica.md](../epica.md), §5.4 fila 6.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir el archivo único donde vive el número.
- [ ] Escribir el criterio de cuándo sube cada parte, con un ejemplo de cada uno.
- [ ] Escribir qué se hace cuando el cambio parece de dos tipos.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-002-HU-001-retrodocumentar-el-numero-de-version](A-EP-002-HU-001-retrodocumentar-el-numero-de-version/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-002-HU-001-retrodocumentar-el-numero-de-version/resultado_pruebas.md#6-veredicto-de-la-fase) — el CA-02 y el CA-03 sí; el CA-01 no. Pendiente el commit |

**La fase retro-documenta y no toca `VERSION` ni el registro.** El número existe y se usó 23 veces; lo que falta es la prueba de que es la única fuente y de que ninguna parte se saltó.

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
| Dependencia | EP-001, porque se versionan reglas escritas | Alto |
| Riesgo | Que todo se marque como corrección para no alarmar | El criterio se escribe con ejemplos reales de cada tipo |
| Riesgo | Que el número quede declarado en dos sitios | Un solo archivo lo declara; los demás lo citan |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El número vive en un archivo único
- [ ] El criterio de cada parte está escrito con ejemplos
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No necesita nada más que reglas escritas |
| **N**egociable | Sí | El esquema del número se puede discutir |
| **V**aliosa | Sí | Distingue el cambio que obliga del que no |
| **E**stimable | Sí | Es un archivo y un criterio |
| **S**mall (pequeña) | Sí | Alcance corto |
| **T**esteable | Sí | Se prueba clasificando cambios reales |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Las 73 entradas del registro recorridas una por una: ninguna baja el número y todas declaran su tipo salvo la primera. CA-01 en «No»: `15.4.0` aparece dos veces, con contenidos distintos |
