from maya import cmds
import random

def createObjects(mode, numObjects):
    """This creates objects. Supports Cubes, Spheres, Cones, and Cylinder."""
    objList = []

    for n in range(numObjects):
        if mode == 'Cube':
            obj = cmds.polyCube()
        elif mode == 'Sphere':
            obj = cmds.polySphere()
        elif mode == 'Cone':
            obj = cmds.polyCone()
        elif mode == 'Cylinder':
            obj = cmds.polyCylinder()
        else:
            obj.error("I don't know what to create!")
        
        objList.append(obj[0])

    cmds.select(objList)


def randomize(objList=None, minValue=0, maxValue=10, axes='xyz', mode='Absolute'):
    if objList is None:
        objList = cmds.ls(selection=True)

    for obj in objList:
        for axis in axes:
            current = 0
            if mode == 'Relative':
                current = cmds.getAttr(obj + '.t%s' % axis)

            val = current + random.uniform(minValue, maxValue)
            cmds.setAttr(obj + '.t%s' % axis, val)


def showWindow():
    name = "Randomizer Window"
    if cmds.window(name, query=True, exists=True):
        cmds.deleteUI(name)

    cmds.window(name)
    cmds.showWindow()

    column = cmds.columnLayout()
    cmds.frameLayout(label = "Choose an object type")

    cmds.columnLayout()
    cmds.radioCollection("objectCreationType")
    cmds.radioButton(label = "Cube", select = True)
    cmds.radioButton(label = "Sphere")
    cmds.radioButton(label = "Cone")
    cmds.radioButton(label = "Cylinder")

    cmds.intField("numObjects" , value = 5)

    cmds.setParent(column)
    frame = cmds.frameLayout("Choose your max range")

    cmds.gridLayout(numberOfColumns = 2, cellWidth = 100)

    for axis in 'xyz':
        cmds.text(label = '%s axis' % axis)
        cmds.floatField('%sAxisField' % axis, value = random.uniform(0, 10))
    
    cmds.setParent(frame)
    cmds.rowLayout(numberOfColumns = 2)

    cmds.radioCollection("randomMode")
    cmds.radioButton(label = "Absolute", select = True)
    cmds.radioButton(label = "Relative")

    cmds.setParent(column)
    cmds.rowLayout(numberOfColumns = 2)
    cmds.button(label = "Create", command = onCreateClick)
    cmds.button(label = "Randomize", command = onRandomClick)


def onCreateClick(*args):
    print "Create button clicked"
    radio = cmds.radioCollection("objectCreationType", query=True, select=True)
    mode = cmds.radioButton(radio, query=True, label=True)

    numObjects = cmds.intField("numObjects", query=True, value=True)

    print mode, numObjects

    createObjects(mode, numObjects)
    onRandomClick()

def onRandomClick(*args):
    print "Randomize button clicked"
    radio = cmds.radioCollection("randomMode", query=True, select=True)
    mode = cmds.radioButton(radio, query=True, label=True)

    for axis in 'xyz':
        val = cmds.floatField("%sAxisField" % axis, query=True, value=True)
        randomize(minValue=val*-1, maxValue=val, mode=mode, axes=axis)