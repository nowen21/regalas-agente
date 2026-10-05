# HU-002 · Solo entra quien tiene cuenta, y cada grupo hace lo suyo


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/cuentas/`, `proyectos/cimiento/core/inicio/`, `proyectos/cimiento/templates/` |
| **Tipo** | Funcional |
| **Prioridad** | Must: segunda de la épica |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada el 2026-10-04, con sus cuatro criterios probados |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** que solo entre quien tiene cuenta, y que el grupo consulta no pueda cambiar nada
- **Para** que los niveles de las reglas y los límites solo los cambie un administrador

---

## 3. Contexto y descripción

Las pantallas de Cimiento (HU-001) están abiertas a quien abra la dirección. Las de las HU siguientes cambian niveles de reglas y límites, que solo debe tocar un administrador ([épica](../epica.md), §5.4, preguntas 2, 9 y 14).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Se entra con usuario y contraseña, con las cuentas de Django | Análisis 1 del pendiente 119, acuerdo 14 |
| RN-02 | Hay dos grupos: administrador, que registra proyectos y cambia niveles y límites, y consulta, que solo ve | Acuerdo 14 |
| RN-03 | Un superusuario de Django cuenta como administrador | Propuesta del agente: la primera cuenta se crea con `createsuperuser` |
| RN-04 | Sin cuenta, toda pantalla lleva a la entrada; la de base apagada se ve sin entrar | Acuerdo 15: sin base no hay cuentas que revisar |

### 3.2 Supuestos

- La HU-001 está terminada: Cimiento corre sobre MariaDB y tiene su plantilla común.

### 3.3 Fuera de alcance

- Una pantalla para crear cuentas: se crean con órdenes de `manage.py`.
- Recuperar la contraseña por correo.

---

## 4. Criterios de aceptación

### CA-01 · Sin cuenta, se pide entrar

**Sale de:** análisis 1 del pendiente 119, punto 12.

```gherkin
Dado que nadie ha entrado
Cuando se abre cualquier pantalla de Cimiento
Entonces lleva a la página de entrada
Y con usuario y contraseña válidos vuelve a la pantalla pedida
```

**Cómo validarlo:**
1. Abrir `http://127.0.0.1:«PUERTO»/` sin haber entrado → lleva a `/entrar/`.
2. Escribir usuario y contraseña de una cuenta → vuelve a la página de inicio, con el nombre de la cuenta y «Salir» en la cabecera.
3. Correr `python manage.py test core.cuentas` → pasan los casos de entrada.

**Aprobado cuando:** los tres pasos dan lo dicho.

### CA-02 · Una contraseña equivocada no deja entrar

**Sale de:** análisis 1 del pendiente 119, punto 12.

```gherkin
Dado una cuenta que existe
Cuando se escribe una contraseña equivocada
Entonces se queda en la entrada con un mensaje que no dice si el usuario existe
Y no se entra
```

**Cómo validarlo:**
1. En `/entrar/`, escribir un usuario que existe y otra contraseña → mensaje de usuario o contraseña equivocados.
2. Repetir con un usuario que no existe → el mismo mensaje.

**Aprobado cuando:** los dos mensajes son iguales y no se entra.

### CA-03 · El grupo consulta no puede cambiar nada

**Sale de:** análisis 1 del pendiente 119, punto 12.

```gherkin
Dado una cuenta del grupo consulta
Cuando abre una pantalla que solo es para administradores
Entonces recibe «No tiene permiso» con código 403, sin datos de esa pantalla
Y una cuenta del grupo administrador sí la abre
```

**Cómo validarlo:**
1. Correr `python manage.py test core.cuentas` → pasan los casos de permiso por grupo.

**Aprobado cuando:** consulta recibe 403 y administrador y superusuario reciben la pantalla.

### CA-04 · Las cuentas se crean con una orden

**Sale de:** análisis 1 del pendiente 119, punto 12.

```gherkin
Dado que Cimiento está preparado
Cuando se corre la orden de crear cuenta con un grupo
Entonces la cuenta queda creada en ese grupo
Y los dos grupos existen aunque no haya cuentas
```

**Cómo validarlo:**
1. Correr `python manage.py crear_cuenta --usuario prueba --grupo consulta` y escribir la contraseña dos veces → dice que la cuenta quedó en el grupo consulta.
2. Correr `python manage.py test core.cuentas` → pasan los casos de la orden y de los grupos.

**Aprobado cuando:** la cuenta queda creada en su grupo y los dos grupos existen.

### Criterios de aceptación transversales

- [ ] Autorización: solo quien tiene permiso ejecuta la acción; sin permiso se deniega **sin filtrar datos ni su existencia**, y no se elude cambiando parámetros/ruta (`04`).
- [ ] Privacidad: datos personales/sensibles no se exponen ni se registran en claro; se tratan según `marco-normativo` (`12`, [`00·N4`](../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | Las contraseñas las guarda Django con su resumen; nunca en claro (`00·N6`) |
| RNF-02 | **Seguridad** | La salida de la sesión es por POST, con su protección CSRF |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdo 14; punto 12.

Modelo de datos afectado: las tablas de cuentas y grupos de Django; los grupos `administrador` y `consulta`.

---

## 7. Tareas técnicas derivadas

- [ ] Módulo `core/cuentas/` con la migración que crea los dos grupos.
- [ ] Entrada y salida con las vistas de Django y plantillas propias.
- [ ] Toda pantalla pide entrar; la de base apagada no.
- [ ] Mezcla `SoloAdministrador` para las pantallas de las HU siguientes.
- [ ] Orden `crear_cuenta`.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-002-entrada-y-grupos` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-002-entrada-y-grupos/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-002-entrada-y-grupos/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-002-entrada-y-grupos/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001 | Alto |
| Riesgo | Con la base apagada, revisar la sesión falla antes de llegar a la vista | La revisión de la base va antes que la de la entrada |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
