from sorting import bubbleSort

class pair:
   def __init__(self, f, s):
      self.first = f
      self.second = s

   def __repr__(self):
      return "Klass:("+str(self.first)+", "+str(self.second)+")"

#   def __str__(self):
#     return "("+str(self.first)+", "+str(self.second)+")"

def naturalComparer(a, b):
   return a > b

def pairComparer(a, b):
   return abs(a.first-a.second) > abs(b.first-b.second)

data = [-2, 45, 10, 1, -9]
#data = ["Jamal", "Zaid", "Arshad", "Qamar", "Majeed"]
#data = [pair(99,24), pair(71,0), pair(45,89), pair(-5,35), pair(-2,12)]
print('Data in the Array')
print(data)

bubbleSort(data, naturalComparer)

print('Sorted Array in Ascending Order')
print(data)


