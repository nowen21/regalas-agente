# HU-015 · Se ve lo que corre sin tokens y lo que conviene automatizar


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-015 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien decide qué pasar a un programa
- **Quiero** ver qué corre sin gastar tokens y qué se repite tanto que conviene automatizar
- **Para** empezar por lo que más ahorra

---

## 3. Contexto y descripción

«Gasto» solo mostraba lo que llega al modelo; un enganche que corre sin entregarle nada no aparecía, y nada decía qué se repite ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 4, puntos 9 y 10).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | El lector guarda cada ejecución de un enganche, también la que no le entrega nada al modelo | Punto 9 |
| RN-02 | «Lo que corre sin tokens»: cada enganche con cuántas veces corrió y cuántos tokens agregó | Punto 9 |
| RN-03 | De cada comando se guarda solo el programa y su orden (`git status`, `python manage.py`), nunca el comando completo | Punto 10 |
| RN-04 | «Candidatos a automatizar», con los tokens que se ahorrarían: archivos leídos tres veces o más en el período; enganches que agregan contexto en casi cada mensaje; comandos que se repiten tres veces o más | Punto 10 |
| RN-05 | Los pedidos de una misma palabra clave que siguen los mismos pasos quedan para cuando haya más datos | Acuerdo 4 |

### 3.2 Supuestos

- El vigilante de la HU-011 guarda lo nuevo de los `.jsonl`.

### 3.3 Fuera de alcance

- RN-05.

---

## 4. Criterios de aceptación

### CA-01 · Lo que corre sin tokens

**Sale de:** análisis 2 del pendiente 119, punto 9.

```gherkin
Dado una sesión con un enganche que le entrega contexto al modelo y otro que no
Cuando se guarda y se abre «Gasto»
Entonces «Lo que corre sin tokens» trae los dos, con sus veces y sus tokens, el segundo con cero
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_tercera_tanda` desde `proyectos/cimiento/` → pasan los casos de ejecuciones.

**Aprobado cuando:** el enganche sin tokens aparece con sus veces.

### CA-02 · Candidatos a automatizar

**Sale de:** análisis 2 del pendiente 119, punto 10.

```gherkin
Dado un período con un archivo leído tres veces, un enganche en cada mensaje y un comando repetido
Cuando se abre «Gasto»
Entonces «Candidatos a automatizar» los nombra con los tokens que se ahorrarían
Y del comando solo se ve el programa y su orden
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_tercera_tanda` → pasan los casos de candidatos.

**Aprobado cuando:** ninguna fila guarda un comando completo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Privacidad** | No se guarda el comando completo ni texto (`12`) |
| RNF-02 | **Rendimiento** | «Gasto» sigue respondiendo en menos de un segundo con 30 días |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 4. Modelo de datos: tabla nueva `consumo_ejecuciondeenganche`; campo nuevo `orden` en `consumo_gastodeherramienta`.

---

## 7. Tareas técnicas derivadas

- [x] El lector y el guardado de ejecuciones y órdenes.
- [x] Las dos secciones de «Gasto».
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-015-tercera-tanda` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-015-tercera-tanda/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-015-tercera-tanda/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-015-tercera-tanda/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Guardar algo privado de un comando | Solo programa y orden |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 2 del pendiente 119 |
