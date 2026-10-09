# EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo

> El alcance, los criterios y las HU salen de la propuesta final y de «Lo que se tiene que hacer» del [análisis 1 del pendiente 119](../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), aprobado el 2026-10-04. Los campos que no son alcance (tipo, prioridad, estimación, riesgos, supuestos) son propuesta del agente.

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-025 |
| **Planteamiento de origen** | El [pendiente 119](../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/pendiente.md), V2: nadie ve cuántos tokens se gastan ni puede ajustar las reglas sin tocar código |
| **Iniciativa / Objetivo estratégico** | Que Cimiento pueda evolucionar sin quedar atrapado por sus propias reglas, y que se sepa en qué se gastan los tokens |
| **Producto / Sistema** | Cimiento, la aplicación Django de `proyectos/cimiento/` |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | XL: diez HU |
| **Horizonte** | N/A |
| **Product Owner** | Ing. José Dúmar Jiménez Ruíz |
| **Tech Lead / Arquitecto** | N/A |
| **Estado** | En curso |

## 2. Resumen ejecutivo

Cimiento pasa a tener pantallas propias, sobre MariaDB, desde donde se registran los proyectos y se fija en cada uno qué tan rígida es cada regla, sin cambiar código. El freno del agente lee ese nivel de la base.

Además, Cimiento guarda cuántos tokens gasta cada proyecto y en qué (sesión, enganche, archivo leído y los demás niveles), lo muestra en vivo y avisa cuando un enganche o un archivo pesa demasiado. Con eso se decide qué pasar a un programa.

## 3. Problema y oportunidad

### 3.1 Situación actual

Cada regla se aplica como está escrita en el código, igual para todos los proyectos. Ajustarla es un cambio de código. Nadie ve cuántos tokens se gastan ni en qué: el dato existe en los `.jsonl` de Claude Code, que se borran a los 30 días.

### 3.2 Impacto de no hacerlo

Una regla fija puede bloquear a Cimiento para corregirse, como pasó el 2026-10-04. Y sin medir no se sabe qué automatizar primero.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [H-1 de la sesión del 2026-10-04](../../../historico-chat/resumenes/2026-10-04/sesion-2.md) | 1012 llamadas en una sesión, con unos 450 000 tokens releídos por llamada |
| [H-2 de la sesión del 2026-10-04](../../../historico-chat/resumenes/2026-10-04/sesion-2.md) | La regla de un solo análisis abierto bloqueó a Cimiento para cambiar esa misma regla |

## 4. Objetivo y propuesta de valor

**Objetivo:** que cada proyecto tenga su nivel de reglas configurado desde Cimiento y que el gasto de tokens se vea en vivo.

**Hipótesis de valor:**
> Creemos que una administración con niveles por regla y un tablero de gasto, para quien mantiene Cimiento y sus proyectos, logrará ajustar reglas sin tocar código y saber qué automatizar. Lo sabremos cuando un nivel se cambie desde la pantalla y el freno lo respete, y cuando el tablero muestre el gasto por enganche.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| Quien mantiene Cimiento | Corrige una regla sin quedar bloqueado por ella | Cualitativo |
| Quien mantiene Cimiento | Ve qué enganche o archivo gasta más tokens | Cuantitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Cimiento sobre MariaDB `cimiento`, con pantallas propias (Tabler, htmx y ApexCharts) y entrada con usuario.
- Registro de proyectos y niveles de cada regla por proyecto.
- El freno lee el nivel de la base y, sin conexión, no deja modificar nada.
- Gasto de tokens guardado, recibido en vivo, mostrado en un tablero y con avisos por límite.

### 5.2 Fuera del alcance

- Otras máquinas: todo corre en una sola (acuerdo 4).
- Otras herramientas de IA distintas de Claude Code: queda la separación entre leer el formato y guardar, para que se agreguen después.

### 5.3 Diferido a fases posteriores

