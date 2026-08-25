# Especificación del módulo Proyectos  ·  `[CAPA 3]`

- **Slug del módulo:** `proyectos`
- **Estado:** aprobada, el 2026-08-25 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 1, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Guardar qué proyectos administra la plataforma, dónde vive el código de cada uno, y mostrar en qué va cada uno sin tener que entrar a su carpeta.

- **Dentro de alcance:** registrar un proyecto con su nombre y su ruta (`F-001`), avisar cuando esa ruta deja de existir (`F-002`), y mostrar el estado de un proyecto (`F-003`).
- **Fuera de alcance:** tocar el código del proyecto, configurar qué reglas rigen en él (`F-004`, versión 5), y traer su documentación, que es del módulo Importación.

## 2. Contexto — qué hay hoy

Módulo nuevo, no hay código previo. Lo que existe en este repositorio es documentación de un proyecto, no una plataforma: **el propio repositorio será el primer proyecto que se conecte**, y esa es la prueba real de este módulo.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que basta con guardar la ruta del código para saber dónde está el proyecto; que el estado se puede calcular leyendo lo que la plataforma guarda, sin abrir la carpeta del proyecto.
- **Dependencias:** ninguna. Es el primer módulo, y de él dependen Importación y Auditoría.
- **Preguntas abiertas:** ninguna que detenga. Si un proyecto se mueve seguido, habrá que decidir si la ruta se corrige sola; hoy se avisa y la corrige el usuario.

## 4. Reglas de negocio

1. **Registrar un proyecto no toca su código.** Baja de `RN-2` del análisis: ningún cambio de estado sin aprobación, y el código del proyecto no es de la plataforma.
2. **La ruta viva y el estado se calculan, no se guardan.** Baja de la sección 3 del [modelo de datos](../../cvds/diseno/modelo-de-datos.md): un dato guardado que también se puede calcular es una segunda verdad que envejece.
3. **La versión de reglas que declara un proyecto debe existir.** Baja de `F-006` y del riesgo conocido: un número inventado mayor que el real apagaría el aviso de desfase en vez de dispararlo.
4. **Perder la ruta no borra nada.** Baja de la ficha `F-002`: la documentación vive en la plataforma, no en el proyecto.

## 5. Modelo de datos

- **Entidades:** `Proyecto`, con los campos de la sección 3 del [modelo de datos](../../cvds/diseno/modelo-de-datos.md): nombre, ruta del código, versión de reglas adoptada, fecha de conexión. Y dos calculados que no se guardan: ruta viva y estado.
- **Dónde vive:** el texto en la carpeta del proyecto dentro del repositorio de la plataforma; el índice en la base local, reconstruible.
- **Valores configurables:** ninguno en esta versión.
- **Migración:** no aplica, no hay datos previos.

## 6. Comportamiento y flujos

**Conectar un proyecto.** Se recibe nombre y ruta. Se comprueba que la ruta exista y que no esté ya registrada. Se crea la carpeta del proyecto en la plataforma y se guarda el registro. Se anota la acción en la auditoría.

- Ruta que no existe: no se registra, y se responde con la ruta que se buscó.
- Ruta ya registrada: se responde con qué proyecto la tiene.
- Carpeta sin control de versiones: se registra, y se advierte que su código no tiene respaldo.

**Detectar la ruta perdida.** Al listar proyectos se comprueba si cada ruta existe. La que no, se marca y se avisa; su documentación se sigue mostrando igual. Volver a apuntar la ruta quita el aviso.

**Ver el estado.** Se lee lo que la plataforma guardó de ese proyecto y se responde: qué etapas tienen documento, qué fases están abiertas y qué falta aprobar. Un proyecto sin nada escrito responde «sin empezar», que es un dato, no una pantalla vacía.

## 7. Interfaz

Pantallas `P-01` Inicio y `P-02` Un proyecto, del [diseño de interfaz](../../cvds/diseno/diseno-de-interfaz.md). Conectar y desconectar piden confirmación; desconectar no borra la documentación del proyecto.

## 8. Permisos y autorización

Un solo usuario, sin credenciales propias: quien tenga la máquina, entra. Es lo declarado en la sección 8 del [diseño](../../cvds/diseno/README.md), y se rehace el día que la plataforma corra en un servidor.

## 9. Marco normativo

No aplica: el módulo no guarda datos de personas ni información regulada.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Conectar | Ruta válida · ruta que no existe · ruta ya registrada · carpeta sin control de versiones |
| Ruta perdida | Ruta que se borra después de registrada · ruta que se vuelve a apuntar |
| Estado | Proyecto sin nada escrito · proyecto con documentos · proyecto con ruta perdida |
| Rendimiento | Listar cincuenta proyectos en menos de un segundo (`RNF-02`) |
| Que NO pase | Que registrar toque algo dentro de la carpeta del proyecto |

## 11. Criterios de aceptación

- `CA-1` Un proyecto queda registrado y aparece en la lista.
- `CA-2` Una ruta que no existe no se registra, y se dice por qué.
- `CA-3` Registrar dos veces la misma ruta avisa cuál proyecto ya la tiene.
- `CA-4` Una ruta que dejó de existir queda avisada, y su documentación se sigue viendo.
- `CA-5` El estado se ve sin abrir la carpeta del proyecto.
- `CA-6` Un proyecto sin trabajo abierto lo dice, y no muestra una pantalla vacía.
- `CA-7` Listar cincuenta proyectos responde en menos de un segundo.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Se guarda la ruta, no una copia del código | Copiar el código a la plataforma | La plataforma administra documentación, no código |
| El estado se calcula al pedirlo, y se guarda solo como índice | Guardarlo y actualizarlo en cada cambio | Un estado guardado a mano envejece y miente |
| Desconectar no borra la documentación | Borrarla al desconectar | Desconectar es reversible; borrar no |

## 13. Trazabilidad

| Funcionalidad | Requisito | Fase que lo construye |
|---|---|---|
| F-001 | RF-01 | B, y su base en A |
| F-002 | RF-02 | C |
| F-003 | RF-03 | G |

## 14. Cruces con otros módulos

- **Auditoría:** toda acción de este módulo se registra allá.
- **Importación:** trae la documentación de un proyecto ya conectado.
- **Reglas:** cada proyecto declara qué versión adoptó; ese campo se usa desde la versión 3.
