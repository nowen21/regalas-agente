# Especificación del módulo Auditoría  ·  `[CAPA 3]`

- **Slug del módulo:** `auditoria`
- **Estado:** aprobada, el 2026-08-25 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 1, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Dejar constancia de qué se hizo en la plataforma: quién, cuándo, sobre qué y qué cambió. Sirve para rastrear cualquier cambio hasta su origen meses después.

- **Dentro de alcance:** registrar cada acción que cambia algo, y enlazar lo que cada sesión dejó escrito (`F-018`).
- **Fuera de alcance:** consultar lo registrado con filtros (`F-019`, versión 4), y guardar la conversación completa de las sesiones.

## 2. Contexto — qué hay hoy

Módulo nuevo. Lo más parecido que existe es el historial del control de versiones, que dice qué archivo cambió pero no responde quién aprobó qué ni por qué se hizo.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que registrar la acción alcanza, y que el porqué queda cubierto por lo que la sesión escribe: el resumen y las decisiones.
- **Dependencias:** el módulo Proyectos, para saber en qué proyecto ocurrió cada acción.
- **Preguntas abiertas:** ninguna. La duda 2 del análisis se resolvió el 2026-08-25: se registran **las acciones más lo que la sesión dejó escrito**, y la transcripción se sigue guardando aparte, sin entrar a la auditoría.

## 4. Reglas de negocio

1. **Lo registrado no se edita ni se borra.** Baja de `DA-08`: un registro editable no sirve para demostrar nada.
2. **Toda acción que cambia algo se registra.** Baja de `RF-18` y de `RNF-12`.
3. **Ninguna credencial entra al registro.** Baja de `RN-9`: lo que se guarda hoy se publica mañana.
4. **Se registra la acción, no la conversación.** Baja de `DA-08` y del alcance aprobado en la etapa 1.
5. **Lo que la sesión dejó escrito se enlaza desde el registro.** Baja de la decisión del 2026-08-25: la acción dice qué se hizo, y el resumen dice por qué. Sin ese enlace, la auditoría responde una pregunta y no la otra.

## 5. Modelo de datos

- **Entidad:** `Registro de auditoría`, con los campos de la sección 3 del [modelo de datos](../../cvds/diseno/modelo-de-datos.md): qué se hizo, sobre qué, quién, cuándo, qué cambió y en qué proyecto.
- **Campo adicional:** `sesión`, para enlazar el registro con lo que esa sesión dejó escrito. Vacío si la acción no vino de una sesión del agente.
- **Cómo se guarda:** texto que solo se agrega. No hay operación de editar ni de borrar, y eso es parte del diseño, no un olvido.
- **Índice:** por proyecto y por fecha, para que la consulta de la versión 4 no lea todo el historial.
- **Migración:** no aplica.

## 6. Comportamiento y flujos

**Registrar.** Cada vez que un módulo cambia algo, entrega la acción con sus datos. Se agrega al final del registro y se indexa. Si el registro no se puede escribir, **la acción no se da por hecha**: primero queda la constancia, después el efecto.

- Acción sin proyecto asociado, como publicar una versión de reglas: se registra igual, con el campo de proyecto vacío.
- Acción hecha en una sesión del agente: queda enlazada con esa sesión, para poder leer después el resumen y las decisiones que la explican.
- Sesión que no dejó nada escrito: el enlace queda vacío, y eso también es un dato.
- Texto que trae algo parecido a una credencial: se tapa antes de escribir.
- El registro no se puede escribir: se avisa y la acción se detiene.

## 7. Interfaz

En la versión 1 no tiene pantalla: solo registra. La pantalla `P-09` llega en la versión 4, con `F-019`.

## 8. Permisos y autorización

Un solo usuario. El campo `quién` distingue si la acción la hizo el usuario o el agente, que es lo único que hoy hay que separar.

## 9. Marco normativo

No aplica. Si algún día la plataforma guarda datos de clientes, esta sección se rehace: un registro que no se puede borrar choca con el derecho a que borren lo suyo.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Registrar | Acción con proyecto · acción global · acción del usuario · acción del agente · acción dentro de una sesión, con su enlace |
| Integridad | Intentar editar un registro · intentar borrarlo |
| Credenciales | Texto con una clave entre comillas · sin comillas · palabra que solo lo parece |
| Falla | El registro no se puede escribir: la acción se detiene |
| Que NO pase | Que una acción cambie algo sin quedar registrada |

## 11. Criterios de aceptación

- `CA-1` Toda acción que cambia algo queda registrada.
- `CA-2` El registro dice quién, cuándo y sobre qué.
- `CA-3` Lo registrado no se puede editar ni borrar.
- `CA-4` Si el registro no se puede escribir, la acción no se ejecuta.
- `CA-5` Ninguna credencial queda en el registro.
- `CA-6` Una acción hecha en una sesión queda enlazada con lo que esa sesión dejó escrito.
- `CA-7` La conversación completa no entra al registro.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Primero la constancia, después el efecto | Ejecutar y registrar después | Si falla en medio, queda un cambio del que nadie sabe |
| Se registra la acción, no el contenido completo | Guardar el antes y el después enteros | El texto ya está versionado; duplicarlo dobla el tamaño sin agregar verdad |
| Se enlaza lo que la sesión dejó escrito | Guardar la conversación entera, o no guardar nada de ella | La acción dice qué se hizo; el resumen dice por qué. La transcripción completa pesa mucho, se llena de ruido y arrastra credenciales |
| Sin pantalla en la versión 1 | Construir la consulta desde el principio | Registrar temprano es barato; consultar puede esperar |

## 13. Trazabilidad

| Funcionalidad | Requisito | Fase que lo construye |
|---|---|---|
| F-018 | RF-18 | D |
| F-019 | RF-19 | Versión 4 |

## 14. Cruces con otros módulos

- **Todos los módulos** le entregan sus acciones.
- **Proyectos:** aporta en qué proyecto ocurrió cada una.
- **Seguridad:** tapa las credenciales antes de que lleguen al registro.
