# Resultado de Pruebas — Fase `C-EP-004-HU-003-el-transversal-de-errores-se-vuelve-a-medir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-004-HU-003-el-transversal-de-errores-se-vuelve-a-medir` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-29 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** **el transversal de errores se cumple hoy**, comprobado ejecutándolo.
Lo que la fase `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` declaró en rojo el 2026-08-17 **era cierto
entonces**: los tres criterios numerados quedaron verificados, y lo que falló fue el transversal: un `.md` que no se podía decodificar **terminaba la corrida entera con un volcado de Python**. Lo resolvió después `B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida`, y hasta hoy nadie
había vuelto a mirarlo.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 2 de 2 | 2 de 2 |
| **Casos comprobados leyendo en vez de corriendo** | 0 | **0** |

---

## 3. Resultado por caso

### CP-001 — El criterio se cumple hoy

**Cómo se ejecutó.** Una carpeta con dos archivos: uno con bytes que no son UTF-8 y otro con dos rayas largas en prosa. La corrida tiene que terminar en 0, sin volcado, **y seguir contando las dos marcas del legible**.

**Qué salió:** termina en 0, sin volcado, y cuenta las 2 marcas del legible

**Resultado: pasa.**

### CP-002 — La medición no se da por buena de más

No basta con que no se caiga. Un programa que se traga el error y deja de mirar el resto también «no se cae», y sería peor: diría cero marcas sobre un árbol sin revisar.

**Resultado: pasa.** La medición está escrita de forma que el caso bueno solo no
alcanza para dar verde.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 Por qué esta fase existe, y no bastaba con anotarlo

El veredicto de la fase `A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo` **no se toca**: fue cierto el día que se
escribió, y reescribirlo borraría el rastro de que el criterio estuvo en rojo.

Pero **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). Sin una fase que
lo declare, la historia arrastra un «no cumple» que ya no existe, y quien lo lea
después va a buscar un trabajo que ya está hecho.

### 4.2 Rastros

Ninguno. Las carpetas temporales las borra el propio medidor, y no se tocó
ningún proyecto real.

---

## 5. Defectos encontrados

**Ninguno.**

---

## 6. Evidencias

- El medidor: `historico-chat/scripts/2026-08-29/medir-los-cinco-rojos.py`
- El generador de esta fase: `historico-chat/scripts/2026-08-29/cerrar-los-cinco-rojos.py`
- La fase que hizo el trabajo: `B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida`
