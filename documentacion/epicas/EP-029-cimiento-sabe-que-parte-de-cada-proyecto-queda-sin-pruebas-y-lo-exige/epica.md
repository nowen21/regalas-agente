# EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1 del pendiente 141](../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), aprobado el 2026-10-08. Los campos que no son alcance (tipo, prioridad, estimación, riesgos, supuestos) son propuesta del agente.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-029 |
| **Planteamiento de origen** | El [pendiente 141](../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md), V2: Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración |
| **Iniciativa / Objetivo estratégico** | Que Cimiento, como línea base, sepa y haga cumplir qué tan probado está cada proyecto que administra |
| **Producto / Sistema** | Cimiento y el instalador |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | XL: cinco HU |
| **Horizonte** | N/A |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | Terminada |

## 2. Resumen ejecutivo

En la página de cada proyecto, Cimiento deja elegir qué tan estricto ser con la revisión de pruebas y cada cuántos días hacerla. El botón «Revisar» corre las pruebas del proyecto con la herramienta de su lenguaje y guarda qué parte quedó sin pruebas; una página muestra todos los proyectos. Al empezar a trabajar, Cimiento avisa si la revisión falta o está vencida, y el instalador pone en cada proyecto la parte que revisa. La configuración vive solo en la base de Cimiento: sale la copia que cada proyecto tenía y nadie leía. Al final, Cimiento corre también las pruebas de navegador del proyecto que las tenga.

## 3. Problema y oportunidad

### 3.1 Situación actual

Ningún proyecto mide qué parte de su programa queda sin pruebas; la configuración no lo exige ni guarda el estado; ninguna prueba usa un navegador real; y `.agente/configuracion.md` se escribe en cada proyecto sin que ningún programa la lea.

### 3.2 Impacto de no hacerlo

Un hueco sin medir no se ve, y lo que corre en el navegador se puede dañar sin que falle ninguna prueba.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-1 de la sesión del 2026-10-07](../../../historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md) | Cimiento no sabe qué parte del programa de cada proyecto queda sin pruebas, ni lo exige |

## 4. Objetivo y propuesta de valor

**Objetivo:** que en cada proyecto se sepa qué parte queda sin pruebas y cuándo se revisó, y que Cimiento lo haga cumplir.

**Hipótesis de valor:**
> Creemos que una revisión que se arranca con un botón, se exige desde la configuración y se avisa al empezar a trabajar logrará que ningún proyecto acumule partes sin probar sin que nadie lo note. Lo sabremos cuando la página muestre la última revisión de cada proyecto registrado.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien administra los proyectos | Ve en una página qué tan probado está cada uno | Cualitativo |
| Quien trabaja en un proyecto | Recibe el aviso cuando la revisión está vencida | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Dos ajustes nuevos por proyecto y el estado de la revisión en la base.
- La revisión con coverage.py, PHPUnit con PCOV y `ng test --code-coverage`, según el lenguaje; el resto, «sin medición».
- El botón «Revisar», su orden de consola y la página con todos los proyectos.
- El aviso al empezar a trabajar y el bloqueo del commit cuando el proyecto lo pide.
- La parte que revisa, puesta por el instalador y quitada por el desinstalador.
- La salida de `.agente/configuracion.md`.
- Las pruebas de navegador con Playwright de los proyectos que las tengan.

### 5.2 Fuera del alcance

- Exigir un porcentaje mínimo (`08·T6`).
- Escribir las pruebas de navegador de cada proyecto (acuerdo 6).

### 5.3 Diferido a fases posteriores

- Herramientas para lenguajes que no son Python, PHP ni Angular.

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| Quien administra los proyectos | Elige qué tan estricto ser y arranca la revisión | Ver el estado de todos en un solo sitio |
| Quien trabaja en un proyecto | Programa y guarda los cambios | Saber a tiempo que toca revisar |

## 7. Criterios de aceptación de la épica

