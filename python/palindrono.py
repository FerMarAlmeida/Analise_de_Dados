# Escreva um programa que verifique se um número é palíndromo.
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
# Exemplos: 454, 10501

s = input("Digite o número a verificar, sem espaços:")
x = s[::-1] 
if x == s:
    print(f"{s} é palíndromo")
else:
    print(f"{s} não é palíndromo")
