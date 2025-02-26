# test_binary_tree.py

import unittest
from binary_tree import TreeNode, max_depth

class TestBinaryTree(unittest.TestCase):
    def test_normal_cases(self):
        """
        Tests typical tree structures.
        """
        root = TreeNode("Are you interested in loans?")
        root.yes = TreeNode("Do you have a high credit score?")
        root.no = TreeNode("Are you looking for short-term financial help?")
        root.yes.yes = TreeNode("You qualify for a premium loan.")
        root.yes.no = TreeNode("You qualify for a standard loan.")
        root.no.yes = TreeNode("Consider a personal loan.")
        root.no.no = TreeNode("Consider financial counseling.")

        self.assertEqual(max_depth(root), 3)  # Maximum depth should be 3

    def test_edge_cases(self):
        """
        Tests edge cases like single-node tree, deep left-skewed tree, and empty tree.
        """
        # Edge Case 1: Single-node tree
        single_node = TreeNode("Only one question")
        self.assertEqual(max_depth(single_node), 1)

        # Edge Case 2: Left-skewed tree (all 'Yes' responses)
        left_skewed = TreeNode("Start")
        left_skewed.yes = TreeNode("Q1")
        left_skewed.yes.yes = TreeNode("Q2")
        left_skewed.yes.yes.yes = TreeNode("Q3")
        self.assertEqual(max_depth(left_skewed), 4)

        # Edge Case 3: Empty tree
        self.assertEqual(max_depth(None), 0)

if __name__ == "__main__":
    unittest.main()
