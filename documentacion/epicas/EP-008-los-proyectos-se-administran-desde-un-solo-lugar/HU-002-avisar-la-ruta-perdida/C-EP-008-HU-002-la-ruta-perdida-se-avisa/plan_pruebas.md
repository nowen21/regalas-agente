# Plan de Pruebas — Fase C-EP-008-HU-002: la ruta perdida se avisa   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-C-EP-008-HU-002 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que una ruta que dejó de existir se avise diciendo **cuál era**, que se pueda corregir sin saltarse lo que conectar comprueba, y que comprobar cincuenta rutas no vuelva lenta la lista.

**No se prueba** buscar la carpeta sola en otro lado: la historia lo deja fuera.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que corregir la ruta haga lo suyo y rechace lo que debe | Sí |
| Interfaz | Que el aviso se vea y diga la ruta | Sí |
| Rendimiento | Que cincuenta proyectos listen bajo un segundo | Sí |
| Aislamiento | Que corregir no toque ninguna de las dos carpetas | Sí |

### 3.2 Técnicas

- **Probar lo que ya estaba construido, no solo lo que se agrega.** Media fase existía antes de abrirla, y un plan que solo mire lo nuevo daría por probado lo que nadie probó.
- Borrar carpetas de mentira para provocar la ruta perdida.
- Casos que buscan el rechazo, no el camino feliz.
- Sabotaje: romper el código a propósito, restaurando con copia y corriendo la suite completa al final.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| `CA-01` la ruta que dejó de existir se avisa | [CP-001](#cp-001--la-ruta-que-dejó-de-existir-se-marca-y-se-nombra) | ☐ |
| `CA-02` su documentación se sigue viendo | [CP-002](#cp-002--con-la-ruta-perdida-su-documentación-sigue-a-la-vista) | ☐ |
| `CA-03` volver a apuntar la ruta quita el aviso | [CP-003](#cp-003--corregir-la-ruta-quita-el-aviso-y-queda-registrado) | ☐ |
| `CA-03` corregir no se salta lo que conectar comprueba | [CP-004](#cp-004--la-ruta-nueva-se-comprueba-igual-que-al-conectar) | ☐ |
| La versión de reglas sale de la carpeta nueva | [CP-005](#cp-005--corregir-la-ruta-relee-la-versión-de-reglas) | ☐ |
| `RNF-02` listar cincuenta proyectos bajo un segundo | [CP-006](#cp-006--cincuenta-proyectos-listan-bajo-un-segundo) | ☐ |
| Que NO pase: que corregir toque alguna de las dos carpetas | [CP-007](#cp-007--que-no-pase-que-corregir-toque-las-carpetas) | ☐ |

## 5. Los casos

### CP-001 · La ruta que dejó de existir se marca, y se nombra

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el proyecto se marque, y que el aviso diga **qué ruta se buscó** |
| **Cómo se corre** | Se conecta un proyecto de mentira, se borra su carpeta, y se abre la lista |
| **Resultado esperado** | Aparece marcado, y el aviso **nombra la ruta**. No basta con «esa ruta no existe» |
| **Si falla** | Sin la ruta, el usuario no puede ver si fue un renombre, un movimiento o un disco sin montar |

**Este caso prueba código que ya existía antes de la fase.** `ruta_viva` salió de la fase B sin que nadie estuviera pensando en esta historia, así que nunca se probó contra ella.

### CP-002 · Con la ruta perdida, su documentación sigue a la vista

| Campo | Valor |
|---|---|
| **Qué comprueba** | `RN-1`: perder la ruta no pierde nada, porque la documentación vive en la plataforma |
| **Cómo se corre** | Se conecta un proyecto, se le guarda un documento, se borra su carpeta de código, y se entra al proyecto |
| **Resultado esperado** | Su documento se lee completo, y se ve el aviso de que su código no está |
| **Si falla** | Si la documentación desaparece con la ruta, la plataforma está guardando en el sitio equivocado |

### CP-003 · Corregir la ruta quita el aviso, y queda registrado

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la corrección funcione de punta a punta |
| **Cómo se corre** | Con la ruta perdida, se corrige a una carpeta que sí existe |
| **Resultado esperado** | El aviso desaparece, la ficha trae la ruta nueva, y la auditoría tiene el registro con la ruta vieja y la nueva |
| **Si falla** | Se revisa si la ruta se guardó solo en el índice: al rehacerlo volvería la vieja |

**El registro tiene que decir de dónde a dónde.** «Se corrigió la ruta» sin las dos rutas no sirve para rastrear nada.

### CP-004 · La ruta nueva se comprueba igual que al conectar

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que corregir no sea una puerta de atrás |
| **Cómo se corre** | Se intenta corregir a una ruta que no existe, y después a una que ya tiene otro proyecto |
| **Resultado esperado** | Las dos se rechazan, diciendo por qué. **La ruta que tenía se conserva**, no queda vacía |
| **Si falla** | Es el mismo hueco que la fase H cerró para la versión de reglas, ahora en la ruta |

### CP-005 · Corregir la ruta relee la versión de reglas

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que no se afirme sobre lo que no se leyó |
| **Cómo se corre** | Se corrige la ruta a una carpeta cuyo `CLAUDE.md` declara **otra** versión |
| **Resultado esperado** | La versión que queda es la de la carpeta nueva |
| **Si falla** | La plataforma estaría diciendo que ese proyecto adoptó una versión que su carpeta actual no declara |

### CP-006 · Cincuenta proyectos listan bajo un segundo

| Campo | Valor |
|---|---|
| **Qué comprueba** | `RNF-02`, y que comprobar rutas no lo rompa |
| **Cómo se corre** | Se conectan cincuenta proyectos de mentira y se pide la lista, midiendo |
| **Resultado esperado** | Menos de un segundo, **con el número escrito en el resultado** |
| **Si falla** | Se decide qué hacer antes de cerrar la fase: comprobar menos seguido, o en otro momento |

**El número se escribe aunque pase.** Un «cumple» sin el número no sirve para comparar cuando haya doscientos proyectos.

### CP-007 · Que NO pase: que corregir toque las carpetas

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que corregir la ruta sea una anotación de la plataforma, en las **dos** carpetas |
| **Cómo se corre** | Se retratan la carpeta vieja y la nueva, se corrige la ruta, y se comparan las dos archivo por archivo |
| **Resultado esperado** | Ninguna de las dos cambió |
| **Si falla** | Corregir estaría moviendo o copiando código, que es lo que la plataforma nunca hace |

**Se miran las dos, no solo la nueva.** El descuido posible es «mover» el proyecto de verdad, y eso tocaría la vieja.

## 6. Lo que este plan NO puede probar

- **Que la medición valga para el uso real.** Se mide con cincuenta proyectos de mentira en la misma máquina. Un disco de red o una carpeta enorme cambian el número.
- **Que el usuario se entere del aviso.** Se prueba que el aviso esté y diga la ruta, no que alguien lo lea.

## 7. Criterios de salida

- Los siete casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- El número de la medición escrito, aunque cumpla.
- Las pruebas validadas con sabotaje, restaurando con copia y corriendo la suite completa al final.
- Ninguna carpeta real del usuario borrada ni usada como conejillo.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
