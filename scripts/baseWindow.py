from maya import cmds
import random


class Window(object):
    def __init__(self, name):
        if cmds.window(name, query=True, exists=True):
            cmds.deleteUI(name)

        cmds.window(name)
        self.buildUI()
        cmds.showWindow()

    def buildUI(self):
        print "No UI is defined"