username = ""
while username != "Tawa": #Loop runs as long as username is not "!=" equal to Tawa
   username= input("Enter username: ")

print("Welcome %s" % username)


while True:
    username=input("Enter username: ")
    if username=="Tawa":
        break                      #this breaks while loop when conditions have been met
    else:
        continue                   #this continues the while loop until it is true
