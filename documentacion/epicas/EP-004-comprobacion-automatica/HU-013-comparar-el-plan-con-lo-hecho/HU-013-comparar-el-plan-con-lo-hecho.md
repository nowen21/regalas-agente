# HU-013 — Comparar el plan aprobado con lo que se hizo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-013 |
| **Épica / Feature** | [EP-004 Comprobación automática](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien aprueba un plan
- **Quiero** que un programa avise cuando lo que se hizo no es lo que el plan decía
- **Para** no tener que revisarlo yo documento por documento

---

## 3. Contexto y descripción

Las doce historias de esta épica comprueban un documento **contra su molde**: que no le falten secciones, que los enlaces lleven a algún lado, que los nombres estén bien. Ninguna compara **dos documentos entre sí**.

Y ahí es donde se cuelan los desvíos que importan. El 2026-08-14 una fase cerró con sus tres criterios en "cumple" y el programa no hacía lo que esos criterios piden: los casos se habían corrido llamando por dentro la función, no por donde el plan decía. Nadie lo vio hasta la sesión siguiente, y lo vio una persona.

Lo que hay que comparar no necesita criterio. Son listas:

| Lo que el plan dice | Contra qué se compara |
|---|---|
| Los archivos que declara la sección 2.1 del plan de trabajo | Los archivos que cambiaron de verdad |
| Los casos del plan de pruebas | Los casos del resultado de pruebas |
| Los criterios de la HU | Los criterios con caso ejecutado en el resultado |
| Los pasos de cada caso | Los pasos que el resultado dice que se siguieron |

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un archivo cambiado que el plan no declara es un hallazgo ([`02·F8`](../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)) |
| RN-02 | Un caso que está en el resultado y no en el plan, o al revés, es un hallazgo |
| RN-03 | Un criterio dado por cumplido sin caso ejecutado es un hallazgo |
| RN-04 | Un caso en "cumple" cuyos pasos no son los del plan es un hallazgo: se probó otra cosa |
| RN-05 | El programa **no juzga** si lo que salió es correcto: solo dice si coincide con lo que el plan decía |
| RN-06 | El hallazgo dice qué regla, qué documento y qué se esperaba, como cualquier otro ([EP-004 · HU-003](../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md)) |

### 3.2 Supuestos

- Los documentos de la fase se escriben con las plantillas centrales, así que sus secciones tienen un sitio fijo donde buscar.

### 3.3 Fuera de alcance

- Decidir si el resultado de una prueba es correcto. Eso es criterio.
- Detener el trabajo cuando aparece el hallazgo: eso es [EP-005 · HU-003](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).
- Comprobar la forma de cada documento por separado, que ya es [HU-004](../HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md).

---

## 4. Criterios de aceptación

### CA-01 — Avisa el archivo tocado que el plan no declara

```gherkin
Dado un plan de trabajo aprobado con su lista de archivos
Cuando cambió un archivo que esa lista no nombra
Entonces sale un hallazgo que dice cuál
```

**Cómo validarlo:**

1. Tomar una fase con su plan, y cambiar un archivo que el plan no declara.
2. Correr la comprobación. Resultado esperado: el hallazgo nombra ese archivo.
3. Declararlo en el plan y volver a correr. Resultado esperado: ya no sale.
- **Aprobado cuando:** salirse del plan se nota sin que nadie compare a mano.

### CA-02 — Avisa el caso y el criterio que no cuadran

```gherkin
Dado un plan de pruebas y su resultado
Cuando un caso está en uno y no en el otro, o un criterio se da por cumplido sin caso
Entonces sale un hallazgo por cada uno
```

**Cómo validarlo:**

1. Quitar un caso del resultado y correr la comprobación. Resultado esperado: hallazgo.
2. Marcar un criterio como cumplido sin caso. Resultado esperado: hallazgo.
3. Dejarlos cuadrados. Resultado esperado: ninguno.
- **Aprobado cuando:** no se puede cerrar una fase con una exigencia que nadie probó.

### CA-03 — Avisa el caso cuyos pasos no son los del plan

```gherkin
Dado un caso en "cumple"
Cuando los pasos que el resultado dice que se siguieron no son los del plan
Entonces sale un hallazgo
```

**Cómo validarlo:**

1. Escribir un resultado cuyo paso 1 no coincide con el paso 1 del caso.
2. Correr la comprobación. Resultado esperado: hallazgo que nombra el caso y el paso.
- **Aprobado cuando:** un caso que probó otra cosa no pasa por probado.

### Criterios de aceptación transversales

- [ ] **Inocuidad** — no modifica ningún documento.
- [ ] **Límites** — una fase sin resultado de pruebas todavía no produce hallazgos de este tipo.
- [ ] **Errores** — un documento que no se puede leer se reporta, no rompe la corrida.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Precisión** | Cero falsos positivos por diferencias de redacción: se comparan identificadores y rutas, no frases |
| RNF-02 | **Rendimiento** | Corre sobre una fase en lo que tarda guardar un archivo |

---

## 6. Diseño y referencias

- **Documento funcional:** el hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen`.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Leer del plan de trabajo la lista de archivos declarados.
- [ ] Comparar contra los archivos cambiados.
- [ ] Cruzar los casos del plan de pruebas con los del resultado.
- [ ] Cruzar los criterios de la HU con los casos ejecutados.
- [ ] Comparar los pasos de cada caso con los que el resultado dice.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado](A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**Mitad retro-documentación, mitad construcción.** Ya se compara parte —cada tarea cuelga de un criterio, los dos veredictos se contrastan—, y falta la mitad concreta de `02·F8`: **nadie compara los archivos tocados con los que el plan declaró**.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU-001](../HU-001-criterio-de-lo-comprobable/HU-001-criterio-de-lo-comprobable.md), el criterio de lo que un programa puede comprobar | Medio |
| Dependencia | [HU-003](../HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md), la forma del hallazgo | Medio |
| Riesgo | Que la comparación de pasos dé falsos positivos por redacción | Se comparan identificadores y orden, y lo dudoso se reporta como aviso, no como falla |
| Riesgo | Que el hallazgo salga y nadie lo atienda | Depende de [EP-005 · HU-003](../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md), que decide qué detiene |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Avisa el archivo tocado fuera del plan
- [ ] Avisa el caso y el criterio que no cuadran
- [ ] Avisa el caso cuyos pasos no son los del plan
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Los documentos que compara ya existen |
| **N**egociable | Sí | Qué tan estricta es la comparación de pasos se puede discutir |
| **V**aliosa | Sí | Es lo que habría cazado el defecto que se coló el 2026-08-14 |
| **E**stimable | Sí | Cuatro comparaciones de listas |
| **S**mall (pequeña) | No | Son cuatro comparaciones; puede ir en dos fases |
| **T**esteable | Sí | Se arma una fase de prueba con desvíos sembrados |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen` |
