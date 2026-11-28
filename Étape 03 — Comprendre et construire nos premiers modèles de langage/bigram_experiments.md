# Experimentation with different corpus


## First test 

```
texte = "ababac"

for _ in range(5) :
    print(generator(texte, 12))
```

### **Result :**
```text
ababacbacababacaba
ababacbabababababa
ababacccbacababacc
ababaccabababaccac
ababaccabacbacbaba
```
### **Interpretation :**
The first test to see if the code works, and yes it works ! But the code had a limitation as I had hardcoded the population as ["a", "b", "c"]. So the next step was to make the program adaptive and I only had to change the population to be L the list of every character of the corpus. 

## Second test

```
texte = "ababacd"

for _ in range(5) :
    print(generator(texte, 12))
```

### **Result :**
```text
ababacdbabababacdab
ababacdbababacddaba
ababacdabababababac
ababacdababacdcdaba
ababacdbabacddbabac
```
### **Interpretation :**
Second test to see if the code correctly handles another input character. And we can see that yes, there's no problem with that and the generation is made flawlessly. We can also see that "c" is always followed by "d" because in the corpus, there is nothing after "c" other than "d". And as I have decided, in the corpus "d" is never followed by any other charater so the probability to generate any character after "d" is 1/4 because we have 4 characters in the corpus.


## Third test

```
texte = "le chat mange la souris et le rat mange le pain"

for _ in range(5) :
    print(generator("le", 12))
```

### **Result :**
```text
le lat e lat l
le manget sour
le change pais
le pange ra pa
le e sourat ch
```
### **Interpretation :**
Third test with a French sentence. With this test I wanted to know what would be the result with a real sentence and not only random characters. I'm very happy with this test because it's the first time that I'm generating "text" although it doesn't make any sense. 


## Fourth test

```
texte = """le petit chat dort sur le tapis rouge pendant que la pluie tombe sur la maison. le matin, le chat se leve et mange son pain. la souris regarde le chat depuis la porte de la cuisine. elle a faim mais le chat est trop grand. alors la souris attend que le chat parte dans le jardin. dans le jardin, le chat chasse les oiseaux et dort sous un arbre. pendant ce temps, la souris entre dans la cuisine et mange le pain du chat. le soir, le chat rentre a la maison et ne trouve plus son pain. le chat regarde la souris et la souris regarde le chat."""

for _ in range(5) :
    print(generator("le", 120))
```

### **Result :**
```text
le re degat rd fa plegre m chaitrat cet t chat quisortega platregret lat let egatinde lare. paises pa le auret cha lele le
le le le cha et t s ega le ndis lla d. chant luret chat n chars t chale s, e cha charore cha t d t lat eaimbrben, souisor 
le e ongrde ce s e e ja t faisouvet lan, pon. le lele le pe s pin les e lombrde chat s puimapean. len. cha matris risungas
leate cha laure pat lelat lan chatisingatint t t pa rdet mpatrd ux aison da suin, tre ar pse lan soirt t esondatistre sois
le le lege pant pain. ple mar pe mais let. lason lat ate t t cha legansoroues e atr suisorbrbe s m pisons psouesoue rorous
```
### **Interpretation :**
This last test was with a longer training corpus. With this one, I wanted to know what would happen if I gave my program a bigger corpus. Would it be able to generate words or sentences. Obviously, full sentences were very unlikely. But word was possible, we can see three "chat", cat in English, and seven "cha". It's an interesting result because the word "chat" is very abundant in the text. So even with a simple character generation program that can only see the previous character, I have been able to generate words !

## Conclusion

With this program, I have been able to discover how we can generate characters from simple rules and a training corpus. And with those experiments we have been able to see how we can reproduce simple patterns.
Finally, theses experiments show that a bigram model can easily capture local partern but cannot reliably build coherent sentences.