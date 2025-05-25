import random

N = 100  # número de spins
J = 1
h = 1

# Gerar spins aleatórios (-1 ou 1)
spins = [random.choice([-1, 1]) for _ in range(N)]

# Cálculo da energia usando o Hamiltoniano
energia = 0

# Primeiro termo: interação entre spins vizinhos
for i in range(N - 1):
    energia -= J * spins[i] * spins[i + 1]

# Segundo termo: interação com o campo
energia += h * sum(spins)

print("Energia do sistema:", energia)