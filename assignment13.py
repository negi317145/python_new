
#Q.1 Name and handle the exception occured in the following program: 
try:
 a=3
 if a<4:
    a=a/(a-3)
    print(a)
except Exception:
      print("hello excception occured")



#Q.2- Name and handle the exception occurred in the following program: 

l=[1,2,3]
try:
  print(l[3])
except Exception as e:
  print("exception occurred")
  print(e)


#Q.3-What will be the output of the following code:
#try:
    #raise NameError("Hi there")  # Raise Error
#except NameError:
    #print ("An exception")
    #raise # To determine whether the exception was raised or not

#output:
    #raise NameError("Hi there") #Raise Error
#NameError: Hi there


#Q.4-To determine whether the exception was raised or not


# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output
#-5.0
#a/b result in 0


#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error
#2. Value Error
#3. Index Error

#1.import Error
try:
    import messi
except Exception as e:
    print(e)

#2.Value Error
try:
    val=int("himanshu")
except Exception as e:
    print(e)

#3.Index Error
try:
    list=[1,2,3]
    print(list[12])
except Exception as e:
    print(e)



#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. 
     #The code must keep taking input till the user enters the appropriate age number(less than 18). 
import time
class AgeTooSmallError(Exception):
 pass
while True:
  try:
   print("enter age\n")
   age=int(input())
   if(age<19):
    raise AgeTooSmallError("age is below 18")
   break

  except Exception as e:
     print(e)
     print("age is above 18")