# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 08:32:15 2018

@author: mosee
"""

from seance import Seance

class Serie(object):

    def __init__(self):
        super().__init__()
        self.sections = []
        self.studentsNb = 0
        self.seances = []
        
    def addSection(self, newSection):
        if type(newSection) is str:
            self.sections.append(newSection)
        else:
            raise TypeError('newSection should be a string !!')
    
    def removeSection(self, oldSection):
        if type(oldSection) is str:
            self.sections.remove(oldSection)
        else:
            raise TypeError('oldSection should be a string !!')
    
    def getSections(self):
        return(self.sections)
        
    def setstudentsNb(self, newNb):
        if type(newNb) is int:
            if newNb >= 0:
                self.studentsNb = newNb
            else:
                raise ValueError('nexNb should be positive !!')
        else:
            raise TypeError('newNb should be a int !!')

    def getStudentsNb(self):
        return(self.setstudentsNb)

    def addSeance(self, newSeance):
        if type(newSeance) is Seance:
            self.seance.append(newSeance)
        else:
            raise TypeError("newSeance should be a 'Seance' object !!!")

    def removeSeance(self, oldSeance):
        if type(oldSeance) is Seance:
            self.seance.remove(oldSeance)
        else:
            raise TypeError("oldSeance should be a 'Seance' object !!!")




if __name__ == '__main__':
    test = Serie()
    print('\nInitial sections :')
    print(test.getSections())
    
    for s in ['EIT', 'EM1', 'EM2']:
        print('\nAdding %s to sections' % s)
        test.addSection(s)
        print('New value of sections : ', test.getSections())
    
    for s in ['EIT', 'EM2']:
        print('\nRemoving %s to sections' % str(s))
        test.removeSection(s)
        print('New value of sections : ', test.getSections())
    
    s = 3
    print('\nTrying to add a int (%i) to sections' % s)
    try:
        test.addSection(s)
    except TypeError:
        print('TypeError catched (as expected)')
        print('value of sections has not changed : ', test.getSections())
    print('\nTrying to remove a int (%i) to sections' % s)
    try:
        test.removeSection(s)
    except TypeError:
        print('TypeError catched (as expected)')
        print('value of sections has not changed : ', test.getSections())
        
    s = 'EM2'
    print('\nTrying to remove %s to sections' % s)
    try:
        test.removeSection(s)
    except ValueError:
        print('ValueError catched (as expected)')
        print('value of sections has not changed : ', test.getSections())
