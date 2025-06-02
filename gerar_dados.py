# gerar_dados.py

import pandas as pd

# Gerando um dataset falso de vendas
dados = {
    'id_cliente': [1, 2, 3, 4, 5],
    'cidade': ['SP', 'RJ', 'BH', 'POA', 'CUR'],
    'valor_compra': [150, 230, 99, 430, 120]
}

df = pd.DataFrame(dados)

print("Dados gerados:")
print(df)

# Salvando em CSV
df.to_csv('dados_vendas.csv', index=False)

print("Arquivo CSV criado com sucesso!")