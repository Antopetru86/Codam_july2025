#!/usr/bin/env python3
import sys
import re

parameter = sys.argv[1:] #slice out file's name

if len(parameter)!=2:
    print("none")
else: 
    key = parameter[0] #to define the keyword
    text= parameter[1] #define text in which keyword is looked for
    matchword = re.findall(key,text)  #key = pattern #text
    if len(matchword)==0:
        print("none")
    else:
        print(len(matchword))     
 