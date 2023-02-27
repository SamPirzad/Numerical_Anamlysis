from sympy import *

x = symbols("x")
y1 = symbols("y1") 
y2 = symbols("y2")
y3 = symbols("y3")
y = Function("y")(x) 

function = Derivative(Derivative(y,x)) + x*Derivative(y,x) + y - sqrt(1+x)

def solve_equation( x0 , x4 , h):
    eq1 = (y2 - 2*y1 + x0 )/(h)**2 - (y2-x0)/(2*h) + y1 - sqrt(1+0.25)
    eq2 = (y3 - 2*y2 + y1 )/(h)**2 - (y3-y1)/(2*h) + y2 - sqrt(1+0.5)
    eq3 = (x4 - 2*y3 + y2 )/(h)**2 - (x4-y2)/(2*h) + y3 - sqrt(1+0.75)
    
    print(f"if h = {h} the results will be :")
    print(solve([eq1,eq2,eq3],(y1,y2,y3)))

h1 = 0.25
h2 = h1/2
h3 = h2/2
x0 = 20
x4 = 25
solve_equation(x0,x4,h1) 
solve_equation(x0,x4,h2) 
solve_equation(x0,x4,h3) 



