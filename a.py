class NestedIterator(object):
    
    def __init__(self, nestedList):
        self.my_list = []
        self.index = 0
        for i in nestedList:
            if i.isInteger() == True:
                self.my_list.append(i.getInteger())
            else:
                self.read_list(i.getList())
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
    def read_list(self,l):
        for i in l:
            if i.isInteger() == True:
                self.my_list.append(i.getInteger())
            else:
                self.read_list(i.getList())
    

    def next(self):
        """
        :rtype: int
        """
        re = self.my_list[self.index]
        self.index += 1
        return re
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index == len(self.my_list):
            return False
        return True
