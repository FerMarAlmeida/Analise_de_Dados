## Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
## O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário.
## Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor = float(input("Digite o valor da casa: "))
salário = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))
meses = anos * 12
prestacao = valor / meses
if prestacao > salário * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")
