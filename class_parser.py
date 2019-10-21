# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:00:04 2019

@author: hp
"""
from class_info import ClassInfo
import os
from pprint import pprint
class ClassParser:
    def __init__(self, path):
        self.path = path
        self.classes = []
        self.classNames = []
        self.totalAttributes = 0
        self.totalMethods = 0
        self.publicMethods = 0
        self.privateMethods = 0
        self.privateAttributes = 0
        self.publicAttributes = 0
        self.totalInheritedMethods = 0
        self.totalInheritedAttributes = 0
        self.totalOverriddenMethods = 0
        self.totalOverriddenAttributes = 0
        self.totalClasses = 0
    
    def __len_(self):
        return len(self.classes)
    
    def __get_class(self, temp_line):
        replaces = ['class', '(', ')', ':', ',']
        for r in replaces:
            temp_line = temp_line.replace(r, ' ')
        temp_line = temp_line.split()
        self.classNames.append(temp_line[0])
        newClass = ClassInfo(temp_line[0], set(), set(), set())
        self.classes.append(newClass)
        if len(temp_line) > 1:
            for i in range(1, len(temp_line)):
                newClass.parentClasses.add(temp_line[i])
                    
    def parse(self):    
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.py' in file:
                    try:
                        self.__parse(os.path.join(r, file))
                    except Exception:
                        pass
                    
    def __parse(self, file_name):
        print('Parsing file...', file_name)
        f = open(file_name, 'r', encoding = 'utf-8')
        for i, line in enumerate(f):
            try:
                if '#' in line:
                    line = line[0:line.find('#')]
            except Exception:
                pass
            temp_line = line.split()
            if 'class' in temp_line:
                temp_line = ' '.join(temp_line)
                self.__get_class(temp_line)
                        
            elif 'def' in temp_line:
                temp_line = ' '.join(temp_line)                        
                replaces = ['def', '(', ')', ':']
                for r in replaces:
                    
                    temp_line = temp_line.replace(r, ' ')
                
                temp_line = temp_line.split()
                if self.__len_() > 0 and 'self' in temp_line:
                    self.classes[self.__len_() - 1].methods.add(temp_line[0])
                    
            elif 'self.' in line and '=' in line:
                temp_line = ' '.join(temp_line)
                temp_line = temp_line.split('=')[0]
                
                temp_line = ''.join(temp_line)
                replaces = [',', '(', ')', ':','[', ']', '{', '}', '|'] 
                for r in replaces:
                    temp_line = temp_line.replace(r, ' ')
                
                
                temp_line = temp_line.split()
                for word in temp_line:
                    if 'self.' in word:
                        temp_word = word.replace('self.', ' ').split()
                        temp_word = ''.join(temp_word)
                        if self.__len_() > 0:
                            self.classes[self.__len_() - 1].attributes.add(temp_word)
                            

    def __get_this_class(self, name):
        for i in self.classes:
            if i.name == name:
                return i
            
    def find_inherited_methods(self):
        temp = self.classNames[0: len(self.classNames)]
        dic = {}
        self.depthOfInheritance = 1
        while len(self.classNames) != len(dic):
            class_name = temp[0]
            temp.pop(0)
            this_class = self.__get_this_class(class_name)
            if len(this_class.parentClasses) == 0:
                dic[this_class.name] = 1
                continue
            parents = this_class.parentClasses
            okay = True
            for i in parents:
                if i in self.classNames:
                    if i not in dic:
                        okay = False
                        break
            if okay == False:
                temp.append(class_name)
                continue
            dic[class_name] = 1
            for i in parents:
                if i not in self.classNames:
                    continue
                parent_class = self.__get_this_class(i)
                dic[class_name] = max(dic[class_name], dic[parent_class.name] + 1)
                self.depthOfInheritance = max(self.depthOfInheritance, dic[class_name])
                this_class.inheritedMethods = this_class.inheritedMethods.union(parent_class.methods)
                this_class.inheritedAttributes =  this_class.inheritedAttributes.union(parent_class.attributes)

    def just_call_this_method(self):
        self.parse()
        try:
            self.find_inherited_methods()
        except Exception:
            pass
        for i in self.classes:
            i.precalc()
        self.__store_info()    
    def __store_info(self):
        for per_class in self.classes:
            self.totalAttributes += len(per_class.get_total_attributes())
            self.totalMethods += len(per_class.get_total_methods())
            self.totalInheritedMethods += len(per_class.inheritedMethods)
            self.totalInheritedAttributes += len(per_class.inheritedAttributes)
            self.totalOverriddenMethods += len(per_class.get_overridden_methods())
            self.totalOverriddenAttributes += len(per_class.get_overridden_attributes())
            self.publicMethods += len(per_class.publicMethods)
            self.privateMethods += len(per_class.privateMethods)
            self.privateAttributes += len(per_class.privateAttributes)
            self.publicAttributes += len(per_class.publicAttributes)
            self.totalClasses += 1
    
    def print_all_class_info(self):
        for i in self.classes:
            pprint(vars(i))
folder_path = 'E:\\Spyder\\pp\\Software-Metrics\\test'                           
cp = ClassParser(folder_path)
cp.just_call_this_method()
pprint(vars(cp))


