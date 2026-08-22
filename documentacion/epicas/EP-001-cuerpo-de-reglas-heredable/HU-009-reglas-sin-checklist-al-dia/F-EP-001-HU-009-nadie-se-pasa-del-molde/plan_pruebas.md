# Plan de Pruebas — Fase F-EP-001-HU-009-nadie-se-pasa-del-molde

**Para qué sirve este documento.** Dice **con qué se comprueba** que la fase quedó bien antes de darla por cerrada: qué caso cubre cada criterio de aceptación, cómo se ejecuta y qué resultado se espera. Lo ejecutado y lo que dio está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba, y qué no

**Se prueba** que ninguna regla queda publicada reprobando su checklist, que ningún sello afirma algo que su regla ya no dice, que las citas y enlaces siguen resolviendo, y que **ninguna exigencia cambió** al recortar.

**No se prueba** que la regla recortada sea mejor prosa: eso lo juzga quien la lee. Tampoco se prueban las 21 fases de retrodocumentación de capítulos, que son de otra historia.

## 1. Alcance de ejecución ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

La fase toca `base/`, `notas/`, `CHANGELOG.md` y `VERSION`. Se corren las suites del estándar y la batería completa del `pre-push`; no se corre la suite de la interfaz, que esta fase no toca.

## 2. Trazabilidad criterio a caso ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| CA de HU-009 | Caso | Tipo |
|---|---|---|
| CA-01 · ninguna regla publicada reprueba su checklist | P-01, P-02 | automática |
| CA-01 · el sello dice la verdad sobre el cuerpo de hoy | P-03 | automática |
| transversal · no regresión del cuerpo de reglas | P-04, P-05, P-06 | automática |
| transversal · la exigencia no cambia al recortar | P-07 | manual documentada |

## 3. Los casos

### P-01 · Ninguna regla en NO CUMPLE

```
python validadores/validar.py metareglas
```

**Esperado:** cero fallas. Al abrir la fase daba 27, una por cada regla publicada con el sello en NO CUMPLE.

### P-02 · Ninguna regla pasada del molde

```
python validadores/validar.py metareglas
```

**Esperado:** ningún aviso «el cuerpo de X mide N caracteres». Al abrir la fase había 34.

### P-03 · Ningún sello vencido

Lo comprueba el mismo subcomando: un sello está vencido cuando el archivo se tocó después de su fecha **y** el cuerpo guardado ya no coincide con el de la regla.

**Esperado:** ninguno, porque cada regla tocada se volvió a sellar con la fecha y la versión del día.

### P-04 · Los enlaces y las citas resuelven

```
python validadores/validar.py estandar
```

**Esperado:** sin incumplimientos. Es el caso que cubre el riesgo `F-03`: mover el cuerpo de `F12`, `DOC11` y `M6` a un anexo deja citas apuntando a lo que se movió.

### P-05 · El texto heredable no gana marcas de generación automática

```
python validadores/validar.py marcas --preparados
```

**Esperado:** sin fallas en lo que se va a guardar. Los anexos nuevos arrastran la puntuación del texto que se movió, y esa es justo la que el trinquete detiene.

### P-06 · La versión y el registro de cambios acompañan

```
python validadores/validar.py versionado
```

**Esperado:** cero fallas. Cada unidad de la fase sube `VERSION` y agrega su entrada ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)), escrita para quien no conoce el proyecto ([`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md)).

### P-07 · La exigencia sobrevive al recorte

**Cómo se ejecuta:** para cada regla recortada se compara el cuerpo anterior con el nuevo y se responde una pregunta: **¿qué tendría que hacer distinto un proyecto que ya la cumplía?** Si la respuesta no es «nada», el recorte se llevó una exigencia y se deshace.

**Esperado:** «nada» en las 34. Lo que salió de cada una queda escrito en [notas/porques-recortados-al-molde.md](../../../../../notas/porques-recortados-al-molde.md), que es la evidencia revisable de este caso.

**Por qué es manual.** Ningún programa sabe si dos redacciones exigen lo mismo. La automatizable es su consecuencia, no ella: si el recorte hubiera cambiado la exigencia, el sello quedaría vencido y `P-03` lo vería.

## 4. Criterio de cierre

La fase cierra con **los siete casos en verde**. Si cualquiera falla, se corrige antes de publicar: no se cierra con un caso rojo anotado como pendiente.
