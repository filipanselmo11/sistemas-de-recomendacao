
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

def SimilaridadeCosseno(avalicao1,avalicao2):
    somatorioX = 0
    somatorioY = 0
    for chave in avalicao1:
        if chave in avalicao2:
            x = avalicao1[chave]
            y = avalicao2[chave]
            somatorioX = somatorioX + x**2
            somatorioY = somatorioY + y**2
    
    raizX = sqrt(somatorioX)
    raizY = sqrt(somatorioY)
    prodRaizXY = raizX * raizY
    prodXY = x * y
    divisao = prodXY / prodRaizXY
    return divisao


print(SimilaridadeCosseno(usuarios["Angelica"], usuarios["Veronica"]))

