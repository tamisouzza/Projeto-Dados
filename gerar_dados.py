import os
import pandas as pd

# Criar pasta 'dados' se não existir
if not os.path.exists('dados'):
    os.makedirs('dados')

# Dados de exemplo para clientes
clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3],
    'nome': ['Ana Silva', 'Bruno Costa', 'Carla Souza'],
    'email': ['ana@email.com', 'bruno@email.com', None]
})

# Dados de exemplo para produtos
produtos = pd.DataFrame({
    'id_produto': [101, 102, 103],
    'nome_produto': ['Produto A', 'Produto B', 'Produto C'],
    'categoria': ['Categoria 1', 'Categoria 2', None],
    'preco_unitario': [10.0, 20.5, 15.0]
})

# Dados de exemplo para vendas
vendas = pd.DataFrame({
    'id_venda': [1001, 1002, 1003],
    'id_cliente': [1, 2, 1],
    'id_produto': [101, 103, 102],
    'quantidade': [2, 1, 5]
})

# Salvar arquivos CSV na pasta dados
clientes.to_csv('dados/clientes.csv', index=False)
produtos.to_csv('dados/produtos.csv', index=False)
vendas.to_csv('dados/vendas.csv', index=False)

print("Arquivos clientes.csv, produtos.csv e vendas.csv criados na pasta dados.")