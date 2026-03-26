#
user_input = input("Expression: ")

x, y, z = user_input.split(" ")
#


float(x)
float(z)

if y == "+":
    print(float(format(int(x)+int(z))))

if y == "-":
    print(float(format(int(x)-int(z))))

if y == "/":
    print(float(format(int(x)/int(z))))

if y == "*":
    print(float(format(int(x)*int(z))))
