import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
l=random.randint(0,len(letters)-1)
l=letters[l]
n=random.randint(0,len(numbers)-1)
n=numbers[n]
s=random.randint(0,len(symbols)-1)
s=symbols[s]
'''#print(letters[b])
#print(len(letters))
for i in range(4):
    b+=1
    print(letters[b])
#print(letters[b]+letters[b+b]+letters[b+1]+letters[b+2])
c=random.randint(0,len(letters)-1)
d=random.randint(0,len(letters)-1)
e=random.randint(0,len(letters)-1)
print(letters[b]+letters[c]+letters[d]+letters[e])
output=""
for i in range(4):
    b=random.randint(0,len(letters)-1)
    #print(letters[b])
    output=letters[b]+letters[b]+letters[b]+letters[b]
    print(output)
'''
print(l+l+l+l+n+n+s+s)
