import ctypes
import random

ArrayType = ctypes.c_int * 5  # c_int is C integer type and * 5 means 5 C type integers, the array of 5
slots = ArrayType()

for i in range(5):
    slots[i] = i * i

for v in slots:
    print(v)
