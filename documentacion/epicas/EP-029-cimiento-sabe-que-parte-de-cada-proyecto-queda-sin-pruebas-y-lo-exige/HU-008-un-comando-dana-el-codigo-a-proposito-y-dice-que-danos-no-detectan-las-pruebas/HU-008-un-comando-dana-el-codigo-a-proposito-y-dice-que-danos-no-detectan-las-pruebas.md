# HU-008 · Un comando de Cimiento daña el código a propósito y dice qué daños no detectan las pruebas

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/pruebas/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja en cualquier proyecto que hereda de Cimiento
- **Quiero** dañar el código a propósito con un solo comando y ver qué daños no detectan las pruebas
- **Para** saber si las pruebas sirven, sin escribir un guion cada vez y sin riesgo de dejar el código dañado

---

## 3. Contexto y descripción

Para saber si una prueba detecta un error, se daña el código a propósito y se mira si la prueba falla. Cada vez se escribía un guion nuevo: hay 19 en `historico-chat/scripts/`, del 2026-08-25 al 2026-08-28, y desde entonces no se volvió a hacer. Sale del [análisis 1 del pendiente 148](../../../../historico-chat/resumenes/2026-10-08/pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/analisis-1.md), acuerdos 1 y 2, punto 1 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El comando recibe un archivo con la lista de daños (nombre, archivo, texto original, texto dañado) y la orden que corre las pruebas |
| RN-02 | Antes de dañar, las pruebas tienen que pasar sin daños; si no pasan, no se daña nada |
| RN-03 | Un daño cuyo texto original no aparece exactamente una vez en su archivo no se aplica, y se reporta así |
| RN-04 | Por cada daño: copia el archivo, lo daña, corre las pruebas, lo devuelve desde la copia aunque algo falle, y borra los archivos que aparecieron con el daño |
| RN-05 | Las pruebas detectan el daño si la orden termina con error o se pasa del tiempo |
| RN-06 | Al final corre las pruebas sin daños y comprueba que cada archivo dañado quedó igual a su copia |
| RN-07 | No depende del lenguaje del proyecto: cambia texto y corre la orden que se le da |

### 3.2 Supuestos

- La orden de pruebas devuelve un código distinto de cero cuando alguna falla, como hacen `unittest`, `pytest`, `phpunit` y `ng test`.

### 3.3 Fuera de alcance

- Generar los daños solo: la lista la escribe quien prueba.
- Una pantalla para el comando.

---

## 4. Criterios de aceptación

### CA-01 · Dice qué daños detectan las pruebas y cuáles no

**Sale de:** análisis 1 del pendiente 148, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto cuyas pruebas pasan, y dos daños: uno que una prueba detecta y otro que ninguna detecta
Cuando se corre danar_a_proposito
Entonces la tabla dice que el primero se detectó y el segundo no
Y un daño cuyo texto no aparece en el archivo sale como «no se aplicó»
```

**Cómo validarlo:** correr `manage.py test core.pruebas.tests_danar` → resultado esperado: los casos pasan.

### CA-02 · El código queda como estaba, pase lo que pase

**Sale de:** punto 1

```gherkin
Dado un daño que hace que las pruebas escriban un archivo nuevo, o que se cuelguen
Cuando termina el comando, o se cae a mitad de un daño
Entonces cada archivo dañado es igual a su copia
Y el archivo nuevo ya no está
Y las pruebas sin daños vuelven a pasar
```

**Cómo validarlo:** correr `manage.py test core.pruebas.tests_danar` → resultado esperado: los casos pasan.

### CA-03 · Sin pruebas que pasen no daña nada

**Sale de:** punto 1

```gherkin
Dado un proyecto cuyas pruebas fallan sin daños
Cuando se corre danar_a_proposito
Entonces no se toca ningún archivo
Y dice que primero hay que arreglar las pruebas
```

**Cómo validarlo:** correr `manage.py test core.pruebas.tests_danar` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Escribe bien en la consola de Windows |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 148](../../../../historico-chat/resumenes/2026-10-08/pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] La lógica de dañar, correr y devolver.
- [x] El comando.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-008-danar-a-proposito` |  | (vacío) | [plan_trabajo.md](A-EP-029-HU-008-danar-a-proposito/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-008-danar-a-proposito/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-008-danar-a-proposito/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Dejar el código dañado | Se cubre con el CA-02 |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Se sabe si las pruebas sirven |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django sobre un proyecto de juguete en una carpeta temporal |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 148 |
