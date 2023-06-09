def NFAApprox(w,q,k):

    configurations=[(1,0,0)]

    #Por si la longitud es distinta
    while len(w)>len(q):
        q+=" "

    while len(configurations) != 0:

        current_configuration = configurations.pop(0)
        print(current_configuration)

        if current_configuration[0]>(len(w)+1)*(k+1):
            continue

        #accepting states
        if current_configuration[0]%(len(w)+1)==0:
            errors=current_configuration[0]/(len(w)+1)-1
            return True

        if w[current_configuration[1]] == q[current_configuration[2]]:
            #match, next state is i+1 j+1 state+1
            configurations.append((current_configuration[0]+1,current_configuration[1]+1,current_configuration[2]+1))
        else:
            #mismatch
            configurations.append((current_configuration[0]+len(w)+2,current_configuration[1]+1,current_configuration[2]+1))

        #deletion
        configurations.append((current_configuration[0]+len(w)+2,current_configuration[1]+1,current_configuration[2]))

        #insertion
        configurations.append((current_configuration[0]+len(w)+1,current_configuration[1],current_configuration[2]+1))


    return False

print(NFAApprox("survey","survessssy",2))
