def resolver_n_rainhas(n):
    def backtrack(linha):
        if linha == n:
            # Forma o tabuleiro e salva as posiçoes das rainhas
            solucoes.append(["." * c + "Q" + "." * (n - c - 1) for c in estado])
            return
            
        for c in range(n):
            if c not in cols and (linha - c) not in diag1 and (linha + c) not in diag2:
                
                cols.add(c); diag1.add(linha - c); diag2.add(linha + c); estado.append(c)
                
                # explora
                backtrack(linha + 1)
                
                # backtrackign
                cols.remove(c); diag1.remove(linha - c); diag2.remove(linha + c); estado.pop()

    solucoes, estado = [], []
    cols, diag1, diag2 = set(), set(), set()
    
    backtrack(0)
    return solucoes

n = 7 
todas_solucoes = resolver_n_rainhas(n)

print(f"num de solucoes{n}: {len(todas_solucoes)}\n")

for i, sol in enumerate(todas_solucoes, 1):
    print(f"--- Solução {i} ---")
    for linha in sol:
        print(linha)
    print() # linha em branco
    #-------------------------------------------
    # ALGORITMO COM COMPLEXIDADE O(N!)
    #-------------------------------------------