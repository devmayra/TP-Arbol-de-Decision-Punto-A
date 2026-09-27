import math

print("=" * 60)
print("ÁRBOL DE DECISIÓN - EMPRESA DE TELECOMUNICACIONES")
print("=" * 60)
print()

# ============================================================================
# OBJETIVO 1: CALCULAR ENTROPÍA DEL CONJUNTO ORIGINAL
# ============================================================================

print("OBJETIVO 1: ENTROPÍA DEL CONJUNTO ORIGINAL")
print("-" * 60)

# Datos del conjunto
total = 10
aceptaron = 5
no_aceptaron = 5

# Probabilidades
p_si = aceptaron / total
p_no = no_aceptaron / total

# Cálculo de entropía
H_original = - (p_si * math.log2(p_si) + p_no * math.log2(p_no))

print(f"Total de clientes: {total}")
print(f"Aceptaron (Sí): {aceptaron}")
print(f"No aceptaron (No): {no_aceptaron}")
print()
print(f"P(Sí) = {aceptaron}/{total} = {p_si}")
print(f"P(No) = {no_aceptaron}/{total} = {p_no}")
print()
print(f"H_original = -(P(Sí) × log₂(P(Sí)) + P(No) × log₂(P(No)))")
print(f"H_original = -({p_si} × {math.log2(p_si):.3f} + {p_no} × {math.log2(p_no):.3f})")
print(f"H_original = {H_original:.3f}")
print()
print()

# ============================================================================
# OBJETIVO 2: EVALUAR GANANCIA DE INFORMACIÓN PARA LOS ATRIBUTOS
# ============================================================================

print("OBJETIVO 2: GANANCIA DE INFORMACIÓN POR ATRIBUTO")
print("=" * 60)
print()

# ============================================================================
# ATRIBUTO 1: EDAD
# ============================================================================

print("ATRIBUTO 1: EDAD")
print("-" * 60)

# Subconjunto Joven (≤30): IDs 1, 3, 8
print("Subconjunto Joven (≤30): 3 clientes (IDs 1, 3, 8)")
total_joven = 3
si_joven = 0
no_joven = 3
p_si_joven = si_joven / total_joven if si_joven > 0 else 0
p_no_joven = no_joven / total_joven
H_joven = 0 if si_joven == 0 or no_joven == 0 else - (p_si_joven * math.log2(p_si_joven) + p_no_joven * math.log2(p_no_joven))
print(f"  Aceptó Sí: {si_joven}, No: {no_joven}")
print(f"  H_Joven = {H_joven:.3f}")
print()

# Subconjunto Adulto (31-50): IDs 2, 4, 6, 7, 9, 10
print("Subconjunto Adulto (31-50): 6 clientes (IDs 2, 4, 6, 7, 9, 10)")
total_adulto = 6
si_adulto = 4
no_adulto = 2
p_si_adulto = si_adulto / total_adulto
p_no_adulto = no_adulto / total_adulto
H_adulto = - (p_si_adulto * math.log2(p_si_adulto) + p_no_adulto * math.log2(p_no_adulto))
print(f"  Aceptó Sí: {si_adulto}, No: {no_adulto}")
print(f"  P(Sí) = {si_adulto}/{total_adulto} = {p_si_adulto:.3f}")
print(f"  P(No) = {no_adulto}/{total_adulto} = {p_no_adulto:.3f}")
print(f"  H_Adulto = {H_adulto:.3f}")
print()

# Subconjunto Mayor (>50): ID 5
print("Subconjunto Mayor (>50): 1 cliente (ID 5)")
total_mayor = 1
si_mayor = 1
no_mayor = 0
H_mayor = 0
print(f"  Aceptó Sí: {si_mayor}, No: {no_mayor}")
print(f"  H_Mayor = {H_mayor:.3f}")
print()

# Entropía ponderada - EDAD
print("Entropía ponderada:")
peso_joven = total_joven / total
peso_adulto = total_adulto / total
peso_mayor = total_mayor / total
H_ponderada_edad = (peso_joven * H_joven) + (peso_adulto * H_adulto) + (peso_mayor * H_mayor)
print(f"  Peso_Joven = {total_joven}/{total} = {peso_joven}")
print(f"  Peso_Adulto = {total_adulto}/{total} = {peso_adulto}")
print(f"  Peso_Mayor = {total_mayor}/{total} = {peso_mayor}")
print(f"  H_ponderada = ({peso_joven} × {H_joven:.3f}) + ({peso_adulto} × {H_adulto:.3f}) + ({peso_mayor} × {H_mayor:.3f})")
print(f"  H_ponderada = {H_ponderada_edad:.4f}")
print()

# Ganancia - EDAD
ganancia_edad = H_original - H_ponderada_edad
print(f"Ganancia (Edad) = {H_original:.3f} - {H_ponderada_edad:.4f} = {ganancia_edad:.3f}")
print()
print()

# ============================================================================
# ATRIBUTO 2: TIENE LÍNEA FIJA
# ============================================================================

print("ATRIBUTO 2: TIENE LÍNEA FIJA")
print("-" * 60)

# Subconjunto Línea fija = Sí: IDs 2, 4, 5, 7, 9
print("Subconjunto Línea fija = Sí: 5 clientes (IDs 2, 4, 5, 7, 9)")
total_si_linea = 5
si_linea_si = 5
no_linea_si = 0
H_linea_si = 0
print(f"  Aceptó Sí: {si_linea_si}, No: {no_linea_si}")
print(f"  H_Línea_Sí = {H_linea_si:.3f}")
print()

