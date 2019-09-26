import copy


class node():
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
  
class tree():
  def __init__(self):
    self.root = None


def traverse(node, finalL):
  if node:
    finalL = traverse(node.left, finalL)
    finalL.append(node.val)
    finalL = traverse(node.right, finalL)
  return finalL

def check(node):
  listA = traverse(node, [])
  print (listA)
  i = 0
  while i + 1 < len(listA):
    if listA[i] > listA[i+1]:
      return False
    i +=1
  return True

y = tree()
y.root = node(4)
data1 = node(1)
data7 = node(7)
data0=node(0)
data2=node(2)
data5=node(3)
data9=node(9)
y.root.left = data1
y.root.right = data7
data1.left=data0
data1.right=data2
data7.left=data5
data7.right=data9

print(check(y.root))
