# Comparador de números inteiros

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 == num2:
    print('Os valores são iguais!')
elif num1 > num2:
    print('O valor {} é maior que o valor {}'.format(num1, num2))
elif num1 < num2:
    print('O valor {} é menor que o valor {}'.format(num1, num2))

# ou no final utilizar ELSE para considerar que os valores seriam iguais.
