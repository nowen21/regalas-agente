# Plan de Pruebas · Fase `B-EP-023-HU-007-el-freno-detiene-antes-y-despues-de-actuar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU007-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-007: CA-02, capas 1 y 2 |
| **Fecha** | 2026-10-03 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-10-03 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El freno antes y después de actuar, y el hallazgo anotado | Claude | Proyecto de prueba con git en una carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-02 |
| Seguridad | ☑ | Nada se escribe fuera del proyecto ni del plan |

### 3.3 Técnicas de diseño de casos

- Partición por canal: herramienta de escritura, consola, segundo plano, publicación y programa que escribe por dentro; y por estado de la fase: sin aprobar, aprobada y sin fase.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-02 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_el_freno.py`; las de los programas que cambia: las del instalador y las del enganche de antes; `validar.py estandar`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-02 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-004 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-02 | CP-005 | Funcional | Alta | Sí | ☑ |
| HU-007 | RNF-06 | CP-006 | Trazabilidad | Media | Parcial | ☑ |

**Cobertura:** 1 de 1 criterio de esta fase, en sus capas 1 y 2, y el RNF-06.

## 6. Casos de prueba

### CP-001 · Herramienta de escritura

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Precondiciones** | T-01, T-03 y T-05 terminadas |
| **Datos de entrada** | Una fase en curso con plan sin aprobar y luego aprobado; una regla que autoriza el resumen |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sin aprobar el plan, escribir el plan de pruebas de la fase | Pasa |
| 2 | Sin aprobar el plan, escribir un archivo de código | Se detiene |
| 3 | Con el plan aprobado, escribir un archivo que declara | Pasa |
| 4 | Con el plan aprobado, escribir uno que no declara | Se detiene |
| 5 | Sin fase en curso, escribir el resumen de la sesión y luego un archivo de código | El resumen pasa y el código se detiene |
| 6 | Sin fase en curso, escribir una HU | Pasa: la autoriza `13·DOC15` |
| 7 | Con un análisis prendido cuya fila «de una y sin fase» nombra un archivo, escribirlo | Pasa |
| 8 | Escribir fuera del proyecto, también con `..` o `~` | Se detiene |
| 9 | Leer el enganche que pone el instalador | Corre sobre toda acción |

### CP-002 · Consola

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Precondiciones** | T-01 y T-03 terminadas |
| **Datos de entrada** | La misma fase, con el plan aprobado |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Redirigir la salida a un archivo que el plan no declara | Se detiene |
| 2 | Copiar, mover o borrar un archivo que el plan no declara | Se detiene |
| 3 | Correr una orden en segundo plano | Se detiene |
| 4 | Instalar un paquete global o cambiar la configuración global de git | Se detiene |
| 5 | Dejar un proceso corriendo después del turno | Se detiene |
| 6 | Una orden que solo lee, como `git status` | Pasa |

### CP-003 · Lo que se publica

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Precondiciones** | T-01 y T-03 terminadas |
| **Datos de entrada** | Una herramienta que publica fuera del proyecto |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Usarla | El freno pregunta antes de actuar |

### CP-004 · Después de actuar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Un archivo ya cambiado antes de la orden |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Un programa escribe por dentro un archivo que el plan no declara | Avisa el hallazgo |
| 2 | Escribe uno que el plan declara | No avisa nada |
| 3 | El archivo que ya estaba cambiado antes de la orden | No cuenta |

### CP-005 · El hallazgo queda anotado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Precondiciones** | T-02 y T-03 terminadas |
| **Datos de entrada** | Una sesión con su transcripción y su resumen |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | El freno detiene una escritura | El resumen suma el hallazgo con qué pasó y por qué importa, y el mensaje dice que se vuelve al análisis |

### CP-006 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Algo fuera del plan pasa, o algo permitido se detiene | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios y RNF con caso / criterios y RNF de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
