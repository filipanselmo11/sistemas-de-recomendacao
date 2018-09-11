from math import sqrt

usuarios = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
"Slighty Stoopid": 3.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},

"Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0,
"Slighty Stoopid": 3.5, "Vampire Weekend": 2.0},

"Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Dedmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
"Slighty Stoopid": 1.0},

"Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slighty Stoopid": 4.5,
"The Strokes": 4.0, "Vampire Weekend": 2.0},

"Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
"Vampire Weekend": 1.0},

"Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slighty Stoopid": 4.5,
"The Strokes": 4.0, "Vampire Weekend": 4.0},

"Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slighty Stoopid": 4.0,
"The Strokes": 5.0},

"Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slighty Stoopid": 2.5, "The Strokes": 3.0}}


def manhattan(avalicao1, avalicao2):
    distancia = 0
    for chave in avalicao1:
        if chave in avalicao2:
            distancia = distancia + abs(avalicao1[chave] - avalicao2[chave])
    return distancia

def computaVizinho(nomeUsuario, usuarios):
    distancias = []
    for usuario in usuarios:
        if usuario != nomeUsuario:
            distancia = manhattan(usuarios[usuario], usuarios[nomeUsuario])
            distancias.append((distancia, usuario))
    distancias.sort()
    return distancias

def recomendacao(nomeUsuario, usuarios):
    vizinho = computaVizinho(nomeUsuario, usuarios)[0][1]
    recomendacoes = []
    avalicoesVizinho = usuarios[vizinho]
    avalicaoesUsuario = usuarios[nomeUsuario]
    for artista in avalicoesVizinho:
        if not artista in avalicaoesUsuario:
            recomendacoes.append((artista, avalicoesVizinho[artista]))
    return sorted(recomendacoes, key = lambda Artista: Artista[1], reverse = True)



print("Base de Dados: ", usuarios)
print("Código da função de  manhattan: ",manhattan(usuarios['Sam'], usuarios['Hailey']))
print("Código da função de computar os vizinhos: ",computaVizinho("Sam", usuarios))
print("Recomendação: ",recomendacao("Hailey", usuarios))