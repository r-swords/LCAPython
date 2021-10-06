import unittest

class Node:
 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 

def findLCARecur(root, n1, n2, v):
     
    if root is None:
        return None
 
    if root.key == n1 :
        v[0] = True
        return root
 
    if root.key == n2:
        v[1] = True
        return root
 
    left_lca = findLCARecur(root.left, n1, n2, v)
    right_lca = findLCARecur(root.right, n1, n2, v)
 
    if left_lca and right_lca:
        return root
 
    return left_lca if left_lca is not None else right_lca
 
 
def find(root, k):
     
    if root is None:
        return False
     
    if (root.key == k or find(root.left, k) or
        find(root.right, k)):
        return True
     
    return False
 
def findLCA(root, n1, n2):
     
    v = [False, False]
 
    lca = findLCARecur(root, n1, n2, v)
 
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and
        find(lca, n1)):
        return lca
 
    return None
 
class TestCases(unittest.TestCase):

    def test_empty_tree(self):
        root = None
        self.assertIsNone(findLCA(root, 1, 1))

    def test_one_node(self):
        root = Node(1)
        self.assertEqual(1, findLCA(root, 1, 1).key)

    def test_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        self.assertEqual(2, findLCA(root, 3, 4).key)
    
    def test_balance_tree(self):
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

