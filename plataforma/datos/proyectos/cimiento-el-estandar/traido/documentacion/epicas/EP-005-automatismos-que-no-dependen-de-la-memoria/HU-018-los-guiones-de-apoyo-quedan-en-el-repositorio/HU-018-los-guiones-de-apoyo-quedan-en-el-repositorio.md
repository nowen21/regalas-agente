# HU-018 — Que los guiones de apoyo queden en el repositorio, sin depender de que el agente se acuerde

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-018 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Enganches |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien va a preguntar dentro de un mes con qué se hizo un cambio grande
- **Quiero** que el guion que lo aplicó esté en el repositorio y no en una carpeta temporal
- **Para** que el resultado y el **cómo** se guarden juntos, en vez de que uno sobreviva y el otro se borre

---

## 3. Contexto y descripción

**La regla existe, es del usuario, y se dejó de cumplir al día siguiente de precisarla.**

Se fijó el 2026-08-20. El usuario la precisó el 2026-08-22 con estas palabras: *«nada se debe escribir por fuera, todo debe quedar en historico-chat»*. **Se incumplió desde el 2026-08-24**, cuatro días seguidos:

| Día | Guiones escritos fuera del repositorio |
|---|---|
| 2026-08-24 | 1 |
| 2026-08-25 | 15 |
| 2026-08-26 | 14 |
| 2026-08-27 | 8 |

**Treinta y ocho**, más dos clones enteros de la plataforma con su entorno virtual — 6.831 archivos. Lo destapó el usuario preguntando por tercera vez.

### El daño no es de orden

El **resultado** de cada cambio quedaba versionado y **el cómo se borraba con el temporal**. Cuatro días de sabotajes, guiones de cierre y mediciones sin respuesta a *«¿con qué se hizo esto?»* — que es la segunda vez que esa pregunta se queda sin respuesta, y la primera es la que originó la regla.

### Por qué no basta con haberlo escrito

**La regla vive en un recuerdo, y nada la hace cumplir.** Un recuerdo se consulta cuando uno se acuerda de consultarlo, que es justo cuando ya no hace falta.

Y hay algo peor que el olvido: **la herramienta ofrece una carpeta temporal en cada sesión y la nombra como el sitio recomendado**. El camino cómodo apunta al lado contrario de la regla, y ahí no gana la buena intención.

**Es el argumento de este estándar aplicado a sí mismo:** lo que depende de que el agente se acuerde se incumple sin que nadie se entere.

### Lo que ya existe, y lo que falta

| Pieza | Estado |
|---|---|
| La prohibición: [`04·S9`](../../../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas) — «el agente escribe solo dentro de la carpeta del proyecto» | **Ya está** |
| **Dónde sí van** los guiones de apoyo | **Falta**: solo vive en un recuerdo |
| Algo que lo haga cumplir | **Falta** |
| El canal para hacerlo cumplir: enganches en `PostToolUse` sobre `Write\|Edit` | **Ya está**, y ocho enganches lo usan |
| El precedente: `hook_recuerdos.py` mueve al repositorio lo que la herramienta guardó afuera | **Ya está** |

### 3.1 Reglas de negocio

| ID | Regla | De dónde baja |
|---|---|---|
| RN-01 | Un guion de apoyo se escribe en `historico-chat/scripts/AAAA-MM-DD/`, y se queda ahí versionado | El usuario, 2026-08-22 |
| RN-02 | **Escribir** fuera del proyecto se avisa en el momento; **leer** fuera no | `04·S9`, que ya lo separa así |
| RN-03 | El aviso dice **dónde debía ir**, no solo que está mal | Un aviso que no dice qué hacer se aprende a ignorar |
| RN-04 | El enganche **avisa, no mueve ni borra** | `EP-004 §10.2`. Mover un archivo que el agente acaba de escribir rompe lo que estaba haciendo |
| RN-05 | La ruta del proyecto se resuelve **antes de comparar**, para que un enlace o un `..` no la burlen | Una comprobación de rutas que compara texto se engaña sola |
| RN-06 | La carpeta del día lleva su `README.md` diciendo qué hizo cada guion | El README madre de `historico-chat/scripts/` ya lo pide |

### 3.2 Supuestos

- El enganche recibe la ruta escrita en `tool_input.file_path`, que es lo que ya usan los ocho enganches del repositorio. **Comprobado leyendo `hook_md.py`**, no supuesto.

### 3.3 Fuera de alcance

- **Los 38 guiones que estaban afuera.** Se trajeron el 2026-08-27 con su fecha real y su README. Eso tapó los casos, no la causa.
- **Los dos clones de la plataforma**, 6.831 archivos con un entorno virtual. Lo que valía era el resultado del experimento, ya escrito en su fase.
- **Lo que se escribe por `Bash`.** El enganche ve la ruta de `Write` y `Edit`; una redirección dentro de un comando no la ve. Se dice acá para que la cobertura no se lea de más.
- **Mover o borrar nada.** El enganche avisa.

---

## 4. Criterios de aceptación

### CA-01 — Escribir fuera del proyecto avisa en el momento

```gherkin
Dado que el agente escribe un archivo fuera de la carpeta del proyecto
Cuando termina la herramienta de escritura
Entonces aparece un aviso que nombra la ruta escrita
Y dice dónde debía ir
```

**Cómo validarlo:**
1. Correr el enganche con una entrada que declare una ruta de la carpeta temporal del sistema.
2. Leer la salida. Resultado esperado: un aviso con la ruta, y `historico-chat/scripts/AAAA-MM-DD/` nombrado.
3. Comprobar que el archivo **no se movió ni se borró**.
- **Aprobado cuando:** avisa, nombra el destino, y no toca nada.

