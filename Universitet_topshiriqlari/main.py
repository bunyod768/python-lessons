import math
# matematik ifodalar
x,y,z = 0.0374,-0.825,16
v= (1+math.pow(math.sin(x+y),2))*math.pow(x,math.fabs(y)) /math.fabs((x-(2*y))/(1+math.pow(x*y,2))) + math.pow(math.cos(math.atan(1/z)),2)
v=format(v,'.4f')
print(v)
