# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:26:43 2018

@author: mosee
"""

from datetime import datetime

class Seance(object):

    def __init__(self, newDate=datetime.today(), newAssistants = []):
        super().__init__()
        self.date = newDate
        self.assistants = newAssistants

    def setDate(self, newDate):
        if type(newDate) is datetime:
            self.date = newDate
        else:
            raise TypeError("newDate should a 'datetime' object !!")
        
    def getDate(self):
        return(self.date)

    def addAssistant(self, newAssistant):
        if type(newAssistant) is str:
            self.assistants.append(newAssistant)
        else:
            raise TypeError("newAssistant should be a string !!")

    def removeAssistant(self, oldAssistant):
        if type(oldAssistant) is str:
            self.assistants.remove(oldAssistant)
        else:
            raise TypeError('oldAssistant should be a string !!')

    def getAssistants(self):
        return(self.assistants)



if __name__ == '__main__':
    test = Seance()
    test.setDate(datetime.today())