- Un usuario propio de MariaDB para Cimiento, en vez de `root`, cuando la base deje de ser solo local.

### 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Administrar el nivel de las reglas por proyecto y ver el gasto de tokens |
| 2 | Actores | Administrador (registra proyectos, cambia niveles y límites) y consulta (solo ve) |
| 3 | Información | Proyecto (nombre, ruta, carpeta de Claude Code, límites), nivel por regla y proyecto, llamada con su gasto |
| 4 | Campos | Cada entidad tiene campos de identificación, ruta, nivel, límites y conteos; se especifican en cada HU |
| 5 | Validaciones | Ruta existente y única por proyecto; nivel dentro de los tres valores; límite numérico positivo |
| 6 | Reglas de negocio | Las reglas del núcleo siempre frenan y no se configuran; sin conexión a la base el freno no deja modificar |
| 7 | Estados | Proyecto activo o inactivo; nivel frena, avisa o apagada |
| 8 | Operaciones | Registrar, editar y desactivar proyectos; cambiar niveles y límites; consultar el tablero |
| 9 | Restricciones | El grupo consulta no cambia nada; nadie cambia el nivel de una regla del núcleo |
| 10 | Relaciones | Un proyecto tiene muchos niveles y muchas llamadas |
| 11 | Consultas | Lista de proyectos; tablero por proyecto, sesión, enganche y archivo leído |
| 12 | Mensajes | Aviso al agente cuando un enganche o archivo pasa su límite; aviso de base apagada |
| 13 | Errores | Ruta inexistente, base sin conexión, `.jsonl` ilegible: se informan y no se guarda nada a medias |
| 14 | Permisos | Por grupo de Django: administrador y consulta |
| 15 | Auditoría | Quién cambió cada nivel y cuándo |
| 16 | Resultado final | Niveles configurados desde la pantalla y respetados por el freno; gasto visible en vivo |
| 17 a 26 | Ciclo de vida, integraciones y demás | Integración con la telemetría de Claude Code (HU-007); configurabilidad por proyecto (HU-004); el correo que manda la telemetría es dato personal y no sale de la máquina; el resto no aplica porque Cimiento corre en una sola máquina para una persona |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| Administrador | Registra proyectos y fija niveles y límites | Ajustar reglas sin tocar código |
| Consulta | Mira el tablero | Ver el gasto |
| El agente | Lee los niveles a través del freno y recibe los avisos | Saber qué tan estricta es cada regla |

**Volumetría estimada:** una persona; decenas de proyectos; miles de llamadas por día.

## 7. Criterios de aceptación de la épica

