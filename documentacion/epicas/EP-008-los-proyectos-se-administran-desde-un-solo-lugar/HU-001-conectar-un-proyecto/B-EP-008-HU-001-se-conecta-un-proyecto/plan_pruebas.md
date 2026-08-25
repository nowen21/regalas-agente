# Plan de Pruebas — Fase B-EP-008-HU-001: se conecta un proyecto   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-008-HU-001 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-08-25 |

---

## 2. Qué se prueba

Que un proyecto quede conectado con lo que lo identifica, que lo que no debe registrarse se rechace diciendo por qué, y que conectar **no toque nada** dentro de la carpeta del proyecto.

**No se prueba** avisar la ruta perdida (fase C), traer su documentación (fase E) ni calcular su estado (fase G).

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que guardar y rechazar hagan lo suyo | Sí |
| Integración | Que conectar pase por la auditoría y por el almacén | Sí |
| Interfaz | Que las dos pantallas muestren y dejen conectar | Sí |
| Aislamiento | Que la carpeta del proyecto no cambie | Sí |
| Manual | Conectar el repositorio real del estándar, sin escribir en él | No: lo hace una persona |

### 3.2 Técnicas

- Comparar la carpeta entera antes y después, archivo por archivo.
- Casos que buscan el rechazo, no el camino feliz.
- Sabotaje: romper el código a propósito para comprobar que las pruebas lo cazan.
- Proyectos de mentira creados y borrados por la propia prueba.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| `CA-01` un proyecto queda registrado | [CP-001](#cp-001--un-proyecto-queda-conectado) | ☐ |
| `CA-02` una ruta que no existe no se registra | [CP-002](#cp-002--la-ruta-que-no-existe-se-rechaza-y-se-dice-cuál-era) | ☐ |
| `CA-03` registrar dos veces la misma ruta avisa | [CP-003](#cp-003--la-ruta-ya-registrada-dice-qué-proyecto-la-tiene) | ☐ |
| `RN-3` la versión declarada debe existir | [CP-004](#cp-004--una-versión-de-reglas-que-no-existe-se-rechaza) | ☐ |
| Transversal: sin control de versiones se advierte | [CP-005](#cp-005--la-carpeta-sin-control-de-versiones-se-conecta-con-advertencia) | ☐ |
| `RN-3` de la HU: la acción queda en la auditoría | [CP-006](#cp-006--conectar-deja-su-registro-en-la-auditoría) | ☐ |
| Las dos pantallas muestran y dejan conectar | [CP-007](#cp-007--se-ve-la-lista-y-se-entra-a-un-proyecto) | ☐ |
| Un proyecto sin estándar instalado se conecta, con aviso | [CP-008](#cp-008--el-proyecto-sin-estándar-instalado-se-conecta-con-aviso) | ☐ |
| `CA-04` · que NO pase: que se toque el código | [CP-009](#cp-009--que-no-pase-que-conectar-toque-la-carpeta-del-proyecto) | ☐ |

## 5. Los casos

### CP-001 · Un proyecto queda conectado

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el proyecto quede con lo que lo identifica, y que su carpeta de documentación exista |
| **Cómo se corre** | Se crea una carpeta de mentira con su `CLAUDE.md` declarando una versión que sí existe, y se conecta |
| **Resultado esperado** | Aparece en la lista, con su nombre, su ruta, su versión y su fecha. Su carpeta de documentación existe en la plataforma. El estado responde `sin empezar` |
| **Si falla** | Se revisa qué dato no se está guardando, o dónde quedó la carpeta |

### CP-002 · La ruta que no existe se rechaza, y se dice cuál era

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que no se registre un proyecto que apunta a la nada |
| **Cómo se corre** | Se intenta conectar con una ruta inventada |
| **Resultado esperado** | No se registra, y la respuesta **trae la ruta que se buscó**, para poder ver el error de tecleo |
| **Si falla** | Un rechazo que no dice qué ruta se buscó obliga a adivinar |

### CP-003 · La ruta ya registrada dice qué proyecto la tiene

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que dos proyectos no apunten al mismo código |
| **Cómo se corre** | Se conecta una carpeta, y después se intenta conectar la misma con otro nombre |
| **Resultado esperado** | No se registra el segundo, y se dice **cuál** proyecto ya la tiene, no solo que está repetida |
| **Si falla** | Se revisa si la comparación de rutas normaliza mayúsculas y separadores: la misma carpeta escrita distinto es la misma carpeta |

### CP-004 · Una versión de reglas que no existe se rechaza

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que un número inventado no entre |
| **Cómo se corre** | Se conecta un proyecto cuyo `CLAUDE.md` declare `999.0.0`, que no está en el registro de cambios |
| **Resultado esperado** | Se rechaza, diciendo que esa versión no existe |
| **Si falla** | Es el pendiente 82 otra vez: un número mayor que el real apaga el aviso de desfase en vez de dispararlo. **Comprobar contra la vigente no basta** |

### CP-005 · La carpeta sin control de versiones se conecta, con advertencia

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la advertencia no se convierta en rechazo |
| **Cómo se corre** | Se conecta una carpeta que no esté bajo control de versiones |
| **Resultado esperado** | **Se registra**, y se advierte que su código no tiene respaldo |
| **Si falla** | Si rechaza, la plataforma deja fuera a los proyectos que más falta le hacen |

### CP-006 · Conectar deja su registro en la auditoría

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la fase D sirva para algo de verdad, y no solo en sus propias pruebas |
| **Cómo se corre** | Se cuentan los registros, se conecta un proyecto, y se vuelve a contar |
| **Resultado esperado** | Hay un registro nuevo, con el proyecto y con qué se hizo. Y **si el registro no se puede escribir, el proyecto no queda conectado** |
| **Si falla** | Se revisa si conectar está escribiendo por fuera de `con_constancia` |

### CP-007 · Se ve la lista y se entra a un proyecto

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que las dos pantallas muestren lo que hay |
| **Cómo se corre** | Con dos proyectos conectados, se pide la lista y después uno de ellos |
| **Resultado esperado** | La lista trae los dos con su estado; la de uno trae su ruta, su versión y qué falta. **Sin ningún proyecto conectado, la lista lo dice**, en vez de quedar en blanco |
| **Si falla** | Una pantalla vacía sin explicación se lee como un error de la plataforma |

### CP-008 · El proyecto sin estándar instalado se conecta, con aviso

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la plataforma sirva también para los proyectos que todavía no adoptaron el estándar |
| **Cómo se corre** | Se conecta una carpeta **sin** `CLAUDE.md`, o con uno que no declare versión |
| **Resultado esperado** | **Se registra**, con la versión vacía, y se avisa que no adoptó ninguna. El aviso se ve en la pantalla del proyecto |
| **Si falla** | Si rechaza, la plataforma deja fuera a los proyectos que más falta le hacen. Es lo contrario de lo que se decidió el 2026-08-25 |

**Ojo con la diferencia que este caso protege:** vacío y falso no son lo mismo. `CP-004` rechaza una versión inventada; este acepta la ausencia. Si los dos se resuelven con el mismo camino, uno de ellos quedó mal.

### CP-009 · Que NO pase: que conectar toque la carpeta del proyecto

| Campo | Valor |
|---|---|
| **Qué comprueba** | `RN-1`: registrar un proyecto es una anotación de la plataforma, no una intervención en su código |
| **Cómo se corre** | Se anota qué archivos tiene la carpeta del proyecto y con qué contenido, se conecta, y se compara **archivo por archivo** |
| **Resultado esperado** | Ningún archivo cambió, se creó ni se borró. Tampoco cambió su fecha |
| **Si falla** | Se busca qué escribió allá, y se corrige antes de seguir. Es el caso que más daño evita: la plataforma administra proyectos ajenos |

## 6. Lo que este plan NO puede probar

- **Que la plataforma sirva para los proyectos reales del usuario.** Se prueba con carpetas de mentira y con el repositorio del estándar; los demás llegan cuando se conecten.
- **Que la pantalla se entienda.** Se prueba que muestre lo que debe, no que sea clara. Eso lo dice el usuario al usarla.
- **Que el estado sea correcto.** Acá siempre responde `sin empezar`, porque todavía no hay documentos que mirar. Se prueba en la fase G.

## 7. Criterios de salida

- Los nueve casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- Las pruebas validadas con sabotaje: romper lo que cada una promete cuidar, y comprobar que falla.
- Ninguna carpeta real del usuario usada como conejillo.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_trabajo.md](plan_trabajo.md).
