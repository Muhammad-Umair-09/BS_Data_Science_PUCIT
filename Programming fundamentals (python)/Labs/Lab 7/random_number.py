from random import randint

j = 0
while j <= 9:
    rno = randint(22, 88)
    print("a random number is:", rno)
    j = j+1
    
# the code end at above line, following are comments and
# compilers/interpreters ignore them completely

# this code demonstrate to generate random numbers
# we need to add the line no 1 as it is (no need here to understand it fully)
# the builtin function randint will generate a random number
# everytime it is called, which is different from previous
# it generate random number between its parameters
# so in example the random number generated is between
# 22 and 88


# If you are not comfortable with random numbers
# use input and reduce the iterations of the loop
# from a big number to a smaller value
