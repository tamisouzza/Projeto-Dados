# processar_dados.py

import pandas as pd
import os

#  Criar a pasta de dados processados se não existir
if not os.path.exists('dados/processados'):
    os.makedirs('dados/processados')

# Ler os dados brutos
clientes = pd.read_csv('dados/clientes.csv')
produtos = pd.read_csv('dados/produtos.csv')
vendas = pd.read_csv('dados/vendas.csv')

#  Verificar dados
print("Clientes:\n", clientes.head())
print("Produtos:\n", produtos.head())
print("Vendas:\n", vendas.head())

#  Verificar dados nulos
print("\nDados nulos por coluna:\n")
print("Clientes:\n", clientes.isnull().sum())
print("Produtos:\n", produtos.isnull().sum())
print("Vendas:\n", vendas.isnull().sum())

# Tratamento de dados nulos
clientes.fillna({'email': 'sem_email@dominio.com'}, inplace=True)
produtos.fillna({'categoria': 'Não Informado'}, inplace=True)
vendas.dropna(inplace=True)

# Fazer um merge (junção) dos dados de vendas com clientes e produtos
vendas_merged = vendas.merge(clientes, on='id_cliente')
vendas_merged = vendas_merged.merge(produtos, on='id_produto')

#  Criar coluna de valor total da venda
vendas_merged['valor_total'] = vendas_merged['quantidade'] * vendas_merged['preco_unitario']

# Salvar dados processados
vendas_merged.to_csv('dados/processados/vendas_tratadas.csv', index=False)

print("\n✅ Dados processados e salvos em dados/processados/vendas_tratadas.csv")
