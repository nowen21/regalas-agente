# Plan de Pruebas — Fase A-EP-008-HU-001: la plataforma levanta y guarda   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-008-HU-001 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que la plataforma levante en la máquina, guarde, y que lo guardado sobreviva: al reinicio, y a perder el índice.

**No se prueba** conectar un proyecto: eso es la fase B.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que guardar y leer funcionen sobre datos de mentira | Sí |
| Integración | Que la plataforma levante y responda | Sí |
| Recuperación | Que el índice se reconstruya desde el texto | Sí |
| Manual | Que se levante desde cero siguiendo lo escrito | No: lo hace una persona |

### 3.2 Técnicas

- Prueba de reinicio: guardar, apagar, abrir y volver a leer.
- Prueba de destrucción: borrar el índice a propósito.
- Prueba sin red: desconectar la máquina antes de correr.
- Casos que buscan el rechazo, no el camino feliz.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| La plataforma levanta sin red (`RNF-03`) | [CP-001](#cp-001--levanta-sin-red) | ☐ |
| Lo guardado sobrevive al reinicio | [CP-002](#cp-002--lo-guardado-sobrevive-al-reinicio) | ☐ |
| Perder la base no pierde información (`RNF-04`) | [CP-003](#cp-003--el-índice-se-reconstruye) | ☐ |
| La fuente es texto legible sin la plataforma (`DA-01`) | [CP-004](#cp-004--lo-guardado-se-lee-sin-la-plataforma) | ☐ |
| Se levanta desde cero siguiendo lo escrito | [CP-005](#cp-005--alguien-la-levanta-siguiendo-solo-el-texto) | ☐ |
| Nada de la fase toca un proyecto ajeno | [CP-006](#cp-006--que-no-pase-que-toque-algo-de-afuera) | ☐ |

## 5. Los casos

### CP-001 · Levanta sin red

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la plataforma arranque con la máquina desconectada |
| **Cómo se corre** | Se desconecta la red y se levanta |
| **Resultado esperado** | Levanta y responde, sin errores de red |
| **Si falla** | Se busca qué componente sale afuera, y se quita |

### CP-002 · Lo guardado sobrevive al reinicio

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que lo escrito quede, y no viva solo en memoria |
| **Cómo se corre** | Se guarda un dato de mentira, se apaga la plataforma, se abre y se lee |
| **Resultado esperado** | El dato está, igual a como se guardó |
| **Si falla** | Se revisa qué se guardó en memoria y no en disco |

### CP-003 · El índice se reconstruye

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que perder la base no pierda información |
| **Cómo se corre** | Se guarda, se borra la base entera, se pide reconstruir |
| **Resultado esperado** | Todo vuelve a estar, leído desde el texto |
| **Si falla** | Hay un dato que solo vivía en la base: se mueve al texto |

### CP-004 · Lo guardado se lee sin la plataforma

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la fuente sea texto legible por una persona |
| **Cómo se corre** | Se abre lo guardado con un editor cualquiera |
| **Resultado esperado** | Se entiende qué dice, sin la plataforma |
| **Si falla** | Se está guardando en un formato que ata la información a la herramienta |

### CP-005 · Alguien la levanta siguiendo solo el texto

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que lo escrito para levantarla sirva |
| **Cómo se corre** | En una carpeta limpia, siguiendo los pasos escritos y sin agregar nada de memoria |
| **Resultado esperado** | Levanta al primer intento |
| **Si falla** | Se corrige el texto, no la memoria de quien lo escribió |

### CP-006 · Que NO pase: que toque algo de afuera

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la fase no escriba fuera de la plataforma |
| **Cómo se corre** | Se anota qué archivos hay en una carpeta ajena, se corre todo, y se compara |
| **Resultado esperado** | Ningún archivo ajeno cambió, se creó ni se borró |
| **Si falla** | Se busca qué escribió afuera, y se corrige antes de seguir |

## 6. Lo que este plan NO puede probar

- **Que la base elegida sirva para lo que viene.** Se prueba con datos de mentira y pocos; el volumen real llega con la fase E.
- **Que reutilizar lo existente haya sido buena idea.** Eso se sabrá en las fases siguientes.

## 7. Criterios de salida

- Los seis casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
