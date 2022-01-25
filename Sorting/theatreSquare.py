import math
def theatreSquare(m,n,a):
    to_the_right = math.ceil(n / a)
    to_the_left = math.ceil(m / a)

    return (to_the_right * to_the_left)

 


print(theatreSquare(2,1,1))  