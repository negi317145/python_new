#Q.1- Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com"
#"jeff42@amazon.com"

import re
a= "zuck26@facebook.com"
b= "page33@google.com"
c="jeff42@amazon.com"
p=re.compile(r"([a-zA-z0-9._]+)@([a-z]+)\.([a-z]+)")
def abc(sep):
  result=p.match(sep)
	
  print(result[1])
  print(result[2])
  print(result[3])
abc(a)
abc(b)
abc(c)
result=p.search(a)
result=p.search(b)
result=p.search(c)

print("****************************************************************************************************************")
     

#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
line = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p=re.compile(r"B[a-zA-z]+")
p1=re.compile(r"b[a-zA-z]+")

result=p.finditer(line)
res=p1.finditer(line)
for r in result:
   print(r)
for i in res:
   print(i)
	
print("****************************************************************************************************************")
     
#Q.3- Split the following irregular sentence into words
	 
n = "A, very very; irregular_sentence"
p=re.compile(r'[^a-zA]+')
print(p.sub(' ',n))