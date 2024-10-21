# Nome completo
print("Bem-vindos a Madeireira do Lenhador Eduarda Elisa da Silva Oliveira RU: 4876813 \n")

# Função para escolher o tipo de madeira
def escolha_tipo():
    while True:
        tipo = input("\nEscolha o tipo de madeira:\n PIN - Tora de Pinho\n PER - Tora de Perobax\n MOG - Tora de Mogno\n IPE - Tora de Ipê\n IMB - Tora de Imbuia: ").upper()
        if tipo == "PIN":
            return 150.40
        elif tipo == "PER":
            return 170.20
        elif tipo == "MOG":
            return 190.90
        elif tipo == "IPE":
            return 210.10
        elif tipo == "IMB":
            return 220.70
        else:
            print("Escolha Inválida, entre com o modelo novamente.")  

# Função para escolher a quantidade de toras e calcular o desconto
def qtd_toras():
    while True:
        try:
            qtd = float(input("Informe a quantidade de toras (em m³): \n"))
            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras.")  
                continue
            elif qtd < 100:
                return qtd, 0.0
            elif qtd >= 100 and qtd < 500:
                return qtd, 0.04
            elif qtd >= 500 and qtd < 1000:
                return qtd, 0.09
            elif qtd >= 1000 and qtd <= 2000:
                return qtd, 0.16
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")

# Função para escolher o transporte
def transporte():
    while True:
        try:
            opcao = int(input("\nEscolha o tipo de transporte \n(1 - transporte Rodoviário - R$ 1000.00,\n 2 - Transporte Ferroviário R$ 2000.00, \n 3 - Transporte Hidroviário R$ 2500.00): "))
            if opcao == 1:
                return 1000
            elif opcao == 2:
                return 2000
            elif opcao == 3:
                return 2500
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Erro: Por favor, insira um número válido para o transporte.")

# Código principal (main)
if __name__ == "__main__":
   
    # Escolher o tipo de madeira
    valor_madeira = escolha_tipo()
    
    # Escolher a quantidade de toras e obter o desconto
    qtd, desconto = qtd_toras()
    
    # Escolher o transporte
    valor_transporte = transporte()
    
    # Calcular o total
    total = ((valor_madeira * qtd) * (1 - desconto)) + valor_transporte
    
    # Exibir o resultado final
    print(f"\nPedido finalizado:\n- Tipo de madeira: R$ {valor_madeira:.2f} por m³")
    print(f"- Quantidade de toras: {qtd} m³")
    print(f"- Desconto aplicado: {desconto*100:.0f}%")
    print(f"- Valor do transporte: R$ {valor_transporte:.2f}")
    print(f"\nValor total a pagar: R$ {total:.2f}")  