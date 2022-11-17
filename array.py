#importing the array module for use
import array 

#another way of importing array module with an alias of arr 
#-import array as arr 
#import all from array module 
#-import array import * 

#create array using array method specified for integers 'i'
#the first array is the module, the second is the constructor 
#'i' is the type code for the type of elements the array will hold 
a = array.array("i",[1,2,3,4,5,6])

print("Array a: ", a)

#accessing elements 
#print element at array index  
print("Value at index 2 of array a: ", a[2])
#print using negative index values
print("Value at negative index 2 of array a: ", a[-2], "\n")

#array operations len(), append(), extend(), insert(), pop(), remove(), concatenate, slicing, 

#array with a decimal type code 
b = array.array ('d',[1.1,2.1,3.1])
#print the length of the array 
print("Array b: ", b)
#length of array b 
print("Length of array b: ", len(b), "\n")

#append() add single element at the end of array 
b.append(3.4)
print("Array b appended: ", b)

#extend() add more than one element at the end of an array 
b.extend([4.5,3.6,7.2])
print("Array b extended: ", b) 

#insert() add element at a specific position or index 
b.insert(2,3.4)
print("Array b inserted: ", b) 
print("Array b with method values added: ", b, "\n")

#"array", list of strings
#you can treat lists as arrays but the data type cannot be specified 
c = ["a","b","c","d","e","f","g"]
print(c)
#removing elements of an array pop(), remove() 

#pop() remove element and return it 
#pop last elements and return it
print("Popping the last element of array c: ", c.pop())
#pop 3rd element and return it 
print("Popping the 3rd element of array c: ", c.pop(3))
#remove() remove element without returning it 
c.remove("a")
print("Removing first element: ", c, "\n")

#concatenation or combining array's 
#to concatenate use the + symbol 
d = array.array ("i", [1,2,3,4,5])
e = array.array ("i", [6,7,8,9])
#creating an array f of integer type 
f = array.array("i") 
#concatenating the array's
f = d + e
print("Array d: ", d, "\nArray e: ", e, "\nArray f (Array d+e): ", f, "\n")
#you cannot concatenate array's of different data types 

#slicing an array returns the range specified 
#here we are pulling the range of array f index's 0-3
print ("Slicing array f to return elements 0-3: ", f[0:3])

#negative index slicing which will not include the negative index specified 
print ("Negative index slice 0-(-3): ", f[0:-3])

#you can print a reversed copy of an array using ::-1 but it does not reverse the array itself and 
#uses high memory to do so, so it is not preferred to achieve "reversing" this way 
print ("Reversing array using slice: ", f[::-1])
print("Array f: ", f, "\n")

#looping array's for, while
#for loop
print("For Loop: ")
print("All values of array f: ")
for i in f: 
    print(i)
    
#while loop 
print("\nWhile Loop: ")
#must initialize your iterator, specify the condition, implement iterator

#initialize iterator "temp"
temp = 0 
#the condition 
#while temp variable is less than 5 
while temp < f[5]:
    #print(f[temp])
    print("Iterator: ", temp, "Value: ", f[temp])
    #iterator
    temp=temp+1 #or temp+=1

#while loop using len()
print("\nIterating through an array using len(): ")
templen = 0
while templen < len(f):
    print(f[templen])
    templen+=1






