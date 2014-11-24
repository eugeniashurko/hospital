__author__ = 'Саша'

import HMS.HMS.Controller as Controller

class EventDispatcher:

    def __init__(self):
        self.controllerContainer = []


    def addController(self, controller):
        pass

    def removeController(self, controller):
        pass


    def processEvent(self, event):
        flag = False
        for c in self.controllerContainer:
            if (c.processEvent(event)):
                flag = True
                break
        return flag
