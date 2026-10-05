# HU-001 · Cimiento corre sobre MariaDB y tiene la base de sus pantallas


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `plantillas/`, `proyectos/cimiento/` (configuración, `core/inicio/`, `templates/`), `proyectos/cimiento/core/herramientas/instalar.py` |
| **Tipo** | Técnica |
| **Prioridad** | Must: primera de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada el 2026-10-04, con sus cinco criterios probados |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** que Cimiento guarde sus datos en MariaDB y tenga una plantilla común para sus pantallas
- **Para** construir encima la administración y el tablero de tokens sin rehacer la base

---

## 3. Contexto y descripción

Cimiento es una base Django sin módulos, sobre SQLite, y solo tiene el administrador que trae Django. Las demás HU de la [épica](../epica.md) guardan en MariaDB `cimiento` y muestran pantallas con Tabler, htmx y ApexCharts, que se instalan con npm. La plantilla de estructura Django del estándar hoy solo admite dependencias de pip.

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | La conexión a MariaDB se lee del `.env`, que no se versiona | Análisis 1 del pendiente 119, acuerdo 15 |
| RN-02 | Las dependencias de npm se declaran en `package.json` con `package-lock.json`, se instalan en `node_modules/`, que no se versiona, y Django las lee con `STATICFILES_DIRS` | Acuerdo 6 |
| RN-03 | Las pantallas son propias, con plantillas de Django, no con el administrador de Django | Acuerdo 3 |
| RN-04 | La instalación crea la base antes de activar el freno | Acuerdo 15 |
| RN-05 | Sin conexión a MariaDB, se dice que hay que prenderla y dónde la busca; no se muestra un error interno | Acuerdo 15 |

### 3.2 Supuestos

- MariaDB 11.4 corre en esta máquina en el puerto 3307, con el usuario `root` sin contraseña (verificado el 2026-10-04).
- Node y npm están instalados.

### 3.3 Fuera de alcance

- Entrar con usuario y contraseña: HU-002.
- Un usuario propio de MariaDB en vez de `root` (épica, §5.3).
- Que el freno lea la base: HU-005.

---

## 4. Criterios de aceptación

### CA-01 · Cimiento guarda en MariaDB con la conexión del `.env`

**Sale de:** análisis 1 del pendiente 119, punto 11.

```gherkin
Dado que el .env de Cimiento trae la conexión a MariaDB
Cuando se corre la preparación de la base
Entonces la base cimiento existe y tiene las tablas de Django
Y .env.example lista las variables de la conexión, sin valores
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `.venv\Scripts\python manage.py preparar_base` → dice que la base `cimiento` está lista y sin migraciones pendientes.
2. Correr `.venv\Scripts\python manage.py showmigrations` → todas las migraciones marcadas con `[X]`.
3. Abrir `.env.example` → trae `DB_NOMBRE`, `DB_USUARIO`, `DB_CLAVE`, `DB_SERVIDOR` y `DB_PUERTO`, sin valores.

**Aprobado cuando:** los tres pasos dan lo dicho.

### CA-02 · Sin MariaDB, Cimiento dice qué hacer

**Sale de:** análisis 1 del pendiente 119, punto 11.

```gherkin
Dado que MariaDB no responde
Cuando se corre la preparación de la base o se abre una pantalla
Entonces el mensaje dice que hay que prender MariaDB, con el servidor y el puerto que busca
Y no se muestra la traza de Python ni se crea nada a medias
```

**Cómo validarlo:**
1. Correr `.venv\Scripts\python manage.py preparar_base` con `DB_PUERTO=3399` puesto en el ambiente → el mensaje dice que MariaDB no responde en `127.0.0.1:3399` y que hay que prenderla; sale con error.
2. Correr `python manage.py test core.inicio` → el caso de la pantalla sin base pasa.

**Aprobado cuando:** el mensaje sale sin traza de Python y la prueba pasa.

### CA-03 · La plantilla de estructura Django admite dependencias de npm

**Sale de:** análisis 1 del pendiente 119, punto 2.

```gherkin
Dado la plantilla de estructura de un proyecto Django
Cuando un proyecto necesita una biblioteca del navegador
Entonces la plantilla dice cómo declararla con npm, dónde se instala y cómo la lee Django
Y la versión del estándar sube como MENOR
```

**Cómo validarlo:**
1. Abrir `plantillas/estructura-proyecto-django.md` → el árbol trae `package.json`, `package-lock.json` y `node_modules/` (no se versiona), y «Dependencias» explica npm.
2. Abrir `CHANGELOG.md` y `VERSION` → entrada nueva y versión MENOR.

**Aprobado cuando:** los dos pasos dan lo dicho.

### CA-04 · Las pantallas tienen su plantilla común

**Sale de:** análisis 1 del pendiente 119, punto 3.

```gherkin
Dado que se instalaron Tabler, htmx y ApexCharts con npm
Cuando se abre la página de inicio de Cimiento
Entonces se ve con menú lateral y cabecera, con los estilos de Tabler
Y la página dice a qué base está conectada
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `npm ci` y después `.venv\Scripts\python manage.py runserver`.
2. Abrir `http://127.0.0.1:«PUERTO del .env»/` → menú lateral con «Inicio», cabecera con «Cimiento», y la línea «Base de datos: cimiento, en MariaDB 11.4».
3. Correr `python manage.py test core.inicio` → pasan los casos de la página.

