# Plan de Pruebas · «alcance»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

| Campo | Valor |
|---|---|
| **Código** | PP-000 |
| **Versión** | 1.0 |
| **Alcance del plan** | Proyecto / Release / Épica EP-000 / HU-000 |
| **Fecha** | AAAA-MM-DD |
| **Elaborado por** | «Nombre — QA Lead» |
| **Revisado por** | «Nombre» |
| **Aprobado por** | «Nombre — PO» |
| **Estado** | Borrador / Aprobado / En ejecución / Cerrado |

> Plantilla del `plan_pruebas`, basada en ISO/IEC/IEEE 29119-3. Va junto con el `plan_trabajo` de la fase (`planes/trabajo.md`) y se guarda en la carpeta de la fase (ruta `02·F12.13`) como `plan_pruebas.md`.
>
> Proporcionalidad: este formato completo es para un release o una épica. Para una sola fase o HU se usan solo las secciones **3, 5, 6, 9 y 12**, y el resto es opcional. Una fase chica no se infla con un plan de release.
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta. El párrafo «Para qué sirve este documento» se queda.

## 1. Introducción

> Presenta el plan: qué busca, qué abarca y en qué documentos se apoya.

### 1.1 Propósito

> Es la razón de ser del plan, en una o dos frases.

«Qué se busca validar con este plan y ante quién responde.»

### 1.2 Alcance

> Separa lo que este plan prueba de lo que deja por fuera, para que nadie dé por probado lo excluido.

**Se prueba**
- «Módulo, funcionalidad, integración incluida»

**No se prueba**
- «Exclusión explícita y su justificación»

### 1.3 Documentos de referencia

> Son los documentos contra los que se diseñan los casos, con dónde encontrar cada uno.

| Documento | Ubicación |
|---|---|
| Historias de usuario / Épica | «enlace» |
| Contrato de API | «enlace» |
| Diseño / Prototipos | «enlace» |
| Normativa aplicable | «enlace» |

## 2. Elementos a probar

> Son los componentes o módulos que el plan cubre, con su versión y quién los desarrolla.

| ID | Componente / Módulo | Versión | Responsable de desarrollo |
|---|---|---|---|
| CMP-01 | | | |
| CMP-02 | | | |

## 3. Estrategia de pruebas

> Dice cómo se va a probar: en qué niveles, de qué tipos, con qué técnicas, con qué prioridades y qué suites se corren.

### 3.1 Niveles de prueba

> Son las capas en que se prueba, de la función aislada a la aceptación del usuario, con quién prueba cada una y dónde.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | Lógica aislada de funciones y servicios | Desarrollo | Local | Sí |
| Integración | Interacción entre componentes y BD | Desarrollo / QA | DEV | Parcial |
| Sistema | Flujos completos end-to-end | QA | QA | Parcial |
| Aceptación (UAT) | Validación del usuario final | Usuario clave | QA / Staging | No |
| Regresión | Que lo existente siga funcionando | QA | QA | Sí |

### 3.2 Tipos de prueba

> Marca con ☑ los tipos de prueba que aplican a este alcance y con ☐ los que no, con el criterio que se comprueba en cada uno.

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Criterios de aceptación de las HU |
| Seguridad | ☐ | Autenticación, autorización, OWASP Top 10 |
| Rendimiento | ☐ | Tiempo de respuesta y carga concurrente |
| Usabilidad | ☐ | Flujo comprensible sin capacitación |
| Compatibilidad | ☐ | Navegadores y dispositivos soportados |
| Accesibilidad | ☐ | WCAG 2.1 nivel «A/AA» |
| Migración de datos | ☐ | Integridad y completitud |
| Recuperación | ☐ | Comportamiento ante fallo y rollback |

### 3.3 Técnicas de diseño de casos

> Son las técnicas con que se sacan los casos a partir de los criterios de aceptación.

- Partición de equivalencia: clases válidas e inválidas de cada entrada.
- Valores límite: mínimo, mínimo±1, máximo, máximo±1, vacío, nulo.
- Tabla de decisión: combinaciones de reglas de negocio.
- Transición de estados: flujos con estados (borrador → aprobado → anulado).
- Pruebas exploratorias: sesiones con carta de exploración documentada.

