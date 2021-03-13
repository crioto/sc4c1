# Types

def agecheck(age):
    if age < 18:
        print("Вам еще рано сюда")
    else:
        print("Добро пожаловать")

print("Введите ваш возраст")
input1 = input()
agecheck(int(input1))

# Normal functions

def myfunc():
    print("This is my function")

# Functions with arguments
def myfunc2(myword):
    print("This is an argument: " + myword)

def myfunc3(myword1, myword2):
    print("First argument: " + myword1)
    print("Second argument: " + myword2)

# Functions with return values
def myfunc4():
    return "This is so cool"

def myfunc5(x, y, z):
    result = x * y * z
    return str(result)

# Working code
print("The result is " + myfunc5(10, 10, 10))
print("The result is " + myfunc5(20, 20, 20))
print("The result is " + myfunc5(30, 30, 30))
print("The result is " + myfunc5(40, 40, 40))


