def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
make_multiplier_of_2= make_multiplier_of(2)
make_multiplier_of_3= make_multiplier_of(3)
print (make_multiplier_of_2(4))
print (make_multiplier_of_3(4))