### 3.4 Priorización

> Define cuánta cobertura se exige en cada nivel de prioridad. La prioridad de cada caso sale de esta tabla.

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Crítica | Flujo principal de negocio o riesgo legal | 100% |
| Alta | Funcionalidad frecuente | 100% |
| Media | Funcionalidad secundaria | ≥ 80% |
| Baja | Casos poco frecuentes | Según tiempo |

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

> Fija qué suites corre la ejecución de la fase y cuáles quedan fuera.

La ejecución de una fase corre solo lo que la fase toca, no la suite completa por si acaso:

1. La suite del módulo nuevo o refactorizado (obligatoria).
2. Las suites que la fase refactorizó explícitamente, declaradas en el `plan_trabajo`.
3. Las suites que dependen directamente de los archivos tocados (matriz de dependencias del refactor, [`02·F17`](../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)).

Por defecto no se corre la suite entera del proyecto ni los módulos ajenos a la matriz. Una regresión total se declara aparte y de forma explícita (por ejemplo, antes de un release), fuera del flujo normal de la fase.

## 4. Criterios de entrada y salida

> Fijan cuándo puede empezar la ejecución, cuándo se da por terminada y cuándo se detiene.

### 4.1 Criterios de entrada

> Son las condiciones que deben cumplirse antes de ejecutar el primer caso.

- [ ] Build desplegado y estable en el ambiente de pruebas
- [ ] Criterios de aceptación de las HU documentados
- [ ] Casos de prueba diseñados y revisados
- [ ] Datos de prueba cargados
- [ ] Ambiente y accesos disponibles
- [ ] Pruebas unitarias del desarrollador pasando

### 4.2 Criterios de salida

> Son las condiciones que deben cumplirse para dar la ejecución por terminada.

- [ ] 100% de los casos críticos y altos ejecutados
- [ ] ≥ «95»% de casos ejecutados en total
- [ ] 0 defectos abiertos de severidad crítica o alta
- [ ] Defectos medios y bajos documentados y aceptados por el PO
- [ ] Pruebas de regresión ejecutadas sin nuevos hallazgos
- [ ] Informe de pruebas emitido y aprobado

### 4.3 Criterios de suspensión y reanudación

> Dicen cuándo se detiene la ejecución y qué tiene que pasar para retomarla.

**Suspender si:** el ambiente cae, un defecto bloqueante impide más del «30»% de los casos, o el build no cumple las pruebas de humo.
**Reanudar cuando:** se despliegue una corrección verificada y las pruebas de humo pasen.

## 5. Matriz de trazabilidad

