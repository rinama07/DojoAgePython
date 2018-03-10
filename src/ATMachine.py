"""
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
Entregar o menor número de notas;
É possível sacar o cash solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um cash finito de cédulas para aumentar a dificuldade do problema);
notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:
cash do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
cash do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
"""


def withdraw(cash):
    available_bills = [100, 50, 20, 10]
    bills = [0, 0, 0, 0]

    print("withdraw amount: {amount}".format(amount=cash))

    i = 0
    while cash > 0 and i < len(available_bills):
        if cash >= available_bills[i]:
            cash -= available_bills[i]
            bills[i] += 1
        else:
            i += 1

    for i, bill in enumerate(bills):
        print("{number} bills of {value}".format(number=bill, value=available_bills[i]))

    print("remaining cash: {cash}".format(cash=cash))

    return bills
