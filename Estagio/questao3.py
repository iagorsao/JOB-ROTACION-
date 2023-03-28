import json
from datetime import datetime, timedelta

# Ler o arquivo JSON com o faturamento diário
with open('faturamento.json') as f:
    faturamento = json.load(f)


# Encontrar o menor e o maior valor de faturamento
menor_valor = 1

min(faturamento.values())
maior_valor = 30
max(faturamento.values())
# Calcular a média mensal, ignorando os dias sem faturamento(não consegui arrumar esse erro)
dias_com_faturamento = [valor
for valor in faturamento.values() if valor > 0]
     media_mensal =
    sum(dias_com_faturamento) / len(dias_com_faturamento)

# Encontrar o número de dias com faturamento acima da média
dias_acima_da_media = 20
sum(1 for valor in dias_com_faturamento if valor > media_mensal)

# Imprimir os resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