- [x] **CAE-01** — Un nivel cambiado en la pantalla cambia lo que hace el freno en ese proyecto, y solo en ese.
- [x] **CAE-02** — Sin conexión a MariaDB, el freno no deja modificar nada y lo avisa.
- [x] **CAE-03** — El tablero muestra en vivo el gasto de todos los proyectos por proyecto, sesión, enganche y archivo leído.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| Cambios de regla hechos sin tocar código | 0 | Todos los de nivel | 30 días | Historia de niveles en la base |
| Gasto visible por enganche | No se mide | Medido en todos los proyectos | 30 días | El tablero |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| [HU-001](HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas/HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md) | Cimiento corre sobre MariaDB y tiene la base de sus pantallas | Must | N/A | N/A | Terminada |
| [HU-002](HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo/HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md) | Solo entra quien tiene cuenta, y cada grupo hace lo suyo | Must | N/A | N/A | Terminada |
| [HU-003](HU-003-los-proyectos-quedan-registrados-en-cimiento/HU-003-los-proyectos-quedan-registrados-en-cimiento.md) | Los proyectos quedan registrados en Cimiento | Must | N/A | N/A | Terminada |
| [HU-004](HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto/HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md) | Cada regla tiene su nivel en cada proyecto | Must | N/A | N/A | Terminada |
| [HU-005](HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar/HU-005-el-freno-aplica-el-nivel-guardado-y-sin-base-no-deja-modificar.md) | El freno aplica el nivel guardado, y sin base no deja modificar | Must | N/A | N/A | Terminada |
| [HU-006](HU-006-el-gasto-de-cada-llamada-queda-guardado/HU-006-el-gasto-de-cada-llamada-queda-guardado.md) | El gasto de cada llamada queda guardado | Must | N/A | N/A | Terminada |
| [HU-007](HU-007-el-gasto-llega-a-cimiento-en-vivo/HU-007-el-gasto-llega-a-cimiento-en-vivo.md) | El gasto llega a Cimiento en vivo | Should | N/A | N/A | Terminada |
| [HU-008](HU-008-el-gasto-se-ve-en-vivo-en-el-tablero/HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) | El gasto se ve en vivo en el tablero | Must | N/A | N/A | Terminada |
| [HU-009](HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado/HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) | Se avisa cuando un enganche o un archivo pesa demasiado | Should | N/A | N/A | Terminada |
| [HU-010](HU-010-el-gasto-se-ve-por-los-demas-niveles/HU-010-el-gasto-se-ve-por-los-demas-niveles.md) | El gasto se ve por los demás niveles | Could | N/A | N/A | Terminada |
| [HU-011](HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe/HU-011-el-gasto-llega-a-la-base-en-cuanto-claude-code-lo-escribe.md) | El gasto llega a la base en cuanto Claude Code lo escribe | Must | N/A | N/A | Terminada |
| [HU-012](HU-012-la-telemetria-se-retira/HU-012-la-telemetria-se-retira.md) | La telemetría se retira | Must | N/A | N/A | Terminada |
| [HU-013](HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas/HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas.md) | Cada proyecto tiene su configuración en tres capas | Must | N/A | N/A | Terminada |
| [HU-014](HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion/HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion.md) | Los avisos muestran las rutas como lo diga la configuración | Should | N/A | N/A | Terminada |
| [HU-015](HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar/HU-015-se-ve-lo-que-corre-sin-tokens-y-lo-que-conviene-automatizar.md) | Se ve lo que corre sin tokens y lo que conviene automatizar | Should | N/A | N/A | Terminada |
| [HU-016](HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento/HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento.md) | Cerrar y reabrir una fase, y separar los cambios por sesión, son funcionalidades de Cimiento | Must | N/A | N/A | Terminada |
| [HU-017](HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace/HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace.md) | El freno no deja escribir un guion para lo que Cimiento ya hace | Should | N/A | N/A | Terminada |
| [HU-018](HU-018-cimiento-trae-su-ayuda-y-su-manual/HU-018-cimiento-trae-su-ayuda-y-su-manual.md) | Cimiento trae su ayuda y su manual | Should | N/A | N/A | Terminada |
| [HU-019](HU-019-toda-accion-trae-su-contraria/HU-019-toda-accion-trae-su-contraria.md) | Toda acción trae su contraria | Must | N/A | N/A | Terminada |
| [HU-020](HU-020-lo-que-crea-el-andamio-se-puede-quitar/HU-020-lo-que-crea-el-andamio-se-puede-quitar.md) | Lo que crea el andamio se puede quitar | Must | N/A | N/A | Terminada |
| [HU-021](HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto/HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto.md) | El estándar se puede desinstalar de un proyecto | Should | N/A | N/A | Terminada |
| [HU-022](HU-022-un-pendiente-cerrado-se-puede-reabrir/HU-022-un-pendiente-cerrado-se-puede-reabrir.md) | Un pendiente cerrado se puede reabrir | Should | N/A | N/A | Terminada |
| [HU-023](HU-023-el-analisis-se-prende-desde-un-turno-anterior/HU-023-el-analisis-se-prende-desde-un-turno-anterior.md) | El análisis se prende desde un turno anterior | Should | N/A | N/A | Terminada |
| [HU-024](HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos/HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos.md) | El aviso del freno dice cómo salir sin tocar archivos | Must | N/A | N/A | Terminada |
| [HU-025](HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento/HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) | Cada línea del `.jsonl` queda en la base en el momento | Must | N/A | N/A | En curso |
| [HU-026](HU-026-la-pantalla-gasto-dice-primero-lo-importante/HU-026-la-pantalla-gasto-dice-primero-lo-importante.md) | La pantalla «Gasto» dice primero lo importante | Must | N/A | N/A | Terminada |
| [HU-027](HU-027-la-pantalla-se-entera-en-el-momento/HU-027-la-pantalla-se-entera-en-el-momento.md) | La pantalla se entera en el momento de lo que guarda el vigilante | Must | N/A | N/A | En curso |
| [HU-028](HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto/HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md) | El trabajo de cada mensaje sale de lo que está abierto | Must | N/A | N/A | Terminada |
| [HU-029](HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo/HU-029-el-vigilante-se-reinicia-solo-cuando-cambia-su-codigo.md) | El vigilante se reinicia solo cuando cambia su código | Must | N/A | N/A | Terminada |
| [HU-030](HU-030-el-resumen-del-gasto-responde-en-la-mitad-del-tiempo-y-no-se-recalcula-con-cada-aviso/HU-030-el-resumen-del-gasto-responde-en-la-mitad-del-tiempo-y-no-se-recalcula-con-cada-aviso.md) | El Resumen del gasto responde en la mitad del tiempo y no se recalcula con cada aviso | Should | S | N/A | Terminada |
| [HU-031](HU-031-cerrar-fase-entiende-los-formatos-de-las-plantillas-y-marca-todo-lo-que-cierra/HU-031-cerrar-fase-entiende-los-formatos-de-las-plantillas-y-marca-todo-lo-que-cierra.md) | `cerrar_fase` entiende los formatos de las plantillas y marca todo lo que cierra | Must | M | N/A | Terminada |
| [HU-032](HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender/HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md) | Cada momento de cada enganche y cada revisión de git se puede suspender desde Cimiento | Must | L | N/A | Terminada |

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| `proyectos/cimiento/config/` | Modificado | MariaDB, archivos de npm, módulos nuevos |
| `proyectos/cimiento/core/` | Nuevo | Módulos de administración y de consumo |
| `core/enganches/freno.py` | Modificado | Lee el nivel de MariaDB |
| `core/enganches/presupuesto.py` | Modificado | La suma se extiende, no se copia |
| `plantillas/estructura-proyecto-django.md` | Modificado | Admite dependencias de npm |

