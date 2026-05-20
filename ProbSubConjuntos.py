# 1. Método para encontrar UMA solução
def soma_zero_um(nums):
    def backtrack(inicio, caminho, soma):
        if caminho and soma == 0: return caminho
        for i in range(inicio, len(nums)):
            res = backtrack(i + 1, caminho + [nums[i]], soma + nums[i])
            if res: return res
    return backtrack(0, [], 0)

# 2. Método para encontrar TODAS as soluções
def soma_zero_todos(nums):
    solucoes = []
    def backtrack(inicio, caminho, soma):
        if caminho and soma == 0: solucoes.append(caminho)
        for i in range(inicio, len(nums)):
            backtrack(i + 1, caminho + [nums[i]], soma + nums[i])
    
    backtrack(0, [], 0)
    return solucoes

# --- Testes Iniciais ---
testes = [
    [-7, -3, -2, 5, 8],
    [1, 2, 3, 4, 5, 10],
    [-5, 2, 3, -1, 1]
]

for t in testes:
    print(f"\nConjunto: {t}")
    print(f"Uma solução: {soma_zero_um(t)}")
    print(f"Todas as soluções: {soma_zero_todos(t)}")

    #O Problema da Soma dos Subconjuntos consiste simplesmente em procurar, dentro de uma lista de números 
    #positivos e negativos, uma combinação de elementos que some exatamente zero. A grande dificuldade 
    #computacional desse problema é que o algoritmo precisa decidir se "inclui" ou "exclui" cada número da lista,
    # o que faz a quantidade de testes dobrar a cada novo elemento inserido na conta (O(2 )). 
    
    #Por causa desse crescimento exponencial, conjuntos pequenos são resolvidos em frações de segundo, mas listas com 50 elementos ou mais geram quatrilhões de caminhos possíveis, travando qualquer computador moderno antes que ele consiga checar todas as combinações na força bruta.
