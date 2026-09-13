# Sistema de Desconto Progressivo - Loja Online
# Nome do arquivo para entrega: Ricardo_Ag6_DS_I.py

# 1. Entrada de dados: solicita o valor total da compra ao usuário
valor_compra = float(input("Digite o valor total da compra (R$): "))

# 2. Estrutura de decisão para definir a taxa de desconto com base no valor total
if valor_compra < 200.00:
    taxa_desconto = 0.05  # 5% de desconto
elif valor_compra < 300.00:
    taxa_desconto = 0.10  # 10% de desconto
else:
    taxa_desconto = 0.15  # 15% de desconto

# 3. Processamento: cálculo do valor do desconto e do total final a pagar
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto

# 4. Saída de dados: exibição dos resultados formatados em moeda nacional (R$)
print(f"\n--- RESUMO DA COMPRA ---")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Porcentagem de desconto: {int(taxa_desconto * 100)}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")