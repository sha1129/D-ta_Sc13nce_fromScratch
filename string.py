# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:45:19 2020

@author: turjo
"""

"""
String 
"""

#sttring can have single or doubles qutoes

#multi line string
multi_line_string = """you have seen this before
dfsfs
"""

#f string 
fname = "Shanshan"
lname = "lao"

full_name= f"{fname} {lname}"

#try and except
try:
    print(0/0)
except ZeroDivisionError:
    print("cant divide by 0")
finally:
    print ("go fuck yourself")