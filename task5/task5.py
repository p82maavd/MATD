

import sys
import string
import os


if __name__ == '__main__':

    files=['1-0.txt', '10-0.txt', '100-0.txt', '102-0.txt', '103-0.txt', '107-0.txt', '108-0.txt', '11-0.txt', '110-0.txt', '111-0.txt', '113-0.txt', '116-0.txt', '119-0.txt', '12-0.txt', '120-0.txt', '121-0.txt', '122-0.txt', '124-0.txt', '125-0.txt', '13-0.txt', '131-0.txt', '132-0.txt', '133-0.txt', '134-0.txt', '135-0.txt', '137-0.txt', '140-0.txt', '141-0.txt', '142-0.txt', '143-0.txt', '144-0.txt', '145-0.txt', '147-0.txt', '149-0.txt', '15-0.txt', '153-0.txt', '155-0.txt', '158-0.txt', '16-0.txt', '160-0.txt', '161-0.txt', '163-0.txt', '165-0.txt', '166-0.txt', '167-0.txt', '17-0.txt', '171-0.txt', '174-0.txt', '176-0.txt', '177-0.txt', '178-0.txt', '179-0.txt', '18-0.txt', '19-0.txt', '20-0.txt', '21-0.txt', '22-0.txt', '23-0.txt', '24-0.txt', '26-0.txt', '27-0.txt', '32-0.txt', '35-0.txt', '36-0.txt', '41-0.txt', '43-0.txt', '44-0.txt', '45-0.txt', '46-0.txt', '47-0.txt', '51-0.txt', '55-0.txt', '60-0.txt', '70-0.txt', '71-0.txt', '72-0.txt', '74-0.txt', '76-0.txt', '77-0.txt', '78-0.txt', '82-0.txt', '83-0.txt', '84-0.txt', '86-0.txt', '91-0.txt', '93-0.txt', '94-0.txt', '95-0.txt', '98-0.txt']
    for x in range(len(files)):
        files[x]=files[x][0:files[x].find("-")]
    print(files)
    
    dictionary= {}
    
    if len(sys.argv) >= 0:
        cont=0
        for f in files:
            print(f)
            cont+=1
            infile = open("gutenberg/"+f+"-1.txt", 'r',errors="ignore")
            nameoutfile="dictionary.txt"
            outfile= open(nameoutfile,"w")

            while 1:
                

                line = infile.readline()
                    
                if line == '':
                    break
                
                if line != "\n":
                    
                    words=line.split(" ")
                    #print(words)

                    for word in range(len(words)):
                        if words[word]=="" or words[word]=="\n" or words[word]==" ":
                            continue
                        #Fix this
                        if word==len(words)-1:
                            if dictionary.get(words[word][0:-1])!=None:
                                dictionary[words[word][0:-1]].add(int(f))
                            else:
                                dictionary[words[word][0:-1]]=set()
                                dictionary[words[word][0:-1]].add(int(f))
                        #dictionary.update({words[word]: f})
                        if dictionary.get(words[word])!=None:
                            dictionary[words[word]].add(int(f))
                        else:
                            dictionary[words[word]]=set()
                            dictionary[words[word]].add(int(f))

            infile.close()

        for x in dictionary:
            
            lista=list(dictionary[x])
            lista.sort()
            lista=str(lista).replace("[","").replace("]","")
            cad = x+": "+str(lista)+"\n\n"
            outfile.write(cad)

        outfile.close()
            #print("Words of file: ",listofwords)

        while True:
            print("")
            print("Introduce two words to obtain in which files contain them")
            first=input("First Word: ")
            second=input("Second Word: ")

            set1=dictionary[first]
            #print(set1)
            set2=dictionary[second]
            #print(set2)
            intersection=list(set1.intersection(set2))
            intersection.sort()
            
            print(first, " and ", second, "appear in files: ",intersection)