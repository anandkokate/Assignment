import hashlib
import base64
import mmh3
class BloomFilter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.data = [0]*m
        self.n = 0
    def insert(self, element):
        if self.k == 1:
            
            hash1 = mmh3.hash(element,41) % self.m
            self.data[hash1] = 1
        elif self.k == 2:
            hash1 = mmh3.hash(element,41) % self.m
            hash2 = mmh3.hash(element,42) % self.m
            self.data[hash1] = 1
            self.data[hash2] = 1
        self.n += 1
    def search(self, element):
        
        if self.k == 1:
            hash1 = mmh3.hash(element,41) % self.m
            if self.data[hash1] == 0:
                return "Not in Bloom Filter"
        elif self.k == 2:
            
            hash1 = mmh3.hash(element,41) % self.m
            hash2 = mmh3.hash(element,42) % self.m
            if self.data[hash1] == 0 or self.data[hash2] == 0:
                return "Not in Bloom Filter"
        prob = (1.0 - ((1.0 - 1.0/self.m)**(self.k*self.n))) ** self.k
        return "Might be in Bloom Filter with false positive probability "+str(prob)

bloom=BloomFilter(50,2)
usernames=['anand','shubham','Ajay','shivaji','Shreenath','chaitanya','Nitin']
for name in usernames:
    bloom.insert(name)
    
username=input('Enter Username:')
b=bloom.search(username)
print(b)

