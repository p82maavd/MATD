def NFAApprox(w,q,k):
    #(state number, index i index j)
    configurations=[(1,0,0)]

    while len(configurations) != 0:

        #take some configuration from list
        current_configuration = configurations.pop(0)
        print(current_configuration) 
        
        #accepting states      
        if current_configuration[2]>=len(q) and current_configuration[0]%(len(w)+1)==0:

            if current_configuration[0]>(len(w)+1)*(k+1):
                return False
            
            return True

        # out of index
        if current_configuration[1]>=len(w) or current_configuration[2]>=len(q) or current_configuration[0]>(len(w)+1)*(k+1):
            pass
        else:
            
            if w[current_configuration[1]] == q[current_configuration[2]]:
                #match, next state is i+1 j+1 state+1
                configurations.insert(0,(current_configuration[0]+1,current_configuration[1]+1,current_configuration[2]+1))
                
            else:
                #mismatch
                configurations.append((current_configuration[0]+len(w)+2,current_configuration[1]+1,current_configuration[2]+1))

        #deletion
        configurations.append((current_configuration[0]+len(w)+2,current_configuration[1]+1,current_configuration[2]))

        #insertion
        configurations.append((current_configuration[0]+len(w)+1,current_configuration[1],current_configuration[2]+1))


    return False

print(NFAApprox("survey","urveys",2))

