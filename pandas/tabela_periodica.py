# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:51:54 2024.

@author: Rogerio
"""
import pandas as pd

# Carregando dados
df = pd.read_excel("tabela_periodica.xlsx")

#
# Breve sumário
#
print("#\n# Breve sumário\n#")

# Total de linhas
total_linhas = len(df)
print(f"- Total de linhas: {total_linhas}")

# Grupos dos elementos
grupos_elementos = set()
for grupo in list(df["GroupBlock"]):
    grupos_elementos.add(grupo)
print(f"- Lista de grupos de elementos.: {grupos_elementos}")

#
# Estatísticas
#
print("\n#\n# Estatísticas para algumas colunas\n#")

# media
print("- Média")
massa_atomica = df["AtomicMass"].mean()
print(f"  + Massa atômica.....: {massa_atomica}")
ponto_de_fusao = df["MeltingPoint"].mean()
print(f"  + Ponto de fusão....: {ponto_de_fusao}")
ponto_de_ebulicao = df["BoilingPoint"].mean()
print(f"  + Ponto de ebulição.: {ponto_de_ebulicao}")

# Distribuição dos elementos nos grupos

