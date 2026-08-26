# Estado de fase - G-EP-008-HU-003: se ve el estado de un proyecto   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Módulo** | Proyectos |
| **Épica / HU** | [EP-008](../../epica.md) · [HU-003](../HU-003-ver-el-estado-de-un-proyecto.md) |
| **Versión del producto** | 1, fase G de ocho |
| **Última actualización** | 2026-08-25 |
| **Veredicto de las pruebas** | Cumple. 9 de 9 casos aprobados, en [resultado_pruebas.md](resultado_pruebas.md) |

---

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `faed710`.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | 👤 La HU-003 aprobada el 2026-08-25 | ☑ |
| 2 | Disparo / autorización de inicio | 👤 El usuario pidió seguir, el 2026-08-25 | ☑ |
| 3 | Diseño del plan detallado | Los dos planes escritos | ☑ |
| 4 | Pausa y presentación | Presentados y leídos | ☑ |
| 5 | Aprobación del plan detallado | 👤 «si», el 2026-08-25 | ☑ |
| 6 | Ejecución continua | Traer las etapas, calcular y mostrar el estado | ☑ |
| 7 | Pruebas | Los nueve casos con veredicto: 9 de 9 aprobados | ☑ |
| 8 | Cierre de la fase | [funcionalidad_implementada.md](funcionalidad_implementada.md), y el defecto anotado en el cierre de la fase E | ☑ |
| 9 | Commit único | 👤 «si», el 2026-08-25. Commit `faed710` | ☑ |

---

## 2. Qué falta para avanzar

**Nada: la fase cerró**, en el commit `faed710`. Las siete tareas hechas, los nueve casos en verde con su evidencia, y el cierre escrito. Con esto **la HU-003 queda cerrada**, y con ella la épica `EP-008` completa.

**Lo que la fase produjo, que es lo que vino a hacer:**

```
etapas del ciclo con documento : 7 de 7
fases en total                 : 127
fases todavía abiertas         :  41
fases que no se dejan leer     :   5   (nombradas, con su ruta)
documentos aprobados           : 228 de 994
```

**`CP-009` pasó de la forma dura.** Con la ruta apuntando a una carpeta que no existe, los ocho datos del estado salen **idénticos**. Se calcula desde lo traído, no leyendo el proyecto.

**Las cinco ilegibles son fases suyas**, y quedan nombradas en la evidencia. Suponer que estaban cerradas habría dado 41 abiertas; suponerlas abiertas, 46. Ninguna de las dos cifras sería verdad.

**Y quedó anotado el defecto de la fase E**, que estaba cerrada cuando se encontró: declaraba recorrer la documentación del ciclo y no recorría las etapas del ciclo.

## 3. Lo que ya se decidió

| Qué | Decisión |
|---|---|
| De dónde sale el estado | De lo **traído**, no de leer la carpeta del proyecto. `CA-01` dice «sin abrir su carpeta» |
| Si se guarda | No. Se calcula al pedirlo: un estado guardado envejece y miente |
| Qué pasa con `cvds/` | Entra a lo que se trae, y con eso se cierra el hueco de la fase E |
| Qué pasa con una estación ilegible | Se dice cuántas y cuáles, con su ruta. Nunca se supone |
| Cómo se dice lo aprobado | Con palabras, no solo con color |
| Qué se prueba | Nueve casos. El que más protege es el de la estación ilegible; el más duro es borrar la carpeta y comprobar que el estado sale igual |
| Qué se anota al cerrar | El defecto de la fase E, que estaba cerrada cuando se encontró |
