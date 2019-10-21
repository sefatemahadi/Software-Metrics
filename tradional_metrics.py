# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:06:30 2019

@author: hp
"""
import os
class LOC:
    def __init__(self, path):
        self.path = path
    
    def loc(self):
        self.lines = 0
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.py' in file:
                    print('Now reading..', os.path.join(r, file))
                    try:
                        f = open(os.path.join(r, file), 'r', encoding = 'utf-8')
                        for line in f:
                            try:
                                self.lines += 1
                            except Exception:
                                pass
                    except Exception:
                        pass
                        
folder_path = 'E:\\Spyder\\pp\\catapult-master'      
temp = LOC(folder_path)
temp.loc()
temp.lines

import re
def stripComments(code):
    code = str(code)
    return re.sub(r'(?m)^ *#.*\n?', '', code)

print(stripComments("""#foo bar
'''bar foo'''
# buz"""))

import ast

with open('test//test.py') as f:
    print(ast.parse(f.read()))