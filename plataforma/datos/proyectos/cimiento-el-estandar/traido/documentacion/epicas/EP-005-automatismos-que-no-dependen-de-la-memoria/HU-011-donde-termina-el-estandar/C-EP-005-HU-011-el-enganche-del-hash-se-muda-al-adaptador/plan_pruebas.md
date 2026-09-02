# Plan de Pruebas — Fase `C-EP-005-HU-011-el-enganche-del-hash-se-muda-al-adaptador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **no queda ninguna pieza de adaptador en la carpeta de lo agnóstico**, que el enganche mudado sigue corriendo, y que la mudanza **no mejora el recuento del amarre**, porque mover código no desamarra nada.

### 1.2 Alcance

**Entra:** la ubicación del enganche, la ruta que el instalador escribe, la cuenta de los dos canales por los que un enganche se conecta, y el recuento del amarre.

**No entra:** las otras cuatro fallas de la batería interna, que son de `EP-004·HU-008`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | La línea base y las tres decisiones |
| [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md](../HU-011-donde-termina-el-estandar.md) | El `CA-04`, con sus tres pasos de validación |
| [anatomia/que-esta-amarrado-a-la-herramienta.md](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md) | Qué se pierde si mañana el agente es otro |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La carpeta de lo agnóstico | Que no quede ningún enganche adentro |
| La lista de lo conectado | Que cuente **los dos canales**, no solo el de la herramienta |
| El comando que escribe el instalador | Que apunte al adaptador |
| El enganche mudado | Que corra de verdad después de un commit |
| El recuento del amarre | Que **no baje** por la mudanza |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De frontera** | Es literalmente lo que el CA pide: que no haya piezas del lado equivocado |
| **De conexión** | Un enganche mudado sin actualizar quien lo llama **deja de correr en silencio** |
| **De no mejora** | Un número que sube por una mudanza es un número que miente |
| **De no regresión** | La batería interna completa: la fase toca el instalador, del que cuelga todo |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Si el `post-commit` apunta a un archivo que no existe, deja de correr sin decirlo** |
| Alta | CP-001, CP-003 | La frontera y la cuenta de los dos canales |
| Media | CP-004, CP-005 | El recuento y la no regresión |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`test_la_frontera_del_adaptador.py` entera, `validar.py amarre`, y la batería interna completa por la no regresión.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- El recuento del amarre **anotado antes** de mover nada: sin ese número no hay con qué comparar.

### 4.2 Criterios de salida

- Las nueve pruebas de la frontera en verde.
- El enganche comprobado **con un commit de verdad**, no solo leyendo el archivo.
- El recuento igual al de antes.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **el recuento del amarre baja**: querría decir que la mudanza sacó al enganche del alcance de quien lo mide, y eso es peor que tenerlo en la carpeta equivocada — porque deja de verse.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-04 · paso 1 — ningún enganche en lo agnóstico | CP-001 | De frontera |
| CA-04 · paso 2 — el comando apunta al adaptador | CP-002 | De conexión |
| CA-04 — lo conectado se cuenta por los dos canales | CP-003 | De frontera |
| CA-04 · paso 3 — el recuento no bajó | CP-004 | De no mejora |
| Transversal — no regresión | CP-005 | De no regresión |

---

## 6. Casos de prueba

### CP-001 — Ningún enganche en la carpeta de lo agnóstico

- **Acción:** listar los `hook_*.py` de `validadores/`.
- **Resultado esperado:** ninguno.

### CP-002 — El comando que se instala apunta al adaptador, y el enganche corre

- **Acción:** correr el instalador sobre este repositorio y leer el `post-commit`; después, hacer un commit de verdad.
- **Resultado esperado:** el comando nombra `adaptadores/claude-code/hook_estacion.py`, y el commit deja el hash anotado en la estación 12 de la fase que cierra.
- **Por qué se prueba con un commit y no leyendo:** un enganche que apunta a un archivo que no existe **falla en silencio**, y leerlo no lo revela.

### CP-003 — Lo conectado se cuenta por los dos canales

- **Precondición:** el enganche mudado se conecta por el `post-commit`, no por la tabla de la herramienta.
- **Acción:** comparar los `hook_*.py` del adaptador contra lo que el instalador conecta.
- **Resultado esperado:** las dos listas coinciden. **Con un solo canal no coinciden**, y esa fue la falla que apareció al mover.

### CP-004 — El recuento del amarre no bajó

- **Acción:** `validar.py amarre` antes y después.
- **Resultado esperado:** el mismo número. Mover código no desamarra nada.

### CP-005 — No regresión

- **Acción:** `validar.py internas`.
- **Resultado esperado:** ninguna falla nueva.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

El repositorio del estándar. El `CP-002` usa un commit real de esta misma fase.

### 7.2 Datos de prueba

Ninguno: lo que se mira son archivos del propio repositorio.

### 7.3 Usuarios de prueba

No aplica.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un proyecto instalado con la ruta vieja.** Acá se corre el instalador enseguida; en un proyecto heredero el `post-commit` seguirá apuntando al sitio anterior hasta que alguien lo corra, y en ese lapso el enganche no anota nada. No rompe el commit, pero tampoco avisa.

---

## 8. Herramientas

`unittest` y `git`. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | El enganche deja de correr sin decirlo |
| **Alta** | La cuenta de lo conectado deja fuera un canal |
| **Media** | El mapa no dice dónde vive la pieza |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md` y se arregla en la fase si cabe en su alcance.

### 9.3 Contenido mínimo de un reporte

Qué se corrió, qué salió, qué se esperaba.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Después |
|---|---|---|
| Enganches en `validadores/` | 1 | 0 |
| Recuento del amarre | 27 de 85 | el mismo |

### 12.2 Dónde se miden

`validar.py amarre` y la prueba de la frontera.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por buena la mudanza leyendo el archivo del enganche | El `CP-002` exige un commit de verdad |
| Leer un recuento igual como «no pasó nada» | Se anota antes y después, y se dice que la igualdad es el resultado esperado |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-31 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
