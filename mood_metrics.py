# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:58:57 2019

@author: hp
"""

from class_parser import ClassParser

class MoodMetrics:
    def __init__(self, folder_path):
        self.project = ClassParser(folder_path)
        self.project.just_call_this_method()
        
    def mhf(self): #method hiding factor
        return 1 - self.project.publicMethods/(min(1, self.project.totalClasses - 1))/self.project.totalMethods
    
    def ahf(self): #attribute hiding factor
        return 1 - self.project.publicAttributes/(min(1, self.project.totalClasses - 1))/self.project.totalAttributes
    
    def mif(self): #method inheritance factor
        return self.project.totalInheritedMethods/self.project.totalMethods
    
    def aif(self): #attribute inheritance factor
        return self.project.totalInheritedAttributes/self.project.totalAttributes
    
    def pf(self): #polymorphism Factor
        return self.project.totalOverriddenMethods/self.project.totalInheritedMethods
    
    def get_mood_metrics(self):
        print('MHF: ', round(self.mhf(), 2))
        print('AHF: ', round(self.ahf(), 2))
        print('MIF: ', round(self.mif(), 2))
        print('AIF: ', round(self.aif(), 2))
        print('PF: ', round(self.pf(), 2))

folder_path = 'E:\\Spyder\\pp\\Software-Metrics\\test' 
folder_path = 'E:\\Spyder\\pp\\catapult-master'      
temp = MoodMetrics(folder_path)
temp.get_mood_metrics()
print(temp.project.classes)
