# Plan de Pruebas — Fase B-EP-005-HU-003-el-hallazgo-grave-detiene   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso** — y en este molde, eso incluye los **transversales**.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-005-HU-003 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-005-HU-003-el-hallazgo-grave-detiene` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

**Condición de arranque.** Carpetas temporales. **Ningún archivo del repositorio se rompe**, y el enganche se dispara **como orden del sistema**, no llamando a la función.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Detención | Que la falla detenga y el aviso no | Carpeta temporal | Sí |
| Reversibilidad | Que el archivo quede entero | Carpeta temporal | Sí |
| No regresión | Que el silencio y el tiempo sigan como estaban | Carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-03 |
| **Negativa** | ☑ | Que **no** detenga con avisos — es la mitad del criterio |
| Reversibilidad | ☑ | El transversal que esta fase enciende |
| Errores · Rendimiento | ☑ | Los dos transversales que la fase A dejó en «Sí» |

### 3.3 Técnicas de diseño de casos

- **Se prueban los dos lados, y el que más importa es el negativo.** Que detenga con una falla es fácil; que **no** detenga con avisos es lo que decide si el enganche se puede vivir. Un enganche que detiene de más se apaga, y con él se pierde lo que sí servía.
- **Se dispara como orden del sistema**, con el JSON que le manda la herramienta: lo que importa es lo que la herramienta recibe, no lo que la función devuelve.
- **La reversibilidad se comprueba leyendo el archivo**, no razonando sobre el orden de las operaciones.
- **Los transversales que ya pasaban se vuelven a correr**: encender la detención es el momento más fácil para romperlos.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera.

---

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | [CA-03](../HU-003-disparo-al-escribir-un-archivo.md#ca-03--el-hallazgo-grave-detiene-el-resto-avisa) | [CP-001](#cp-001--la-falla-detiene), [CP-002](#cp-002--el-aviso-no-detiene) | Funcional · Negativa | Crítica | Sí | ☐ |
| HU-003 | **Transversal · Reversibilidad** | [CP-003](#cp-003--transversal-de-reversibilidad-el-archivo-queda-entero) | Reversibilidad | Crítica | Sí | ☐ |
| HU-003 | **Transversal · Errores** | [CP-004](#cp-004--los-dos-transversales-que-ya-pasaban) | Errores | Alta | Sí | ☐ |
| HU-003 | **Transversal · Rendimiento** | [CP-004](#cp-004--los-dos-transversales-que-ya-pasaban) | Rendimiento | Media | Sí | ☐ |
| HU-003 | [CA-02](../HU-003-disparo-al-escribir-un-archivo.md#ca-02--lo-que-no-le-toca-se-ignora-en-silencio) | [CP-004](#cp-004--los-dos-transversales-que-ya-pasaban) | Regresión | Alta | Sí | ☐ |

**Cobertura:** el CA que la fase cierra, el que hay que mantener y **los tres transversales** = 100%.

---

## 6. Casos de prueba

### CP-001 — La falla detiene

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / CA-03 |
| **Tipo** | Funcional · **Prioridad** Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un documento con un incumplimiento de severidad **falla** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento y disparar el enganche como orden del sistema | Corre |
| 2 | Mirar lo que recibe la herramienta | Pide **detener** |
| 3 | Leer el mensaje | Dice **qué** está mal y **dónde** |
| 4 | Comprobar que no es un volcado técnico | No lo es |

**Resultado esperado final:** un documento con un incumplimiento grave no se puede dejar así, y quien lo escribió sabe qué arreglar sin correr nada a mano.

> **El paso 3 es lo que hace vivible la detención.** Detener sin decir qué obliga a investigar, y eso es lo que hace que se apague el enganche.

---

### CP-002 — El aviso no detiene

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / CA-03 |
| **Tipo** | **Negativa** · **Prioridad** Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un documento con uno o varios **avisos** y ninguna falla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento y disparar el enganche | Corre |
| 2 | Mirar lo que recibe la herramienta | **No** pide detener |
| 3 | Comprobar que los avisos igual se ven | Se ven |
| 4 | Repetir con muchos avisos | Sigue sin detener: **la cantidad no convierte un aviso en falla** |

**Resultado esperado final:** lo dudoso avisa y no detiene, como decidió `CA-02` de la HU del hallazgo.

> **Este es el caso que decide si el enganche se puede vivir.** Un enganche que detiene de más se apaga, y apagarlo se lleva también lo que sí servía. El paso 4 cierra la puerta al «cien avisos ya son grave».

---

### CP-003 — Transversal de reversibilidad: el archivo queda entero

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / **Transversal · Reversibilidad** |
| **Tipo** | Reversibilidad · **Prioridad** Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | El documento con falla del CP-001 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el documento, con un contenido conocido | Queda escrito |
| 2 | Disparar el enganche, que detiene | Detiene |
| 3 | **Leer el archivo** | Está **entero**, tal como se escribió |
| 4 | Comprobar que el enganche no lo modificó ni lo borró | No lo tocó |
| 5 | Arreglar el defecto y volver a disparar | Ya no detiene |

**Resultado esperado final:** detener detiene **el trabajo**, no la escritura. Nada queda a medias.

> **Es el transversal que esta fase enciende.** En la fase A no aplicaba, porque nada detenía. El paso 4 es el que importa: un enganche que «deshiciera» la escritura para impedirla sería más peligroso que el defecto que busca.

---

### CP-004 — Los dos transversales que ya pasaban

| Campo | Valor |
|---|---|
| **HU / exigencia** | HU-003 / CA-02 y transversales de errores y rendimiento |
| **Tipo** | Regresión · **Prioridad** Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un archivo que no le toca, uno que ya no está, y uno normal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Disparar sobre un archivo que no es documento | Calla, **y corrió**: se mira el código de salida |
| 2 | Disparar sobre un archivo que ya no está | No revienta |
| 3 | Cronometrar el disparo sobre un documento limpio | Sigue sin notarse |
| 4 | Comprobar que ninguno de los tres detiene | Ninguno |

**Resultado esperado final:** encender la detención no rompió nada de lo que ya estaba bien.

> **El paso 4 es el que se olvida.** Al agregar un camino que detiene, el riesgo es que se dispare donde no debe — sobre lo que no le toca, o sobre un archivo que ya no está.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que detener deje el archivo a medias (riesgo `R-03`) | Inmediato: se pierde trabajo |
| **Crítica** | Que un aviso detenga (riesgo `R-01`) | Inmediato: es lo que hace que se apague el enganche |
| **Alta** | Que un falso positivo llegue como falla (riesgo `R-02`) | Es defecto del validador que lo emite: se reporta a su fase |
| **Media** | Que el mensaje no diga qué arreglar | Se corrige antes de cerrar: detener sin decir qué no sirve |
| **Baja** | Que otra sesión esté tocando `validadores/` | Se guarda solo lo propio |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los dos CA que toca y **los tres transversales** |
| Casos ejecutados | 4 de 4 |
| Documentos con falla que **no** detienen | **0** |
| Documentos con solo avisos que **sí** detienen | **0** |
| Archivos que quedan a medias tras detener | **0** |
| Detenciones sin decir qué arreglar | **0** |
| Tiempo del disparo, contra la línea base de la fase A | Que no suba |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