### 10.2 Decisiones de arquitectura (ADR)

Ninguna aparte: las decisiones están en «Lo acordado» del análisis 1 del pendiente 119.

### 10.3 Integraciones

| Sistema externo | Protocolo | Responsable | Estado del acuerdo |
|---|---|---|---|
| Telemetría de Claude Code | OpenTelemetry por HTTP | Anthropic | Documentado, verificado el 2026-10-04 |

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | El freno consulta el nivel sin arrancar Django |
| **Seguridad** | La conexión a la base se lee del `.env`, que no se versiona (`00·N6`) |
| **Disponibilidad** | Sin base, el freno no deja modificar |
| **Auditoría y trazabilidad** | Queda quién cambió cada nivel y cuándo |
| **Escalabilidad** | N/A: una máquina |
| **Accesibilidad** | N/A |

### 10.5 Deuda técnica generada o pagada

- `root` sin contraseña en MariaDB: se paga cuando la base salga de la máquina (§5.3).

## 11. Cumplimiento y normativa

| Norma / Política | Requisito aplicable | Cómo se cumple |
|---|---|---|
| Capítulo `12` de privacidad | El correo del usuario llega con la telemetría | Se guarda solo en la base local |

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | MariaDB 11.4 corriendo en el puerto 3307 con la base `cimiento` | Técnica | Usuario | Antes de HU-001 | Resuelta: verificada el 2026-10-04 |

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | MariaDB apagada detiene todo el trabajo | Media | Alto | El aviso dice que hay que prenderla | Usuario |
| R-02 | La telemetría cambia de formato | Baja | Medio | La lectura de los `.jsonl` sigue como respaldo | Agente |

