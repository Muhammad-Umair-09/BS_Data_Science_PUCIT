a = 2222
b = 3.14

fs1 = f"the value of a is {a} and that of b is {b}"  # fstring, the simple way of joining message and data in variables
print(fs1)

c = -2 + 4j
print(f"a complex number is {c}")
fs2 = f"the value of its real part is {c.real} and its imaginary part is {c.imag}"
print(fs2)

print("-----------")

print("the value of a is {} and b is {} ".format(a, b))  # :5d  :nn.dd
print("the value of a is {} and b is {} ".format(a, b))  # :5d  :nn.dd
print("the value of b is {1} and a is {0} ".format(a, b))  # :5d  :nn.dd
print("the value of a is {:8d} and b is {:12.4f} ".format(a, b))
print("the value of a is {:<+8d} and b is {:12.4f} ".format(a, b))
print("the value of a is {:+<+8d} and b is {:<12.4f} ".format(a, b))
print("the value of a is {:0>8d} and b is {:12.4f} ".format(a, b))

print("-----------")   # better to use format instead % operator

print("a = %d and b = %f"%(a,b))
print("a = %8d and b = %12.3f"%(a,b))
print("a = %20d and b = %+20.1f"%(a,b))
