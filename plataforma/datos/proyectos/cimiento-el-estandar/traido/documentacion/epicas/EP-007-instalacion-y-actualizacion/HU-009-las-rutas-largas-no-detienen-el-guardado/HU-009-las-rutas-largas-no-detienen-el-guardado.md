# HU-009 — Que una ruta larga no detenga el guardado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja en Windows con el estándar instalado
- **Quiero** que guardar no falle con `Filename too long`
- **Para** no descubrir el tope a mitad de un commit, cuando ya está todo decidido

---

## 3. Contexto y descripción

**Pasó, y detuvo un commit dos veces.** Al guardar 1005 archivos que la plataforma había traído, `git add` se negó: **59 rutas pasaban de 260 caracteres**, y la más larga llegaba a 307. Se resolvió con `git config core.longpaths true`, y entró sin más.

**El tope no lo pone el prefijo que se agregó, y eso se midió.** La primera explicación —«la carpeta de la plataforma es muy larga»— resultó falsa: acortarla al mínimo ahorra 15 caracteres y la ruta más larga quedaría en 292, todavía sobre 260. **Lo que consume el presupuesto es este repositorio en su propio sitio**: su ruta más larga mide 252 sin prefijo ninguno, con **8 caracteres de holgura**.

**Ningún cambio de nombres crea los 55 caracteres que hacen falta.** Se probaron las combinaciones: acortar la convención de carpetas ahorra 14 y deja la holgura en 22; acortar además el prefijo de la plataforma al mínimo deja **2 caracteres de margen**, que no es margen. `core.longpaths` no es el parche: es la salida.

**Y hoy depende de que alguien se acuerde**, que es exactamente la clase de problema que este estándar existe para eliminar. Está puesto en esta máquina porque se puso a mano en medio de un commit fallido.

**Lo que esta historia no puede prometer, y conviene decirlo antes:** la configuración de git **no viaja al clonar**. Se comprobó clonando un repositorio de prueba con el ajuste puesto: en el clon no está. Vive en `.git/config`, que cada clon crea nuevo. Así que ponerlo al instalar **sirve para la copia donde se instala, y para ninguna otra**.

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | El instalador deja `core.longpaths` puesto en el repositorio donde corre | El commit que se detuvo dos veces |
| RN-02 | Si alguien lo puso en `false` a propósito, **no se pisa**: se dice y se sigue | Es la misma cortesía que el instalador ya tiene con `core.hooksPath` |
| RN-03 | Se pone en cualquier sistema, no solo en Windows | Fuera de Windows el ajuste es inerte, y detectar el sistema al instalar no sirve: la copia puede terminar en otra máquina |
| RN-04 | **No se toca la configuración global de la máquina.** Se dice cómo, y lo decide el usuario | Es un cambio fuera del proyecto, y `00·N1` pide aprobación para eso |
| RN-05 | Queda escrito, para quien clone y no instale, qué hacer si ve `Filename too long` | La configuración no viaja: sin esto, esa persona no tiene de dónde enterarse |

### 3.2 Supuestos

- Quien usa el estándar corre `instalar.py` al menos una vez en su copia.
- `git config core.longpaths true` basta para guardar rutas de más de 260 caracteres en Windows. **Comprobado**: es lo que dejó pasar el commit de los 1005 archivos, con 59 rutas por encima del tope.

### 3.3 Fuera de alcance

- **Acortar la convención de carpetas del estándar.** Se midió y no alcanza: ahorra 14 caracteres donde hacen falta 55.
- **Tocar la configuración global de la máquina**, que es de `RN-04`.
- **Los proyectos que ya están clonados y no vuelvan a instalar.** No hay forma de alcanzarlos: la configuración no viaja.

---

## 4. Criterios de aceptación

### CA-01 — Instalar deja el ajuste puesto

```gherkin
Dado un repositorio donde el estándar se va a instalar
Cuando se corre el instalador con «--aplicar»
Entonces «core.longpaths» queda en «true» en ese repositorio
Y el instalador lo dice entre sus pasos, como dice los demás
```

**Cómo validarlo:**
1. Crear un repositorio de prueba vacío y comprobar que no tiene el ajuste: `git config --get core.longpaths` no devuelve nada.
2. Correr el instalador **sin** `--aplicar`. Resultado esperado: entre los pasos aparece que lo va a poner, y `git config --get core.longpaths` **sigue sin devolver nada**.
3. Correr el instalador con `--aplicar`. Resultado esperado: `git config --get core.longpaths` devuelve `true`.
4. Correrlo otra vez con `--aplicar`. Resultado esperado: dice que ya estaba puesto, y no lo escribe de nuevo.
- **Aprobado cuando:** el modo que muestra no escribe, el que aplica escribe, y el segundo paso no repite trabajo.

