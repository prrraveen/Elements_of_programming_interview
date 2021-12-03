class DoublyListNode:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '

            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' -> ... -> '

                result += str(node.data)
                result += ' -> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next

        return result

    def __str__(self):
        return self.__repr__()
