import math

def obter_numero(prompt):
    return float(input(prompt))

def calcular_antecessor(numero):
    return numero - 1

def calcular_sucessor(numero):
    return numero + 1

def calcular_dobro(numero):
    return numero * 2

def calcular_triplo(numero):
    return numero * 3

def calcular_raiz_quadrada(numero):
    return math.sqrt(numero)

def calcular_media(n1, n2):
    return (n1 + n2) / 2

# Entrada de dados
num1 = obter_numero("Digite o primeiro número:")
num2 = obter_numero("Digite o segundo número:")

# Cálculos
antecessor = calcular_antecessor(num1)
sucessor = calcular_sucessor(num1)
dobro = calcular_dobro(num1)
triplo = calcular_triplo(num1)
raiz_quadrada = calcular_raiz_quadrada(num1)
media = calcular_media(num1, num2)

# Exibição dos resultados
print(f'O antecessor do número {num1} informado é {antecessor} e o sucessor é {sucessor}.')
print(f'O dobro é {dobro}, o triplo é {triplo} e a sua raiz quadrada é {raiz_quadrada:.2f}.')
print(f'A média dos números {num1} e {num2} é {media:.2f}.')
