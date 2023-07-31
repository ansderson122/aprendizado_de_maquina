dados = [
    [0, 1, 3, 1],
    [1, 0, 2, 0],
    [2, 1, 3, 1],
    [2, 0, 0, 0],
    [0, 0, 4, 1]
]

def distancia(ponto1, ponto2):
    if len(ponto1) != len(ponto2):
        return
    
    soma = 0
    for a, b in zip(ponto1, ponto2):
        soma += (a - b) ** 2
    return soma ** (1 / 2)

def inserirDado():
    a = int(input("Esta com febre: "))
    b = int(input("Esta com enjôo: "))
    c = int(input("Esta com manchas: "))
    return [a, b, c]

def main():
    k = int(input("Digite o valor de k: "))
    continua = True
    while continua:
        distancias = []
        print("inserir dados 1")
        print("sair 0 ")
        a = int(input())
        if a == 0:
            continua = False
            continue

        dado = inserirDado()
        d = 0
        for index, dado2 in enumerate(dados):
            d = distancia(dado, dado2[0:3])
            distancias.append([d, index])

        distancias = sorted(distancias, key=lambda x: x[0])

        doente = 0 
        saudavel = 0
        i = 0
        while i < k:
            if dados[distancias[i][1]][3] == 0:
                saudavel += 1
            else:
                doente += 1
            i += 1
        
        if saudavel >= doente:
            dado.append(0)
            print("Você está saudável.")
        else: 
            dado.append(1)
            print("Você está doente.")
        dados.append(dado)

if __name__ == "__main__":
    main()
