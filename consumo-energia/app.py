# --- CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE ---

def calcular_consumo():
    print("=== CALCULADORA DE CONSUMO ELÉTRICO ===")
    
    aparelho = input("Nome do aparelho (ex.: Geladeira): ")
    potencia = float(input("Potência do aparelho em watts (W): "))
    horas_dia = float(input("Tempo médio de uso diário (horas): "))
    
    # Cálculo do consumo mensal em kWh
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    # Cálculo do custo estimado (R$ 0,75 por kWh)
    tarifa_kwh = 0.75
    custo_estimado = consumo_mensal * tarifa_kwh
    
    print("\n----------------------------------")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_estimado:.2f}/mês (Tarifa: R$ {tarifa_kwh:.2f}/kWh)")
    print("----------------------------------")

if __name__ == "__main__":
    calcular_consumo()