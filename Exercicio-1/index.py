print("Sistema Desenvolvido por Eduarda Elisa da Silva Oliveira, RU: 4876813")

def calcular_valor_mensal(valor_base, idade):
    # Definindo as porcentagens de acordo com a idade
    if 0 <= idade < 19:
        porcentagem = 100 / 100
    elif 19 <= idade < 29:
        porcentagem = 150 / 100
    elif 29 <= idade < 39:
        porcentagem = 225 / 100
    elif 39 <= idade < 49:
        porcentagem = 240 / 100
    elif 49 <= idade < 59:
        porcentagem = 350 / 100
    elif idade >= 59:
        porcentagem = 600 / 100
    else:
        return "Idade inválida."
    
    # Calculando o valor mensal
    valor_mensal = valor_base * porcentagem
    return valor_mensal

# Tentando Solicitar inputs do usuário
try:
    valor_base = float(input("Informe o valor base do plano: "))
    idade = int(input("Informe a idade do cliente: "))
    
    # Calculando o valor mensal com base nos inputs
    valor_mensal = calcular_valor_mensal(valor_base, idade)
    
    if isinstance(valor_mensal, float):
        print(f"O valor mensal do plano é de: R$ {valor_mensal:.2f}")
    else:
        print(valor_mensal)  # Caso de idade inválida

    # Capturando erro de  tipagem nos inputs
except ValueError:
    print("Por favor, insira um valor válido para o valor base ou a idade.")