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
              
print(matrice)