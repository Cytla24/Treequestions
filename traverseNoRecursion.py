def inorderTraversal(root: TreeNode) -> List[int]:
        
        stack = []
        done = 0
        current = root
        finalL = []
        
        while True:
            
            if current:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                finalL.append(current.val)
                current = current.right
            else:
                break
        
        return finalL
