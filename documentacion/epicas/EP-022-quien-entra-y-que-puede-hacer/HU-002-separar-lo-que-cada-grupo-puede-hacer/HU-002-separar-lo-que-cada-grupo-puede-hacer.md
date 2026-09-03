# HU-002 — Separar lo que cada grupo puede hacer

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-022 Quién entra y qué puede hacer](../epica.md) |
| **Funcionalidad** | `F-037` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Acceso |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-02, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien responde por lo que se aprueba
- **Quiero** que el agente no pueda aprobar lo que él mismo construyó
- **Para** que la aprobación siga siendo de una persona y no un trámite

---

## 3. Contexto y descripción

**`00·N1` pide que todo cambio de estado lo autorice una persona.** Un agente que se aprobara a sí mismo volvería la aprobación un trámite: firmaría su propio trabajo y el registro diría que hubo autorización.

**Son dos grupos y no cuatro.** El análisis define cuatro actores; solo dos entran. «Un proyecto administrado» no es una persona ni un programa que entre —es una carpeta que se observa—, y «quien recibe un proyecto» tiene escrito que **no puede entrar**. Construir cuatro grupos habría sido construir de más.

**Y `aprobar --quien` deja de ser texto libre.** Hasta hoy aceptaba cualquier nombre: una aprobación decía quién la dio y no lo probaba — que es exactamente el hueco que `EP-017` vino a tapar en los documentos, un nivel más abajo.

### 3.1 Reglas de negocio

- `RN-1` Hay dos grupos: `usuario` y `agente`.
- `RN-2` **El agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas.**
- `RN-3` El usuario puede todo: *«nada le está vedado»*, dice el análisis.
- `RN-4` **Una orden solo acepta el nombre de una cuenta que exista.**
- `RN-5` El rechazo dice **qué permiso falta y por qué existe**.

### 3.2 Supuestos

- Los perfiles del análisis caben en grupos de Django.

### 3.3 Fuera de alcance

- **Permisos por proyecto.** Un grupo rige en toda la plataforma.
- Perfiles para los dos actores que no entran.

---

## 4. Criterios de aceptación

### CA-01 — El agente no puede aprobar, publicar ni derogar

```gherkin
Dada una cuenta del grupo agente
Cuando intenta aprobar un documento
Entonces no se hace, y no queda ninguna aprobación
```

**Cómo validarlo:** intentándolo con las cuatro acciones restringidas.
- **Aprobado cuando:** ninguna pasa. **Es el criterio que decide.**

### CA-02 — El rechazo dice qué permiso falta

```gherkin
Dado un rechazo por permisos
Cuando se lee
Entonces nombra el permiso, dice por qué existe, y dice qué grupo lo tiene
```

**Cómo validarlo:** leyendo el motivo.
- **Aprobado cuando:** trae los tres datos.

### CA-03 — Una cuenta que no existe se rechaza

```gherkin
Dado un nombre que no es una cuenta
Cuando se intenta aprobar con él
Entonces no se hace, y se dice que la constancia diría quién sin probarlo
```

**Cómo validarlo:** aprobando con un nombre inventado.
- **Aprobado cuando:** no queda nada guardado.

### Criterios transversales

- El superusuario puede, aunque no esté en ningún grupo.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Un rechazo no deja nada a medio guardar |
| Claridad | El motivo del rechazo se entiende sin salir de la pantalla |

---

## 6. Diseño y referencias

- Funcionalidad `F-037` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- La sección 6 del [análisis](../../../../cvds/analisis-requisitos/README.md), que define los actores.
- La sección 8.3 del [diseño](../../../../cvds/diseno/README.md), que separa los dos grupos.

---

## 7. Tareas técnicas derivadas

1. Los dos grupos con sus permisos, que se puedan poner al día muchas veces.
2. Preguntar si una cuenta puede algo.
3. El rechazo con su porqué.
4. Que `aprobar` exija una cuenta con permiso.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [AB-EP-022-HU-002-el-agente-no-aprueba](AB-EP-022-HU-002-el-agente-no-aprueba/estado-fase.md) | Los tres CA | Cerrada el 2026-09-02: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que trae las cuentas |
| **Riesgo 1** | Que el agente se apruebe a sí mismo. No tiene el permiso |
| **Riesgo 2** | Que un rechazo deje algo a medio guardar. Se comprueba que no quede ninguna aprobación |
| **Riesgo 3** | Que construir cuatro grupos deje dos sin usar. Son dos, y se dice por qué |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La `HU-001` cerrada.
- ☑ La épica aprobada el 2026-09-02.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que el agente no aprueba.
- ☑ Comprobado que un rechazo no deja nada guardado.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita las cuentas de la `HU-001` |
| Negociable | Sí | Qué separa a los grupos se puede ajustar |
| Valiosa | Sí | Sin ella, una aprobación dice quién y no lo prueba |
| Estimable | Sí | Son grupos y permisos de Django |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se intenta con cada grupo y se mira |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-02 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
