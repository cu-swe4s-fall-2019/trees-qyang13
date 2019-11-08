import binary_tree as bt
import unittest


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree_insert(self):
        '''
        Unit test for insert function of binary tree
        '''
        tree = None
        tree = bt.insert(tree, 5, 'val1')
        tree = bt.insert(tree, 6, 'val2')
        tree = bt.insert(tree, 4, 'val3')
        tree = bt.insert(tree, 5, 'val4')

        self.assertEqual(tree.key, 5)
        self.assertEqual(tree.right.key, 6)
        self.assertEqual(tree.left.key, 4)
        self.assertEqual(tree.right.left.key, 5)
        self.assertEqual(tree.value, 'val1')
        self.assertEqual(tree.right.value, 'val2')
        self.assertEqual(tree.left.value, 'val3')
        self.assertEqual(tree.right.left.value, 'val4')

    def test_binary_tree_search(self):
        '''
        Unit test for search function of binary tree
        '''
        tree = None
        tree = bt.insert(tree, 5, 'val1')
        tree = bt.insert(tree, 6, 'val2')
        tree = bt.insert(tree, 4, 'val3')

        self.assertEqual(bt.search(tree, 5), 'val1')
        self.assertEqual(bt.search(tree, 6), 'val2')
        self.assertEqual(bt.search(tree, 4), 'val3')
        self.assertEqual(bt.search(tree, 0), None)


if __name__ == '__main__':
    unittest.main()