## 14. Supuestos y restricciones

**Supuestos**
- Una sola máquina y una sola persona.

**Restricciones**
- Django con plantillas propias, sin frontend aparte; lo nuevo va como clases en `proyectos/cimiento/core/`.

## 15. Hoja de ruta

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001 | Ninguna | Todo lo demás guarda en la base y usa las pantallas | Terminada |
| 2 | HU-002 | HU-001 | Las pantallas de administración nacen protegidas | Terminada |
| 3 | HU-003 | HU-002 | Los niveles y el gasto son de un proyecto | Terminada |
| 4 | HU-004 | HU-003 | El nivel es de una regla en un proyecto | Terminada |
| 5 | HU-005 | HU-004 | Sin niveles guardados no hay qué leer | Terminada |
| 6 | HU-006 | HU-003 | Sin datos guardados no hay qué mostrar | Terminada |
| 7 | HU-007 | HU-006 | Guarda en las mismas tablas | Terminada |
| 8 | HU-008 | HU-006, HU-007 | Necesita datos y la llegada en vivo | Terminada |
| 9 | HU-009 | HU-003, HU-006 | Usa los límites del registro y los datos guardados | Terminada |
| 10 | HU-010 | HU-008 | Amplía lo que ya funciona | Terminada |
| 11 | HU-020 | Ninguna | Sin quitar, cada error del andamio se arregla a mano | Terminada |
| 12 | HU-016 | Ninguna | Cerrar fases es lo que más se repite | Terminada |
| 13 | HU-019 | HU-020 | La regla general, con el andamio de primer ejemplo | Terminada |
| 14 | HU-022 | HU-019 | Contraria de cerrar un pendiente | Terminada |
| 15 | HU-023 | Ninguna | Contraria de olvidar prender el análisis | Terminada |
| 16 | HU-021 | HU-019 | Contraria de instalar | Terminada |
| 17 | HU-011 | HU-006 | El tablero deja de leer los `.jsonl` | Terminada |
| 18 | HU-012 | HU-011 | Se retira cuando el gasto ya llega solo | Terminada |
| 19 | HU-013 | HU-003 | La configuración por proyecto en la base | Terminada |
| 20 | HU-014 | HU-013 | Lee la configuración | Terminada |
| 21 | HU-024 | HU-013 | La salida del freno usa la suspensión | Terminada |
| 22 | HU-015 | HU-011 | Mide lo que corre | Terminada |
| 23 | HU-017 | HU-016 | Necesita las funcionalidades que reemplazan guiones | Terminada |
| 24 | HU-018 | HU-001 | Las pantallas existen | Terminada |

## 16. Estrategia de entrega

| Tema | Cómo |
|---|---|
| Despliegue | En la máquina del usuario, HU por HU |
| Migración de datos | No aplica: la base SQLite de Cimiento no tiene datos propios |
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

- [ ] Todas las HU obligatorias completadas y aceptadas
- [ ] Criterios de aceptación de la épica verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica entregada
- [ ] Métricas midiendo

## 19. Referencias

- [Análisis 1 del pendiente 119](../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md)

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Agente | Creación de la épica desde el análisis aprobado |
| 2026-10-09 | Agente | Suma la HU-030, del análisis 1 del pendiente 146 |
| 2026-10-09 | Agente | Suma la HU-031, del análisis 1 del pendiente 150 |
| 2026-10-09 | Agente | Suma la HU-032, del análisis 1 del pendiente 149 |
