# Resultado de pruebas — Fase A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos` |
| **HU** | [HU-007](../HU-007-claves-y-datos-sensibles.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-004-HU-007 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Repositorios de mentira en carpetas temporales. Estándar 23.2.1 |

**Ninguna clave real, en ningún momento** ([`00·N4`](../../../../../base/00-nucleo-blindado.md) · [`08·T4`](../../../../../base/08-pruebas.md)). Y ninguna cadena con forma de credencial quedó escrita entera en el repositorio: se arman en tiempo de ejecución, porque el escaneo de GitHub bloquea el envío si ve una con forma real aunque sea de mentira — ya pasó, y por eso existe el recuerdo [Fixtures sin secretos literales](../../../../../historico-chat/memory/fixtures-sin-secretos-literales.md).

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Los tres criterios se comprueban y se probaron; los dos transversales también, incluido el de privacidad —**el hallazgo no reproduce el secreto que encontró**— y los tres bordes de archivo.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--la-clave-armada-se-reporta-con-archivo-y-línea) | CA-01 | Crítica | Una clave con forma de AWS, armada en tiempo de ejecución | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md#cp-002--el-archivo-de-configuración-con-secretos-se-reporta-al-versionarlo) | CA-02 | Crítica | Un `.env` forzado a versionar en un repositorio temporal | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md#cp-003--el-ejemplo-y-el-dato-de-prueba-no-se-reportan) | CA-03 | Alta | Siete moldes y tres formas de leer del entorno | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md#cp-004--la-lista-de-lo-que-cuenta-como-ejemplo-sale-del-programa) | CA-03 | Alta | Las dos expresiones de `secretos.py`, leídas del programa | Aprobado | EV-02 |

---

### Detalle de CP-001 — La clave armada se reporta, con archivo y línea

| # | Qué se comprobó | Qué salió |
|---|---|---|
| 1 | Que se reporte | **Un** hallazgo, no dos |
| 2 | Que diga el archivo | `config/ajustes.py` |
| 3 | Que diga la línea | **3**, que es donde estaba |
| 4 | Con qué severidad | **Falla** — un secreto con forma reconocible detiene |

**Tres formatos probados y detectados**, entre esta fase y los casos que ya existían: clave de AWS, bloque de clave privada y tokens de proveedor. La métrica del plan pedía al menos tres.

---

### Detalle de CP-002 — El archivo de configuración se reporta al versionarlo

Se creó un repositorio temporal, se escribió un `.env` con una contraseña y se forzó su versionado. **Se reporta.**

**Quién lo reporta no es `secretos.py` sino `versionado.py`**, y la separación tiene sentido: uno mira **el contenido** de lo versionado y el otro **qué archivos** están versionados. Un `.env` es un problema aunque su contenido sea inocuo, porque mañana no lo será.

---

### Detalle de CP-003 — El ejemplo y el dato de prueba no se reportan

**Siete moldes, ninguno reportado:** `changeme`, `your-api-key`, `tu_clave_aqui`, `<TU_CLAVE>`, `placeholder`, `xxxxxxxx`, `ejemplo-de-token`.

**Tres formas de leer del entorno, ninguna reportada:** `os.environ[…]`, `process.env…`, `config(…)`.

**El segundo grupo importa más que el primero.** Marcar una línea que lee del entorno enseñaría exactamente lo contrario de lo que la regla pide: leer del entorno **es** la forma correcta, y un validador que la reporta empuja a esconderla.

**Y los `.md` quedan fuera a propósito:** la documentación muestra secretos de ejemplo porque para eso es documentación. Reportarlos obligaría a escribirla torcida, que es la salida mala que ya está descrita en el [pendiente 55](../../../../../pendientes/55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) para otro validador.

---

### Detalle de CP-004 — La lista de lo que cuenta como ejemplo sale del programa

**Estaba en dos expresiones regulares de `secretos.py` y en ningún documento**, así que nadie podía saber qué escribir para no disparar un falso positivo. Se leyó del programa y quedó escrita en [`validadores/docs/secretos.md`](../../../../../validadores/docs/secretos.md):