**Aprobado cuando:** la página se ve así y las pruebas pasan.

### CA-05 · La instalación prepara Cimiento

**Sale de:** análisis 1 del pendiente 119, punto 11.

```gherkin
Dado el estándar recién clonado, con MariaDB prendida
Cuando se instala el estándar en su propia carpeta
Entonces se instalan las dependencias de npm de Cimiento y se crea su base, antes de poner los enganches
Y si MariaDB está apagada, la instalación lo dice como pendiente y sigue con lo demás
```

**Cómo validarlo:**
1. Correr `python validadores/instalar.py "«carpeta del estándar»"` (simulación) → aparece el paso «preparar Cimiento» antes de los enganches.
2. Correr `python manage.py test core.herramientas.tests_instalacion` → pasan los casos de la preparación con y sin base.

**Aprobado cuando:** el paso aparece en ese orden y las pruebas pasan.

### Criterios de aceptación transversales

- [ ] Errores: un fallo previsto da mensaje accionable **sin exponer detalles internos**; el sistema queda consistente, sin datos a medias (`05`, [`00·N3`](../../../../base/00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
- [ ] Idempotencia: reintentar o doble-enviar **no duplica** efectos ([`03·D6`](../../../../base/03-datos.md#d6--concurrencia-e-idempotencia)).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | Ninguna credencial queda en un archivo versionado (`00·N6`) |
| RNF-02 | **Compatibilidad** | Las versiones de npm quedan fijas en `package-lock.json` (`10·DEP2`) |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdos 3, 5, 6 y 15; puntos 2, 3 y 11.

Modelo de datos afectado: las tablas de Django; ninguna propia todavía.

---

## 7. Tareas técnicas derivadas

- [ ] Plantilla de estructura Django con npm, y la versión MENOR.
- [ ] Conexión a MariaDB desde el `.env`; `.env.example`, `lock.txt` y el README de Cimiento al día.
- [ ] Orden `preparar_base`: crea la base si falta y aplica las migraciones; sin MariaDB, dice qué hacer.
- [ ] `package.json` con Tabler, htmx y ApexCharts; plantilla común y página de inicio.
- [ ] El instalador prepara Cimiento antes de poner los enganches.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-001-mariadb-y-plantilla-comun` | CA-01 a CA-05 | (vacío) | [plan_trabajo.md](A-EP-025-HU-001-mariadb-y-plantilla-comun/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-001-mariadb-y-plantilla-comun/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-001-mariadb-y-plantilla-comun/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | MariaDB corriendo en el puerto 3307 (épica, DEP-01) | Alto |
| Riesgo | Las pruebas de Cimiento ya no corren con MariaDB apagada | Las que no usan la base siguen siendo `SimpleTestCase`; el mensaje dice que hay que prenderla |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
