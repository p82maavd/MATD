#Count the ocurrences of a pattern in a text using a naive approach

def naiveAlgorithm(pattern, text):
    cont=0
    numberPatterns=0
    for x in range(0,len(text)-len(pattern)):
        for y in range(0,len(pattern)):
            if cont == len(pattern):
                cont=0
                numberPatterns+=1
            if text[x+y] == pattern[y]:
                cont+=1
            else:
                cont=0
                break
    #print(numberPatterns)
    return numberPatterns

