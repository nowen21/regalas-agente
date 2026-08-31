# HU-001 — Buscar en lo conversado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-011 Lo que se repite sale a la luz](../epica.md) |
| **Funcionalidad** | `F-033` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Medición |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Pendiente, sin aprobar |
---

## 2. Narrativa

- **Como** quien trabaja con el agente todos los días
- **Quiero** buscar dentro de lo que se ha conversado, sin abrir archivo por archivo
- **Para** poder encontrar cuándo se dijo algo, y cuántas veces

---

## 3. Contexto y descripción

Las conversaciones ya se escriben: [validadores/historico.py](../../../../validadores/historico.py) anota cada mensaje del usuario y cada respuesta del agente en `historico-chat/`, con la hora del reloj de la máquina y con las claves ya tapadas.

Lo que falta es que la plataforma las lea y las indexe, para poder buscar en ellas.

**No cambia cómo se escriben.** El enganche sigue siendo el que escribe; la plataforma solo lee lo que ya está.

### 3.1 Reglas de negocio

- `RN-1` El texto sigue siendo la fuente; el índice se puede borrar y rehacer.
- `RN-2` Ninguna credencial entra a lo indexado.
- `RN-3` Indexar no modifica ni mueve el archivo del histórico.

### 3.2 Supuestos

- Que lo que el enganche escribe alcanza. Si algún día una conversación no pasa por ahí, no se indexa y nadie se entera.

### 3.3 Fuera de alcance

- Contar y agrupar, que es [HU-002](../HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md).
- Traer conversaciones de otras herramientas.

---

## 4. Criterios de aceptación

### CA-01 — Lo conversado se encuentra por una palabra suya

```gherkin
Dado una sesión ya escrita en el histórico
Cuando el usuario busca una palabra que se dijo en ella
Entonces la sesión aparece entre los resultados
Y se ve en qué mensaje se dijo
```

### CA-02 — El índice se puede borrar y rehacer

```gherkin
Dado el índice de conversaciones ya construido
Cuando se borra entero y se manda rehacer
Entonces vuelve completo, leído desde los archivos del histórico
```

### CA-03 — Ninguna credencial queda en lo indexado

```gherkin
Dado un mensaje del histórico que traía una clave
Cuando se indexa
Entonces lo indexado trae la clave tapada, igual que el archivo
```

**Cómo validarlo:** buscar en lo indexado las formas de clave que `secretos.py` conoce, y que no aparezca ninguna.

### CA-04 — Indexar no toca el histórico

```gherkin
Dado los archivos de historico-chat
Cuando se indexan
Entonces ningún archivo cambia, se mueve ni se borra
```

**Cómo validarlo:** comparar la carpeta antes y después. Es el caso de «que NO pase» de esta historia.

### Criterios transversales

- Una búsqueda sin coincidencias lo dice, en vez de devolver una lista vacía sin explicación.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Recuperación | El índice se reconstruye desde el texto (`RNF-04`) |
| Disponibilidad | Funciona sin red (`RNF-03`) |
| Seguridad | Ninguna credencial escrita (`RNF-05`) |

---

## 6. Diseño y referencias

- Funcionalidad `F-033` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-33` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Decisión que la gobierna: [`DA-01`](../../../../cvds/diseno/decisiones-de-arquitectura.md).
- De dónde sale el texto: [validadores/historico.py](../../../../validadores/historico.py).

---

## 7. Tareas técnicas derivadas

1. Leer los archivos del histórico y guardarlos en el índice.
2. Buscar por palabra y devolver en qué sesión y en qué mensaje.
3. Rehacer el índice desde cero.
4. Comprobar que nada del histórico se modificó.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| Por abrir | Esta historia | Sin abrir. Va en la versión 2 |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-008 HU-001`: la plataforma tiene que existir |
| **Riesgo** | Que indexar todas las conversaciones acumuladas pese. Se mide con lo que ya hay, que es volumen real |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su cambio anotado.
- ☑ El texto de origen existe y ya viene sin credenciales.
- ☐ El módulo Medición tiene especificación aprobada.

## 11. Definition of Done

- ☐ Los cuatro criterios con veredicto y evidencia.
- ☐ Comprobado que el histórico no cambió.
- ☐ Comprobado que el índice se rehace completo.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita que la plataforma exista, nada más |
| Negociable | Sí | Qué campos se indexan se puede ajustar |
| Valiosa | A medias | Sola sirve poco: su valor llega con `HU-002` |
| Estimable | Sí | Es leer, guardar y buscar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se busca una palabra que se dijo, y tiene que aparecer |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-033`, que entró al inventario ese día desde [pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md](../../../../pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md) |
