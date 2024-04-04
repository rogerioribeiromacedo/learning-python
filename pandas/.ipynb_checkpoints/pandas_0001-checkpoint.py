import pandas as pd

# Criando dataframe com alguns elementos da tabela periódica
df = pd.DataFrame(
    {"Simbolo": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"], 
     "Numero atômico": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     "Nome elemento": ["Hidrogênio", "Hélio", "Lítio", "Berílio", "Boro", "Carbono", "Nitrogênio", "Oxigênio", "Flúor", "Neônio"]}
)

# Exbibindo o dataframe
print(df)
