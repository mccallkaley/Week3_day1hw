#group derek together then hawinks in a group print first group which is hawkins second
import re

with open('files/names.txt') as file:
    data = file.read()
  
    print("=================")
    print("Full Name/Twitter")
    print("=================")
    pattern = re.compile("([A-Z][a-z]+)\, ([A-Z][A-Za-z]+[\W]*)") 
#char in range A-Z,a-z,+(one or more of) \, char in range A-Z, in range 

    pattern2 = re.compile("\@[\w]+")
    found = pattern.findall(data)
    found2 = pattern2.findall(data)
  #  print(found)
   # print(found2)
    for name in found:
        for email in found2:
            if (name[1].lower() in email):
                print(f"{name[1]} {name[0]} / {email}")
            elif (name[0].lower() in email):
                print(f"{name[1]} {name[0]} / {email}")
            