from functools import reduce

x=map(lambda x:x*2,range(5))
f = lambda a,b: a if (a > b) else b
print (reduce(f, [47,11,42,102,13]))
def sum(a,b):
    return a+b
a= reduce(sum,range(10))
print (a)
def Counter(max):
    counter=0

    while(counter<max):
        yield counter
        counter+=1
    return

def  secMax(arr):
    if len(arr)<2 :
        raise ValueError
    maxNux=arr[1] if arr[1] >arr[0] else arr[0]
    secMax= arr[1] if arr[1] <=arr[0] else arr[0]
    for idx in range(2,len(arr)):
        if arr[idx] >= maxNux:
            maxNux,secMax = arr[idx],maxNux
        elif arr[idx]> secMax:
            secMax=arr[idx]
    return secMax


def p2(num):
    ans=1
    counter=0
    while (True):
        if counter<num:
            yield ans
            ans*=2
            counter+=1
            continue
        return
def closeProdact2(num):
    if num==0:
        raise ValueError
    p2=1
    prevp2=1
    while (num>p2):
        prevp2,p2 =p2,p2*2
    if num==p2:
        return p2
    else:
        return prevp2



if __name__=="__main__":
   # for num in Counter(19):
    #    print(num)
    for num in p2(10):
       print (num)

    print(secMax([1,2]))
    print (secMax(range(10)))
    print (secMax([1 ,1 ,2 ,2 ,2 ,3 ,3 ,3 ]))
    print (secMax([3,3,3,3,3,3]))
    print (secMax([-17,20,30,48,39,37]))
    print (closeProdact2(1026))
