class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f"Too many cookies, max capacity is {self.capacity}")
        self.size += n

    def withdraw(self, n):
        if self.size <= n:
            raise ValueError(f"There are not enough cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0 :
            raise ValueError("Wrong capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
         jar = Jar(4)
         jar.deposit(4)
         jar.withdraw(1)
         print(jar.capacity)
         print(jar.size)
         print(jar)

if __name__=="__main__":
    main()