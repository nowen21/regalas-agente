# Funcionalidad implementada — Fase A-EP-005-HU-008-enganche-del-resumen (módulo Automatismos)

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-008-enganche-del-resumen` |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-008: [CA-01](../HU-008-enganche-del-resumen.md#ca-01--el-archivo-nace-solo), [CA-02](../HU-008-enganche-del-resumen.md#ca-02--avisa-cuando-la-sesión-ya-produjo-algo-y-el-resumen-sigue-vacío), [CA-03](../HU-008-enganche-del-resumen.md#ca-03--del-propósito-se-muestra-lo-que-sigue-abierto-y-nada-más) y los tres [RNF](../HU-008-enganche-del-resumen.md#5-requisitos-no-funcionales) |
| **Fecha de cierre** | Sin cerrar: la fase se **reabrió** el 2026-08-14 |
| **Commit** | `40f9937` el trabajo de la corrida 1; falta el de la corrección |

---

> ## ⚠ Este documento se escribió con la fase cerrada, y la fase se reabrió
>
> Lo de abajo dice que el resumen nace solo al abrir la sesión. **No nacía nunca.** El detalle está en el [resultado de pruebas](resultado_pruebas.md), defecto DEF-03, y en la [ampliación del plan](plan_trabajo.md).
>
> Se reescribe cuando la fase vuelva a cerrar, y para eso falta [CP-018](plan_pruebas.md#cp-018--el-archivo-aparece-solo-en-una-sesión-real): que en una sesión nueva de verdad el archivo aparezca solo.

---

## 1. Qué se implementó — resumen

El resumen de la sesión ya no depende de que nadie se acuerde: nace solo al abrir, avisa qué le falta mientras se trabaja, y muestra el hallazgo que la sesión vino a resolver, con su pregunta viva.

Con esto queda cerrada la cadena del hallazgo H-4 del 2026-08-14, que decía que lo aprendido en una sesión no tenía dónde escribirse. Ahora tiene modelo, tiene sitio, se encuentra desde el índice y lo sostiene un programa.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · el archivo se crea al abrir | programa | `validadores/resumen.py` · `crear()` | ✅ | CP-001 |
| RN-02 · se renombra con la transcripción | programa | `validadores/historico.py` · `_mover_resumen()` | ✅ | CP-003 |
| RN-03 · avisa una vez por hueco | programa | `validadores/resumen.py` · `falta()` y `marcar_avisado()` | ✅ | CP-004 y CP-007 |
| RN-04 · el aviso dice qué falta | programa | `validadores/hook_resumen.py` · `aviso()` | ✅ | CP-004 |
| RN-05 · para cerrar cuentan los del propósito | programa | `validadores/resumen.py` · `proposito()` | ✅ | CP-006 |
| RN-06 · se muestra lo abierto del propósito y nada más | programa | `validadores/resumen.py` · `proposito()` | ✅ | CP-006 |
| RN-07 · no escribe hallazgos | programa | `validadores/resumen.py` · `_desde_modelo()` | ✅ | CP-001, y el defecto DEF-01 que lo destapó |
| RN-08 · no detiene el trabajo | programa | `validadores/hook_resumen.py` · `main()` | ✅ | CP-009 |
| RN-09 · no modifica un hallazgo escrito | programa | `validadores/resumen.py` | ✅ | CP-001 |
| Instalación en cada proyecto | programa | `validadores/instalar.py` · `HOOKS_CLAUDE` | ✅ | Los dos enganches en `.claude/settings.json` |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Dónde va el archivo y cómo se llama | ✅ hecha | `resumen.py` · `ruta_de()` | CP-001 |
| T-02 | Crearlo con el modelo y no pisarlo | ✅ hecha | `resumen.py` · `crear()` | CP-001 |
| T-03 | El enganche de `SessionStart` | ✅ hecha | `hook_resumen.py` · `inicio()` | Corrida real sobre esta sesión |
| T-04 | Que `renombrar()` mueva también el resumen | ✅ hecha | `historico.py` · `_mover_resumen()` | CP-003 |
| T-05 | Pruebas de creación y renombrado | ✅ hecha | `pruebas.py` | 5 casos |
| T-06 | Detectar que la sesión produjo algo | ✅ hecha | `hook_resumen.py` · `_produjo_algo()` | CP-004, por los dos caminos |
| T-07 | Detectar qué le falta al resumen | ✅ hecha | `resumen.py` · `falta()` | CP-004 y CP-005 |
| T-08 | Imprimir el aviso con la lista y marcar | ✅ hecha | `hook_resumen.py` · `aviso()` | CP-004 |
| T-09 | Pruebas del aviso | ✅ hecha | `pruebas.py` | 4 casos |
| T-10 | Encontrar el hallazgo del propósito | ✅ hecha | `resumen.py` · `proposito()` | CP-006 |
| T-11 | Imprimirlo y no imprimir otros temas | ✅ hecha | `hook_resumen.py` · `inicio()` | CP-006 |
| T-12 | Pruebas del propósito | ✅ hecha | `pruebas.py` | 3 casos |
| T-13 | Sale con código 0 aunque no pueda escribir | ✅ hecha | `hook_resumen.py` · `main()` | CP-009 |
| T-14 | El aviso no se repite | ✅ hecha | `resumen.py` · `marcar_avisado()` | CP-007 |
| T-15 | Medir lo que suma al arranque | ✅ hecha | — | CP-008: 0,13 s |
| T-16 | Dos filas en `HOOKS_CLAUDE` y correr el instalador | ✅ hecha | `instalar.py` · `.claude/settings.json` | Los dos enganches puestos |
| T-17 | Documentar y pasar `DOC22` a hecha | ✅ hecha | `validadores/README.md` · `reglas-validables.md` | Las dos entradas |
| T-18 | `CHANGELOG.md` y `VERSION` | ✅ hecha | — | Versión 15.1.0 |

**Correspondencia con el plan:** 18 tareas en el plan, 18 acá. Cuadra.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**  ·  [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| Ninguno | — | — |

Es la primera fase de la sesión que no necesitó ampliar el plan. La diferencia estuvo en §2: el análisis leyó los siete enganches que ya corrían y la tabla del instalador antes de escribir nada.

**Esfuerzo real contra estimado:** 31 h estimadas.

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

- **Fuente:** [resultado_pruebas.md](resultado_pruebas.md) · **Veredicto:** Cumple.
- **Suites corridas + resultado:** `validadores/pruebas.py`, 226 casos con una falla ajena a esta fase (la regla `G9` que otra sesión está escribiendo), y `validar.py estandar` en 0 fallas.
- **Verificaciones manuales** ([`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)):
  - Correr el enganche de arranque contra esta sesión real y comprobar que encuentra su propósito.
  - Renombrar una sesión en un proyecto de juguete y verificar que se mueven los dos archivos y los dos índices.
  - Medir lo que suma al arranque contra el enganche que ya existía.
