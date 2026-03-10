student_mark=[88,89,92,93,77,78,78,55,69,62,77,44,97,83,43,42,75,77]
even=[]
odd=[]
for i in student_mark:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even marks:",even)
print("Odd marks:",odd)

'''
Even marks: [88, 92, 78, 78, 62, 44, 42]
Odd marks: [89, 93, 77, 55, 69, 77, 97, 83, 43, 75, 77]'''
