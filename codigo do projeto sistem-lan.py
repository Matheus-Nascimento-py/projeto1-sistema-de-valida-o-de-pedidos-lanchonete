# Mensagem de saudação + menu forecido ao cliente

print('BEM VINDO A SUA LANCHONETE FAVORITA!!!')
menu = ['Hamburguer P', 'Hamburguer M', 'Hamburguer G', 
         'Batata P', 'Batata M', 'Batata G', 
         'Refrigerante', 'Suco', 'Sobremesa']

preco = [10.00, 15.00, 20.00,
         5.00, 7.00, 10.00,
         4.00, 2.00, 6.00]

print(menu)
print('_______________________________________________')

#atribuindo os preços + soma dos valores do pedido

for i in range(len(menu)):
    print(f'{i+1}, {menu [i]} - R${preco [i]: .2f}') 

pedido = []
total = 0.0

#gerando e validando pedidos + interação com usuário/cliente

while True:
    escolha = input("escolha o número de item que deseja pedir (ou '0' para finalizar): ")

    if escolha == '0':
        break
    elif escolha.isdigit() and 1 <= int(escolha) and 1 <= int(escolha) <= len(menu):
        item_id = int(escolha) - 1
        pedido.append(menu [item_id])
        total += preco [item_id]
        print(f'Voê pediu: {menu [item_id]} - R$ {preco [item_id]: .2f}')
    else:
        print('Escolha inválida. Por favor, tente novamente')

#resultado do pedido, mensagem final ao cliente

print("\npedido do cliente")
print('_________________________________________________')
for item in pedido:
    print(item)
print(f'Total: R$ {total: .2f}')