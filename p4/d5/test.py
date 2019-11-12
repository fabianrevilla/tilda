import unittest
from bintree import *

#b=Bintree()
#b.store("ogge",18)



#
#b.store("abbe",17)
#
#b.store("kalle",4)
#b.write()
#x=b.search("henke")
#print(x)
#print(b.root.key)
#print(b.root.value)

class BintreeTest(unittest.TestCase):
    
    def testInsert(self):
        #""" Testar Subj och Pred """
        b = Bintree()
        b.store("adam", 123)
        self.assertEqual(b.root.key,"adam")
        self.assertEqual(b.root.value,123)

    def testInsertMore(self):
        b = Bintree()
        b.store("danne",22)
        b.store("jonte",13)
        b.store("abbe",19)
        self.assertEqual(b.root.left.key,"abbe")
        self.assertEqual(b.root.right.key,"jonte")
    
        
    def testSearch(self):
        b = Bintree()
        b.store("danne",22)
        b.store("jonte",13)
        b.store("abbe",19)
        with self.assertRaises(KeyError):
            b.search("eva")
        self.assertEqual(b.search("jonte"),13)

    def testContains(self):
        b=Bintree()
        b.store("adam", 123)
        self.assertEqual("eva" in b,False)
        self.assertEqual("adam" in b,True)

if __name__ == '__main__':
    unittest.main()

