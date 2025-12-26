
def moneyback(arr, n):
    c30= c60=c120=0

    for i in range(n):
        if arr[n] == 30:
            c30+=1
        elif arr[n]==60:
            if c30>0:
                c30-=1
                c60+=1
            else:
                return -1
        elif arr[n]==120:
            if c30>=3:
                c30-=3
                c120+=1
            else:
                if c30>0 and c60>0:
                    c30-=1
                    c60-=1
                    c120+=1
                else:
                    return -1
        else:
            return 1




print(moneyback([30,60,120], 3))