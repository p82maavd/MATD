#Count the ocurrences of a pattern in a text using a deterministic finite automaton approach

def showTable(table):
    for x in range(len(table)):
        var="Estado "+str(x)+str(table[x])
        print(var)


def getTable(states,pattern,alphabet):
    initialTable=[]
    for x in range(len(pattern)):
        initialTable.append([0]*len(alphabet))
    for i in range(len(states)-1):
        for j in range(len(alphabet)):
            if alphabet[j]==states[i+1][-1]:
                initialTable[i][j]=i+1
            else:
                cad=states[i]+alphabet[j]
                for k in range(0,len(cad)):
                    
                    for l in range(len(states)):
                        if cad[k:]==states[l]:
                            initialTable[i][j]=len(cad[k:])
                            break
    return initialTable

def deterministicFiniteAutomatonAlgorithm(pattern,text,alphabet):

    #We get the differents states of the patter recognition
    states=[""]
    for x in range(len(pattern)):
        states.append(states[x]+pattern[x])

    initialTable = getTable(states,pattern,alphabet)
    showTable(initialTable)

    currentState=0
    numberPatterns=0
    for x in range(len(text)-1):
        print(x)
        currentState=initialTable[currentState][alphabet.index(text[x])]
        if currentState==len(pattern):
            #print("Pattern found in position: ",str(x-len(pattern)+1))
            pattfound="\x1b[1;33m"+text[x-len(pattern)+1:x+1]+"\x1b[0;37m"
            result=text[0:x-len(pattern)]+pattfound+text[x+1:]
            numberPatterns+=1
            currentState=0
            #print(result)

    print("Number of patterns in text: ",numberPatterns)


