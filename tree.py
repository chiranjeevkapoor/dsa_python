from collections import deque      
from typing import List
from collections import deque         
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else: 
            self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
    def inOrderTraversal(self, root):
        res=[]
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res.extend(self.inOrderTraversal(root.right))
        return res

    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res.extend(self.preOrderTraversal(root.left))
            res.extend(self.preOrderTraversal(root.right))
            
        return res
    
    def postOrderTraversal(self, root):
        res = []
        if root:
            res.extend(self.postOrderTraversal(root.left))
            res.extend(self.postOrderTraversal(root.right))
            res.append(root.data)
        return res
    
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans
    
    def rightViewlevel(self, root):
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size-1:
                    ans.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

    
    def leftViewlevel(self, root):
        ans = []
        if not root:
            return ans
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == 0:
                    ans.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
    def zigzagLevelOrder(root):
        ans = []
        if not root:
            return []
        q = deque([root])
        left_to_right=True
        while q:
            size = len(q)
            level = deque()
            for i in range(size):
                node = q.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            left_to_right = not left_to_right
            ans.append(list(level))
            
        return ans
    # def leftViewRecursion(self, root):
    #     res = []


    # def rightView(node, level)

    def iterpreOrderTrav(self, root):
        if root is None:
            return []

        ##root left right
        res = []

        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    
    def iterpostOrderTrav(self, root):
        if root is None:
            return []
        postorder = []
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node.data)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        stack2.reverse()
        return stack2
    
    def iterpost(self, root):
        postorder = []
        stack = []
        current = root

        while current or len(stack)!=0:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack[-1].right:
                    stack.append(stack[-1].right)
                    current = stack[-1].right
                else:

                # else:
                #     popped_node = stack.pop()
                #     postorder.append(popped_node.data)
        
        # return postorder
    
    
        


    
    







root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(2)
# print(root.printTree())
# print(root.inOrderTraversal(root))  
# print(root.preOrderTraversal(root))
print(root.postOrderTraversal(root))
# print(root.iterpreOrderTrav(root))
# print(root.levelOrder(root))
# print(root.rightViewlevel(root))
# print(root.leftViewlevel(root))
print(root.iterpostOrderTrav(root))
print(root.iterpost(root))