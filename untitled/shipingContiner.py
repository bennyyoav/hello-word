class shipincontainer:
    seiralNumber=1000
    @classmethod
    def get_seiral_number(cls):
        result=cls.seiralNumber
        cls.seiralNumber+=1
        return result

    @classmethod
    def createwithoutItems(cls,ownerCode):
        return cls(ownerCode,context=None)

    @classmethod
    def createWithitems(cls,ownerCode,items):
        return cls(ownerCode, list(items))


    def __init__(self,ownerCode,context):
        self.ownerCode=ownerCode
        self.context=context
        self.seiralNumber=shipincontainer.get_seiral_number()


a= shipincontainer("aa","bb")
b=shipincontainer("aa","bb")
print (b.seiralNumber)
print (shipincontainer.seiralNumber)