def maxDominos(m,n):
    product = m*n 
    
    return product//2
    
    
m, n = list(map(int, input().split()))
 
print(maxDominos(m, n))