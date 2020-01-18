"add  new discription"
def twice(x):
    return 2*x
def printHello():
     return ("hello")

def fibielemReq(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibielemReq(num - 1) + fibielemReq(num - 2)


if __name__=="__main__":
    print (fibielemReq(1))
    print (fibielemReq(2))
    print (fibielemReq(3))






