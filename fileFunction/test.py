

def letterToNb(letter):
    listeAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter = letter.lower()
    for i in range(0, len(listeAlphabet)):
        if listeAlphabet[i] == letter:
            return i


def codeCesar(clef, mots):
    listeAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                     'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    clef = clef.lower()
    clef = letterToNb(clef)
    mots = list(mots)
    for i in range(0, len(mots)):
        lettreX = letterToNb(mots[i])
        mots[i] = listeAlphabet[lettreX+clef]
    mots = ''.join(mots)
    return mots

def decryptCodeCesar(clef, mots):
    listeAlphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                     'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    clef = clef.lower()
    clef = letterToNb(clef)
    mots = list(mots)
    for i in range(0, len(mots)):
        lettreX = letterToNb(mots[i])
        mots[i] = listeAlphabet2[lettreX-clef]
    mots = ''.join(mots)
    return mots

test = codeCesar("b", "tom")
print(test)
test = decryptCodeCesar("b", test)
print(test)