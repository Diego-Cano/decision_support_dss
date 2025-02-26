# binary_tree.py

class TreeNode:
    """Represents a node in the decision support binary tree."""
    def __init__(self, question):
        self.question = question  # The question at this node
        self.yes = None  # Left child (Yes branch)
        self.no = None   # Right child (No branch)

def max_depth(root):
    """
    Recursively calculates the maximum depth of a binary tree.
    
    """
    if not root:
        return 0  # Base case: if tree is empty

    left_depth = max_depth(root.yes)
    right_depth = max_depth(root.no)

    return 1 + max(left_depth, right_depth)  # Depth formula
