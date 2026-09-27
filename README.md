# TP 4 — Árbol de Decisión, Punto A: Empresa de Telecomunicaciones

## Materia: Procesamiento de Aprendizaje Automático

---

## Descripción

Implementación de un árbol de decisión para predecir si un cliente de una empresa de telecomunicaciones aceptará una oferta de plan de datos móviles, basado en atributos como edad, uso de datos y disponibilidad de línea fija.

## Objetivo

Construir un árbol de decisión calculando la entropía y ganancia de información de tres atributos diferentes, para identificar cuál es el mejor predictor y determinar las reglas de clasificación.

## Contenido del repositorio

- `Arbol_Decision_PuntoA.ipynb` - Notebook con resolución completa del ejercicio en formato markdown
- `README.md` - Este archivo

## Metodología

1. **Cálculo de entropía original** del conjunto de datos
2. **Evaluación de ganancia de información** para:
   - Edad (Joven ≤30, Adulto 31–50, Mayor >50)
   - Tiene línea fija (Sí/No)
   - Uso de datos (Bajo ≤3GB, Medio 3.1–6GB, Alto >6GB)
3. **Construcción del árbol** basado en el atributo con mayor ganancia
4. **Generación de reglas** de predicción

## Resultados clave

| Atributo | Ganancia |
|:--------:|:--------:|
| Edad | 0.450 |
| **Línea fija** | **1.0** |
| Uso de datos | 0.6 |

**Mejor atributo:** Línea fija (ganancia máxima = 1.0)

**Regla de predicción:**
- Si cliente tiene línea fija → Aceptará la oferta
- Si cliente no tiene línea fija → No aceptará la oferta

## Herramientas

- Jupyter Notebook
- Cálculos manuales de entropía e información ganada