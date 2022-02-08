class Set_of_stack:
    def __init__(self, init: [int] = []):
        self._data = [[]]
        self._limit = 5
        self._size = 0
        for x in init:
            self.push(x)


    def push(self, x):
        if not self._data[-1]:
            self._data.append([])

        if len(self._data[-1]) < self._limit:
            self._data[-1].append(x)
        else:
            self._data.append([x])
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise ValueError("stack is empty")
        else:
            x = self._data[-1].pop()
            if len(self._data[-1]) == 0:
                del self._data[-1]
            self._size -= 1
            return x

    def peak(self):
        if self._size == 0:
            raise ValueError("stack is empty")
        else:
            return self._data[-1][-1]

    def __len__(self):
        return self._size