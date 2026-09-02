# Resultado de Pruebas — Fase `B-EP-007-HU-002-el-registro-de-version-se-anuncia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-007-HU-002-el-registro-de-version-se-anuncia` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el CA-02 se cumple. La simulación compara ahora la huella que
va a quedar y nombra el archivo del registro, así que ningún archivo aparece sin
haberse anunciado. El CA-01 sigue en pie: simular no escribe nada.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la clase en verde | 4 de 4 | **4 de 4** |
| Pruebas marcadas como fallo esperado | 0 | **0** |
| Archivos que aparecen sin anunciarse | 0 | **0** |

---

## 3. Resultado por caso

### CP-003 — Lo que muestra es lo que hace

```
Ran 4 tests in 3.941s
OK
```

**Los dos cambios hicieron falta, y por razones distintas.** Comparar la huella
prevista hace que la simulación **sepa** que va a registrar. Nombrar el archivo
hace que lo **diga**: el anuncio anterior nombraba la carpeta, y la prueba
compara nombres de archivo, así que con solo el primer cambio el criterio
seguía sin cumplirse.

**Resultado: pasa.**

### CP-002 — El modo que muestra no escribe ni un archivo

Sigue en verde. El arreglo toca la comparación y el texto del anuncio; no toca
nada que escriba.

**Resultado: pasa.**

### CP-004 — Un proyecto al día no anuncia trabajo

Sigue en verde. Cuando el proyecto está al día, la huella prevista es igual a la
que hay, y la simulación no inventa cambios.

**Resultado: pasa.**

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El defecto no era una mentira del anuncio

Vale dejarlo dicho porque cambia dónde se busca. La simulación no estaba
diciendo algo distinto de lo que iba a hacer: estaba comparando el proyecto
consigo mismo antes de tocarlo, y desde ahí **no había ningún cambio que ver**.
El anuncio era correcto sobre un estado que no era el que importaba.

### 4.2 Por qué el nombre se predice con la misma función que lo elige

Si el anuncio calculara el nombre por su cuenta, el día que cambie la forma del
nombre los dos se separan y vuelve el mismo defecto por otra puerta. Los dos
salen de `_nombre_libre`.

---

## 5. Defectos encontrados

**Ninguno nuevo.**

---

## 6. Evidencias

- `validadores/instalar.py`, `_huellas_previstas` y `registrar_version`
- `validadores/versiones.py`, `nombre_previsto`
- `validadores/pruebas.py`, clase `MostrarAntesDeHacer`
