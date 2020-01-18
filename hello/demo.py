"add  new discription"


def twice(x):
    return 2 * x


def printHello():
    return ("hello")


def fibielemReq(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibielemReq(num - 1) + fibielemReq(num - 2)


def fibieSerial(size):
    fibiSerial = []
    for elem in range(size):
        fibiSerial.append(fibielemReq(elem))
        print (elem)
    return fibiSerial


if __name__ == "__main__":
    print(fibieSerial(10))
