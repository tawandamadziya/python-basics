#def foo(temp_areture):
 #   if temp_areture>25:
  #      return "Hot"
   # elif temp_areture>=15 and temp_areture<=25:
    #    return "Warm"
   # elif temp_areture>15:
   #     return "Cold"

#user_input=float(input("Enter tempareture:"))
#print(foo(user_input))    
def foo(name):
    return "Hi %s" % (name).upper()
sname=str(input("Enter name:"))    
print(foo(sname))