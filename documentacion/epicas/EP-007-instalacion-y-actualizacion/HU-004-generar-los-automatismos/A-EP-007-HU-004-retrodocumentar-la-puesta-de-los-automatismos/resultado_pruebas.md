# Resultado de pruebas — Fase A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-004-retrodocumentar-la-puesta-de-los-automatismos` |
| **HU** | [HU-004](../HU-004-generar-los-automatismos.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-007-HU-004 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Proyectos temporales con git, instalados de verdad. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Los seis enganches quedan registrados en nueve momentos, no se duplican al reinstalar, y ninguno detiene la sesión cuando no encuentra nada que hacer.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Un proyecto instalado de verdad | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-01 | Alta | Los momentos declarados en los ajustes | Aprobado | EV-02 |
| [CP-003](plan_pruebas.md) | CA-01 | Crítica | Los enganches sobre una carpeta sin nada instalado | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-02 | Alta | La tabla de los seis, y una segunda instalación | Aprobado | EV-02 |

---

### Detalle de CP-001 y CP-002 — Los seis enganches, y cuándo corre cada uno

**Los seis quedan registrados, en nueve momentos:** hay tres que corren en más de uno.

| Enganche | Cuándo corre | Qué hace | Si falla |
|---|---|---|---|
| `hook_sesion.py` | Al abrir la sesión | Entrega las reglas que rigen y el aviso de versión | La sesión abre sin las reglas puestas |
| `hook_recuerdos.py` | Al abrir la sesión · al escribir un archivo | Recoge el almacén local hacia el repositorio | Quedan dos copias del mismo recuerdo |
| `hook_resumen.py` | Al abrir la sesión · en cada mensaje | Crea el resumen del día y avisa si sigue vacío | El resumen no nace solo |
| `hook_historico.py` | En cada mensaje · al terminar la respuesta | Escribe la transcripción con la hora del reloj | Se pierde la sesión: el chat se borra y el repositorio no la tiene |
| `hook_checklist.py` | En cada mensaje | Avisa qué le falta a la instalación | Nadie se entera de una instalación incompleta |
| `hook_md.py` | Al escribir un archivo | Comprueba el documento recién escrito | El documento mal formado pasa sin aviso |

**La fila de `hook_historico.py` es la que más pesa:** es el único cuyo fallo **pierde información que no se puede reponer**. Los demás dejan de ayudar; ese destruye.

---

### Detalle de CP-003 — Un enganche que se cae no detiene el trabajo

Se corrieron cuatro enganches contra una **carpeta vacía**, sin nada instalado, que es el escenario en que más fácil revientan: no hay `historico-chat/`, ni ajustes, ni reglas.

| Enganche | Código de salida |
|---|---|
| `hook_sesion.py` | **0** |
| `hook_historico.py` | **0** |
| `hook_recuerdos.py` | **0** |
| `hook_resumen.py` | **0** |

**Los cuatro terminan en 0 y no escriben nada.** Es la propiedad que hace que instalar el estándar sea seguro: un enganche que reventara al abrir la sesión dejaría el proyecto inutilizable, y el usuario no tendría cómo saber que la causa fue la instalación.

> **Este caso ya destapó algo esta misma sesión.** `hook_resumen.py` era el único de los seis que no preparaba su salida, y con la salida en una tubería su texto no se podía ni decodificar. Se corrigió en la 23.2.1, y nació la prueba que recorre los seis para que la lista no vuelva a quedar coja.

---

### Detalle de CP-004 — No se duplican ni se pisa lo del proyecto

| Qué se probó | Qué salió |
|---|---|
| Instalar dos veces y comparar los ajustes | **Idénticos**: ningún enganche duplicado |
| Ruta con espacios | La ruta generada funciona igual |

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Cuántos enganches y en qué momentos | Leyendo `.claude/settings.json` del proyecto instalado | **6 enganches · 9 registros · 4 momentos** |
| 2 | Que ninguno reviente sin nada instalado | Corriéndolos contra una carpeta vacía | Los cuatro en 0 |
| 3 | Que no se dupliquen | Instalando dos veces | Idénticos |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 328 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-004-generar-los-automatismos.md#ca-01--los-automatismos-quedan-puestos-y-funcionando) | CP-001, CP-002, CP-003 | Los seis registrados en nueve momentos, y ninguno detiene la sesión | Sí |
| [CA-02](../HU-004-generar-los-automatismos.md#ca-02--no-se-duplican-ni-se-pisa-lo-del-proyecto) | CP-004 | Dos instalaciones dejan los ajustes idénticos | Sí |
| Transversal · Límites | Prueba propia, fuera del plan | El enganche corre contra un proyecto sin nada y termina en 0 | Sí |
| Transversal · Compatibilidad | Prueba propia, fuera del plan | La ruta generada funciona con espacios | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Enganches registrados | Los 6 | **6**, en 9 momentos | Sí |
| Enganches duplicados al reinstalar | **0** | **0** | Sí |
| Enganches que detienen la sesión al fallar | **0** | **0** | Sí |
| Tabla de los seis, con su momento y su fallo | Escrita | Escrita, en §2 | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los dos criterios quedaron verificados y los dos transversales también. Lo que más importaba comprobar es el CA-01 en su parte silenciosa: **ningún enganche detiene el trabajo cuando no encuentra nada que hacer**. Se probó contra una carpeta vacía, que es donde revientan, y los cuatro terminan en 0. Y quedó escrita la tabla de los seis con lo que pasa si cada uno falla — que es el dato que faltaba para saber cuál duele más.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `GenerarLosAutomatismos`: 4 pruebas, en verde |
| EV-02 | La tabla de los seis | §2 de este documento |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 328 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
