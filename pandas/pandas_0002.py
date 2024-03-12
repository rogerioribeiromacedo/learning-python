import pandas as pd

# Importando dados de arquivo csv (tabela_periodica.csv)
# Origem dos dados: https://pubchem.ncbi.nlm.nih.gov/periodic-table/
df = pd.read_csv("tabela_periodica.csv", sep=",")

# 
# Imprimindo as primeiras 12 linhas do dataframe (apenas algumas colunas)
print("#\n# Imprimindo as primeiras 12 linhas do dataframe\n#")
print(df[["AtomicNumber", "Symbol", "Name", "AtomicMass"]].head(12))
print("")

# 
# Imprimindo as 12 últimas linhas do dataframe (apenas alguns colunas)
print("#\n# Imprimindo as 12 últimas linhas do dataframe\n#")
print(df[["AtomicNumber", "Symbol", "Name", "AtomicMass"]].tail(12))
print("")
