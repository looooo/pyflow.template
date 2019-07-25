from PyFlow.Packages.template.template_node import templateNode
from PyFlow.UI.UIInterfaces import IPackage

_NODES = {
            templateNode.__name__: templateNode
         }



class template(IPackage):
    """Base pyflow package
    """
    def __init__(self):
        super(template, self).__init__()

    @staticmethod
    def GetNodeClasses():
        return _NODES

    @staticmethod
    def GetPinClasses():
        return {}

    @staticmethod
    def GetExporters():
        return {}

    @staticmethod
    def GetFunctionLibraries():
        return {}

    @staticmethod
    def GetToolClasses():
        return {}

    @staticmethod
    def UIPinsFactory():
        return {}

    @staticmethod
    def UINodesFactory():
        return {}

    @staticmethod
    def PinsInputWidgetFactory():
        return {}

    @staticmethod
    def PrefsWidgets():
        return {}
