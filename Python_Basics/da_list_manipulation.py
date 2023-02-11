#def foo(da_list):
#    return [i for i in da_list if isinstance(i, int)]

#print(foo([90, "jon", 80, "Can", 9, "orlando"]))    


#def foo(da_list):
#    return [i for i in da_list if i>0]

#print(foo([-5,-3,2,1,5,-9]))    

#def foo(da_list):#My code that doesnt work
#    return [i for i in da_list if not isinstance(i, str) i.replace(i, 0)]

#def foo(da_list):#Solution
#    return [i if not isinstance(i, str) else 0 for i in da_list ]

def foo(da_list):
    return sum([float(i) for i in da_list])

dat_list=["1.2", "2.6", "3.3"]
print(foo(dat_list))    