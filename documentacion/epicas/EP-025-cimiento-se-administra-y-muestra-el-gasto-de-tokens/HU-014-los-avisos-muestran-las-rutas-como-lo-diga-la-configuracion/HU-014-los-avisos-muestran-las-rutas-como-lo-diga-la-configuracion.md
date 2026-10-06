# HU-014 · Los avisos muestran las rutas como lo diga la configuración


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-014 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/enganches/`, `adaptadores/claude-code/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien lee los avisos del agente
- **Quiero** que las rutas salgan relativas al proyecto o completas, según lo que diga su configuración
- **Para** abrirlas sin adivinar desde dónde están escritas

---

## 3. Contexto y descripción

Cada enganche armaba sus rutas a su manera, y `hook_md.py` seguía usando las copias viejas de `validadores/` ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdos 3 y 5, puntos 7 y 8).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | `Proyecto.mostrar`, que nombra una ruta en un aviso, la da relativa o completa según el ajuste «Rutas en los avisos» del proyecto | Punto 7 |
| RN-02 | Un proyecto sin registro usa el valor de fábrica, relativas: la base de Cimiento es de los proyectos que administra | Propuesta del agente |
| RN-03 | Los enganches que muestran rutas las piden a `Proyecto.mostrar` | Punto 7 |
| RN-04 | La lógica de `hook_md.py` pasa a `core/enganches/`, con `raiz_pedida` y `archivo_editado` de `core/comun/consola.py`; el adaptador solo lee la entrada y llama a `core/` | Punto 8 |

### 3.2 Supuestos

- La HU-013 dejó el ajuste en la base.

### 3.3 Fuera de alcance

- Retirar `validadores/comun.py`, `enlaces.py`, `marcas.py` y `sesiones.py`: `evals/correr.py` los sigue usando.

---

## 4. Criterios de aceptación

### CA-01 · Las rutas según el ajuste

**Sale de:** análisis 2 del pendiente 119, punto 7.

```gherkin
Dado un proyecto registrado con «Rutas en los avisos» en completas
Cuando un aviso nombra un archivo del proyecto
Entonces sale con su ruta completa
Y con «relativas», o sin registro, sale relativa al proyecto
```

**Cómo validarlo:**
1. Correr `python manage.py test core.proyectos.tests_rutas` desde `proyectos/cimiento/` → pasan los casos de rutas.

**Aprobado cuando:** cambiar el ajuste cambia cómo sale la ruta.

### CA-02 · `hook_md.py` en `core/`

**Sale de:** análisis 2 del pendiente 119, punto 8.

```gherkin
Dado una edición de un .md con un enlace roto y una marca de redacción
Cuando corre el enganche
Entonces el adaptador solo lee la entrada y llama a core/
Y el resultado es el de antes: código 2 con los enlaces rotos y la marca nombrada
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_md` → pasan los casos del enganche.

**Aprobado cuando:** el adaptador no importa nada de `validadores/`.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | El ajuste se lee una vez por proyecto y por proceso |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdos 3 y 5.

---

## 7. Tareas técnicas derivadas

- [x] `Proyecto.mostrar` con el ajuste.
- [x] Los enganches que muestran rutas.
- [x] `hook_md.py` en `core/`.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-014-rutas-y-hook-md` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-014-rutas-y-hook-md/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-014-rutas-y-hook-md/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-014-rutas-y-hook-md/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-013 | Alto |
| Riesgo | Que una prueba con carpetas temporales vea rutas completas | Sin registro vale el de fábrica |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 2 del pendiente 119 |
