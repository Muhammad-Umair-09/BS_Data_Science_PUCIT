import gc

class SomeObj:
    h = 90
    def __del__(self):
        print('The object is destroyed.')

print(111111)
obj1 = SomeObj()
print(222222)
obj1 = SomeObj()
print(333333)
#del obj1
print(444444)
#obj1 = None
print(555555)

for i in range(3):
    arr = [0]
    arr[0] = arr

print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)