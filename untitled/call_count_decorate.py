import functools
import time
class callCount:
    def __init__(self,f):
        self.f=f
        self.count=0
    def __call__(self, *args, **kwargs):
        self.count+=1
        if self.count<10:
            return self.f( *args, **kwargs)
        else:
            print ("stop")

def printTime(func):
    @functools.wraps(func)  # make the __name__   and __doc__ get the data of the source and not the decorate function
    def warrper(*args, **kwargs):
        print("running func {} at {}".format(func.__name__,time.asctime()))
        return func(*args, **kwargs)
    return warrper
def doTwice(func):
    def doTwiceWrapper(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args, **kwargs)
    return doTwiceWrapper

@callCount
def hello(name):
    print("Hello , {}".format(name))


for _ in range (10):
    hello("shira")
@printTime
@doTwice
def hi(name):
    print("hi , {}".format(name))

hi("benny")
hi("david")



