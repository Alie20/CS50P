class Jar:
    def __init__(self, capacity=12):
        if capacity <0 :
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪"*self.size)

    def deposit(self, n):
        if self._size+n >12:
            raise ValueError
        self._size += n


    def withdraw(self, n):
        if self._size < n :
            raise ValueError
        if self._size-n <0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
def main():

    jar = Jar()
    jar.deposit(2)
    jar.deposit(1)
    jar.deposit(1)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()