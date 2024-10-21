#  Apresenta o nome e o menu da pizzaria
print("--------- Bem-vindos à Pizzaria da Eduarda Elisa da Silva Oliveira RU: 4876813---------")
print("---------------------------- Cardápio ----------------------------")
print("--------------------------------------------------------------")
print("| Tamanho  |  Pizza Salgada(PS)  |  Pizza Doce(PD)  |")
print("|    P     |       R$ 30.00       |       R$ 34.00      |")
print("|    M     |       R$ 45.00       |       R$ 48.00      |")
print("|    G     |       R$ 60.00       |       R$ 66.00      |")
print("--------------------------------------------------------------")

#  Inicializa o acumulador para o total do pedido
total = 0  

#  Inicia um loop para permitir que o cliente faça vários pedidos
while True:  
    #  Input do sabor
    sabor = input("\nEntre com o sabor desejado (PS/PD): ").upper()  # Torna maiúsculo
    if sabor not in ['PS', 'PD']:  # Valida o sabor
        print("Sabor inválido. Tente novamente.")  
        continue  # Volta ao início do loop

    #  Input do tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:  # Valida o tamanho
        print("Tamanho inválido. Tente novamente.")  
        continue  # Volta ao início do loop

    #  Estrutura aninhada para definir o preço
    if sabor == 'PS':  # Pizza Salgada
        if tamanho == 'P':
            preco = 30
        elif tamanho == 'M':
            preco = 45
        elif tamanho == 'G':
            preco = 60
    elif sabor == 'PD':  # Pizza Doce
        if tamanho == 'P':
            preco = 34
        elif tamanho == 'M':
            preco = 48
        elif tamanho == 'G':
            preco = 66

    # Adiciona o preço da pizza ao total
    total += preco
    print(f"\nVocê pediu uma Pizza {'Salgada' if sabor == 'PS' else 'Doce'} no tamanho {tamanho}: R$ {preco:.2f}")

    #  Pergunta se o usuário quer pedir mais algo
    continuar = input("\nDeseja mais alguma coisa? (S/N): ").upper()
    if continuar == 'N':  # Encerra o pedido
        break  # Sai do loop

# Comentário explicando que estamos saindo do loop e exibindo o valor total
# Apresenta o total final do pedido
print(f"\nO valor total a ser pago: R$ {total:.2f}")