# Subconjunto Línea fija = No: IDs 1, 3, 6, 8, 10
print("Subconjunto Línea fija = No: 5 clientes (IDs 1, 3, 6, 8, 10)")
total_no_linea = 5
si_linea_no = 0
no_linea_no = 5
H_linea_no = 0
print(f"  Aceptó Sí: {si_linea_no}, No: {no_linea_no}")
print(f"  H_Línea_No = {H_linea_no:.3f}")
print()

# Entropía ponderada - LÍNEA FIJA
print("Entropía ponderada:")
peso_si_linea = total_si_linea / total
peso_no_linea = total_no_linea / total
H_ponderada_linea = (peso_si_linea * H_linea_si) + (peso_no_linea * H_linea_no)
print(f"  Peso_Sí = {total_si_linea}/{total} = {peso_si_linea}")
print(f"  Peso_No = {total_no_linea}/{total} = {peso_no_linea}")
print(f"  H_ponderada = ({peso_si_linea} × {H_linea_si:.3f}) + ({peso_no_linea} × {H_linea_no:.3f})")
print(f"  H_ponderada = {H_ponderada_linea:.4f}")
print()

# Ganancia - LÍNEA FIJA
ganancia_linea = H_original - H_ponderada_linea
print(f"Ganancia (Línea fija) = {H_original:.3f} - {H_ponderada_linea:.4f} = {ganancia_linea:.3f}")
print()
print()

# ============================================================================
# ATRIBUTO 3: USO DE DATOS
# ============================================================================

print("ATRIBUTO 3: USO DE DATOS")
print("-" * 60)

# Subconjunto Uso Bajo (≤3GB): IDs 1, 3, 8
print("Subconjunto Uso Bajo (≤3GB): 3 clientes (IDs 1, 3, 8)")
total_bajo = 3
si_bajo = 0
no_bajo = 3
H_bajo = 0
print(f"  Aceptó Sí: {si_bajo}, No: {no_bajo}")
print(f"  H_Bajo = {H_bajo:.3f}")
print()

# Subconjunto Uso Medio (3.1-6GB): IDs 2, 6, 7, 10
print("Subconjunto Uso Medio (3.1-6GB): 4 clientes (IDs 2, 6, 7, 10)")
total_medio = 4
si_medio = 2
no_medio = 2
p_si_medio = si_medio / total_medio
p_no_medio = no_medio / total_medio
H_medio = - (p_si_medio * math.log2(p_si_medio) + p_no_medio * math.log2(p_no_medio))
print(f"  Aceptó Sí: {si_medio}, No: {no_medio}")
print(f"  P(Sí) = {si_medio}/{total_medio} = {p_si_medio}")
print(f"  P(No) = {no_medio}/{total_medio} = {p_no_medio}")
print(f"  H_Medio = {H_medio:.3f}")
print()

# Subconjunto Uso Alto (>6GB): IDs 4, 5, 9
print("Subconjunto Uso Alto (>6GB): 3 clientes (IDs 4, 5, 9)")
total_alto = 3
si_alto = 3
no_alto = 0
H_alto = 0
print(f"  Aceptó Sí: {si_alto}, No: {no_alto}")
print(f"  H_Alto = {H_alto:.3f}")
print()

# Entropía ponderada - USO DE DATOS
print("Entropía ponderada:")
peso_bajo = total_bajo / total
peso_medio = total_medio / total
peso_alto = total_alto / total
H_ponderada_uso = (peso_bajo * H_bajo) + (peso_medio * H_medio) + (peso_alto * H_alto)
print(f"  Peso_Bajo = {total_bajo}/{total} = {peso_bajo}")
print(f"  Peso_Medio = {total_medio}/{total} = {peso_medio}")
print(f"  Peso_Alto = {total_alto}/{total} = {peso_alto}")
print(f"  H_ponderada = ({peso_bajo} × {H_bajo:.3f}) + ({peso_medio} × {H_medio:.3f}) + ({peso_alto} × {H_alto:.3f})")
print(f"  H_ponderada = {H_ponderada_uso:.4f}")
print()

# Ganancia - USO DE DATOS
ganancia_uso = H_original - H_ponderada_uso
print(f"Ganancia (Uso de datos) = {H_original:.3f} - {H_ponderada_uso:.4f} = {ganancia_uso:.3f}")
print()
print()

# ============================================================================
# RESUMEN DE RESULTADOS
# ============================================================================

print("=" * 60)
print("RESUMEN - GANANCIAS DE INFORMACIÓN")
print("=" * 60)
print()
print(f"Edad:          {ganancia_edad:.3f}")
print(f"Línea fija:    {ganancia_linea:.3f}")
print(f"Uso de datos:  {ganancia_uso:.3f}")
print()

# Identificar mejor atributo
ganancias = {
    'Edad': ganancia_edad,
    'Línea fija': ganancia_linea,
    'Uso de datos': ganancia_uso
}

mejor_atributo = max(ganancias, key=ganancias.get)
mejor_ganancia = ganancias[mejor_atributo]

print(f"✓ MEJOR ATRIBUTO: {mejor_atributo} (Ganancia = {mejor_ganancia:.3f})")
print()
print("=" * 60)