- **Defectos abiertos que se aceptaron:** ninguno. Los dos que aparecieron se corrigieron dentro de la fase.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

- **Punto de entrada:** no hay que hacer nada. Al abrir la sesión el archivo aparece en `historico-chat/resumenes/AAAA-MM-DD/`, y los avisos llegan solos.
- **Permisos o datos base sembrados:** N/A.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / `DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El enganche crea, avisa y muestra; no escribe hallazgos | Reconocer un hallazgo es criterio. Lo que un programa puede hacer es que el hueco se vea | `validadores/resumen.py` |
| "Produjo algo" se mide contra git | Se descartó contar archivos escritos: escribir un borrador no es producir | `validadores/hook_resumen.py` |
| El aviso sale una vez por hueco, máximo dos | Se descartó el aviso único: dejaba pasar el caso de escribir un hallazgo y no decir nunca si la sesión cierra | `validadores/resumen.py` |
| La marca del aviso vive dentro del resumen | Un archivo de estado aparte se desincroniza y hay que limpiarlo | `validadores/resumen.py` |
| Solo se muestra lo abierto del propósito | Mostrar todo lo abierto es ruido, y el ruido se deja de leer | `validadores/resumen.py` |
| El resumen se mueve antes que la transcripción | Si algo falla, lo que queda mal es el resumen y no el índice, que es por donde la próxima sesión llega | `validadores/historico.py` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El aviso mira si la sección de cierre está llena, no si el tema cerró de verdad | Diferido por el plan | La pregunta viva de H-4: con qué señal se sabe que un tema cerró |
| Los siete enganches viejos siguen sin especificación de módulo | Diferido por el plan | [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md) pide retro-documentarlos |
| La suite queda con una falla que no es de esta fase | Cambio del entorno | La regla `G9` que otra sesión está escribiendo en `base/09-git.md` |

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / `DOC13`

- [x] `validadores/README.md` con los dos programas nuevos.
- [x] `validadores/reglas-validables.md`: `DOC22` pasa a la lista de hechas en lo que un programa sí puede comprobar.
- [x] `plantillas/historico-chat.md` dice que el resumen también lo crea un enganche.
- [x] Especificación del módulo al día con lo realmente implementado.
- [ ] Mapa de dependencias vivo (`DOC9`): N/A, este repositorio no lo tiene.
- [ ] Catálogo de módulos (`DOC13`): N/A, este repositorio no lo tiene.

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

- Cambios de esquema / migraciones: N/A.
- Datos base / permisos: N/A.
- Comandos post-deploy: `python validadores/instalar.py <proyecto> --aplicar`, que conecta los dos enganches.
- Reversión: revertir el commit y correr el instalador otra vez. Los resúmenes ya creados no se borran: son documentos del usuario, no artefactos del programa.
