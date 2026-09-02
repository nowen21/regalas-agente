# Diseño de la interfaz   ·   `[CAPA 3]`

**Para qué sirve este documento.** Qué pantallas hay, qué se ve y qué se hace en cada una, cómo se llega de una a otra, y qué pasa cuando algo falta. La interfaz **administra**: desde ella se crea, se edita y se publica, y todo cambio queda firmado y registrado ([`DA-12`](decisiones-de-arquitectura.md)).

> **Escrito desde la propuesta**, igual que el resto de [cvds/README.md/](../README.md). Reescrito el 2026-08-24: la versión anterior describía una pantalla que solo dejaba mirar.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. Para quién es

| Quién | Qué viene a hacer | Cuánto sabe del proyecto |
|---|---|---|
| El usuario | Administrar todos sus proyectos: ver cómo van, escribir, aprobar y entregar | Todo |
| Quien recibe un proyecto | Nada acá: recibe el expediente generado, no entra a la plataforma | Nada |

## 2. Las pantallas

Cada pantalla, qué muestra y qué deja hacer desde ahí.

| # | Pantalla | Qué muestra | Qué deja hacer |
|---|---|---|---|
| P-01 | Inicio | Todos los proyectos, su estado y lo que se desvió | Entrar a uno, o conectar uno nuevo |
| P-02 | Un proyecto | Sus etapas, sus fases abiertas, qué falta aprobar y su ruta | Entrar a cualquier documento, abrir una fase, pedir el expediente |
| P-03 | Un documento | El documento completo, con lo que le falta por llenar | Editarlo, aprobarlo, ver su historia |
| P-04 | Historia de un documento | Cómo estaba en cada versión, y qué aprobación tenía | Comparar dos versiones |
| P-05 | Fases | Todas las fases del proyecto, con su estación y su puerta pendiente | Abrir, avanzar y cerrar una fase |
| P-06 | Reglas | Las reglas vigentes por capítulo, y las derogadas aparte | Escribir, editar, derogar y publicar una versión |
| P-07 | Configuración de un proyecto | Qué reglas y qué moldes rigen ahí | Activar y desactivar lo opcional |
| P-08 | Memoria | Lo que el agente guardó, de lo más reciente a lo más viejo | Buscar, corregir y dar de baja |
| P-09 | Auditoría | Lo que se hizo, con quién, cuándo y sobre qué | Filtrar por proyecto, fecha y tipo de acción |
| P-10 | Expediente | Qué documentos entran, cuáles faltan y cuáles tienen huecos | Armarlo y generar el entregable |
| P-11 | Traer un proyecto | Qué se encontró en su carpeta y qué se reconoció | Traerlo, y ver qué quedó sin reconocer |
| P-12 | Reportes | Cómo va cada proyecto, con la misma medida | Comparar proyectos |

## 3. Cómo se llega de una a otra

```
Inicio (P-01)
├── Un proyecto (P-02)
│   ├── Un documento (P-03) ──> Historia (P-04)
│   ├── Fases (P-05)
│   ├── Configuración (P-07)
│   └── Expediente (P-10) ──> [generar entregable]
├── Reglas (P-06)
├── Memoria (P-08)
├── Auditoría (P-09)
├── Traer un proyecto (P-11)
└── Reportes (P-12)
```

**Desde cualquier pantalla se vuelve al inicio.** Lo que cambia algo pide confirmación en el momento, y queda registrado.

## 4. Qué pide aprobación, y qué no

> No todo cambio es igual. Lo que se puede deshacer se hace y se registra; lo que no, se aprueba antes.

| Qué se hace | Qué pide antes |
|---|---|
| Escribir o editar un documento | Nada: se guarda y queda registrado |
| Aprobar un documento | Confirmación, y queda la firma con la huella del texto |
| Publicar una versión de reglas | Confirmación, y no procede si rompe algo que servía |
| Derogar una regla | Confirmación: no se borra, se marca |
| Traer un proyecto | Muestra qué va a traer antes de traerlo |
| Dar de baja una anotación | Confirmación: no se borra, se marca |
| Conectar o desconectar un proyecto | Confirmación; desconectar no borra su documentación |

## 5. Qué pasa cuando falta algo

> Es la mitad del diseño de una pantalla, y la que se olvida. Una pantalla que muestra vacío sin decir por qué hace pensar que el dato no existe.

| Situación | Qué se ve |
|---|---|
| La ruta de un proyecto se perdió | Su documentación se muestra igual, con el aviso de qué ruta buscó |
| Un proyecto no tiene ninguna etapa escrita | Aparece como «sin empezar», que es un dato, no un error |
| Un documento tiene espacios sin llenar | Se muestra, con la cuenta de cuántos le faltan |
| Se pide el expediente y falta un documento | Se lista cuál falta, y no se inventa |
| Se aprueba y el texto cambió después | La aprobación aparece como caducada, con qué cambió |
| La base no responde | Los documentos se muestran leyendo el texto, y se avisa que la búsqueda no está disponible |
| No hay nada guardado que coincida con lo buscado | Se dice que no hay, sin sugerir nada inventado |
| Una fase no puede avanzar | Se dice qué puerta falta, no solo que no puede |

## 6. Cómo se ve

Las decisiones de presentación que valen para todas las pantallas.

| Qué | Cómo |
|---|---|
| Lo primero que se lee en cada pantalla | Qué se está mirando, sin siglas |
| Lo aprobado y lo que no | Dicho con palabras, no solo con color: quien no distingue colores tiene que poder saberlo |
| Lo que cambia algo | Se distingue de lo que solo muestra, antes de hacer clic |
| Los documentos | Con su formato: las tablas como tablas, y los enlaces abriendo lo que nombran |
| El tamaño de letra y el contraste | Legible sin acercarse a la pantalla |

## 7. Lo que la interfaz NO hace

- **No escribe el código de los proyectos.** Eso lo hace el agente trabajando.
- **No borra nada de forma definitiva.** Lo que deja de valer se marca.
- **No sale a la red.** Todo lo que muestra está en la máquina.
- **No aprueba sola.** La firma siempre es de una persona.

## 8. Lo que queda por decidir

| # | Duda | Qué la resuelve |
|---|---|---|
| 1 | Si la memoria se muestra completa o solo lo de los últimos meses | Se decide al ver cuánto crece, no antes |
| 2 | Si el expediente que se entrega incluye la auditoría | Es la duda 5 del análisis, y la responde el usuario |
| 3 | Si hace falta una pantalla de comprobaciones, o basta con que avisen | Se decide cuando haya comprobaciones corriendo |
