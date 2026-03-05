'''1. Access First-Level Elements

2. What is the output of list2[0] and list2[3]?

3. Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.

4. Retrieve 60, 80, and 90 from the nested list using indexing.
 		
5. What is the output of list2[4][1]?
		
6. Write a statement to access the element 336.
		
7. The last element (336).
			 
8. The second-to-last sub-list ([112, 114, 116]).
							
9. Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
			
10. Retrieve the element 116 from the list [112, 114, 116].

11. Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
		
12.	Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].	

13.	Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
			
14.	Write a slice to reverse the entire list2.	

15.	Reverse the list [112, 114, 116].

16.	Write a slice to get [60, 80, 90].

17.	From the main list, extract [10, 30, [112, 114, 116]] using slicing.

18.	Slice to extract [221, 226, 336] from the main list.

19.	Write a slice to extract [40, 50, [60, 80, 90]].

20.	Write a slice to get [10, 30, [112, 114, 116], 226].

'''

l1 = [10, 20, 30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116], 221, 226, 336]
print(l1)

#1 Access First-Level Elements
print(l1[0:3])

#2 What is the output of list2[0] and list2[3]?
print(l1[0])
print(l1[3])

#3 Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.
print(l1[3])

#4 Retrieve 60, 80, and 90 from the nested list using indexing.
print(l1[3][2])

#5 What is the output of list2[4][1]?
print([l1[4][1]])

#6 Write a statement to access the element 336.
print(l1[-1])

#7 The last element (336).
print(l1[7])

#8 The second-to-last sub-list ([112, 114, 116]).
print(l1[-4])

#9 Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(l1[3][4])

#10 Retrieve the element 116 from the list [112, 114, 116].
print(l1[4][2])

#11 Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
print(l1[3][0])

#12 Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].
print(l1[2:4])

#13 Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
print(l1[3][3:])

#14 Write a slice to reverse the entire list2.
# a=l1
# a.reverse()
# print(a)

#15 Reverse the list [112, 114, 116].
print(l1[-4][::-1])

#16 Write a slice to get [60, 80, 90].
print(l1[3][2][0::])

#17 From the main list, extract [10, 30, [112, 114, 116]] using slicing.
print(l1[:5:2])

#18 Slice to extract [221, 226, 336] from the main list.
print(l1[5::])

#19 Write a slice to extract [40, 50, [60, 80, 90]].
print(l1[3][0:3])

#20 Write a slice to get [10, 30, [112, 114, 116], 226].
print(l1[0:8:2])

# 1.Create an empty list and use append() to add five different numbers to it. Print the final list.
l2=[]
l2.append(45)
l2.append(74)
l2.append(89)
l2.append(36)
l2.append(52)
print(l2)

# 2. Create a list of student name  and append a new Student name  and print the length of list .
stu_list=[]
stu_list.append("sahil")
print(len(stu_list))

# 3. Append a list [10, 20, 30] to another list and observe the result.
l3=[]
l3.append([10, 20, 30] )
print(l3)

# 4. Create a list and make a copy using copy().
l4=[20,30,50,40]
l5=l4.copy()
print("befor: " ,l4)
print("after: ",l5)

# 5. Create a list with at least 10 elements, use clear(), and check the length of the list afterward.
l6=[10,20,56,41,52,36,52,78,53,41]
print(l6)
l6.clear()
print(l6)

# 6. Create a nested list and clear only the inner list while keeping the outer list intact .
l7=[10,20,30,[45,69,52,36,12],40,60,70]
print(l7)
l7[3].clear()
print(l7)
# 7. Given nums = [1, 2, 3, 4, 2, 2, 5, 2], find how many times 2 appears in the list.

# 8. Create a list of words and find how many times a particular word appears.

# 9. Create two lists, list1 in integer variable  and list2 in String variable. Use extend() to add elements of list2 to list1.     
#    Print the final result.

# 10. Given fruits = ['apple', 'banana', 'cherry', 'banana', 'grape'], find the index of banana.

# 11. Insert the number 100 at the beginning of the list [10, 20, 30].

# 12. Insert 'Python' at index 2 in a list of programming languages and print the result.

# 13. Given numbers = [5, 10, 15, 20, 25], remove and print the last element using pop().

# 14. Remove an element at index 2 and print both the removed element and the updated list.

# 15. Given colors = ['red', 'blue', 'green', 'blue', 'yellow'], remove the first occurrence of 'blue'.

# 16. Reverse the list [1, 4, 9, 16, 25] and print the result.

# 17. Reverse a list of words and join them to form a sentence words = ["Hello", "world", "Python"].

# 18. Sort a list of numbers [10, 5, 8, 3, 1] in ascending and then in descending order.
