# def formatter(text):
    # return "******\n" + text + "\n******"

# def printwithformatter(formattingfunction, text):
    # print(formattingfunction(text))

# printwithformatter(formatter, "hello")



from functools import partial
def sumof(a,b):
    return(a + b)

print(sumof(1,2))

plustwo=partial(sumof,2)
print(plustwo(1))
