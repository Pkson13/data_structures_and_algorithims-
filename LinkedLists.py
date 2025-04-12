class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    # def __str__(self):
    #     return self.data
    
    def __repr__(self):
        return self.data

class Linked_list:
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        current = self.head
        node = []
        
        while current:
            node.append(current.data)
            current = current.next_node
        return " -> ".join(node)
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count
    
    def sum_of_data(self):
        sum = 0
        current = self.head
        while current:
            sum += self.head.data
            current = current.next_node.data
        return sum
    
    def add_node_to_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return self.head
    
    def add_node_to_tail(self, node_name):
        current = self.head

        while current.next_node:
            current = current.next_node
        
        new_node = Node(node_name)
        current.next_node = new_node
        return new_node

    def search(self, target):
        current = self.head
        node = 1
        while current:
            if current.data == target:
                return f'found at node {node}'
            node += 1 
            current = current.next_node

    def insert_node(self, index, data):
        if index == 0:
            first = self.add_node_to_head(data)
            return first
        position = 1
        current = self.head
        while position != index:
            current = current.next_node
            position += 1
        next_node = current.next_node
        new_node = Node(data)
        new_node.next_node = next_node
        current.next_node = new_node
        return new_node
            

            
            
