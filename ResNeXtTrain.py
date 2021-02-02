from ikomia import dataprocess
import ResNeXtTrain_process as processMod
import ResNeXtTrain_widget as widgetMod


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class ResNeXtTrain(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        return processMod.ResNeXtTrainProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        return widgetMod.ResNeXtTrainWidgetFactory()
