# HU-010 — El capítulo que rige lo que se escribe llega al escribirlo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-010 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Done |

---

## 2. Narrativa

- **Como** quien aprueba un plan y espera que se ejecute como dice el estándar
- **Quiero** que el capítulo que gobierna el documento que se está escribiendo llegue completo en ese momento
- **Para** que la regla esté delante cuando se decide, y no después de haberla incumplido

---

## 3. Contexto y descripción

Cargar `base/` entero en cada arranque no cabe: son 369 KB. Cargar solo lo que rige cada frase ([HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md)) deja fuera el capítulo más pesado y más operativo: [`02 · flujo de trabajo`](../../../../base/02-flujo-de-trabajo/base.md), 88 KB, que dice qué se pregunta, qué se edita, qué se aprueba y cómo se cierra una fase.

Ese capítulo no hace falta siempre: hace falta **cuando se está trabajando una fase**. Y eso se sabe sin adivinar, porque ya hay un enganche que corre en cada escritura y sabe qué archivo se escribió ([`instalar.py:186`](../../../../validadores/instalar.py)). Un `plan_trabajo.md` dice que se está planificando; un `resultado_pruebas.md`, que se está cerrando; un archivo de `base/`, que se está tocando el cuerpo de reglas.

El 2026-08-14 el agente ofreció dos opciones donde [`02·F9`](../../../../base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md) manda reportar un hallazgo. Tenía la línea del índice de esa regla, no su texto.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Al escribir un archivo, llega completo el capítulo que gobierna ese tipo de archivo |
| RN-02 | La correspondencia entre tipo de archivo y capítulo está escrita en un solo sitio, no repartida en el programa |
| RN-03 | Lo que ya llegó en esta sesión no se vuelve a mandar: se dice que ya está |
| RN-04 | Un archivo que no le toca a ningún capítulo no dispara nada, y en silencio |
| RN-05 | No modifica el archivo que se escribió |

### 3.2 Supuestos

- El enganche de escritura sabe qué archivo se escribió, y ya lo usa para comprobar enlaces.

### 3.3 Fuera de alcance

- Lo que llega al abrir la sesión, que es [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md).
- Comprobar si la regla se cumplió, que es EP-004.
- Detener el trabajo, que es [HU-003](../HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md).

---

## 4. Criterios de aceptación

### CA-01 — Al escribir llegan las reglas relacionadas

```gherkin
Dado que se escribe o se cambia un documento que un capítulo gobierna
Cuando termina de escribirse
Entonces llegan las reglas relacionadas: el capítulo dueño, las que citan al documento
  y las que él cita
```

**Cómo validarlo:**

1. Escribir un `plan_trabajo.md` en un proyecto de prueba. Resultado esperado: llegan las reglas del capítulo `02` que gobiernan el plan.
2. Cambiar una regla de `base/` que cite a otra. Resultado esperado: **llega la citada**, aunque viva en otro capítulo.
3. Comprobar que también llegan **las que la citan a ella**, que es por donde se rompe algo sin notarlo.
- **Aprobado cuando:** lo que se relaciona con lo que se está tocando está delante, sin ir a buscarlo.

> **Cambiado el 2026-08-18.** Antes decía *«llega completo el capítulo»*, que era la forma que se veía cuando se escribió la historia. Con el índice de [`citas.py`](../../../../validadores/citas.py) y las dependencias de [`metareglas.py`](../../../../validadores/metareglas.py) ya construidos, **mandar el capítulo entero es la forma cara de resolver algo que una consulta resuelve mejor**: el capítulo `02` pesa 98 KB y obliga a encontrar la regla uno mismo.
>
> **Y hay una diferencia que decide:** el capítulo completo solo trae a los vecinos del mismo capítulo. La consulta **cruza capítulos** — que es donde estaba el choque de `02·F2` con `02·F0`, y donde está la relación de `20·M17` con `00·ID7`.

### CA-02 — No se repite lo que ya llegó

```gherkin
Dado que un capítulo ya llegó en esta sesión
Cuando se escribe otro archivo del mismo tipo
Entonces no se manda otra vez
```

**Cómo validarlo:**

1. Escribir dos planes seguidos.
2. Resultado esperado: el capítulo llega una vez; la segunda solo se recuerda que ya está.
- **Aprobado cuando:** no se llena la sesión de texto repetido.

### CA-03 — Lo que no le toca no dispara nada

```gherkin
Dado que se escribe un archivo que ningún capítulo gobierna
Cuando termina de escribirse
Entonces no llega nada y no se dice nada
```

**Cómo validarlo:**

1. Escribir un archivo cualquiera fuera de la documentación.
2. Resultado esperado: silencio.
- **Aprobado cuando:** el que trabaja en otra cosa no recibe reglas que no le tocan.

### Criterios de aceptación transversales

- [ ] **Inocuidad** — no modifica el archivo escrito.
- [ ] **Límites** — un proyecto sin `base/` no se ve afectado.
- [ ] **Errores** — si el capítulo no se puede leer, se dice y el trabajo sigue.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Oportunidad** | Llega en el mismo momento de la escritura, no después |
| RNF-02 | **Silencio** | Una vez por capítulo y por sesión |
| RNF-03 | **Rendimiento** | No demora la escritura del archivo |

---

## 6. Diseño y referencias

- **Documento funcional:** el hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen`.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la correspondencia entre tipo de archivo y capítulo, en un solo sitio.
- [ ] Que el enganche de escritura mande el capítulo que corresponde.
- [ ] Llevar la cuenta de lo que ya llegó en la sesión.
- [ ] Medir lo que suma a la escritura.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo](A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase construye.** El disparo existe y lo que hace es comprobar enlaces: al escribir un plan de trabajo, el capítulo que lo rige no llega. El límite es el costo — el arranque ya pesa unos 73 KB, medidos en la fase A de HU-009.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md), que define cómo se decide qué llega puesto | Medio |
| Dependencia | [HU-003](../HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md), que es el enganche que ya corre al escribir | Alto |
| Riesgo | Que el capítulo llegue tarde, cuando el documento ya está escrito | Llega igual: lo que se escribió se puede corregir, y lo que sigue ya nace con la regla puesta |
| Riesgo | Que la correspondencia crezca y nadie la mantenga | Vive en un solo archivo, y un tipo sin capítulo no dispara nada |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Al escribir un documento de fase llega su capítulo completo
- [ ] No se repite dentro de la misma sesión
- [ ] Lo que no le toca no dispara nada
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Se apoya en el enganche de HU-003 |
| **N**egociable | Sí | Qué archivo trae qué capítulo se puede discutir |
| **V**aliosa | Sí | Es la que evita el incumplimiento, en vez de detectarlo después |
| **E**stimable | Sí | Una correspondencia y un cambio en el enganche |
| **S**mall (pequeña) | Sí | Un comportamiento |
| **T**esteable | Sí | Se escribe un archivo y se mira qué llegó |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen` |
