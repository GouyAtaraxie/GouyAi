texte = "bonjour gouyai"
L = []
stoi = {}
itos = {}
for caracter in texte :
    if caracter not in L :
        L.append(caracter)

for index, caracter in enumerate(L) :
    stoi[caracter] = index
    itos[index] = caracter

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

print(encodé, décodé)
    