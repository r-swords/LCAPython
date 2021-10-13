import unittest

class Node:
 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 

# Returns the Node which contains the lca

def findLCARecursive(root, number_1, number_2, found):
     
    if root is None:
        return None
 
    if root.key == number_1 :
        found[0] = True
        return root
 
    if root.key == number_2:
        found[1] = True
        return root
 
    left_lca = findLCARecursive(root.left, number_1, number_2, found)
    right_lca = findLCARecursive(root.right, number_1, number_2, found)
 
    if left_lca and right_lca:
        return root
 
    return left_lca if left_lca is not None else right_lca
 

# Determinse whether a value is in the tree

def find(root, k):
     
    if root is None:
        return False
     
    if (root.key == k or find(root.left, k) or
        find(root.right, k)):
        return True
     
    return False
    

# Returns the Node which contains the lca if boht numbers are in the tree, otherwise None 

def findLCA(root, number_1, number_2):
     
    found = [False, False]
 
    lca = findLCARecursive(root, number_1, number_2, found)
 
    if (found[0] and found[1] or found[0] and find(lca, number_2) or found[1] and
        find(lca, number_1)):
        return lca
 
    return None
 


class TestCases(unittest.TestCase):

    def testEmptyTree(self):
        root = None
        self.assertIsNone(findLCA(root, 1, 1))

    def testOneNode(self):
        root = Node(1)
        self.assertEqual(1, findLCA(root, 1, 1).key)

    def testUnbalancedTree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        self.assertEqual(2, findLCA(root, 3, 4).key)
    
    def testBalanceTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(2, findLCA(root, 4, 5).key)
        self.assertEqual(1, findLCA(root, 4, 7).key)
        self.assertEqual(3, findLCA(root, 3, 3).key)
        self.assertIsNone(findLCA(root, 10, 12))
        self.assertIsNone(findLCA(root, 1, 11))
        self.assertIsNone(findLCA(root, 11, 1))


if __name__ == "__main__":
    unittest.main()

