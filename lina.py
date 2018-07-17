'''
Class for Linear algebra operations
'''
class Matrix():
    def __init__(self, values=[2,2,2,3,3,3], n=2, m=3):
        self.column = m
        self.rows   = n
        self.matrix = [[]]*n
        for row in range(n):
            self.matrix[row]   = values[0:m]
            values[0:m] = []

    def showMat(self):#Matrix in Terminal zeigen können
        for i in range(self.rows):
            find_all(',',str(self.matrix))
            print(self.matrix)
        '''
        Input are two matrices
        '''
