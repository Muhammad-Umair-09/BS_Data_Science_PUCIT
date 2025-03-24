def mile2km(miles):
    return miles* 1.60934

c=["Kasur", "Multan", "Karachi", "Sialkot", "Quetta"]
d=[8,57,279,18,325]
i=0
while i< len(d):
    print(c[i], mile2km(d[i]))
    i=i+1
