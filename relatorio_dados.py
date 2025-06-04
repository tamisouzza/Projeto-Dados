import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# --- Função para criar gráficos e salvar ---
def criar_grafico_barras(df, coluna_nome, coluna_valor, titulo, nome_arquivo, cor):
    plt.figure(figsize=(8, 5))
    plt.bar(df[coluna_nome], df[coluna_valor], color=cor)
    plt.title(titulo, fontsize=14)
    plt.xlabel(coluna_nome.capitalize(), fontsize=12)
    plt.ylabel('Quantidade Vendida', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(nome_arquivo)
    plt.close()

# --- Preparar dados ---
clientes = pd.read_csv('dados/clientes.csv')
produtos = pd.read_csv('dados/produtos.csv')
vendas = pd.read_csv('dados/vendas.csv')

vendas_cliente = vendas.groupby('id_cliente')['quantidade'].sum().reset_index()
vendas_cliente = vendas_cliente.merge(clientes, on='id_cliente', how='left').fillna({'nome': 'Desconhecido'})

vendas_produto = vendas.groupby('id_produto')['quantidade'].sum().reset_index()
vendas_produto = vendas_produto.merge(produtos, on='id_produto', how='left').fillna({'nome_produto': 'Desconhecido'})

# --- Criar gráficos ---
criar_grafico_barras(vendas_cliente, 'nome', 'quantidade', 'Total de Vendas por Cliente', 'vendas_cliente.png', 'skyblue')
criar_grafico_barras(vendas_produto, 'nome_produto', 'quantidade', 'Total de Vendas por Produto', 'vendas_produto.png', 'lightgreen')

# --- Criar PDF profissional ---
class PDF(FPDF):
    def header(self):
        # Cabeçalho com título e linha
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Relatório de Vendas - Projeto Dados', 0, 1, 'C')
        self.set_line_width(0.5)
        self.line(10, 25, 200, 25)
        self.ln(10)

    def footer(self):
        # Rodapé com página
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Capa
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 60, 'Relatório de Vendas', 0, 1, 'C')
pdf.set_font('Arial', '', 14)
pdf.cell(0, 10, f'Data: {datetime.now().strftime("%d/%m/%Y")}', 0, 1, 'C')
pdf.ln(40)

pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, "Este relatório apresenta um resumo das vendas realizadas, divididas por cliente e produto. "
                     "As análises permitem identificar os principais clientes e produtos em volume de vendas, auxiliando em decisões estratégicas.")

# Página vendas por cliente
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Vendas por Cliente', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 8, "Aqui estão os dados de vendas agrupados por cliente, mostrando a quantidade total vendida para cada um.")
pdf.image('vendas_cliente.png', x=15, w=180)
pdf.ln(10)

# Página vendas por produto
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Vendas por Produto', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 8, "Aqui estão os dados de vendas agrupados por produto, facilitando a visualização dos itens mais vendidos.")
pdf.image('vendas_produto.png', x=15, w=180)

pdf.output('relatorio_profissional.pdf')

print("PDF profissional gerado: relatorio_profissional.pdf")

