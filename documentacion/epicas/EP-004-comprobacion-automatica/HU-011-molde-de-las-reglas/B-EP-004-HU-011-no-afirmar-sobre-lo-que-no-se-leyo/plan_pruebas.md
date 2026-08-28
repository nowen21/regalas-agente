# Plan de Pruebas — Fase `B-EP-004-HU-011-no-afirmar-sobre-lo-que-no-se-leyo`   ·   `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó y se cerró el 2026-08-22 y **este documento se quedó siendo la plantilla en blanco**: 363 líneas de molde con 36 marcadores sin reemplazar. Lo destapó la [HU-022](../../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md).
>
> **No se inventa nada.** Los casos salen del [resultado_pruebas.md](resultado_pruebas.md), que sí se escribió y documenta qué entró y qué salió en cada uno, y de las 10 pruebas que quedaron en el repositorio. **Lo que no se puede reconstruir —qué se pensó antes de ejecutar— no se escribe.**

---

## 1. Propósito y alcance

Comprobar que la comprobación de meta-reglas **no afirma sobre lo que no leyó** (`04·R4`).

Apuntarla a un proyecto corría las reglas del estándar contra una carpeta que **no tiene cuerpo de reglas**. Buscaba cuatro archivos que un proyecto no tiene, no los encontraba, y **reportaba igual**: una falla y cuatro avisos, los cinco falsos. Y la falla decía `«VERSION dice  y el CHANGELOG»`, **con el hueco donde iba el dato que no pudo leer**.

**Entra:** reconocer si la carpeta es el estándar por lo que solo el estándar tiene; decirlo en una línea y nombrar la bandera correcta si no lo es; y que la comprobación de la versión **calle cuando no pudo leer su archivo**.

**No entra:** los demás subcomandos. `--raiz` significa «el proyecto» en casi todos, y si el mismo problema aparece en otro sale como pendiente aparte.

---

## 2. Estrategia

**Unitario** sobre carpetas de mentira en tres estados —el estándar, un proyecto, y una instalación a medias— y **de sistema** sobre dos repositorios reales: `AgroSystem` y el estándar mismo.

**Casi todos los casos son de lo que NO debe pasar.** Es el tema de la fase: el defecto no era callar de menos, era **hablar de más**.

---

## 3. Casos de prueba

| Caso | Qué entra | Qué debe salir |
|---|---|---|
| **CP-001** · apuntar a un proyecto | una carpeta con `.agente/` | **Ninguna falla**, y un aviso que nombra la bandera buena |
| **CP-002** · el estándar se reconoce | tiene cuerpo de reglas y versión | Sí |
| **CP-003** · cuerpo de reglas pero sin versión | instalación a medias | **No es el estándar** |
| **CP-004** · sobre el estándar sigue comprobando | el repositorio real | Igual que antes, **sin el aviso de carpeta ajena** |
| **CP-005** · sin los archivos no se reporta nada | carpeta vacía | **Silencio** |
| **CP-006** · con los archivos sigue comprobando | versión sin su entrada | Falla, **y con el dato en el mensaje** |

**El `CP-004` es el que impide que el arreglo se pase de largo.** Enseñar a callar es fácil; lo difícil es que **siga hablando donde debe**. Sin ese caso, una comprobación que no reporta nunca pasaría en verde.

**El `CP-006` cierra el otro extremo:** el mensaje con el hueco venía de reportar sin el dato. Ahora, o hay dato y se dice, o no se reporta.

**El `CP-003` es el borde real:** una instalación a medias tiene una mitad de las señas del estándar. Tratarla como estándar devuelve los falsos de antes.

---

## 4. Criterio de aprobación

- Los seis casos, ejecutados.
- **Corrido sobre dos repositorios reales**, uno que es el estándar y otro que no.
- Que `--catalogo` **siga encontrando lo que sí servía**.
- La suite en verde.

---

## 5. Qué se ejecutó, y con qué resultado

Está en el [resultado_pruebas.md](resultado_pruebas.md). En corto: sobre `AgroSystem`, apuntar con `--raiz` pasó de **una falla y cuatro avisos falsos** a **un aviso que dice qué usar en su lugar**. Sobre el estándar sigue comprobando igual, sin incumplimientos. Y `--catalogo` sigue encontrando las **56 reglas propias sin respaldo**, que era lo que sí servía. Las suites `test_metareglas_no_afirma_sobre_un_proyecto` (7) y `test_checklist_cadena` (3) quedaron en verde.

---

## 6. Herramientas y datos

`unittest`, y dos repositorios reales sin modificar: `AgroSystem` y el estándar. **Ninguna prueba usa credenciales** (`00·N6`).

---

## 7. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | **Retrodocumentado.** La fase cerró el 2026-08-22 sin este documento |
