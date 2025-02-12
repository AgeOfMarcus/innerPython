# Author: Marcus Weinberger

class Test:
    def __init__(self, value):
        self._value = value
    def __getitem__(self, index):
        if type(index) == slice:
            return 'yea buddy', index.start, index.stop, index.step
        return self._value

test = Test('hello')
print(test[0:1])