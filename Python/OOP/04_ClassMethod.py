# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:17:19 2022

@author: Krystian
"""


class Student:
    
    listStudents = []
    
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.listStudents.append(self)
    
    @classmethod    
    def countStudents(cls):
        print('Number of students:', len(Student.listStudents))
 
              
# %%
student1 = Student('Jan', 'Kowalski', 18)
student2 = Student('Artur', 'Czesak', 23)
student3 = Student('Kamil', 'Betkowski', 22)

# %%

Student.countStudents()