import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/dados_vendas.csv')

# Análise 1: Faturamento por cidade
faturamento_cidade = df.groupby('cidade')['valor_compra'].sum().reset_index()

print("\nFaturamento por cidade:")
print(faturamento_cidade)

# Análise 2: Média de compra por forma de pagamento
media_pagamento = df.groupby('forma_pagamento')['valor_compra'].mean().reset_index()

print("\nMédia de compra por forma de pagamento:")
print(media_pagamento)

# Salvar os resultados
faturamento_cidade.to_csv('dados/faturamento_cidade.csv', index=False)
media_pagamento.to_csv('dados/media_pagamento.csv', index=False)

print("\nArquivos salvos com sucesso!")
