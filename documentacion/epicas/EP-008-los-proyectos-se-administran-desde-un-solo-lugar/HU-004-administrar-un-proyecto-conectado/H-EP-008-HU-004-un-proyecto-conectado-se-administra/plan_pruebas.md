# Plan de Pruebas — Fase H-EP-008-HU-004: un proyecto conectado se administra   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-H-EP-008-HU-004 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que se pueda deshacer una conexión y corregir lo que se guardó mal, **sin que nada se borre y sin que nada se mueva**.

**No se prueba** corregir la ruta perdida, que es la fase C.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que los tres cambios hagan lo suyo | Sí |
| Integración | Que los cuatro pasen por la auditoría | Sí |
| Interfaz | Que las pantallas pregunten antes | Sí |
| Recuperación | Que rehacer el índice no resucite un desconectado | Sí |
| Aislamiento | Que la carpeta del proyecto no cambie | Sí |

### 3.2 Técnicas

- Comparar la carpeta entera antes y después, archivo por archivo.
- Comprobar lo que **queda**, no solo lo que se rechaza: la documentación después de desconectar.
- Sabotaje: romper el código a propósito, restaurando con copia y no con el control de versiones.
- Proyectos de mentira creados y borrados por la propia prueba.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| `CA-01` desconectar saca el proyecto y deja su documentación | [CP-001](#cp-001--desconectar-saca-el-proyecto-y-su-documentación-se-queda) | ☐ |
| `CA-01` rehacer el índice no lo resucita | [CP-002](#cp-002--rehacer-el-índice-no-resucita-al-desconectado) | ☐ |
| `CA-02` renombrar no mueve la carpeta | [CP-003](#cp-003--renombrar-cambia-el-nombre-y-no-mueve-la-carpeta) | ☐ |
| `CA-03` la versión corregida se vuelve a comprobar | [CP-004](#cp-004--corregir-la-versión-la-vuelve-a-comprobar) | ☐ |
| `CA-04` los cuatro piden confirmación y quedan registrados | [CP-005](#cp-005--los-cuatro-preguntan-antes-y-quedan-registrados) | ☐ |
| Los desconectados se siguen viendo | [CP-006](#cp-006--los-desconectados-se-ven-y-se-ve-que-su-documentación-sigue-ahí) | ☐ |
| Reconectar reactiva al desconectado, con su documentación | [CP-007](#cp-007--reconectar-la-ruta-de-un-desconectado-lo-reactiva) | ☐ |
| `CA-05` · que NO pase: que desconectar toque el proyecto | [CP-008](#cp-008--que-no-pase-que-desconectar-toque-la-carpeta-del-proyecto) | ☐ |

## 5. Los casos

### CP-001 · Desconectar saca el proyecto, y su documentación se queda

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que desconectar sea reversible: saca de la lista y no borra |
| **Cómo se corre** | Se conecta un proyecto, se le guarda algo en su carpeta de documentación, se anota qué tenía, y se desconecta |
| **Resultado esperado** | Deja de aparecer entre los conectados, y su carpeta **sigue con lo mismo que tenía**, no solo existiendo |
| **Si falla** | Si la carpeta existe pero está vacía, se borró algo. Es la falla más grave de esta fase |

**Comprobar que la carpeta existe no basta.** Se compara su contenido, porque una carpeta vacía también existe.

### CP-002 · Rehacer el índice no resucita al desconectado

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la marca de desconectado viva en el texto y no solo en la base |
| **Cómo se corre** | Se desconecta un proyecto, se borra el índice entero y se manda rehacer |
| **Resultado esperado** | Sigue desconectado |
| **Si falla** | La marca quedó solo en la base: es `DA-01` incumplido, y el proyecto vuelve solo cada vez que alguien rehace el índice |

### CP-003 · Renombrar cambia el nombre y no mueve la carpeta

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el identificador y el nombre sigan siendo cosas distintas |
| **Cómo se corre** | Se anota **dónde está** la carpeta de documentación, se renombra el proyecto, y se vuelve a mirar |
| **Resultado esperado** | La lista muestra el nombre nuevo, y la carpeta es exactamente la misma ruta, con lo mismo dentro |
| **Si falla** | Se está recalculando el identificador con el nombre nuevo. Es lo que la fase B guardó aparte justamente para evitar |

### CP-004 · Corregir la versión la vuelve a comprobar

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que corregir no sea una puerta de atrás para meter un número que no existe |
| **Cómo se corre** | Se conecta un proyecto con una versión válida, se le cambia el `CLAUDE.md` a `999.0.0`, y se pide corregir |
| **Resultado esperado** | No se guarda, y se dice que esa versión no existe. La que tenía antes se queda |
| **Si falla** | Es el pendiente 82 entrando por otra puerta |

### CP-005 · Los cuatro preguntan antes, y quedan registrados

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que ningún cambio de estado ocurra sin que el usuario lo confirme |
| **Cómo se corre** | Se pide cada uno de los cuatro (conectar, desconectar, renombrar, corregir) y se mira qué pasa **antes** de confirmar |
| **Resultado esperado** | Nada cambia hasta confirmar. Al confirmar, cada uno deja **un** registro en la auditoría, con quién y cuándo |
| **Si falla** | Si algo cambió antes de confirmar, la pregunta era decorativa |

**La confirmación tiene que decir qué NO va a pasar.** Al desconectar, que la documentación se queda. Sin eso, el usuario no confirma: adivina.

### CP-006 · Los desconectados se ven, y se ve que su documentación sigue ahí

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que desconectar no sea lo mismo que desaparecer |
| **Cómo se corre** | Con un proyecto conectado y otro desconectado, se pide la pantalla |
| **Resultado esperado** | Los dos se ven, separados, y del desconectado se dice cuándo se desconectó y que su documentación sigue guardada |
| **Si falla** | Si desaparece, el usuario no tiene cómo saber que quedó algo suyo, ni cómo llegar a ello |

### CP-007 · Reconectar la ruta de un desconectado lo reactiva

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que desconectar sirva de verdad para corregir un error: conectar mal, desconectar, volver a conectar bien |
| **Cómo se corre** | Se conecta un proyecto, se le guarda documentación, se desconecta, y se vuelve a conectar **la misma carpeta** |
| **Resultado esperado** | Vuelve el **mismo** proyecto: mismo identificador, misma documentación. No aparece uno nuevo, y no hay dos apuntando a esa ruta |
| **Si falla** | Si se crea uno nuevo, la documentación del anterior queda huérfana: una carpeta con cosas adentro que ya no es de nadie |

**Antes de confirmar tiene que avisar.** Si el usuario quería empezar de cero con esa carpeta, va a recibir la historia vieja sin haberla pedido. La pantalla dice que ese proyecto ya estuvo conectado y que tiene documentación guardada.

### CP-008 · Que NO pase: que desconectar toque la carpeta del proyecto

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que desconectar sea, igual que conectar, una anotación de la plataforma |
| **Cómo se corre** | Se anota qué archivos tiene la carpeta del proyecto con su contenido y su fecha, se desconecta, y se compara **archivo por archivo** |
| **Resultado esperado** | Ningún archivo cambió, se creó ni se borró |
| **Si falla** | Desconectar está tocando código ajeno, que es peor que al conectar: acá el usuario cree que está quitando algo |

## 6. Lo que este plan NO puede probar

- **Que reactivar sea siempre lo que el usuario quería.** Se prueba que reactive y que avise antes; si alguien quería empezar de cero con esa carpeta, el aviso se lo dice y la decisión sigue siendo suya.
- **Que la confirmación se entienda.** Se prueba que exista y que detenga el cambio, no que el texto sea claro. Eso lo dice el usuario al usarla.

## 7. Criterios de salida

- Los ocho casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- Las pruebas validadas con sabotaje, restaurando con copia y **corriendo la suite completa al final**.
- Ninguna carpeta real del usuario usada como conejillo.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
