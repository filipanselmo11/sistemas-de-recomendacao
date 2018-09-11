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

def Pearson(xi, yi):
    numeroBandas = 0
    soma1 = 0
    somaXI = 0
    somaYI = 0
    somaXI2 = 0
    somaYI2 = 0
    for chave in xi:
        if chave in yi:
            numeroBandas = numeroBandas + 1
            prod = xi[chave] * yi[chave]
            soma1 = soma1 + prod
            somaXI = somaXI + xi[chave]
            somaYI = somaYI + yi[chave]
            somaXI2 = somaXI2 + pow(xi[chave],2)
            somaYI2 = somaYI2 + pow(yi[chave],2)
    
    prodSoma = (somaXI * somaYI) / numeroBandas
    subtracao = soma1 - prodSoma
    potenciaSomaXi = pow(somaXI,2)
    subtracao2 = somaXI2 - potenciaSomaXi






#print(usuarios["Haylei"])
print(usuarios["Bill"])