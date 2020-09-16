class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        while node is not None:
            # Store the node's next node
            nextNode = node.next_node
            # Set the node's next node to be its previous node (first one's prev is None)
            node.next_node = prev
            # Sets the current node to be prev
            prev = node
            # Moves on to the next node until hitting the final node's none and break the while loop
            node = nextNode
        # Sets the final to be the last node(prev)
        self.head = prev