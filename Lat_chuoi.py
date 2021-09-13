str="tHE fOX iS cOMING fOR tHE cHICKEN"
l=str.split(" ")
n= len(l)
for i in range(0,n):
    s = s + l[n-i-1].lower() + " "
print(s)