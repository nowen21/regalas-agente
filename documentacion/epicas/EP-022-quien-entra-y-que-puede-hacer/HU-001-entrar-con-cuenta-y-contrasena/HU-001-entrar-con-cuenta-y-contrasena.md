# HU-001 — Entrar con cuenta y contraseña

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-022 Quién entra y qué puede hacer](../epica.md) |
| **Funcionalidad** | `F-036` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Acceso |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-02, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien responde por lo que la plataforma dice
- **Quiero** que pida cuenta y contraseña
- **Para** que se sepa quién hizo cada cosa, y no entre cualquiera que alcance el puerto

---

## 3. Contexto y descripción

**Estaba definido y aplazado, no descartado.** El análisis fijó los permisos de cada actor; el diseño los aplazó mientras hubiera un solo usuario, y advirtió que **con dos es una falla**. El usuario levantó ese aplazamiento el 2026-09-02.

**Se usa `django.contrib.auth`.** Escribir autenticación es la forma más común de escribirla mal: guardar contraseñas, compararlas sin filtrar tiempos, expirar sesiones. Ninguna de esas se escribe acá.

**Y el guardián va como middleware.** Un decorador por vista hay que acordarse de ponerlo: **la vista que alguien escriba dentro de seis meses nacería abierta**, y nadie lo notaría porque funcionar funciona.

### 3.1 Reglas de negocio

- `RN-1` **Ninguna pantalla responde sin haber entrado.** La que no lo exige es la de entrar.
- `RN-2` Las contraseñas se guardan cifradas. **Nunca en claro, ni en el registro.**
- `RN-3` Entrar lleva a donde se iba.
- `RN-4` **Un intento fallido no dice cuál de los dos datos estuvo mal.**
- `RN-5` Las cuentas se crean en la máquina, y la contraseña se pide sin mostrarla.

### 3.2 Supuestos

- Quien alcanza la consola de la máquina ya tiene la máquina.

### 3.3 Fuera de alcance

- **Exponer la plataforma a la red.**
- **Recuperar contraseña por correo.** No hay correo.

---

## 4. Criterios de aceptación

### CA-01 — Ninguna pantalla responde sin haber entrado

```gherkin
Dada una plataforma con cuentas
Cuando se pide cualquier dirección sin haber entrado
Entonces lleva al formulario de entrar
```

**Cómo validarlo:** recorriendo **todas las rutas registradas**, sacadas del enrutador y no de una lista escrita a mano.
- **Aprobado cuando:** ninguna responde, salvo las dos declaradas abiertas. **Es el criterio que decide.**

### CA-02 — Entrar lleva a donde se iba

```gherkin
Dado que se pidió una pantalla sin haber entrado
Cuando se entra
Entonces se llega a esa pantalla, no a la portada
```

**Cómo validarlo:** pidiendo el tablero, entrando, y mirando dónde queda.
- **Aprobado cuando:** queda en el tablero.

### CA-03 — Un intento fallido no dice cuál dato estuvo mal

```gherkin
Dada una cuenta que existe con la contraseña equivocada
Y una cuenta que no existe con cualquier contraseña
Cuando se intentan las dos
Entonces las dos reciben el mismo mensaje
```

**Cómo validarlo:** probando los dos casos.
- **Aprobado cuando:** el mensaje es el mismo. Decir «esa cuenta no existe» confirma qué cuentas hay.

### Criterios transversales

- **La contraseña no aparece en la respuesta ni se guarda en claro.**

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Seguridad | La contraseña nunca queda escrita en claro (`00·N6`) |
| Mantenibilidad | Una pantalla nueva nace protegida |

---

## 6. Diseño y referencias

- Funcionalidad `F-036` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- La sección 8 del [diseño](../../../../cvds/diseno/README.md), rehecha el 2026-09-02.
- [Especificación del módulo Acceso](../../../acceso/spec.md).

---

## 7. Tareas técnicas derivadas

1. Instalar `django.contrib.auth` con su middleware.
2. El middleware que exige haber entrado, con su lista corta de abiertas.
3. La pantalla de entrar, con el mensaje único.
4. La orden para crear cuentas, que pide la contraseña sin mostrarla.
5. Que la barra de arriba diga quién entró.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [AA-EP-022-HU-001-sin-entrar-no-se-ve-nada](AA-EP-022-HU-001-sin-entrar-no-se-ve-nada/estado-fase.md) | Los tres CA | Cerrada el 2026-09-02: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-001`: los permisos cuelgan del modelo de Proyecto |
| **Riesgo 1** | **Que una pantalla nueva nazca abierta.** Middleware, no decorador |
| **Riesgo 2** | Que el error confirme qué cuentas existen. Un solo mensaje |
| **Riesgo 3** | Que se pierdan las cuentas al borrar la base. **Se acepta y se declara** |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ El diseño rehizo su sección 8.
- ☑ La épica aprobada el 2026-09-02.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado contra todas las rutas registradas.
- ☑ Comprobado que la contraseña no se guarda en claro.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | Lo trae Django |
| Negociable | Sí | Qué queda abierto se puede ajustar, y se lee en una lista |
| Valiosa | Sí | Sin ella, `RNF-09` es el día en que todo queda abierto |
| Estimable | Sí | Es instalar y conectar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se pide una dirección sin entrar y se mira |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-02 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
