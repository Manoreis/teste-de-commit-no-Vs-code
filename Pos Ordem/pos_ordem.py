# Estruturas de Dados Avançados
# Pesquisa binária - Pós Ordem
# Classe do Nó da Árvore Binária


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

# Classe da Árvore Binária
class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA:
    # Percurso em pós ordem (o correto é "postorder" em inglês) 
    # O parametro self é o objeto da classe BinaryTree
    def postorder(self, node=None):
        # o parametro node é o nó da árvore, que é um objeto da classe Node
        # se o nó for nulo, o nó é a raiz da árvore
        if node is None:
            node = self.root
        # se o nó tiver um filho à esquerda, chama a função recursivamente    
        if node.left:
            self.postorder(node.left)
        # se o nó tiver um filho à direita, chama a função recursivamente
        if node.right:
            self.postorder(node.right)
        # imprime o nó
        print(node, end=' ')


      