### CA-02 — Escribir dentro del proyecto no avisa

```gherkin
Dado que el agente escribe un archivo del proyecto
Cuando termina la herramienta de escritura
Entonces no aparece ningún aviso
```

**Cómo validarlo:**
1. Correr el enganche con una ruta de `documentacion/`, otra de `validadores/` y otra de `historico-chat/scripts/`.
2. Resultado esperado: **silencio en las tres**.
3. Correr con una ruta relativa y con una que traiga `..` y termine dentro del proyecto.
4. Resultado esperado: silencio también.
- **Aprobado cuando:** ninguna ruta de dentro produce aviso.

**Este es el criterio que decide si sirve.** Un enganche que avisa en cada escritura se apaga el mismo día, y entonces no queda nada.

### CA-03 — La ruta se resuelve antes de comparar

```gherkin
Dado un camino que sale del proyecto y vuelve a entrar
Cuando se comprueba si está dentro
Entonces se compara la ruta ya resuelta, no el texto
```

**Cómo validarlo:**
1. Pasar una ruta con `..` que termine **dentro** del proyecto. Resultado esperado: silencio.
2. Pasar una que empiece dentro y termine **fuera**. Resultado esperado: avisa.
3. Pasar una ruta que empiece con el nombre del proyecto pero sea otra carpeta hermana. Resultado esperado: **avisa**.
- **Aprobado cuando:** ninguno de los tres se decide comparando texto.

**El paso 3 es el que se cuela.** `C:/proyecto` y `C:/proyecto-viejo` comparten prefijo, y comparar texto daría el segundo por dentro.

### CA-04 — La regla dice dónde van los guiones

```gherkin
Dado que `04·S9` dice dónde NO se escribe
Cuando alguien busca dónde SÍ van los guiones de apoyo
Entonces lo encuentra en `base/`, no en un recuerdo
```

**Cómo validarlo:**
1. Buscar en `base/` la ruta `historico-chat/scripts/`. Resultado esperado: aparece, con su regla.
2. Comprobar que la regla declara su dependencia con `04·S9` y no la repite.
3. Correr `validar.py metareglas`. Resultado esperado: sin incumplimientos.
- **Aprobado cuando:** la regla existe, pasa su propio checklist, y no duplica `S9`.

### CA-05 — El enganche no rompe nada si algo falta

```gherkin
Dado que el enganche recibe una entrada sin ruta, o rota
Cuando corre
Entonces no revienta ni bloquea la escritura
```

**Cómo validarlo:**
1. Entrada sin `file_path`. Resultado esperado: silencio, código de salida normal.
2. Entrada que no es JSON. Resultado esperado: silencio.
3. Ruta vacía. Resultado esperado: silencio.
- **Aprobado cuando:** ninguna entrada mala detiene el trabajo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Corre en cada escritura: no puede leer el árbol ni abrir archivos |
| RNF-02 | **No estorbar** | Un fallo del enganche no detiene la escritura |

---

## 6. Diseño y referencias

- **Dónde vive la lógica:** `validadores/rutas_fuera.py`, agnóstico de la herramienta.
- **Dónde habla con la herramienta:** `adaptadores/claude-code/hook_rutas.py`, igual que los otros ocho.
- **La regla que ya existe:** [`04·S9`](../../../../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto--solo-autorizadas-exactas).
- **El precedente:** `hook_recuerdos.py`, que trae al repositorio lo que la herramienta guardó afuera.

---

## 7. Tareas técnicas derivadas

- [ ] «Backend» Decir si una ruta resuelta está dentro del proyecto.
- [ ] «Backend» El enganche, que lee la ruta y avisa con el destino.
- [ ] «Documentación» La regla en `base/`, declarando su dependencia con `S9`.
- [ ] «Documentación» Que el instalador la enganche, como los otros ocho.
- [ ] «Pruebas» Los cinco criterios, con el caso de las carpetas hermanas.
- [ ] «Documentación» Entrada en el `CHANGELOG` y subir `VERSION`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera`](A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera/) | CA-01 a CA-05 | (vacío) | [plan_trabajo](A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera/plan_pruebas.md) | | En curso |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que avise de más y se aprenda a ignorar | `CA-02`, con las rutas de dentro. Es el criterio que decide si sirve |
| Riesgo | Que se compare texto y una carpeta hermana pase por dentro | `CA-03` paso 3 |
| Riesgo | Que un fallo del enganche detenga el trabajo | `CA-05` y `RNF-02` |
| Límite | Lo escrito por `Bash` no se ve | Declarado en el §3.3. La cobertura no se lee de más |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible — no aplica: no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [x] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código implementado y revisado
- [ ] Pruebas unitarias escritas y en verde
- [ ] Criterios de aceptación validados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas — no aplica
- [ ] Aceptada por el Product Owner

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | El canal de enganches ya existe |
| **N**egociable | ☑ | El texto del aviso se puede discutir sin tocar el objetivo |
| **V**aliosa | ☑ | Cuatro días de incumplimiento medidos, y la pregunta «con qué se hizo esto» sin respuesta dos veces |
| **E**stimable | ☑ | Una función, un enganche, una regla y sus pruebas |
| **S**mall (pequeña) | ☑ | Una sola fase |
| **T**esteable | ☑ | Los cinco criterios se comprueban dándole entradas al enganche |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-27 | Agente, con el usuario | Creación de la HU. Sale del [pendiente 89](../../../../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md), con las salidas **1 y 3** aprobadas y la **2** —un validador que compara al cierre— dejada fuera: detecta lo que la 1 evita |
