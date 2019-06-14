#https://stackoverflow.com/questions/23153319/n-ary-tree-in-python
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
