import math
def function(a,b,c):
    
    determinant = ((b*b) - 4*(a*c))
    if determinant < 0:
        print("Solution 1 : ",-b, "-iV(",-determinant,")/",2*a) 
        print("Solution 2 : ",-b,"+iV(",-determinant,")/",2*a)
    elif determinant == 0:
        solution = ((-b)/(2*a))
        print('La seule solution est:', solution)
    elif determinant >=1:
        solution1 = (((-b)-(math.sqrt(determinant)))/(2*a))
        solution2 = (((-b)+(math.sqrt(determinant)))/(2*a))
        print('La solution 1 est: ',solution1,' et la solution 2 est: ',solution2)
    
a= input("a = ")
b= input("b = ")
c= input("c = ")

a = int(a)
b = int(b)
c = int(c)


function(a, b, c)