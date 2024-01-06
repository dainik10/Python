def smart_div(d):
    def division(a,b):
        if type(b)==str:
            return "Second input must be integer"
        else:
            return d(a,b)
    return division
@smart_div
def div(a,b):
    return a/b
a=div(10,2)
print(a)
a=div(10,"abc")
print(a)
