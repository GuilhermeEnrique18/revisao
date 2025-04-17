opcao = "S"
while opcao == "S":
    n = float(input("Digite um número para saber se é par ou ímpar. Pode ser positivo ou negativo: "))
    if n %2 == 0 and n > 0:
        print("É par e positivo")
    elif n %2 == 0 and n < 0:
        print("É par e negativo")
    elif n %2 == 1 and n < 0:
        print("É impar e negativo")
    else:
        print("É impar e positivo")
    opcao = input("Digite S para continuar ou qualquer tecla para parar: ")

print("PROGRAMA FINALIZADO")