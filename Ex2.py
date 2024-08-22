import pandas as pd
import numpy as np


url = "https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv"


df = pd.read_csv(url, header=None)

# Verificar a quantidade de colunas e exibir as primeiras linhas para conferência
print(f"Quantidade de colunas no DataFrame original: {df.shape[1]}")
print(df.head())


df.columns = [
    'Área A',
    'Perímetro P',
    'Extensão do núcleo',
    'Largura',
    'Coeficiente de Assimetria',
    'Extensão do sulgo do núcleo',
    'Classe',
    'Coluna Extra 1',
    'Coluna Extra 2'
]


df = df.iloc[:, :6]  # Manter apenas as primeiras 6 colunas

# Remover as linhas com valores nulos
df = df.dropna()


df['Compactação'] = 4 * np.pi * df['Área A'] / (df['Perímetro P'] ** 2)


df.to_csv('seeds_final.csv', index=False)


print(df.head())