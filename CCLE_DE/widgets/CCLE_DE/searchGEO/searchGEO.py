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

class OWsearchGEO(OWBwBWidget):
    name = "searchGEO"
    description = "Search GEO databank for datasets to download"
    priority = 0
    icon = getIconName(__file__,"search_icon.png")
    want_main_area = False
    docker_image_name = "biodepot/searchgeo"
    docker_image_tag = "latest"
    inputs = [("trigger",str,"handleInputstrigger")]
    outputs = [("directory",str),("list",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    searchTerm=pset(['CCLE'])
    directory=pset("/data")
    authors=pset([])
    datasetType=pset([])
    desc=pset([])
    numProbes=pset(None)
    numSamples=pset(None)
    organsim=pset([])
    geoAccession=pset([])
    meshTerms=pset([])
    platformTech=pset([])
    project=pset([])
    pubDate=pset([])
    relSeries=pset(None)
    relPlatform=pset([])
    reporterID=pset([])
    sampleSource=pset([])
    sampleType=pset([])
    sampleValType=pset([])
    subInst=pset([])
    subsetDesc=pset([])
    subsetVarType=pset([])
    suppFiles=pset([])
    tagLen=pset([])
    title=pset([])
    updateDate=pset([])
    list=pset("AccessionIDs.txt")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"searchGEO")) as f:
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
        outputValue="/data"
        if hasattr(self,"directory"):
            outputValue=getattr(self,"directory")
        self.send("directory", outputValue)
        outputValue=None
        if hasattr(self,"list"):
            outputValue=getattr(self,"list")
        self.send("list", outputValue)
