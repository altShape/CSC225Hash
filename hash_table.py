"""CSC 225 - Hash table starter. Complete the TODO sections."""

# These prime sizes are provided; you do not need to test for prime numbers.
SIZES = [11, 23, 47, 97, 197, 397]


class HashTable:
    def __init__(self, method="linear", hash_method="mod"):
        self.method = method           # linear, quadratic, or chaining
        self.hash_method = hash_method # mod or digit
        self.capacity = 11
        self.count = 0

        if method == "chaining":
            # Each position must have its OWN list.
            # [[]] * 11 would repeat references to the SAME list.
            self.table = [[] for i in range(self.capacity)]
        else:
            self.table = [None] * self.capacity

    def hash_key(self, key):
        # These two hash functions are already provided.
        if self.hash_method == "mod":
            return key % self.capacity
        total = 0
        for digit in str(abs(key)):
            total += int(digit)
        return total % self.capacity

    def probe_index(self, start, i):
        if self.method == "linear":
            return (start + i) % self.capacity
        if self.method == "quadratic":
            return (start + i * i) % self.capacity
        raise NotImplementedError(f"{self.method} is not called yet")
    
    def insert(self, key):
        if self.search(key) is not None:
            print(f"{key} is already in the table.")
            return False
        if self.method == "quadratic":
            if (self.count + 1) / self.capacity > 0.50:
                print(f" limit  of 0.50 reached.")
                return False
        elif self.count >= self.capacity:
            print(f"Table is full.")
            return False
        start = self.hash_key(key)
        for i in range(self.capacity):
            index = self.probe_index(start, i)
            if self.table[index] is None:
                self.table[index] = key
                self.count += 1
                return True
        return False

    def search(self, key):
        start = self.hash_key(key)
        for i in range(self.capacity):
            index = self.probe_index(start, i)
            if self.table[index] is None:
                return None
            if self.table[index] == key:
                return index
        return None

    def resize(self):
        pass

    def show(self):
        print("\nMethod:", self.method, "| Hash:", self.hash_method)
        print("Size:", self.capacity, "| Values:", self.count)
        print("Load factor:", round(self.count / self.capacity, 2))
        for i in range(self.capacity):
            print(i, ":", self.table[i])


#ht = HashTable("linear", "mod")
#ht.insert(10)
#ht.insert(21)
#ht.insert(32)
#ht.insert(43)
#ht.insert(54)
#ht.show()
#print(ht.search(32))
#print(ht.search(999))
#ht.insert(21)
#print(ht.count)
ht = HashTable("quadratic", "mod")
ht.insert(10)
ht.insert(21)
ht.insert(32)
ht.insert(43)
ht.insert(54)
ht.show()
print(ht.search(10))
print(ht.search(21))
print(ht.search(32))
print(ht.search(43))
print(ht.search(54))