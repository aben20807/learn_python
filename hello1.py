# div
a = 22
b = 33
print(a / b)  # ans is float
print(a // b) # ans is int

# Object
a = 1
print(id(a))
print(type(id(a)))
print(type(a))
print(type(print(a)))

# condition
integer = 10
if integer > 5:
    print("> 5")
elif integer > 0:
    print("> 0")
else:
    print("else")

# for
for i in range(3):
    print("hello"+str(i)) # int to string

# while
i = 1
sumN = 0;
while(i <= 10):
    sumN += i
    i += 1
print(sumN)

# sum
print(sum(range(1, 11)))

# is
n1 = 1
n2 = 2
if(n1 is not n2):
    print("n1 is not n2")

# in
s = "abcd"
if 'a' in s:
    print("'a' in s")
if 'e' not in s:
    print("'e' not in s")
array = [0, 1, 2]
if (0 in array):
    print("0 in array")

# lambda
f = lambda x: x**x
print(f(2))

g = lambda x, y: x + y
print(g(3, 4))

# del
# except
aa = 1
print(type(aa))
del aa # delete object
try:
    print(type(aa))
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

# raise
try:
    raise NameError
except NameError:
    print("catch NameError")

# complex
c = 1 + 3j
print(c)
print(c.real)
print(c.imag)
