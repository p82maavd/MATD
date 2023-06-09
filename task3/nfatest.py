import unittest

def NFAApprox(w,q,k):
    #(state number, index i index j)
    configuration=[(1,0,0)]

    #while len(q)<len(w):
    #    q+=" "

    print(len(w),len(q))

    while len(configuration) != 0:
        #take some configuration from list
        cc = configuration.pop(0)        

        # check if we are in an accepting state        
        if cc[0] == k and cc[1] == len(w):
            return True

        # check if we are not in a state out of machine or indices i,j out of w,q
        if cc[0] == k+1 or cc[1] > len(w) or cc[2] > len(q):
            continue

        # match
        if cc[1] < len(w) and cc[2] < len(q) and w[cc[1]] == q[cc[2]]:
            configuration.append((cc[0], cc[1]+1, cc[2]+1))                 
        # mismatch
        else:
            configuration.append((cc[0]+1, cc[1]+1, cc[2]+1))

        # deletion 
        configuration.append((cc[0]+1, cc[1]+1, cc[2]))

        #insertion
        configuration.append((cc[0]+1, cc[1], cc[2]+1))


    return False

#print(NFAApprox("survey","surveeey",2))

# The test based on unittest module
class TestErrors(unittest.TestCase):
    def runTest(self):
        maxNumbersOfErrors=4
        self.assertEqual(NFAApprox("survey","surveey",maxNumbersOfErrors), 1, "incorrect number of errors")
        self.assertEqual(NFAApprox("survey","survessy",maxNumbersOfErrors), 2, "incorrect number of errors")
        #self.assertEqual(NFAApprox("survey","durvey",maxNumbersOfErrors), 1, "incorrect number of errors")
        self.assertEqual(NFAApprox("survey","durveys",maxNumbersOfErrors), 2, "incorrect number of errors")
        #self.assertEqual(NFAApprox("survey","urvey",maxNumbersOfErrors), 1, "incorrect number of errors")
 
# run the test
unittest.main()