### CA-02 — Un «false» puesto a propósito no se pisa

```gherkin
Dado un repositorio donde alguien puso «core.longpaths» en «false»
Cuando se corre el instalador con «--aplicar»
Entonces el ajuste sigue en «false»
Y el instalador dice que lo encontró así y que no lo tocó
```

**Cómo validarlo:**
1. En un repositorio de prueba, poner `git config core.longpaths false`.
2. Correr el instalador con `--aplicar`.
3. Leer el ajuste. Resultado esperado: sigue en `false`.
4. Leer los pasos del instalador. Resultado esperado: dice que lo encontró puesto en `false` y que no lo pisó.
- **Aprobado cuando:** el valor no cambió y el instalador lo dijo.

### CA-03 — Quien clone y no instale sabe qué hacer

```gherkin
Dado que la configuración de git no viaja al clonar
Cuando alguien clona el repositorio en Windows y ve «Filename too long»
Entonces encuentra escrito qué comando lo resuelve, y por qué pasa
```

**Cómo validarlo:**
1. Buscar en el registro de cambios y en la documentación de instalación la frase `Filename too long`. Resultado esperado: aparece, con el comando que lo resuelve.
2. Leer ese texto sin conocer el proyecto. Resultado esperado: se entiende qué pasó, qué correr y por qué el instalador no pudo hacerlo por uno.
3. Comprobar que dice **también** el comando global, y que dice que es decisión de quien lee. Resultado esperado: los dos están, y el global está marcado como opcional.
- **Aprobado cuando:** alguien que se tropieza con el error tiene de dónde enterarse sin preguntar.

### Criterios de aceptación transversales

- [x] **No regresión** — el instalador sigue haciendo todo lo demás igual, y la suite queda verde (`08`, `02·F5`).
- [x] **Límites** — está definido qué pasa si la carpeta no es un repositorio de git.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | El instalador **no** toca la configuración fuera del repositorio donde corre |
| RNF-02 | **Claridad** | Sus pasos dicen qué hizo con el ajuste, en la misma forma que dice lo demás |

---

## 6. Diseño y referencias

- **Dónde se cambia:** `instalar_git` en [validadores/instalar.py](../../../../validadores/instalar.py), junto al bloque que pone `core.hooksPath`.
- **Lo medido:** la señal `S-042`, con los números del tope y por qué acortar nombres no alcanza.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] «Backend» Poner `core.longpaths` en `instalar_git`, respetando un `false` puesto a mano.
- [ ] «Pruebas» Casos del modo que muestra, del que aplica, del segundo paso y del `false`.
- [ ] «Documentación» Dejar escrito qué hacer al ver `Filename too long`, con los dos comandos.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas`](A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/) | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo](A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/plan_trabajo.md) | [plan_pruebas](A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/plan_pruebas.md) | [resultado](A-EP-007-HU-009-el-instalador-deja-puestas-las-rutas-largas/resultado_pruebas.md) · cumple | Terminada |

Los tres van juntos porque **poner el ajuste sin escribir qué hacer al clonar deja fuera a la mitad de los casos**, y esa mitad es la que se tropieza sin aviso.

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que alguien lea esto como que el problema quedó resuelto para todos | `CA-03` existe para eso, y el cierre lo dirá: **la configuración no viaja al clonar** |
| Riesgo | Que el ajuste se ponga en un sistema donde no aplica | Fuera de Windows es inerte. Detectar el sistema sería peor: la copia puede terminar en otra máquina |
| Riesgo | Que el instalador pise un `false` puesto a propósito | `RN-02` y `CA-02`. Es la misma cortesía que ya tiene con `core.hooksPath` |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible — no aplica: no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [x] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [x] Código implementado y en rama principal
- [x] Pruebas unitarias e integración pasando — 402 de 402
- [ ] Code review aprobado — lo hace el usuario al aprobar la fase
- [x] Todos los criterios de aceptación verificados
- [x] Requisitos no funcionales validados
- [x] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | No depende de nada abierto |
| **N**egociable | ☑ | Si se prefiere no tocar configuración, `CA-03` sola ya avisa |
| **V**aliosa | ☑ | Detuvo un commit dos veces, y hoy depende de que alguien se acuerde |
| **E**stimable | ☑ | Un bloque en el instalador, sus pruebas y un texto |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los tres criterios se comprueban con repositorios de prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-26 | Agente, con el usuario | Creación de la HU. Sale del hallazgo `H-28` y de la señal `S-042` |
| 2026-08-26 | Agente | Cerrada la fase `A`. Los tres criterios cumplidos; dos defectos, los dos en la forma de probar (`S-051`) |
