#def mean_f(*args): #args(argument(s)) is used as a name better to read code
#    return sum(*args) / len(*args)

#my_func=(3, 6, 8, 9, 7, 5)
#print(mean_f(my_func))   


#another way 
#def mean_f(*args): 
#    return sum(args) / len(args)
#print(mean_f(10, 5, 9, 8, 2, 3))    

#list 
def foo(*args): 
    return sorted(i.upper() for i in args)
print(foo("John", "Amy", "Jerif"))    