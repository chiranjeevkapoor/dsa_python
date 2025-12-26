def combination(n,r):
    n_fact = 1
    nmin_fact = 1
    r_fact = 1
    for i in range(n,0,-1):
        n_fact*=i
    for i in range(n-r, 0, -1):
        nmin_fact*=i
    for i in range(r,0,-1):
        r_fact *=i
    
    return (n_fact)//(nmin_fact*r_fact)



def ways(n, m, p, e):
    
    pencil = combination(n, p)
    eraser = combination(m, e)

    return pencil*eraser

print(ways(5,3,5,3))





