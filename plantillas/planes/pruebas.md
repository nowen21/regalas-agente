# Plan de Pruebas — «alcance»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Código** | PP-000 |
| **Versión** | 1.0 |
| **Alcance del plan** | Proyecto / Release / Épica EP-000 / HU-000 |
| **Fecha** | AAAA-MM-DD |
| **Elaborado por** | [Nombre — QA Lead] |
| **Revisado por** | [Nombre] |
| **Aprobado por** | [Nombre — PO] |
| **Estado** | Borrador / Aprobado / En ejecución / Cerrado |

> Basado en ISO/IEC/IEEE 29119-3. Va **junto con el `plan_trabajo` de la fase** (`planes/trabajo.md`); se guarda en `documentacion/<modulo>/fase-<XX>-<slug>/plan_pruebas.md`.
>
> **Proporcionalidad:** este formato completo es para un release/épica. Para una **sola fase o HU**, usar únicamente las secciones **3, 5, 6, 9 y 12** — el resto es opcional. No inflar una fase chica con un plan de release.

---

## 1. Introducción

### 1.1 Propósito

[Qué se busca validar con este plan y ante quién responde.]

### 1.2 Alcance

**Se prueba**
- [Módulo, funcionalidad, integración incluida]

**No se prueba**
- [Exclusión explícita y su justificación]

### 1.3 Documentos de referencia

| Documento | Ubicación |
|---|---|
| Historias de usuario / Épica | [enlace] |
| Contrato de API | [enlace] |
| Diseño / Prototipos | [enlace] |
| Normativa aplicable | [enlace] |

---

## 2. Elementos a probar

| ID | Componente / Módulo | Versión | Responsable de desarrollo |
|---|---|---|---|
| CMP-01 | | | |
| CMP-02 | | | |

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | Lógica aislada de funciones y servicios | Desarrollo | Local | Sí |
| Integración | Interacción entre componentes y BD | Desarrollo / QA | DEV | Parcial |
| Sistema | Flujos completos end-to-end | QA | QA | Parcial |
| Aceptación (UAT) | Validación del usuario final | Usuario clave | QA / Staging | No |
| Regresión | Que lo existente siga funcionando | QA | QA | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Criterios de aceptación de las HU |
| Seguridad | ☐ | Autenticación, autorización, OWASP Top 10 |
| Rendimiento | ☐ | Tiempo de respuesta y carga concurrente |
| Usabilidad | ☐ | Flujo comprensible sin capacitación |
| Compatibilidad | ☐ | Navegadores y dispositivos soportados |
| Accesibilidad | ☐ | WCAG 2.1 nivel [A/AA] |
| Migración de datos | ☐ | Integridad y completitud |
| Recuperación | ☐ | Comportamiento ante fallo y rollback |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia** — clases válidas e inválidas de cada entrada.
- **Valores límite** — mínimo, mínimo±1, máximo, máximo±1, vacío, nulo.
- **Tabla de decisión** — combinaciones de reglas de negocio.
- **Transición de estados** — flujos con estados (borrador → aprobado → anulado).
- **Pruebas exploratorias** — sesiones con carta de exploración documentada.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Crítica | Flujo principal de negocio o riesgo legal | 100% |
| Alta | Funcionalidad frecuente | 100% |
| Media | Funcionalidad secundaria | ≥ 80% |
| Baja | Casos poco frecuentes | Según tiempo |

### 3.5 Alcance de la corrida automatizada  ·  `02·F5`

La corrida de una fase es **quirúrgica**, no la suite completa "por si acaso":

1. La **suite del módulo** nuevo/refactorizado (obligatoria).
2. Las suites que la fase **refactorizó explícitamente** (declaradas en el `plan_trabajo`).
3. Las suites que **dependen directamente** de los archivos tocados (matriz de dependencias del refactor · `F4.3`).

**NO** correr por defecto la suite entera del proyecto ni módulos ajenos a la matriz. Una **regresión total** se declara aparte y explícita (ej. pre-release), no como parte del flujo normal de fase.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- [ ] Build desplegado y estable en el ambiente de pruebas
- [ ] Criterios de aceptación de las HU documentados
- [ ] Casos de prueba diseñados y revisados
- [ ] Datos de prueba cargados
- [ ] Ambiente y accesos disponibles
- [ ] Pruebas unitarias del desarrollador pasando

### 4.2 Criterios de salida

- [ ] 100% de los casos críticos y altos ejecutados
- [ ] ≥ [95]% de casos ejecutados en total
- [ ] 0 defectos abiertos de severidad crítica o alta
- [ ] Defectos medios/bajos documentados y aceptados por el PO
- [ ] Pruebas de regresión ejecutadas sin nuevos hallazgos
- [ ] Informe de pruebas emitido y aprobado

### 4.3 Criterios de suspensión y reanudación

**Suspender si:** el ambiente cae, un defecto bloqueante impide más del [30]% de los casos, o el build no cumple las pruebas de humo.
**Reanudar cuando:** se despliegue una corrección verificada y las pruebas de humo pasen.

---

## 5. Matriz de trazabilidad

> Ningún criterio de aceptación puede quedar sin al menos un caso de prueba.

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-001 | CA-02 | CP-003 | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF-01 | CP-004 | Seguridad | Crítica | No | ☐ |
| HU-002 | CA-01 | CP-005 | Funcional | Alta | No | ☐ |

**Cobertura:** [n] CA cubiertos de [n] totales = [%]

---

## 6. Casos de prueba

### CP-001 — [Título del caso]

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | [Estado previo del sistema y datos requeridos] |
| **Datos de entrada** | [Valores concretos] |
| **Diseñado por** | |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | [Acción del usuario] | [Respuesta del sistema] |
| 2 | | |
| 3 | | |

