# HU-004 — Generar y poner los automatismos

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Cumplida — los dos CA y los dos transversales verificados el 2026-08-17 |

---

## 2. Narrativa

- **Como** quien instala el estándar en un proyecto
- **Quiero** que los automatismos queden puestos y apuntando bien
- **Para** que las comprobaciones se disparen desde el primer día, sin configurar nada a mano

---

## 3. Contexto y descripción

Los automatismos son lo que convierte una regla escrita en una regla que se cumple. Si hay que ponerlos a mano, en la mitad de los proyectos no se ponen, y las comprobaciones quedan de adorno.

Además tienen una parte que cambia por máquina: dónde vive el estándar. Por eso se generan en el momento de instalar, con la ruta real, en vez de copiarse de un archivo fijo que funcionaría solo en una máquina.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El instalador deja puestos todos los automatismos |
| RN-02 | Se generan con la ruta real de esta máquina, no se copian de un archivo fijo |
| RN-03 | Una versión anterior del mismo automatismo se reemplaza, no se duplica |
| RN-04 | Lo que el proyecto ya tenía configurado por su cuenta se respeta |
| RN-05 | Un automatismo nuevo del estándar llega solo en la siguiente instalación |

### 3.2 Supuestos

- El proyecto puede tener sus propios automatismos, y esos no son del estándar.

### 3.3 Fuera de alcance

- Escribir los automatismos. Eso es EP-005.
- Instalar la herramienta que los ejecuta.

---

## 4. Criterios de aceptación

### CA-01 — Los automatismos quedan puestos y funcionando

```gherkin
Dado que se instala en un proyecto
Cuando termina la instalación
Entonces los automatismos están puestos
Y apuntan al estándar de esta máquina
```

**Cómo validarlo:**

1. Instalar en un proyecto de prueba.
2. Revisar dónde quedaron los automatismos. Resultado esperado: están, y la ruta que traen es la real.
3. Provocar el evento que dispara uno. Resultado esperado: corre.
- **Aprobado cuando:** funcionan sin tocar nada más.

### CA-02 — No se duplican ni se pisa lo del proyecto

```gherkin
Dado que el proyecto ya tenía automatismos propios y una versión anterior de los del estándar
Cuando se instala
Entonces los del estándar se reemplazan por la versión nueva
Y los propios del proyecto quedan intactos
```

**Cómo validarlo:**

1. Dejar en el proyecto un automatismo propio y una versión vieja de uno del estándar.
2. Instalar. Resultado esperado: el del estándar quedó en su versión nueva, una sola vez.
3. Revisar el propio del proyecto. Resultado esperado: sigue igual.
- **Aprobado cuando:** ni se duplica ni se pisa lo ajeno.

### Criterios de aceptación transversales

- [ ] **Límites** — un proyecto con varios repositorios adentro recibe los automatismos en cada uno.
- [ ] **Compatibilidad** — la ruta generada funciona con espacios y tildes.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Portabilidad** | La ruta se genera en el momento, no se asume |
| **Idempotencia** | Instalar de nuevo no duplica |
| **Respeto** | Lo que el proyecto configuró por su cuenta no se toca |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Generar cada automatismo con la ruta real.
- [ ] Reemplazar la versión anterior sin duplicar.
- [ ] Respetar lo que el proyecto ya tenía.
- [ ] Ponerlos en cada repositorio que haya dentro del proyecto.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos](A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos/README.md) | CA-01 y CA-02 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos/resultado_pruebas.md#6-veredicto-de-la-fase) — los dos CA y los dos transversales verificados. Pendiente el commit |

**La fase retro-documenta.** El instalador deja puestos los seis enganches. La prueba que falta es la más importante: que ninguno detenga el trabajo si falla — hoy eso está por diseño y sin comprobar.

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
| Dependencia | EP-005, porque instala los automatismos que esa épica define | Alto |
| Riesgo | Que la ruta generada deje de servir si el estándar se mueve | Se vuelve a generar en la siguiente instalación |
| Riesgo | Que se pise la configuración propia del proyecto | Se respeta lo que ya estaba y solo se reemplaza lo del estándar |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Los automatismos quedan puestos y funcionando
- [ ] No se duplican ni pisan lo del proyecto
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita los automatismos de EP-005 |
| **N**egociable | Sí | Cuáles se instalan se puede discutir |
| **V**aliosa | Sí | Sin esto, las comprobaciones no se disparan |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Generar y poner archivos |
| **T**esteable | Sí | Se prueba instalando sobre un proyecto con configuración propia |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Seis enganches en nueve momentos, sin duplicarse, y ninguno detiene la sesión sobre una carpeta vacía. Queda escrita la tabla de los seis con qué pasa si cada uno falla |