- [x] **CAE-01**: cada proyecto tiene en su página qué tan estricta es la revisión y cada cuántos días toca, y la base guarda el resultado.
- [x] **CAE-02**: el botón «Revisar» guarda qué parte quedó sin pruebas, con la herramienta del lenguaje del proyecto.
- [x] **CAE-03**: al empezar a trabajar, Cimiento avisa si la revisión falta o está vencida.
- [x] **CAE-04**: ningún proyecto tiene `.agente/configuracion.md`.
- [x] **CAE-05**: las pruebas de navegador de un proyecto corren desde Cimiento y su resultado sale en la página.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Proyectos registrados con al menos una revisión guardada | 0 | Todos los que tengan pruebas | Al cerrar la HU-002 | La página de revisiones |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| [HU-001](HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas/HU-001-la-configuracion-de-cada-proyecto-dice-que-tan-estricta-es-la-revision-de-pruebas.md) | La configuración de cada proyecto dice qué tan estricta es la revisión de pruebas y cada cuántos días toca | Must | M | No aplica | Terminada |
| [HU-002](HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas/HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md) | El botón «Revisar» muestra qué parte de cada proyecto queda sin pruebas | Must | L | No aplica | Terminada |
| [HU-003](HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida/HU-003-al-empezar-a-trabajar-cimiento-avisa-si-la-revision-falta-o-esta-vencida.md) | Al empezar a trabajar, Cimiento avisa si la revisión falta o está vencida | Must | M | No aplica | Terminada |
| [HU-004](HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece/HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md) | Cada proyecto consulta su configuración en Cimiento y la copia local desaparece | Must | S | No aplica | Terminada |
| [HU-005](HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto/HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md) | Cimiento corre las pruebas de navegador de cada proyecto | Must | M | No aplica | Terminada |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| `core/proyectos/ajustes.py` y la página del proyecto | Modificado | Los dos ajustes nuevos |
| Una app nueva, `core/pruebas/` | Nuevo | El estado de la revisión, la revisión por lenguaje y su página |
| `core/enganches/sesion.py` y `.githooks/pre-commit` | Modificado | El aviso y el bloqueo |
| `core/herramientas/instalar.py` y `desinstalar.py` | Modificado | La parte que revisa |
| `core/proyectos/copia.py` | Se quita | La copia local |

### 10.2 Decisiones de arquitectura (ADR)

Ninguna aparte: están en «Lo acordado» del análisis 1 del pendiente 141.

### 10.3 Integraciones

coverage.py, PHPUnit con PCOV, la orden `ng test` de Angular y Playwright.

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Usabilidad** | Avisos, opciones y botones se entienden sin saber del tema (`00·ID7`, acuerdo 8) |
| **Rendimiento** | La revisión corre solo al pedirla; el aviso lee la base sin arrancar Django |
| **Seguridad** | N/A |
| **Disponibilidad** | Sin base, el aviso no se cae: se calla |
| **Auditoría y trazabilidad** | Cada revisión queda con su fecha |
| **Escalabilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

- Se paga: la copia `.agente/configuracion.md`, que nadie lee.

## 11. Cumplimiento y normativa

N/A.

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | Las herramientas de cada lenguaje instaladas en la máquina donde corre el proyecto | Externa | Quien instala | Al revisar | Abierta |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | Revisar un proyecto grande tarda varios minutos | Alta | Medio | Solo corre al pedirla (acuerdo 11) | Agente |
| R-02 | Falta la herramienta del lenguaje en la máquina | Media | Bajo | La página dice qué falta, en palabras sencillas, y no falla | Agente |

## 14. Supuestos y restricciones

**Supuestos**
- Cada proyecto sabe correr sus pruebas desde su carpeta.

**Restricciones**
- `20·M3`: ninguna herramienta de un lenguaje entra a `base/`.

## 15. Hoja de ruta

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001 | Ninguna | Las demás leen estas opciones | Terminada |
| 2 | HU-002 | HU-001 | Guarda el resultado donde lo dejó la HU-001 | Terminada |
| 3 | HU-003 | HU-001, HU-002 | Compara las opciones con el resultado | Terminada |
| 4 | HU-004 | HU-001 | Sale cuando la configuración nueva ya vive en la base | Terminada |
| 5 | HU-005 | HU-002 | Acuerdo 2: va de última | Terminada |

## 16. Estrategia de entrega

| Tema | Cómo |
|---|---|
| Despliegue | En la máquina del usuario, HU por HU |
| Migración de datos | Tablas nuevas, aditivas |
| Plan de reversión | Revertir el commit de la HU |
| Capacitación y gestión del cambio | N/A |
| Soporte post-despliegue | N/A |

## 17. Definition of Ready (épica)

- [x] Problema y objetivo validados con el negocio
- [x] Alcance delimitado (dentro y fuera)
- [x] Métricas de éxito definidas y medibles
- [x] Historias de usuario identificadas
- [x] Dependencias y riesgos registrados
- [x] Viabilidad técnica evaluada
- [x] Capacidad confirmada

## 18. Definition of Done (épica)

- [x] Todas las HU obligatorias completadas y aceptadas
- [x] Criterios de aceptación de la épica verificados
- [ ] Requisitos no funcionales validados
- [x] Documentación técnica entregada
- [ ] Métricas midiendo

## 19. Referencias

- [Análisis 1 del pendiente 141](../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md)

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | Agente | Creación de la épica desde el análisis aprobado |
| 2026-10-08 | Agente | Terminadas las cinco HU, con los análisis 2 y 3 del pendiente 141: la épica queda terminada |
