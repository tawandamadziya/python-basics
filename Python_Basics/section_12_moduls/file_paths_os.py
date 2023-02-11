import time
import os
import pandas

while True:
    if os.path.exists("list.py\pemps_today.csv"):
        data= pandas.read_csv("list.py\pemps_today.csv")
        print(data.mean()["st2"])
    else:
        print("File does not exist") 
    time.sleep(10)           
