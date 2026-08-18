# Resultado de pruebas — Fase A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |
| **HU** | [HU-003](../HU-003-disparo-al-escribir-un-archivo.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-005-HU-003 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Carpetas temporales, con el enganche corrido como orden del sistema. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 2 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). El disparo corre en el momento y calla con lo que no le toca. Lo que falla es el **CA-03**: pide que el hallazgo grave **detenga** y el resto avise, y hoy **todo avisa**.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Un `.md` con un enlace roto | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-02 | Alta | Un `.py`, que no le toca | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-03 | Crítica | Una falla y un aviso | **Falla** | EV-01 |

---

### Detalle de CP-001 y CP-002 — Corre en el momento, y calla con lo que no le toca

| Qué se probó | Qué salió |
|---|---|
| Un `.md` con un enlace a un archivo que no existe | **Avisa en el momento**, nombrando el archivo que falta |
| Un `.py` recién escrito | **Calla**, y el enganche **corrió igual**: termina en 0 sin decir nada |

**El segundo caso comprueba dos cosas a la vez, y la segunda es la que importa.** Que calle y que no se haya ejecutado se ven idénticos desde fuera. El caso mira el código de salida para separarlos: si el enganche no hubiera corrido, no habría código que mirar.

**Por qué avisar en el momento y no al cerrar:** un enlace roto avisado tres horas después ya se copió a otros documentos.

---

### Detalle de CP-003 — Qué hace hoy con una falla y con un aviso

**Hace lo mismo con las dos: avisar.** El CA-03 dice «el hallazgo grave detiene; el resto avisa», y hoy el enganche informa y el trabajo sigue en los dos casos.

**No es un descuido pequeño.** Lo que la HU quería es que un documento con un incumplimiento grave no se pueda dejar así: que el trabajo se detenga hasta arreglarlo. Sin eso, el aviso depende de que alguien lo lea — y en este mismo repositorio hay constancia de un aviso ignorado durante una sesión entera: `00·ID8`, el 2026-08-14, llegaba completa y se incumplió igual.

Es el defecto `D-01`.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que calle con lo que no le toca **y haya corrido** | Mirando salida y código de salida | Salida vacía, código 0 |
| 2 | Que no reviente con un archivo que ya no está | Disparándolo sobre una ruta inexistente | No revienta |
| 3 | Cuánto tarda | Cronometrando el disparo | **Por debajo de 5 s**, medido |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 348 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **Nada detiene.** El CA-03 pide que el hallazgo grave detenga el trabajo, y hoy avisa igual que el resto. Un aviso que nadie lee es lo mismo que no avisar | Escrito en [`automatismos/spec.md`](../../../../automatismos/spec.md) §4.3. El arreglo toca `hook_md.py`, que §2.1 del [plan aprobado](plan_trabajo.md) no declara. Se propone |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los tres transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-003-disparo-al-escribir-un-archivo.md#ca-01--al-escribir-un-archivo-corre-la-comprobación) | CP-001 | Corre en el momento y nombra el problema | Sí |
| [CA-02](../HU-003-disparo-al-escribir-un-archivo.md#ca-02--lo-que-no-le-toca-se-ignora-en-silencio) | CP-002 | Calla, y se comprueba que **corrió igual** | Sí |
| [CA-03](../HU-003-disparo-al-escribir-un-archivo.md#ca-03--el-hallazgo-grave-detiene-el-resto-avisa) | CP-003 | **Todo avisa.** Nada detiene | **No** |
| Transversal · Rendimiento | Verificación 3 | Por debajo de 5 s, medido | Sí |
| Transversal · Errores | Verificación 2 | El archivo que ya no está no lo revienta | Sí |
| Transversal · Reversibilidad | — | **No aplica hoy**: como nada detiene, no hay forma de dejar un archivo a medias | N/A |

**El que no cumple:** el **CA-03**. Se traslada a una fase `B-EP-005-HU-003`.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los tres transversales | Sí |
| Casos ejecutados | 3 de 3 | 3 de 3 | Sí |
| Archivos que no le tocan y produjeron ruido | **0** | **0** | Sí |
| Tiempo del disparo | Que no se note | Por debajo de 5 s | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el disparo funciona y está bien pensado en lo que hace: avisa en el momento —no al cerrar, cuando el enlace roto ya se copió a otros documentos— y calla con lo que no le toca sin dejar de ejecutarse. Pero el CA-03 pide que el hallazgo grave **detenga**, y hoy no detiene nada. La diferencia importa: un aviso depende de que alguien lo lea, y este repositorio tiene constancia de uno ignorado durante una sesión entera.

**Qué falta para que cumpla:** que el hallazgo de severidad falla detenga la escritura (`D-01`). Toca `hook_md.py`, que el plan aprobado no declara: **pide una fase `B-EP-005-HU-003`**.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `DisparoAlEscribirUnArchivo`: 4 pruebas, en verde |
| EV-02 | Lo escrito | [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md) §4.3 |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 348 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
