# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:59:34 2019

@author: hp
"""

class ClassInfo:
    def __init__(self, className = '', methods = set(), attributes = set(), parentClasses = set()):
        self.name = className
        self.methods = methods
        self.attributes = attributes
        self.parentClasses = parentClasses
        self.inheritedMethods = set()
        self.inheritedAttributes = set()
        self.__refresh()
        
    def __refresh(self):
        self.publicMethods = set()
        self.privateMethods = set()
        self.privateAttributes = set()
        self.publicAttributes = set()
    
    def precalc(self):
        self.__refresh()
        for method in self.get_total_methods():
            if method[0] == '_':
                self.privateMethods.add(method)
            else:
                self.publicMethods.add(method)
        for attribute in self.get_total_attributes():
            if attribute[0] == '_':
                self.privateAttributes.add(attribute)
            else:
                self.publicAttributes.add(attribute)
                
    def get_overridden_methods(self):
        return self.methods.intersection(self.inheritedMethods)
    
    def get_overridden_attributes(self):
        return self.attributes.intersection(self.inheritedAttributes) 
    
    def get_total_methods(self):
        return self.methods.union(self.inheritedMethods)
    
    def get_total_attributes(self):
        return self.attributes.union(self.inheritedAttributes)
