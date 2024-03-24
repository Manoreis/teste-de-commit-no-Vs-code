"""
Modelo da arvore binária:

       'O'
     /     \
   'A'      'I'
  /   \    /   \
'P'   'M''R'   'C'
     /   \
   'r'    '.'
         /   \
       'o'   'f'
"""
from pos_ordem import BinaryTree, Node
# arvore pós-ordem
def postorder_exemplo_tree():
#instanciando arvore binária
    tree = BinaryTree()

#instanciando nós da árvore e seus respectivos valores
    n6 = Node('A')
    n9 = Node('I')
    n1 = Node('P')
    n5 = Node('M')
    n2 = Node('r')
    n4 = Node('.')
    n7 = Node('R')
    n3 = Node('f')
    n0 = Node('O')
    n10 = Node('o')
    n8 = Node('C')
# instanciando endereco dos nós
    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n4.left = n10 
    n9.left = n8
    n8.right = n7
#definindo a raiz da árvore
    tree.root = n0
#retornando a árvore   
    return tree
    
    
if __name__ == "__main__":
    tree = postorder_exemplo_tree()
    print("Percurso em pós ordem:")
    tree.postorder()
    print() 
   

    