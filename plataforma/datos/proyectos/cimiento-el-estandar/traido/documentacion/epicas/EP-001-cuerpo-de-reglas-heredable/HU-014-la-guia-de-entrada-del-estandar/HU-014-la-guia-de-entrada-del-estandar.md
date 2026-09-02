# HU-014 — La guía de entrada del estándar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-014 |
| **Épica** | [EP-001 — Cuerpo de reglas heredable y en capas](../epica.md) |
| **Componente** | Cuerpo de reglas |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario, vía el proyecto `matematica` (pendiente 73) |
| **Estado** | Terminada |
## 2. Narrativa

- **Como** quien llega a un proyecto que hereda el estándar sin conocer sus reglas
- **Quiero** un documento de entrada, en lenguaje llano, que explique el ciclo completo del desarrollo y las cualidades que exige un producto en producción, enlazando cada punto a la regla o capítulo que lo manda
- **Para** entender por qué se trabaja así sin tener que leer el cuerpo normativo, y que ningún proyecto escriba su propia versión que después diverja

## 3. Contexto y descripción

En el proyecto `matematica` quedó escrita, a pedido del usuario, una guía que resume los 10 pasos del ciclo de desarrollo y las 9 cualidades del producto para producción. Nada de su contenido es de ese proyecto: es la cadena `02·F0` y el mapa de los capítulos `03` a `12` y los patrones opt-in, dichos en lenguaje de entrada. Doctrina transversal guardada en un solo proyecto es el mismo defecto que la memoria local: los demás no la ven, y si cada uno escribe la suya, divergen.

Es el [pendiente 73](../../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md); el material de partida está en su adjunto `73-adjunto-guia-desarrollo-profesional.md`, copia literal de la guía de origen (borrado al cerrar, como el pendiente ordenaba; el historial de git lo conserva).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La guía vive en el estándar y los proyectos la referencian; ninguno la copia |
| RN-02 | Cada paso y cada cualidad enlaza a la regla o capítulo que lo exige — la guía explica, no legisla |
| RN-03 | La guía no crea exigencia nueva: si algo suyo debe volverse norma, sigue el procedimiento del capítulo `20` aparte |
| RN-04 | Se escribe agnóstica de stack y de dominio (`20·M3`): lo que en el adjunto era del proyecto de origen no entra |

### 3.2 Supuestos

- El documento no se suma al núcleo que el cargador entrega al abrir sesión: es material de consulta, como el glosario, y no gasta el techo de 90 KB.

### 3.3 Fuera de alcance

- Crear reglas o validadores nuevos. La guía es doctrinal.
- El reemplazo físico de la copia en `matematica`: eso es del proyecto de origen, avisado al cerrar.
- El pendiente 74 (inventario de funcionalidades), aunque toque la misma zona del flujo.

## 4. Criterios de aceptación

### CA-01 — La guía existe en el estándar, completa y enlazada al cuerpo normativo

```gherkin
Dado que el material de la guía está en el adjunto del pendiente 73
Cuando el estándar la adopta como documento propio
Entonces existe en base/ un documento de entrada con los 10 pasos y las 9 cualidades
Y cada paso y cada cualidad enlaza a la regla o capítulo del estándar que lo exige
Y nada del proyecto de origen queda en el texto
```

**Cómo validarlo:**

1. Abrir el documento nuevo en `base/` y contar: 10 pasos y 9 cualidades. Resultado esperado: están todos.
2. Recorrer los enlaces: cada paso apunta a su regla de flujo, cada cualidad a su capítulo o patrón opt-in. Resultado esperado: ningún punto queda sin ancla al cuerpo normativo, y ningún enlace roto.
3. Compararlo contra el adjunto. Resultado esperado: ningún contenido transversal se perdió, y lo que era del proyecto de origen (su tabla de correspondencia, sus rutas) no está.
- **Aprobado cuando:** las tres cosas dan lo esperado y `validar.py estandar` no reporta enlaces rotos en el documento.

### CA-02 — La guía llega a los herederos y se encuentra sin saber que existe

```gherkin
Dado que la guía vive en base/
Cuando un proyecto instala o actualiza el estándar
Entonces la recibe con base/ igual que el glosario
Y el README de base/ la nombra como puerta de entrada
```

**Cómo validarlo:**

1. Comprobar que el documento está dentro de `base/` (lo que viaja es la carpeta entera). Resultado esperado: viaja sin tocar el instalador.
2. Abrir el README de `base/` y el mapa del sitio. Resultado esperado: la nombran, con una línea que dice para quién es.
3. Comprobar que el cargador no la suma al texto de apertura. Resultado esperado: el techo de 90 KB no se mueve.
- **Aprobado cuando:** el documento viaja con `base/`, está enlazado desde su README y el mapa, y el arranque no crece.

### Criterios de aceptación transversales

- [ ] **No regresión** — ninguna regla existente cambia; la guía solo cita.

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Legibilidad | La entiende quien no conoce el estándar (`00·ID7`): lenguaje llano, jerga solo con su enlace |
| Neutralidad | Agnóstica de stack, de dominio y de herramienta (`20·M3`) |

## 6. Tareas técnicas derivadas

- [x] Escribir el documento en `base/` desde el adjunto, enlazando cada punto.
- [x] Enlazarlo desde el README de `base/` y el mapa del sitio.
- [x] Versionar (MENOR) y cerrar el pendiente 73 con su aviso al proyecto de origen.

## 7. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional](A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional/plan_trabajo.md) | CA-01 y CA-02 | **Cerrada 2026-08-21, Cumple** (2 de 2 casos; v28.2.0) |

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | El adjunto del pendiente 73 como material de partida | Alto |
| Riesgo | Que la guía repita normas con otras palabras y divergan | RN-02: la guía enlaza, no re-enuncia exigencias |
| Riesgo | Que crezca hasta ser un segundo cuerpo normativo | RN-03 y el fuera de alcance lo cortan |

## 9. Definition of Ready

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y verificables
- [x] Material de partida disponible (el adjunto)
- [x] Dependencias identificadas

## 10. Definition of Done

- [x] Documento publicado en `base/`, enlazado desde README y mapa
- [x] Todos los criterios de aceptación verificados
- [x] Versión subida y pendiente 73 cerrado con su aviso

## 11. Validación INVEST

| Criterio | Cumple | Observación |
|---|:--:|---|
| Independiente | Sí | Solo necesita el adjunto, que ya está en el repo |
| Negociable | Sí | La forma final del documento se discute |
| Valiosa | Sí | Evita que cada proyecto escriba su versión y diverja |
| Estimable | Sí | Un documento con enlaces |
| Pequeña | Sí | Una fase |
| Testeable | Sí | Conteo, enlaces y comparación contra el adjunto |

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-21 | El agente, por orden del usuario («73») | Creación desde el pendiente 73, reportado por `matematica` |
| 2026-08-21 | El agente, con HU y planes aprobados por el usuario | Fase A cerrada en Cumple; nace `base/guia-de-entrada.md`, versión 28.2.0, pendiente 73 a `hecho/` con aviso a los 9 instalados |
