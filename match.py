import re
txt = "use of python in machine learning "
x= re.search("^use.*learning$",txt)
if(x):
    print("YES! We have a match!")
else:
    print("No match")