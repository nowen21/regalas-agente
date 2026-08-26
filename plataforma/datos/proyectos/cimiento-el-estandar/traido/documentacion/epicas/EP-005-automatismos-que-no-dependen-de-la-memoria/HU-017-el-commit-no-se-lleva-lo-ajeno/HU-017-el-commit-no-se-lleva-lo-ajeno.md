# HU-017 — El commit no se lleva el trabajo de otra sesión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-017 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Enganches de git |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En implementación. CA-01, CA-02 y CA-03 cerrados en la fase A |

---

## 2. Narrativa

- **Como** quien trabaja con más de una sesión abierta sobre el mismo repositorio
- **Quiero** que se me avise cuando un commit está mezclando lo que dos sesiones tocaron
- **Para** no publicar trabajo que otra conversación todavía está corrigiendo

---

## 3. Contexto y descripción

Un `git add -A` no distingue de quién es cada archivo. Con dos sesiones abiertas, la que commitea primero se lleva lo que la otra tiene a medio construir, y lo publica.

Pasó el 2026-08-22 en este repositorio: una sesión commiteó un validador con el criterio que reprobaba documentos correctos, un archivo de pruebas sin sus últimos casos y tres carpetas de fase sin llenar. Estuvo ocho minutos publicado. El caso ya estaba escrito como riesgo en el planteamiento del estándar, §8, y esta es la primera vez que se documenta con daño medido.

**La regla que se incumple ya existe** y es del propio `CLAUDE.md`: no hay commit hasta que el usuario lea el cambio y lo apruebe. Lo que falta no es la regla, es que algo la haga cumplir cuando el que commitea ni siquiera sabe que está arrastrando lo ajeno.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo que se comprueba es que el commit **mezcle** dos sesiones, no de quién es el commit: `git` no sabe qué sesión lo lanza |
| RN-02 | Avisa y deja pasar. Retomar lo que otra sesión dejó a medias es legítimo; hacerlo sin darse cuenta, no |
| RN-03 | El aviso nombra al menos un archivo concreto, o no dice qué sacar |
| RN-04 | Una sesión que lleva medio día sin escribir ya no cuenta: su registro no debe hacer ruido mañana |
| RN-05 | El registro de qué tocó cada sesión no se versiona: es estado de trabajo, y versionarlo lo volvería el próximo archivo que dos sesiones se pisan |

### 3.2 Supuestos

- La herramienta le da a los enganches un identificador de sesión. Si algún día no lo diera, no se anota nada y no se rompe nada.

### 3.3 Fuera de alcance

- Impedir el commit. Un enganche que rechaza se apaga en una tarde, y está medido en el [pendiente 11](../../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md).
- Saber qué sesión está viva ahora mismo. Eso exigiría que las sesiones se anunciaran, y no hace falta para lo que se quiere detectar.
- Dos personas en máquinas distintas: eso lo resuelve el repositorio remoto.

---

## 4. Criterios de aceptación

### CA-01 — Un commit que mezcla dos sesiones avisa

```gherkin
Dado que dos sesiones tocaron archivos distintos del mismo repositorio
Cuando se prepara un commit que incluye archivos de las dos
Entonces el enganche avisa, diciendo cuántas sesiones mezcla y cuántos archivos de cada una
Y el commit sigue adelante
```

**Cómo validarlo:**

1. Anotar dos sesiones con archivos distintos.
2. Preparar un commit que incluya archivos de las dos. Resultado esperado: sale un aviso que dice «2 sesiones».
3. Comprobar el código de salida del enganche. Resultado esperado: el commit no se detiene.
- **Aprobado cuando:** el caso del 2026-08-22 habría avisado.

### CA-02 — El aviso dice por dónde empezar

```gherkin
Dado un commit que mezcla dos sesiones
Cuando sale el aviso
Entonces nombra archivos concretos de la sesión ajena
```

**Cómo validarlo:**

1. Preparar el commit mezclado.
2. Leer el aviso. Resultado esperado: aparece el nombre de al menos un archivo que no salió de esta conversación.
- **Aprobado cuando:** quien lo lee sabe qué sacar del commit sin ir a investigar.

### CA-03 — No avisa cuando no hay nada que avisar

```gherkin
Dado un commit de una sola sesión, o vacío, o con archivos ajenos que no entran
Cuando corre el enganche
Entonces no dice nada
```

**Cómo validarlo:**

1. Preparar un commit con archivos de una sola sesión. Resultado esperado: silencio.
2. Preparar un commit vacío. Resultado esperado: silencio.
3. Dejar fuera del commit lo que tocó la otra sesión. Resultado esperado: silencio.
4. Envejecer el registro de una sesión más allá de su vigencia. Resultado esperado: silencio.
- **Aprobado cuando:** el aviso no salta en el commit de todos los días. Un aviso que salta siempre se apaga.

### Criterios de aceptación transversales

- [x] **Límites** — sin identificador de sesión, y con un archivo de otro proyecto, no se anota nada y nada se rompe.
- [x] **No regresión** — el enganche de `pre-commit` sigue rechazando lo que ya rechazaba: secretos, artefactos y marcas nuevas.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Rendimiento | La comprobación corre en cada commit: no puede tardar más de lo que tarda leer unos archivos de texto |
| Robustez | Si anotar falla, el trabajo del agente sigue igual. Lo único que se pierde es el aviso |
| Privacidad | El registro guarda rutas del repositorio, nada más |

---

## 6. Diseño y referencias

- **Documento funcional:** [epica.md](../epica.md).
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno. El registro es un archivo de texto por sesión.

---

## 7. Tareas técnicas derivadas

- [x] Anotar qué archivo toca cada sesión, sea cual sea su extensión.
- [x] Comprobar, sobre lo preparado, si mezcla dos sesiones.
- [x] Colgar la comprobación del `pre-commit` que escribe el instalador, sin cortar el commit.
- [x] Dejar el registro fuera del control de versiones.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones](A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones/plan_trabajo.md) | CA-01, CA-02, CA-03 | Cerrada 2026-08-22 — Cumple. Del [pendiente 80](../../../../pendientes/hecho/dos-sesiones-a-la-vez-no-se-pisan.md) |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | El enganche que se dispara al escribir un archivo, HU-003, que es donde se anota | Alto |
| Riesgo | Que el aviso salte en commits normales y se apague | Se ataca con la vigencia de RN-04, y con que la mitad de las pruebas sean de lo que NO debe avisar |
| Riesgo | Que el registro crezca sin límite | Cada archivo se anota una sola vez por sesión |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

---

## 11. Definition of Done (DoD)

- [x] Los tres CA verificados con evidencia
- [x] Pruebas de la fase en verde
- [x] Trazabilidad escrita en los dos lados
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | No necesita nada más que el enganche de escritura, que ya existe |
| Negociable | Sí | Avisar o rechazar era la decisión, y se tomó con el motivo escrito |
| Valiosa | Sí | Evita publicar trabajo a medias, que ya pasó con daño medido |
| Estimable | Sí | Un módulo, un subcomando y una línea en el enganche |
| Pequeña | Sí | Una fase |
| Testeable | Sí | Diez casos, y la mitad son de lo que no debe avisar |

---

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-22 | Nace del [pendiente 80](../../../../pendientes/hecho/dos-sesiones-a-la-vez-no-se-pisan.md), que a su vez sale del hallazgo H-6 de la sesión de ese día. Se construye y se cierra el mismo día |
