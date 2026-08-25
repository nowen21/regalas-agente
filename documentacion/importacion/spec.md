# Especificación del módulo Importación  ·  `[CAPA 3]`

- **Slug del módulo:** `importacion`
- **Estado:** aprobada, el 2026-08-25 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 1, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Traer a la plataforma la documentación que un proyecto ya tiene escrita, para empezar a gobernarlo sin rehacer su historia.

- **Dentro de alcance:** traer lo que siga un molde conocido (`F-027`), y reportar lo que no se reconoció (`F-028`).
- **Fuera de alcance:** transformar lo que no tiene forma conocida, corregir lo traído, y tocar el proyecto de origen.

## 2. Contexto — qué hay hoy

Módulo nuevo. **El caso real de prueba es este mismo repositorio**, que tiene documentación de sobra: siete épicas, más de cien historias, más de cien fases con sus planes y resultados, reglas, memoria y pendientes. Si el módulo no puede con esto, no puede con nada.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que buena parte de lo escrito sigue un molde conocido; que lo que no lo sigue es minoría y se puede listar.
- **Dependencias:** el módulo Proyectos, porque solo se trae a un proyecto ya conectado.
- **Preguntas abiertas:** ninguna que detenga. **La incertidumbre es cuánta documentación se va a reconocer**, y por eso esta fase va temprano en la versión 1: se sabrá probando, no discutiendo.

## 4. Reglas de negocio

1. **Traer no modifica el proyecto de origen.** Baja de `DA-10` y de `RN-2`: si algo sale mal, el proyecto queda como estaba.
2. **Lo que no se reconoce no se transforma.** Baja de la ficha `F-028`: se reporta y lo decide el usuario.
3. **Traer dos veces no duplica.** Baja de la ficha `F-027`.
4. **Nada se pierde en silencio.** Baja de `RN-4`: lo que no entró, se dice cuál es y dónde está.

## 5. Modelo de datos

- **Entidades que se crean al traer:** `Documento` y sus versiones, `Épica`, `Historia`, `Fase` y `Funcionalidad`, según lo que se reconozca.
- **Qué se guarda de cada uno:** su tipo, su contenido y de qué archivo salió, para poder volver a mirarlo.
- **Lo que no se reconoce:** no crea entidad. Queda en el reporte, con su ruta.
- **Migración:** no aplica; lo traído es nuevo para la plataforma.

## 6. Comportamiento y flujos

**Traer.** Se recorre la carpeta del proyecto, se identifica cada documento por su forma, y se crea lo reconocido dentro de la plataforma. Antes de escribir nada se muestra qué se va a traer, y el usuario confirma.

- Documento que sigue un molde conocido: entra con su tipo.
- Documento que no se reconoce: no entra, y va al reporte.
- Un documento que ya se trajo antes: no se duplica; se dice que ya estaba.
- Nombres repetidos dentro del proyecto: se avisa antes de traer, y el usuario decide.
- Falla a mitad: se descarta lo traído en esa pasada, y el proyecto de origen queda intacto.

**Reportar lo no reconocido.** Al terminar, se lista qué quedó afuera y dónde está cada archivo. Si todo se reconoció, se dice, en vez de mostrar una lista vacía.

## 7. Interfaz

Pantalla `P-11` del [diseño de interfaz](../../cvds/diseno/diseno-de-interfaz.md): muestra qué se encontró, qué se reconoció y qué no, y pide confirmación antes de traer.

## 8. Permisos y autorización

Un solo usuario. Traer es una acción que cambia el estado de la plataforma, así que pide confirmación y queda registrada en la auditoría.

## 9. Marco normativo

No aplica, con una advertencia: **la documentación de un proyecto puede contener información de un cliente**. Traerla no la publica, porque todo queda en la máquina del usuario, pero el día que la plataforma corra en un servidor, esta sección se rehace.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Traer | Proyecto con documentos que siguen el molde · proyecto sin documentación · proyecto con documentos mezclados |
| No duplicar | Traer dos veces el mismo proyecto |
| Reportar | Documentos que no siguen ningún molde · todo reconocido |
| Falla a mitad | Interrumpir la traída y comprobar que el origen quedó intacto |
| Caso real | Traer este mismo repositorio, con sus más de cien fases |
| Que NO pase | Que se modifique o se mueva algo dentro del proyecto de origen |

## 11. Criterios de aceptación

- `CA-1` Los documentos que siguen un molde conocido quedan adentro, con su tipo.
- `CA-2` El proyecto de origen queda intacto.
- `CA-3` Traer dos veces no duplica.
- `CA-4` Lo no reconocido queda listado con su ruta.
- `CA-5` Nada se transforma sin que el usuario lo diga.
- `CA-6` Si todo se reconoció, se dice.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Se copia, no se mueve | Mover la documentación a la plataforma | Si algo sale mal, el proyecto se queda sin lo suyo |
| Lo no reconocido se reporta y no se toca | Intentar adivinar su forma | Adivinar mal es peor que no traer: ensucia lo que sí sirve |
| Se muestra qué se va a traer antes de traerlo | Traer y avisar después | Es un cambio de estado, y se aprueba antes |

## 13. Trazabilidad

| Funcionalidad | Requisito | Fase que lo construye |
|---|---|---|
| F-027 | RF-27 | E |
| F-028 | RF-28 | F |

## 14. Cruces con otros módulos

- **Proyectos:** solo se trae a un proyecto ya conectado.
- **Auditoría:** traer queda registrado, con cuántos documentos entraron y cuántos no.
- **Ciclo de vida:** lo traído se convierte en sus épicas, historias y fases, y desde la versión 5 se opera desde la plataforma.
