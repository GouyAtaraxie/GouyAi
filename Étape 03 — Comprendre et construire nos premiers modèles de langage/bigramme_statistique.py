import random

texte = "ababac"
L = []
stoi = {}
itos = {}
for character in texte :
    if character not in L :
        L.append(character)

for index, character in enumerate(L) :
    stoi[character] = index
    itos[index] = character

matrice = [[0 for _ in range(len(itos))] for _ in range(len(itos))]

for i in range(len(texte)-1) :
    matrice[stoi[texte[i]]][stoi[texte[i+1]]] += 1

matrice_proba = [[0 for _ in range(len(itos))] for _ in range(len(itos))]

for i in range(len(matrice)) :
    somme = sum(matrice[i])
    length = len(matrice[i])
    if somme == 0 :
        for j in range(len(matrice)) :
            matrice_proba[i][j] = 1/length
    else :
        for j in range(len(matrice)) :
            matrice_proba[i][j] = matrice[i][j]/somme
        
        
def encoder(stoi, texte) :
    L=[]
    for i in range(len(texte)) :
        L.append(stoi[texte[i]])
    return L

def decoder(itos, encodé) :
    L=''
    for i in range(len(encodé)) :
        L += itos[encodé[i]]
    return L

def generator(text, long):
    txt = text[-1:]
    for _ in range(long) :
        txt += random.choices(
            population=L,
            weights=matrice_proba[stoi[txt[-1:]]],
            k=1
            )[0]
    return text+txt[1:]

encodé = encoder(stoi, texte)

décodé = decoder(itos, encodé)

for _ in range(5) :
    print(generator(texte, 5))