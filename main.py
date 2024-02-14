with open("demo1.txt", mode="a") as file:
    file.write("This was appended with python")

import datetime

current_date = datetime.datetime.now()
print(current_date)
