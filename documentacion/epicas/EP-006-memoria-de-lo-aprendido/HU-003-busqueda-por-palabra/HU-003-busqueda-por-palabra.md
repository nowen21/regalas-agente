# HU-003 — Buscar por palabra sin instalar nada

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso — CA-02, RNF y transversales cumplidos; el CA-01 a medias |
---

## 2. Narrativa

- **Como** quien está resolviendo algo parecido a lo de hace meses
- **Quiero** buscar por palabra en lo guardado, sin instalar nada
- **Para** encontrar lo que ya se resolvió antes de resolverlo otra vez

---

## 3. Contexto y descripción

Guardar sin poder buscar es guardar en un cajón. La búsqueda tiene que estar el primer día, y tiene que funcionar en cualquier máquina sin instalar nada, porque una búsqueda que exige preparativos no se usa.

La búsqueda por palabra es limitada a propósito: encuentra lo que se nombra igual. Con eso alcanza para la mayoría de las veces, y es lo que siempre va a estar disponible.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Se puede buscar por palabra sin instalar nada |
| RN-02 | La búsqueda dice dónde está lo que encontró, no solo que existe |
| RN-03 | Se puede filtrar por tipo y por alcance |
| RN-04 | El contenido no sale de la máquina |
| RN-05 | Buscar no modifica lo guardado |

### 3.2 Supuestos

- El volumen de lo guardado permite recorrerlo entero sin que la espera moleste.

### 3.3 Fuera de alcance

- Buscar por significado. Eso es HU-004.
- Ordenar los resultados por qué tan útiles fueron.

---

## 4. Criterios de aceptación

### CA-01 — Se busca por palabra y aparece dónde está

```gherkin
Dado que hay cosas guardadas
Cuando se busca una palabra que aparece en una de ellas
Entonces sale esa cosa, con el archivo donde está
```

**Cómo validarlo:**

1. Guardar tres cosas, una con una palabra distintiva.
2. Buscar esa palabra. Resultado esperado: sale una sola, con su ruta.
3. Buscar una palabra que no está en ninguna. Resultado esperado: dice que no encontró nada.
- **Aprobado cuando:** el resultado alcanza para abrir lo que se encontró.

### CA-02 — Se puede filtrar por tipo y por alcance

```gherkin
Dado que hay cosas guardadas de tipos y alcances distintos
Cuando se busca filtrando por uno de ellos
Entonces solo salen las que corresponden
```

**Cómo validarlo:**

1. Guardar cosas de dos tipos y dos alcances.
2. Buscar filtrando por un tipo. Resultado esperado: solo salen las de ese tipo.
3. Filtrar por alcance. Resultado esperado: igual.
- **Aprobado cuando:** los filtros hacen lo que dicen.

### Criterios de aceptación transversales

- [ ] **Privacidad** — el contenido no sale de la máquina para buscar.
- [ ] **Límites** — buscar en una memoria vacía responde sin error.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Autonomía** | Sin instalar nada y sin conexión |
| **Rendimiento** | La búsqueda responde rápido con el volumen esperado |
| **Inocuidad** | Buscar no modifica lo guardado |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), criterio CAE-03.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Recorrer lo guardado y buscar la palabra.
- [ ] Devolver el archivo y el fragmento donde apareció.
- [ ] Agregar los filtros por tipo y por alcance.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra](A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**No cumple**](A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra/resultado_pruebas.md#6-veredicto-de-la-fase) — el CA-02 sí, el CA-01 a medias. Pendiente el commit |
| `B-EP-006-HU-003` — **propuesta, sin abrir** | Lo que le falta al CA-01 | Dos arreglos de una línea en `cmd_search`: imprimir `where_`, y cerrar la conexión del camino sin resultados |

**La fase retro-documentó, y encontró dos defectos.** La búsqueda corre sin instalar nada, ignora los acentos en los dos sentidos, filtra por tipo y alcance, y su índice **sí** está sincronizado —se comprobó con alta, modificación y borrado—. Lo que no hace es **decir dónde está** lo que encontró: `where_` se guarda y `cmd_search` no lo saca. Eso deja el CA-01 sin cumplir.

| Medición, 2026-08-17 | Valor |
|---|---|
| Tiempo por búsqueda léxica sobre las 237 señales reales | **0,0046 s** |
| Herramientas que hubo que instalar | **0** |
| Señales perdidas al archivar | **0** |
| Diferencias de resultado por acentos | **0** |

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
| Dependencia | HU-002, porque busca sobre lo que esa historia guarda | Alto |
| Riesgo | Que no encuentre lo que se nombra distinto | Es la limitación conocida; la resuelve HU-004 |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Se busca por palabra sin instalar nada
- [ ] El resultado dice dónde está lo encontrado
- [ ] Los filtros por tipo y alcance funcionan
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita lo guardado de HU-002 |
| **N**egociable | Sí | Los filtros se pueden discutir |
| **V**aliosa | Sí | Sin búsqueda, guardar no sirve |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Recorrer y filtrar |
| **T**esteable | Sí | Se prueba con cosas guardadas a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. CA-02, RNF y transversales verificados; CA-01 en «No» porque la búsqueda no dice dónde está lo encontrado. Se propone la fase B con los dos arreglos |
