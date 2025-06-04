import pandas as pd
import matplotlib.pyplot as plt

# Ler arquivos CSV
clientes = pd.read_csv('dados/clientes.csv')
produtos = pd.read_csv('dados/produtos.csv')
vendas = pd.read_csv('dados/vendas.csv')

# Calcular total vendido por cliente
vendas_cliente = vendas.groupby('id_cliente')['quantidade'].sum().reset_index()
vendas_cliente = vendas_cliente.merge(clientes, on='id_cliente', how='left')
vendas_cliente = vendas_cliente.fillna({'nome': 'Desconhecido'})

# Calcular total vendido por produto
vendas_produto = vendas.groupby('id_produto')['quantidade'].sum().reset_index()
vendas_produto = vendas_produto.merge(produtos, on='id_produto', how='left')
vendas_produto = vendas_produto.fillna({'nome_produto': 'Desconhecido'})

# Gráfico vendas por cliente
plt.figure(figsize=(8, 5))
plt.bar(vendas_cliente['nome'], vendas_cliente['quantidade'], color='skyblue')
plt.title('Total de Vendas por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico vendas por produto
plt.figure(figsize=(8, 5))
plt.bar(vendas_produto['nome_produto'], vendas_produto['quantidade'], color='lightgreen')
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
