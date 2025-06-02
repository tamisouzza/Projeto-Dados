from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum, avg

# Iniciar sessão Spark
spark = SparkSession.builder \
    .appName("PipelineDados") \
    .getOrCreate()

# Ler dados
df = spark.read.csv('dados/dados_vendas.csv', header=True, inferSchema=True)

df.show(5)

# Faturamento por cidade
faturamento = df.groupBy('cidade').agg(spark_sum('valor_compra').alias('faturamento'))
faturamento.show()

# Média por forma de pagamento
media = df.groupBy('forma_pagamento').agg(avg('valor_compra').alias('media_compra'))
media.show()

# Salvar resultados
faturamento.write.csv('dados/faturamento_spark', header=True, mode='overwrite')
media.write.csv('dados/media_pagamento_spark', header=True, mode='overwrite')

print("\nProcessamento Spark finalizado!")

# Encerrar Spark
spark.stop()
