'''
Dota 2
Super Mario
Zelda
KOFXIII
Doom
Crash Bandicood
Fifa 18
God Of War
'''
from math import sqrt

usuarios = {"Angelica": {"Dota 2": 4.5, "Super Mario": 5.6, "Zelda": 6.7, "Doom": 9.0, "Fifa 18": 6.7,
"Crash Bandicood": 8.9},

"Dan": {"Super Mario": 5.6, "Dota 2": 5.6, "Doom": 9.0, "Fifa 18": 7.8, "Zelda": 6.5, "Crash Bandicood": 6.7},

"Sam": {"Zelda": 5.6, "Dota 2": 7.7, "Doom": 5.4, "God Of War": 7.9, "Fifa 18": 5.6, "Super Mario": 9.8}}

def manhattan(avalicao1, avalicao2): #Distancia de Manhattan

    distancia = 0
    for chave in avalicao1:
        if chave in avalicao2:
            distancia += abs(avalicao1[chave] - avalicao2[chave])
    return distancia

def euclidiana(avalicao1, avalicao2):
    distancia = 0
    for chave in avalicao1:
        if chave in avalicao2:
            potencia = pow(avalicao1[chave] - avalicao2[chave],2)
            distancia += sqrt(potencia)
    return distancia

def mikwonsk(avaliacao1, avaliacao2, r):
    distancia = 0
    commonRatings = False
    for chave in avaliacao1:
        if chave in avaliacao2:
            distancia += pow(abs(avaliacao1[chave] - avaliacao2[chave]),r)
            commonRatings = True
    if commonRatings:
        return pow(distancia,1/r)
    else:
        return 0

def obterVizinhaca(nomeUsuario, usuarios):
    distancias = []
    for usuario in usuarios:
        if usuario != nomeUsuario:
            distancia = mikwonsk(usuarios[usuario], usuarios[nomeUsuario], 1)
            distancias.append((distancia, usuario))
    distancia.sort()
    return distancias


def recomendacao(nomeUsuario, usuarios):
    vizinho = obterVizinhaca(nomeUsuario, usuarios)[0][1]
    recomendacoes = []
    avaliacaoVizinho = usuarios[vizinho]
    avaliacaoUsuarios = usuarios[nomeUsuario]
    for jogo in avaliacaoVizinho:
        if not jogo in avaliacaoUsuarios:
            recomendacoes.append(jogo, avaliacaoVizinho[jogo])
    return sorted(recomendacoes, key = lambda gameTuple: gameTuple[1], reverse = True)



#print(calculaVizinhoProximo("Sam", usuarios))
print(usuarios["Angelica"])
#print("\n")
print(usuarios["Dan"])
#print("\n")
#print(usuarios["Sam"])
#print("\n")

print(euclidiana(usuarios["Angelica"], usuarios["Dan"]))
print(manhattan(usuarios["Angelica"], usuarios["Sam"]))
print(mikwonsk(usuarios["Angelica"], usuarios["Sam"], 2))

print(recomendacao('Angelica',usuarios))
