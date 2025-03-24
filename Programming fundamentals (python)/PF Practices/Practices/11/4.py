import random
import string
i=1
while i<=10:
    a=(random.choice(string.ascii_uppercase))
    if a=="A" or a=="I" or a=="E" or a=="O" or a=="U":
        print("Vowel")
    else:
        print("Consonant")
    i=i+1
