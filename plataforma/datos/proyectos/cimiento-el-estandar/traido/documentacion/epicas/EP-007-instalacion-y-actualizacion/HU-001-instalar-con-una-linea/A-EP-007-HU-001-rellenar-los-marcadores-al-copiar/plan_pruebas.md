# Plan de Pruebas — «Fase A-EP-007-HU-001: rellenar los marcadores al copiar»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-007-HU-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-007-HU-001-rellenar-los-marcadores-al-copiar` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente — el usuario |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**, como pide la plantilla por proporcionalidad.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Correr la instalación entera sobre una carpeta vacía y mirar lo que quedó escrito | Carpeta temporal | Sí |
| Aceptación | Abrir un enlace de un archivo instalado y ver que llega a la regla | Carpeta temporal | No — es un clic |

**Por qué integración y no unitarias.** El defecto no está en ninguna función suelta: cada una hace bien lo suyo. Está en que **una de las cuatro rellena y tres no**. Probar cada función por separado no lo habría atrapado; correr la instalación entera, sí. Es la lección de la [20.0.1](../../../../../CHANGELOG.md), que se publicó sin esto.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA de la HU-001 |
| Compatibilidad | ☑ | Rutas con espacios y tildes, que es donde vive este repositorio |
| Rendimiento | ☐ | No aplica: se instala una vez |
| Seguridad | ☐ | No aplica: no hay usuarios ni permisos |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia** — carpeta vacía (instalación nueva) contra carpeta ya instalada (reinstalación).
- **Valores límite** — ruta con espacios y con tildes; carpeta que existe pero está vacía.
- **Triangulación** — el veredicto no sale de la propia función que se cambió: sale de **leer los archivos escritos** y buscar la marca, que es una fuente independiente de la que los escribió ([`08`](«RUTA-ESTANDAR»/base/08-pruebas.md)).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):

1. La suite nueva de esta fase (`test_instalar_marcadores.py`).
2. Las pruebas que ya existan de `instalar.py`.
3. Las de `checklist.py`, porque lee el sello de uno de los archivos que se tocan.

**No** se corre la suite entera del repositorio.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo) | [CP-001](#cp-001--ninguna-copia-conserva-un-marcador), [CP-002](#cp-002--el-enlace-instalado-abre-la-regla) | Funcional | Crítica | CP-001 sí · CP-002 no | ☐ |
| HU-001 | [CA-02](../HU-001-instalar-con-una-linea.md#ca-02--correrla-dos-veces-no-rompe-nada) | [CP-003](#cp-003--reinstalar-no-cambia-lo-que-ya-estaba-bien) | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF — Compatibilidad | [CP-004](#cp-004--la-ruta-con-espacios-y-tildes-se-escribe-entera) | Compatibilidad | Alta | Sí | ☐ |

**Cobertura:** 3 de 3 exigencias cubiertas = 100%.

---

## 6. Casos de prueba

### CP-001 — Ninguna copia conserva un marcador

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Una carpeta temporal vacía. El estándar en su ubicación actual |
| **Datos de entrada** | La ruta de la carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear una carpeta temporal vacía | La carpeta existe y no tiene nada dentro |
| 2 | Correr la instalación apuntando a esa carpeta | Termina sin preguntar nada |
| 3 | Listar todos los `.md` que quedaron dentro | Sale la lista, con al menos `CLAUDE.md`, `.agente/stack-instalacion.md`, los 4 de `.agente/` y el índice de memoria |
| 4 | Buscar la marca `«` en cada uno de esos archivos | Ningún archivo la contiene |
| 5 | Borrar la carpeta temporal | Queda borrada |

**Resultado esperado final:** ningún archivo escrito por la instalación conserva un hueco sin llenar.
**Postcondiciones:** la carpeta temporal ya no existe.

> **Este es el caso que faltó.** Correrlo antes de publicar la 20.0.1 habría mostrado el defecto que después reportó un proyecto.

---

### CP-002 — El enlace instalado abre la regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Tipo** | Aceptación — verificación manual |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 pasó y la carpeta temporal **no** se borró todavía |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `.agente/stack-instalacion.md` de la carpeta instalada | Se ve el documento con sus citas a reglas |
| 2 | Hacer clic en la primera cita a una regla | Abre el archivo de esa regla, en la carpeta del estándar |
| 3 | Repetir con una cita del `CLAUDE.md` instalado | Abre la regla que cita |

**Resultado esperado final:** las citas llevan a la regla que nombran.

> **Por qué va a mano.** Que la ruta esté escrita no prueba que abra: eso lo dice el clic. Es lo que [`08·T4`](«RUTA-ESTANDAR»/base/08-pruebas.md#t4--protege-los-datos-reales-al-probar) llama verificación manual documentada, y es justo lo que nadie hizo la vez pasada.

---

### CP-003 — Reinstalar no cambia lo que ya estaba bien

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 |
| **Tipo** | Funcional — idempotencia |
| **Prioridad** | Alta |
| **Precondiciones** | Una carpeta temporal donde ya corrió la instalación |
| **Datos de entrada** | La misma ruta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el contenido de cada archivo instalado | Queda el registro del antes |
| 2 | Correr la instalación otra vez sobre la misma carpeta | Termina sin preguntar |
| 3 | Comparar cada archivo contra el registro del paso 1 | Ninguno cambió |
| 4 | Buscar la marca `«` otra vez | Ningún archivo la contiene |

**Resultado esperado final:** repetir es seguro y sigue sin quedar ningún hueco.

---

### CP-004 — La ruta con espacios y tildes se escribe entera

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF Compatibilidad |
| **Tipo** | Compatibilidad — valor límite |
| **Prioridad** | Alta |
| **Precondiciones** | Una carpeta temporal cuyo nombre lleve un espacio y una tilde |
| **Datos de entrada** | Una ruta como `…/proyecto de prueba ñ/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Crear la carpeta con espacio y tilde en el nombre | La carpeta existe |
| 2 | Correr la instalación apuntando ahí | Termina sin error |
| 3 | Abrir un archivo instalado y leer la ruta que quedó escrita | Está completa, con su espacio y su tilde, sin cortar ni escapar mal |

**Resultado esperado final:** la ruta escrita es la ruta real.

> **Por qué importa acá.** El repositorio del estándar vive en una ruta con espacios y tilde. Si el relleno se rompe con eso, se rompe en la máquina donde se desarrolla.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Después del cambio, un archivo instalado sigue con el marcador | Inmediato |
| **Alta** | La segunda corrida cambia algo que ya estaba bien | Antes de cerrar |
| **Media** | La ruta con tilde se escribe mal | Antes de cerrar |
| **Baja** | El texto de la salida no dice qué se rellenó | Se anota como deuda |

### 9.2 Qué se hace con un defecto

Se diagnostica, se corrige y se vuelve a correr el caso. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior ([`02·F15`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md), etapa 7).

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — las 3 con caso |
| Casos ejecutados | 4 de 4 |
| Archivos instalados con marca `«` | **0** |

El veredicto de cada caso y el concepto final **no van acá**: van en el `resultado_pruebas.md` de esta fase. Este plan dice qué se va a medir; aquel dirá cuánto dio.
