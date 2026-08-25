# Plan de Pruebas — Fase D-EP-009-HU-001: la constancia va antes que el efecto   ·   `[CAPA 3]`

## 1. Identificación

| Campo | Valor |
|---|---|
| **Código** | PP-D-EP-009-HU-001 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-25 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente |

---

## 2. Qué se prueba

Que ninguna acción cambie algo sin dejar constancia, que la constancia no se pueda alterar después, y que ninguna clave termine escrita en ella.

**No se prueba** consultar lo registrado: no hay pantalla en esta versión.

## 3. Estrategia

### 3.1 Niveles

| Nivel | Objetivo | Automatizado |
|---|---|---|
| Unitario | Que el registro se escriba con sus seis datos | Sí |
| Integridad | Que editar y borrar no se puedan | Sí |
| Falla | Que la acción se detenga cuando el registro no se puede escribir | Sí |
| Credenciales | Que la clave quede tapada y el molde no | Sí |

### 3.2 Técnicas

- Prueba de bloqueo: dejar el registro sin poder escribirse a propósito.
- Prueba de intento: pedir lo que no debe poderse, y comprobar el archivo después.
- Casos que buscan el rechazo, no el camino feliz.
- Claves inventadas, nunca reales.

### 3.5 Alcance de la corrida

Un ciclo. Si un caso falla, se corrige y se corre el ciclo completo, no solo el caso que falló.

## 4. Matriz de trazabilidad

| Qué exige | Caso | Estado |
|---|---|---|
| `CA-01` toda acción queda registrada | [CP-001](#cp-001--la-acción-queda-registrada-con-sus-seis-datos) | ☐ |
| `CA-02` lo registrado no se edita ni se borra | [CP-002](#cp-002--editar-o-borrar-no-se-puede-y-el-intento-queda) | ☐ |
| `CA-03` sin constancia no hay efecto | [CP-003](#cp-003--con-el-registro-bloqueado-nada-cambia) | ☐ |
| `CA-05` ninguna credencial entra al registro | [CP-004](#cp-004--la-clave-queda-tapada-con-comillas-y-sin-ellas) | ☐ |
| `CA-05` el molde no se tapa | [CP-005](#cp-005--lo-que-solo-parece-clave-se-deja-legible) | ☐ |
| `CA-04` la acción queda enlazada con su sesión | [CP-006](#cp-006--el-enlace-a-la-sesión-está-y-vacío-cuando-no-la-hay) | ☐ |
| Que NO pase: que una acción cambie algo sin registro | [CP-007](#cp-007--que-no-pase-que-algo-cambie-sin-quedar-registrado) | ☐ |

## 5. Los casos

### CP-001 · La acción queda registrada con sus seis datos

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que el registro traiga qué se hizo, sobre qué, quién, cuándo, qué cambió y en qué proyecto |
| **Cómo se corre** | Se ejecuta una acción y se lee el registro |
| **Resultado esperado** | Los seis datos están. El de proyecto puede ir vacío, y eso se ve como vacío, no como faltante |
| **Si falla** | Se revisa qué dato no se está entregando desde el módulo que actúa |

### CP-002 · Editar o borrar no se puede, y el intento queda

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que lo escrito no se pueda alterar después |
| **Cómo se corre** | Se anota el contenido del registro, se intenta editar y borrar, y se compara |
| **Resultado esperado** | El registro no cambió, y hay constancia del intento |
| **Si falla** | Existe una operación de escritura que no debería existir: se quita, no se protege |

### CP-003 · Con el registro bloqueado, nada cambia

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que la constancia vaya antes que el efecto |
| **Cómo se corre** | Se deja el registro sin poder escribirse y se pide una acción que cambie algo |
| **Resultado esperado** | La acción se detiene, se avisa por qué, y **nada cambió** |
| **Si falla** | El cambio se está haciendo antes del registro: se invierte el orden |

### CP-004 · La clave queda tapada, con comillas y sin ellas

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que ninguna credencial llegue al registro |
| **Cómo se corre** | Se registra un texto con `password: "inventada123"` y otro con `API_KEY=inventada123`, ambas falsas |
| **Resultado esperado** | Las dos tapadas. El nombre de la variable queda legible |
| **Si falla** | Es el pendiente 84 otra vez, ahora en la plataforma |

### CP-005 · Lo que solo parece clave se deja legible

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que tapar de más no vuelva ilegible el registro |
| **Cómo se corre** | Se registra un texto con `clave: tu-clave`, otro con `changeme` y otro que lee del entorno |
| **Resultado esperado** | Ninguno de los tres se tapa |
| **Si falla** | El enmascarador está tapando moldes, y quien lea el registro no entiende de qué se hablaba |

### CP-006 · El enlace a la sesión está, y vacío cuando no la hay

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que se pueda llegar desde la acción a lo que la sesión dejó escrito |
| **Cómo se corre** | Se registra una acción dentro de una sesión y otra fuera de toda sesión |
| **Resultado esperado** | La primera trae el enlace y se puede seguir; la segunda lo trae vacío, y eso se muestra como dato |
| **Si falla** | Se revisa qué identifica una sesión, que es la duda 2 del plan de trabajo |

### CP-007 · Que NO pase: que algo cambie sin quedar registrado

| Campo | Valor |
|---|---|
| **Qué comprueba** | Que no exista un camino que escriba saltándose la auditoría |
| **Cómo se corre** | Se cuentan los registros, se ejecutan todas las acciones que la plataforma sabe hacer, y se vuelve a contar |
| **Resultado esperado** | Tantos registros nuevos como acciones ejecutadas. Ninguna de menos |
| **Si falla** | Hay un camino que escribe directo: se cierra ese camino, no se le agrega el registro aparte |

## 6. Lo que este plan NO puede probar

- **Que registrar antes de ejecutar no haga lento el trabajo.** Se prueba con pocas acciones; el volumen real llega con el uso.
- **Que el enmascarador reconozca toda forma de clave.** Reconoce las que `secretos.py` conoce hoy. Una forma nueva se descubre cuando aparece.
- **Que la acción de la fase B quede bien registrada.** Esa fase todavía no existe.

## 7. Criterios de salida

- Los siete casos con veredicto escrito.
- Ningún caso en **No cumple** sin corregir.
- Ninguna credencial real usada en las pruebas.

---

**Pendiente de aprobación.** Se presenta junto con [plan_trabajo.md](plan_trabajo.md).
