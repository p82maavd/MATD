

alphabet=["G","C","A","Error"]
states=["","G","GC","GCA","GCAG","GCAGA","GCAGAG","GCAGAGA","GCAGAGAG"]


def showTable(table):
    print(alphabet)
    for x in range(len(table)):
        var="Estado "+str(x)+str(table[x])
        print(var)

def getFirst(initialTable):
    for i in range(len(initialTable[0])):
        if i == 1:
            return i


NO_OF_CHARS = 256
 
def getNextState(pat, M, state, x):
    '''
    calculate the next state
    '''
 
    # If the character c is same as next character
      # in pattern, then simply increment state
 
    if state < M and x == ord(pat[state]):
        return state+1
 
    i=0
    # ns stores the result which is next state
 
    # ns finally contains the longest prefix
     # which is also suffix in "pat[0..state-1]c"
 
     # Start from the largest possible value and
      # stop when you find a prefix which is also suffix
    for ns in range(state,0,-1):
        if ord(pat[ns-1]) == x:
            while(i<ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i+=1
            if i == ns-1:
                return ns
    return 0
 
def computeTF(pat, M):
    '''
    This function builds the TF table which
    represents Finite Automata for a given pattern
    '''
    global NO_OF_CHARS
 
    TF = [[0 for i in range(NO_OF_CHARS)]\
          for _ in range(M+1)]
 
    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
 
    return TF
 
def search(pat, txt):
    '''
    Prints all occurrences of pat in txt
    '''
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)   

    showTable(TF)
 
    # Process txt over FA.
    state=0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".\
                   format(i-M+1))
 

search("gabgacgab","gabgabgacgab")


#gabgacgab

#gabgab deberia volver a 3
