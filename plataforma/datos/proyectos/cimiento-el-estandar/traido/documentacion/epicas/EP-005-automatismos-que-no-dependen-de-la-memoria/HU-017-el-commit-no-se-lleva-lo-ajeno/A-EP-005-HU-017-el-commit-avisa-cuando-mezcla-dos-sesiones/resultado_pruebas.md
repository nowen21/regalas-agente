# Resultado de Pruebas — Fase A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-017-el-commit-avisa-cuando-mezcla-dos-sesiones` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), PP-A-EP-005-HU-017 v1.0 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Resumen de la ejecución

| Métrica | Meta | Resultado |
|---|---|---|
| Exigencias con al menos un caso | 4 de 4 | 4 de 4 |
| Casos en verde | 10 de 10 | 10 de 10 |
| Casos de lo que NO debe avisar | 5 o más | 5 de 10 |
| Suites vecinas que se rompen | 0 | 0 |

---

## 2. Ejecución caso por caso

| Caso | Qué salió | Concepto |
|---|---|---|
| CP-001 | Un aviso, severidad de aviso, con «2 sesiones» en el texto | Pasa |
| CP-002 | El mensaje nombra el archivo de la sesión ajena | Pasa |
| CP-003 | Silencio | Pasa |
| CP-004 | Silencio | Pasa |
| CP-005 | Silencio | Pasa |
| CP-006 | Silencio | Pasa |
| CP-007 | Avisa, como debe | Pasa |
| CP-008 | El registro queda vacío | Pasa |
| CP-009 | El registro queda vacío y no se levanta ninguna excepción | Pasa |
| CP-010 | Una sola entrada | Pasa |

**Corrida:** `python -m unittest discover -s validadores/tests -p "test_dos_sesiones_no_se_pisan.py"`, 10 pruebas, 0,07 s, todas en verde.

---

## 3. Verificaciones manuales

Se corrió el subcomando contra este repositorio con el árbol como estaba: `validar.py sesiones` devolvió «sin incumplimientos», que es lo correcto porque no había nada preparado.

**Las suites vecinas**, que son las que dependen de lo que la fase toca:

| Suite | Por qué se corre | Resultado |
|---|---|---|
| `test_instalar_marcadores` | El `pre-commit` que escribe el instalador gana una línea | 6 en verde |
| `test_instalar_reparar` | Ídem | 7 en verde |
| `test_la_corrida_completa_en_una_linea` | `validar.py` gana un subcomando | 7 corridas, 2 fallas **previas**: las mismas dos que fallaban antes de esta fase |

---

## 4. Defectos encontrados

Ninguno propio.

**Lo que sí hubo que decidir en marcha:** el subcomando nuevo entraba por defecto en la corrida completa de `validar.py`, donde no tiene nada que mirar porque fuera de la hora del commit no hay nada preparado. Se declaró fuera, con su motivo escrito, que es como esta casa deja constancia de lo que no corre y por qué.

---

## 5. Veredicto por criterio de aceptación

| Exigencia | Casos | Concepto |
|---|---|---|
| CA-01 | CP-001 | Cumple |
| CA-02 | CP-002 | Cumple |
| CA-03 | CP-003 a CP-007 | Cumple |
| Límites | CP-008, CP-009, CP-010 | Cumple |

## 5.1 Lo que el plan exigía

Se cumplió tal como estaba escrito. El plan de esta fase sí se escribió antes de tocar nada, a diferencia del de la fase de los moldes, que quedó anotado como incumplimiento en su propio documento.

**Lo que no se pudo probar de verdad:** que el caso del 2026-08-22 habría avisado. Para comprobarlo haría falta reproducir dos sesiones reales commiteando a la vez, y eso no se puede montar en una prueba. Lo que sí se probó es la decisión que el guardián toma con esos datos, que es lo que estaba en la mano.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios quedaron en verde, cinco de los diez casos comprueban que el aviso no salte donde no debe, y las suites vecinas no perdieron ninguna prueba que antes pasara.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El módulo y el subcomando | [`validadores/sesiones.py`](../../../../../validadores/sesiones.py) |
| EV-02 | El cableado | [`adaptadores/claude-code/hook_md.py`](../../../../../adaptadores/claude-code/hook_md.py), [`validadores/instalar.py`](../../../../../validadores/instalar.py), `.gitignore` |
| EV-03 | Las pruebas | [`test_dos_sesiones_no_se_pisan.py`](../../../../../validadores/tests/test_dos_sesiones_no_se_pisan.py), 10 en verde |

---

## 8. Ciclos anteriores

Ninguno.
