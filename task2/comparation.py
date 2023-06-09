import random
import time
from naive import naiveAlgorithm
from dfa import deterministicFiniteAutomatonAlgorithm
from kmp import KMPSearch
from bmh import BMHSearch

alphabet=["A","C","G","T"]

f = open("dna.50MB", "r")
text = f.read()
text.replace('\n',"")
#print(text)

patterns=[]

for x in range(100):
    word=""
    for y in range(random.randint(4,10)):
        word+=alphabet[random.randint(0,len(alphabet)-1)]
    patterns.append(word)

#print(patterns)

naiveTime=0
dfaTime=0
kmpTime=0
bmhTime=0
for x in range(len(patterns)):
    print(x)
    
    naivetini=time.time() 
    naiveAlgorithm(patterns[x],text)
    naivetfi=time.time()
    naiveTime+=naivetfi-naivetini

    dfatini=time.time() 
    deterministicFiniteAutomatonAlgorithm(patterns[x],text)
    dfatfi=time.time()
    dfaTime+=dfatfi-dfatini

    kmptini=time.time() 
    KMPSearch(patterns[x],text)
    kmptfi=time.time()
    kmpTime+=kmptfi-kmptini

    bmhtini=time.time() 
    BMHSearch(patterns[x],text)
    bmhtfi=time.time()
    bmhTime+=bmhtfi-bmhtini
    
print("Naive Time: ",naiveTime)
print("DFA Time: ",dfaTime)
print("KMP Time: ",kmpTime)
print("BMH Time: ",bmhTime)