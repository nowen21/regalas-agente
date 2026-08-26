# HU-001 — Instalar todo con una sola línea

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-007 Instalación y actualización](../epica.md) |
| **Módulo / Componente** | Instalador |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien va a usar el estándar en un proyecto nuevo
- **Quiero** dejarlo listo con una sola línea
- **Para** empezar a trabajar hoy y no perder la mañana en pasos manuales

---

## 3. Contexto y descripción

Lo que exige configurarse a mano no se configura. Y si se configura, sale distinto en cada proyecto, que es peor: nadie puede decir qué tiene puesto cada uno.

Una sola línea deja el proyecto listo: las carpetas, los documentos que hereda, los automatismos y el registro. Sin preguntas que el estándar ya tenga decididas.

Y termina comprobando: instalar y verificar son el mismo paso, porque declarar completo lo que nadie miró es la forma más común de tener una instalación a medias.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Una sola línea deja el proyecto listo y operativo |
| RN-02 | No se pregunta lo que el estándar ya tiene decidido |
| RN-03 | Correrla dos veces no duplica ni rompe nada |
| RN-04 | Al terminar, comprueba y dice qué quedó fuera |
| RN-05 | Lo que es decisión del usuario no lo toma el instalador |

### 3.2 Supuestos

- La máquina tiene lo mínimo para correr el instalador, y nada más.

### 3.3 Fuera de alcance

- Instalar la herramienta con la que se conversa con la IA.
- Decidir qué código va dentro del proyecto.

---

## 4. Criterios de aceptación

### CA-01 — Una línea deja el proyecto listo

```gherkin
Dado que hay un proyecto sin nada del estándar
Cuando se corre la línea de instalación
Entonces el proyecto queda con todo lo que debe tener
Y al terminar se dice qué quedó puesto
```

**Cómo validarlo:**

1. Tomar una carpeta de proyecto sin nada instalado.
2. Correr la línea de instalación. Resultado esperado: termina sola, sin preguntar.
3. Revisar el proyecto. Resultado esperado: están las carpetas, los documentos heredados y los automatismos.
- **Aprobado cuando:** no hizo falta ningún paso manual.

### CA-02 — Correrla dos veces no rompe nada

```gherkin
Dado que el proyecto ya está instalado
Cuando se corre la línea otra vez
Entonces no se duplica ni se pisa nada
```

**Cómo validarlo:**

1. Correr la instalación sobre un proyecto ya instalado.
2. Comparar el antes y el después. Resultado esperado: lo que ya estaba al día no cambió.
3. Revisar si algo quedó duplicado. Resultado esperado: nada.
- **Aprobado cuando:** repetir es seguro.

### CA-03 — Al terminar dice qué quedó fuera

```gherkin
Dado que la instalación termina
Cuando algo no se pudo dejar puesto
Entonces se dice cuál y por qué
```

**Cómo validarlo:**

1. Provocar que un componente no se pueda instalar.
2. Correr la instalación. Resultado esperado: termina y nombra lo que faltó, con el motivo.
3. Arreglar la causa y correr otra vez. Resultado esperado: ya no lo nombra.
- **Aprobado cuando:** nunca se declara completo lo que no se miró.

### Criterios de aceptación transversales

- [ ] **Límites** — una carpeta que no es un proyecto, y un proyecto a medio instalar, tienen comportamiento definido.
- [ ] **Errores** — un fallo dice qué pasó y qué hacer, sin dejar el proyecto a medias.
- [ ] **Compatibilidad** — funciona sin internet y en rutas con espacios y tildes.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Autonomía** | Sin internet y sin dependencias que haya que instalar antes |
| **Idempotencia** | Correrla de nuevo no cambia lo que ya está al día |
| **Compatibilidad** | Rutas con espacios y tildes |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es una línea de terminal.
- **Documento funcional:** [documentacion/epicas/EP-007-instalacion-y-actualizacion/epica.md](../epica.md), criterio CAE-01.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el instalador con una sola entrada.
- [ ] Hacer que cada paso sea repetible sin efectos.
- [ ] Comprobar al terminar y reportar lo que faltó.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| [`A-EP-007-HU-001-rellenar-los-marcadores-al-copiar`](A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/) | CA-01, CA-02 | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md](A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_trabajo.md) | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_pruebas.md](A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/plan_pruebas.md) | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/resultado_pruebas.md](A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/resultado_pruebas.md) · **Cumple** | Cerrada |
| [`B-EP-007-HU-001-prepara-su-propia-salida`](B-EP-007-HU-001-prepara-su-propia-salida/) | CA-01 | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/plan_trabajo.md](B-EP-007-HU-001-prepara-su-propia-salida/plan_trabajo.md) | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/plan_pruebas.md](B-EP-007-HU-001-prepara-su-propia-salida/plan_pruebas.md) | [documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/resultado_pruebas.md](B-EP-007-HU-001-prepara-su-propia-salida/resultado_pruebas.md) · **Cumple** | Cerrada |

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
| Dependencia | EP-003 y EP-005, porque instala los modelos y los automatismos | Alto |
| Riesgo | Que la instalación pise algo del proyecto | No pisar lo escrito es una historia propia, HU-005 |
| Riesgo | Que falle a medias y deje el proyecto inservible | Cada paso es repetible y se reporta lo que faltó |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Una línea deja el proyecto operativo
- [ ] Correrla dos veces es seguro
- [ ] Al terminar comprueba y reporta
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Instala lo que producen las otras épicas |
| **N**egociable | Sí | Qué instala se puede discutir |
| **V**aliosa | Sí | Sin esto, nada de lo anterior llega a un proyecto |
| **E**stimable | Sí | El alcance lo fija la lista de componentes |
| **S**mall (pequeña) | Parcial | Son varios componentes |
| **T**esteable | Sí | Se prueba instalando en una carpeta vacía |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