| Grupo | Cuántos | Cómo se reconoce |
|---|---:|---|
| El valor **entero** es un molde | 15 formas | `changeme`, `placeholder`, `dummy`, `sample`, `example`, `ejemplo`, `null`, `none`, `password`, `secret`, `test`, `123456`, `abc123`, `xxx…`/`…`/`***`, y cualquier cosa entre `<` y `>` |
| El valor **empieza** como molde | 9 prefijos | `your`, `tu`, `my`, `mi`, `example`, `ejemplo`, `placeholder`, `sample`, `dummy`, `test` |
| La línea **lee del entorno** | 6 formas | `env`, `getenv`, `os.environ`, `process.env`, `config(`, `${` |

Y con eso quedó escrito **cómo escribir un ejemplo que no dispare nada**, que es lo que le faltaba a quien redacta documentación o pruebas.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el hallazgo no reproduzca el secreto | Buscando el valor dentro del mensaje | **No aparece**, ni en la falla ni en el aviso |
| 2 | Que el aviso nombre la clave y no su valor | Leyendo el mensaje | Dice `password`; no dice el valor |
| 3 | Los tres bordes de archivo | Binario, uno de ~2 MB y uno ilegible, todos versionados | **Ninguno rompe**, y el archivo normal del mismo repositorio se sigue revisando |
| 4 | Falsos positivos en este repositorio | `validar.py secretos` | **0** |
| 5 | Que la suite siga verde | `python validadores/pruebas.py` | 289 pruebas · verde, con 5 fallos esperados |

**El punto 3 es el que de verdad prueba los bordes.** Que un binario no reviente no sirve de nada si se lleva por delante el resto de la corrida: por eso el caso comprueba que, con los tres archivos raros presentes, el archivo normal **se sigue reportando**.

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | **Qué cuenta como ejemplo y qué como clave estaba solo en dos expresiones del código.** Nadie podía saber qué escribir para no disparar un falso positivo | **Corregido en esta fase**: escrito en [`validadores/docs/secretos.md`](../../../../../validadores/docs/secretos.md), que §2.1 del plan declara |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

**Ninguno deja un criterio de aceptación en «No».**

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-007-claves-y-datos-sensibles.md#ca-01--una-clave-escrita-en-el-código-se-reporta) | CP-001 | Un hallazgo, con archivo, línea y severidad de falla. Tres formatos probados | Sí |
| [CA-02](../HU-007-claves-y-datos-sensibles.md#ca-02--un-archivo-que-no-debe-guardarse-se-reporta) | CP-002 | Un `.env` versionado se reporta, por `versionado.py` | Sí |
| [CA-03](../HU-007-claves-y-datos-sensibles.md#ca-03--un-ejemplo-no-se-confunde-con-una-clave) | CP-003, CP-004 | Siete moldes y tres formas de leer del entorno, ninguno reportado. Y la lista quedó escrita | Sí |
| Transversal · Privacidad | Verificaciones 1 y 2 | **El hallazgo no reproduce el secreto.** Dice archivo, línea, motivo y el nombre de la clave, nunca su valor | Sí |
| Transversal · Límites | Verificación 3 | Binario, enorme y sin permisos: ninguno rompe, y no se llevan el resto de la corrida | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| **Claves reales usadas** | **0** | **0** | Sí |
| Cadenas de prueba que quedaron en el repositorio | **0** | **0** — todas se arman en tiempo de ejecución | Sí |
| Falsos positivos en el repositorio | Todos anotados | **0** que anotar | Sí |
| Formatos de credencial probados | Al menos 3, todos detectados | **3**, los tres detectados | Sí |
| Pruebas de la suite | Línea base + las nuevas, en verde | Línea base + **8**, en verde | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los tres criterios de aceptación quedaron verificados, y los dos transversales que el plan no cubrió también. El de privacidad es el que más importaba y el que nadie había comprobado: **un informe que copiara el secreto encontrado sería una segunda filtración**, y encima en un archivo que se versiona. No lo copia. Y quedó escrito, por primera vez, qué cuenta como ejemplo y qué como clave — lo que le faltaba a quien redacta documentación o pruebas para no disparar falsos positivos.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clases `ClavesYDatosSensibles` (8 pruebas nuevas) y `Secretos` (8, ya existentes) |
| EV-02 | Qué cuenta como ejemplo | [`validadores/docs/secretos.md`](../../../../../validadores/docs/secretos.md), sección escrita en esta fase |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 289 pruebas, verde, 5 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
