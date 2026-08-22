# Plan de Pruebas — Fase A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Ningún enganche del repositorio se rompe para probar.** El fallo se **simula**: romper uno de verdad afecta a todas las sesiones abiertas.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Instalación | Que los seis enganches queden registrados | Carpeta temporal | Sí |
| Disparo | Que cada uno se dispare en el momento que declara | Carpeta temporal | Sí |
| Tolerancia al fallo | Que un enganche caído no detenga el trabajo | Fallo simulado | Sí |
| Inventario | La tabla de los seis, con su momento y qué pasa si fallan | Lectura del instalador | No |

**De dónde sale la tabla de los seis.** Del **instalador**, no de la documentación: lo que corre es lo que él registra, y la documentación puede estar vieja (riesgo `R-03`).

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Tolerancia al fallo | ☑ | El CA-02, que es el que hace que los enganches sean vivibles |
| Inventario | ☑ | Los seis, con su momento |
| Seguridad | ☑ | Que la instalación de prueba no toque nada fuera de su carpeta |

### 3.3 Técnicas de diseño de casos

- **Se prueba el caso malo, no el aviso** — el CA-02 se comprueba con un enganche que **se cae**, no con uno que reporta algo. Un aviso que no traba no prueba que un fallo tampoco trabe.
- **La función, no el disparo** — el riesgo `R-02`: probar los disparos abriendo sesiones de verdad ensuciaría el histórico. Se prueba la función de cada enganche, que está separada del disparo.
- **El recorrido incluye los que se agreguen** — el caso del CA-01 recorre **lo que el instalador registra**, no una lista de seis escrita a mano. Un enganche nuevo entra solo.
- **Un enganche que traba detiene la fase** — el riesgo `R-01`: si uno sí detiene el trabajo al fallar, se para y se reporta de inmediato. La herramienta quedaría trabada para todos.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y el instalador sobre carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | [CA-01](../HU-004-generar-los-automatismos.md#ca-01--los-automatismos-quedan-puestos-y-corriendo) | [CP-001](#cp-001--los-enganches-que-el-instalador-registra-quedan-puestos), [CP-002](#cp-002--cada-enganche-se-dispara-en-el-momento-que-declara) | Funcional | Alta | Sí | ☐ |
| HU-004 | [CA-02](../HU-004-generar-los-automatismos.md#ca-02--si-uno-falla-el-trabajo-no-se-detiene) | [CP-003](#cp-003--un-enganche-que-se-cae-no-detiene-el-trabajo) | Tolerancia al fallo | Crítica | Sí | ☐ |
| HU-004 | RNF — que ningún automatismo trabe el trabajo | [CP-004](#cp-004--la-tabla-de-los-enganches-con-su-momento-y-su-fallo) | Inventario | Alta | No | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Los enganches que el instalador registra quedan puestos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal con un proyecto de prueba |
| **Datos de entrada** | La lista de enganches que el instalador registra |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer del instalador qué enganches registra | Salen seis, y queda la lista con su fecha |
| 2 | Instalar en el proyecto de prueba | Termina |
| 3 | Comprobar que los seis quedaron registrados | Los seis |
| 4 | Comprobar que ninguno quedó registrado dos veces | Ninguno |
| 5 | Agregar un enganche de mentira al instalador y repetir | Entra solo, sin tocar la prueba |

**Resultado esperado final:** la puesta de automatismos se comprueba contra lo que el instalador hace, no contra una lista escrita.

---

### CP-002 — Cada enganche se dispara en el momento que declara

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Los momentos declarados: abrir sesión, mandar mensaje, terminar respuesta y escribir archivo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Por cada enganche, leer en qué momento declara correr | Queda la tabla |
| 2 | Ejercitar la función de cada uno en su momento | Cada una responde |
| 3 | Comprobar que ninguno corre en un momento que no le toca | Ninguno |
| 4 | Comprobar que la prueba no abrió sesiones reales | No las abrió |

**Resultado esperado final:** cada automatismo corre donde dice, sin ensuciar el histórico para comprobarlo.

---

### CP-003 — Un enganche que se cae no detiene el trabajo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-02 |
| **Tipo** | Tolerancia al fallo |
| **Prioridad** | Crítica |
| **Precondiciones** | Fallo **simulado**, sin romper ningún enganche real |
| **Datos de entrada** | Un enganche que lanza un error al correr |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Simular que un enganche falla al correr | Falla |
| 2 | Comprobar que el trabajo **sigue** | Sigue |
| 3 | Comprobar que el fallo **queda dicho** | Queda dicho: fallar en silencio es peor |
| 4 | Repetir simulando el fallo en cada uno de los seis | Los seis: ninguno traba |
| 5 | Comprobar que ningún enganche real del repositorio se tocó | Ninguno |

**Resultado esperado final:** los automatismos son ayuda, no un punto único de falla.

> **El paso 4 recorre los seis a propósito.** El que no se prueba es el que traba la herramienta el día que se cae.

---

### CP-004 — La tabla de los enganches, con su momento y su fallo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RNF |
| **Tipo** | Inventario |
| **Prioridad** | Alta |
| **Precondiciones** | Los tres casos anteriores corridos |
| **Datos de entrada** | Lo observado en el CP-002 y el CP-003 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar la tabla: enganche, momento en que corre, qué hace | Una fila por enganche |
| 2 | Agregar qué pasa si cada uno falla | Cada fila con su veredicto medido |
| 3 | Comprobar que la tabla salió del instalador, no de `docs/` | Del instalador |
| 4 | Anotar la diferencia si la documentación dice otra cosa | Queda como hallazgo |

**Resultado esperado final:** hay una tabla de lo que corre de verdad, y se sabe si la documentación coincide.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un enganche detenga el trabajo al fallar (riesgo `R-01`) | **Se para y se reporta de inmediato**: la herramienta quedaría trabada |
| **Crítica** | Que se rompa un enganche real del repositorio para probar | Inmediato. Afecta a todas las sesiones abiertas |
| **Alta** | Que un enganche falle en silencio | Antes de cerrar: fallar sin decirlo es peor que fallar |
| **Media** | Que la documentación y el instalador no coincidan (riesgo `R-03`) | Se anota; la tabla sale del instalador |
| **Baja** | Que probar los disparos ensucie el histórico (riesgo `R-02`) | Se prueba la función, separada del disparo |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Enganches reales rotos para probar | **0** |
| Enganches que traban el trabajo al fallar | **0** |
| Enganches que fallan en silencio | **0** |
| Sesiones reales abiertas para probar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
