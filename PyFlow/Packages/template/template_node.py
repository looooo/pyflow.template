from PyFlow.Core import NodeBase


class templateNode(NodeBase):
    def __init__(self, name):
        super(templateNode, self).__init__(name)

    @staticmethod
    def category():
        return 'template'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'A simple template node.'
