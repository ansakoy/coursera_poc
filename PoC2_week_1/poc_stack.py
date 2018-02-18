# TEMPLATE: http://www.codeskulptor.org/#poc_stack_template.py

"""
Stack class
"""


class Stack:
    """
    A simple implementation of a FILO stack.
    """

    def __init__(self):
        """
        Initialize the stack.
        """
        self.stack = list()

    def __len__(self):
        """
        Return number of items in the stack.
        """
        return len(self.stack)

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return str(self.stack)

    def push(self, item):
        """
        Push item onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Pop an item off of the stack
        """
        return self.stack.pop(-1)

    def clear(self):
        """
        Remove all items from the stack.
        """
        self.stack = list()


def test():
    my_stack = Stack()
    my_stack.push(0)
    my_stack.push(3)
    my_stack.push(4)
    print 'expected {}, result {}'. format([0, 3, 4], my_stack)
    my_stack.pop()
    print 'expected {}, result {}'.format([0, 3], my_stack)
    my_stack.push(6)
    my_stack.push(7)
    my_stack.push(8)
    print 'expected {}, result {}'.format([0, 3, 6, 7, 8], my_stack)
    my_stack.pop()
    my_stack.pop()
    print 'expected {}, result {}'.format([0, 3, 6], my_stack)


# test()

def home_work_test():
    ############################
    # test code for the stack

    my_stack = Stack()
    my_stack.push(72)
    my_stack.push(59)
    my_stack.push(33)
    my_stack.pop()
    my_stack.push(77)
    my_stack.push(13)
    my_stack.push(22)
    my_stack.push(45)
    my_stack.pop()
    my_stack.pop()
    my_stack.push(22)
    my_stack.push(72)
    my_stack.pop()
    my_stack.push(90)
    my_stack.push(67)
    while len(my_stack) > 4:
       my_stack.pop()
    my_stack.push(32)
    my_stack.push(14)
    my_stack.pop()
    my_stack.push(65)
    my_stack.push(87)
    my_stack.pop()
    my_stack.pop()
    my_stack.push(34)
    my_stack.push(38)
    my_stack.push(29)
    my_stack.push(87)
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    return my_stack.pop()