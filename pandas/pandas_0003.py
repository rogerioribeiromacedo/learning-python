import pandas as pd

df = pd.read_excel("tabela_periodica.xlsx")

# Valores máximo e mínimo da coluna 'AtomicMass'
atomic_mass_max = df["AtomicMass"].max()
atomic_mass_min = df["AtomicMass"].min()

# Raio atômico
atomic_radius_max = df["AtomicRadius"].max()
atomic_radius_min = df["AtomicRadius"].min()

# Criando um 'set' com os elementos da coluna 'StandardState'
standard_state = set()
for i in list(df['StandardState']):
    standard_state.add(i)

print("#\n# Resultados\n#")
print(f"# - Número de elementos..........: {len(df)}")
print("# - Massa atômica:")
print(f"    + Maior valor de massa atômica.: {atomic_mass_max}")
print(f"    + Menor valor de massa atômica.: {atomic_mass_min}")
print("# - Raio atômico:")
print(f"    + Maior raio atômico...........: {atomic_radius_max}")
print(f"    + Menor raio atômico...........: {atomic_radius_min}")
print("# - Estados padrão:")
print(f"    + {standard_state}")
