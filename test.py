from simpy import*
var('a b c')
L=limit(((a**x+b**x+c**x)/3)**(1/x),x,0)
print(L)
display(L)
