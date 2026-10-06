# HU-013 · Cada proyecto tiene su configuración en tres capas


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-013 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/proyectos/`, `proyectos/cimiento/core/enganches/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** administrador de Cimiento
- **Quiero** una configuración base para todos los proyectos, la de cada proyecto encima, y poder suspender un rato una regla o el freno con su motivo
- **Para** ajustar cada proyecto y salir de un bloqueo sin tocar archivos ni código

---

## 3. Contexto y descripción

Los límites de tokens vivían como columnas del proyecto, sin valor común; no había dónde decir cómo se muestran las rutas; y ante un bloqueo del freno la única salida era tocar archivos a mano ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 3, puntos 5 y 6; [análisis 3](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), acuerdos 1, 3 y 5, punto 3).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Capa 1, la base de Cimiento: cada ajuste tiene un valor común, que el administrador cambia en «Configuración». Sin valor guardado, vale el de fábrica | Análisis 2, acuerdo 3; análisis 3, acuerdo 5 |
| RN-02 | Capa 2, el proyecto: en «Proyectos» cada ajuste puede tener su valor, que manda solo para él; vacío, vale el de la base. Cambiar la base no pisa al proyecto que tiene el suyo. Las reglas siguen con su nivel por proyecto | Análisis 2, acuerdo 3 |
| RN-03 | Los ajustes son «Rutas en los avisos» (relativas o completas), «Límite por enganche» y «Límite por archivo». Los límites dejan de ser columnas del proyecto y lo que tenía cada uno pasa a su ajuste | Análisis 2, acuerdo 3 |
| RN-04 | Capa 3, la suspensión: una regla, o el freno entero, se suspende para un proyecto con motivo y vencimiento, de hasta 30 días. Se levanta antes con un botón. Nunca se suspenden el núcleo (`00·N1` a `00·N8`, `00·N6` incluida) ni el histórico | Análisis 3, acuerdos 1 y 5 |
| RN-05 | Los enganches leen todo desde MariaDB sin Django: el valor del proyecto, si no el de la base, si no el de fábrica; sin base, el de fábrica | Análisis 2, acuerdo 3 |
| RN-06 | Cada cambio escribe `.agente/configuracion.md` en la carpeta del proyecto: una copia de lo que vale, generada desde la base, que no se edita | Análisis 3, acuerdo 3 |
| RN-07 | El aviso por límite pasa de `hook_presupuesto.py` a `core/enganches/presupuesto.py` y lee los límites de los ajustes | Análisis 2, punto 6 |

### 3.2 Supuestos

- El freno nombra la regla en su motivo, como hoy.

### 3.3 Fuera de alcance

- Que el aviso del freno diga la salida: HU-024.
- Mostrar las rutas según el ajuste: HU-014.

---

## 4. Criterios de aceptación

### CA-01 · Base y proyecto

**Sale de:** análisis 2 del pendiente 119, punto 5.

```gherkin
Dado un ajuste con valor en la base y un proyecto sin el suyo
Cuando el proyecto lo lee
Entonces vale el de la base
Y cuando el proyecto pone el suyo, vale el suyo aunque la base cambie
Y sin base de datos vale el de fábrica
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos.tests_configuracion` desde `proyectos/cimiento/` → pasan los casos de capas.
2. Entrar como administrador a «Configuración» y a «Proyectos» → se ven y se guardan los ajustes.

**Aprobado cuando:** la lectura sin Django da el valor de la capa que manda.

### CA-02 · Suspender y levantar

**Sale de:** análisis 3 del pendiente 119, punto 3.

```gherkin
Dado un proyecto con 02·F8 en «frena»
Cuando el administrador la suspende con motivo y vencimiento
Entonces el freno la deja pasar hasta que vence o se levanta
Y suspender el freno entero deja pasar todo, menos el núcleo
Y no se puede suspender 00·N6, otra regla del núcleo ni el histórico, ni sin motivo, ni por más de 30 días
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos.tests_configuracion` → pasan los casos de suspensión.

**Aprobado cuando:** la suspensión vencida o levantada ya no cuenta.

### CA-03 · La copia y los límites

**Sale de:** análisis 2 del pendiente 119, puntos 5 y 6; análisis 3, punto 3.

```gherkin
Dado un cambio en la base, en un proyecto o en una suspensión
Cuando se guarda
Entonces .agente/configuracion.md del proyecto dice lo que vale
Y el aviso por límite usa el límite de los ajustes
Y lo que cada proyecto tenía en sus columnas de límites quedó en sus ajustes
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos.tests_configuracion core.enganches.tests_limites` → pasan los casos de la copia y los límites.

**Aprobado cuando:** la copia coincide con la base.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | El freno lee niveles y suspensiones en una sola conexión |
| RNF-02 | **Auditoría** | Cada suspensión guarda quién, cuándo, por qué y hasta cuándo, y quién la levantó |
| RNF-03 | **Seguridad** | Solo el administrador cambia la base, los ajustes y las suspensiones |

---

## 6. Diseño y referencias

Documento funcional: los análisis 2 y 3 del pendiente 119. Modelo de datos: tablas nuevas `proyectos_ajustebase`, `proyectos_ajustedelproyecto` y `proyectos_suspension`; salen las columnas `limite_enganche` y `limite_archivo` de `proyectos_proyecto`.

---

## 7. Tareas técnicas derivadas

- [x] El catálogo de ajustes, los modelos y la migración que pasa los límites.
- [x] La lectura sin Django, y el freno con las suspensiones.
- [x] Las pantallas «Configuración», ajustes del proyecto y suspensiones.
- [x] La copia `.agente/configuracion.md`.
- [x] El aviso por límite en `core/`.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-013-tres-capas` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-013-tres-capas/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-013-tres-capas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-013-tres-capas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Una suspensión que se olvida | Vence sola; no pasa de 30 días |
| Riesgo | Suspender lo que protege las claves | El núcleo y el histórico no se ofrecen y el servidor los rechaza |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde los análisis 2 y 3 del pendiente 119 |
