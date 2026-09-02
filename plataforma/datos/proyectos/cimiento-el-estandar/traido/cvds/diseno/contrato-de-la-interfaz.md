# El contrato de la plataforma   ·   `[CAPA 3]`

**Para qué sirve este documento.** Qué se le puede pedir a la plataforma desde la misma máquina, qué devuelve, y qué se promete que no va a cambiar. **No se expone nada a la red** ([`DA-03`](decisiones-de-arquitectura.md)): este es el contrato de lo que corre en la propia máquina, y el que usa el agente al abrir sesión.

> **Escrito desde la propuesta**, igual que el resto de [cvds/README.md/](../README.md). Reescrito el 2026-08-24: la versión anterior describía un contrato de solo lectura.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. Qué es y qué no es este contrato

| Es | No es |
|---|---|
| Lo que la plataforma responde a quien se lo pida desde la misma máquina | Un servicio publicado: no escucha fuera de la máquina |
| El canal por el que el agente recibe las reglas y escribe lo que la sesión deja | Una forma de saltarse las aprobaciones: lo que las exige, las sigue exigiendo |
| Estable entre versiones menores | Inmutable: una versión mayor puede cambiarlo, y lo declara antes |

## 2. Lo que se puede pedir

| # | Qué se pide | Qué se recibe | Qué pasa si algo falta |
|---|---|---|---|
| 1 | Las reglas que rigen en un proyecto | Las vigentes, con la versión adoptada y si quedó atrás | Proyecto sin registrar: se responde que no está, con los que sí |
| 2 | El estado de un proyecto | Sus etapas, fases y qué falta aprobar | Ruta perdida: se responde lo guardado, con el aviso |
| 3 | La lista de proyectos | Todos, con su estado | Nunca falta: sin proyectos, se responde que no hay |
| 4 | Un documento | Su contenido, sus huecos y su estado de aprobación | Documento que figura y no está: se dice cuál falta y dónde debería estar |
| 5 | Guardar un documento | El documento guardado, y el registro de auditoría | Documento que no existe: no se crea a la fuerza, se dice |
| 6 | Registrar una aprobación | La firma guardada, con la huella del texto | Texto que cambió desde que se leyó: no se firma, y se dice |
| 7 | Abrir, avanzar o cerrar una fase | La fase en su estación nueva | Puerta sin cumplir: no avanza, y dice cuál falta |
| 8 | Escribir en la memoria | La anotación guardada | Anotación que corrige a otra: queda enlazada, y la anterior se marca |
| 9 | Consultar la memoria | Lo guardado que coincide | Nada coincide: se responde que no hay, y no se sugiere nada |
| 10 | Correr las comprobaciones | Qué cumple y qué no, con archivo y línea | Comprobación que no aplica ahí: lo dice, en vez de dar veredicto |
| 11 | Armar el expediente | El expediente, con lo que falta señalado | Documentos con huecos: se avisa antes de generar |
| 12 | Consultar la auditoría | Lo registrado, filtrado | Sin coincidencias: se responde que no hay |

## 3. Qué se promete que no cambia

| Promesa | Hasta cuándo |
|---|---|
| Los nombres con que se piden las doce cosas de arriba | Mientras no haya versión mayor |
| Que toda petición que cambia algo quede registrada en la auditoría | Siempre: es `DA-08` |
| Que lo que exige aprobación no avance sin ella | Siempre: es `DA-12` |
| Que la respuesta diga siempre qué falta, en vez de responder vacío | Siempre |
| Que funcione sin red | Mientras rija RNF-03 |

## 4. Qué NO se promete

- **Que la forma de la respuesta no crezca.** Se pueden agregar datos nuevos; lo que no se quita es lo que ya estaba.
- **Que responda rápido con cualquier tamaño.** Los únicos tiempos comprometidos son los de RNF-01 y RNF-02.
- **Que dos máquinas respondan lo mismo.** Cada una responde por su propio repositorio.

## 5. Cuando la plataforma no responde

| Qué pasa | Qué hace quien pide |
|---|---|
| La plataforma no está levantada | El agente lee la fuente en texto y avisa que trabaja sin ella: `DA-04` |
| La base no responde | Se leen los documentos igual; lo que no funciona es buscar |
| El generador falla | El texto sigue intacto: se vuelve a pedir cuando se corrija |

> **Ninguna de estas fallas pierde información.** Todo lo que la plataforma responde existe primero como texto, y sigue existiendo si ella se cae.

## 6. Lo que este contrato deja abierto

- **Qué se registra exactamente de una sesión del agente.** Es la duda 2 del análisis: hoy dice «se audita la acción», y falta acordar cuáles.
- **Si alguna petición podrá venir de otra máquina.** Hoy no, y el día que sí, hace falta decidir quién puede pedir qué.
