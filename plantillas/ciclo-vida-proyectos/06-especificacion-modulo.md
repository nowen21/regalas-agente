# Especificación del módulo «NOMBRE DEL MÓDULO»  ·  `[CAPA 3 · plantilla de especificación]`

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> **Cómo se usa.** Es el esqueleto para redactar la especificación de **un** módulo. Se copia a `documentacion/«slug-modulo»/spec.md`, se reemplaza cada `«…»`, se responde cada `[[guía]]` y se borran las guías. Antes de escribir código, esta especificación debe estar completa y **aprobada** (`02·F2`). Ninguna sección se borra: si no aplica, se deja el título con "No aplica porque ...".

- **Slug del módulo:** `«slug-en-kebab»`
- **Estado:** `«borrador / aprobada / en implementación / cerrada»`

## 1. Propósito y alcance

> Presenta el módulo y fija sus bordes.

«Una o dos frases: qué se construye y para qué.»

- **Dentro de alcance:** «qué entra».
- **Fuera de alcance:** «qué no cubre este módulo, para cerrar expectativas» (`01·C3`).

## 2. Contexto · qué hay hoy

> Es lo que ya existe en el proyecto y se relaciona con el módulo.

[[Si es módulo nuevo: "Módulo nuevo, no hay código previo".]]
«Lo que ya existe relacionado con esto (archivos, tablas, servicios), con enlaces `archivo:línea`.» (`02·F1`)

## 3. Supuestos, dependencias y preguntas abiertas

> Es el filtro de ambigüedad: lo que falta confirmar, conseguir o aclarar.

[[Se llena antes de diseñar, `01·C7`.]]

- **Supuestos:** «lo que se da por cierto sin confirmar; cada uno es un riesgo si es falso».
- **Dependencias / prerequisitos:** «qué debe existir antes de arrancar (otros módulos, tablas, permisos, datos)».
- **Preguntas abiertas:** «lo que hay que aclarar antes de codear; ninguna debería quedar viva al empezar».

## 4. Reglas de negocio

> Son las invariantes que el código debe garantizar y que no se ven leyendo un archivo suelto (`13·DOC2`).

1. «Regla: de dónde baja (el identificador del requisito, la historia o la decisión), y por qué existe.»
2. «…»

[[Una regla de negocio no nace acá. Baja de un requisito, de una historia de usuario o de una decisión ya tomada, y por eso se pide el identificador y no una frase: «lo pidió el cliente» no se puede seguir hasta ninguna parte. La que no tenga procedencia no se escribe en esta sección: se sube a la historia que corresponda y baja desde allá. Una regla con buena justificación y ningún origen entra sin resistencia y sin dejar rastro de que entró, y de ahí baja sola a decisiones, trazabilidad, pruebas y criterios de aceptación.]]

## 5. Modelo de datos

> Son los datos que el módulo crea o cambia, y cómo afectan a lo que ya está guardado.

[[Diseño según regla base `03`: normalización, auditoría, catálogos, cero-hardcode. Nombres concretos según `mapeo-nombres.md` de capa 3.]]

- **Entidades nuevas / modificadas:** «tabla: campos, tipo, relaciones (FK), restricciones (UNIQUE), índices».
- **Valores configurables:** «qué va a catálogo en vez de quemarse en código» (`03·D4`).
- **Migración / compatibilidad:** «cómo afecta a datos existentes» (`03·D3`).

## 6. Comportamiento y flujos

> Es la lógica del módulo vista desde afuera.

«Cómo se comporta el módulo en sus casos principales: entrada, proceso y salida.»
[[Incluir el caso feliz y los caminos de error relevantes.]]

## 7. Interfaz / UI (si aplica)

> Es la parte del módulo que toca el usuario final. Si no hay UI, se escribe "No aplica porque...".

«Qué ve y hace el usuario final: pantallas, campos, acciones, estados (vacío/cargando/error).»

## 8. Permisos y autorización

> Dice quién puede hacer qué en el módulo.

[[Regla base `04·S1`: authz en el servidor + scope. Nombres según capa 3.]]

| Permiso | Quién lo tiene | Qué habilita |
|---|---|---|
| `«recurso.accion»` | «rol» | «…» |

## 9. Marco normativo (si aplica)

> Es lo que la ley o la norma le exige al módulo.

[[Solo si el módulo toca leyes/normas, regla `16`. El detalle del marco está en `marco-normativo.md` de capa 3.]]
«Qué exige la norma y cómo lo cumple el módulo. Si no aplica: "No aplica".»

## 10. Plan de pruebas

> Dice cómo se comprueba que el módulo cumple esta especificación.

[[Regla base `08` + triangulación [`08·T7`](«RUTA-ESTANDAR»/base/08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos). Se aprueba junto con esta especificación.]]

- Los escenarios que se cubren: caso feliz, casos límite, errores, permisos, validaciones.
- **Corner cases (derivados):** «valores de frontera, clases de equivalencia, casos inválidos».
- **Triangulación:** «para los cálculos, de qué fuentes independientes sale el resultado esperado».
- **Verificación manual:** «lo que el entorno de pruebas no cubre» (`08·T4`).

## 11. Criterios de aceptación (Definition of Done)

> Es la lista de condiciones que deben cumplirse para dar el módulo por terminado.

- [ ] «Comportamiento X funciona según esta especificación.»
- [ ] Pruebas verdes (incluida la triangulación de los cálculos).
- [ ] Trazabilidad de la especificación a la implementación sin faltantes (`13·DOC3`).
- [ ] Documentación persistida (regla `13`).
- [ ] «…»

## 12. Decisiones tomadas

> Son las decisiones cerradas, para que no se reabran (`13·DOC2`).

[[Fecha, motivo, y si se revierte una, dejar rastro.]]

- «`fecha`: decisión, y por qué.»

## 13. Trazabilidad (se completa al implementar)

> Muestra dónde quedó implementada cada afirmación técnica de esta especificación, con su evidencia (`13·DOC3`).

[[Una fila por afirmación técnica. Se llena al cerrar.]]

| Ítem de la especificación | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| «…» | «modelo/servicio/vista/prueba/permiso» | «archivo» | ⏳ | «enlace» |

## 14. Cruces con otros módulos

> Registra qué usa este módulo de otros y quién usa lo de este. Si no hay cruces en un sentido, esa tabla lleva una fila "Ninguno": vacía no dice si es que no hay o si es que nadie lo revisó.

[[`13·DOC7`: el cruce se registra en los **dos** documentos. Si esta especificación consume otro módulo, se anota abajo **y** el módulo consumido lo registra en su historial cruzado. Una mención de paso ("algo parecido se hizo en X") no es un cruce: no se anota.]]

**Qué consume este módulo de otros:**

| Módulo | Qué consume | Por qué |
|---|---|---|
| `«slug-del-otro-modulo»` | «servicio, tabla, evento, permiso» | «para qué lo necesita» |

**Historial cruzado, quién consume de este módulo:**

| Fecha | Módulo que consume | Qué cambió acá por eso |
|---|---|---|
| AAAA-MM-DD | `«slug-del-otro-modulo»` | «nada / se expuso X / se estabilizó el contrato de Y» |
