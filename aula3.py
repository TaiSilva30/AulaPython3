#Declarando váriaveis

dia = int(input("Qual o dia de hoje? "))
pedidopizza = int(input("Quantas pizzas comprou? "))
pedidobebida = int(input("Quantas bebidas comprou? "))
pedidobolo = int(input("Quantos bolos comprou? "))
pedidodoce = int(input("Quantos doces comprou? "))


diafesta = 26
minpizza = 10
minbebida = 12
minbolo = 5
mindoce = 600

if diafesta == dia:
    print("Ana esta fazendo as compras no dia da festa!")

if(pedidopizza <= minpizza):
    print("Ana não comprou pizzas suficientes")
elif (pedidopizza >= minpizza):
    print("Ana comprou pizzas suficientes")

if(pedidobebida <= minbebida):
    print("Ana não comprou bebidas suficientes")
elif (pedidobebida >= minbebida):
    print("Ana comprou bebidas suficientes")

if(pedidobolo <= minbolo):
    print("Ana não comprou bolo suficientes")
elif (pedidobolo >= minbolo):
    print("Ana comprou bolo suficientes")

if(pedidodoce <= mindoce):
    print("Ana não comprou doce suficientes")
elif (pedidodoce >= mindoce):
    print("Ana comprou doce suficientes")