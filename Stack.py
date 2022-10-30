import random


class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class Stack:
    def __init__(self):
        self.first = None
        self.size = 0
        self.delStack = Stack
    def append(self,data):
        if data is not None:
                self.first = Node(data,self.first)
                self.size +=1
        else:
            string = input('Взять элемент из вспомогательного списка ?(Y/N): ')
            if(string.lower() == "y"):
                self.first = self.delStack.first
            elif(string.lower()=="n"):
                self.first = Node(data,self.first)
                self.size +=1
            else:
                print("Введён неверный аргумент.")
    def appendRand(self,start, end,time):
        for i in range(time):
            self.append(random.randint(start,end))
            self.size +=1
    def pop(self):
        node = self.first
        delStack = Stack()
        string = input('Удалить элемент полностью ?(Y/N): ')
        if (string.lower() == "y"):
            if(node is not None):
                self.first= node.next
                node.next = None
                return node.data
            else:
                raise Exception('Пустой стэк.')
        elif(string.lower() == "n"):
            delStack.append(node.data)
        else:
            print("Неправильный аргумент")
    def getSize(self):
        return self.size
    def __iter__(self):
        node=self.first
        while node is not None:
            yield node
            node=node.next
    def iterate(self):
        current = self.first
        num = 0
        while current:
            num +=1
            val = current.data
            current = current.next
            yield str(num) +'-й элемент в очереди ->'+ str(val)
    def isEmpty(self):
        return self.first == None
stack = Stack()
stack.append(5)
print('Norm')
for i in stack.iterate():
    print(i)
