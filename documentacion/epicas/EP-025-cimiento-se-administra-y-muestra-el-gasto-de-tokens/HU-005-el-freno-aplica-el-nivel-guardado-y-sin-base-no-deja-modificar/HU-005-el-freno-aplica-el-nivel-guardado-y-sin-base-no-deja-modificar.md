# HU-005 · El freno aplica el nivel guardado, y sin base no deja modificar


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/enganches/`, `adaptadores/claude-code/`, `proyectos/cimiento/core/herramientas/instalar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must: quinta de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada el 2026-10-05, con sus cuatro criterios probados |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** que el freno aplique el nivel que cada regla tiene en el proyecto
- **Para** que bajar una regla a «avisa» o «apagada» desde la pantalla cambie lo que hace el agente, sin tocar código

---

## 3. Contexto y descripción

El freno (`core/enganches/freno.py`) decide antes y después de cada acción del agente con lo que está en el código; no lee ninguna configuración por proyecto. Desde la HU-004 los niveles quedan en MariaDB ([épica](../epica.md), CAE-01 y CAE-02).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Cuando el freno detiene por una regla, aplica su nivel en el proyecto: frena detiene, avisa deja hacer y avisa, apagada deja hacer sin decir nada | Análisis 1 del pendiente 119, acuerdo 13 |
| RN-02 | Las reglas del núcleo siempre frenan, tengan o no fila | Acuerdo 13 |
| RN-03 | El freno lee la base directo con PyMySQL, sin arrancar Django, con la conexión del `.env` de Cimiento | Acuerdo 15 |
| RN-04 | Sin conexión a la base, no se deja modificar nada; leer y analizar siguen permitidos; el aviso dice que hay que prender MariaDB | Acuerdo 15 |
| RN-05 | Un proyecto que no está registrado, o que está inactivo, tiene todas sus reglas en «frena» | Propuesta del agente: lo de hoy sigue igual |
| RN-06 | La instalación deja PyMySQL donde corren los enganches | Acuerdo 15 |

### 3.2 Supuestos

- Las HU-003 y HU-004 están terminadas: proyectos y niveles están en la base.

### 3.3 Fuera de alcance

- Cambiar qué reglas revisa el freno: sigue revisando las mismas (`02·F8`, `04·S9`, `04·S10`, `00·N1`).

---

## 4. Criterios de aceptación

### CA-01 · El nivel de la regla cambia lo que hace el freno, solo en ese proyecto

**Sale de:** análisis 1 del pendiente 119, punto 14.

```gherkin
Dado un proyecto registrado con 02·F8 en «avisa» y otro con 02·F8 sin cambiar
Cuando el agente escribe un archivo que el plan no declara en cada uno
Entonces en el primero la escritura pasa y el agente recibe el aviso de 02·F8
Y en el segundo el freno la detiene, como hasta hoy
```

**Cómo validarlo:**
1. Correr `python manage.py test core.enganches.tests_freno` → pasan los casos de nivel.
2. Correr `python manage.py test core.niveles.tests_lectura` → el freno lee los niveles guardados en la base.

**Aprobado cuando:** avisa deja pasar con aviso, apagada deja pasar sin aviso y frena detiene, solo en el proyecto del nivel.

### CA-02 · El núcleo siempre frena

**Sale de:** análisis 1 del pendiente 119, punto 14.

```gherkin
Dado una fila de nivel «apagada» para una regla del núcleo puesta a mano en la base
Cuando el freno decide sobre una acción que esa regla detiene
Entonces la detiene
```

**Cómo validarlo:**
1. Correr `python manage.py test core.enganches.tests_freno` → pasa el caso del núcleo.

**Aprobado cuando:** la regla del núcleo frena aunque tenga fila.

### CA-03 · Sin base, no se modifica nada

**Sale de:** análisis 1 del pendiente 119, punto 14.

```gherkin
Dado que MariaDB no responde
Cuando el agente escribe un archivo, aunque el plan lo declare
Entonces el freno lo detiene con el aviso de prender MariaDB
Y una lectura o una orden que no escribe sigue pasando
```

**Cómo validarlo:**
1. Correr `python manage.py test core.enganches.tests_freno` → pasan los casos sin base.

**Aprobado cuando:** escribir se detiene con el aviso y leer pasa.

### CA-04 · La instalación deja PyMySQL

**Sale de:** análisis 1 del pendiente 119, punto 14.

```gherkin
Dado la instalación del estándar en su propia carpeta
Cuando PyMySQL no está en el Python que corre los enganches
Entonces la instalación lo instala
Y si ya está, no hace nada
```

**Cómo validarlo:**
1. Correr `python validadores/instalar.py "«carpeta del estándar»"` → aparece el paso de PyMySQL.
2. Correr las pruebas de `PrepararCimiento` en `tests_instalacion.py` → pasan los casos de PyMySQL.

**Aprobado cuando:** el paso aparece y las pruebas pasan.

### Criterios de aceptación transversales

- [ ] Errores: un fallo previsto da mensaje accionable **sin exponer detalles internos**; el sistema queda consistente, sin datos a medias (`05`, [`00·N3`](../../../../base/00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
- [ ] Rendimiento: responde dentro del umbral acordado con un **volumen realista** (`06`).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Leer los niveles es una conexión y una consulta por acción, sin Django; menos de medio segundo con MariaDB local |
| RNF-02 | **Disponibilidad** | Sin base, el freno no deja modificar (RN-04) |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdos 13 y 15; punto 14.

Modelo de datos afectado: se leen `proyectos_proyecto` y `niveles_nivelderegla`.

---

## 7. Tareas técnicas derivadas

- [ ] Lector de niveles con PyMySQL.
- [ ] El freno aplica el nivel antes y después de actuar; sin base, detiene lo que modifica.
- [ ] Los enganches entregan el aviso de «avisa».
- [ ] La instalación deja PyMySQL.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-005-el-freno-lee-los-niveles` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-005-el-freno-lee-los-niveles/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-005-el-freno-lee-los-niveles/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-005-el-freno-lee-los-niveles/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-004 | Alto |
| Riesgo | MariaDB apagada detiene el trabajo en todos los proyectos de la máquina | Es lo acordado (acuerdo 15); el aviso dice cómo seguir |
| Riesgo | Un error del lector deja al agente sin poder escribir | El enganche que falla deja pasar y lo avisa, como hoy |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
