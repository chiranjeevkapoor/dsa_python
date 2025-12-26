                                
 # Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to get the left
# and right view of the binary tree
class Solution:
    def rightsideView(self, root):
        # Vector to store the result
        res = []
        
        # Call the recursive function
        # to populate the right-side view
        self.recursionRight(root, 0, res)
        
        return res

    def leftsideView(self, root):
        # Vector to store the result
        res = []
        
        # Call the recursive function
        # to populate the left-side view
        self.recursionLeft(root, 0, res)
        
        return res

    # Recursive function to traverse the
    # binary tree and populate the left-side view
    def recursionLeft(self, root, level, res):
        # Check if the current node is None
        if not root:
            return
        
        # Check if the size of the result list
        # is equal to the current level
        if len(res) == level:
            # If equal, add the value of the
            # current node to the result list
            res.append(root.data)
        
        # Recursively call the function for the
        # left child with an increased level
        self.recursionLeft(root.left, level + 1, res)
        
        # Recursively call the function for the
        # right child with an increased level
        self.recursionLeft(root.right, level + 1, res)

    # Recursive function to traverse the
    # binary tree and populate the right-side view
    def recursionRight(self, root, level, res):
        # Check if the current node is None
        if not root:
            return
        
        # Check if the size of the result list
        # is equal to the current level
        if len(res) == level:
            # If equal, add the value of the
            # current node to the result list
            res.append(root.data)
            
            # Recursively call the function for the
            # right child with an increased level
            self.recursionRight(root.right, level + 1, res)
            
            # Recursively call the function for the
            # left child with an increased level
            self.recursionRight(root.left, level + 1, res)

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

solution = Solution()

# Get the Right View traversal
rightView = solution.rightsideView(root)

# Print the result for Right View
print("Right View Traversal:", end=" ")
for node in rightView:
    print(node, end=" ")
print()

# Get the Left View traversal
leftView = solution.leftsideView(root)

# Print the result for Left View
print("Left View Traversal:", end=" ")
for node in leftView:
    print(node, end=" ")
print()
                                
                            