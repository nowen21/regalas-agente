# Especificación del módulo «NOMBRE DEL MÓDULO»  ·  `[CAPA 3 · plantilla de especificación]`

> **Cómo se usa.** Es el esqueleto para redactar la especificación de **un** módulo. Se copia a `documentacion/«slug-modulo»/spec.md`, se reemplaza cada `«…»`, se responde cada `[[guía]]` y se borran las guías. **Antes de escribir código, esta especificación debe estar completa y aprobada** (regla base `02`·F2). Ninguna sección se borra: si no aplica, se deja el título con "No aplica porque ...".

- **Slug del módulo:** `«slug-en-kebab»`
- **Estado:** `«borrador / aprobada / en implementación / cerrada»`

---

## 1. Propósito y alcance

«Una o dos frases: qué se construye y para qué.»

- **Dentro de alcance:** «qué entra».
- **Fuera de alcance:** «qué NO cubre este módulo, para cerrar expectativas» (regla `01`·C3).

## 2. Contexto — qué hay hoy

[[Si es módulo nuevo: "Módulo nuevo, no hay código previo".]]
«Lo que ya existe relacionado con esto (archivos, tablas, servicios), con enlaces `archivo:línea`.» (regla `02`·F1)

## 3. Supuestos, dependencias y preguntas abiertas

[[Se llena ANTES de diseñar. Es el filtro de ambigüedad, regla `01`·C7.]]

- **Supuestos:** «lo que se da por cierto sin confirmar; cada uno es un riesgo si es falso».
- **Dependencias / prerequisitos:** «qué debe existir antes de arrancar (otros módulos, tablas, permisos, datos)».
- **Preguntas abiertas:** «lo que hay que aclarar antes de codear; ninguna debería quedar viva al empezar».

## 4. Reglas de negocio

[[Las invariantes que el código debe garantizar y que no se ven leyendo un archivo suelto — regla `13`·DOC2.]]

1. «Regla — de dónde baja (el identificador del requisito, la historia o la decisión) — por qué existe.»
2. «…»

[[**Una regla de negocio no nace acá.** Baja de un requisito, de una historia de usuario o de una decisión ya tomada, y por eso se pide el identificador y no una frase: «lo pidió el cliente» no se puede seguir hasta ninguna parte. La que no tenga procedencia **no se escribe en esta sección**: se sube a la historia que corresponda y baja desde allá. Una regla con buena justificación y ningún origen entra sin resistencia y sin dejar rastro de que entró — y de ahí baja sola a decisiones, trazabilidad, pruebas y criterios de aceptación.]]

## 5. Modelo de datos

[[Diseño según regla base `03`: normalización, auditoría, catálogos, cero-hardcode. Nombres concretos según `mapeo-nombres.md` de capa 3.]]

- **Entidades nuevas / modificadas:** «tabla → campos, tipo, relaciones (FK), restricciones (UNIQUE), índices».
- **Valores configurables:** «qué va a catálogo en vez de quemarse en código» (regla `03`·D4).
- **Migración / compatibilidad:** «cómo afecta a datos existentes» (regla `03`·D3).

## 6. Comportamiento y flujos

«Cómo se comporta el módulo en sus casos principales: entrada → proceso → salida.»
[[Incluir el caso feliz y los caminos de error relevantes.]]

## 7. Interfaz / UI (si aplica)

«Qué ve y hace el usuario final: pantallas, campos, acciones, estados (vacío/cargando/error).»
[[Si no hay UI: "No aplica".]]

## 8. Permisos y autorización

[[Regla base `04`·S1: authz en el servidor + scope. Nombres según capa 3.]]

| Permiso | Quién lo tiene | Qué habilita |
|---|---|---|
| `«recurso.accion»` | «rol» | «…» |

## 9. Marco normativo (si aplica)

[[Solo si el módulo toca leyes/normas — regla `16`. El detalle del marco está en `marco-normativo.md` de capa 3.]]
«Qué exige la norma y cómo lo cumple el módulo. Si no aplica: "No aplica".»

## 10. Plan de pruebas

[[Regla base `08` + triangulación [`08·T7`](«RUTA-ESTANDAR»/base/08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos). Se aprueba junto con esta especificación.]]

- **Escenarios:** caso feliz, casos límite, errores, permisos, validaciones.
- **Corner cases (derivados):** «valores de frontera, clases de equivalencia, casos inválidos».
- **Triangulación:** «para los cálculos, de qué fuentes independientes sale el resultado esperado».
- **Verificación manual:** «lo que el entorno de pruebas no cubre» (regla `08`·T4).

## 11. Criterios de aceptación (Definition of Done)

- [ ] «Comportamiento X funciona según esta especificación.»
- [ ] Pruebas verdes (incluida la triangulación de los cálculos).
- [ ] Trazabilidad especificación → implementación sin faltantes (regla `13`·DOC3).
- [ ] Documentación persistida (regla `13`).
- [ ] «…»

## 12. Decisiones tomadas

[[Decisiones cerradas, para que no se reabran — regla `13`·DOC2. Fecha, motivo, y si se revierte una, dejar rastro.]]

- «`fecha` — decisión — por qué.»

## 13. Trazabilidad (se completa al implementar)

[[Tabla de la regla `13`·DOC3: una fila por afirmación técnica de esta especificación, con dónde quedó implementada y su evidencia. Se llena al cerrar.]]

| Ítem de la especificación | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| «…» | «modelo/servicio/vista/prueba/permiso» | «archivo» | ⏳ | «enlace» |

## 14. Cruces con otros módulos

[[Regla `13`·DOC7: el cruce se registra en los **dos** documentos. Si esta especificación consume otro módulo, se anota abajo **y** el módulo consumido lo registra en su historial cruzado. Una mención de paso ("algo parecido se hizo en X") no es un cruce: no se anota.]]

**Qué consume este módulo de otros:**

| Módulo | Qué consume | Por qué |
|---|---|---|
| `«slug-del-otro-modulo»` | «servicio, tabla, evento, permiso» | «para qué lo necesita» |

**Historial cruzado — quién consume de este módulo:**

| Fecha | Módulo que consume | Qué cambió acá por eso |
|---|---|---|
| AAAA-MM-DD | `«slug-del-otro-modulo»` | «nada / se expuso X / se estabilizó el contrato de Y» |

_(Si no hay cruces en un sentido, se deja la tabla con una fila "Ninguno". Vacía no dice si es que no hay o si es que nadie lo revisó.)_
