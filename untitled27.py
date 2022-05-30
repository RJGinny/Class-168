#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:18:26 2022

@author: riddhiekajain
"""

class Citizen:
    def __init__(self, name, age, dob, id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id =id_number
        
    def add_citizen(self):
            print("Name: "+self.citizen_name)
            print("Age: "+str(self.citizen_age))
            print("Date of Birth: "+self.citizen_dob)
            print("Citizen Id: "+self.citizen_id)
            print("Citizen Added")
            
citizen1 = Citizen("Peter",8, "19th october 2012", "0198")
citizen1.add_citizen()

citizen2 = Citizen("Sophia",10, "19th october 2010", "0178")
citizen2.add_citizen()