> Cruza cada exigencia de la HU con los casos que la prueban. Ningún criterio de aceptación ni requisito no funcional queda sin al menos un caso, y los `RNF-0N` van en esta misma tabla, con su fila propia.
>
> Cada `CP-00N` se escribe como enlace a su caso de §6, y cada `CA-0N` o `RNF-0N` como enlace a su exigencia en la HU, aquí y en el `resultado_pruebas`. Un identificador suelto obliga a buscarlo a mano, y así se termina juzgando un caso sin haber leído lo que exigía.

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | [CP-001](#cp-001--título-del-caso), [CP-002](#cp-002--título-del-caso-negativo) | Funcional | Crítica | Sí | ☐ |
| HU-001 | CA-02 | «CP-003» | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF-01 | «CP-004» | Seguridad | Crítica | No | ☐ |
| HU-002 | CA-01 | «CP-005» | Funcional | Alta | No | ☐ |

**Cobertura:** «n» de «n» exigencias cubiertas = «%». Cuentan los `CA-0N` y los `RNF-0N`, cada uno por separado.

## 6. Casos de prueba

> Detalla cada caso, un bloque por caso: a qué exigencia responde, con qué estado y datos arranca, qué pasos sigue y qué resultado espera. El resultado de correrlo no se anota aquí: va en el `resultado_pruebas.md` de la fase (plantilla `planes/resultados.md`).

### CP-001 · «Título del caso»

> Es el caso del camino feliz: su ficha, sus pasos y el resultado esperado.

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | «Estado previo del sistema y datos requeridos» |
| **Datos de entrada** | «Valores concretos» |
| **Diseñado por** | |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «Acción del usuario» | «Respuesta del sistema» |
| 2 | | |
| 3 | | |

**Un paso, una acción.** Cada fila lleva un solo verbo y un solo resultado esperado. Dos acciones en la misma fila comparten un único renglón de resultado: al ejecutar se registra el de la segunda y el de la primera se pierde, sin que nadie lo note.

```
INCORRECTO: | 1 | Tomar la lista de origen y contar cuántos términos tiene | Queda un número por grupo |
            — se anota el conteo y no queda rastro de qué lista se tomó
CORRECTO:   | 1 | Tomar la lista de origen                | Queda a la vista, con su archivo |
            | 2 | Contar cuántos términos tiene por grupo | Queda un número por grupo        |
```

**Resultado esperado final:** «Estado observable del sistema»
**Postcondiciones:** «Registros creados, estados modificados, eventos de auditoría»

### CP-002 · «Título del caso negativo»

> Es el caso negativo: entra con datos inválidos a propósito para comprobar la validación.

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Funcional — validación |
| **Prioridad** | Alta |
| **Precondiciones** | |
| **Datos de entrada** | «Datos inválidos deliberados» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | | «Mensaje de error específico; el estado no cambia» |

## 7. Datos y ambientes de prueba

> Dice dónde se prueba, con qué datos y con qué usuarios, y qué no alcanza a reproducir el entorno.

### 7.1 Ambientes

> Son los ambientes donde corren las pruebas, con qué datos cuenta cada uno y quién responde por él.

| Ambiente | URL | Uso | Versión de datos | Responsable |
|---|---|---|---|---|
| DEV | | Integración continua | Sintéticos | |
| QA | | Pruebas de sistema | Copia anonimizada | |
| Staging | | UAT y regresión | Réplica de producción | |

### 7.2 Datos de prueba

> Son los conjuntos de datos que usan los casos, de dónde salen y si requieren anonimización. Ningún dato personal real entra sin anonimizar a un ambiente distinto de producción ([`00·N4`](../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada), `12` privacidad). La norma de protección de datos que aplica se declara en `.agente/marco-normativo.md`; aquí no se asume una jurisdicción.

| Conjunto | Descripción | Origen | Anonimización |
|---|---|---|---|
| DS-01 | «Usuarios y roles de prueba» | Script `seed.sql` | N/A |
| DS-02 | «Registros de negocio» | Copia de producción | Requerida |

### 7.3 Usuarios de prueba

> Son las cuentas de prueba por rol, con sus permisos y para qué se usa cada una.

| Usuario | Rol | Permisos | Propósito |
|---|---|---|---|
| `qa.admin` | Administrador | Todos | Flujos completos |
| `qa.operador` | Operador | Limitados | Verificar restricciones |
| `qa.consulta` | Consulta | Solo lectura | Pruebas negativas de autorización |

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

> Lista lo que el entorno automático no cubre y por eso exige verificación manual documentada.

- «Integraciones externas reales, comportamiento del navegador, permisos del SO, symlinks/rutas especiales, concurrencia real, archivos con encoding/tamaño extremos, rendimiento sobre volúmenes reales, etc.»

## 8. Herramientas

> Son las herramientas que se usan en cada propósito y quién responde por cada una.

| Propósito | Herramienta | Responsable |
|---|---|---|
| Gestión de casos y defectos | «Jira / Azure Test Plans» | |
| Automatización UI | «Playwright / Cypress / Selenium» | |
| Automatización API | «Postman / pytest / RestAssured» | |
| Pruebas unitarias | «pytest / PHPUnit / Jest» | |
| Rendimiento | «k6 / JMeter» | |
| Análisis estático y seguridad | «SonarQube / OWASP ZAP» | |
| Cobertura de código | «coverage.py / Istanbul» | |

## 9. Gestión de defectos

> Dice cómo se clasifica, se reporta, se sigue y se registra cada defecto que aparezca al ejecutar.

### 9.1 Clasificación por severidad

> Define cada nivel de severidad y en cuánto tiempo se atiende un defecto de ese nivel.

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Crítica** | Bloquea el flujo principal, pérdida de datos o brecha de seguridad | Inmediato |
| **Alta** | Funcionalidad importante inoperante sin alternativa | 24 h |
| **Media** | Falla con alternativa disponible | Dentro del sprint |
| **Baja** | Cosmético o de bajo impacto | Backlog |

### 9.2 Flujo del defecto

> Son los estados por los que pasa un defecto, desde que se reporta hasta que se cierra o se reabre.

```
Nuevo → Asignado → En corrección → Listo para pruebas → Verificado → Cerrado
                                                       ↘ Reabierto ↗
```

### 9.3 Contenido mínimo de un reporte

> Es lo que trae todo reporte de defecto para que otra persona lo pueda reproducir.

- ID, título descriptivo, severidad y prioridad
- Ambiente, build y usuario utilizado
- Pasos exactos para reproducir
- Resultado esperado frente al resultado obtenido
- Evidencia (captura, log, request/response)
- Caso de prueba y HU asociados

### 9.4 Registro

> Es la lista de los defectos encontrados, cada uno con el caso que lo destapó, su severidad y su estado.

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| DEF-01 | | CP-001 | Alta | Abierto | | | |

## 10. Cronograma

> Ubica en el tiempo cada actividad de pruebas, del diseño de casos al informe de cierre, con su responsable.

| Actividad | Inicio | Fin | Responsable |
|---|---|---|---|
| Diseño de casos de prueba | | | QA |
| Preparación de ambiente y datos | | | DevOps / QA |
| Ejecución — ciclo 1 | | | QA |
| Corrección de defectos | | | Desarrollo |
| Ejecución — ciclo 2 (reprueba) | | | QA |
| Pruebas de regresión | | | QA |
| UAT | | | Usuario clave |
| Informe y cierre | | | QA Lead |

## 11. Roles y responsabilidades

> Dice quién hace qué en el proceso de pruebas.

| Rol | Responsabilidad |
|---|---|
| QA Lead | Elabora el plan, define estrategia, aprueba el cierre |
| Analista de pruebas | Diseña y ejecuta casos, reporta defectos |
| Desarrollador | Pruebas unitarias, corrige defectos |
| Product Owner | Aprueba criterios de salida y acepta defectos residuales |
| Usuario clave | Ejecuta UAT y firma la aceptación |
| DevOps | Provisiona ambientes y despliega builds |

## 12. Métricas e informe

> Define qué se mide de la ejecución y dónde queda lo que dio.

### 12.1 Métricas

> Son las métricas del proceso de pruebas, con su fórmula y la meta que el plan fija.

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) totales | 100% |
| Casos ejecutados | Ejecutados / diseñados | ≥ 95% |
| Tasa de aprobación | Aprobados / ejecutados | ≥ 95% |
| Densidad de defectos | Defectos / punto de historia | ≤ «n» |
| Efectividad de detección | Defectos en QA / (QA + producción) | ≥ 90% |
| Tasa de reapertura | Reabiertos / corregidos | ≤ 10% |

### 12.2 Dónde se miden

> Dice en qué documento queda el resultado de las métricas.

El resumen de la ejecución, el veredicto por criterio y el concepto final van en el `resultado_pruebas.md` de la fase (plantilla `planes/resultados.md`), porque son resultado de ejecutar. Este plan define qué se va a medir; aquel documento dice cuánto dio.

## 13. Riesgos del proceso de pruebas

> Son los riesgos que pueden frenar la ejecución de las pruebas, su impacto y cómo se mitigan.

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RP-01 | Ambiente inestable | Retrasa la ejecución | Ventana de despliegue acordada |
| RP-02 | Datos insuficientes | Casos no ejecutables | Scripts de carga versionados |
| RP-03 | Entrega tardía de desarrollo | Compresión del ciclo | Pruebas por incrementos |

## 14. Control de versiones

> Registra cada versión de este plan: cuándo, quién la hizo y qué cambió.

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0 | | | Versión inicial |

## 15. Aprobación

> Recoge la firma de quienes aprueban el plan.

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| QA Lead | | | |
| Product Owner | | | |
| Líder técnico | | | |
