import time
while True:
    with open("list.py\peoples_names.txt") as file:
        print(file.read())
        time.sleep(10)