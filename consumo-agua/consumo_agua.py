# Programa: Consumo de Água (com match/case)

# Solicita os dados de entrada
tipo_imovel = input("Digite o tipo de imóvel (Comercial, Casa ou Apartamento): ").strip().capitalize()
consumo = float(input("Digite o consumo mensal de água (em m³): "))

# Estrutura match/case para o tipo de imóvel
match tipo_imovel:
    case "Comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    case "Apartamento":
        # if/else internos para analisar o consumo do apartamento
        if consumo < 10:
            print("Consumo econômico – excelente controle de água!")
        elif consumo <= 25:
            print("Consumo moderado – dentro do padrão residencial.")
        else:
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
            
    case "Casa":
        # if/else internos para analisar o consumo da casa
        if consumo <= 25:
            print("Consumo moderado – dentro do padrão residencial.")
        else:
            print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
            
    case _:
        print("Tipo de imóvel inválido. Por favor, digite Comercial, Casa ou Apartamento.")