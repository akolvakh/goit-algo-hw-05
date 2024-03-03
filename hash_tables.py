class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return None
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)

        if self.table[key_hash] is None:
            return None

        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                return self.table[key_hash].pop(i)
        return None


H = HashTable(10)

H.insert("Kendrick Lamar", "DNA")
H.insert("Drake", "0 - 100")
H.insert("Weeknd", "I feel it come in")
H.insert("Asap Rocky", "D.M.B.")
H.insert("Travis Scott", "Sicko mode")
H.insert("21 Savage", "A lot")
H.insert("Mishlawi", "That's Me")
H.insert("Tame Impala", "Let it happen")
H.insert("Thundercat", "Them Changes")
H.insert("Tory Lanez", "Lavender Sunflower")
H.insert("Vic Rose", "God's plan")
H.delete("Vic Rose")

print(H.get("Kendrick Lamar"))
print(H.get("Drake"))
print(H.get("Weeknd"))
print(H.get("Asap Rocky"))
print(H.get("Travis Scott"))
print(H.get("21 Savage"))
print(H.get("Mishlawi"))
print(H.get("Tame Impala"))
print(H.get("Thundercat"))
print(H.get("Tory Lanez"))

assert H.get("Vic Rose") is None




