# Plan de Pruebas — Fase `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas`   ·   `[CAPA 3]`

---

## 1. Introducción

### 1.1 Propósito

Comprobar que la regla existe con su forma, que no fija un idioma, y que los modelos la citan en vez de repetirla.

### 1.2 Alcance

**Dentro:** la regla nueva, su clasificación, y los dos documentos modelo.

**Fuera:** la ortografía y la gramática, que son otra regla, y el programa que la comprobaría.

### 1.3 Documentos de referencia

- [HU-037](../HU-037-la-norma-de-redaccion-del-agente.md)
- El [pendiente 93](../../../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md)
- El [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md)

---

## 2. Elementos a probar

| Elemento | Por qué entra |
|---|---|
| La forma de la regla | Una regla mal formada no rige: la primera discusión es sobre su forma |
| Que no nombre un idioma concreto | Si lo nombra, deja de servir a un proyecto en otro idioma |
| El texto repetido en los modelos | Es lo que la regla viene a reemplazar |

---

## 3. Estrategia de pruebas

En seco, sobre el propio repositorio: el validador de meta-reglas comprueba el molde, el identificador y la clasificación; lo demás se lee.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- El alcance, decidido por el usuario.

### 4.2 Criterios de salida

- `validar.py metareglas` sin incumplimientos.
- `validar.py estandar` sin fallas, con el enlace del modelo resolviendo.
- El cuerpo de la regla sin ningún idioma nombrado.

### 4.3 Criterios de suspensión y reanudación

Si para que pase hubiera que tocar un archivo que otra sesión tiene en curso, no se toca: se declara y el criterio queda a medias.

---

## 5. Matriz de trazabilidad

| CA | Caso |
|---|---|
| CA-01 | CP-001 |
| CA-03 | CP-002 |
| CA-02 | CP-003 |

---

## 6. Casos de prueba

### CP-001 — La regla existe y cumple su molde

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Prioridad** | **Crítica** |
| **Cómo** | `python validadores/validar.py metareglas` |
| **Resultado esperado** | Sin incumplimientos, con la regla contada entre las del capítulo |

### CP-002 — No fija un idioma

| Campo | Valor |
|---|---|
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |
| **Cómo** | Leer el cuerpo buscando el nombre de un idioma o de un país |
| **Resultado esperado** | Ninguno: dice «el que usa el proyecto» |

### CP-003 — Los modelos citan en vez de repetir

| Campo | Valor |
|---|---|
| **Tipo** | De ejecución |
| **Cómo** | Buscar el texto de la regla once en los dos modelos, y comprobar que el enlace resuelve |
| **Resultado esperado** | El de instalación cita; el de usuario queda declarado |

---

## 7. Datos y ambientes de prueba

El propio repositorio, sin copias.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Incumplimientos de `metareglas` | **0** |
| Idiomas nombrados en el cuerpo | **0** |
| Archivos de otra sesión tocados | **0** |

---

## 15. Aprobación

Alcance aprobado el 2026-08-30, con la decisión del usuario sobre a qué se aplica.
