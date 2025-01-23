import unittest
from AVL_Tree import AvlTree



class TestAvlTree(unittest.TestCase):
    def setUp(self):
        self.tree = AvlTree()

    def test_insert_and_balance(self):
        """Test insertion and automatic balancing of the AVL tree."""
        self.tree.insert(10,"Flight 10")
        self.tree.insert(20, "Flight 20")
        self.tree.insert(30,"Flight 30")  

        # 20 should be the root here 
        self.assertEqual(self.tree.root.key, 20)
        self.assertEqual(self.tree.root.left.key, 10)
        self.assertEqual(self.tree.root.right.key, 30)

    def test_search(self):
        """Test searching for keys in the AVL tree."""
        self.tree.insert(10,"Flight 10")
        self.tree.insert(20, "Flight 20")

        # existing key
        node = self.tree.search(self.tree.root, 10)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, "Flight 10")

        #  non-existing key
        node = self.tree.search(self.tree.root, 30)
        self.assertIsNone(node)

    def test_delete(self):
        """Test deletion and rebalancing of the AVL tree."""
        self.tree.insert(10, "Flight 10")
        self.tree.insert(20,  "Flight 20")
        self.tree.insert(30,"Flight 30")

        self.tree.delete(20)  
        self.assertEqual(self.tree.root.key, 30)
        self.assertEqual(self.tree.root.left.key, 10)
        self.assertIsNone(self.tree.root.right)

    def test_inorder_traversal(self):
        self.tree.insert(10, "Flight 10")
        self.tree.insert(20, "Flight 20")
        self.tree.insert(30, "Flight 30")

        result = list(self.tree.inorder_traversal(self.tree.root))
        self.assertEqual(result, [
            (10,"Flight 10"),
            (20, "Flight 20"),
            (30, "Flight 30"),
        ])

    def test_complex_balancing(self):
        """Test complex insertion and balancing case."""
        keys = [30, 20, 40, 10, 25, 35, 50]
        for key in keys:
            self.tree.insert(key, f"Flight {key}")

        # After all insert, 30 should still be the root
        self.assertEqual(self.tree.root.key, 30)

        # Verify tree structure
        self.assertEqual(self.tree.root.left.key, 20)
        self.assertEqual(self.tree.root.right.key, 40)
        self.assertEqual(self.tree.root.left.left.key, 10)
        self.assertEqual(self.tree.root.left.right.key, 25)
        self.assertEqual(self.tree.root.right.left.key, 35)
        self.assertEqual(self.tree.root.right.right.key, 50)

    def test_delete_and_rebalance(self):
        keys = [30, 20, 40, 10, 25, 35, 50]
        for key in keys:
            self.tree.insert(key, f"Flight {key}")

        self.tree.delete(40)  # Deleting a node with two children
        result = list(self.tree.inorder_traversal(self.tree.root))

        # Ensure the tree remains balanced and the key is deleted
        self.assertEqual(result, [
            (10, "Flight 10"),
            (20, "Flight 20"),
            (25, "Flight 25"),
            (30, "Flight 30"),
            (35, "Flight 35"),
            (50, "Flight 50"),
        ])


if __name__ == "__main__":
    unittest.main()


# i get output if u want see it now :
"""
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
"""