import mmh3
from bitarray import bitarray

class BloomFilter(set):
 
    def __init__(self, size, hash_count):
        super(BloomFilter, self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.size = size
        self.hash_count = hash_count
 
    def __len__(self):
        return self.size
 

    def __iter__(self):
        return iter(self.bit_array)
 

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1
 
        return self
 

    def __contains__(self, item):
        out = True
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                out = False
 
        return out
 

bloom = BloomFilter(100, 10)
usernames=['anand','shubham','Ajay','shivaji','Shreenath','chaitanya','Nitin','Ankush','Rushikesh','Ram','Abhijit']

for name in usernames:
    bloom.add(name)
    
username=input('Enter username:')

if username in bloom:
    print(username,'is already present')
else:
    print('valid username')
   
