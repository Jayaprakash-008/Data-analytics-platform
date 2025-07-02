def perimeter( radius, height,variable=2,pi=3.14):
    ans = variable * pi * radius * height
    return ans


def area_of_circle(radius1, radius2,pi=3.14):
    ans = pi * radius1 * radius2
    return ans


def addition(num1,num2,num3):
    ans = num1+num2+num3
    return ans

#defining a formula pi*r*h
def formula1 (radius, height, pi=3.14):
    ans = pi*radius*height
    return ans
formula = formula1(10,20)
print(formula)

#defining a formula 2*pi*r*r
def formula2 (variable,radius1,radius2,pi=3.14 ):
    ans = variable*pi*radius1*radius2
    return ans
formula = formula2(2,10,20)
print(formula)

#defining a formula l*b
def formula3 (length,breadth):
    ans = length * breadth
    return ans
formula = formula3(10,20)
print(formula)

def formula3 (length=10,breadth=20):
    ans = length * breadth
    return ans
formula = formula3()
print(formula)







