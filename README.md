Data Project – Data Cleaning and Analysis with Python

This project was developed for learning and practice purposes, focusing on data cleaning, transformation, and exploratory analysis using Python and its main data libraries.

Objective
Work with raw data to extract insights and prepare it for analysis. The main steps include:

Data loading

Cleaning and preprocessing

Data transformation

Exploratory data analysis (EDA)

Visualization

Technologies and Tools
Python 3

Jupyter Notebook

Pandas

NumPy

Matplotlib

Seaborn

Google Colab (optional)

Project Structure

📁 Projeto-Dados/
├── dados/              # Raw datasets
├── notebooks/          # Jupyter notebooks with analysis
│   └── projeto_dados.ipynb
├── imagens/            # Charts and graphics generated
├── requirements.txt    # Dependencies (if needed)
└── README.md

Steps Performed
Loading the dataset
Raw data was loaded using pandas.read_csv() for initial exploration.

Data cleaning

Removed duplicates

Filled or removed missing values

Standardized text and numeric formats

Data transformation

Created new calculated columns

Filtered and grouped relevant information

Exploratory Data Analysis (EDA)

Identified patterns, distributions, and outliers

Used visualizations to understand trends and relationships

Visualization

Charts created with Matplotlib and Seaborn

Saved outputs to the /imagens folder

How to Run
You can run this project using Jupyter Notebook locally or open it directly on Google Colab:

Open on Google Colab

Or clone and run locally:

git clone https://github.com/tamisouzza/Projeto-Dados.git
cd Projeto-Dados

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Start Jupyter Notebook
jupyter notebook

Author
Developed by Tami Soares
GitHub Profile#  Projeto de Dados

Este projeto demonstra um pipeline de dados simples, desenvolvido com foco nas principais etapas de um fluxo de dados: geração, ingestão, processamento, armazenamento e análise.

---

##  Tecnologias e Ferramentas Utilizadas
- Python
- Pandas
- SQL (PostgreSQL simulado)
- Apache Spark (conceitual no projeto)
- Git e GitHub

---

##  Descrição do Projeto

O projeto simula um fluxo de dados completo, com as seguintes etapas:

1. **Geração de Dados:** Criação de dados fictícios representando uma base de vendas (clientes, produtos e transações).
2. **Processamento e Transformação:** Limpeza, transformação e preparação dos dados para análise, utilizando Python e bibliotecas de dados.
3. **Armazenamento:** Dados processados armazenados em formato estruturado, simulando um banco relacional (PostgreSQL).
4. **Análise de Dados:** Consultas SQL para gerar insights e análises exploratórias.

---

##  Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/tamisouzza/projeto-dados.git

