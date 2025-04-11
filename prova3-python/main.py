produtos = []

contador = 0

while(contador < 5):
    produto= input("digite  o produto:")
    preco= float(input("digite o preço do produto:"))

    contador+=1

    produtos.append({"produto": produto, "preço": preco})

print(produtos)