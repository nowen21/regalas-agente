# Funcionalidad implementada — Fase `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` (módulo Acceso)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-001](../HU-001-entrar-con-cuenta-y-contrasena.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `AA-EP-022-HU-001-sin-entrar-no-se-ve-nada` |
| **Épica / HU** | [EP-022](../../epica.md) · [HU-001](../HU-001-entrar-con-cuenta-y-contrasena.md) |
| **Módulo** | Acceso |
| **Fecha de cierre** | 2026-09-01 |
| **Versión del estándar bajo la que cerró** | 37.2.1 |

---

## 1. Qué se implementó — resumen

**La plataforma pide cuenta y contraseña, y ninguna pantalla responde sin haber entrado.**

**El guardián va como middleware, y esa es la decisión que más protege.** Un decorador por vista hay que acordarse de ponerlo: la pantalla que alguien escriba dentro de seis meses nacería abierta, y nadie lo notaría porque funcionar, funciona. Con esto **nace protegida**, y abrirla exige escribirlo en una lista de dos renglones que se lee de un vistazo.

**Se usa `django.contrib.auth` y no se escribió nada propio.** Guardar contraseñas, compararlas sin filtrar tiempos, expirar sesiones: cada una tiene una forma correcta y varias que parecen correctas.

**Y `/esta-viva/` quedó protegida.** Se pensó dejarla abierta —una comprobación de vida que pide contraseña no puede decir «estoy caída»— y se cerró al leer qué responde: **la ruta de la carpeta de datos**. Una comprobación que revela dónde vive algo no responde a cualquiera.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «Ninguna pantalla sin entrar» (`RN-1`) | guardián | `ExigirHaberEntrado` en [plataforma/nucleo/acceso/middleware.py](../../../../../plataforma/nucleo/acceso/middleware.py) | ✅ | CP-001 |
| «La contraseña cifrada» (`RN-2`) | ajeno | Lo trae `django.contrib.auth` | ✅ | CP-002 |
| «Lleva a donde se iba» (`RN-3`) | guardián | `redirect_to_login` con la ruta pedida | ✅ | CP-002 |
| «El mensaje no distingue» (`RN-4`) | vista | `Entrar.form_invalid` | ✅ | CP-002 |
| «La contraseña se pide sin mostrarla» (`RN-5`) | consola | `crear_cuenta`, con `getpass` | ✅ | — |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 · T-02 | `auth` instalada, y el guardián con su lista corta |
| T-03 · T-04 | La pantalla de entrar y la orden de crear cuentas |
| T-05 · T-06 | Quién entró en la barra, y **cinco archivos de pruebas que aprendieron a entrar** |
| T-07 | **11 pruebas** |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `plataforma/nucleo/acceso/` | 11 pruebas de esta fase, en verde |
| La batería de la plataforma completa | 610 pruebas, en verde |
| La batería del estándar | 733 pruebas, en verde |

**Lo que las pruebas no dicen:** nada sobre alguien intentando entrar muchas veces: no hay límite de intentos.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Desde `plataforma/`:

```
python manage.py crear_cuenta jose --grupo usuario
python manage.py crear_cuenta el-agente --grupo agente
python manage.py crear_cuenta jose --cambiar-clave
```

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| **Middleware, no decorador** | Una pantalla nueva nace protegida |
| **La lista de lo abierto es corta y se lee** | Cada renglón es una decisión |
| **Un solo mensaje para los dos errores** | Distinguir confirma qué cuentas existen |
| **La contraseña se pide sin mostrarla** | La línea de órdenes queda en el historial |
| **`/esta-viva/` no queda abierta** | Revela la ruta de la carpeta de datos |

Señal registrada: [`S-125`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **No hay límite de intentos** ni demora entre uno y otro. Con la plataforma en una máquina no expuesta, quien puede intentar ya está adentro; en un servidor, hay que mirarlo.
- **Las cuentas se pierden si se borra la base.** Es lo segundo que no se reconstruye, junto con las aprobaciones.
- **La contraseña solo exige ocho caracteres.**

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [documentacion/acceso/spec.md](../../../../acceso/spec.md) | Nace: módulo nuevo |
| [cvds/diseno/README.md](../../../../../cvds/diseno/README.md) | Su sección 8, rehecha entera |
| [documentacion/senales.md](../../../../senales.md) | `S-125` |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

**Ninguna migración y ninguna dependencia nueva.**
