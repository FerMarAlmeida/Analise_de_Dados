## Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, …

n = int(input("Tabuada de:"))

for x in range(1, 10):
    print(f"{n} x {x} = {n * x}")
