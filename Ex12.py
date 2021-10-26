# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

nomeProduto = input("Digite o nome do seu Produto: ")
precoProduto = float(input(f"Digite o valor {nomeProduto} : "))
produtoDesconto = precoProduto - (precoProduto * 0.05)

print(f"O preco do seu produto é R$ {precoProduto:.2f}, porem estamos com a \n"
      f"liquidação do produto {nomeProduto}, e tem 5% de desconto \n"
      f"o preço final é R$ {produtoDesconto:.2f}")
