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
    if sum(matrice[i]) == 0 :
        for j in range(len(matrice)) :
            matrice_proba[i][j] = 1/(len(matrice[i]))
    else :
        for j in range(len(matrice)) :
            matrice_proba[i][j] = matrice[i][j]/sum(matrice[i])
        
        
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

encodé = encoder(stoi, texte)

décodé = decoder(itos, encodé)
              
print(matrice, matrice_proba)