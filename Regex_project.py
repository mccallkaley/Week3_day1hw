"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""
#  ([A-Z][a-z]+) 1st capuring group Capital char followed by lower  
#  + matches the previous token between one and unlimited times, as many times as possible, giving back as needed (greedy
# ([A-Z][a-z]*) 2nd group matches the previous token between zero and unlimited times, as many times as possible, 
# giving back as neede
# \s matches any whitespace character 
# * matches the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)

import re

with open("files/regex-test.txt") as file:
    
    data = file.readlines()
    
    pattern2 = re.compile("([A-Z][a-z]+) ([A-Z][a-z]*)*\s*([A-Z][a-z]+)")
    
    for line in data:
        matches = pattern2.match(line)
        if matches:
            print(line)
        else:
            print("None")