data = int(input("Qual a data da inscricao? "))
condEspecial = (input("Possui indicação especial? "))


datamaxinscricao = 28
condicao = "sim"


# validação data de inscrição
if data <= datamaxinscricao:
    print("Dentro do prazo")
elif data >= datamaxinscricao and condEspecial == "sim":
    print("Dentro do prazo")
else:
    print("Fora do prazo")