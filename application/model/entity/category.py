class Category:
    def __init__(self, name, id, description):
        self._id = id
        self._name = name
        self._description = description

    def setId(self, id):
        self._id = id

    def getDescription(self, description):
        return self._description

    def getName(self, name):
        return self._name
