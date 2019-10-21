# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:35:42 2019

@author: hp
"""
#abc
#def
#class info
#
class ClassInfo:
    def __init__(self, className = '', methods = set(), attributes = set(), parentClasses = set()):
        self.name = className
        self.methods = methods
        self.attributes = attributes
        self.parentClasses = parentClasses
        self.inheritedMethods = set()
        self.__refresh()
    
    def __refresh23(self):
        self.publicMethods = set()
        self.privateMethods = set()
        self.privateAttributes = set()
        self.publicAttributes = set()
    
    def precalc(self):
        self.__refresh()
        for method in self.methods:
            if method[0] == '_':
                self.privateMethods.add(method)
            else:
                self.publicMethods.add(method)
        for attribute in self.attributes:
            if method[0] == '_':
                self.privateAttributes.add(attribute)
            else:
                self.publicAttributes.add(attribute)
                
    def inheritedMethods(self, inheritedMethods):
        self.inheritedMethods = inheritedMethods
        

class ClassInfo2(ClassInfo, abc):
    def __init__(self, className = '', methods = set(), attributes = set(), parentClasses = set()):
        self.name = className
        self.methods = methods
        self.attributes = attributes
        self.parentClasses = parentClasses
        self.inheritedMethods = set()
        self.__refresh()
    
                
    def inheritedMethods(self, inheritedMethods):
        self.__inheritedMethods = inheritedMethods
        
        
class class3(ClassInfo2):
    