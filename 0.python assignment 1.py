# strings  

string1="Hello"
string2=input("enter your name :")
result=string1+" "+ string2
print(result)

string3=", Welcome to Python Programming"
result=(result+string3)
print(result)

#string slicing

string="Hello Zara ,Welcome to Python Programming"
print(string[0])       
print(string[-1])      
print(string[:5])      
print(string[-11:])  
print(string[::-1])    
print(string[23:29])   

#string methods

strM="Python beginner tutorial"
print(strM.upper())
print(strM.lower())
print(strM.capitalize())
print(strM.count('t'))
print(strM.replace("Python","Machine Learning"))

#tuples

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t_combine = t1 + t2
print(t_combine)
print(t_combine * 3)
print(t_combine[2])
print(t_combine[:3])
print(t_combine[-3:])