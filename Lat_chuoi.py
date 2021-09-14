s=""
str="tHE fOX iS cOMING fOR tHE cHICKEN"
l=str.split(" ")
n= len(l)
for i in range(0,n):
    s = s + l[n-i-1] + " "
s1 = ""

for i in s:
    if i.isupper():
        i=i.lower()
    else:
        i=i.upper()

    s1 = s1 + i + " "

print(s1)