**Resultado esperado final:** [Estado observable del sistema]
**Postcondiciones:** [Registros creados, estados modificados, eventos de auditoría]

**Ejecución**

| Fecha | Ejecutado por | Ambiente | Build | Resultado | Defecto | Evidencia |
|---|---|---|---|---|---|---|
| | | QA | v1.0.0 | Aprobado / Fallido / Bloqueado | DEF-00 | [enlace] |

---

### CP-002 — [Título del caso negativo]

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Funcional — validación |
| **Prioridad** | Alta |
| **Precondiciones** | |
| **Datos de entrada** | [Datos inválidos deliberados] |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | | [Mensaje de error específico; el estado no cambia] |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

| Ambiente | URL | Uso | Versión de datos | Responsable |
|---|---|---|---|---|
| DEV | | Integración continua | Sintéticos | |
| QA | | Pruebas de sistema | Copia anonimizada | |
| Staging | | UAT y regresión | Réplica de producción | |

### 7.2 Datos de prueba

| Conjunto | Descripción | Origen | Anonimización |
|---|---|---|---|
| DS-01 | [Usuarios y roles de prueba] | Script `seed.sql` | N/A |
| DS-02 | [Registros de negocio] | Copia de producción | Requerida |

> **Regla:** ningún dato personal real sin anonimizar en ambientes distintos de producción (`00·N4` · `12` privacidad). La norma concreta de protección de datos que aplica se declara en `.agente/marco-normativo.md` (no se asume una jurisdicción aquí).

### 7.3 Usuarios de prueba

| Usuario | Rol | Permisos | Propósito |
|---|---|---|---|
| `qa.admin` | Administrador | Todos | Flujos completos |
| `qa.operador` | Operador | Limitados | Verificar restricciones |
| `qa.consulta` | Consulta | Solo lectura | Pruebas negativas de autorización |

### 7.4 Qué NO reproduce el entorno de pruebas  ·  `08·T4`

Lo que el entorno automático **no** cubre y exige **verificación manual documentada** (para no dar por probado lo que no se probó):

- [Integraciones externas reales, comportamiento del navegador, permisos del SO, symlinks/rutas especiales, concurrencia real, archivos con encoding/tamaño extremos, rendimiento sobre volúmenes reales, etc.]

---

## 8. Herramientas

| Propósito | Herramienta | Responsable |
|---|---|---|
| Gestión de casos y defectos | [Jira / Azure Test Plans] | |
| Automatización UI | [Playwright / Cypress / Selenium] | |
| Automatización API | [Postman / pytest / RestAssured] | |
| Pruebas unitarias | [pytest / PHPUnit / Jest] | |
| Rendimiento | [k6 / JMeter] | |
| Análisis estático y seguridad | [SonarQube / OWASP ZAP] | |
| Cobertura de código | [coverage.py / Istanbul] | |

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Crítica** | Bloquea el flujo principal, pérdida de datos o brecha de seguridad | Inmediato |
| **Alta** | Funcionalidad importante inoperante sin alternativa | 24 h |
| **Media** | Falla con alternativa disponible | Dentro del sprint |
| **Baja** | Cosmético o de bajo impacto | Backlog |

### 9.2 Flujo del defecto

```
Nuevo → Asignado → En corrección → Listo para pruebas → Verificado → Cerrado
                                                       ↘ Reabierto ↗
```

### 9.3 Contenido mínimo de un reporte

- ID, título descriptivo, severidad y prioridad
- Ambiente, build y usuario utilizado
- Pasos exactos para reproducir
- Resultado esperado vs. resultado obtenido
- Evidencia (captura, log, request/response)
- Caso de prueba y HU asociados

### 9.4 Registro

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| DEF-01 | | CP-001 | Alta | Abierto | | | |

---

## 10. Cronograma

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

---

## 11. Roles y responsabilidades

| Rol | Responsabilidad |
|---|---|
| QA Lead | Elabora el plan, define estrategia, aprueba el cierre |
| Analista de pruebas | Diseña y ejecuta casos, reporta defectos |
| Desarrollador | Pruebas unitarias, corrige defectos |
| Product Owner | Aprueba criterios de salida y acepta defectos residuales |
| Usuario clave | Ejecuta UAT y firma la aceptación |
| DevOps | Provisiona ambientes y despliega builds |

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de requisitos | CA con caso / CA totales | 100% |
| Casos ejecutados | Ejecutados / diseñados | ≥ 95% |
| Tasa de aprobación | Aprobados / ejecutados | ≥ 95% |
| Densidad de defectos | Defectos / punto de historia | ≤ [n] |
| Efectividad de detección | Defectos en QA / (QA + producción) | ≥ 90% |
| Tasa de reapertura | Reabiertos / corregidos | ≤ 10% |

### 12.2 Resumen de ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | % Aprobación |
|---|---:|---:|---:|---:|---:|---:|
| 1 | | | | | | |
| 2 | | | | | | |

### 12.3 Concepto final

**Recomendación:** Apto para producción / Apto con observaciones / No apto
**Riesgos residuales aceptados:** [defectos abiertos y su justificación]

---

## 13. Riesgos del proceso de pruebas

| ID | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| RP-01 | Ambiente inestable | Retrasa la ejecución | Ventana de despliegue acordada |
| RP-02 | Datos insuficientes | Casos no ejecutables | Scripts de carga versionados |
| RP-03 | Entrega tardía de desarrollo | Compresión del ciclo | Pruebas por incrementos |

---

## 14. Control de versiones

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0 | | | Versión inicial |

---

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| QA Lead | | | |
| Product Owner | | | |
| Líder técnico | | | |