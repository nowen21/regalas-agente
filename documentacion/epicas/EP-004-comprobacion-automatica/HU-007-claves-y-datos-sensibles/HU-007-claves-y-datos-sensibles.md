# HU-007 — Comprobar que no salgan claves ni datos sensibles

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada — los tres CA y los dos transversales verificados el 2026-08-17 |
---

## 2. Narrativa

- **Como** quien responde por lo que se publica
- **Quiero** que un programa avise antes de guardar una clave, un archivo de configuración local o un dato sensible
- **Para** que no se filtre algo que después ya no se puede retirar

---

## 3. Contexto y descripción

Una clave guardada en el historial no se borra borrándola después: queda en el historial. Un archivo de configuración con datos de la máquina de alguien tampoco debería viajar. Y un dato sensible escrito en un registro se queda ahí para siempre.

Son de las pocas fallas que no se pueden arreglar más tarde, y por eso conviene atajarlas antes de guardar, no después.

Todo esto se responde con un sí o un no: el archivo tiene forma de clave o no, el nombre está en la lista de lo que no se guarda o no está, la llamada al registro incluye algo que parece una clave o no.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | No se guarda un archivo de claves, un artefacto generado ni la configuración local de una máquina |
| RN-02 | No se escribe una clave dentro del código |
| RN-03 | No se manda una clave a un registro de eventos |
| RN-04 | Lo dudoso sale como aviso: un texto que parece una clave puede ser un ejemplo |
| RN-05 | La comprobación mira lo que va a quedar guardado, no solo lo que está suelto en la carpeta |

### 3.2 Supuestos

- Las claves de verdad tienen forma reconocible. Lo que no la tiene, un programa no lo va a distinguir de un texto cualquiera.

### 3.3 Fuera de alcance

- Quitar la clave del historial una vez guardada. Eso es una operación de rescate, no una comprobación.
- Decidir si un dato es personal. Eso es criterio y depende del marco normativo del proyecto.

---

## 4. Criterios de aceptación

### CA-01 — Una clave escrita en el código se reporta

```gherkin
Dado que un archivo de código trae una clave escrita
Cuando se corre la comprobación
Entonces la reporta con su archivo y su línea
Y no muestra la clave entera en el mensaje
```

**Cómo validarlo:**

1. Escribir en un archivo de prueba una asignación con una clave de forma reconocible.
2. Correr la comprobación. Resultado esperado: la reporta con archivo y línea.
3. Leer el mensaje. Resultado esperado: no repite la clave completa.
- **Aprobado cuando:** el hallazgo permite ubicarla sin volver a exponerla.

### CA-02 — Un archivo que no debe guardarse se reporta

```gherkin
Dado que se va a guardar un archivo de configuración local o de claves
Cuando se corre la comprobación sobre lo que va a quedar guardado
Entonces lo reporta antes de que quede en el historial
```

**Cómo validarlo:**

1. Preparar para guardar un archivo con nombre de configuración local.
2. Correr la comprobación sobre lo que va a quedar guardado. Resultado esperado: lo reporta y dice por qué no debe guardarse.
3. Sacarlo y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el archivo se detecta antes de quedar guardado.

### CA-03 — Un ejemplo no se confunde con una clave

```gherkin
Dado que un documento del estándar muestra un ejemplo con forma de clave
Cuando se corre la comprobación
Entonces no lo reporta como falla
```

**Cómo validarlo:**

1. Ubicar en la documentación un ejemplo que muestre cómo NO se escribe una clave.
2. Correr la comprobación sobre la documentación. Resultado esperado: no sale como falla.
3. Revisar si sale como aviso. Resultado esperado: si sale, el mensaje deja claro que puede ser un ejemplo.
- **Aprobado cuando:** el ejemplo no rompe la corrida.

### Criterios de aceptación transversales

- [ ] **Privacidad** — el hallazgo no reproduce el secreto encontrado.
- [ ] **Límites** — un archivo binario, uno enorme y uno sin permisos de lectura tienen comportamiento definido.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Seguridad** | El mensaje no reproduce el secreto |
| **Rendimiento** | La comprobación de lo que va a guardarse no demora tanto como para que se salte |
| **Determinismo** | El mismo insumo da el mismo resultado |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Reconocer las formas de clave más comunes sin listar productos concretos en la regla.
- [ ] Comprobar los nombres de archivo que no deben guardarse.
- [ ] Comprobar las llamadas al registro de eventos.
- [ ] Comprobar solo lo que va a quedar guardado, cuando así se pida.
- [ ] Escribir pruebas donde los ejemplos se arman al vuelo, para no dejar una clave de forma real dentro de las pruebas.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos](A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos/resultado_pruebas.md#6-veredicto-de-la-fase) — los tres CA y los dos transversales verificados. Pendiente el commit |

**La fase retro-documenta.** Los dos programas existen y corren. Lo que la fase pone en primer plano es el CA-03: que un ejemplo no se confunda con una clave — un detector con falsos positivos se apaga, y entonces no detecta nada.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-003, porque los hallazgos salen con la forma ya definida | Alto |
| Riesgo | Que marque tantos falsos positivos que se apague | Lo dudoso es aviso; solo lo inequívoco detiene |
| Riesgo | Que las propias pruebas dejen una clave de forma real guardada | Los ejemplos de prueba se arman al vuelo, nunca escritos completos |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Se detectan claves en el código, archivos que no deben guardarse y claves en el registro
- [ ] Ningún mensaje reproduce el secreto
- [ ] Los ejemplos de la documentación no rompen la corrida
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la forma del hallazgo de HU-003 |
| **N**egociable | Sí | Qué formas se reconocen se puede ampliar |
| **V**aliosa | Sí | Evita la falla que no se puede deshacer |
| **E**stimable | Sí | Alcance acotado a formas conocidas |
| **S**mall (pequeña) | Sí | Tres comprobaciones parecidas |
| **T**esteable | Sí | Se prueba con casos armados a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Los tres CA verificados y los dos transversales también: el hallazgo no reproduce el secreto, y los tres bordes de archivo no rompen la corrida. Queda escrito qué cuenta como ejemplo y qué como clave |
