salarioBase =float(input("Digite o valor do salario mínimo atual. "
                         "Caso não saiba o atual (2025) esta no valor de 1412: "))
salarioUsuario = float(input("Digite o seu salario: "))
salarioTotal = salarioUsuario / salarioBase
print(f"{salarioTotal:.2f}")