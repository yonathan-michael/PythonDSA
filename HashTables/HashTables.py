class HashTable:
    def __init__(self):
        self.max = 100
        self.table = [[] for i in range(self.max)]

    def get_hash(self, key):
        return key % self.max

    def add_item(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, item in enumerate(self.table[h]):
            if self.table[h][index][0] == key:
                self.table[h][index] = (key, value)
                found = True
                break
        if not found:
            self.table[h].append((key, value))

    def get_item(self, key):
        h = self.get_hash(key)
        for item in self.table[h]:
            if item[0] == key:
                return item[1]

    def delete_item(self, key):
        h = self.get_hash(key)
        for i in range(len(self.table[h])):
            if self.table[h][i][0] == key:
                del self.table[h][i]

    def print_table(self):
        for list in self.table:
            print(list)


t = HashTable()
f = open("myFile0.csv", "r")
f.readline()
for line in f:
    split = line.split(",")
    t.add_item(int(split[0]), split[1][:-1])

print(t.print_table())

