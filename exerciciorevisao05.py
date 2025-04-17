opcao = "s"
while opcao == "s":
    peso = float(input("informe o seu peso: "))
    altura = float(input("informe a sua altura: "))
    imc = peso / altura ** 2
    if imc < 18.6:
        print("Você está abaixo do peso")
    elif imc > 18.5 and imc < 25:
        print("Você está no peso ideal")
    elif imc > 24.9 and imc < 30:
        print("Levemente acima do peso")
    elif imc > 29.9 and imc < 35:
        print("Obesidade grau I")
    elif imc > 34.9 and imc < 40:
        print("Obesidade grau II(Severa)")
    else:
        print("Obesidade grau III(Morbida)")
    opcao = input("Deseja continuar? S para sim qualquer tecla para nao")