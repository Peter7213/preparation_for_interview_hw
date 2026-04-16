class Stack:

    def __init__(self, arr):
        self.arr = arr

    def is_empty(self):                                     #По названию функции: если пуст, то правда
        if self.arr:
            return False
        return True

    def remove(self, target_element):
        self.arr.remove(target_element)
        return

    def push(self, new_element):
        self.arr = self.arr + new_element

    def pop(self):
        pop_ = self.arr[-1]
        self.arr = self.arr[:-1]
        return pop_

    def peek(self):
        return self.arr[-1]

    def size(self):
        return len(self.arr)

    def count(self, item):
        return self.arr.count(item)

    def __getitem__(self, index):                   #Нагуглил конечно
        return self.arr[index]

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > len(self.arr):
            raise StopIteration
        return self.arr[self.counter]


if __name__ == '__main__':

    x = Stack('}{}')

    # print(x.is_empty())
    x.push('[')
    print(vars(x))
    print(x.pop())
    print(x.peek())
    print(x.size())
