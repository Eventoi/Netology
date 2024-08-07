class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пустой')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Стек пустой')
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_balanced(string):
    stack = Stack()
    for char in string:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return 'Несбалансированно'
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                return 'Несбалансированно'
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


print(is_balanced('(((([{}]))))'))  # True
print(is_balanced('[([])((([[[]]])))]{}()'))  # True
print(is_balanced('{{[()]}}'))  # True
print(is_balanced('}{'))  # False
print(is_balanced('{{[(])]}}'))  # False
print(is_balanced('[[{())}]'))  # False