import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWbonferroni(OWBwBWidget):
    name = "bonferroni"
    description = "Calculate bonferroni correction to find genes differentially expressed"
    priority = 2
    icon = getIconName(__file__,"calculator_icon.png")
    want_main_area = False
    docker_image_name = "biodepot/bonferroni"
    docker_image_tag = "latest"
    inputs = [("trigger",str,"handleInputstrigger")]
    outputs = [("file",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    outputDir=pset("/data/GEO_DL")
    alphaLevel=pset(0.05)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"bonferroni")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputstrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("trigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue="/data/GEO_DL/results.csv"
        if hasattr(self,"file"):
            outputValue=getattr(self,"file")
        self.send("file", outputValue)
