# Diseño de la interfaz local   ·   `[CAPA 3]`

**Para qué sirve este documento.** Qué pantallas hay, qué se ve en cada una, cómo se llega de una a otra y qué pasa cuando algo falta. La interfaz **solo lee** ([`DA-06`](decisiones-de-arquitectura.md)): lo que cambia el estado del proyecto se hace trabajando con el agente, donde hay aprobación.

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md). Cubre RF-12, y el generador del entregable de RF-10.

**Estado: BORRADOR** (2026-08-24, sin aprobar).

---

## 1. Para quién es

| Quién | Qué viene a hacer | Cuánto sabe del proyecto |
|---|---|---|
| El usuario | Revisar qué hay escrito y qué guardó el agente, sin abrir archivo por archivo | Todo |
| Quien recibe el proyecto | Leer los documentos del ciclo y descargarse el entregable | Nada: es la primera vez que lo ve |

## 2. Las pantallas

Cada pantalla, qué muestra y qué deja hacer desde ahí.

| # | Pantalla | Qué muestra | Qué deja hacer |
|---|---|---|---|
| P-1 | Inicio | En qué estado está el proyecto: etapas del ciclo, cuáles tienen documento y cuáles no | Entrar a cualquiera |
| P-2 | Documentos del ciclo | La lista de las siete etapas, con sus documentos y su estado de aprobación | Abrir uno, o pedir su entregable |
| P-3 | Un documento | El documento completo, legible, con sus tablas | Volver, o pedir el `.docx` |
| P-4 | Memoria | Lo que el agente guardó, lo más reciente primero | Buscar por palabra, y abrir una anotación |
| P-5 | Una anotación | Qué pasó, por qué importa, qué se decidió y dónde queda el detalle | Ir al documento que nombra |
| P-6 | Reglas | Las reglas vigentes, agrupadas por capítulo, y las derogadas aparte | Abrir una y ver desde qué versión rige |

## 3. Cómo se llega de una a otra

```
Inicio (P-1)
├── Documentos del ciclo (P-2) ──> Un documento (P-3) ──> [pedir .docx]
├── Memoria (P-4) ──────────────> Una anotación (P-5) ──> Un documento (P-3)
└── Reglas (P-6)
```

**Desde cualquier pantalla se vuelve al inicio.** No hay flujos de varios pasos: se mira una cosa y se vuelve, porque nada de lo que se hace acá cambia el proyecto.

## 4. Qué ve cada quien

| Pantalla | El usuario | Quien recibe el proyecto |
|---|---|---|
| Documentos y su contenido | Todo | Todo |
| Memoria | Todo | **No la ve**: es trabajo interno, no entregable |
| Reglas | Todo | Todo |

## 5. Qué pasa cuando falta algo

> Es la mitad del diseño de una pantalla y la que se olvida. Una pantalla que muestra vacío sin decir por qué hace pensar que el dato no existe.

| Situación | Qué se ve |
|---|---|
| La memoria no está disponible | Los documentos se muestran igual, y un aviso dice que la memoria no se pudo leer |
| Un documento figura en la lista pero no está en el disco | Se dice cuál falta y dónde debería estar, en vez de mostrarlo vacío |
| Una etapa no tiene documento todavía | Aparece como «sin escribir», que es un dato, no un error |
| Un documento tiene espacios sin llenar | Se muestra, con la cuenta de cuántos le faltan |
| Se pide el `.docx` de un documento con espacios sin llenar | Se avisa antes de generar, y se deja decidir |
| No hay nada guardado que coincida con lo buscado | Se dice que no hay, sin sugerir nada inventado |

## 6. Cómo se ve

Las decisiones de presentación que valen para todas las pantallas.

| Qué | Cómo |
|---|---|
| Lo primero que se lee en cada pantalla | Qué es lo que se está mirando, sin siglas |
| Los documentos | Con su formato: tablas como tablas, y los enlaces abriendo el documento que nombran |
| Lo que está aprobado y lo que no | Dicho con palabras, no solo con color: quien no distingue colores tiene que poder saberlo |
| El tamaño de letra y el contraste | Legible sin acercarse a la pantalla |

## 7. Lo que la interfaz NO hace

- **No edita.** Ni documentos, ni reglas, ni memoria.
- **No borra.** Nada de lo que muestra se puede quitar desde ahí.
- **No sale a la red.** Todo lo que muestra está en la máquina.
- **No sustituye al agente.** Es para mirar, no para trabajar.

## 8. Lo que queda por decidir

| # | Duda | Qué la resuelve |
|---|---|---|
| 1 | Si el `.docx` conserva la numeración del `.md` o la del cliente | Es la P-1 del [inventario](../analisis-requisitos/inventario-funcionalidades.md), y la decide quien reciba el entregable |
| 2 | Si la memoria se muestra completa o solo lo de los últimos meses | Se decide al ver cuánto crece, no antes |
