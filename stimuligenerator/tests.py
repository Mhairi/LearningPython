import unittest
from stimuligenerator import GenerateSelf, GeneratePartner, GenerateGroupvsPartner
from stimuligenerator import GenerateGroupvsSelf, GenerateSelfvsPartner

#These 4 classes simply test if the first object returns what it should 
#(e.g., that the self-interest stimuli give more to the self than the
#other person).

class SelfInterestTests(unittest.TestCase): #Takes an array of two numbers, self vs. other (e.g., [75,25]).
    def test_self_more_than_other(self):
        for i in xrange(1,100): #Run this 100 times to be sure
            selfvalues = GenerateSelf() #Assign the results of GenerateSelf to the variable selfvalues
            isselfmore = selfvalues[0] > selfvalues[1] #Returns true if self is more than other
            self.assertTrue(isselfmore) #Our testcondition - will FAIL if not True
    
class PartnerInterestTests(unittest.TestCase):
    def test_other_more_than_self(self):
        for i in xrange(1,100): #Run this 100 times
            partnervalues = GeneratePartner() #Assign our two integer array to the variable partner values
            ispartnermore = partnervalues[1] > partnervalues[0] #Returns true if partner gets more than self
            self.assertTrue(ispartnermore)

class GroupInterestTests(unittest.TestCase):
    def test_group_vs_partner(self):
        for i in xrange(1,100):#Run this 100 times
            grouparray = GenerateGroupvsPartner()
            #Next, we create a variable that tests whether the sum of the first array in grouparray is larger
            #than that of the second array
            isgroupmore = (grouparray[0][0] + grouparray[0][1]) > (grouparray[1][0] + grouparray[1][1])
            isgroupmore = grouparray[1][0] < grouparray[1][1] #Remains true if self gets less than partner in other option
            self.assertTrue(isgroupmore)

    def test_group_vs_self(self):
        for i in xrange(1,100): #Run this 100 times
            grouparray = GenerateGroupvsSelf()
            isgroupmore = (grouparray[0][0] + grouparray[0][1]) > (grouparray[1][0] + grouparray[1][1])
            isgroupmore = grouparray[1][0] > grouparray[1][1] #Remains true if self gets more than partner in other option
            self.assertTrue(isgroupmore)
    
    def test_self_vs_partner(self):
        for i in xrange(1,100): #Run this 100 times
            currentarray = GenerateSelfvsPartner()
            isresultcorrect = currentarray[0][0] > currentarray[0][1]
            isresultcorrect = currentarray[1][0] < currentarray[1][1]
            self.assertTrue(isresultcorrect)
            
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()