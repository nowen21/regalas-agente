# Plan de Pruebas · Fase `A-EP-025-HU-005-el-freno-lee-los-niveles`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP025-HU005-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-005: CA-01 a CA-04 |
| **Fecha** | 2026-10-05 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | [Análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El freno con cada nivel y sin base | Claude | Proyectos temporales, lector sustituido | Sí |
| Integración | El lector contra la base | Claude | Base de pruebas en MariaDB | Sí |
| Regresión | Las 308 pruebas del freno | Claude | Proyectos temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02, CA-04 |
| Errores | ☑ | CA-03 |

### 3.3 Técnicas de diseño de casos

- Partición por nivel: frena, avisa, apagada, sin fila.
- Partición por acción: escribe por la herramienta, escribe por consola, solo lee, publica.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02, CA-03 | 100% |
| Media | CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Desde `proyectos/cimiento/`: `python manage.py test core.enganches.tests_freno core.niveles.tests_lectura`, y `PrepararCimiento` de `tests_instalacion.py` importando `core.validadores` primero (pendiente 121).

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | CA-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-005 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-005 | CA-03 | CP-003 | Errores | Alta | Sí | ☐ |
| HU-005 | CA-04 | CP-004 | Funcional | Media | Sí | ☐ |

**Cobertura:** 4 de 4 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Frena, avisa y apagada por proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Precondiciones** | T-01 a T-04 terminadas |
| **Datos de entrada** | Un proyecto sin fase en curso; lector sustituido con `02·F8` en cada nivel |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir un archivo con `02·F8` sin fila | «detiene» por `02·F8` |
| 2 | Con `02·F8` en «avisa» | «avisa» con el motivo de `02·F8` |
| 3 | Con `02·F8` en «apagada» | «deja» sin motivo |
| 4 | Después de una orden que escribió, con «avisa» y con «apagada» | En «avisan» y en ninguna lista, respectivamente |
| 5 | El lector contra la base de pruebas: un proyecto con `02·F8` en «avisa» y otro sin fila | Trae «avisa» para el primero y nada para el segundo; un proyecto inactivo trae nada |
| 6 | Las 308 pruebas de antes | Pasan |

### CP-002 · El núcleo siempre frena

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Lector con `00·N1` en «apagada» |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Publicar con una herramienta que publica | «pregunta», como siempre |
| 2 | Un motivo con `(00·N1)` que detiene | Sigue en «detiene» |

### CP-003 · Sin base

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-03 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Lector que no responde; una fase con plan aprobado que declara el archivo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el archivo declarado | «detiene» con «prender MariaDB» |
| 2 | Una orden que solo lee | «deja» |
| 3 | Después de una orden que escribió | Un aviso de base apagada |
| 4 | El lector real con un puerto sin servidor | `BaseSinRespuesta` con el servidor y el puerto |

### CP-004 · PyMySQL en la instalación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-04 |
| **Precondiciones** | T-07 terminada |
| **Datos de entrada** | La importación de PyMySQL sustituida |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Con PyMySQL | «PyMySQL ya estaba»; no se instala nada |
| 2 | Sin PyMySQL, en simulación | Anuncia que lo instala |
| 3 | Sin PyMySQL, aplicando | Corre `pip install` con el mismo Python |
| 4 | La instalación falla | «OMITIDO» con el motivo |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Una regla del núcleo deja de frenar, o sin base se modifica | Antes de cerrar la fase |
| **Media** | Una de las 308 pruebas de antes falla | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si para cerrar la fase obliga a tocar algo que el plan no declara, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
