#Q.1- Create a list with user defined inputs. 
x=input()
y=input()
z=input()
l=[x,y,z]
print(l)

#Q.2- Add the following list to above created list:
#[google’,’apple’,’facebook’,’microsoft’,’tesla’]
x=input()
y=input()
z=input()
l=[x,y,z]
print(l)
l.append(['google’,’apple’,’facebook’,’microsoft’,’tesla’] )
print(l)

#Q.3- Count the number of time an object occurs in a list.
a=5
b=2
c=5
d=5
l=[a,b,c,d]
print(l)
print(l.count(5))
print(l)

#Q.4- create a list with numbers and sort it in ascending order. 
x=4
y=3
z=6
l=[x,y,z]
l.sort()
print(l)

#Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B,
#in ascending order. [List]
a=[1,3,2]
b=[4,5,6]
c=a+b
print(c)
c.sort()
print(c)

#Q.6-Implement a stack and queue using lists.
# stack
s=[]
print(s)
s.append(1)
s.append(2)
s.append(3
s.append(4)
print(s)
s.pop()
print(s)

#OPTIONAL QUESTION
#Q.1- Count even and odd numbers in that list.
l=[3,6,5,8,1,2]
print(l)
e=0
o=0
for x in l:
    if x%2==0:
	    e=e+1
	else:
	    o=o+1
	print(e)
	print(o)
