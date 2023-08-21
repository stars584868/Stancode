class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ds = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.ds.append(val)
        else:
            if self.mins[-1] > val:
                self.mins.append(val)
        self.ds.append(val)

    def pop(self) -> None:
        if len(self.ds) != 0:
            num = self.ds.pop()
            if num == self.mins[-1]:
                self.mins.pop()

    def top(self) -> int:
        if len(self.ds) != 0:
            return self.ds[-1]  # 倒數第1個

    def get_min(self) -> int:
        if len(self.ds) != 0:
            return self.mins[-1]


if __name__ == '__main__':
    my_stack = MinStack()
    print(my_stack.top(), end=', ')
    print(my_stack.get_min(), end=', ')
    my_stack.pop()
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top(), end=', ')
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top())
