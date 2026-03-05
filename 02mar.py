# s = {1,2,3,4,5}

# s.add(6)          # adding element

# fs = frozenset(s) # convert set → frozenset
# print(type(fs))

# fs.add(10)        # trying to modify


#what is range

# r=range(0,-100,-10)
# print(r)
# r=range(5)

# s="instagram"
# n=len(s)
# for i in range(len("instagram")):
#     print(i,"---->",s[i])
    

s="instagram"
n=len(s)
for i in range(len(s)-1,-1,-1):
    print(i,"---->",s[i])
    
print("--"*34)

s="instagram"
n=len(s)
for i in range(len(s)):
    print(8-i,"---->",s[8-i])
    