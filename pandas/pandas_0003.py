import pandas as pd

# Importando dados de arquivo csv (tabela_periodica.csv)
# Origem dos dados: https://pubchem.ncbi.nlm.nih.gov/periodic-table/
df_geral = pd.read_csv("tabela_periodica.csv", sep=",")

#
# Criando um dataframe formado apenas por algumas colunas dos dados originais
df_colunas = df_geral[["AtomicNumber", "Symbol", "Name", "AtomicMass", "GroupBlock"]]

# Valores máximo e mínimo da coluna 'AtomicMass'
atomic_mass_max = df_colunas["AtomicMass"].max()
atomic_mass_min = df_colunas["AtomicMass"].min()

print("#\n# Resultados\n#")
print(f"Número de elementos..........: {len(df_colunas)}")
print(f"Maior valor de massa atômica.: {atomic_mass_max}")
print(f"Menor valor de massa atômica.: {atomic_mass_min}")
