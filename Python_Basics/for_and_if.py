colors = [11, 34, 98, 43, 45, 54, 54]
for items in colors:
    if items>50:
        print(items)

print(" ")        

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for items in colors:
    if items is int(items):
        print(items)        

print(" ")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for items in colors:
    if items is int(items) and items>50:
        print(items)
