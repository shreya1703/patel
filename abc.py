#1
print "Hello World"
print 'single line' "#"
print """multiline(---------)"""

#2
print "------Datatypes-----"
a=16 #Int Datatype
a1="abc" #String Datatype
c=10
d=20
b=123.23 #Float Datatype
e=c+d #Expression
c=2.3+3.2j #Complex Datatype

#3
print "----Expression-----"
e=c+d
e1=d-c
print "Sum is",e
print "Subtraction is",e1

#4
f=float(a)
print "int to float",f
h=oct(d)
print "decimal to octal",h
m=bin(d)
print "decimal to binary",m
n=hex(d)
print "decimal to hex",n
print"i/o"
name=raw_input("Enter your name\n")
print"Name:",name
age=input("Enter your age\n")
print"Age:",age
